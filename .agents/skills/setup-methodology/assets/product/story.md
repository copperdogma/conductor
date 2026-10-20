---
title: "TITLE"
status: "Draft"
priority: "PRIORITY"
ideal_refs: []
spec_refs: []
decision_refs: []
depends_on: []
category_refs: []
tracked_projects: []
---

# Story NNN — TITLE

**Priority**: PRIORITY
**Status**: Draft
**Decision Refs**: None yet
**Depends On**: None

## Goal

{What this story changes and why it matters.}

## Acceptance Criteria

- [ ] {Concrete result 1}
- [ ] {Concrete result 2}
- [ ] {Concrete result 3}

## Out of Scope

- {What this story explicitly does not do}

## Tasks

- [ ] Read the relevant Ideal, Spec, state, graph, and decision context
- [ ] Implement the needed doc, skill, script, or log changes
- [ ] Update related decisions, research, and evidence if applicable
- [ ] Run required checks:
  - [ ] `make methodology-compile`
  - [ ] `make methodology-check`
  - [ ] Run project-provided lint gates when available
  - [ ] If agent tooling changed: `make skills-check`
  - [ ] Run applicable project tests for changed behavior; no absent test command is required
- [ ] Search docs and update any related surfaces
- [ ] Verify acceptance against the project Ideal, Spec, and relevant decisions

## Workflow Gates

- [ ] Build complete
- [ ] Validation complete or explicitly skipped by user
- [ ] Story marked done via `/mark-story-done`

## Files to Modify

- {path} — {reason}

## Notes

{Context, constraints, references}

## Plan

{Filled in during `/build-story`}

## Work Log

{YYYYMMDD-HHMM — action: result, evidence, next step}
