#!/usr/bin/env python3
"""Collect or replay public model catalogs. No model calls, scheduling or dispatch.

Python 3.10+, POSIX. Operational usage: docs/model-watch/collector-runbook.md.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
from http.client import HTTPException
import json
import os
from pathlib import Path
import signal
import socket
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "docs/model-watch/collector-sources.json"
SOURCES = {"general": "https://openrouter.ai/api/v1/models",
           "decisions": "https://openrouter.ai/api/v1/models?output_modalities=decisions"}
MAX_LIMITS = {"attempt_seconds": 15, "run_seconds": 90, "feed_bytes": 8 * 1024**2,
              "run_bytes": 32 * 1024**2, "state_bytes": 448 * 1024**2,
              "max_pages": 8, "packet_bytes": 8192, "newest_slice": 40}
VERSION = 1


class CollectionError(ValueError):
    """A bounded, content-free operational error code."""

    def __init__(self, code, evidence=None):
        super().__init__(code)
        self.evidence = evidence


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":"), allow_nan=False)


def encode(value):
    return (canonical(value) + "\n").encode()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def strict_json(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise CollectionError("duplicate_json_key")
            result[key] = value
        return result
    def constant(_):
        raise CollectionError("nonfinite_json")
    return json.loads(raw, object_pairs_hook=pairs, parse_constant=constant)


def load_config(path):
    raw = path.read_bytes()
    config = strict_json(raw)
    if not isinstance(config, dict) or config.get("version") != VERSION or config.get("sources") != SOURCES:
        raise CollectionError("unsupported_source_config")
    limits = config.get("limits", {})
    if set(limits) != set(MAX_LIMITS):
        raise CollectionError("invalid_limits")
    for key, maximum in MAX_LIMITS.items():
        value = limits[key]
        if type(value) is not int or not 0 < value <= maximum:
            raise CollectionError("invalid_limits")
    if limits["packet_bytes"] < 2048:
        raise CollectionError("packet_limit_too_small")
    return config


def validate_rows(rows, feed):
    if not isinstance(rows, list) or not rows:
        raise CollectionError("empty_or_invalid_rows")
    ids = set()
    for row in rows:
        if not isinstance(row, dict):
            raise CollectionError("invalid_row")
        identity = row.get("id")
        if (not isinstance(identity, str) or not 1 <= len(identity) <= 512 or
                "/" not in identity or not all(identity.split("/")) or
                any(c.isspace() or ord(c) < 32 for c in identity)):
            raise CollectionError("invalid_id")
        if identity in ids:
            raise CollectionError("duplicate_id")
        ids.add(identity)
        architecture = row.get("architecture")
        if not isinstance(architecture, dict) or not isinstance(architecture.get("output_modalities"), list):
            raise CollectionError("missing_modality")
        modalities = architecture["output_modalities"]
        if not modalities or not all(isinstance(x, str) for x in modalities):
            raise CollectionError("invalid_modality")
        if ("decisions" if feed == "decisions" else "text") not in modalities:
            raise CollectionError("wrong_feed_modality")
    canonical(rows)  # Reject nonfinite fixture values as well as live JSON.
    return sorted(rows, key=lambda row: row["id"])


def validate_body(body, feed, *, page=False):
    if not isinstance(body, dict) or set(("data", "total_count", "links")) - body.keys():
        raise CollectionError("unrecognized_catalog_envelope")
    total = body["total_count"]
    links = body["links"]
    if type(total) is not int or total <= 0 or not isinstance(links, dict) or "next" not in links:
        raise CollectionError("invalid_coverage_metadata")
    next_url = links["next"]
    if next_url is not None and (not isinstance(next_url, str) or not next_url):
        raise CollectionError("invalid_pagination")
    rows = validate_rows(body["data"], feed)
    if len(rows) > total or (not page and next_url is None and len(rows) != total):
        raise CollectionError("incomplete_catalog")
    return rows, total, next_url


def extract_snapshot(document, feed_name):
    """Normalize supported historical formats without inventing missing timestamps."""
    if feed_name not in SOURCES or not isinstance(document, dict):
        raise CollectionError("invalid_snapshot")
    sources = document.get("sources", document)
    if not isinstance(sources, dict):
        raise CollectionError("invalid_snapshot")
    source = sources.get(feed_name, sources.get("generation") if feed_name == "general" else None)
    if not isinstance(source, dict):
        raise CollectionError("missing_feed")
    status = source.get("status", source.get("http_status", 200))
    if status != 200:
        raise CollectionError("historical_source_unavailable")
    body = source.get("body", source)
    if not isinstance(body, dict):
        raise CollectionError("invalid_snapshot")
    if "models" in body:
        rows = validate_rows(body["models"], feed_name)
        total = body.get("count")
        if type(total) is not int or total < len(rows):
            raise CollectionError("invalid_legacy_count")
        coverage = "complete" if len(rows) == total else "sample"
    else:
        rows, total, next_url = validate_body(body, feed_name)
        if next_url is not None:
            raise CollectionError("historical_pagination_incomplete")
        coverage = "complete"
    return {"coverage": coverage, "rows": rows, "total_count": total,
            "observed_at": source.get("observed_at", document.get("retrieved_at")),
            "body_sha256": sha(encode(body))}


def changed_fields(before, after, path=""):
    if type(before) is not type(after):
        return [path or "/"]
    if isinstance(before, dict):
        result = []
        for key in sorted(before.keys() | after.keys()):
            child = path + "/" + key.replace("~", "~0").replace("/", "~1")
            if key not in before or key not in after:
                result.append(child)
            else:
                result.extend(changed_fields(before[key], after[key], child))
        return result
    return [] if before == after else [path or "/"]


def diff_rows(before_rows_or_None, after_rows):
    after = {row["id"]: row for row in after_rows}
    if before_rows_or_None is None:
        return {"comparison": "baseline", "added": [], "removed": [], "changed": [], "unchanged_count": 0}
    before = {row["id"]: row for row in before_rows_or_None}
    changed = []
    for identity in sorted(before.keys() & after.keys()):
        fields = changed_fields(before[identity], after[identity])
        if fields:
            changed.append({"id": identity, "fields": fields,
                            "old_canonical_slug": before[identity].get("canonical_slug"),
                            "new_canonical_slug": after[identity].get("canonical_slug")})
    return {"comparison": "compared", "added": sorted(after.keys() - before.keys()),
            "removed": sorted(before.keys() - after.keys()), "changed": changed,
            "unchanged_count": len(before.keys() & after.keys()) - len(changed)}


def allowed_url(url, feed):
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or parsed.netloc != "openrouter.ai" or parsed.path != "/api/v1/models" or parsed.fragment:
        raise CollectionError("url_outside_allowlist")
    pairs = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query = dict(pairs)
    if len(query) != len(pairs) or set(query) - {"offset", "limit", "output_modalities"}:
        raise CollectionError("pagination_query_changed")
    if query.get("output_modalities", "text") != ("decisions" if feed == "decisions" else "text"):
        raise CollectionError("pagination_feed_changed")
    for key in ("offset", "limit"):
        if key in query and (not query[key].isascii() or not query[key].isdigit() or (key == "limit" and not 1 <= int(query[key]) <= 1000)):
            raise CollectionError("invalid_pagination_query")
    return url


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Fail visibly rather than silently discover a new source/contract.
        raise CollectionError("redirect_requires_review")


class Budget:
    def __init__(self, seconds):
        self.deadline = time.monotonic() + seconds
        self.requests = 0
        self.bytes = 0

    def remaining(self):
        value = self.deadline - time.monotonic()
        if value <= 0:
            raise CollectionError("run_deadline")
        return value


@contextmanager
def wall_limit(seconds):
    """POSIX main-thread wall deadline, including a server that drips bytes."""
    def expired(_signum, _frame):
        raise CollectionError("run_deadline")
    previous = signal.signal(signal.SIGALRM, expired)
    prior_timer = signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, *prior_timer)
        signal.signal(signal.SIGALRM, previous)


def fetch_feed(feed, config, cache, budget, opener=None):
    evidence = {"pages": [], "attempts": []}
    try:
        return _fetch_feed(feed, config, cache, budget, opener, evidence)
    except (ValueError, KeyError, TypeError, OSError, RecursionError, HTTPException) as error:
        code = str(error) if isinstance(error, CollectionError) else type(error).__name__
        raise CollectionError(code, evidence) from None


def _fetch_feed(feed, config, cache, budget, opener, evidence):
    limits = config["limits"]
    opener = opener or urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    url = config["sources"][feed]
    seen, rows = set(), []
    pages, attempts = evidence["pages"], evidence["attempts"]
    total, bytes_read = None, 0
    validators = {}
    while url is not None:
        allowed_url(url, feed)
        if url in seen or len(seen) >= limits["max_pages"]:
            raise CollectionError("pagination_cycle_or_limit")
        seen.add(url)
        headers = {"Accept": "application/json", "Accept-Encoding": "identity", "User-Agent": "Conductor-catalog-collector/1"}
        if not pages and cache and cache.get("conditional_ok"):
            for key, header in (("etag", "If-None-Match"), ("last_modified", "If-Modified-Since")):
                value = cache.get(key)
                if isinstance(value, str) and 0 < len(value) <= 512 and not any(c in value for c in "\r\n"):
                    headers[header] = value
        response = None
        for attempt in range(2):
            budget.remaining()
            budget.requests += 1
            try:
                request = urllib.request.Request(url, headers=headers)
                response = opener.open(request, timeout=min(limits["attempt_seconds"], budget.remaining()))
                break
            except urllib.error.HTTPError as error:
                attempts.append({"url": url, "http_status": error.code})
                error.close()
                sent_validator = "If-None-Match" in headers or "If-Modified-Since" in headers
                if error.code == 304 and sent_validator and not pages and cache and cache.get("conditional_ok"):
                    return {"snapshot": {**cache["snapshot"], "observed_at": datetime.now(timezone.utc).isoformat()},
                            "pages": [], "attempts": attempts, "http_status": 304,
                            "etag": cache.get("etag"), "last_modified": cache.get("last_modified"),
                            "conditional_ok": True}
                if error.code not in {408, 429, 500, 502, 503, 504} or attempt:
                    raise CollectionError("http_" + str(error.code)) from None
            except (urllib.error.URLError, TimeoutError, socket.timeout, ConnectionError):
                attempts.append({"url": url, "error": "transport_failure"})
                if attempt:
                    raise CollectionError("transport_failure") from None
            time.sleep(min(0.25, budget.remaining()))
        if response is None:
            raise CollectionError("transport_failure")
        with response:
            attempt_receipt = {"url": url, "http_status": response.status, "bytes": 0}
            attempts.append(attempt_receipt)
            if response.status != 200:
                raise CollectionError("unexpected_http_status")
            allowed_url(response.geturl(), feed)
            if response.headers.get("Content-Encoding", "identity").lower() not in {"identity", ""}:
                raise CollectionError("unexpected_content_encoding")
            # Identity encoding was requested; refuse compressed input rather than
            # permit unbounded decompression. Preserve an explicit failure receipt.
            chunks = []
            while True:
                budget.remaining()
                block = response.read(min(65536, limits["feed_bytes"] - bytes_read + 1))
                if not block:
                    break
                bytes_read += len(block)
                budget.bytes += len(block)
                attempt_receipt["bytes"] += len(block)
                if bytes_read > limits["feed_bytes"]:
                    raise CollectionError("feed_byte_limit")
                chunks.append(block)
            raw = b"".join(chunks)
            # Save bounded HTTP200 evidence before parsing/schema validation.
            pages.append(raw)
            page = strict_json(raw)
            page_rows, page_total, next_url = validate_body(page, feed, page=True)
            if total is not None and total != page_total:
                raise CollectionError("pagination_total_changed")
            total = page_total
            rows.extend(page_rows)
            if len(pages) == 1:
                validators = {"etag": response.headers.get("ETag"), "last_modified": response.headers.get("Last-Modified")}
            url = urllib.parse.urljoin(url, next_url) if next_url is not None else None
    rows = validate_rows(rows, feed)
    if len(rows) != total:
        raise CollectionError("incomplete_catalog")
    body = {"data": rows, "total_count": total, "links": {"next": None}}
    return {"snapshot": {"coverage": "complete", "rows": rows, "total_count": total,
                         "observed_at": datetime.now(timezone.utc).isoformat(), "body_sha256": sha(encode(body))},
            "pages": pages, "attempts": attempts, "http_status": 200,
            # A first-page validator cannot validate a merged multipage snapshot.
            **validators, "conditional_ok": len(pages) == 1}


def atomic_bytes(path, raw):
    fd, temporary = tempfile.mkstemp(dir=path.parent, prefix=".writing-")
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        Path(temporary).unlink(missing_ok=True)


def load_state(root, config, mode):
    path = root / "state.json"
    signature = sha(encode(config))
    if not path.exists():
        return {"version": VERSION, "config_sha256": signature, "mode": mode, "feeds": {}, "review_backlog": []}
    state = strict_json(path.read_bytes())
    if not isinstance(state, dict) or state.get("version") != VERSION or state.get("config_sha256") != signature or state.get("mode") != mode:
        raise CollectionError("state_config_or_mode_mismatch")
    if not isinstance(state.get("feeds"), dict) or set(state["feeds"]) - SOURCES.keys() or not isinstance(state.get("review_backlog"), list):
        raise CollectionError("invalid_state")
    for ref in state["feeds"].values():
        if not isinstance(ref, dict) or set(ref) != {"run_id", "snapshot_sha256"} or not isinstance(ref["snapshot_sha256"], str) or len(ref["snapshot_sha256"]) != 64:
            raise CollectionError("invalid_feed_reference")
    for run_id in [state.get("latest_run"), *state["review_backlog"], *(ref["run_id"] for ref in state["feeds"].values())]:
        if not isinstance(run_id, str) or not run_id or any(c not in "0123456789TZ-abcdef" for c in run_id):
            raise CollectionError("invalid_run_reference")
    return state


def previous_feed(root, state, feed):
    ref = state["feeds"].get(feed)
    if ref is None:
        return None
    if not isinstance(ref, dict):
        raise CollectionError("invalid_feed_reference")
    raw = (root / "runs" / ref["run_id"] / "snapshot.json").read_bytes()
    if sha(raw) != ref.get("snapshot_sha256"):
        raise CollectionError("baseline_hash_mismatch")
    record = strict_json(raw)
    snapshot = record["feeds"][feed]
    if snapshot.get("coverage") != "complete":
        raise CollectionError("baseline_not_complete")
    validate_rows(snapshot["rows"], feed)
    return {"snapshot": snapshot, **record["http"].get(feed, {})}


def packet_for(root, run_id, snapshots, deltas, state, status, config):
    run_dir = root / "runs" / run_id
    packet = {"version": VERSION, "mode": state["mode"], "status": status,
              "run_id": run_id, "config_sha256": state["config_sha256"],
              "snapshot_ref": str(run_dir / "snapshot.json"), "delta_ref": str(run_dir / "delta.json"),
              "review_backlog_ref": str(root / "state.json"), "review_backlog_count": len(state["review_backlog"]),
              "requires_semantic_review": True, "completion_claim": False, "feeds": {}}
    for feed in SOURCES:
        snapshot = snapshots.get(feed)
        delta = deltas[feed]
        feed_packet = {"coverage": snapshot["coverage"] if snapshot else "unavailable",
                       "observed_at": snapshot.get("observed_at") if snapshot else None,
                       "comparison": delta["comparison"],
                       "added_count": len(delta.get("added", [])), "removed_count": len(delta.get("removed", [])),
                       "changed_count": len(delta.get("changed", [])), "selected": []}
        if snapshot:
            rows = sorted(snapshot["rows"], key=lambda row: (-(row.get("created") if type(row.get("created")) is int else 0), row["id"]))
            selected = rows[:config["limits"]["newest_slice"]] if feed == "general" else rows
            feed_packet["total_rows"] = len(rows)
            feed_packet["selected"] = [row["id"] for row in selected]
            feed_packet["omitted_rows"] = len(rows) - len(selected)
        else:
            feed_packet["error"] = delta.get("error", "unavailable")
        packet["feeds"][feed] = feed_packet
    # Enforce byte cap while keeping mandatory references and explicit omissions.
    cap = config["limits"]["packet_bytes"]
    while len(encode(packet)) > cap:
        candidates = [item for item in packet["feeds"].values() if item["selected"]]
        if not candidates:
            raise CollectionError("packet_reference_overflow")
        largest = max(candidates, key=lambda item: len(encode(item["selected"])))
        largest["selected"].pop()
        largest["omitted_rows"] += 1
    packet["omitted_delta_details"] = sum(len(d.get("added", [])) + len(d.get("removed", [])) + len(d.get("changed", [])) for d in deltas.values())
    # Added field is small, but must also fit at the exact boundary.
    if len(encode(packet)) > cap:
        return packet_for_smaller(packet, cap)
    return packet


def packet_for_smaller(packet, cap):
    for item in packet["feeds"].values():
        while item["selected"] and len(encode(packet)) > cap:
            item["selected"].pop()
            item["omitted_rows"] += 1
    if len(encode(packet)) > cap:
        raise CollectionError("packet_reference_overflow")
    return packet


def state_size(root):
    total, count = 0, 0
    for base, directories, files in os.walk(root, followlinks=False):
        for name in [*directories, *files]:
            path = Path(base) / name
            if path.is_symlink():
                raise CollectionError("state_symlink")
        for name in files:
            count += 1
            total += (Path(base) / name).stat().st_size
            if count > 10000:
                raise CollectionError("state_file_limit")
    return total


def run(config, state_root, mode, snapshot_path=None, fetcher=None):
    root = state_root
    state = load_state(root, config, mode)
    limits = config["limits"]
    if state_size(root) + limits["run_bytes"] > limits["state_bytes"]:
        raise CollectionError("state_disk_limit")
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S") + "Z-" + uuid.uuid4().hex[:12]
    snapshots, deltas, http, raw_pages = {}, {}, {}, {}
    started = time.monotonic()
    budget = Budget(limits["run_seconds"])
    document, input_raw = None, None
    if mode == "replay":
        with snapshot_path.open("rb") as stream:
            input_raw = stream.read(limits["feed_bytes"] * 2 + 1)
        if len(input_raw) > limits["feed_bytes"] * 2:
            raise CollectionError("replay_byte_limit")
        document = strict_json(input_raw)
    for feed in SOURCES:
        previous = previous_feed(root, state, feed)
        try:
            if mode == "replay":
                snapshot = extract_snapshot(document, feed)
                http[feed] = {"source": "offline_replay", "input_sha256": sha(input_raw), "attempts": []}
            else:
                result = (fetcher or fetch_feed)(feed, config, previous, budget)
                snapshot = result["snapshot"]
                http[feed] = {key: value for key, value in result.items() if key not in {"snapshot", "pages"}}
                raw_pages[feed] = result["pages"]
            snapshot["last_validated_at"] = snapshot["observed_at"]
            if previous and (mode == "collect" and http[feed].get("http_status") == 304):
                snapshot["body_created_at"] = previous["snapshot"].get("body_created_at")
            else:
                snapshot["body_created_at"] = snapshot["observed_at"]
            snapshot["semantic_sha256"] = sha(encode(snapshot["rows"]))
            same_body = previous and previous["snapshot"].get("semantic_sha256") == snapshot["semantic_sha256"]
            snapshot["semantic_changed_at"] = previous["snapshot"].get("semantic_changed_at") if same_body else snapshot["observed_at"]
            snapshots[feed] = snapshot
            if snapshot["coverage"] == "sample":
                deltas[feed] = {"comparison": "sample_only", "saved_count": len(snapshot["rows"]), "total_count": snapshot["total_count"]}
            else:
                deltas[feed] = diff_rows(previous["snapshot"]["rows"] if previous else None, snapshot["rows"])
        except (ValueError, KeyError, TypeError, OSError, RecursionError, HTTPException) as error:
            code = str(error) if isinstance(error, CollectionError) else type(error).__name__
            deltas[feed] = {"comparison": "unavailable", "error": code}
            http[feed] = {"source": mode, "error": code}
            if isinstance(error, CollectionError) and error.evidence:
                raw_pages[feed] = error.evidence["pages"]
                http[feed]["attempts"] = error.evidence["attempts"]
        deltas[feed]["baseline_run_id"] = state["feeds"].get(feed, {}).get("run_id")
    good = sum(item.get("coverage") == "complete" for item in snapshots.values())
    status = "complete" if good == 2 else "partial" if snapshots else "unavailable"
    if any(d["comparison"] != "compared" or d.get("added") or d.get("removed") or d.get("changed") for d in deltas.values()):
        state["review_backlog"].append(run_id)
    state["latest_run"] = run_id
    record = {"version": VERSION, "collector_sha256": sha(Path(__file__).read_bytes()),
              "mode": mode, "run_id": run_id, "config_sha256": state["config_sha256"],
              "source_urls": config["sources"], "feeds": snapshots, "http": http,
              "replay_source": str(snapshot_path.resolve()) if snapshot_path else None}
    packet = packet_for(root, run_id, snapshots, deltas, state, status, config)
    packet["prepared_at"] = datetime.now(timezone.utc).isoformat()
    if len(encode(packet)) > limits["packet_bytes"]:
        packet = packet_for_smaller(packet, limits["packet_bytes"])
    receipt = {"version": VERSION, "mode": mode, "status": status, "run_id": run_id,
               "packet_ref": str(root / "runs" / run_id / "packet.json"), "requests": budget.requests,
               "response_bytes": budget.bytes, "elapsed_ms": round((time.monotonic() - started) * 1000),
               "packet_bytes": len(encode(packet)), "model_calls": 0, "dispatches": 0}
    files = {"snapshot.json": encode(record), "delta.json": encode({"version": VERSION, "feeds": deltas}),
             "packet.json": encode(packet), "receipt.json": encode(receipt)}
    if input_raw is not None:
        files["replay-input.json"] = input_raw
    for feed, pages in raw_pages.items():
        for index, raw in enumerate(pages):
            files[f"{feed}-page-{index:03}.json"] = raw
    record_hash = sha(files["snapshot.json"])
    for feed, snapshot in snapshots.items():
        if snapshot["coverage"] == "complete":
            state["feeds"][feed] = {"run_id": run_id, "snapshot_sha256": record_hash}
    state_bytes = encode(state)
    if sum(map(len, files.values())) + len(state_bytes) + len(encode(receipt)) > limits["run_bytes"]:
        raise CollectionError("run_disk_limit")
    budget.remaining()
    runs = root / "runs"
    runs.mkdir(exist_ok=True)
    staging = Path(tempfile.mkdtemp(dir=runs, prefix=".staging-"))
    # A crash leaves an unreferenced staging/committed directory for inspection.
    # The single manifest is the commit point; no partial per-feed pointer writes.
    for name, raw in files.items():
        atomic_bytes(staging / name, raw)
    destination = runs / run_id
    if destination.exists():
        raise CollectionError("run_identity_collision")
    os.rename(staging, destination)
    directory = os.open(runs, os.O_RDONLY)
    try:
        os.fsync(directory)
    finally:
        os.close(directory)
    atomic_bytes(root / "state.json", state_bytes)
    return receipt


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["collect", "replay"])
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--state-root", type=Path, required=True)
    parser.add_argument("--snapshots", type=Path, nargs="+")
    args = parser.parse_args(argv)
    os.umask(0o077)
    try:
        if (args.mode == "replay") != bool(args.snapshots):
            raise CollectionError("snapshots_required_only_for_replay")
        root = args.state_root
        if not root.is_absolute() or root.is_symlink():
            raise CollectionError("state_root_must_be_absolute_non_symlink")
        root = root.resolve()
        if root == ROOT or ROOT in root.parents or root in ROOT.parents:
            raise CollectionError("state_root_must_be_outside_checkout")
        if any((parent / ".git").exists() for parent in [root, *root.parents]):
            raise CollectionError("state_root_must_be_outside_git_checkout")
        config = load_config(args.config)
        root.mkdir(parents=True, exist_ok=True, mode=0o700)
        with (root / "job.lock").open("a") as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                print(canonical({"status": "overlap", "model_calls": 0, "dispatches": 0}))
                return 0
            try:
                final_code = 0
                inputs = args.snapshots if args.mode == "replay" else [None]
                for path in inputs:
                    atomic_bytes(root / "last-attempt.json", encode({
                        "status": "in_progress", "mode": args.mode,
                        "started_at": datetime.now(timezone.utc).isoformat(),
                        "model_calls": 0, "dispatches": 0}))
                    with wall_limit(config["limits"]["run_seconds"]):
                        receipt = run(config, root, args.mode, path)
                    atomic_bytes(root / "last-attempt.json", encode(receipt))
                    print(canonical(receipt))
                    if receipt["status"] != "complete":
                        final_code = 2
                return final_code
            except (ValueError, KeyError, TypeError, OSError, RecursionError, HTTPException) as error:
                code = str(error) if isinstance(error, CollectionError) else type(error).__name__
                receipt = {"status": "error", "error": code, "model_calls": 0, "dispatches": 0}
                # Separate last-attempt status prevents a prior good packet from
                # hiding a new state/write failure. Never overwrite the manifest.
                try:
                    atomic_bytes(root / "last-attempt.json", encode(receipt))
                except OSError:
                    pass  # stdout and exit status remain authoritative on disk failure.
                print(canonical(receipt))
                return 2
    except (ValueError, KeyError, TypeError, OSError, RecursionError, HTTPException) as error:
        code = str(error) if isinstance(error, CollectionError) else type(error).__name__
        print(canonical({"status": "error", "error": code, "model_calls": 0, "dispatches": 0}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
