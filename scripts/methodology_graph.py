#!/usr/bin/env python3
"""Compile lightweight methodology surfaces for Conductor."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRAPH_PATH = ROOT / "docs/methodology/graph.json"
STORIES_INDEX_PATH = ROOT / "docs/stories.md"
STORIES_DIR = ROOT / "docs/stories"
PROJECTS_PATH = ROOT / "projects.yaml"
STATE_PATH = ROOT / "docs/methodology/state.yaml"


def canonical_project_root() -> Path:
    """Prefer the repo's primary checkout root over an ephemeral worktree path."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--git-common-dir"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return ROOT

    common_dir = result.stdout.strip()
    if not common_dir:
        return ROOT

    common_path = Path(common_dir)
    if not common_path.is_absolute():
        common_path = (ROOT / common_path).resolve()

    return common_path.parent


PROJECT_ROOT = canonical_project_root()


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> dict[str, object]:
    if not text.startswith("---\n"):
        return {}

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}

    block = text[4:end].splitlines()
    data: dict[str, object] = {}
    current_key: str | None = None

    for raw in block:
        if not raw.strip():
            continue
        if raw.startswith("  - ") or raw.startswith("- "):
            if current_key is None:
                continue
            item = raw.split("- ", 1)[1].strip()
            if not isinstance(data.get(current_key), list):
                data[current_key] = []
            cast = data[current_key]
            assert isinstance(cast, list)
            cast.append(strip_quotes(item))
            continue

        if ":" not in raw:
            continue

        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key

        if not value:
            data[key] = []
        elif value == "[]":
            data[key] = []
        elif value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            if inner:
                data[key] = [strip_quotes(part.strip()) for part in inner.split(",")]
            else:
                data[key] = []
        else:
            data[key] = strip_quotes(value)

    return data


def parse_projects_yaml() -> list[dict[str, object]]:
    if not PROJECTS_PATH.exists():
        return []

    projects: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    current_list_key: str | None = None

    for raw in PROJECTS_PATH.read_text().splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#") or line.startswith("version:") or line.startswith("projects:"):
            continue

        if line.startswith("  - "):
            current = {}
            projects.append(current)
            current_list_key = None
            key, value = line[4:].split(":", 1)
            current[key.strip()] = strip_quotes(value.strip())
            continue

        if current is None:
            continue

        if line.startswith("    ") and not line.startswith("      - "):
            key, value = line.strip().split(":", 1)
            key = key.strip()
            value = value.strip()
            if value:
                current[key] = strip_quotes(value)
                current_list_key = None
            else:
                current[key] = []
                current_list_key = key
            continue

        if line.startswith("      - ") and current_list_key:
            value = strip_quotes(line.strip()[2:].strip())
            cast = current[current_list_key]
            assert isinstance(cast, list)
            cast.append(value)

    return projects


def parse_state_categories() -> list[dict[str, str]]:
    if not STATE_PATH.exists():
        return []

    categories: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    in_categories = False

    for raw in STATE_PATH.read_text().splitlines():
        line = raw.rstrip()
        if line.startswith("categories:"):
            in_categories = True
            continue
        if not in_categories:
            continue
        if not line:
            continue
        if line.startswith("tracked_projects:") or line.startswith("notes:"):
            break
        if line.startswith("  ") and line.endswith(":") and not line.startswith("    "):
            slug = line.strip()[:-1]
            current = {"key": slug}
            categories.append(current)
            continue
        if current is None:
            continue
        if line.startswith("    ") and ":" in line:
            key, value = line.strip().split(":", 1)
            current[key.strip()] = strip_quotes(value.strip())

    return categories


def parse_story(path: Path) -> dict[str, object]:
    text = path.read_text()
    frontmatter = parse_frontmatter(text)

    match = re.match(r"story-(\d+)-", path.name)
    story_id = match.group(1) if match else "000"
    title = str(frontmatter.get("title") or f"Story {story_id}")
    status = str(frontmatter.get("status") or "Draft")
    priority = str(frontmatter.get("priority") or "Medium")

    return {
        "id": int(story_id),
        "file": str(path.relative_to(ROOT)),
        "title": title,
        "status": status,
        "priority": priority,
        "ideal_refs": frontmatter.get("ideal_refs", []),
        "spec_refs": frontmatter.get("spec_refs", []),
        "decision_refs": frontmatter.get("decision_refs", frontmatter.get("adr_refs", [])),
        "depends_on": frontmatter.get("depends_on", []),
        "category_refs": frontmatter.get("category_refs", []),
    }


def collect_stories() -> list[dict[str, object]]:
    stories = [parse_story(path) for path in sorted(STORIES_DIR.glob("story-*.md"))]
    stories.sort(key=lambda story: int(story["id"]))
    return stories


def build_graph() -> dict[str, object]:
    stories = collect_stories()
    counts = Counter(story["status"] for story in stories)
    return {
        "project": {
            "name": "Conductor",
            "root": str(PROJECT_ROOT),
            "registry": str(PROJECTS_PATH.relative_to(ROOT)),
            "state": str(STATE_PATH.relative_to(ROOT)),
        },
        "tracked_projects": parse_projects_yaml(),
        "categories": parse_state_categories(),
        "stories": stories,
        "story_counts": {
            "Draft": counts.get("Draft", 0),
            "Pending": counts.get("Pending", 0),
            "In Progress": counts.get("In Progress", 0),
            "Blocked": counts.get("Blocked", 0),
            "Done": counts.get("Done", 0),
        },
        "logs": {
            "align_projects": "docs/align-projects.md",
            "scout": "docs/scout.md",
        },
    }


def build_stories_index(graph: dict[str, object]) -> str:
    stories = graph["stories"]
    counts = graph["story_counts"]

    lines = [
        "# Stories",
        "",
        "_Generated by `make methodology-compile`._",
        "",
        "## Summary",
        "",
        f"- Draft: {counts['Draft']}",
        f"- Pending: {counts['Pending']}",
        f"- In Progress: {counts['In Progress']}",
        f"- Blocked: {counts['Blocked']}",
        f"- Done: {counts['Done']}",
        "",
    ]

    if not stories:
        lines.append("No stories yet.")
        lines.append("")
        return "\n".join(lines)

    lines.extend(
        [
            "## Index",
            "",
            "| ID | Status | Priority | Title | File |",
            "| --- | --- | --- | --- | --- |",
        ]
    )

    for story in stories:
        lines.append(
            f"| {story['id']:03d} | {story['status']} | {story['priority']} | "
            f"{story['title']} | `{story['file']}` |"
        )

    lines.append("")
    return "\n".join(lines)


def rendered_outputs() -> tuple[str, str]:
    graph = build_graph()
    graph_text = json.dumps(graph, indent=2, sort_keys=True) + "\n"
    stories_text = build_stories_index(graph)
    return graph_text, stories_text


def cmd_compile() -> int:
    graph_text, stories_text = rendered_outputs()
    GRAPH_PATH.write_text(graph_text)
    STORIES_INDEX_PATH.write_text(stories_text)
    print(f"Wrote {GRAPH_PATH.relative_to(ROOT)}")
    print(f"Wrote {STORIES_INDEX_PATH.relative_to(ROOT)}")
    return 0


def cmd_check() -> int:
    expected_graph, expected_stories = rendered_outputs()

    if not GRAPH_PATH.exists():
        print(f"{GRAPH_PATH.relative_to(ROOT)} does not exist. Run make methodology-compile.", file=sys.stderr)
        return 1
    if not STORIES_INDEX_PATH.exists():
        print(f"{STORIES_INDEX_PATH.relative_to(ROOT)} does not exist. Run make methodology-compile.", file=sys.stderr)
        return 1

    current_graph = GRAPH_PATH.read_text()
    current_stories = STORIES_INDEX_PATH.read_text()

    if current_graph != expected_graph:
        print(f"{GRAPH_PATH.relative_to(ROOT)} is out of date. Run make methodology-compile.", file=sys.stderr)
        return 1
    if current_stories != expected_stories:
        print(f"{STORIES_INDEX_PATH.relative_to(ROOT)} is out of date. Run make methodology-compile.", file=sys.stderr)
        return 1

    print(f"Methodology graph is current: {GRAPH_PATH.relative_to(ROOT)}")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] not in {"compile", "check"}:
        print("Usage: methodology_graph.py [compile|check]", file=sys.stderr)
        return 2
    if argv[1] == "compile":
        return cmd_compile()
    return cmd_check()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
