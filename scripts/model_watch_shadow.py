#!/usr/bin/env python3
"""Finite, script-only model-watch shadow. No AI turns or notifications.

launchd calendar entries have no year field. The campaign date guard is therefore
authoritative, including after sleep, reboot, or a future annual calendar match.
"""
from __future__ import annotations

import argparse
from datetime import date, datetime, timedelta, timezone
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import uuid
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent))
import codex_quota
from model_watch_collect import atomic_bytes, encode, strict_json

LABEL = "com.copperdogma.conductor.model-watch-shadow"
ZONE = "America/Edmonton"
FILES = ("scripts/model_watch_shadow.py", "scripts/model_watch_collect.py",
         "scripts/codex_quota.py", "docs/model-watch/collector-sources.json")


def validate_manifest(manifest):
    if (not isinstance(manifest, dict) or manifest.get("version") != 1
            or manifest.get("label") != LABEL or manifest.get("timezone") != ZONE
            or manifest.get("quota_min_remaining_percent") != 20):
        raise ValueError("invalid_campaign")
    start, end = (date.fromisoformat(manifest[key]) for key in ("start_date", "end_date"))
    if end - start != timedelta(days=6):
        raise ValueError("campaign_requires_seven_dates")
    for key, limit in (("hour", 24), ("minute", 60), ("deadline_hour", 24), ("deadline_minute", 60)):
        if type(manifest.get(key)) is not int or not 0 <= manifest[key] < limit:
            raise ValueError("invalid_campaign_time")
    if (manifest["hour"], manifest["minute"]) >= (manifest["deadline_hour"], manifest["deadline_minute"]):
        raise ValueError("invalid_deadline")
    for key in ("python_path", "codex_path"):
        if not isinstance(manifest.get(key), str) or not Path(manifest[key]).is_absolute():
            raise ValueError("executable_must_be_absolute")
    hashes = manifest.get("runtime_sha256")
    if not isinstance(hashes, dict) or set(hashes) != set(FILES):
        raise ValueError("invalid_runtime_manifest")
    for value in hashes.values():
        if not isinstance(value, str) or len(value) != 64 or any(c not in "0123456789abcdef" for c in value):
            raise ValueError("invalid_runtime_hash")
    return start, end


def make_launchagent(root: Path, manifest: dict) -> dict:
    """Pure planner; caller owns file creation, validation and installation."""
    start, end = validate_manifest(manifest)
    if not root.is_absolute():
        raise ValueError("campaign_root_must_be_absolute")
    slots = []
    for offset in range(7):
        day = start + timedelta(days=offset)
        slots.append({"Month": day.month, "Day": day.day,
                      "Hour": manifest["hour"], "Minute": manifest["minute"]})
    expiry = end + timedelta(days=1)
    slots.append({"Month": expiry.month, "Day": expiry.day, "Hour": 0, "Minute": 5})
    return {
        "Label": LABEL,
        "ProgramArguments": [manifest["python_path"], str(root / "runtime/scripts/model_watch_shadow.py"),
                             "tick", "--campaign", str(root)],
        "WorkingDirectory": str(root / "runtime"),
        "EnvironmentVariables": {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "PYTHONDONTWRITEBYTECODE": "1"},
        "StartCalendarInterval": slots, "RunAtLoad": True, "KeepAlive": False,
        "ProcessType": "Background", "ExitTimeOut": 5,
        "StandardOutPath": str(root / "launchd.stdout.log"),
        "StandardErrorPath": str(root / "launchd.stderr.log"),
    }


def host_zone():
    path = str(Path("/etc/localtime").resolve())
    return path.split("/zoneinfo/", 1)[-1] if "/zoneinfo/" in path else "unknown"


def disable_job():
    result = subprocess.run(["/bin/launchctl", "disable", f"gui/{os.getuid()}/{LABEL}"],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
    return result.returncode == 0


def verify_runtime(root, manifest):
    for relative, expected in manifest["runtime_sha256"].items():
        path = root / "runtime" / relative
        if path.resolve() != path.absolute() or not path.is_file():
            raise ValueError("runtime_path_invalid")
        if path.stat().st_size > 1024 * 1024 or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError("runtime_hash_mismatch")


def quota_decision(result):
    """Check the sanitized transport result again at the admission boundary."""
    if not isinstance(result, dict) or result.get("status") not in {"eligible", "blocked", "unavailable"}:
        return {"status": "unavailable", "assessed_windows": []}
    windows = result.get("assessed_windows", [])
    if not isinstance(windows, list):
        return {"status": "unavailable", "assessed_windows": []}
    clean = []
    for row in windows:
        if not isinstance(row, dict) or row.get("duration_mins") not in {300, 10080}:
            return {"status": "unavailable", "assessed_windows": []}
        remaining = row.get("remaining_percent")
        if (type(remaining) not in {float, int} or not math.isfinite(remaining)
                or not 0 <= remaining <= 100):
            return {"status": "unavailable", "assessed_windows": []}
        clean.append({"duration_mins": row["duration_mins"], "remaining_percent": remaining})
    status = result["status"]
    if any(row["remaining_percent"] < 20 for row in clean):
        status = "blocked"
    elif status == "eligible" and not clean:
        status = "unavailable"
    return {"status": status, "assessed_windows": clean}


def collect(root, manifest):
    # The maintained collector emits one small JSON receipt. Run it in the same
    # process group so launchd also terminates it if the parent is stopped.
    result = subprocess.run([
        manifest["python_path"], str(root / "runtime/scripts/model_watch_collect.py"), "collect",
        "--config", str(root / "runtime/docs/model-watch/collector-sources.json"),
        "--state-root", str(root / "collector"),
    ], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=110)
    if len(result.stdout) > 16384:
        raise ValueError("collector_receipt_too_large")
    receipt = strict_json(result.stdout)
    if result.returncode != 0 or not isinstance(receipt, dict) or receipt.get("status") != "complete":
        return {"status": "error"}
    return {key: receipt[key] for key in ("status", "run_id", "packet_ref", "requests", "response_bytes")
            if key in receipt}


def tick(root: Path, now=None, quota_reader=None, collector=None, disabler=None, zone_reader=None):
    """Attempt at most once per selected local date; dependencies are injectable."""
    root = Path(root)
    # Do not create arbitrary roots or follow redirected campaign paths.
    if (not root.is_absolute() or root.resolve() != root.absolute() or not root.is_dir()
            or any((p / ".git").exists() for p in (root, *root.parents))):
        receipt = {"status": "error", "reason": "invalid_campaign_root", "model_calls": 0, "dispatches": 0}
        try:
            receipt["disabled"] = bool((disabler or disable_job)())
        except Exception:
            receipt["disabled"] = False
        return receipt
    lock = (root / "campaign.lock").open("a+")
    try:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return {"status": "overlap", "model_calls": 0, "dispatches": 0}
        receipt = {"version": 1, "model_calls": 0, "dispatches": 0}
        manifest = None
        local = None
        end = None
        day_entry = None
        days = None
        try:
            manifest = strict_json((root / "campaign.json").read_bytes())
            start, end = validate_manifest(manifest)
            instant = now if now is not None else datetime.now(timezone.utc)
            if instant.tzinfo is None or instant.utcoffset() is None:
                raise ValueError("timezone_required")
            local = instant.astimezone(ZoneInfo(ZONE))
            receipt.update({"observed_at": instant.astimezone(timezone.utc).isoformat(),
                            "local_date": local.date().isoformat(), "campaign": LABEL})
            current = local.hour * 3600 + local.minute * 60 + local.second + local.microsecond / 1000000
            slot = manifest["hour"] * 3600 + manifest["minute"] * 60
            deadline = manifest["deadline_hour"] * 3600 + manifest["deadline_minute"] * 60
            if local.date() > end:
                receipt["status"] = "expired"
            elif local.date() < start:
                receipt["status"] = "outside_window"
            elif current < slot:
                receipt["status"] = "before_slot"
            elif current > deadline:
                receipt["status"] = "missed_window"
            else:
                if (zone_reader or host_zone)() != ZONE:
                    raise ValueError("host_timezone_changed")
                verify_runtime(root, manifest)
                state_path = root / "days.json"
                days = strict_json(state_path.read_bytes()) if state_path.exists() else {"version": 1, "days": []}
                if (not isinstance(days, dict) or days.get("version") != 1
                        or not isinstance(days.get("days"), list) or len(days["days"]) > 7
                        or any(not isinstance(row, dict) or "date" not in row for row in days["days"])):
                    raise ValueError("invalid_day_reservations")
                if any(row["date"] == local.date().isoformat() for row in days["days"]):
                    receipt["status"] = "duplicate_day"
                else:
                    day_entry = {"date": local.date().isoformat(), "status": "reserved",
                                 "reserved_at": receipt["observed_at"]}
                    days["days"].append(day_entry)
                    atomic_bytes(state_path, encode(days))
                    try:
                        quota = quota_decision((quota_reader or (lambda: codex_quota.read_quota(manifest["codex_path"])))())
                    except Exception:
                        quota = {"status": "unavailable", "assessed_windows": []}
                    receipt["quota"] = quota
                    if quota["status"] != "eligible":
                        receipt["status"] = "quota_" + quota["status"]
                    else:
                        result = (collector or (lambda: collect(root, manifest)))()
                        if not isinstance(result, dict) or result.get("status") != "complete":
                            receipt["status"] = "collection_error"
                        else:
                            receipt["status"] = "collected_complete"
                            receipt["collection"] = result
        except Exception as exc:
            receipt["status"] = "error"
            # Never copy subprocess output or arbitrary exception text to disk.
            receipt["reason"] = str(exc) if type(exc) is ValueError and str(exc) in {
                "host_timezone_changed", "runtime_path_invalid", "runtime_hash_mismatch",
                "invalid_day_reservations", "timezone_required"} else "operation_failed"
        finally:
            if receipt.get("status") == "error" or (local and end and (local.date() > end or
                    (local.date() == end and receipt.get("status") != "before_slot"))):
                try:
                    receipt["disabled"] = bool((disabler or disable_job)())
                except Exception:
                    receipt["disabled"] = False
            if day_entry is not None:
                day_entry["status"] = receipt["status"]
                atomic_bytes(root / "days.json", encode(days))
            ticks = root / "ticks"
            ticks.mkdir(mode=0o700, exist_ok=True)
            # Bounded pilot log: last-tick always updates; retain at most 256
            # immutable receipts even if RunAtLoad is invoked repeatedly.
            if len(list(ticks.iterdir())) < 256:
                atomic_bytes(ticks / (uuid.uuid4().hex + ".json"), encode(receipt))
            atomic_bytes(root / "last-tick.json", encode(receipt))
        return receipt
    finally:
        lock.close()


def main(argv=None):
    os.umask(0o077)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("tick", "status"))
    parser.add_argument("--campaign", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.command == "tick":
        receipt = tick(args.campaign)
    else:
        receipt = {name: strict_json((args.campaign / name).read_bytes())
                   for name in ("campaign.json", "days.json", "last-tick.json")
                   if (args.campaign / name).is_file()}
    print(json.dumps(receipt, sort_keys=True, separators=(",", ":")))
    return 2 if receipt.get("status") == "error" else 0


if __name__ == "__main__":
    raise SystemExit(main())
