#!/usr/bin/env python3
"""Compile a small product methodology graph from local authored files.

The state file deliberately uses JSON syntax, which is a strict subset of
JSON-compatible YAML and needs no third-party parser.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


def default_root() -> Path:
    """Find the project checkout containing this installed script."""
    for candidate in (Path(__file__).resolve().parent.parent, *Path(__file__).resolve().parents):
        if (candidate / "docs/ideal.md").is_file() and (candidate / "docs/spec.md").is_file():
            return candidate
    return Path.cwd()


def load_state(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ValueError(f"missing required methodology state: {path}")
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(
            f"cannot parse {path}: expected JSON-compatible YAML (JSON syntax): {exc}"
        ) from exc
    if not isinstance(state, dict):
        raise ValueError("methodology state must be a JSON object")
    project = state.get("project")
    if not isinstance(project, dict) or not project.get("name") or not project.get("mission"):
        raise ValueError("methodology state requires project.name and project.mission")
    categories = state.get("categories")
    if not isinstance(categories, dict):
        raise ValueError("methodology state requires a categories mapping (use {} when empty)")
    for slug, category in categories.items():
        if not isinstance(category, dict) or not isinstance(category.get("spec_ref"), str):
            raise ValueError(f"categories.{slug} requires a string spec_ref")
        for key in ("substrate", "phase", "summary"):
            if not isinstance(category.get(key), str):
                raise ValueError(f"categories.{slug} requires a string {key}")
        if category["phase"] not in {"climb", "hold", "converge"}:
            raise ValueError(f"categories.{slug}.phase must be climb, hold, or converge")
    lanes = state.get("lanes", {})
    if not isinstance(lanes, dict):
        raise ValueError("methodology state lanes must be a mapping")
    for name, lane in lanes.items():
        if not isinstance(lane, dict) or lane.get("status") not in {"absent", "deferred", "active"}:
            raise ValueError(f"lanes.{name}.status must be absent, deferred, or active")
        if not isinstance(lane.get("reason"), str):
            raise ValueError(f"lanes.{name} requires a string reason")
        if lane["status"] == "deferred" and not isinstance(lane.get("trigger"), str):
            raise ValueError(f"lanes.{name} with deferred status requires a concrete trigger")
        if lane["status"] == "deferred" and not lane["trigger"].strip():
            raise ValueError(f"lanes.{name} with deferred status requires a concrete trigger")
    return state


def read_authored_doc(path: Path, label: str) -> str:
    if not path.is_file():
        raise ValueError(f"missing required authored {label}: {path}")
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        raise ValueError(f"{label} is empty; provide a real project-authored document")
    if re.search(r"(?im)^\s*(?:TODO|TBD|replace me|your project name here)\s*$", text):
        raise ValueError(f"{label} contains an unfilled placeholder")
    return text


def parse_spec(text: str) -> tuple[list[dict[str, str]], set[str]]:
    headings = [
        {"id": match.group(2), "title": match.group(3).strip()}
        for match in re.finditer(r"^(#{2,6})\s+(spec:\d+(?:\.\d+)*)\s+(.+?)\s*$", text, re.M)
    ]
    if not headings:
        raise ValueError("spec.md must contain at least one '## spec:N Title' heading")
    ids = [item["id"] for item in headings]
    if len(ids) != len(set(ids)):
        raise ValueError("spec.md contains duplicate spec headings")
    top_level_categories = {
        match.group(1)
        for match in re.finditer(r"^##\s+(spec:\d+)\s+.+?$", text, re.M)
    }
    if not top_level_categories:
        raise ValueError("spec.md must contain at least one top-level '## spec:N Title' category")
    return headings, top_level_categories


def parse_frontmatter(text: str, path: Path) -> dict[str, Any]:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: story requires YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{path}: unterminated story frontmatter")
    result: dict[str, Any] = {}
    current_list: str | None = None
    for line_no, raw in enumerate(text[4:end].splitlines(), 2):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        list_match = re.fullmatch(r"\s+-\s*(.*?)\s*", raw)
        if list_match:
            if current_list is None:
                raise ValueError(f"{path}:{line_no}: list item without a frontmatter key")
            value = unquote(list_match.group(1))
            result[current_list].append(value)
            continue
        match = re.fullmatch(r"([a-zA-Z_][\w-]*):(?:\s*(.*))?", raw)
        if not match:
            raise ValueError(f"{path}:{line_no}: unsupported frontmatter syntax")
        key, raw_value = match.group(1), (match.group(2) or "").strip()
        if key in result:
            raise ValueError(f"{path}:{line_no}: duplicate frontmatter key {key}")
        current_list = None
        if raw_value == "[]" or raw_value == "":
            result[key] = []
            current_list = key
        elif raw_value.startswith("[") and raw_value.endswith("]"):
            inside = raw_value[1:-1].strip()
            result[key] = [] if not inside else [unquote(part.strip()) for part in inside.split(",")]
            if not inside:
                current_list = key
        else:
            result[key] = unquote(raw_value)
    for key in ("title", "status", "priority"):
        if not isinstance(result.get(key), str) or not result[key].strip():
            raise ValueError(f"{path}: frontmatter requires non-empty {key}")
    for key in ("spec_refs", "category_refs", "depends_on"):
        value = result.get(key, [])
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            raise ValueError(f"{path}: {key} must be a list of strings")
        result[key] = value
    return result


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def story_id_from_path(path: Path) -> str:
    match = re.match(r"story-(\d+)-", path.name)
    if not match:
        raise ValueError(f"story filename must begin story-NNN-: {path.name}")
    return str(int(match.group(1)))


def parse_stories(root: Path, spec_ids: set[str], state: dict[str, Any]) -> list[dict[str, Any]]:
    story_dir = root / "docs/stories"
    paths = sorted(story_dir.glob("story-*.md")) if story_dir.is_dir() else []
    known_categories = state["categories"]
    stories: list[dict[str, Any]] = []
    seen: set[str] = set()
    for path in paths:
        story_id = story_id_from_path(path)
        if story_id in seen:
            raise ValueError(f"duplicate story ID {story_id}: {path.name}")
        seen.add(story_id)
        fm = parse_frontmatter(path.read_text(encoding="utf-8"), path.relative_to(root))
        for ref in fm["spec_refs"]:
            if ref not in spec_ids:
                raise ValueError(f"{path.relative_to(root)} references unknown spec {ref}")
        for category in fm["category_refs"]:
            if category not in known_categories:
                raise ValueError(f"{path.relative_to(root)} references unknown category {category}")
        dependencies = [canonical_story_id(item) for item in fm["depends_on"]]
        stories.append({
            "id": story_id,
            "title": fm["title"],
            "status": fm["status"],
            "priority": fm["priority"],
            "path": path.relative_to(root).as_posix(),
            "spec_refs": sorted(set(fm["spec_refs"])),
            "category_refs": sorted(set(fm["category_refs"])),
            "depends_on": dependencies,
        })
    story_ids = {story["id"] for story in stories}
    for story in stories:
        for dependency in story["depends_on"]:
            if dependency not in story_ids:
                raise ValueError(f"story {story['id']} depends on unknown story {dependency}")
    return stories


def canonical_story_id(value: str) -> str:
    match = re.fullmatch(r"(?:story-)?(\d+)", value.strip(), re.I)
    if not match:
        raise ValueError(f"story dependency must be a numeric ID: {value}")
    return str(int(match.group(1)))


def build_outputs(root: Path) -> tuple[str, str]:
    read_authored_doc(root / "docs/ideal.md", "Ideal")
    spec_text = read_authored_doc(root / "docs/spec.md", "Spec")
    state = load_state(root / "docs/methodology/state.yaml")
    spec, category_spec_ids = parse_spec(spec_text)
    spec_ids = {item["id"] for item in spec}
    mapped_spec_ids: set[str] = set()
    for slug, category in state["categories"].items():
        spec_ref = category["spec_ref"]
        if spec_ref not in category_spec_ids:
            raise ValueError(f"categories.{slug} references unknown spec {category['spec_ref']}")
        if spec_ref in mapped_spec_ids:
            raise ValueError(f"multiple state categories map to {spec_ref}")
        mapped_spec_ids.add(spec_ref)
    missing_categories = category_spec_ids - mapped_spec_ids
    if missing_categories:
        raise ValueError("methodology state is missing top-level spec categories: " + ", ".join(sorted(missing_categories)))
    stories = parse_stories(root, spec_ids, state)
    counts = dict(sorted(Counter(story["status"] for story in stories).items()))
    categories = [
        {"id": item["id"], "title": item["title"], "state": state["categories"].get(slug)}
        for item in spec
        if item["id"] in category_spec_ids
        for slug in [next((key for key, value in state["categories"].items() if value["spec_ref"] == item["id"]), "")]
    ]
    graph = {
        "project": {"name": state["project"]["name"], "mission": state["project"]["mission"]},
        "sources": {
            "ideal": "docs/ideal.md",
            "spec": "docs/spec.md",
            "state": "docs/methodology/state.yaml",
            "stories": "docs/stories/*.md",
        },
        "categories": categories,
        "lanes": state.get("lanes", {}),
        "stories": stories,
        "story_counts": counts,
    }
    graph_text = json.dumps(graph, indent=2, sort_keys=True) + "\n"
    lines = ["# Stories", "", "_Generated by `methodology_graph.py compile`._", "", "## Summary", ""]
    if counts:
        lines.extend(f"- {status}: {count}" for status, count in counts.items())
    else:
        lines.append("No stories yet.")
    lines.extend(["", "## Index", "", "| ID | Status | Priority | Title | File |", "| --- | --- | --- | --- | --- |"])
    for story in stories:
        lines.append(f"| {story['id']} | {story['status']} | {story['priority']} | {story['title']} | `{story['path']}` |")
    index_text = "\n".join(lines) + "\n"
    return graph_text, index_text


def run(command: str, root: Path) -> int:
    graph_path = root / "docs/methodology/graph.json"
    index_path = root / "docs/stories.md"
    graph_text, index_text = build_outputs(root)
    if command == "compile":
        graph_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.parent.mkdir(parents=True, exist_ok=True)
        graph_path.write_text(graph_text, encoding="utf-8")
        index_path.write_text(index_text, encoding="utf-8")
        print("Wrote docs/methodology/graph.json and docs/stories.md")
        return 0
    failures = []
    for path, expected in ((graph_path, graph_text), (index_path, index_text)):
        if not path.is_file() or path.read_text(encoding="utf-8") != expected:
            failures.append(path.relative_to(root).as_posix())
    if failures:
        print("Generated methodology output is missing or stale: " + ", ".join(failures), file=sys.stderr)
        return 1
    print("Methodology graph and story index are current")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("compile", "check"))
    parser.add_argument("--root", type=Path, default=default_root(), help="product checkout root")
    args = parser.parse_args(argv)
    try:
        return run(args.command, args.root.resolve())
    except (OSError, ValueError) as exc:
        print(f"methodology {args.command} failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
