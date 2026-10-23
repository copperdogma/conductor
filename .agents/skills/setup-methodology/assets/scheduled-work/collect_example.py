#!/usr/bin/env python3
"""Offline synthetic collector. Replace with a project-owned bounded collector."""
from datetime import datetime, timezone
import json
from pathlib import Path

source = json.loads(Path("sample-input.json").read_text())
count = source["unresolved_count"]
if type(count) is not int or count < 0:
    raise ValueError("invalid synthetic count")
print(json.dumps({
    "observed_at": datetime.now(timezone.utc).isoformat(),
    "status": "attention" if count >= 3 else "ok",
    "signal": {"threshold_exceeded": count >= 3},
    "summary": "Synthetic queue threshold reached." if count >= 3 else "Synthetic queue is below threshold.",
    "period": source["period"],
}))
