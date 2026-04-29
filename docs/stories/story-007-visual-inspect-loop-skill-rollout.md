---
title: "Visual Inspect Loop Skill Rollout"
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
  - "spec:2.2"
  - "spec:4.1"
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
  - "storybook"
  - "doc-web"
  - "cine-forge"
  - "boardgame-ingester"
  - "roborally"
  - "echo-forge"
---

# Story 007 - Visual Inspect Loop Skill Rollout

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: None

## Goal

Roll doc-web's new `/visual-inspect-loop` skill into every tracked repo that
owns visual, rendered, image, screenshot, crop, UI, or visual-golden quality
work, while keeping repos that do not own visual artifacts out of scope.

The user explicitly called out that this should include backend-looking repos
when their correctness depends on images, rendered artifacts, or image-backed
goldens. The rollout should preserve the key behavior from doc-web: personally
inspect the source and result first, record the concrete visual failure, turn it
into a generic failure class, patch the pipeline, rerun, and reinspect before
claiming quality.

## Acceptance Criteria

- [x] The doc-web source skill at
      `/Users/cam/Documents/Projects/doc-web/.agents/skills/visual-inspect-loop/SKILL.md`
      is reviewed against Conductor's Ideal/spec and captured in alignment
      memory.
- [x] A selective repo decision is recorded for every tracked project:
      `sync now`, `sync partially`, `source already has it`, or `defer`.
- [x] The skill is added in isolated target-repo worktrees, not in dirty primary
      checkouts, for the selected visual-surface repos:
      Storybook, CineForge, Board Game Ingester, Robo Rally, and Echo Forge.
- [x] doc-web is treated as the source repo and is not overwritten by the
      rollout.
- [x] Dossier is explicitly deferred unless fresh evidence shows it owns a
      visual/image/rendered-document artifact lane rather than text/entity
      goldens only.
- [x] Each touched repo keeps the skill discoverable through its existing skill
      sync or wrapper surfaces, with repo-native checks passing or any unrelated
      noise called out.
- [x] Repos with a `/ui-scout` skill in this rollout scope instruct UI Scout to
      call `/visual-inspect-loop` when a finding or inline fix depends on
      visual/rendered correctness.
- [x] The Conductor alignment entry records target worktree paths, branch name,
      base, validation commands, and per-repo result after execution.

## Out of Scope

- Making Conductor the canonical copy of this skill.
- Editing any target project's primary checkout.
- Committing or pushing target-repo changes without explicit approval.
- Applying this skill to audio-quality-only work in Echo Forge, text/entity-only
  golden work in Dossier, or non-visual code review.
- Changing the skill into a generic validation or loop-verify replacement.

## Tasks

- [x] Read Conductor Ideal/spec/state and the doc-web source skill.
- [x] Inspect tracked project registry and current target checkout status.
- [x] Record the recommendation-first alignment decision.
- [x] Create isolated target worktrees under
      `/Users/cam/.codex/worktrees/visual-inspect-loop/`.
- [x] In each selected target worktree, copy or adapt the doc-web
      `/visual-inspect-loop` skill without flattening local differences.
- [x] Add generated wrappers or sync outputs only where the repo's existing
      checks require them.
- [x] Update Storybook and Echo Forge `/ui-scout` skills to use
      `/visual-inspect-loop` for visual/rendered findings and inline visual
      fixes.
- [x] Run target repo validation:
  - [x] Storybook: `./scripts/sync-agent-skills.sh --check`,
        `npm run methodology:check`, `git diff --check`
  - [x] CineForge: `make skills-check`, `npm run methodology:check`,
        `git diff --check`
  - [x] Board Game Ingester: `make skills-check`, `make methodology-check`,
        `make lint`, `git diff --check`
  - [x] Robo Rally: `npm run validate`, `git diff --check`
  - [x] Echo Forge: `npm run skills:check`, `npm run methodology:check`,
        `git diff --check`
- [x] Update Alignment 020 with actual worktree paths, branches, validation
      evidence, and any repo-local adaptation.
- [x] Update this story work log with concrete evidence.
- [x] Run Conductor checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If Conductor agent tooling changed: not required
  - [x] If scripts or repo checks changed: not required
- [x] Verify Conductor tenets:
  - [x] I1 - Meaning over text
  - [x] I2 - Distributed ownership
  - [x] I3 - Recommendation-first supervision
  - [x] I4 - Honest divergence
  - [x] I5 - Minimal overhead

## Workflow Gates

- [x] Build complete
- [x] Validation complete or explicitly skipped by user
- [x] Story marked done via `/mark-story-done`

## Files to Modify

- `docs/alignments/align-020-visual-inspect-loop-skill-rollout.md` - repo
  selection, classification, and rollout evidence.
- `docs/align-projects.md` - index the new alignment entry.
- `docs/stories/story-007-visual-inspect-loop-skill-rollout.md` - story source
  of truth and work log.
- Target worktrees, after approval:
  - `.agents/skills/visual-inspect-loop/SKILL.md`
  - repo-native generated wrappers or skill indexes if required by checks

## Notes

- Source skill:
  `/Users/cam/Documents/Projects/doc-web/.agents/skills/visual-inspect-loop/SKILL.md`.
- Primary target checkouts are currently dirty or in-flight, so target edits
  must use isolated worktrees.
- This story intentionally excludes Dossier for now. Dossier owns text/entity
  extraction goldens and evals, but the current evidence does not show a
  maintained visual/image/rendered-artifact lane comparable to doc-web,
  Storybook, CineForge, Board Game Ingester, Robo Rally, or Echo Forge UI work.
- doc-web already has the skill in the checkout named by the user and should be
  treated as the source of truth for this rollout.

## Plan

1. Start from `origin/main` for each selected target repo and create one
   isolated worktree per repo under
   `/Users/cam/.codex/worktrees/visual-inspect-loop/<project-key>`.
2. Use branch `codex/visual-inspect-loop-skill-rollout` in each target worktree
   unless a repo already has that branch.
3. Copy the doc-web skill into each selected repo as
   `.agents/skills/visual-inspect-loop/SKILL.md`.
4. Inspect each repo's existing skill sync/check surfaces and add generated
   wrappers only if that repo expects them.
5. Run the narrow validation commands listed above. Do not treat unrelated
   primary-checkout dirtiness as rollout evidence.
6. Update Alignment 020 with the final per-repo execution result and this story
   with the work log.
7. Stop before commit/push unless Cam explicitly approves that closeout.

## Work Log

20260429-1550 - created: Routed the user's doc-web
`visual-inspect-loop` note into a recommendation-first Conductor alignment and
story. Reviewed Conductor Ideal/spec/state, projects registry, the doc-web
source skill, current skill inventories, and target primary checkout statuses.
Decision: prepare a selective rollout to Storybook, CineForge, Board Game
Ingester, Robo Rally, and Echo Forge; treat doc-web as source; defer Dossier
until it owns a concrete visual/rendered/image artifact lane. Next step: wait
for explicit approval to create isolated target worktrees and apply the skill.

20260429-1600 - implemented and validated: Created isolated target worktrees at
`/Users/cam/.codex/worktrees/visual-inspect-loop/storybook`,
`/Users/cam/.codex/worktrees/visual-inspect-loop/cine-forge`,
`/Users/cam/.codex/worktrees/visual-inspect-loop/boardgame-ingester`,
`/Users/cam/.codex/worktrees/visual-inspect-loop/roborally`, and
`/Users/cam/.codex/worktrees/visual-inspect-loop/echo-forge`, all on branch
`codex/visual-inspect-loop-skill-rollout` from `origin/main`. Added
`.agents/skills/visual-inspect-loop/SKILL.md` plus generated
`.gemini/commands/visual-inspect-loop.toml` in each target repo via that repo's
`scripts/sync-agent-skills.sh`. Base commits: Storybook `e4e4bc2`, CineForge
`fb32223`, Board Game Ingester `8be1912`, Robo Rally `b902e62`, Echo Forge
`82d0674`. Fresh target validation passed: Storybook
`./scripts/sync-agent-skills.sh --check`, `npm run methodology:check`,
`git diff --check`; CineForge `make skills-check`,
`npm run methodology:check`, `git diff --check`; Board Game Ingester
`make skills-check`, `make methodology-check`, `make lint`,
`git diff --check`; Robo Rally `npm run validate`, `git diff --check`; Echo
Forge `npm run skills:check`, `npm run methodology:check`,
`git diff --check`. Used temporary `git add -N` before final `git diff --check`
so the untracked new files were checked, then reset the index; no target files
are staged. CineForge still reports its existing methodology warnings about
architecture audit and UI-scout freshness, but the check exits successfully and
the warnings are unrelated to this rollout. Updated Alignment 020 with
execution evidence. Next step: mark Story 007 done and check in/push the
Conductor and target-repo branches if Cam wants the rollout landed.

20260429-1605 - UI Scout integration: Updated the two rollout-scope repos that
already own a `/ui-scout` skill, Storybook and Echo Forge, so UI Scout remains
the top-level exploratory product-flow skill while `/visual-inspect-loop` owns
the narrow inspect -> generic failure class -> patch -> rerun -> reinspect loop
for visual/rendered findings and inline visual fixes. Fresh checks passed:
Storybook `./scripts/sync-agent-skills.sh --check`,
`npm run methodology:check`, `git diff --check`; Echo Forge
`npm run skills:check`, `npm run methodology:check`, `git diff --check`.
Temporary `git add -N` was used before `git diff --check` so the still-untracked
new visual-inspect files were included in whitespace validation, then the index
was reset. Next step remains closeout if Cam wants the rollout landed.

20260429-1608 - story-done: Marked Story 007 Done after confirming all
acceptance criteria, target repo validation, UI Scout integration, Alignment
020 evidence, and Conductor checks were complete. Added the changelog entry and
refreshed generated methodology surfaces. Next step: check in and push
Conductor plus target repo landings to `main`.
