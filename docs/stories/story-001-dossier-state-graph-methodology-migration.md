---
title: "Prepare Dossier State/Graph Methodology Migration"
status: "Pending"
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
**Status**: Pending
**Decision Refs**: ADR-001
**Depends On**: None

## Goal

Turn the alignment finding about Dossier's outdated build-map-first planning
surface into execution-ready adoption work. Conductor should compare Dossier
against the newer state/graph-first methodology package used elsewhere, decide
what ports cleanly versus what stays Dossier-specific, and queue concrete
target-project work so the migration can actually happen in Dossier.

## Acceptance Criteria

- [ ] Conductor records the specific Dossier methodology gaps against the
      state/graph-first package, including the missing or stale planning
      artifacts and the likely reference surfaces to port from.
- [ ] Conductor produces explicit target-project adoption work for Dossier that
      covers `docs/methodology/state.yaml`, `docs/methodology/graph.json`,
      `AGENTS.md`, `/setup-methodology`, `/triage`, and the intended role of
      `docs/build-map.md` after migration.
- [ ] Conductor memory reflects this as an active work line rather than an
      unresolved alignment note, and the generated backlog surfaces stay current.

## Out of Scope

- Claiming Dossier is migrated before Dossier has its own validated story,
  patches, or applied changes
- Forcing exact textual sync between Dossier and Storybook, doc-web, or
  CineForge
- Deciding unrelated cross-project methodology differences

## Tasks

- [ ] Read the relevant Ideal, Spec, state, graph, and decision context
- [ ] Re-read Alignment 001 plus Dossier's current methodology surfaces to
      confirm the missing state/graph artifacts and current build-map-first
      assumptions
- [ ] Compare Dossier's methodology package against the strongest reference
      implementation(s) among Storybook, doc-web, and CineForge
- [ ] Decide what should migrate as-is, what needs Dossier-specific adaptation,
      and whether `docs/build-map.md` stays as a generated/supporting surface
- [ ] Create the Dossier target-project story or equivalent execution-ready work
      item for the migration
- [ ] Update related scout or alignment memory if applicable
- [ ] Run required checks:
  - [ ] `make methodology-compile`
  - [ ] `make methodology-check`
  - [ ] `make lint`
  - [ ] If agent tooling changed: `make skills-check`
  - [ ] If scripts or repo checks changed: `make test`
- [ ] Search docs and update any related surfaces
- [ ] Verify Conductor tenets:
  - [ ] I1 — Meaning over text
  - [ ] I2 — Distributed ownership
  - [ ] I3 — Recommendation-first supervision
  - [ ] I4 — Honest divergence
  - [ ] I5 — Minimal overhead

## Workflow Gates

- [ ] Build complete
- [ ] Validation complete or explicitly skipped by user
- [ ] Story marked done via `/mark-story-done`

## Files to Modify

- `docs/stories/story-001-dossier-state-graph-methodology-migration.md` —
  track the supervisor work line
- `docs/alignments/align-001-methodology-baseline.md` — link the alignment
  finding to active follow-up work
- `docs/methodology/graph.json` — generated story index
- `docs/stories.md` — generated story backlog view
- `/Users/cam/Documents/Projects/dossier/docs/stories/` — target-project
  migration story or equivalent queued work item

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

{Filled in during `/build-story`}

## Work Log

20260409-1523 — story creation: created after Alignment 001 and direct user
priority setting confirmed Dossier's state/graph migration as the top
cross-project follow-up; next step is to prepare Dossier's target-project
migration work from the supervisor side.
