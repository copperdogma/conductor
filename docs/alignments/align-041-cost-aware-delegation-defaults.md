# Alignment 041 - Cost-Aware Delegation Defaults

**Date**: 2026-06-10
**Classification**: Portable improvement with local adaptation
**Source**: User request in Conductor
**Projects Reviewed**: Conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Focus

Add guidance that lets agents conserve model use during delegated work without
turning individual skills into hard-coded model selectors.

The requested behavior is:

- do not name exact models in repo or skill instructions
- let the calling model decide the lowest sufficient model strength and
  reasoning level for each delegated shard
- keep final judgment with the main thread
- scope delegation only to skills and packets where it is already safe

## Decision

Use a hybrid policy.

`AGENTS.md` owns the general rule: when delegation is explicitly authorized,
choose the lowest model strength and reasoning level that can honestly handle
the delegated shard. The repo guidance must not name, hard-code, or prefer a
specific model because the available model surface can change.

Skill files own the authorization boundary. A skill must still say whether
delegation is appropriate, which packets can be delegated, and which decisions
remain with the coordinator. This prevents a broad repo-level instruction from
being misread as permission to spawn workers inside every skill.

## Local Patch

Patched Conductor surfaces:

- `AGENTS.md`: added the cost-aware delegation default and coordinator-owned
  judgment boundary
- `.agents/skills/loop-verify/SKILL.md`: replaced "cheapest model" wording
  with lowest sufficient model strength/reasoning and explicitly forbids
  hard-coded model names
- `.agents/skills/validate/SKILL.md`: allows low-strength sidecars for
  mechanical validation packets while keeping final disposition in the main
  thread
- `.agents/skills/check-in/SKILL.md`: allows mechanical preflight sidecars for
  large or messy closeouts, but reserves staging, committing, pushing, and
  integration judgment for the main thread
- `.agents/skills/finish-and-push/SKILL.md`: inherits leaf-skill sidecar
  boundaries and keeps closeout/landing/deploy/rollback judgment centralized
- `.agents/skills/skill-surface-audit/SKILL.md`: allows report-only sidecars
  over disjoint scan roots while forbidding edits or cleanup from workers

## Eligible Sidecar Work

Good candidates:

- command execution and result collection
- git, diff, and changed-file inventories
- generated-file freshness checks
- link, alias, and wrapper consistency scans
- log and health evidence collection
- narrow docs consistency scans
- report-only skill-surface inventory shards

The coordinator keeps:

- scope decisions
- semantic or product judgment
- security and trust-boundary judgment
- eval correctness
- architecture calls
- staging, commits, pushes, deploy decisions, and rollback decisions
- final synthesis and user-facing recommendation

## Guardrails

- Do not delegate tiny tasks where setup cost likely exceeds the work.
- Do not treat a repo-level delegation policy as automatic authorization inside
  every skill.
- Do not name exact models in repo-local guidance.
- Do not let workers spawn workers, invoke `/loop-verify`, or widen their
  assignment.
- Record a short rationale when downshifting a delegated shard.
- Treat worker output as evidence, not truth.

## Target Rollout Evidence

Story 026 prepared the target-project rollout in isolated worktrees under:

`/Users/cam/.codex/worktrees/cost-aware-delegation-rollout/`

Branch in each target repo:

`codex/cost-aware-delegation-rollout`

No target primary checkout was edited. No commits or pushes were made.

| Project | Worktree | Patched surfaces | Validation |
| --- | --- | --- | --- |
| Dossier | `/Users/cam/.codex/worktrees/cost-aware-delegation-rollout/dossier` | `AGENTS.md`, `loop-verify`, `validate` | `scripts/sync-agent-skills.sh`; `make skills-check`; `PYTHON=/Users/cam/Documents/Projects/dossier/.venv/bin/python make methodology-check`; `git diff --check` passed. Methodology check retained existing non-local ADR/legacy metadata warnings. |
| Storybook | `/Users/cam/.codex/worktrees/cost-aware-delegation-rollout/storybook` | `AGENTS.md`, `loop-verify`, `validate`, regenerated `docs/methodology/graph.json` and `docs/stories.md` | `scripts/sync-agent-skills.sh`; `scripts/sync-agent-skills.sh --check`; `pnpm methodology:compile`; `pnpm methodology:check`; `git diff --check` passed. Generated diff only advanced UI-scout freshness from 23 to 24 days. |
| doc-web | `/Users/cam/.codex/worktrees/cost-aware-delegation-rollout/doc-web` | `AGENTS.md`, `loop-verify`, `validate` | `scripts/sync-agent-skills.sh`; `make skills-check`; `make methodology-check`; `git diff --check` passed. |
| CineForge | `/Users/cam/.codex/worktrees/cost-aware-delegation-rollout/cine-forge` | `AGENTS.md`, `loop-verify`, `validate`, regenerated `docs/build-map.md`, `docs/methodology/graph.json`, and `docs/stories.md` | `scripts/sync-agent-skills.sh`; `make skills-check`; `npm run methodology:compile`; `npm run methodology:check`; `git diff --check` passed. Existing architecture-audit and UI-scout freshness warnings remain unrelated. Build-map generation uses UTC dates, so `2026-06-11` is expected while local shell time is still `2026-06-10 MDT`. |
| Board Game Ingester | `/Users/cam/.codex/worktrees/cost-aware-delegation-rollout/boardgame-ingester` | `AGENTS.md`, `loop-verify`, `validate` | `scripts/sync-agent-skills.sh`; `make skills-check`; `make methodology-check`; `git diff --check` passed. |
| RoboRally | `/Users/cam/.codex/worktrees/cost-aware-delegation-rollout/roborally` | `AGENTS.md`, `loop-verify`, `validate` | `scripts/sync-agent-skills.sh`; `npm run skills:check`; `npm run methodology:check`; `git diff --check` passed. |
| Echo Forge | `/Users/cam/.codex/worktrees/cost-aware-delegation-rollout/echo-forge` | `AGENTS.md`, `loop-verify`, `validate` | `scripts/sync-agent-skills.sh`; `npm run skills:check`; `npm run methodology:check`; `git diff --check` passed. Existing `No Ideal requirements parsed` warning remains unrelated. |

## Loop Verification

The rollout used `/loop-verify` in docs/ADR alignment mode:

- Round 1 was find-only target-surface discovery across three repo groups.
  Accepted findings: Dossier, Storybook, doc-web, and CineForge had exact
  model-name subagent strategy tables in root `AGENTS.md`. Rejected as blockers:
  missing `check-in`, `deploy`, or `skill-surface-audit` skills where the repo
  simply does not carry those surfaces.
- Main-agent fixes replaced exact model tables with model-name-free
  cost-aware delegation policy, added root policy where missing, and normalized
  `loop-verify` and `validate` wording across all seven target repos.
- Round 2 inspected the patched diffs. Dossier/Storybook and
  Board Game Ingester/RoboRally/Echo Forge returned clean. doc-web returned
  clean. CineForge reported the UTC build-map stamp as a possible issue; the
  finding was rejected because the generator intentionally uses
  `new Date().toISOString().slice(0, 10)`.

## Rollout Boundary

Target-project sync is prepared but not landed. Each repo has its own isolated
worktree and validation evidence, but the changes are not complete on target
`main` branches until the branches are committed, pushed, and landed through
the normal closeout flow.

## Practical Impact

Cam gets a lower-overhead default for mechanical delegated work without losing
the safety property that the main thread owns judgment and irreversible
actions. The policy should reduce wasted high-strength model use on inventory
and evidence-gathering while avoiding hard-coded model names that would go
stale.
