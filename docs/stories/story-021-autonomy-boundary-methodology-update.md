---
title: "Add Autonomy Boundary to Triage and Build Story"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I3"
  - "I5"
spec_refs:
  - "spec:3.2"
  - "spec:4.1"
  - "spec:4.2"
  - "spec:5.2"
  - "spec:5.3"
decision_refs: []
depends_on: []
category_refs:
  - "scouting"
  - "story-prep"
  - "memory"
tracked_projects:
  - "conductor"
---

# Story 021 — Add Autonomy Boundary to Triage and Build Story

**Priority**: High
**Status**: Done
**Decision Refs**: None yet
**Depends On**: None

## Goal

Turn Scout 040's Peter Steinberger autotriage finding into a small Conductor
methodology update.

The useful idea is not GitHub queue automation. It is the explicit boundary
between work that can proceed after the operator says `yes`, work that needs
another product/workflow judgment, and work that is blocked because evidence,
credentials, checkout safety, or verification are missing.

This story should make that boundary visible in `/triage` and `/build-story`
without adding a new artifact class, replacing the plan gate, or broadening
Conductor into a public issue/PR queue runner.

## Acceptance Criteria

- [x] `/triage` output includes a concise autonomy-boundary field for the one
      recommended action.
- [x] The boundary uses simple categories that can be acted on consistently:
      `Go after yes`, `Needs human judgment`, and `Blocked`.
- [x] `/triage` defines those categories in terms of Ideal/spec fit, current
      local evidence, bounded scope, checkout/worktree safety, and honest
      verification.
- [x] `/build-story` planning requires a short autonomy note that says whether
      the approved plan can proceed without another human decision, must pause
      for a judgment call, or is blocked until missing proof/access/state is
      resolved.
- [x] The wording preserves the existing `/build-story` plan gate; it does not
      let a story skip approval before implementation.
- [x] The wording does not import Peter's GitHub queue tooling, RepoBar,
      author-trust scoring, or a required `VISION.md` file.
- [x] Touched generic skill files avoid personal-name wording and use operator
      or human-judgment language instead.
- [x] Scout 040 is updated if the implementation changes the recommendation or
      scope.
- [x] Generated methodology surfaces are current and the relevant checks pass.

## Out of Scope

- Rolling the wording into tracked product repos.
- Creating a canonical central methodology package in Conductor.
- Building direct GitHub issue/PR queue automation.
- Adding RepoBar or any external queue-discovery tool.
- Requiring repos to add `VISION.md`; the local equivalent remains
  Ideal/spec/state/story context.
- Changing `/validate`, `/loop-verify`, `/finish-and-push`, or target-project
  skills unless a direct consistency issue is found while building.
- Treating a `yes` as permission to commit, push, merge, or land without the
  existing explicit closeout requests.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Re-read Scout 040 and Peter's current `github-project-triage` source
- [x] Update Conductor `/triage` with an autonomy-boundary output line and
      category definitions
- [x] Update Conductor `/build-story` with the matching plan-time autonomy note
- [x] Update Scout 040 if the accepted scope changes during implementation
- [x] Search related skill surfaces for consistency and update only if directly
      necessary
- [x] Remove personal-name wording from touched generic skill files
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: not applicable; no scripts or repo
        checks changed
- [x] Search docs and update any related surfaces
- [x] Verify Conductor tenets:
  - [x] I1 — Meaning over text
  - [x] I3 — Recommendation-first supervision
  - [x] I5 — Minimal overhead

## Workflow Gates

- [x] Build complete
- [x] Validation complete or explicitly skipped by user
- [x] Story marked done via `/mark-story-done`

## Files to Modify

- `.agents/skills/triage/SKILL.md` — add autonomy-boundary guidance and output
  field.
- `.agents/skills/build-story/SKILL.md` — add the matching plan-time autonomy
  note and keep generic closeout wording.
- `.agents/skills/align-projects/SKILL.md` — genericize target-worktree and
  in-place-work wording.
- `.agents/skills/check-in/SKILL.md` — genericize inbox and operator wording.
- `.agents/skills/create-adr/SKILL.md` — genericize decision-owner wording.
- `.agents/skills/finish-and-push/SKILL.md` — genericize learning-promotion
  approval wording.
- `.agents/skills/learning-candidate/SKILL.md` — genericize candidate lifecycle
  approval wording.
- `.agents/skills/loop-verify/SKILL.md` — genericize continuation, strict-mode,
  and candidate-promotion wording.
- `.agents/skills/setup-methodology/SKILL.md` — genericize triage-ADR wording.
- `.agents/skills/triage-adr/SKILL.md` — genericize human-decision wording.
- `.agents/skills/validate/SKILL.md` — genericize learning-promotion and impact
  wording.
- `docs/scout/scout-040-peter-steinberger-github-autotriage.md` — update only
  if implementation changes the recommendation or scope.
- `docs/stories/story-021-autonomy-boundary-methodology-update.md` — story
  source of truth and work log.
- Generated methodology files — update via `make methodology-compile`.

## Notes

- Triggered by Scout 040, based on Peter Steinberger's May 23, 2026
  `github-project-triage` / Codex autotriage workflow.
- The adopted principle is the promotion boundary, not the queue machinery:
  project fit, current evidence, bounded action, workspace safety, and
  verification must all be clear before work becomes autonomous after a `yes`.
- This is a low-overhead addition because it makes an implicit decision point
  visible in existing outputs. It should not create a new ceremony.
- Target-project rollout should be considered only after this Conductor-local
  wording proves useful and the operator explicitly asks for a sync.

## Plan

Autonomy note: `Go after approval`. This is a Conductor-local skill wording
change with clear Ideal/spec fit, current upstream evidence, bounded files, no
target-repo edits, and direct repo-native checks. The current `/build-story`
contract still requires this plan approval before implementation. After
approval, no additional human judgment should be needed unless implementation
finds a broader policy conflict or a target-repo rollout question.

1. Set Story 021 to `In Progress` after plan approval and add a work-log entry.
2. Patch `.agents/skills/triage/SKILL.md`:
   - define an `Autonomy Boundary` for the one recommended action
   - use the categories `Go after yes`, `Needs human judgment`, and `Blocked`
   - tie the categories to Ideal/spec fit, current evidence, bounded action
     shape, checkout/worktree safety, and honest verification
   - add the boundary to the output contract near the final recommendation so
     a bare `yes` has clearer meaning
3. Patch `.agents/skills/build-story/SKILL.md`:
   - require an autonomy note in `## Plan`
   - preserve the existing plan approval gate
   - explain how to identify later pause points, blocked work, or work that can
     proceed after approval
4. Search related Conductor skill/docs surfaces for direct consistency issues.
   Update only if the new boundary would otherwise conflict with nearby
   instructions.
5. Update this story's tasks, work log, and generated methodology surfaces.
   Update Scout 040 only if implementation changes the accepted scope.
6. Run checks:
   - `make methodology-compile`
   - `make methodology-check`
   - `make lint`
   - `make skills-check`
   - `git diff --check`
   - skip `make test` unless scripts or repo checks change
7. Leave the story `In Progress` with `Build complete` checked and recommend
   `/validate 021` as the next yes-ready step.

## Work Log

20260523-1602 — story-created: created from Scout 040 after the operator asked
to double-check expected value and then approved a focused story. Scope is
Conductor-local methodology wording first, with no target repo edits and no
GitHub queue automation.

20260525-1518 — build-plan: read Story 021, Conductor Ideal/spec/state/graph,
the Ideal-first methodology note, ADR-001, ADR-002, Scout 040, `/triage`, and
`/build-story`. Rechecked Peter's live upstream source: `agent-scripts` main is
`a7df96d0f2b0167dc569a8293fcf28b6f77e45a2`, while
`skills/github-project-triage/SKILL.md` still contains the relevant `VISION.md`,
autonomous-fit, proof, blocker, and end-to-end verification rules. Plan written;
pause for approval before skill edits.

20260525-1530 — implementation: updated Conductor `/triage` with an
`Autonomy Boundary` output field and category definitions, and updated
`/build-story` so plans must state whether approval means proceed, pause for
human judgment, or stop as blocked. Scope stayed Conductor-local; no target
repo rollout, queue tooling, or new artifact class added.

20260525-1534 — checks-passed: ran `make methodology-compile`,
`make methodology-check`, `make lint`, `make skills-check`, and
`git diff --check`. `make test` was not applicable because no scripts or repo
checks changed. Build complete; ready for `/validate 021`.

20260525-1541 — generic-wording-correction: replaced the new personal-name
judgment category with `Needs human judgment` and removed personal-name wording
from the touched generic skill files.

20260525-1547 — genericity-sweep: scanned `.agents/skills` and removed
pre-existing personal-name wording from generic skill contracts. Re-ran
`make methodology-compile`, `make methodology-check`, `make lint`,
`make skills-check`, and `git diff --check`; all passed.

20260525-1548 — validation: reviewed the tracked and untracked diffs, Story
021 acceptance criteria, workflow gates, Scout 040, and touched skill wording.
No material findings found. `/learning-review` returned `no-candidate` because
the reusable correction is already covered by the story's generic skill wording
change rather than needing a separate learning candidate.

20260525-1549 — closeout: marked Story 021 `Done` after build and validation
gates were complete. Closeout evidence: autonomy-boundary wording is present in
`/triage`, plan-time autonomy wording is present in `/build-story`, touched
generic skills avoid personal-name wording, Scout 040 records the adopted
scope, and generated methodology surfaces were refreshed.
