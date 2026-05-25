#!/usr/bin/env python3
"""Report-only skill surface audit for Conductor."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys
import time
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import methodology_graph

ROOT = Path(__file__).resolve().parent.parent
HOME = Path.home()
DEFAULT_MODEL = "gpt-5.5"
DEFAULT_CONTEXT_TOKENS = 272_000
DEFAULT_EFFECTIVE_PERCENT = 95


@dataclass(frozen=True)
class RootSpec:
    path: Path
    kind: str
    label: str
    project: str
    confidence: str


@dataclass(frozen=True)
class SkillRecord:
    name: str
    base_name: str
    description: str
    path: str
    real_path: str
    root: str
    root_kind: str
    root_label: str
    project: str
    desc_chars: int
    line_bytes: int
    line_tokens: int
    minimum_tokens: int
    body_hash: str
    body_key: str
    enabled: bool = True


@dataclass
class Usage:
    dollar: int = 0
    file_read: int = 0
    text: int = 0

    @property
    def total(self) -> int:
        return self.dollar + self.file_read + self.text


def rel(path: str | Path) -> str:
    item = Path(path)
    try:
        return str(item.relative_to(ROOT))
    except ValueError:
        return str(item)


def expand_home(value: str) -> Path:
    return Path(value).expanduser()


def sanitize_single_line(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("\r", " ").replace("\n", " ").replace("\t", " ")).strip()


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_frontmatter(path: Path) -> tuple[str | None, str, str] | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None

    end = -1
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = index
            break
    if end < 0:
        return None

    name: str | None = None
    description = ""
    frontmatter = lines[1:end]
    body = "\n".join(lines[end + 1 :])

    index = 0
    while index < len(frontmatter):
        line = frontmatter[index]
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            index += 1
            continue

        key, raw = match.group(1), match.group(2)
        if key == "name":
            name = sanitize_single_line(strip_quotes(raw))
        elif key == "description":
            if raw.strip() in {"|", ">"}:
                block: list[str] = []
                cursor = index + 1
                while cursor < len(frontmatter):
                    next_line = frontmatter[cursor]
                    if re.match(r"^[A-Za-z0-9_-]+:\s*", next_line):
                        break
                    block.append(re.sub(r"^\s{2}", "", next_line))
                    cursor += 1
                description = sanitize_single_line(" ".join(block))
                index = cursor - 1
            else:
                description = sanitize_single_line(strip_quotes(raw))
        index += 1

    return name, description, body


def normalize_words(value: str) -> str:
    lowered = value.lower()
    lowered = re.sub(r"[`\"'’().,;:!?/\\\[\]{}_-]+", " ", lowered)
    return re.sub(r"\s+", " ", lowered).strip()


def line_for(name: str, description: str, path: Path) -> str:
    if description:
        return f"- {name}: {description} (file: {path})"
    return f"- {name}: (file: {path})"


def token_cost(text: str, chars_per_token: int) -> int:
    return math.ceil(len(text.encode("utf-8")) / chars_per_token)


def plugin_prefix_for(path: Path) -> str | None:
    parts = path.parts
    if "cache" not in parts or "skills" not in parts:
        return None
    cache_index = parts.index("cache")
    skills_index = len(parts) - 1 - list(reversed(parts)).index("skills")
    if skills_index <= cache_index + 1:
        return None
    maybe_plugin = parts[cache_index + 2] if len(parts) > cache_index + 2 else None
    if not maybe_plugin:
        return None
    if maybe_plugin.startswith("plugin-install-"):
        return maybe_plugin
    return maybe_plugin


def walk_skill_files(root: Path, max_depth: int = 10) -> list[Path]:
    out: list[Path] = []
    seen_dirs: set[Path] = set()

    def walk(directory: Path, depth: int) -> None:
        if depth > max_depth:
            return
        try:
            real_dir = directory.resolve()
        except OSError:
            return
        if real_dir in seen_dirs:
            return
        seen_dirs.add(real_dir)
        try:
            entries = sorted(directory.iterdir(), key=lambda item: item.name)
        except OSError:
            return
        for entry in entries:
            if entry.name in {".git", "node_modules"}:
                continue
            try:
                if entry.is_dir():
                    walk(entry, depth + 1)
                elif entry.is_file() and entry.name == "SKILL.md":
                    out.append(entry)
            except OSError:
                continue

    if root.exists():
        walk(root, 0)
    return out


def discover_skills(roots: list[RootSpec], chars_per_token: int) -> tuple[list[SkillRecord], dict[str, int]]:
    records_by_real_path: dict[str, SkillRecord] = {}
    root_counts: dict[str, int] = {str(root.path): 0 for root in roots}

    for root in roots:
        for path in walk_skill_files(root.path):
            parsed = parse_frontmatter(path)
            if parsed is None:
                continue
            parsed_name, description, body = parsed
            base_name = parsed_name or path.parent.name
            plugin_prefix = plugin_prefix_for(path) if root.kind == "plugin-cache" else None
            name = f"{plugin_prefix}:{base_name}" if plugin_prefix else base_name
            rendered_line = line_for(name, description, path)
            minimum_line = line_for(name, "", path)
            body_key = normalize_words(body)
            body_hash = hashlib.sha1(body_key.encode("utf-8")).hexdigest()[:12] if body_key else "empty"
            try:
                real_path = str(path.resolve())
            except OSError:
                real_path = str(path)
            record = SkillRecord(
                name=name,
                base_name=base_name,
                description=description,
                path=str(path),
                real_path=real_path,
                root=str(root.path),
                root_kind=root.kind,
                root_label=root.label,
                project=root.project,
                desc_chars=len(description),
                line_bytes=len(f"{rendered_line}\n".encode("utf-8")),
                line_tokens=token_cost(f"{rendered_line}\n", chars_per_token),
                minimum_tokens=token_cost(f"{minimum_line}\n", chars_per_token),
                body_hash=body_hash,
                body_key=body_key,
            )
            if real_path not in records_by_real_path:
                records_by_real_path[real_path] = record
                root_counts[str(root.path)] = root_counts.get(str(root.path), 0) + 1

    return sorted(records_by_real_path.values(), key=lambda item: (item.root_kind, item.name, item.path)), root_counts


def find_model_record(value: object, target: str) -> dict[str, object] | None:
    if isinstance(value, list):
        for item in value:
            found = find_model_record(item, target)
            if found:
                return found
        return None
    if not isinstance(value, dict):
        return None
    names = [
        str(value.get(key)).lower()
        for key in ("slug", "id", "model", "name")
        if isinstance(value.get(key), str)
    ]
    if target.lower() in names:
        return value
    for item in value.values():
        found = find_model_record(item, target)
        if found:
            return found
    return None


def model_context(model: str, override_tokens: int | None) -> tuple[int, str, int | None]:
    if override_tokens:
        return override_tokens, "--context-tokens", None

    cache = HOME / ".codex/models_cache.json"
    if cache.exists():
        try:
            data = json.loads(cache.read_text(encoding="utf-8"))
            record = find_model_record(data, model)
            tokens = int(record.get("context_window", 0)) if record else 0
            effective = int(record.get("effective_context_window_percent", 0)) if record else 0
            if tokens > 0:
                return tokens, str(cache), effective if effective > 0 else None
        except (OSError, TypeError, ValueError, json.JSONDecodeError):
            pass

    return DEFAULT_CONTEXT_TOKENS, f"fallback:{DEFAULT_MODEL}", DEFAULT_EFFECTIVE_PERCENT


def budget_summary(
    skills: list[SkillRecord],
    model: str,
    context_tokens_override: int | None,
    budget_percent: float,
    chars_per_token: int,
) -> dict[str, object]:
    context_tokens, context_source, effective_percent = model_context(model, context_tokens_override)
    budget_tokens = math.floor(context_tokens * (budget_percent / 100))
    effective_context_tokens = (
        math.floor(context_tokens * (effective_percent / 100)) if effective_percent else None
    )
    effective_budget_tokens = (
        math.floor(effective_context_tokens * (budget_percent / 100)) if effective_context_tokens else None
    )
    full_tokens = sum(skill.line_tokens for skill in skills)
    minimum_tokens = sum(skill.minimum_tokens for skill in skills)

    if full_tokens <= budget_tokens:
        budgeted_tokens = full_tokens
        included = len(skills)
        omitted = 0
        truncated_chars = 0
        truncated_count = 0
    elif minimum_tokens <= budget_tokens:
        budgeted_tokens = budget_tokens
        included = len(skills)
        omitted = 0
        description_budget = budget_tokens - minimum_tokens
        description_tokens_used = 0
        truncated_chars = 0
        truncated_count = 0
        for skill in skills:
            description_tokens = max(0, skill.line_tokens - skill.minimum_tokens)
            if description_tokens == 0:
                continue
            remaining_tokens = max(0, description_budget - description_tokens_used)
            if description_tokens <= remaining_tokens:
                description_tokens_used += description_tokens
                continue
            included_chars = min(skill.desc_chars, remaining_tokens * chars_per_token)
            truncated = max(0, skill.desc_chars - included_chars)
            if truncated > 0:
                truncated_chars += truncated
                truncated_count += 1
            description_tokens_used = description_budget
    else:
        budgeted_tokens = 0
        included = 0
        for skill in skills:
            if budgeted_tokens + skill.minimum_tokens > budget_tokens:
                break
            budgeted_tokens += skill.minimum_tokens
            included += 1
        omitted = len(skills) - included
        truncated_chars = sum(skill.desc_chars for skill in skills)
        truncated_count = sum(1 for skill in skills if skill.desc_chars > 0)

    return {
        "model": model,
        "context_tokens": context_tokens,
        "context_source": context_source,
        "effective_percent": effective_percent,
        "effective_context_tokens": effective_context_tokens,
        "budget_percent": budget_percent,
        "budget_tokens": budget_tokens,
        "effective_budget_tokens": effective_budget_tokens,
        "full_tokens": full_tokens,
        "minimum_tokens": minimum_tokens,
        "budgeted_tokens": budgeted_tokens,
        "included_skills": included,
        "omitted_skills": omitted,
        "truncated_description_chars": truncated_chars,
        "truncated_description_count": truncated_count,
        "used_of_budget": full_tokens / budget_tokens if budget_tokens else 0,
        "budgeted_used_of_budget": budgeted_tokens / budget_tokens if budget_tokens else 0,
    }


def recent_log_files(months: int, deep_logs: bool) -> list[Path]:
    cutoff = time.time() - max(0, months) * 31 * 24 * 60 * 60
    files: list[Path] = []
    history = HOME / ".codex/history.jsonl"
    if history.exists():
        files.append(history)

    roots = [HOME / ".codex/sessions"]
    if deep_logs:
        roots.extend([HOME / ".codex/archived_sessions", HOME / ".openclaw", HOME / ".clawd"])

    for root in roots:
        if not root.exists():
            continue
        for directory, dirnames, filenames in os.walk(root):
            directory_path = Path(directory)
            try:
                if directory_path != root and directory_path.stat().st_mtime < cutoff:
                    dirnames[:] = []
                    continue
            except OSError:
                continue
            for filename in filenames:
                if not (filename.endswith(".jsonl") or filename.endswith(".log")):
                    continue
                file_path = directory_path / filename
                try:
                    if file_path.stat().st_mtime >= cutoff:
                        files.append(file_path)
                except OSError:
                    continue

    def modified_at(path: Path) -> float:
        try:
            return path.stat().st_mtime
        except OSError:
            return 0

    return sorted(files, key=lambda path: (-modified_at(path), str(path)))


def count_tokens(values: Iterable[str]) -> Counter[str]:
    return Counter(value.lower() for value in values if value)


SKILL_PATH_RE = re.compile(r"(?:^|[/\"'`\\])(?:\.agents/)?skills/([^/\"'`\\\s]+)/SKILL\.md")
PATH_READ_CONTEXT_RE = re.compile(r"\b(cat|find|grep|head|less|nl|open|read|rg|sed|tail|view)\b", re.I)


def count_skill_file_reads(text: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    for line in text.splitlines():
        if "(file:" in line or not PATH_READ_CONTEXT_RE.search(line):
            continue
        counts.update(value.lower() for value in SKILL_PATH_RE.findall(line) if value)
    return counts


def scan_usage(skills: list[SkillRecord], months: int, deep_logs: bool, max_log_mb: int) -> tuple[dict[str, Usage], int]:
    usage: dict[str, Usage] = {skill.name: Usage() for skill in skills}
    aliases: dict[str, set[str]] = {}
    for skill in skills:
        aliases[skill.name] = {
            skill.name.lower(),
            skill.base_name.lower(),
            skill.name.split(":")[-1].lower(),
        }

    consumed = 0
    max_bytes = max_log_mb * 1024 * 1024
    files = recent_log_files(months, deep_logs)

    processed = 0
    for file_path in files:
        try:
            stat = file_path.stat()
            if stat.st_size > 150 * 1024 * 1024:
                continue
            if consumed + stat.st_size > max_bytes:
                break
            text = file_path.read_text(encoding="utf-8", errors="ignore")
            consumed += stat.st_size
            processed += 1
        except OSError:
            continue

        dollar_counts = count_tokens(re.findall(r"\$([A-Za-z][A-Za-z0-9_.:-]{1,80})", text))
        path_counts = count_skill_file_reads(text)
        text_counts = count_tokens(
            re.findall(r"\b(?:use|using|load|read)\s+`?\$?([A-Za-z][A-Za-z0-9_.:-]{1,80})`?", text, re.I)
        )

        for name, candidates in aliases.items():
            item = usage[name]
            for candidate in candidates:
                item.dollar += dollar_counts[candidate]
                item.file_read += path_counts[candidate]
                item.text += text_counts[candidate]

    return usage, processed


def root_specs_active(extra_roots: list[str]) -> list[RootSpec]:
    roots = [
        RootSpec(HOME / ".codex/skills", "codex-user", "Codex user/global skills", "codex-user", "likely loaded when enabled"),
        RootSpec(HOME / ".codex/plugins/cache", "plugin-cache", "Codex plugin cache", "plugin-cache", "cache inventory; loaded subset unknown"),
        RootSpec(ROOT / ".agents/skills", "current-checkout", "Current Conductor checkout skills", "conductor", "likely loaded for this checkout"),
    ]
    for raw in extra_roots:
        roots.append(RootSpec(expand_home(raw), "extra", f"extra root {raw}", "extra", "caller supplied"))
    return roots


def root_specs_portfolio(extra_roots: list[str]) -> list[RootSpec]:
    roots = [
        RootSpec(ROOT / ".agents/skills", "tracked-repo", "Conductor current checkout skills", "conductor", "inventory only"),
    ]
    for project in methodology_graph.parse_projects_yaml():
        key = str(project.get("key") or project.get("name") or "unknown")
        path = Path(str(project.get("path") or ""))
        if path:
            roots.append(RootSpec(path / ".agents/skills", "tracked-repo", f"{key} repo skills", key, "inventory only"))
    for raw in extra_roots:
        roots.append(RootSpec(expand_home(raw), "extra", f"extra root {raw}", "extra", "caller supplied"))
    return roots


def group_by(skills: list[SkillRecord], key: str) -> list[tuple[str, list[SkillRecord]]]:
    groups: dict[str, list[SkillRecord]] = defaultdict(list)
    for skill in skills:
        groups[getattr(skill, key)].append(skill)
    return sorted(
        ((name, items) for name, items in groups.items() if name != "empty" and len(items) > 1),
        key=lambda item: (-len(item[1]), item[0]),
    )


def analyze_mode(name: str, roots: list[RootSpec], args: argparse.Namespace) -> dict[str, object]:
    skills, root_counts = discover_skills(roots, args.chars_per_token)
    usage, log_count = ({skill.name: Usage() for skill in skills}, 0)
    if not args.no_logs:
        usage, log_count = scan_usage(skills, args.months, args.deep_logs, args.max_log_mb)

    duplicate_names = group_by(skills, "base_name")
    duplicate_bodies = group_by(skills, "body_hash")
    plugin_cache_candidates = [
        skill
        for skill in skills
        if skill.root_kind == "plugin-cache"
        and ("plugin-install-" in skill.path or "plugin-backup-" in skill.path)
    ]
    long_descriptions = sorted(
        [skill for skill in skills if skill.desc_chars >= args.long_description_chars],
        key=lambda skill: (-skill.desc_chars, skill.name, skill.path),
    )
    low_usage = sorted(
        [
            skill
            for skill in skills
            if skill.root_kind not in {"plugin-cache", "codex-user"}
            and usage.get(skill.name, Usage()).total == 0
        ],
        key=lambda skill: (skill.root_kind, skill.project, skill.name, skill.path),
    )

    return {
        "mode": name,
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "root_specs": [asdict(root) | {"path": str(root.path)} for root in roots],
        "root_counts": root_counts,
        "skill_count": len(skills),
        "description_chars": sum(skill.desc_chars for skill in skills),
        "budget": budget_summary(skills, args.model, args.context_tokens, args.budget_percent, args.chars_per_token),
        "log_files_scanned": log_count,
        "skills": skills,
        "usage": usage,
        "duplicate_names": duplicate_names,
        "duplicate_bodies": duplicate_bodies,
        "plugin_cache_candidates": plugin_cache_candidates,
        "long_descriptions": long_descriptions,
        "low_usage": low_usage,
    }


def fmt_int(value: object) -> str:
    return f"{int(value):,}"


def fmt_pct(value: object) -> str:
    return f"{float(value) * 100:.1f}%"


def cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_table(headers: list[str], rows: list[list[object]]) -> list[str]:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(cell(item) for item in row) + " |")
    return lines


def usage_text(usage: Usage) -> str:
    return f"${usage.dollar}, reads={usage.file_read}, text={usage.text}"


def render_mode(analysis: dict[str, object], limit: int) -> list[str]:
    mode = str(analysis["mode"])
    skills: list[SkillRecord] = analysis["skills"]  # type: ignore[assignment]
    roots: list[dict[str, object]] = analysis["root_specs"]  # type: ignore[assignment]
    root_counts: dict[str, int] = analysis["root_counts"]  # type: ignore[assignment]
    budget: dict[str, object] = analysis["budget"]  # type: ignore[assignment]
    usage: dict[str, Usage] = analysis["usage"]  # type: ignore[assignment]

    lines = [
        f"## {mode.title()} Mode",
        "",
        f"- skills discovered: {len(skills)}",
        f"- description chars: {fmt_int(analysis['description_chars'])}",
        f"- log files read: {fmt_int(analysis['log_files_scanned'])}",
        "",
        "### Budget",
        "",
    ]
    lines.extend(
        render_table(
            ["Metric", "Value"],
            [
                ["model", budget["model"]],
                ["context tokens", fmt_int(budget["context_tokens"])],
                ["context source", budget["context_source"]],
                [f"{budget['budget_percent']}% budget tokens", fmt_int(budget["budget_tokens"])],
                ["full rendered skill tokens", fmt_int(budget["full_tokens"])],
                ["minimum no-description tokens", fmt_int(budget["minimum_tokens"])],
                ["budgeted tokens used", fmt_int(budget["budgeted_tokens"])],
                ["full used of budget", fmt_pct(budget["used_of_budget"])],
                ["included skills after budget", fmt_int(budget["included_skills"])],
                ["omitted skills after budget", fmt_int(budget["omitted_skills"])],
                ["truncated description chars", fmt_int(budget["truncated_description_chars"])],
            ],
        )
    )

    lines.extend(["", "### Root Summary", ""])
    lines.extend(
        render_table(
            ["Root", "Kind", "Project", "Skills", "Confidence"],
            [
                [rel(str(root["path"])), root["kind"], root["project"], root_counts.get(str(root["path"]), 0), root["confidence"]]
                for root in roots
            ],
        )
    )

    plugin_candidates: list[SkillRecord] = analysis["plugin_cache_candidates"]  # type: ignore[assignment]
    lines.extend(["", "### Plugin Cache Cleanup Candidates", ""])
    if plugin_candidates:
        lines.extend(
            render_table(
                ["Skill", "Disposition", "Path"],
                [
                    [
                        skill.name,
                        "delete candidate after verifying cache/rollback needs",
                        rel(skill.path),
                    ]
                    for skill in plugin_candidates[:limit]
                ],
            )
        )
    else:
        lines.append("- none")

    duplicate_names: list[tuple[str, list[SkillRecord]]] = analysis["duplicate_names"]  # type: ignore[assignment]
    repo_name_groups = [
        (name, group)
        for name, group in duplicate_names
        if sum(1 for skill in group if skill.root_kind in {"tracked-repo", "current-checkout"}) > 1
    ]
    lines.extend(["", "### Repeated Repo-Local Skill Names", ""])
    if repo_name_groups:
        rows: list[list[object]] = []
        for name, group in repo_name_groups[:limit]:
            projects = ", ".join(sorted({skill.project for skill in group}))
            rows.append([name, len(group), projects, "keep by default; alignment review only"])
        lines.extend(render_table(["Skill", "Copies", "Projects", "Disposition"], rows))
    else:
        lines.append("- none")

    duplicate_bodies: list[tuple[str, list[SkillRecord]]] = analysis["duplicate_bodies"]  # type: ignore[assignment]
    lines.extend(["", "### Duplicate Body Hashes", ""])
    if duplicate_bodies:
        rows = []
        for body_hash, group in duplicate_bodies[:limit]:
            projects = ", ".join(sorted({skill.project for skill in group}))
            names = ", ".join(sorted({skill.base_name for skill in group})[:5])
            rows.append([body_hash, len(group), names, projects, "review only; identical body is not deletion proof"])
        lines.extend(render_table(["Body Hash", "Copies", "Names", "Projects", "Disposition"], rows))
    else:
        lines.append("- none")

    long_descriptions: list[SkillRecord] = analysis["long_descriptions"]  # type: ignore[assignment]
    lines.extend(["", "### Long Description Candidates", ""])
    if long_descriptions:
        lines.extend(
            render_table(
                ["Skill", "Chars", "Project", "Disposition", "Path"],
                [
                    [
                        skill.name,
                        skill.desc_chars,
                        skill.project,
                        "shorten candidate; preserve trigger nouns",
                        rel(skill.path),
                    ]
                    for skill in long_descriptions[:limit]
                ],
            )
        )
    else:
        lines.append("- none")

    low_usage: list[SkillRecord] = analysis["low_usage"]  # type: ignore[assignment]
    lines.extend(["", "### Low Usage Evidence Candidates", ""])
    if int(analysis["log_files_scanned"]) == 0:
        lines.append("- skipped because log scanning was disabled")
    elif low_usage:
        lines.extend(
            render_table(
                ["Skill", "Usage Evidence", "Project", "Disposition", "Path"],
                [
                    [
                        skill.name,
                        usage_text(usage.get(skill.name, Usage())),
                        skill.project,
                        "no action without workflow evidence",
                        rel(skill.path),
                    ]
                    for skill in low_usage[:limit]
                ],
            )
        )
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "### Caveats",
            "",
            "- This audit is report-only and does not modify skill files.",
            "- Plugin cache contents are not proof that every listed skill is model-visible.",
            "- Path-read usage evidence excludes rendered prompt inventory lines.",
            "- Low usage evidence is heuristic; implicit trigger selection and path-local workflows may not appear in logs.",
            "- Repeated repo-local skills usually reflect distributed ownership, not accidental duplication.",
        ]
    )
    return lines


def render_markdown(analyses: list[dict[str, object]], limit: int) -> str:
    lines = [
        "# Skill Surface Audit",
        "",
        f"Generated: {time.strftime('%Y-%m-%dT%H:%M:%S%z')}",
        f"Workspace: `{ROOT}`",
        "",
        "This is a report-only audit. Treat every cleanup item as a candidate for",
        "review, not permission to delete or rewrite skills.",
        "",
    ]
    for analysis in analyses:
        lines.extend(render_mode(analysis, limit))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def json_ready(analysis: dict[str, object]) -> dict[str, object]:
    out = dict(analysis)
    out["skills"] = [asdict(skill) for skill in analysis["skills"]]  # type: ignore[index]
    out["usage"] = {name: asdict(item) for name, item in analysis["usage"].items()}  # type: ignore[index,union-attr]
    for key in ("duplicate_names", "duplicate_bodies"):
        out[key] = [
            {"key": group_key, "skills": [skill.path for skill in group]}
            for group_key, group in analysis[key]  # type: ignore[index]
        ]
    for key in ("plugin_cache_candidates", "long_descriptions", "low_usage"):
        out[key] = [asdict(skill) for skill in analysis[key]]  # type: ignore[index]
    return out


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["active", "portfolio", "all"], default="all")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--output", help="Write the report to this path instead of stdout")
    parser.add_argument("--root", action="append", default=[], help="Additional skill root to include")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--context-tokens", type=int)
    parser.add_argument("--budget-percent", type=float, default=2)
    parser.add_argument("--chars-per-token", type=int, default=4)
    parser.add_argument("--months", type=int, default=3)
    parser.add_argument("--max-log-mb", type=int, default=300)
    parser.add_argument("--deep-logs", action="store_true")
    parser.add_argument("--no-logs", action="store_true")
    parser.add_argument("--long-description-chars", type=int, default=300)
    parser.add_argument("--limit", type=int, default=20)
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    analyses: list[dict[str, object]] = []
    if args.mode in {"active", "all"}:
        analyses.append(analyze_mode("active", root_specs_active(args.root), args))
    if args.mode in {"portfolio", "all"}:
        analyses.append(analyze_mode("portfolio", root_specs_portfolio(args.root), args))

    if args.format == "json":
        output = json.dumps({"analyses": [json_ready(analysis) for analysis in analyses]}, indent=2)
    else:
        output = render_markdown(analyses, args.limit)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
