#!/usr/bin/env python3
"""Deterministic collection/gating starter. Python 3.10+, macOS/Linux, no dependencies.

No network/model integration is bundled. A dispatcher is an explicit local adapter.
See README.md for the protocol and the deliberately conservative recovery policy.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def atomic_json(path, value):
    fd, name = tempfile.mkstemp(dir=path.parent, prefix=".writing-")
    try:
        with os.fdopen(fd, "w") as stream:
            stream.write(canonical(value) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        Path(name).unlink(missing_ok=True)


def command(value):
    if not isinstance(value, list) or not value or not all(isinstance(x, str) and x for x in value):
        raise ValueError("command must be a nonempty argv array")
    return value


def validate_config(config):
    if not isinstance(config, dict):
        raise ValueError("config must be an object")
    if config.get("version") != 1 or config.get("mode") not in {"monitor", "report"}:
        raise ValueError("unsupported config")
    if not isinstance(config.get("job"), str) or not config["job"]:
        raise ValueError("missing stable job identity")
    command(config["collector"])
    if config.get("dispatcher"):
        command(config["dispatcher"])
    for field in ("timeout_seconds", "max_age_seconds"):
        value = config[field]
        if type(value) not in (int, float) or not math.isfinite(value) or value <= 0:
            raise ValueError("invalid timing configuration")
    if type(config.get("notify_recovery", False)) is not bool:
        raise ValueError("invalid recovery policy")
    if not isinstance(config.get("policy_version", "1"), str) or not config.get("policy_version", "1"):
        raise ValueError("invalid policy version")


def validate_state(state, config):
    if not isinstance(state, dict) or state.get("version") != 1 or state.get("job") != config["job"]:
        raise ValueError("wrong state version/job")
    if type(state.get("sequence", 0)) is not int or state.get("sequence", 0) < 0:
        raise ValueError("invalid sequence")
    if ("last_key" in state) != ("last_status" in state):
        raise ValueError("incomplete accepted baseline")
    def hash_value(value):
        return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value)
    if "last_key" in state and (not hash_value(state["last_key"]) or state["last_status"] not in {"ok", "attention"}):
        raise ValueError("invalid accepted baseline")
    if "pending" in state:
        pending = state["pending"]
        if not isinstance(pending, dict) or not hash_value(pending.get("event_id")) or not hash_value(pending.get("key")):
            raise ValueError("invalid pending identity")
        if pending.get("status") not in {"prepared", "uncertain"} or pending.get("reason") not in {"attention", "recovered", "report_ready"}:
            raise ValueError("invalid pending phase")
        obs = pending["observation"]
        if not isinstance(obs, dict) or not isinstance(obs.get("observed_at"), str):
            raise ValueError("invalid pending observation")
        # Structural validation without expiring a request that may need an ack.
        stamp = datetime.fromisoformat(obs["observed_at"].replace("Z", "+00:00"))
        validate_observation(obs, config, stamp)


def validate_observation(obs, config, now):
    if not isinstance(obs, dict) or obs.get("status") not in {"ok", "attention"}:
        raise ValueError("invalid collector status")
    if not isinstance(obs.get("observed_at"), str):
        raise ValueError("invalid collector timestamp")
    stamp = datetime.fromisoformat(obs["observed_at"].replace("Z", "+00:00"))
    if stamp.tzinfo is None:
        raise ValueError("collector timestamp needs timezone")
    age = (now - stamp).total_seconds()
    if age < -60 or age > config["max_age_seconds"]:
        raise ValueError("stale or future observation")
    if not isinstance(obs.get("signal"), dict):
        raise ValueError("missing stable signal object")
    if not isinstance(obs.get("summary"), str) or len(obs["summary"]) > 2000:
        raise ValueError("invalid minimized summary")
    if len(canonical(obs).encode()) > 16384:
        raise ValueError("collector output too large")
    if config["mode"] == "report" and (not isinstance(obs.get("period"), str) or not obs["period"]):
        raise ValueError("report requires an explicit reporting period")


def decide(config, state, obs):
    # Policy/version changes deliberately get a new key. Timestamps/prose do not.
    key = digest({"policy": [config["job"], config["mode"], config.get("policy_version", "1")],
                  "status": obs["status"], "signal": obs["signal"],
                  "period": obs.get("period") if config["mode"] == "report" else None})
    if key == state.get("last_key"):
        return key, "unchanged", False
    if config["mode"] == "report":
        return key, "report_ready", True
    if obs["status"] == "attention":
        return key, "attention", True
    if state.get("last_status") == "attention" and config.get("notify_recovery", False):
        return key, "recovered", True
    return key, "quiet", False


def accept(state):
    pending = state.pop("pending")
    state["last_key"] = pending["key"]
    state["last_status"] = pending["observation"]["status"]
    return pending["event_id"]


def run(config, state, state_path, attempt):
    # Only one outstanding request per job. Never overwrite unresolved work.
    if not state.get("pending"):
        # Temporary file bounds memory; collector must also bound its own I/O.
        with tempfile.TemporaryFile() as output:
            result = subprocess.run(command(config["collector"]), stdout=output,
                                    stderr=subprocess.DEVNULL, timeout=config["timeout_seconds"], check=False)
            if result.returncode:
                raise ValueError("collector failed")
            output.seek(0)
            raw = output.read(16385)
        if len(raw) > 16384:
            raise ValueError("collector output too large")
        obs = json.loads(raw)
        now = datetime.now(timezone.utc)
        validate_observation(obs, config, now)
        key, reason, wake = decide(config, state, obs)
        if not wake:
            state.update(last_key=key, last_status=obs["status"])
            atomic_json(state_path, state)
            return {"decision": reason, "dispatch_attempted": False}, 0
        state["sequence"] = state.get("sequence", 0) + 1
        state["pending"] = {"event_id": digest([config["job"], state["sequence"], key]),
                            "key": key, "reason": reason, "status": "prepared",
                            "created_at": now.isoformat(), "observation": obs}
        atomic_json(state_path, state)

    pending = state["pending"]
    event_id = pending["event_id"]
    if pending["status"] == "uncertain":
        return {"decision": "delivery_uncertain", "event_id": event_id, "dispatch_attempted": False}, 2
    if not config.get("dispatcher"):
        return {"decision": "pending_adapter", "event_id": event_id, "dispatch_attempted": False}, 0
    validate_observation(pending["observation"], config, datetime.now(timezone.utc))
    # Crash/timeout after reservation must never cause an automatic paid repeat.
    pending["status"] = "uncertain"
    atomic_json(state_path, state)
    attempt.update(dispatch_attempted=True, event_id=event_id)
    try:
        result = subprocess.run(command(config["dispatcher"]),
                                input=canonical({"job": config["job"], **pending}).encode(),
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                timeout=config["timeout_seconds"], check=False)
    except (OSError, subprocess.TimeoutExpired):
        return {"decision": "delivery_uncertain", "event_id": event_id, "dispatch_attempted": True}, 2
    if result.returncode:
        return {"decision": "delivery_uncertain", "event_id": event_id, "dispatch_attempted": True}, 2
    accept(state)
    atomic_json(state_path, state)
    return {"decision": "accepted", "event_id": event_id, "dispatch_attempted": True}, 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["run", "ack", "retry", "discard"])
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--state-dir", type=Path, required=True)
    parser.add_argument("--event-id", help="required for explicit delivery reconciliation")
    args = parser.parse_args(argv)
    os.umask(0o077)
    attempt = {"dispatch_attempted": False}
    try:
        config_path = args.config.resolve()
        config = json.loads(config_path.read_text())
        validate_config(config)
        args.state_dir = args.state_dir.absolute()
        # Commands execute relative to config directory, independent of scheduler cwd.
        os.chdir(config_path.parent)
        args.state_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
        with (args.state_dir / "job.lock").open("a") as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                print(canonical({"decision": "overlap", "dispatch_attempted": False}))
                return 0
            path = args.state_dir / "state.json"
            state = json.loads(path.read_text()) if path.exists() else {"version": 1, "job": config["job"]}
            validate_state(state, config)
            now = datetime.now(timezone.utc)
            try:
                if args.action == "run":
                    receipt, code = run(config, state, path, attempt)
                else:
                    pending = state.get("pending")
                    if not args.event_id or not pending or pending["event_id"] != args.event_id:
                        raise ValueError("reconciliation needs the current event id")
                    if args.action == "ack":
                        accept(state)
                    elif args.action == "discard":
                        state.pop("pending")
                    else:
                        pending["status"] = "prepared"
                    atomic_json(path, state)
                    receipt, code = {"decision": args.action, "event_id": args.event_id, "dispatch_attempted": False}, 0
            except (ValueError, KeyError, TypeError, OSError, subprocess.TimeoutExpired):
                receipt, code = {"decision": "error", **attempt}, 2
            receipt.update(job=config["job"], at=now.isoformat())
            atomic_json(args.state_dir / "latest.json", receipt)
            with (args.state_dir / "ledger.jsonl").open("a") as stream:
                stream.write(canonical(receipt) + "\n")
            print(canonical(receipt))
            return code
    except (ValueError, KeyError, TypeError, OSError):
        # Do not echo collector output, commands, config, or possibly sensitive paths.
        print(canonical({"decision": "configuration_or_state_error", **attempt}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
