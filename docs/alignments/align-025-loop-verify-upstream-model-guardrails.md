# Alignment 025 — Loop Verify Upstream and Model-Sizing Guardrails

**Date**: 2026-05-11
**Focus**: Route the inbox note about an expensive Storybook `/loop-verify`
run that chased issues ultimately owned by Dossier/doc-web, and decide the
smallest supervisor change that reduces that failure mode.

## Source

Primary Conductor inbox note dated `20260506`:

- `/loop-verify` should short-circuit when the real issue is upstream or
  outside the current repo, especially when Cam controls that upstream repo.
- If local work can still continue, the loop should keep a comprehensive
  upstream issue list while ending when no further local issue remains.
- Worker model choice should not blindly mean "use the best model we have" for
  every verification shard; the main thread should size model strength to the
  work and risk.

## Decision Context

- ADR-001 applies: Conductor is a supervisor, not the canonical copy of every
  project skill.
- ADR-002 applies: this can incubate as Conductor supervisor memory and a
  portable skill refinement before any cross-project sync.
- Alignment 011 established `/loop-verify` as a portable improvement.
- Alignment 019 established that validation and core story-loop work can use
  bounded subagents, but the main thread owns final scope and disposition.
- Story 008 added reviewed-learning hooks, so this failure mode also counts as
  evidence for future learning-review candidates when it repeats or causes a
  high-risk miss.

## Classification

Portable improvement with local adaptation.

The upstream-boundary rule is portable across all tracked repos because each
repo can hit provider, source-artifact, generated-surface, or upstream-project
failures that local shard workers cannot honestly fix. The exact reporting
shape should stay local to each repo's validation and triage surfaces.

The model-sizing rule is also portable, but it should be phrased as coordinator
judgment rather than a fixed model matrix. The runtime and available models
change too often for a hard-coded table to age well.

## Conductor Seed Change

Conductor's local `.agents/skills/loop-verify/SKILL.md` now adds:

- an explicit upstream boundary before worker launch
- required reporting for upstream-owned findings
- a `blocked` stop when upstream issues prevent honest local verification
- a continue-with-local-scope path when the upstream issue can be separated
- a dynamic worker model/reasoning default based on shard complexity, failure
  cost, and token cost instead of always requesting the strongest model

This is not a target-project rollout. It is the supervisor seed and comparison
record for the next adoption step.

## Recommendation

Create a focused follow-up story only if Cam wants this behavior live across
the tracked repos. The story should:

- roll the upstream-boundary rule into `/loop-verify` for each tracked repo
- inspect `/validate`, `/build-story`, `/create-story`, and `/triage` for
  subagent model-selection language and add the same risk-sized default where
  those skills actually spawn workers
- preserve local differences in upstream reporting, especially Storybook's
  Dossier/doc-web dependency lanes
- avoid a central model table; use risk-based selection guidance instead

## Stop Conditions

- Do not claim Storybook, Dossier, doc-web, or any target repo has this fix
  until a target-repo story/rollout applies it there.
- Do not broaden the rollout into provider eval policy, promptfoo setup, or
  aspirational eval planning; those are separate inbox pressures.
- Do not add automatic upstream issue creation unless a target repo already has
  a clear issue/story routing surface for it.

## Practical Impact

This reduces the chance that a future verification run spends hours proving the
wrong repo is broken. It also gives agents permission to use cheaper workers
for low-risk shards while keeping stronger reasoning for contracts and
cross-repo failure modes.

## Rollout Execution

Story 009 applied the portable behavior in isolated target worktrees, not in
primary checkouts.

Shared rollout settings:

- Worktree root:
  `/Users/cam/.codex/worktrees/loop-verify-upstream-model-guardrails/`
- Branch: `codex/loop-verify-upstream-model-guardrails`
- Core edits: `.agents/skills/loop-verify/SKILL.md`,
  `.agents/skills/create-story/SKILL.md`,
  `.agents/skills/build-story/SKILL.md`,
  `.agents/skills/validate/SKILL.md`, and
  `.agents/skills/triage/SKILL.md`
- Extra edits where present: `.agents/skills/golden-verify/SKILL.md`

Per-repo evidence:

| Project | Base | Adaptation | Checks |
| --- | --- | --- | --- |
| Dossier | `834fbc7` | Added upstream-boundary loop stop/reporting, risk-sized core story-loop worker guidance, and narrowed `golden-verify` away from blanket `model: "opus"` while preserving high-capability semantic golden review. | `skills-check` passed; `methodology-check` passed using `/Users/cam/Documents/Projects/dossier/.venv/bin/python` because bare `python3` lacked `yaml`; `git diff --check` passed. |
| Storybook | `c06a0ea` | Added the shared `/loop-verify` contract while preserving Dossier/doc-web upstream dependency routing; added risk-sized guidance to core delegation skills and `golden-verify`. | `bash scripts/sync-agent-skills.sh --check`, `npm run methodology:check`, and `git diff --check` passed. |
| doc-web | `020e8ac` | Added the shared `/loop-verify` contract and risk-sized guidance to core delegation skills. No `golden-verify` equivalent was present. | `make skills-check methodology-check` and `git diff --check` passed. |
| CineForge | `c7fa3d0` | Added the shared `/loop-verify` contract, risk-sized core delegation guidance, and narrowed `golden-verify` model guidance. Regenerated methodology summaries because the fresh `origin/main` graph had a date-based UI scout freshness count stale by five days. | `make skills-check`, `npm run methodology:compile`, `npm run methodology:check`, and `git diff --check` passed. |
| Board Game Ingester | `8e8026e` | Added the shared `/loop-verify` contract and risk-sized guidance to core delegation skills. No `golden-verify` equivalent was present. | `make skills-check methodology-check lint` and `git diff --check` passed. |
| RoboRally | `14bff21` | Added the shared `/loop-verify` contract, risk-sized core delegation guidance, and narrowed `golden-verify` model guidance. | `npm run skills:check`, `npm run methodology:check`, and `git diff --check` passed. |
| Echo Forge | `360e422` | Added the shared `/loop-verify` contract, risk-sized core delegation guidance, and narrowed `golden-verify` model guidance. | `npm run skills:check`, `npm run methodology:check`, and `git diff --check` passed. |

Known limits:

- Dependency-heavy full test suites were not run in the isolated worktrees
  because these worktrees intentionally do not carry installed `node_modules`
  or local `.venv` environments. The validation was scoped to the changed
  process surfaces: skill wrapper checks, methodology graph checks, and diff
  hygiene.
- Dossier's methodology script requires PyYAML, so the check used the primary
  repo's existing virtualenv rather than creating a new environment in the
  isolated worktree.
- CineForge gained generated `docs/build-map.md`, `docs/stories.md`, and
  `docs/methodology/graph.json` updates solely to make its date-sensitive
  methodology check current.
