---
title: "Interview-First New Project Kickoff"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I4"
  - "I5"
spec_refs:
  - "spec:1.2"
  - "spec:2.2"
  - "spec:4.1"
  - "spec:4.2"
  - "spec:5.3"
decision_refs: []
depends_on: []
category_refs:
  - "registry-routing"
  - "alignment"
  - "story-prep"
  - "memory"
tracked_projects:
  - "conductor"
---

# Story 024 — Interview-First New Project Kickoff

**Priority**: High
**Status**: Done
**Decision Refs**: None yet
**Depends On**: None

## Goal

Create a Conductor-owned greenfield kickoff standard for the recurring moment
after Cam has captured a new project's initial concept but before the repo has
an Ideal/spec/methodology shell.

The standard should give the AI enough guidance to classify the project,
explain available setup surfaces, recommend a minimal package, and interview
Cam before setup. It should prevent the old pattern where a new project copies
another repo's framework wholesale and accidentally inherits irrelevant
overhead.

## Acceptance Criteria

- [x] A new `/init-project` skill exists and is explicitly interview-first.
- [x] The skill tells agents to read preserved raw intake, classify the project,
  explain options, ask material questions, and wait for approval before
  creating target-repo files.
- [x] A Conductor runbook records the standard prompt, project-shape variants,
  setup surface menu, first-story rule, and guardrails.
- [x] `/setup-methodology` and setup runbook language route missing Ideal/spec
  back to the interview-first kickoff rather than autonomous scaffolding.
- [x] Public Conductor guidance mentions `/init-project` as the greenfield
  kickoff loop.
- [x] Methodology and skill checks pass.

## Out of Scope

- Bootstrapping `rpg-map-projector` itself.
- Copying this new skill into tracked product repos.
- Creating a canonical shared core or forcing identical framework text across
  all projects.
- Committing, pushing, or modifying target projects.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Implement the needed doc, skill, script, or log changes
- [x] Update related scout or alignment memory if applicable
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: no script changes; not run
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

- `.agents/skills/init-project/SKILL.md` — new interview-first kickoff skill.
- `docs/runbooks/new-project-kickoff.md` — human/AI runbook for the standard.
- `.agents/skills/setup-methodology/SKILL.md` — clarify that setup depends on
  approved kickoff output.
- `docs/runbooks/setup-methodology.md` — align greenfield setup checklist with
  interview-first kickoff.
- `AGENTS.md` — advertise `/init-project` as a specialized Conductor loop.
- `docs/stories/story-024-interview-first-new-project-kickoff.md` — story
  source of truth and closeout evidence.

## Notes

- Cam clarified that the desired first step is not full automation. The AI
  should know what is possible and form a recommendation, then interview Cam,
  discuss alternatives, incorporate corrections, and only set up the project
  after approval.
- The older memory-backed guidance still applies: greenfield setup should start
  from real Ideal/spec intake, and `/setup-methodology` should not invent
  project meaning from a blank template.

## Plan

1. Add a concise `/init-project` skill that makes the interview and approval
   boundary explicit.
2. Add a runbook with the reusable prompt, variant menu, surface menu, and first
   proof story rule.
3. Patch setup-methodology surfaces so agents route to the kickoff conversation
   instead of scaffolding from missing Ideal/spec.
4. Run Conductor methodology and skill checks.

## Work Log

- 20260527-1205 — story created from Cam's project-kickoff standardization
  request; implementation started in Conductor only.
- 20260527-1215 — added interview-first `/init-project`, new kickoff runbook,
  setup-methodology routing language, and AGENTS workflow pointer; checks:
  `make methodology-compile`, `make methodology-check`, `make lint`,
  `make skills-sync`, `make skills-check`, and `git diff --check`.
- 20260527-1225 — refined `/init-project` for naive blank-repo use: the skill
  now separates Conductor source root from target project root, resolves its
  companion runbook relative to the skill file, and does not require the user
  to point new agents at both files manually.
