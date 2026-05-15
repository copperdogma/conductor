# Alignment 030 - Validate Codex Review Closeout Signal

**Date**: 2026-05-15
**Focus**: Decide how Peter Steinberger's `codex-review` workflow should affect
Cam's shared `/validate` and `/loop-verify` methodology.

## Source

Primary source: Scout 032, based on Peter Steinberger's May 14, 2026 X post and
the linked `agent-scripts` `codex-review` skill.

Local evidence: `codex review --help` in the current Codex CLI describes a
non-interactive code-review command with `--uncommitted`, `--base`, and
`--commit` target modes.

## Decision Context

- Alignment 022 already decided that review-mode defect discovery improves
  `/validate` but does not replace `/validate`.
- Alignment 029 already hardened `/loop-verify` against recursive workers,
  runaway docs loops, and scope expansion.
- Scout 032 initially looked like a `/loop-verify` enhancement, then Cam
  clarified that `/validate` is the essential closure checkpoint and
  `/loop-verify` must remain useful for any scoped task.

## Classification

Portable improvement with local adaptation.

The behavior that should travel is:

- `/validate` may use `codex review` as an extra signal for non-trivial code
  diffs when it materially improves closeout confidence
- `/validate` remains the closure authority for task/story intent, artifacts,
  checks, generated surfaces, inbox handling, and final disposition
- `codex review` findings are advisory and need an accepted/rejected ledger
- accepted review-triggered code fixes require focused tests/checks and a fresh
  review signal for the changed scope
- `/loop-verify` gains only general finding-disposition and clean-stop
  discipline, not a code-review-only or story-closure meaning

## Recommendation

Roll this out across tracked repos that carry `/validate` and `/loop-verify`.

Keep the rollout narrow:

- update `.agents/skills/validate/SKILL.md`
- update `.agents/skills/loop-verify/SKILL.md`
- regenerate skill wrappers or methodology outputs only where repo-local
  tooling requires it
- validate with repo-native skill/methodology checks and `git diff --check`

Do not import Peter's helper script yet. If the instruction-level behavior
proves useful and repeated manual target selection becomes friction, a later
story can decide whether a small local helper is worth maintaining.

## Stop Conditions

- Do not require `codex review` for docs-only, scout, alignment, inbox routing,
  generated-index, tiny obvious patch, or product/taste validation work.
- Do not treat a clean `codex review --uncommitted` on a clean checkout as proof
  that committed branch work is clean.
- Do not let `/loop-verify` workers spawn subagents, invoke `/loop-verify`, or
  run nested review loops.
- Do not claim target repos have this behavior until isolated target worktrees
  apply and validate it.

## Practical Impact

This gives Cam a stronger "agent thinks it is done" checkpoint for meaningful
code changes without weakening the broader validation contract. The extra
review signal should catch some concrete code defects while `/validate` still
decides whether the actual task is complete.

## Rollout Execution

Story 013 applied the refined behavior in isolated target worktrees, not in
primary checkouts.

Shared rollout settings:

- Worktree root:
  `/Users/cam/.codex/worktrees/validate-codex-review-signal/`
- Branch: `codex/validate-codex-review-signal-20260515`
- Core edits:
  - `.agents/skills/validate/SKILL.md`
  - `.agents/skills/loop-verify/SKILL.md`
- Generated methodology updates where local tooling required them:
  - Storybook: `docs/methodology/graph.json`, `docs/stories.md`
  - CineForge: `docs/build-map.md`, `docs/methodology/graph.json`,
    `docs/stories.md`

Per-repo evidence:

| Project | Base | Checks |
| --- | --- | --- |
| Dossier | `0f22845` | `./scripts/sync-agent-skills.sh --check`, `PYTHONDONTWRITEBYTECODE=1 PYTHON='uv run --frozen python' make methodology-check`, and `git diff --check` passed. Existing legacy/non-local metadata warnings remain unrelated. |
| Storybook | `377bcf6` | `./scripts/sync-agent-skills.sh --check`, `pnpm methodology:compile`, `npm run methodology:check`, and `git diff --check` passed. |
| doc-web | `c0075f5` | `./scripts/sync-agent-skills.sh --check`, `PYTHONDONTWRITEBYTECODE=1 make methodology-check`, and `git diff --check` passed. |
| CineForge | `4bfedb5` | `./scripts/sync-agent-skills.sh --check`, `pnpm methodology:compile`, `npm run methodology:check`, and `git diff --check` passed. Existing architecture-audit and UI-scout freshness warnings remain unrelated. |
| Board Game Ingester | `d00c742` | `./scripts/sync-agent-skills.sh --check`, `PYTHONDONTWRITEBYTECODE=1 make methodology-check`, `PYTHONDONTWRITEBYTECODE=1 make lint`, and `git diff --check` passed. |
| Robo Rally | `e463af7` | `./scripts/sync-agent-skills.sh --check`, `npm run skills:check`, `npm run methodology:check`, and `git diff --check` passed. |
| Echo Forge | `68bfff8` | `./scripts/sync-agent-skills.sh --check`, `npm run methodology:check`, and `git diff --check` passed. Existing `No Ideal requirements parsed` warning remains unrelated. |

Known limits:

- Product test suites were not run because this rollout only changed shared
  agent-skill text and generated methodology surfaces.
- Primary target checkouts were inspected before worktree creation. Storybook,
  CineForge, and Echo Forge had unrelated dirty files; Board Game Ingester was
  on another feature branch. The rollout kept those live workspaces untouched.

Landed target commits:

| Project | Commit |
| --- | --- |
| Dossier | `8babd53` |
| Storybook | `0741e13` |
| doc-web | `8ebe99b` |
| CineForge | `700a429` |
| Board Game Ingester | `c67b2a1` |
| Robo Rally | `7b7006c` |
| Echo Forge | `4dcdb84` |
