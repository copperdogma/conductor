# Alignment 029 - Loop Verify Runaway Controls

**Date**: 2026-05-12
**Focus**: Refine `/loop-verify` after Echo Forge exposed a repeated runaway
loop failure in docs/ADR alignment work.

## Source

Primary source: Cam's Conductor inbox report from Echo Forge AI, confirmed by
Cam firsthand.

The report identified seven failure contributors:

- the skill discouraged any fixed budget and normalized many rounds
- workers defaulted to fix-capable behavior even for tightly coupled docs
- materiality was broad enough that many wording changes reset the loop
- the worker prompt said to use `$loop-verify` inside the shard
- the stop condition did not distinguish expansion work from in-scope defects
- the orchestration scope widened across ADRs, spec, state, stories, and outputs
- stale subagent summaries made coordinator state noisy

## Decision Context

- ADR-001 applies: Conductor should align workflow meaning, not create a
  canonical central skill core.
- ADR-002 applies: this is a proven recurring methodology issue, so it deserves
  a portable skill refinement rather than ad hoc chat memory.
- Alignment 011 established `/loop-verify` as portable and useful across tracked
  repos.
- Alignment 019 kept main-thread judgment central when subagents gather
  evidence.
- Alignment 025 already fixed a related runaway class: upstream-owned issues and
  risk-sized worker models. It did not address recursion, budgets, docs/ADR
  mode, or expansion gates.

## Classification

Portable improvement with local adaptation.

The no-recursion rule, default budget, docs/ADR find-only mode, narrowed
documentation materiality, stale-agent hygiene, and expansion gate are portable
because all tracked repos can hit the same failure mode when validating
methodology docs.

The exact wording can remain local. The behavior that must travel is:

- coordinator selects `budgeted`, `docs/ADR alignment`, or `strict-until-clean`
  mode before worker launch
- worker prompts forbid recursive `/loop-verify`, spawning subagents, widening
  scope, or starting another round
- docs/ADR alignment defaults to find-only workers and main-agent fixes
- ordinary loops stop at the default budget and ask for explicit continuation
- strict clean-round loops are reserved for explicit approval or objective
  contract-critical surfaces
- expansion findings become follow-up routes instead of silent scope widening

## Recommendation

Adopt the refined loop contract across tracked repos that already carry
`/loop-verify`.

Rollout should be narrow:

- update `.agents/skills/loop-verify/SKILL.md`
- update shared setup-methodology wording only where it still teaches the old
  no-budget loop behavior
- regenerate skill wrappers or methodology surfaces only when local tooling
  requires it
- validate with repo-native skill/methodology checks and `git diff --check`

Do not broaden this into provider/model selection, eval policy, target-product
stories, or unrelated documentation cleanup.

## Stop Conditions

- Do not claim target repos have this behavior until isolated target worktrees
  apply and validate it.
- Do not run `/loop-verify` to validate this `/loop-verify` correction; that
  would exercise the unsafe path this alignment is removing.
- Do not delete strict clean-round behavior. It remains useful for objective,
  bounded, contract-critical work when Cam explicitly wants that proof.

## Practical Impact

This reduces the chance that a docs or ADR verification pass burns hours
rediscovering adjacent alignment work. It keeps the valuable clean-round proof
for code, schemas, evals, generated outputs, and other objective contracts where
the extra verification is worth the cost.

## Rollout Execution

Story 012 applied the refined behavior in isolated target worktrees, not in
primary checkouts.

Shared rollout settings:

- Worktree root:
  `/Users/cam/.codex/worktrees/loop-verify-runaway-controls/`
- Branch: `codex/loop-verify-runaway-controls`
- Core edits:
  - `.agents/skills/loop-verify/SKILL.md`
  - `.agents/skills/setup-methodology/SKILL.md`
  - generated Gemini wrapper for `/loop-verify`
- Generated methodology updates where local tooling required them:
  - Storybook: `docs/methodology/graph.json`, `docs/stories.md`
  - CineForge: `docs/build-map.md`, `docs/methodology/graph.json`,
    `docs/stories.md`

Per-repo evidence:

| Project | Base | Checks |
| --- | --- | --- |
| Dossier | `834fbc7` | `./scripts/sync-agent-skills.sh --check`, `PYTHON=/Users/cam/Documents/Projects/dossier/.venv/bin/python make methodology-check`, and `git diff --check` passed. |
| Storybook | `1d9a877` | `bash scripts/sync-agent-skills.sh --check`, `npm run methodology:compile`, `npm run methodology:check`, and `git diff --check` passed. |
| doc-web | `020e8ac` | `make skills-check`, `make methodology-check`, and `git diff --check` passed. |
| CineForge | `77cea10` | `make skills-check`, `npm run methodology:compile`, `npm run methodology:check`, and `git diff --check` passed. Methodology check still reports existing architecture-audit and UI-scout freshness warnings. |
| Board Game Ingester | `2c0a4fb` | `make skills-check`, `make methodology-check`, and `git diff --check` passed. |
| Robo Rally | `3d99c80` | `npm run skills:check`, `npm run methodology:check`, and `git diff --check` passed. |
| Echo Forge | `46b93d4` | `npm run skills:check`, `npm run methodology:check`, and `git diff --check` passed. |

Known limits:

- Dependency-heavy full test suites were not run in the isolated target
  worktrees because this rollout only changed shared agent-skill text and
  generated wrappers/methodology surfaces.
- Primary target checkouts were inspected before worktree creation. Storybook,
  CineForge, and Echo Forge had unrelated dirty files; Board Game Ingester was
  on another feature branch. The rollout kept those live workspaces untouched.
