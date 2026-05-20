---
title: "Add ADR Triage Loop"
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
  - "spec:4.1"
  - "spec:4.2"
  - "spec:5.1"
  - "spec:5.3"
decision_refs:
  - "ADR-001"
  - "ADR-002"
depends_on: []
category_refs:
  - "alignment"
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

# Story 019 — Add ADR Triage Loop

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: None

## Goal

Create a lightweight ADR triage workflow for the point after an ADR exists but
before the remaining decisions and next action are clear.

The workflow should let an agent inspect an ADR, inventory what is still open,
separate Cam-owned preference/product calls from agent-owned technical
recommendations, judge how far along the ADR is, and recommend the next route.
When the ADR is decision-complete, the route should usually be `/align` rather
than more free-form discussion.

## Acceptance Criteria

- [x] Alignment 037 records the cross-project ADR lifecycle comparison and the
      recommendation-first rollout scope.
- [x] Conductor has a small invocable `/triage-adr` skill, or an explicitly
      justified smaller alternative, with a clear output contract:
      - ADR maturity / status read
      - remaining decision inventory
      - user-preference decisions needing Cam
      - technical decisions where the agent should recommend a path
      - research/evidence gaps
      - one next route
- [x] Caller hooks in `create-adr`, `align`, `create-story`, `build-story`, or
      `/ideation` are added only where they remove ambiguity.
- [x] The workflow does not become a new decision authority: ADRs, stories,
      alignments, and repo-local specs remain the normative surfaces.
- [x] Target repo rollout, if approved during build, uses isolated worktrees
      from current `origin/main` and does not touch active primary checkouts.
- [x] Target repos preserve local ADR template, status, research, and generated
      planning-surface conventions.
- [x] Conductor and any touched target repos pass their native skill,
      methodology, and whitespace checks.

## Out of Scope

- Changing any product ADR's actual decision outcome.
- Forcing a single ADR template, status taxonomy, or research-file convention
  across all repos.
- Making `/ideation` mandatory for ADR work.
- Editing dirty target primary checkouts.
- Committing, pushing, or landing target repo changes without an explicit
  closeout request.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Read Alignment 034, Alignment 037, and the current target-repo ADR skill
      surfaces from `origin/main`
- [x] Design the smallest ADR triage contract that solves the source note
- [x] Implement the Conductor skill / workflow text
- [x] Patch only the needed Conductor caller hooks
- [x] If target rollout is approved, create isolated target worktrees under
      `/Users/cam/.codex/worktrees/adr-triage-loop/`
- [x] Patch target repos with repo-local adaptation
- [x] Update related alignment memory if implementation changes the
      recommendation
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] No scripts or repo checks changed; target repo checks run as listed
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

- `docs/alignments/align-037-adr-triage-loop.md` — comparison and
  recommendation record.
- `docs/align-projects.md` — alignment index entry.
- `docs/stories/story-019-adr-triage-loop.md` — story source of truth.
- `inbox.md` — remove the routed ADR triage raw note once durable artifacts
  exist.
- `.agents/skills/triage-adr/SKILL.md` — likely new workflow skill.
- `.agents/skills/create-adr/SKILL.md` — likely caller hook.
- `.agents/skills/align/SKILL.md` or `.agents/skills/create-story/SKILL.md` —
  possible small caller hooks if build evidence warrants.
- Target repo skill surfaces only from isolated worktrees after approval.

## Notes

- Triggered by the `inbox.md` note asking for an ADR-specific triage mode that
  identifies remaining decisions, separates preference calls from technical
  calls, assesses how far along the ADR is, and recommends `/align` when the
  ADR is effectively decision-complete.
- Read-only comparison on 2026-05-20 found all tracked repos have
  `create-adr`, but no dedicated ADR triage workflow.
- Primary target checkouts are not safe rollout targets as-is: several are
  behind `origin/main`, Storybook has an untracked GEDCOM file, CineForge has a
  local deploy-log edit, Board Game Ingester is on an active story branch, and
  Echo Forge is active Story 053 with many modified/untracked files.
- Recommended target branch if rollout proceeds:
  `codex/adr-triage-loop`.

## Plan

Plan prepared 20260520-1125. Implementation is behind the build-story plan
gate.

Current evidence:

- Conductor Ideal/spec/ADR fit is clear: this is recommendation-first
  supervisor work, not a canonical harness rewrite.
- ADR-002 fits the work as a bounded investigative lane: inspect an existing
  ADR, document evidence, propose the smallest next route, and leave durable
  memory.
- No drift-prone external API/provider/tooling interface is being changed, so
  fresh upstream docs are not needed for this build. The current evidence is
  local repo skill and methodology state.
- `origin/main` was refreshed for all target repos on 2026-05-20.
- Target `origin/main` evidence:
  - Dossier `3d7527f`: no `/triage-adr`; `create-adr` has `/ideation` and
    `/align` propagation; `create-story`/`build-story` have decision-brief
    guidance; 6 ADR dirs.
  - Storybook `0328dd8`: no `/triage-adr`; `create-adr` has `/ideation` but
    no explicit align-after-ADR hook; `create-story`/`build-story` have
    decision-brief guidance; 24 ADR dirs.
  - Doc Web `37ef4af`: no `/triage-adr`; `create-adr` has `/ideation` and
    align-after-ADR guidance; story/build decision-brief hooks are absent; 3
    ADR dirs.
  - CineForge `2a39893`: no `/triage-adr`; `create-adr` has `/ideation` but
    no explicit align-after-ADR hook; story/build decision-brief hooks are
    absent; 3 ADR dirs.
  - Board Game Ingester `d3d5142`: no `/triage-adr`; `create-adr` has
    `/ideation` and align-after-ADR guidance; story/build decision-brief hooks
    are absent; 0 ADR dirs.
  - Robo Rally `40b82fe`: no `/triage-adr`; `create-adr` has `/ideation` but
    no explicit align-after-ADR hook; `create-story`/`build-story` have
    decision-brief guidance; 1 ADR dir.
  - Echo Forge `5bec49b`: no `/triage-adr`; `create-adr` has `/ideation` but
    no explicit align-after-ADR hook; `create-story`/`build-story` have
    decision-brief guidance; 13 ADR dirs.

Implementation plan:

1. Keep the Conductor diff local in this worktree and set Story 019 to
   `In Progress` only after this plan is approved.
2. Add a new Conductor `.agents/skills/triage-adr/SKILL.md`.
   - Make it user-invocable.
   - Trigger on "triage this ADR", "where are we in this ADR?", uncertain ADR
     state, or a maturing ADR conversation.
   - Require reading the actual ADR plus Ideal/spec/state/graph and relevant
     stories/alignment records.
   - Output a compact report:
     - status / maturity read
     - settled decisions
     - user-preference decisions needing Cam
     - technical decisions with agent recommendations
     - research/evidence gaps
     - integration gaps
     - one next route
   - Include route rules for continue discussion, run research, run
     `/ideation`, update ADR, create or adjust stories, run `/align` /
     `/align-projects`, accept/reject, or close stale.
   - Keep `/ideation` optional and only for option-quality gaps.
   - Keep the skill advisory; it does not decide or edit the ADR unless the
     user explicitly asks for that follow-up.
3. Add tiny Conductor caller hooks:
   - `create-adr`: when an existing ADR becomes ambiguous or appears mature,
     route to `/triage-adr` before more ADR creation or alignment.
   - `align-projects`: for ADR-derived cross-project changes, use
     `/triage-adr` first when the ADR's open decisions are unclear.
   - Avoid touching `create-story` or `build-story` unless implementation
     evidence shows a real ambiguity; Story 019's source note is ADR-specific.
4. Update Conductor setup/skill sync surfaces only if required:
   - Run `make skills-check` after adding the skill.
   - Do not generate optional provider command aliases unless an existing check
     requires it.
5. If this plan approval is meant to include target rollout, create isolated
   target worktrees under
   `/Users/cam/.codex/worktrees/adr-triage-loop/<project-key>` from current
   `origin/main`, branch `codex/adr-triage-loop`.
6. In target repos, apply only local-adapted skill/caller changes:
   - Copy the shared `/triage-adr` contract with repo-local path names and
     `/align` rather than Conductor `/align-projects`.
   - Add `create-adr` hooks everywhere.
   - Add `align` hooks where align-after-ADR is currently missing or weak.
   - Do not force story/build hooks into repos where the issue is already
     covered or the local story-loop is intentionally lean.
   - Preserve ADR template, status, research, generated-dashboard, and
     validation conventions.
7. Validate Conductor:
   - `PYTHONDONTWRITEBYTECODE=1 make methodology-compile`
   - `PYTHONDONTWRITEBYTECODE=1 make methodology-check`
   - `PYTHONDONTWRITEBYTECODE=1 make lint`
   - `make skills-check`
   - `git diff --check`
8. Validate target repos if rollout happens:
   - Dossier: `make skills-check`, `make methodology-check`,
     `make triage-facts-check`, `git diff --check` using the repo's Python
     environment if needed.
   - Storybook: `pnpm methodology:compile`,
     `scripts/sync-agent-skills.sh --check`, `pnpm methodology:check`,
     `pnpm triage-facts:check`, `git diff --check`.
   - Doc Web: `make skills-check`, `make methodology-check`,
     `make triage-facts-check`, `git diff --check`.
   - CineForge: `make skills-check`, `npm run methodology:compile`,
     `npm run methodology:check`, `make triage-facts-check`,
     `git diff --check`.
   - Board Game Ingester: `make skills-check`, `make methodology-compile`,
     `make methodology-check`, `make triage-facts-check`, `git diff --check`.
   - Robo Rally: `npm run skills:check`, `npm run methodology:check`,
     `npm run triage-facts:check`, `git diff --check`.
   - Echo Forge: `npm run skills:check`, `npm run methodology:check`,
     `npm run triage-facts:check`, `git diff --check`.
9. Update Story 019 work log with the exact files changed, target worktree
   paths, validation evidence, and any explicit target deferrals.
10. Leave Story 019 `In Progress` with Build complete checked and recommend
    `/validate 019` as the next yes-ready step.

## Work Log

20260520-1050 — story-created: routed the ADR triage inbox note into Alignment
037 and Story 019 after comparing tracked ADR skill/story surfaces; next step is
`/build-story 019` if Cam approves the rollout.

20260520-1125 — build-plan: read Ideal/spec/state/graph, ADR-001, ADR-002,
Alignment 034, Alignment 037, Conductor skill surfaces, and refreshed
`origin/main` for target repo ADR/caller skill evidence. Proposed a small
Conductor `/triage-adr` skill plus tiny caller hooks, with target rollout only
through isolated worktrees. No external upstream docs needed because this build
touches local methodology/skill text only.

20260520-1215 — build-implementation: added Conductor
`.agents/skills/triage-adr/SKILL.md` plus tiny hooks in `create-adr`,
`align-projects`, setup-methodology, the setup runbook, and setup checklist.
The skill is advisory only: it inventories ADR maturity, settled decisions,
Cam-owned decisions, technical recommendations, evidence gaps, integration
gaps, and one next route without making ADRs, stories, alignments, or specs
less authoritative.

Created isolated target worktrees from refreshed `origin/main` on branch
`codex/adr-triage-loop`:

- Dossier `3d7527f` —
  `/Users/cam/.codex/worktrees/adr-triage-loop/dossier`
- Storybook `0328dd8` —
  `/Users/cam/.codex/worktrees/adr-triage-loop/storybook`
- Doc Web `37ef4af` —
  `/Users/cam/.codex/worktrees/adr-triage-loop/doc-web`
- CineForge `2a39893` —
  `/Users/cam/.codex/worktrees/adr-triage-loop/cine-forge`
- Board Game Ingester `d3d5142` —
  `/Users/cam/.codex/worktrees/adr-triage-loop/boardgame-ingester`
- Robo Rally `40b82fe` —
  `/Users/cam/.codex/worktrees/adr-triage-loop/roborally`
- Echo Forge `5bec49b` —
  `/Users/cam/.codex/worktrees/adr-triage-loop/echo-forge`

Each target worktree received only repo-local methodology skill changes:
`.agents/skills/triage-adr/SKILL.md`, `create-adr`, `align`, and
`setup-methodology`. The target skill uses local `/align`, preserves local ADR
templates/status/research conventions, and avoids Conductor-only
`/align-projects` language.

Target validation completed:

- Dossier: `make skills-check`; `make methodology-check triage-facts-check
  PYTHON=/Users/cam/Documents/Projects/dossier/.venv/bin/python`;
  `git diff --check`
- Storybook: `pnpm methodology:compile`;
  `scripts/sync-agent-skills.sh --check`; `pnpm methodology:check`;
  `pnpm triage:facts:check`; `git diff --check`
- Doc Web: `make skills-check methodology-check triage-facts-check`;
  `git diff --check`
- CineForge: `make skills-check`; `npm run methodology:compile`;
  `npm run methodology:check`; `make triage-facts-check
  PYTHON=/Users/cam/Documents/Projects/cine-forge/.venv/bin/python`;
  `git diff --check`
- Board Game Ingester: `make methodology-compile`;
  `make skills-check methodology-check triage-facts-check`; `git diff --check`
- Robo Rally: `npm run skills:check`; `npm run methodology:check`;
  `npm run triage-facts:check`; `git diff --check`
- Echo Forge: `npm run skills:check`; `npm run methodology:check`;
  `npm run triage-facts:check`; `git diff --check`

Dossier and CineForge needed their existing project Python environments in the
isolated worktrees. Echo Forge needed a temporary `node_modules` symlink to the
primary checkout for the triage-facts test; it was removed after validation.
CineForge retained pre-existing methodology freshness warnings for architecture
audit domains and UI scout cadence.

20260520-1220 — conductor-validation: reran
`PYTHONDONTWRITEBYTECODE=1 make methodology-compile`,
`PYTHONDONTWRITEBYTECODE=1 make methodology-check`,
`PYTHONDONTWRITEBYTECODE=1 make lint`, `make skills-check`, and
`git diff --check` after updating Story 019 and Alignment 037. All passed.

20260520-1225 — validation-pass: reviewed the current Conductor diff,
untracked files, Story 019 acceptance criteria, Alignment 037 rollout evidence,
and target worktree adaptations. No material findings found. Verified target
product skills route to repo-local `/align` and do not carry Conductor-only
`/align-projects` or `projects.yaml` language. Reran target skill,
methodology, triage-facts, and whitespace checks, then reran Conductor
`methodology-compile`, `methodology-check`, `lint`, `skills-check`, and
`git diff --check`. All passed; CineForge still reports pre-existing
methodology freshness warnings, and Dossier/CineForge/Echo Forge still need the
repo-specific environment wrappers documented above.

20260520-1245 — marked-done: `/finish-and-push` landed the linked target repo
rollout first, then closed Story 019. Target `main` landing commits:

- Dossier `99bc82b`
- Storybook `e4b140b`
- Doc Web `ac88431`
- CineForge `eb5de87`
- Board Game Ingester `eae77ad`
- Robo Rally `0a2b96a`
- Echo Forge `ec423e7`

Conductor close-out updated `CHANGELOG.md` and reran methodology generation.
