#!/usr/bin/env python3
"""Emit sparse-safe product methodology facts as JSON or readable text."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from methodology_graph import default_root, load_state


def load_json_input(root: Path, relative: str, *, required: bool = False) -> tuple[str, Any, str | None]:
    path = root / relative
    if not path.is_file():
        return ("missing" if required else "absent"), None, f"missing required input: {relative}" if required else None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return "invalid", None, f"cannot parse {relative}: expected JSON-compatible YAML (JSON syntax): {exc}"
    if not isinstance(value, dict):
        return "invalid", None, f"{relative} must contain a JSON object"
    return "present", value, None


def collect_facts(root: Path) -> tuple[dict[str, Any], int]:
    errors: list[str] = []
    state_status, state, state_error = load_json_input(root, "docs/methodology/state.yaml", required=True)
    if state_status == "present":
        try:
            state = load_state(root / "docs/methodology/state.yaml")
        except ValueError as exc:
            state_status, state, state_error = "invalid", None, str(exc)
    if state_error:
        errors.append(state_error)

    graph_status, graph, graph_error = load_json_input(root, "docs/methodology/graph.json", required=True)
    if graph_status == "present":
        stories_value = graph.get("stories")
        if not isinstance(stories_value, list):
            graph_status, graph_error = "invalid", "docs/methodology/graph.json requires a stories array"
            graph = None
        elif any(
            not isinstance(story, dict)
            or not story.get("id")
            or not story.get("title")
            or not story.get("status")
            for story in stories_value
        ):
            graph_status, graph_error = "invalid", "docs/methodology/graph.json contains a malformed story record"
            graph = None
    if graph_error:
        errors.append(graph_error)

    eval_status, registry, eval_error = load_json_input(root, "docs/evals/registry.yaml")
    if eval_status == "present":
        evals = registry.get("evals")
        if not isinstance(evals, list):
            eval_status, eval_error = "invalid", "docs/evals/registry.yaml requires an evals array"
            evals = []
        elif any(not isinstance(item, dict) or not item.get("id") for item in evals):
            eval_status, eval_error = "invalid", "docs/evals/registry.yaml contains a malformed eval record"
            evals = []
    else:
        evals = []
    if eval_error:
        errors.append(eval_error)

    stories = graph.get("stories", []) if graph else []
    story_counts = dict(sorted(Counter(
        str(story.get("status") or "Unknown") for story in stories if isinstance(story, dict)
    ).items()))
    lanes = state.get("lanes", {}) if state else {}
    lane_summary = {
        name: {"status": lane.get("status"), "reason": lane.get("reason", ""), "trigger": lane.get("trigger", "")}
        for name, lane in sorted(lanes.items())
        if isinstance(lane, dict)
    }
    project = graph.get("project") if graph else None
    if not isinstance(project, dict) and state:
        project = state.get("project")
    facts = {
        "status": "invalid" if errors else "valid",
        "errors": errors,
        "project": project,
        "inputs": {"state": state_status, "graph": graph_status, "eval_registry": eval_status},
        "stories": {"total": len(stories), "by_status": story_counts},
        "evals": {"status": eval_status, "total": len(evals) if eval_status == "present" else 0},
        "lanes": lane_summary,
        "skills": skill_surface_facts(root),
    }
    return facts, (1 if errors else 0)


def skill_surface_facts(root: Path) -> dict[str, Any]:
    skill_root = root / ".agents/skills"
    canonical_files = sorted(skill_root.glob("*/SKILL.md")) if skill_root.is_dir() else []
    expected_targets = {
        ".claude/skills": "../.agents/skills",
        ".cursor/skills": "../.agents/skills",
        "skills": ".agents/skills",
    }
    links: dict[str, dict[str, str | None]] = {}
    for relative, expected in expected_targets.items():
        path = root / relative
        if not path.exists() and not path.is_symlink():
            status, target = "absent", None
        elif not path.is_symlink():
            status, target = "drift", None
        else:
            target = str(path.readlink())
            points_to_expected = target == expected and path.exists()
            status = "present" if points_to_expected else "drift"
        links[relative] = {"status": status, "target": target}
    link_statuses = {item["status"] for item in links.values()}
    if "drift" in link_statuses:
        aggregate_link_status = "drift"
    elif link_statuses == {"present"}:
        aggregate_link_status = "present"
    elif link_statuses == {"absent"}:
        aggregate_link_status = "absent"
    else:
        aggregate_link_status = "partial"
    alias_root = root / ".gemini/commands"
    aliases = sorted(alias_root.glob("*.toml")) if alias_root.is_dir() else []
    return {
        "canonical": {"status": "present" if canonical_files else "absent", "count": len(canonical_files)},
        "compatibility_links": {"status": aggregate_link_status, "links": links},
        "command_aliases": {"status": "present" if aliases else "absent", "count": len(aliases)},
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=default_root(), help="product checkout root")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON only")
    args = parser.parse_args(argv)
    facts, status = collect_facts(args.root.resolve())
    if args.json:
        print(json.dumps(facts, indent=2, sort_keys=True))
    elif facts["errors"]:
        print("Triage facts invalid:")
        for error in facts["errors"]:
            print(f"- {error}")
    else:
        print("Triage Facts")
        print(f"- project: {(facts['project'] or {}).get('name', 'unknown')}")
        print(f"- stories: {facts['stories']['total']} {facts['stories']['by_status']}")
        print(f"- eval registry: {facts['evals']['status']} ({facts['evals']['total']})")
        print(f"- optional lanes: {facts['lanes'] or 'none declared'}")
        print(f"- canonical skills: {facts['skills']['canonical']['status']}")
        print(f"- compatibility links: {facts['skills']['compatibility_links']['status']}")
        print(f"- command aliases: {facts['skills']['command_aliases']['status']}")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
