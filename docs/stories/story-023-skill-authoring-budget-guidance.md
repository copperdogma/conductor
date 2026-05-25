---
title: "Roll Out Skill Authoring Budget Guidance"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I5"
spec_refs:
  - "spec:2.1"
  - "spec:2.2"
  - "spec:4.2"
  - "spec:5.1"
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

# Story 023 — Roll Out Skill Authoring Budget Guidance

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: None

## Goal

Carry Scout 041 and Alignment 039's skill-budget lesson into the places where
new repo-local skills are actually written.

The rollout should not install Conductor's full `skill-surface-audit` helper in
every target repo. Conductor remains the portfolio audit owner. The target repos
should instead get small authoring guidance in their `create-cross-cli-skill`
and, where present, `improve-skill` surfaces so agents keep `SKILL.md`
frontmatter descriptions token-efficient at creation and maintenance time.

This prevents skill-surface bloat before it exists while preserving distributed
repo ownership.

## Acceptance Criteria

- [x] Each tracked target repo with `create-cross-cli-skill` receives concise
      description-budget guidance that covers trigger nouns, routing purpose,
      frontmatter length discipline, and where to put longer workflow detail.
- [x] Target repos with `improve-skill` receive a prompt-budget improvement
      pass that asks whether a skill description is doing routing work or just
      prose work.
- [x] Target repos without `improve-skill` are not forced to gain one unless a
      local repo already wants that skill surface for separate reasons.
- [x] Conductor's `skill-surface-audit` remains a central report-only tool; the
      target repos reference it only as an optional cross-repo check after many
      skill changes or before shared-skill rollouts.
- [x] The rollout preserves current provider-wrapper guidance: canonical
      `SKILL.md` packages remain under `.agents/skills`, compatibility links
      are refreshed with the repo's existing sync tool, and optional aliases are
      not reintroduced as required work.
- [x] Target repo changes are made in isolated worktrees/branches, not primary
      checkouts, unless Cam explicitly asks otherwise.
- [x] Each target repo records validation evidence using its native skill
      sync/check and methodology commands where available.
- [x] A final Conductor alignment update records which repos were patched,
      which were deferred, validation evidence, and any local adaptation.

## Out of Scope

- Copying `scripts/skill_surface_audit.py` into every repo.
- Running automatic deletion, disabling, or description rewriting across target
  repos.
- Shortening existing long descriptions as part of this rollout unless the
  authoring-surface patch naturally reveals a small, safe fix.
- Inventing missing `improve-skill` surfaces in doc-web or Board Game Ingester.
- Changing setup-methodology text unless the target repo's existing setup
  surface already carries skill-authoring guidance that would become
  misleading without the new rule.
- Committing, pushing, or landing target repo changes without an explicit
  closeout request.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Compare the current skill-authoring surfaces across tracked repos
- [x] Prepare Alignment 040 with target surfaces, per-project recommendations,
      and rollout constraints
- [x] Create isolated target worktrees and branches from `origin/main`
- [x] Patch each repo's `create-cross-cli-skill` guidance
- [x] Patch each existing `improve-skill` guidance
- [x] Run repo-native skill sync and validation checks
- [x] Record rollout evidence and local deferrals in Alignment 040
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: `make test` not required because no
        scripts or repo-check code changed
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

- `docs/stories/story-023-skill-authoring-budget-guidance.md` — supervisor
  story and rollout work log.
- `docs/alignments/align-040-skill-authoring-budget-guidance.md` — comparison
  evidence and cross-repo rollout plan.
- `docs/align-projects.md` — alignment index.
- Target repos, in isolated worktrees:
  - `.agents/skills/create-cross-cli-skill/SKILL.md` — skill creation guidance.
  - `.agents/skills/improve-skill/SKILL.md` — only where the skill already
    exists.
  - generated skill compatibility/link surfaces only as produced by each repo's
    native `scripts/sync-agent-skills.sh`.

## Notes

- Triggered by Cam's follow-up on Scout 041: the useful target-repo adoption is
  shaping and guidance for token-efficient skills, not repeated per-repo audit
  scripts.
- First inventory found `create-cross-cli-skill` in all seven tracked target
  repos: Dossier, Storybook, doc-web, CineForge, Board Game Ingester,
  RoboRally, and Echo Forge.
- First inventory found `improve-skill` in Dossier, Storybook, CineForge,
  RoboRally, and Echo Forge. doc-web and Board Game Ingester should not gain it
  from this story alone.
- Alignment 039 remains the source for Conductor's audit role and the
  "preserve trigger nouns" cleanup rule.

## Plan

1. Use isolated target worktrees under
   `$HOME/.codex/worktrees/skill-authoring-budget-guidance/<project-key>` with
   `codex/skill-authoring-budget-guidance` branches from `origin/main`.
2. Apply a small shared rubric to every existing `create-cross-cli-skill`:
   - keep `description` routing-focused and concise
   - put trigger nouns up front
   - include domain/action/artifact/tool cues when they decide activation
   - move examples, policy detail, and long workflow prose into the body
   - preserve trigger nouns when shortening existing descriptions
3. Apply the matching maintenance check to each existing `improve-skill`:
   - ask whether frontmatter is doing routing work
   - reject bloat from one-off incidents
   - keep generic skill improvements in skills and app-specific details in
     AGENTS or docs
4. Mention Conductor's `skill-surface-audit` only as an optional central check
   after broad skill edits or before shared-skill rollout.
5. Run each repo's native sync/check commands, then record exact evidence in
   Alignment 040.
6. Return to Conductor, update the story and alignment with rollout results,
   run Conductor checks, and close the story only after target evidence is
   recorded.

## Work Log

20260525-1648 — story-created: created from Cam's approval to turn the
skill-cleaner follow-up into a repo-local skill-authoring guidance rollout.
Prepared the story as pending execution rather than applying target repo edits
in primary checkouts.

20260525-1701 — rollout-applied: created isolated target worktrees under
`/Users/cam/.codex/worktrees/skill-authoring-budget-guidance/` on
`codex/skill-authoring-budget-guidance` branches from `origin/main`, patched
all seven `create-cross-cli-skill` skills and the five existing `improve-skill`
skills, ran each repo's skill sync/check and methodology compile/check, and
recorded validation evidence in Alignment 040. No target primary checkout was
edited. No target repo commit or push was made.

20260525-1704 — conductor-validation: regenerated Conductor methodology
surfaces and ran `make methodology-check`, `make lint`, `make skills-check`, and
`git diff --check`. All passed. `make test` was not required because no
Conductor scripts or repo-check code changed in this story execution pass.

20260525-1706 — validation-sweep: confirmed all seven target worktrees contain
the new `create-cross-cli-skill` description-budget rubric, the five intended
`improve-skill` worktrees contain the maintenance pass, and doc-web plus Board
Game Ingester still do not have `improve-skill`. Skipped `codex review` and
`/loop-verify` because the remaining diffs are docs-only skill guidance and
generated methodology freshness output, with exact surface coverage checked
directly.

20260525-1707 — story-closed: target worktree branches were committed and
pushed to `origin/codex/skill-authoring-budget-guidance`; Alignment 040 records
the commit hashes and validation evidence. Story 023 is marked done after
current-pass validation.
