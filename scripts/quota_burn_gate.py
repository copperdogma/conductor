#!/usr/bin/env python3
"""Inclusive 20% reserve decision for quota rounds; no account mutations."""

from __future__ import annotations

import json
import sys
from typing import Any

from codex_quota import evaluate


def decide(payload: Any, *, draining: bool = False) -> dict[str, Any]:
    """Evaluate a native rate-limit payload, preserving a latched drain."""
    assessment = evaluate(payload)
    windows = assessment["assessed_windows"]
    if draining:
        action, reason = "drain", "already_draining"
    elif assessment["status"] == "unavailable":
        action, reason = "drain", "quota_unavailable"
    elif assessment["status"] == "blocked" or any(
        row["remaining_percent"] <= 20 for row in windows
    ):
        action, reason = "drain", "reserve_reached_or_usage_blocked"
    else:
        action, reason = "continue", "above_reserve"
    return {
        "action": action,
        "reason": reason,
        "quota_status": assessment["status"],
        "assessed_windows": windows,
    }


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (ValueError, OSError):
        payload = None
    print(json.dumps(decide(payload, draining="--draining" in sys.argv[1:]), allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
