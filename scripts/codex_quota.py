#!/usr/bin/env python3
"""Read a small, non-model Codex quota snapshot for local admission gates.

The app-server is used only for initialize and account/rateLimits/read. This
module never starts a turn, reads credentials, or returns account identifiers.
"""

from __future__ import annotations

import json
import math
import os
import selectors
import subprocess
import sys
import time
from collections.abc import Callable, Mapping
from typing import Any


MAX_STDOUT_BYTES = 1024 * 1024
CLIENT_INFO = {"name": "conductor-quota-gate", "title": "Conductor quota gate", "version": "1.0"}
REQUESTS = (
    {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"clientInfo": CLIENT_INFO}},
    {"jsonrpc": "2.0", "method": "initialized", "params": {}},
    {"jsonrpc": "2.0", "id": 2, "method": "account/rateLimits/read", "params": {}},
)
CORE_WINDOW_DURATIONS = {300, 10080}


class QuotaUnavailable(RuntimeError):
    """The quota snapshot could not be assessed safely."""


def _unavailable(reason: str) -> dict[str, Any]:
    return {"status": "unavailable", "assessed_windows": [], "reason": reason}


def _selected_limits(payload: Mapping[str, Any]) -> Mapping[str, Any] | None:
    # Presence of rateLimitsByLimitId is authoritative, even if its codex
    # entry is unusable; silently falling back could assess a different bucket.
    if "rateLimitsByLimitId" in payload:
        by_id = payload["rateLimitsByLimitId"]
        if not isinstance(by_id, Mapping) or "codex" not in by_id:
            return None
        selected = by_id["codex"]
    else:
        selected = payload.get("rateLimits")
    return selected if isinstance(selected, Mapping) else None


def evaluate(payload: Any) -> dict[str, Any]:
    """Return only the quota decision and core-window remaining percentages.

    ``usedPercent`` is validated strictly: booleans, NaN/infinity, and values
    outside 0..100 make the snapshot unavailable rather than being coerced.
    """
    if not isinstance(payload, Mapping):
        return _unavailable("invalid_payload")
    top_level_ordinary = payload.get("ordinaryUsageAllowed")
    if top_level_ordinary is not None and not isinstance(top_level_ordinary, bool):
        return _unavailable("malformed_usage_flag")
    if top_level_ordinary is False:
        return {"status": "blocked", "assessed_windows": []}

    limits = _selected_limits(payload)
    if limits is None:
        return _unavailable("missing_codex_limits")

    bucket_ordinary = limits.get("ordinaryUsageAllowed")
    if bucket_ordinary is not None and not isinstance(bucket_ordinary, bool):
        return _unavailable("malformed_usage_flag")
    if bucket_ordinary is False:
        return {"status": "blocked", "assessed_windows": []}
    windows: list[dict[str, Any]] = []
    blocked = False

    for name in ("primary", "secondary"):
        row = limits.get(name)
        if row is None:
            # Optional windows are nullable in native account status. Null does
            # not assert that an additional five-hour/weekly limit exists.
            continue
        if not isinstance(row, Mapping):
            return _unavailable("malformed_core_window")
        actual_duration = row.get("windowDurationMins", row.get("durationMins"))
        # The server can rotate five-hour and weekly limits between the primary
        # and secondary slots. Duration, not slot name, identifies a core window.
        if isinstance(actual_duration, bool) or not isinstance(actual_duration, int):
            return _unavailable("malformed_window_duration")
        if actual_duration not in CORE_WINDOW_DURATIONS:
            continue
        used = row.get("usedPercent")
        if isinstance(used, bool) or not isinstance(used, (int, float)):
            return _unavailable("malformed_used_percent")
        used = float(used)
        if not math.isfinite(used) or not 0 <= used <= 100:
            return _unavailable("malformed_used_percent")
        remaining = 100.0 - used
        windows.append({"name": name, "duration_mins": actual_duration, "remaining_percent": remaining})
        if remaining < 20:
            blocked = True

    if blocked:
        return {"status": "blocked", "assessed_windows": windows}
    if not windows:
        return _unavailable("no_assessable_core_window")
    return {"status": "eligible", "assessed_windows": windows}


def _next_response(
    fd: int,
    selector: selectors.BaseSelector,
    pending: bytearray,
    output: bytearray,
    response_id: int,
    deadline: float,
) -> Mapping[str, Any]:
    """Read bounded JSONL until one matching JSON-RPC response arrives."""
    while True:
        while b"\n" in pending:
            line, _, rest = pending.partition(b"\n")
            pending[:] = rest
            if not line:
                continue
            try:
                item = json.loads(line.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError):
                raise QuotaUnavailable("invalid_jsonl_response") from None
            if not isinstance(item, Mapping) or item.get("id") != response_id:
                continue
            if "error" in item:
                reason = "initialize_rpc_error" if response_id == 1 else "quota_rpc_error"
                raise QuotaUnavailable(reason)
            if "result" not in item:
                raise QuotaUnavailable("missing_rpc_result")
            return item

        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise QuotaUnavailable("timeout")
        if not selector.select(remaining):
            raise QuotaUnavailable("timeout")
        room = MAX_STDOUT_BYTES + 1 - len(output)
        chunk = os.read(fd, min(65536, room))
        if not chunk:
            raise QuotaUnavailable("missing_rpc_response")
        output.extend(chunk)
        pending.extend(chunk)
        if len(output) > MAX_STDOUT_BYTES:
            raise QuotaUnavailable("stdout_limit_exceeded")


def _run_app_server(codex: str, timeout: float, popen_factory: Callable[..., Any] = subprocess.Popen) -> Any:
    if not isinstance(timeout, (int, float)) or isinstance(timeout, bool) or not math.isfinite(timeout) or timeout <= 0:
        raise QuotaUnavailable("invalid_timeout")
    deadline = time.monotonic() + min(float(timeout), 12.0)
    try:
        proc = popen_factory(
            [codex, "app-server", "--listen", "stdio://"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            bufsize=0,
        )
    except (OSError, ValueError, subprocess.SubprocessError):
        raise QuotaUnavailable("app_server_unavailable") from None

    output = bytearray()
    pending = bytearray()
    selector = selectors.DefaultSelector()
    try:
        if proc.stdin is None or proc.stdout is None:
            raise QuotaUnavailable("app_server_pipe_unavailable")
        try:
            proc.stdin.write((json.dumps(REQUESTS[0], separators=(",", ":")) + "\n").encode("utf-8"))
            proc.stdin.flush()
        except (BrokenPipeError, OSError):
            raise QuotaUnavailable("app_server_pipe_error") from None

        selector.register(proc.stdout.fileno(), selectors.EVENT_READ)
        _next_response(proc.stdout.fileno(), selector, pending, output, 1, deadline)
        try:
            for request in REQUESTS[1:]:
                proc.stdin.write((json.dumps(request, separators=(",", ":")) + "\n").encode("utf-8"))
            proc.stdin.flush()
        except (BrokenPipeError, OSError):
            raise QuotaUnavailable("app_server_pipe_error") from None
        result = _next_response(proc.stdout.fileno(), selector, pending, output, 2, deadline)
        # The server receives EOF only after the quota response has arrived.
        try:
            proc.stdin.close()
        except OSError:
            pass
        return result["result"]
    finally:
        selector.close()
        try:
            if proc.stdin and not proc.stdin.closed:
                proc.stdin.close()
        except OSError:
            pass
        try:
            if proc.stdout:
                proc.stdout.close()
        except OSError:
            pass
        if proc.poll() is None:
            try:
                proc.terminate()
            except OSError:
                pass
        try:
            proc.wait(timeout=max(0.05, min(0.25, deadline - time.monotonic())))
        except subprocess.TimeoutExpired:
            try:
                proc.kill()
            except OSError:
                pass
            try:
                proc.wait(timeout=0.25)
            except subprocess.TimeoutExpired:
                pass


def read_quota(
    codex: str = "codex",
    timeout: float = 12,
    *,
    transport: Callable[[str, float], Any] | None = None,
    popen_factory: Callable[..., Any] = subprocess.Popen,
) -> dict[str, Any]:
    """Read and assess quota; transport may be injected for isolated callers.

    The default process path has a hard 12-second upper bound. ``transport``
    receives the executable name and bounded timeout and returns the same
    payload that an app-server ``account/rateLimits/read`` result would return.
    """
    if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or not math.isfinite(timeout) or timeout <= 0:
        return _unavailable("invalid_timeout")
    bounded_timeout = min(float(timeout), 12.0)
    try:
        payload = transport(codex, bounded_timeout) if transport else _run_app_server(codex, bounded_timeout, popen_factory)
        return evaluate(payload)
    except QuotaUnavailable as exc:
        return _unavailable(str(exc))
    except (OSError, ValueError, TypeError, subprocess.SubprocessError):
        return _unavailable("transport_error")


def main() -> int:
    print(json.dumps(read_quota(), separators=(",", ":"), allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
