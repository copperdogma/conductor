# Alignment 037 - ADR Triage Loop

**Date**: 2026-05-20
**Classification**: Portable improvement with local adaptation
**Source**: `inbox.md` note requesting an ADR triage skill / default loop
**Story**: [Story 019](../stories/story-019-adr-triage-loop.md)
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Focus

Compare how tracked repos handle ADR work after an ADR exists but before the
next action is obvious.

The source problem is recurring ADR ambiguity: a design conversation starts,
an ADR gets created, then the remaining decisions, ownership boundaries, and
next route are no longer clear. The useful loop is not more ADR creation. It is
a compact triage pass over an existing ADR:

- identify remaining decisions
- separate user-preference decisions from technical decisions the agent should
  recommend
- judge how far along the ADR is
- recommend the next route, including `/align` when the ADR is decision-complete

Surfaces compared:

- `inbox.md`
- `projects.yaml`
- `docs/ideal.md`, `docs/spec.md`, `docs/methodology/state.yaml`, and
  `docs/methodology/graph.json`
- existing alignment memory, especially Alignment 034 `/ideation`
- tracked repos' `.agents/skills/create-adr/SKILL.md`
- tracked repos' `.agents/skills/create-story/SKILL.md`
- tracked repos' `.agents/skills/build-story/SKILL.md`
- tracked repos' `docs/decisions/` ADR inventories
- target primary checkout branch/status before any recommendation

## Observations

All tracked repos have a `create-adr` skill, but none has an ADR-specific
triage skill. Existing `create-adr` guidance is creation-oriented: create the
ADR folder, fill context/options/research, show the files, and in some repos
run `/align` after the ADR matures.

The newer story-loop skills already contain part of the wanted behavior.
Dossier, Storybook, Robo Rally, and Echo Forge have `create-story` and
`build-story` decision-brief guidance for unresolved story/build decisions.
Doc Web, CineForge, and Board Game Ingester have more limited story-loop
decision guidance in the primary checkouts inspected here.

ADR volume differs materially:

| Project | ADR dirs found in primary checkout | Current fit |
| --- | ---: | --- |
| Storybook | 24 | Strongest immediate fit; several ADRs have historically lived through long discussion/research loops. |
| Echo Forge | 13 | Strong fit, but the primary checkout is active Story 053 work and must not be edited in place. |
| Dossier | 6 | Strong fit for pending/research-heavy architecture ADRs; story/build decision-brief behavior already exists. |
| Doc Web | 3 | Moderate fit; existing ADRs are mostly accepted, but the align-after-ADR handoff is already explicit. |
| CineForge | 3 | Moderate fit; creative workflow ADRs are high-consequence and benefit from explicit decision inventory. |
| Robo Rally | 1 | Low volume now, but the shared story/build decision-brief behavior already exists. |
| Board Game Ingester | 0 | Lowest urgency; useful only as future-proofing because the ADR scaffold exists. |

Primary checkout state is not clean enough to use as an execution target.
Dossier, Storybook, Doc Web, CineForge, and Robo Rally primary checkouts were
behind `origin/main`; Storybook had an untracked GEDCOM file; CineForge had a
local deploy-log edit; Board Game Ingester was on an active story branch; Echo
Forge was on active Story 053 with many modified and untracked files. Any
rollout must re-read current `origin/main` in isolated target worktrees.

## Classification

- **Portable improvement:** add a lightweight `/triage-adr` loop for existing
  ADRs. The loop should produce a decision inventory, a maturity read, and one
  recommended next route.
- **Portable improvement:** classify remaining ADR decisions into at least two
  buckets: user-preference / product-direction decisions that need Cam, and
  technical decisions where the agent should think hard and recommend a path.
- **Portable improvement:** when an ADR appears decision-complete, the triage
  result should recommend `/align` rather than leaving the conversation in a
  vague "still discussing" state.
- **Intentional adaptation:** ADR templates, status names, research file
  conventions, generated planning surfaces, and repo-local decision docs should
  stay local.
- **Intentional adaptation:** `/ideation` remains optional and caller-owned.
  ADR triage may recommend it only when option quality is the blocker.
- **Unclear drift:** some primary checkout caller-skill hooks differ from the
  recent `/ideation` and setup-methodology rollout evidence. Because several
  primary checkouts are behind or active, Story 019 should verify from
  `origin/main` before treating those differences as live drift.

## Recommended Action By Project

| Project | Recommendation | Reason |
| --- | --- | --- |
| Conductor | Sync now | Conductor should define the ADR triage contract and prove the supervisor artifact shape before any target rollout. |
| Storybook | Sync now | It has the largest ADR surface and the strongest history of long-running decision conversations. |
| Echo Forge | Sync now, isolated only | It has a large active ADR/design surface, but the primary checkout is live Story 053 work. |
| Dossier | Sync partially | Add ADR-specific triage while preserving existing story/build decision-brief behavior and research-heavy ADR conventions. |
| CineForge | Sync partially | Adopt the decision-inventory loop, but preserve generated dashboards and creative-design ADR metadata. |
| Doc Web | Sync partially | Existing align-after-ADR guidance is useful; add only the missing mid-ADR triage loop. |
| Robo Rally | Sync partially | Low ADR volume, but the shared lightweight behavior fits its existing story/build decision-brief pattern. |
| Board Game Ingester | Sync partially / lowest urgency | No ADRs exist yet, so this is future-proofing only; do not create extra ADR overhead. |

## Target Execution Plan

Create Story 019 to design and, if approved, roll out the ADR triage loop.

The build should:

1. Add a Conductor-owned `/triage-adr` skill or equivalent documented workflow.
2. Define the output contract:
   - ADR status / maturity read
   - remaining decision inventory
   - user-preference decisions
   - technical decisions with agent recommendations
   - evidence/research gaps
   - next route: continue discussion, run research, run `/ideation`, update ADR,
     create/adjust stories, run `/align`, accept/reject, or close as stale
3. Patch only the smallest caller hooks needed in `create-adr`, `align`,
   `create-story`, or `build-story`.
4. Verify target repo state from current `origin/main`.
5. Use isolated target worktrees under
   `/Users/cam/.codex/worktrees/adr-triage-loop/<project-key>` for any target
   repo edits.
6. Validate with repo-native skill/methodology checks and `git diff --check`.

## Rollout Evidence

Story 019 implemented the portable improvement as a small `/triage-adr` skill
plus caller hooks in Conductor and the tracked target repos. Target repos were
edited only in isolated worktrees from refreshed `origin/main`; primary
checkouts were not modified.

| Project | Base | Worktree | Changed surfaces |
| --- | --- | --- | --- |
| Conductor | current Story 019 worktree | `/Users/cam/.codex/worktrees/94a4/conductor` | `.agents/skills/triage-adr/SKILL.md`, `create-adr`, `align-projects`, setup-methodology/runbook/checklist docs, Story 019, Alignment 037 |
| Dossier | `3d7527f` | `/Users/cam/.codex/worktrees/adr-triage-loop/dossier` | `.agents/skills/triage-adr/SKILL.md`, `create-adr`, `align`, `setup-methodology` |
| Storybook | `0328dd8` | `/Users/cam/.codex/worktrees/adr-triage-loop/storybook` | `.agents/skills/triage-adr/SKILL.md`, `create-adr`, `align`, `setup-methodology` |
| Doc Web | `37ef4af` | `/Users/cam/.codex/worktrees/adr-triage-loop/doc-web` | `.agents/skills/triage-adr/SKILL.md`, `create-adr`, `align`, `setup-methodology` |
| CineForge | `2a39893` | `/Users/cam/.codex/worktrees/adr-triage-loop/cine-forge` | `.agents/skills/triage-adr/SKILL.md`, `create-adr`, `align`, `setup-methodology` |
| Board Game Ingester | `d3d5142` | `/Users/cam/.codex/worktrees/adr-triage-loop/boardgame-ingester` | `.agents/skills/triage-adr/SKILL.md`, `create-adr`, `align`, `setup-methodology` |
| Robo Rally | `40b82fe` | `/Users/cam/.codex/worktrees/adr-triage-loop/roborally` | `.agents/skills/triage-adr/SKILL.md`, `create-adr`, `align`, `setup-methodology` |
| Echo Forge | `5bec49b` | `/Users/cam/.codex/worktrees/adr-triage-loop/echo-forge` | `.agents/skills/triage-adr/SKILL.md`, `create-adr`, `align`, `setup-methodology` |

Validation run on 2026-05-20:

| Project | Checks |
| --- | --- |
| Dossier | `make skills-check`; `make methodology-check triage-facts-check PYTHON=/Users/cam/Documents/Projects/dossier/.venv/bin/python`; `git diff --check` |
| Storybook | `pnpm methodology:compile`; `scripts/sync-agent-skills.sh --check`; `pnpm methodology:check`; `pnpm triage:facts:check`; `git diff --check` |
| Doc Web | `make skills-check methodology-check triage-facts-check`; `git diff --check` |
| CineForge | `make skills-check`; `npm run methodology:compile`; `npm run methodology:check`; `make triage-facts-check PYTHON=/Users/cam/Documents/Projects/cine-forge/.venv/bin/python`; `git diff --check` |
| Board Game Ingester | `make methodology-compile`; `make skills-check methodology-check triage-facts-check`; `git diff --check` |
| Robo Rally | `npm run skills:check`; `npm run methodology:check`; `npm run triage-facts:check`; `git diff --check` |
| Echo Forge | `npm run skills:check`; `npm run methodology:check`; `npm run triage-facts:check`; `git diff --check` |

Notes:

- Dossier and CineForge needed their existing primary-checkout Python
  environments for methodology or triage-facts dependencies in the isolated
  worktrees.
- Echo Forge's isolated worktree had no `node_modules`; validation used a
  temporary `node_modules` symlink to the primary checkout and removed it after
  the check.
- CineForge methodology checks still report pre-existing freshness warnings for
  architecture audit domains and UI scout cadence; the outputs were current.

Target landing completed on 2026-05-20:

| Project | `main` commit |
| --- | --- |
| Dossier | `99bc82b` |
| Storybook | `e4b140b` |
| Doc Web | `ac88431` |
| CineForge | `eb5de87` |
| Board Game Ingester | `eae77ad` |
| Robo Rally | `0a2b96a` |
| Echo Forge | `ec423e7` |

## Human Judgment

The open policy choice is whether this should become a new invocable
`/triage-adr` skill or only a section inside existing `create-adr` / `align`
skills.

Recommendation: make it a small invocable skill and add tiny caller hooks. The
user request names a distinct mode, and the workflow is useful precisely when
the operator is asking "where are we in this ADR?" rather than creating or
aligning it.

## Practical Impact

Cam should get a clearer answer when an ADR conversation starts to ramble:
what is decided, what is still actually open, which calls need human judgment,
which calls the agent should recommend, and whether the next move is alignment
instead of more discussion.
