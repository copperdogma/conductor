# Alignment 019 — Core Story Loop Subagent Contracts

Date: 2026-04-28

## Focus

Evaluate whether the tracked repos' core story loop skills should adopt the
subagent and verify-loop lessons from Story 005's triage orchestration rollout.

The reviewed skills were:

- `/create-story`
- `/build-story`
- `/validate`
- `/setup-methodology`

## Classification

Portable improvement with local adaptation.

## Decision

All tracked repos benefit from the same behavioral upgrade, but not from exact
text identity in every core story-loop skill.

- `/create-story`: upgrade everywhere with optional sidecar evidence for
  non-trivial story scoping. Sidecars are evidence-only; the main thread keeps
  the story-worthiness decision, story boundary, initial status, and final
  artifact. `/loop-verify` is not the default for story creation.
- `/build-story`: upgrade everywhere with optional delegation only after the
  plan gate. Sidecars may do bounded exploration, disjoint implementation
  slices, tests/evals, artifact inspection, or review of already-written
  changes. The main thread keeps plan approval, integration, final design
  judgment, target-worktree isolation, and validation handoff.
- `/validate`: upgrade everywhere with optional parallel validation packets and
  explicit `/loop-verify` escalation for broad/high-risk diffs, repeated
  material fixes, cross-repo rollouts, or cases where one complete clean round
  matters. The main thread keeps the final disposition and yes-ready next step.
- `/setup-methodology`: make the shared setup skill byte-identical across
  Conductor and the tracked product repos. It now refreshes the accepted
  core-loop guidance and uses repo identity to distinguish product setup from
  Conductor's supervisor package rather than silently forking the skill text.

## Per-Repo Result

| Repo | Result |
| --- | --- |
| Conductor | Upgraded local core story-loop skills and switched setup-methodology to the shared identity-preserving skill with explicit supervisor package behavior. |
| Dossier | Upgraded core story-loop skills and shared setup-methodology in the isolated worktree. |
| Storybook | Upgraded core story-loop skills and shared setup-methodology in the isolated worktree. |
| doc-web | Upgraded core story-loop skills and shared setup-methodology in the isolated worktree. |
| CineForge | Upgraded core story-loop skills and shared setup-methodology in the isolated worktree. |
| Board Game Ingester | Upgraded core story-loop skills and shared setup-methodology in the isolated worktree. |
| Robo Rally | Upgraded core story-loop skills and shared setup-methodology in the isolated worktree. |
| Echo Forge | Upgraded core story-loop skills and shared setup-methodology in the isolated worktree. |

## Implementation Worktrees

Target repos were edited in isolated worktrees under:

`/Users/cam/.codex/worktrees/story006-core-loop/`

Branch:

`codex/story-006-core-loop-subagent-contracts`

Conductor was edited on:

`codex/story-006-core-loop-subagent-contract-review`

## Loop Verification

Ran `/loop-verify` over four disjoint shards:

- `create-story`
- `build-story`
- `validate`
- `setup-methodology`

Round 1 found material missing-contract issues in all four shards and fixed
them. Round 2 found a material generated-surface issue in setup wrappers and a
material missing sequential-fallback issue in validate, then fixed both. Round
3 returned clean across the full original scope.

Material fixes that reset the loop:

- added optional sidecar evidence to `/create-story`
- added post-plan delegation to `/build-story`
- added parallel validation and `/loop-verify` escalation to `/validate`
- made `/setup-methodology` install/refresh the accepted core story-loop
  guidance and kept the file byte-identical across all eight repos
- regenerated stale setup-methodology wrappers in the seven target worktrees
- added the missing validate fallback for unavailable/unsafe/disabled subagents

## Validation

Checks that passed:

- Conductor: `make methodology-compile`, `make methodology-check`,
  `make skills-check`, `make lint`, `make test`, `git diff --check`
- Dossier: `./scripts/sync-agent-skills.sh --check`,
  `PYTHON='uv run --frozen python' make methodology-check`, `git diff --check`
- Storybook: `./scripts/sync-agent-skills.sh --check`,
  `npm run methodology:check`, `npm run methodology:test`,
  `npm run triage:facts:check`, `npm run lint`, `git diff --check`
- doc-web: `make skills-check`, `make methodology-check`, `make lint`,
  `git diff --check`
- CineForge: `make skills-check`, `npm run methodology:check`,
  `git diff --check`
- Board Game Ingester: `make skills-check`, `make methodology-check`,
  `make lint`, `git diff --check`
- Robo Rally: `npm run validate`, `git diff --check`
- Echo Forge: `npm run skills:check`, `npm run methodology:check`,
  `npm run lint`, `npm run triage-facts:check`, `git diff --check`

Known validation limits:

- Dossier broad lint still reports unrelated existing Ruff findings outside
  this rollout; scoped diff and methodology checks passed.
- CineForge broad lint still reports unrelated existing Ruff findings outside
  this rollout; skill wrapper, methodology, and diff checks passed.
- CineForge methodology check still reports its existing architecture/UI
  freshness warnings.
- Storybook and Echo Forge isolated worktrees used temporary symlinks to the
  primary checkout `node_modules` for lint/test commands; the symlinks were
  removed afterward.

## Follow-Up

This alignment records the decision and implementation evidence only. Landing
the target worktrees onto each repo's `main` branch should happen through the
normal `/validate` and `/finish-and-push` flow for Story 006.
