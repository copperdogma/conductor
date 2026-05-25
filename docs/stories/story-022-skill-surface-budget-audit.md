---
title: "Build Skill Surface Budget Audit"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I4"
  - "I5"
spec_refs:
  - "spec:1.1"
  - "spec:2.1"
  - "spec:2.2"
  - "spec:3.2"
  - "spec:4.2"
  - "spec:5.1"
  - "spec:5.2"
  - "spec:5.3"
decision_refs:
  - "ADR-001"
  - "ADR-002"
depends_on: []
category_refs:
  - "alignment"
  - "scouting"
  - "story-prep"
  - "memory"
tracked_projects:
  - "conductor"
  - "dossier"
  - "storybook"
  - "doc-web"
  - "cine-forge"
  - "boardgame-ingester"
  - "roborally"
  - "echo-forge"
---

# Story 022 — Build Skill Surface Budget Audit

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: None

## Goal

Turn Scout 041's `skill-cleaner` finding into a Conductor-owned,
report-only skill-surface audit.

The useful local value is not automatic cleanup. The useful value is a cheap
way to see when skill descriptions, duplicate cache entries, repeated
repo-local skills, or stale roots are consuming model-visible context or
creating wrong-skill risk.

This story should build the smallest useful audit wrapper around the idea. It
must read the tracked project registry, distinguish actual loaded/session
skills from broad filesystem inventory, and produce human-reviewable findings
without modifying target repos or deleting skill files.

## Acceptance Criteria

- [x] Conductor has a report-only skill-surface audit entrypoint that can be
      invoked from the repo and uses `projects.yaml` for tracked repo skill
      roots instead of assuming `~/Projects`.
- [x] The audit separates at least two modes:
      - active-session/current-checkout mode for the skills plausibly visible
        to the current Codex session
      - portfolio-inventory mode for comparing tracked repo `.agents/skills`
        roots without pretending they are all loaded into one prompt
- [x] The report clearly distinguishes:
      - model-visible or active roots, when known
      - plugin cache contents
      - tracked repo-local skill roots
      - optional extra roots supplied by the caller
- [x] The report includes skill-budget pressure, duplicate plugin-cache
      candidates, repeated repo-local skill names/bodies, long-description
      candidates, and heuristic usage evidence with confidence caveats.
- [x] The audit outputs recommended dispositions such as `keep`, `shorten`,
      `disable`, `delete candidate`, or `no action`, but performs no edits.
- [x] Repo-local duplicate skills are treated as alignment inventory by
      default, not deletion candidates; intentional distributed ownership is
      preserved unless a concrete local failure mode is found.
- [x] Long-description findings preserve trigger specificity. The audit must
      not auto-rewrite descriptions from generic upstream suggestions.
- [x] The first Conductor run is recorded in a durable alignment or report
      artifact with the practical next actions and rejected cleanup routes.
- [x] No target repo inbox notes or stories are created unless the first run
      finds a high-confidence repo-local cleanup candidate.
- [x] Conductor checks pass for any changed docs, skills, scripts, and
      generated methodology surfaces.

## Out of Scope

- Installing `skill-cleaner` into every tracked repo.
- Deleting, disabling, or rewriting skills automatically.
- Treating plugin-cache filesystem duplicates as proof that Codex actually
  loaded those skills.
- Collapsing distributed repo-local skill copies into one canonical copy.
- Broad target-repo cleanup work before Conductor has a reviewed audit result.
- Adding a recurring maintenance ceremony unless the first report proves a
  lightweight trigger has net value.
- Committing, pushing, or landing target repo changes without an explicit
  closeout request.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Re-read Scout 041 and the upstream `skill-cleaner` skill/script
- [x] Inspect current Codex/plugin/skill loading evidence enough to separate
      active roots from broad cache inventory
- [x] Decide the smallest local implementation shape:
      - [ ] Conductor skill wrapper only
      - [x] helper script plus skill wrapper
      - [ ] docs-only runbook if implementation does not clear the overhead bar
- [x] Implement the report-only audit entrypoint
- [x] Run active-session/current-checkout mode and portfolio-inventory mode
- [x] Record the first run's durable result in alignment or report memory
- [x] Reject or defer low-confidence cleanup findings explicitly
- [x] Update related scout or alignment memory if applicable
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: `make test`
- [x] Search docs and update any related surfaces
- [x] Verify Conductor tenets:
  - [x] I1 — Meaning over text
  - [x] I2 — Distributed ownership
  - [x] I3 — Recommendation-first supervision
  - [x] I4 — Honest divergence
  - [x] I5 — Minimal overhead

## Workflow Gates

- [x] Build complete
- [x] Validation complete or explicitly skipped by user
- [x] Story marked done via `/mark-story-done`

## Files to Modify

- `docs/stories/story-022-skill-surface-budget-audit.md` — story source of
  truth and work log.
- `.agents/skills/` — only if a local audit skill wrapper is justified.
- `scripts/` — only if a helper script is justified by lower maintenance cost
  than shelling directly to the upstream script.
- `docs/alignments/` and `docs/align-projects.md` — likely place for the first
  durable inventory and recommendation.
- `docs/scout/scout-041-skill-cleaner-skill-budget-audit.md` — update only if
  implementation changes the scout recommendation.
- Generated methodology surfaces after compile: `docs/stories.md` and
  `docs/methodology/graph.json`.

## Notes

- Triggered by Scout 041, which evaluated Peter Steinberger's
  `skill-cleaner` skill.
- Local trial evidence showed real pressure: current Conductor-like roots
  modeled 65 enabled skills and exceeded the 2% full-description budget;
  portfolio inventory across tracked repo roots found 274 enabled skills, 52
  duplicate-name groups, 35 duplicate body groups, and 13 plugin
  install/backup copies.
- The upstream script is useful evidence but not a direct fit. It assumes
  different repo roots, scans plugin cache broadly, and produces generic
  description suggestions that would lose important local trigger nouns.
- The adoption bar is the same one from recent Conductor scout work: no extra
  surface unless it removes more recurring work than it adds.

## Plan

1. Add a small repo-local Python helper at `scripts/skill_surface_audit.py`.
   It will parse `SKILL.md` frontmatter directly, read `projects.yaml` for
   tracked repo roots, and render Markdown or JSON reports.
2. Support three modes:
   - `active`: current Conductor checkout, user Codex skills, plugin cache,
     and optional caller-supplied roots
   - `portfolio`: Conductor plus tracked project `.agents/skills` roots only
   - `all`: both modes in one report
3. Keep all findings report-only. The script should classify duplicate
   plugin-cache copies, repeated repo-local names/bodies, long descriptions,
   low usage evidence, and budget pressure, but never edit or delete files.
4. Add `.agents/skills/skill-surface-audit/SKILL.md` as the operator-facing
   wrapper that explains when to run the helper and how to interpret findings.
5. Run the new helper in active and portfolio mode, then record the first
   result in `docs/alignments/align-039-skill-surface-budget-audit.md` and add
   the index entry to `docs/align-projects.md`.
6. Update this story's tasks/work log and regenerate methodology surfaces.
7. Checks: run the audit helper, `make methodology-compile`,
   `make methodology-check`, `make lint`, `make skills-check`, `make test`,
   and `git diff --check`.

## Work Log

20260525-1527 — story-created: created from Scout 041 follow-up approval as a
Conductor-owned, report-only skill-surface audit story. No target repo edits or
automatic cleanup actions made.

20260525-1538 — build-started: read Story 022, Conductor Ideal/spec,
state/graph, ADR-001, ADR-002, Scout 041, current upstream `skill-cleaner`
skill/script excerpts, existing alignment/index patterns, repo checks, and
skill sync rules. Planned a small Python helper plus Conductor skill wrapper,
with first-run evidence recorded in alignment memory. No tracked project repos
will be edited.

20260525-1546 — implemented: added `scripts/skill_surface_audit.py`,
`.agents/skills/skill-surface-audit/SKILL.md`, and Alignment 039. Full helper
run read 36 newest log files under the default byte cap; active mode found 61
skills, 6,015 full rendered tokens against a 5,440-token budget, and 13 plugin
install/backup cache candidate copies; portfolio mode found 246 repo-local
skills, 14,516 full rendered tokens, 39 repeated name groups, and no
high-confidence target repo cleanup lane.

20260525-1551 — checks-passed: ran `python3 -m py_compile
scripts/skill_surface_audit.py`, audit Markdown/JSON smoke commands,
`make methodology-compile`, `make methodology-check`, `make lint`,
`make skills-check`, `make test`, and `git diff --check`. Removed/restored
generated Python bytecode noise after checks.

20260525-1555 — validation-fixed: `codex review --uncommitted` found that the
usage scan sorted logs by pathname before applying the byte cap, overstated log
coverage by returning candidate file count instead of files actually read, and
left generated bytecode in the diff. Fixed the helper to scan newest logs first
and report processed log files only, then removed tracked Python bytecode and
ignored future `__pycache__` / `.pyc` outputs.

20260525-1558 — validation-fixed-2: follow-up `codex review --uncommitted`
found two more report-quality issues: budget truncation overstated how many
description characters were actually over budget, and path-read usage evidence
counted rendered skill inventory paths as usage. Fixed budget truncation to
estimate only overflow description characters, and excluded prompt inventory
lines from path-read evidence.

20260525-1604 — validation-cleaned: final `codex review --uncommitted` found
only the remaining tracked `scripts/__pycache__/methodology_graph.cpython-314.pyc`
artifact. Removed it from the git index and kept `__pycache__` / `.pyc` ignored
so future Python check runs do not dirty the repo.

20260525-1608 — story-closed: marked Story 022 done after build and validation
gates were complete, the audit helper and durable scout/alignment outputs were
present, generated methodology surfaces were refreshed, and checks passed.
