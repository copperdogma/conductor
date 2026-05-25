# Alignment 040 - Skill Authoring Budget Guidance

**Date**: 2026-05-25
**Classification**: Portable improvement with local adaptation
**Source**: [Scout 041](../scout/scout-041-skill-cleaner-skill-budget-audit.md),
[Alignment 039](./align-039-skill-surface-budget-audit.md)
**Story**: [Story 023](../stories/story-023-skill-authoring-budget-guidance.md)
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Focus

Move the useful `skill-cleaner` lesson to the repo-local point of creation:
`create-cross-cli-skill` and, where present, `improve-skill`.

The target adoption is preventive guidance, not a copied audit script. Conductor
keeps the central `skill-surface-audit` helper and portfolio-level reporting.
The product repos should teach agents to write token-efficient `SKILL.md`
frontmatter before prompt-budget pressure accumulates.

## Current Surface Inventory

All seven tracked target repos have a `create-cross-cli-skill` skill.

| Project | `create-cross-cli-skill` | `improve-skill` | Recommendation |
| --- | --- | --- | --- |
| Dossier | yes | yes | Patch both surfaces. |
| Storybook | yes | yes | Patch both surfaces. |
| doc-web | yes | no | Patch creation guidance only. Do not invent `improve-skill`. |
| CineForge | yes | yes | Patch both surfaces. |
| Board Game Ingester | yes | no | Patch creation guidance only. Do not invent `improve-skill`. |
| RoboRally | yes | yes | Patch both surfaces. |
| Echo Forge | yes | yes | Patch both surfaces. |

The current `create-cross-cli-skill` guidance already tells agents to use
frontmatter with `name`, `description`, and `user-invocable`, then run the
repo's skill-sync checks. It does not yet explain that `description` is
model-visible routing inventory and should be kept concise.

The current `improve-skill` guidance already has a useful anti-bloat rule:
improve for patterns, not one-off incidents. It does not yet include a focused
description-budget pass.

## Portable Guidance

Patch `create-cross-cli-skill` with a small authoring rubric:

- The `description` is routing inventory, not documentation.
- Keep it short enough to scan quickly; a practical default is one sentence,
  roughly 250-300 characters unless trigger specificity truly requires more.
- Put trigger nouns up front: domain, action, artifact, tool, or surface.
- Include the cues that decide activation; avoid generic verbs that could match
  many skills.
- Move examples, policy detail, long workflow explanation, and validation
  matrices into the body, `references/`, or templates.
- Preserve trigger nouns when shortening existing descriptions.

Patch existing `improve-skill` surfaces with a maintenance rubric:

- During any skill improvement, check whether the frontmatter description is
  doing routing work or just prose work.
- Remove repeated explanation from descriptions when the body already covers it.
- Keep app-specific detail out of generic skills unless a different project
  using the same skill would benefit.
- Use Conductor's `skill-surface-audit` only as an optional central check after
  many skill edits or before shared-skill rollouts.

## Rollout Plan

Use one isolated worktree per target repo:

```bash
$HOME/.codex/worktrees/skill-authoring-budget-guidance/<project-key>
```

Create each branch from `origin/main`:

```bash
codex/skill-authoring-budget-guidance
```

Per repo:

1. Inspect branch and status in the primary checkout.
2. Create an isolated worktree from `origin/main`.
3. Patch only existing skill-authoring surfaces.
4. Run `scripts/sync-agent-skills.sh` if the repo uses it.
5. Run the repo's skill and methodology checks.
6. Record validation evidence here before closeout.

## Per-Project Recommendations

| Project | Action | Notes |
| --- | --- | --- |
| Dossier | sync now | Has both target skills and a mature skill-check surface. |
| Storybook | sync now | Has both target skills and prior skill-surface rollout history. |
| doc-web | sync partially | Creation guidance only; no `improve-skill` exists. |
| CineForge | sync now | Has both target skills; preserve local validation commands. |
| Board Game Ingester | sync partially | Creation guidance only; no `improve-skill` exists. |
| RoboRally | sync now | Has both target skills; preserve optional alias wording already present. |
| Echo Forge | sync now | Has both target skills; keep changes quiet and isolated from product work. |
| Conductor | keep local supervisor role | No target `create-cross-cli-skill` surface; Conductor owns this plan and the central audit helper. |

## Stop Conditions

- Do not edit target primary checkouts.
- Do not install the Conductor audit helper into every repo.
- Do not add missing `improve-skill` skills as part of this story.
- Do not shorten unrelated existing descriptions unless there is a clear,
  low-risk edit tied to the authoring guidance.
- Do not call the rollout complete until every target repo has either applied
  patches with validation evidence or a precise deferred reason.
- Do not commit, push, or land target repo branches without an explicit closeout
  request.

## Rollout Evidence

Story 023 applied the planned patches in isolated worktrees. No primary target
checkout was edited.

| Project | Worktree | Base | Commit | Patched surfaces | Validation |
| --- | --- | --- | --- | --- | --- |
| Dossier | `/Users/cam/.codex/worktrees/skill-authoring-budget-guidance/dossier` | `874c54f` | `68cba42` | `create-cross-cli-skill`, `improve-skill` | `scripts/sync-agent-skills.sh`; `make skills-check`; `make PYTHON=/Users/cam/Documents/Projects/dossier/.venv/bin/python methodology-compile`; `make PYTHON=/Users/cam/Documents/Projects/dossier/.venv/bin/python methodology-check`; `git diff --check` passed. The default `python3` lacks PyYAML in this fresh worktree, so validation used the repo's existing venv. |
| Storybook | `/Users/cam/.codex/worktrees/skill-authoring-budget-guidance/storybook` | `e4b140b` | `a31be9c` | `create-cross-cli-skill`, `improve-skill` | `scripts/sync-agent-skills.sh`; `scripts/sync-agent-skills.sh --check`; `npm run methodology:compile`; `npm run methodology:check`; `git diff --check` passed. Methodology compile refreshed UI-scout freshness text for 2026-05-25. |
| doc-web | `/Users/cam/.codex/worktrees/skill-authoring-budget-guidance/doc-web` | `f299e65` | `94a5604` | `create-cross-cli-skill` | `scripts/sync-agent-skills.sh`; `make skills-check`; `make methodology-compile`; `make methodology-check`; `git diff --check` passed. `improve-skill` does not exist and was not invented. |
| CineForge | `/Users/cam/.codex/worktrees/skill-authoring-budget-guidance/cine-forge` | `2db636e` | `6f537cd` | `create-cross-cli-skill`, `improve-skill` | `scripts/sync-agent-skills.sh`; `make skills-check`; `npm run methodology:compile`; `npm run methodology:check`; `git diff --check` passed. Existing architecture-audit and UI-scout freshness warnings remain unrelated; compile refreshed their age/build-map date for 2026-05-25. |
| Board Game Ingester | `/Users/cam/.codex/worktrees/skill-authoring-budget-guidance/boardgame-ingester` | `eae77ad` | `831ea24` | `create-cross-cli-skill` | `scripts/sync-agent-skills.sh`; `make skills-check`; `make methodology-compile`; `make methodology-check`; `git diff --check` passed. `improve-skill` does not exist and was not invented. |
| RoboRally | `/Users/cam/.codex/worktrees/skill-authoring-budget-guidance/roborally` | `0a2b96a` | `3e2d8c8` | `create-cross-cli-skill`, `improve-skill` | `scripts/sync-agent-skills.sh`; `npm run skills:check`; `npm run methodology:compile`; `npm run methodology:check`; `git diff --check` passed. |
| Echo Forge | `/Users/cam/.codex/worktrees/skill-authoring-budget-guidance/echo-forge` | `f0a9e41` | `28536c9` | `create-cross-cli-skill`, `improve-skill` | `scripts/sync-agent-skills.sh`; `npm run skills:check`; `npm run methodology:compile`; `npm run methodology:check`; `git diff --check` passed. Existing `No Ideal requirements parsed` methodology warning remains unrelated; compile refreshed `docs/methodology/graph.json` generated timestamp. |

All seven target commits were pushed to
`origin/codex/skill-authoring-budget-guidance`. They were not landed to target
`main` branches in this closeout pass.

## Practical Impact

Cam gets the skill-budget benefit at the point where new skills are created.
That should reduce future context overhead and wrong-skill activation risk
without turning Conductor into a canonical harness repo or adding a recurring
audit ceremony to every project.
