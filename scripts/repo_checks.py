#!/usr/bin/env python3
"""Lightweight checks for the Conductor repo."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import methodology_graph

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    ROOT / "AGENTS.md",
    ROOT / "README.md",
    ROOT / "Makefile",
    ROOT / "projects.yaml",
    ROOT / "inbox.md",
    ROOT / "docs/ideal.md",
    ROOT / "docs/spec.md",
    ROOT / "docs/methodology/state.yaml",
    ROOT / "docs/methodology/graph.json",
    ROOT / "docs/stories.md",
    ROOT / "docs/scout.md",
    ROOT / "docs/align-projects.md",
]


def ensure_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not path.exists()]
    if missing:
        joined = "\n".join(str(path.relative_to(ROOT)) for path in missing)
        raise SystemExit(f"Missing required files:\n{joined}")


def check_graph_json() -> None:
    json.loads((ROOT / "docs/methodology/graph.json").read_text())


def check_story_frontmatter() -> None:
    for path in sorted((ROOT / "docs/stories").glob("story-*.md")):
        text = path.read_text()
        frontmatter = methodology_graph.parse_frontmatter(text)
        if not frontmatter:
            raise SystemExit(f"Story missing frontmatter: {path.relative_to(ROOT)}")
        for key in ("title", "status", "priority"):
            if key not in frontmatter:
                raise SystemExit(f"Story frontmatter missing '{key}': {path.relative_to(ROOT)}")


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, cwd=ROOT, check=True)


def lint() -> None:
    ensure_required_files()
    check_graph_json()
    check_story_frontmatter()
    print("lint: OK")


def test() -> None:
    lint()
    run([sys.executable, "scripts/methodology_graph.py", "check"])
    run(["./scripts/sync-agent-skills.sh", "--check"])
    print("test: OK")


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] not in {"lint", "test"}:
        print("Usage: repo_checks.py [lint|test]", file=sys.stderr)
        return 2
    if argv[1] == "lint":
        lint()
    else:
        test()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

