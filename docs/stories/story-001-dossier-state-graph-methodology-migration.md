---
title: "Prepare Dossier State/Graph Methodology Migration"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I4"
  - "I5"
spec_refs:
  - "spec:2.2"
  - "spec:4.2"
  - "spec:5.1"
decision_refs:
  - "ADR-001"
depends_on: []
category_refs:
  - "alignment"
  - "story-prep"
  - "memory"
tracked_projects:
  - "dossier"
---

# Story 001 — Prepare Dossier State/Graph Methodology Migration

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001
**Depends On**: None

## Goal

Turn the alignment finding about Dossier's outdated build-map-first planning
surface into execution-ready adoption work. Conductor should compare Dossier
against the newer state/graph-first methodology package used elsewhere, decide
what ports cleanly versus what stays Dossier-specific, and queue concrete
target-project work so the migration can actually happen in Dossier.

## Acceptance Criteria

- [x] Conductor records the specific Dossier methodology gaps against the
      state/graph-first package, including the missing or stale planning
      artifacts and the likely reference surfaces to port from.
- [x] Conductor produces explicit target-project adoption work for Dossier that
      covers `docs/methodology/state.yaml`, `docs/methodology/graph.json`,
      `AGENTS.md`, `/setup-methodology`, `/triage`, and the intended role of
      `docs/build-map.md` after migration.
- [x] Conductor memory reflects this as an active work line rather than an
      unresolved alignment note, and the generated backlog surfaces stay current.

## Out of Scope

- Claiming Dossier is migrated before Dossier has its own validated story,
  patches, or applied changes
- Forcing exact textual sync between Dossier and Storybook, doc-web, or
  CineForge
- Deciding unrelated cross-project methodology differences

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Re-read Alignment 001 plus Dossier's current methodology surfaces to
      confirm the missing state/graph artifacts and current build-map-first
      assumptions
- [x] Compare Dossier's methodology package against the strongest reference
      implementation(s) among Storybook, doc-web, and CineForge
- [x] Decide what should migrate as-is, what needs Dossier-specific adaptation,
      and whether `docs/build-map.md` stays as a generated/supporting surface
- [x] Create the Dossier target-project story or equivalent execution-ready work
      item for the migration
- [x] Update related scout or alignment memory if applicable
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: not needed; no Conductor skill files changed
  - [x] If scripts or repo checks changed: not needed; no Conductor scripts or
        repo-check surfaces changed
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

- `docs/stories/story-001-dossier-state-graph-methodology-migration.md` —
  track the supervisor work line
- `docs/alignments/align-001-methodology-baseline.md` — link the alignment
  finding to active follow-up work
- `docs/methodology/graph.json` — generated story index
- `docs/stories.md` — generated story backlog view
- `/Users/cam/Documents/Projects/dossier/docs/stories/story-095-dossier-state-graph-methodology-migration.md` —
  target-project migration story and queued Dossier-side execution home
- `/Users/cam/Documents/Projects/dossier/docs/stories.md` — queue the new
  Dossier story in Dossier's local backlog index

## Notes

- Alignment 001 confirmed that Dossier still lacks
  `docs/methodology/state.yaml` and `docs/methodology/graph.json`, while
  Storybook, doc-web, and CineForge all plan from those surfaces.
- The user explicitly confirmed this migration is the top current alignment
  target.
- Dossier already has `/setup-methodology`, a setup runbook, and a refreshed
  checklist, so this should be treated as methodology convergence rather than a
  greenfield bootstrap.
- The main design question is not whether to migrate, but what Dossier should
  retain from its build-map-first package once state/graph become canonical.

## Plan

### Exploration Summary

- **Ideal/spec alignment:** proceed. This belongs in Conductor first because
  [ADR-001](../decisions/adr-001-conductor-as-supervisor-not-canonical-core.md)
  makes Conductor recommendation-first; the honest deliverable is queued
  Dossier adoption work, not an unprompted Dossier-side migration.
- **Fresh substrate evidence:** Dossier still has `docs/build-map.md` and does
  not have `docs/methodology/state.yaml` or `docs/methodology/graph.json`.
  Dossier `AGENTS.md` and
  `/Users/cam/Documents/Projects/dossier/.agents/skills/setup-methodology/SKILL.md`
  still teach build-map-first planning.
- **Reference choice:** `doc-web` is the closest state/graph package reference
  for Dossier because it also uses `spec:1` through `spec:9`, while CineForge
  Story 145 is the clearest migration-story pattern for rewiring active
  methodology consumers. Storybook remains the conceptual origin, but not the
  only template.
- **Decision context:** no Dossier-local ADR already governs the state/graph
  migration. Dossier `docs/build-map.md` explicitly says its current planning
  shape was adapted from Storybook and has no local ADR for this methodology
  layer.
- **Primary risks:** blind cross-repo copying instead of Dossier-native
  adaptation; claiming migration completion before Dossier has its own built
  and validated work; and failing to define whether `docs/build-map.md`
  survives as a generated/supporting surface after migration.
- **Expected evidence:** one queued Dossier migration story covering
  `docs/methodology/state.yaml`, `docs/methodology/graph.json`, `AGENTS.md`,
  `/setup-methodology`, `/triage`, and the post-migration role of
  `docs/build-map.md`; updated Conductor alignment memory; regenerated
  Conductor planning surfaces with passing methodology checks.

### Implementation Order

1. Update this Conductor story with the comparative findings, chosen
   references, and the final supervisor-side delivery plan.
2. Create
   `/Users/cam/Documents/Projects/dossier/docs/stories/story-095-dossier-state-graph-methodology-migration.md`
   as the Dossier-side execution home for the migration.
3. Update
   `docs/alignments/align-001-methodology-baseline.md`
   so the methodology conflict points at explicit queued follow-up instead of
   remaining a bare recommendation.
4. Regenerate and verify Conductor planning surfaces with the narrowest honest
   checks for the touched scope.

### Concrete File Changes

- `docs/stories/story-001-dossier-state-graph-methodology-migration.md` —
  record the exploration evidence, approved plan, implementation notes, and
  status progression
- `docs/alignments/align-001-methodology-baseline.md` — link the alignment
  finding to the new queued Dossier work item
- `docs/methodology/graph.json` — regenerate after story/alignment metadata
  changes
- `docs/stories.md` — regenerate after story/alignment metadata changes
- `/Users/cam/Documents/Projects/dossier/docs/stories/story-095-dossier-state-graph-methodology-migration.md` —
  define the Dossier-side migration scope, file targets, acceptance criteria,
  and reference inputs

### Expected Outputs

- A Dossier-native migration story ready for Dossier-side execution
- An explicit recommendation for `docs/build-map.md` after migration:
  supporting/generated surface unless the Dossier-side implementation proves a
  different role is needed
- Conductor alignment memory that shows the methodology conflict has a queued
  follow-up artifact instead of only an open question

### Manual Inspection

- Confirm the Dossier story is adaptation-first and cites Dossier-native
  precedents, especially Stories 076 and 078 plus current `docs/spec.md`
  `spec:9` and `docs/build-map.md`
- Confirm Conductor does not claim Dossier is already migrated
- Confirm cross-project references are used as source patterns, not as
  canonical text-sync targets

### Checks

- `make methodology-compile`
- `make methodology-check`
- `make lint`
- `make skills-check` if Conductor skill files change
- `make test` if Conductor scripts or repo checks change

## Work Log

20260409-1523 — story creation: created after Alignment 001 and direct user
priority setting confirmed Dossier's state/graph migration as the top
cross-project follow-up; next step is to prepare Dossier's target-project
migration work from the supervisor side.

20260409-1617 — `/build-story` exploration and planning completed with no
implementation changes yet. Reviewed Conductor `docs/ideal.md`,
`docs/methodology-ideal-spec-compromise.md`, `docs/spec.md`,
`docs/methodology/state.yaml`, `docs/methodology/graph.json`,
`docs/alignments/align-001-methodology-baseline.md`, and `ADR-001`; reviewed
Dossier `AGENTS.md`, `docs/ideal.md`, `docs/spec.md`,
`docs/methodology-ideal-spec-compromise.md`, `docs/build-map.md`,
`/setup-methodology`, `/triage`, and Stories 076 and 078; compared reference
state/graph packages in Storybook, doc-web, and CineForge plus CineForge Story
145. Files to change if implementation proceeds:
`docs/stories/story-001-dossier-state-graph-methodology-migration.md`,
`docs/alignments/align-001-methodology-baseline.md`,
`docs/methodology/graph.json`, `docs/stories.md`, and new Dossier story
`/Users/cam/Documents/Projects/dossier/docs/stories/story-095-dossier-state-graph-methodology-migration.md`.
Tracked projects affected: `dossier` directly; `storybook`, `doc-web`, and
`cine-forge` only as reference inputs. Risks: blind copy drift, overstating
migration completion, and mishandling the future role of `docs/build-map.md`.
Expected evidence: a queued Dossier migration story covering `state.yaml`,
`graph.json`, `AGENTS.md`, `/setup-methodology`, `/triage`, and `build-map`
role, plus updated Conductor alignment memory and passing Conductor
methodology checks after regeneration.

20260409-1625 — implementation: created Dossier Story 095 at
`/Users/cam/Documents/Projects/dossier/docs/stories/story-095-dossier-state-graph-methodology-migration.md`
as the target-project execution home, added the queued row to
`/Users/cam/Documents/Projects/dossier/docs/stories.md`, updated
`docs/alignments/align-001-methodology-baseline.md` to record the migration
path decision and new follow-up artifact, and moved this story to
`In Progress` so Conductor reflects active supervisor work. Regenerated
Conductor planning surfaces with `make methodology-compile`, then verified
fresh state with `make methodology-check`; `make lint` also passed. No
Conductor skill files or scripts changed, so `make skills-check` and
`make test` were not required for this scope. Dossier already had unrelated
local changes in progress; within Dossier this pass only added Story 095 and
updated `docs/stories.md`.

20260410-0852 — close-out: reran `make methodology-compile`,
`make methodology-check`, `make lint`, `make skills-check`, and
`git diff --check` on the final Conductor close-out pass, then marked this
story `Done` after confirming the queued Dossier migration work and alignment
memory still satisfied the acceptance criteria. Related supervisor follow-up
for inbox-closeout parity was also landed to tracked-project `main` branches
via dedicated `codex/inbox-checkin-landing` worktrees: Dossier `f7f82d7`,
Storybook `9241441`, doc-web `218ae08`, and CineForge `ff82e9d`. This does not
claim the Dossier methodology migration itself is complete; it only confirms
the supervisor-side preparation line is closed with live target-project
landing evidence where applicable.
