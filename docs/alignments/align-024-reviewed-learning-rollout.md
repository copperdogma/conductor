# Alignment 024 — Reviewed Learning Rollout

Date: 2026-05-05

## Focus

Roll Conductor's reviewed learning-candidate workflow from Story 008 into the
tracked project repos after Conductor-local refinement and loop verification.

The portable surfaces are:

- `.agents/skills/learning-review/SKILL.md`
- `.agents/skills/learning-candidate/SKILL.md`
- `docs/learning-candidates/` template, README, and examples
- selected closeout hooks in `/build-story`, `/validate`, `/finish-and-push`,
  and `/loop-verify`

## Classification

Portable improvement with local adaptation.

## Decision

Sync the workflow meaning across tracked repos now, but keep implementation
lightweight and repo-local.

This rollout should add a reviewed learning lane that lets agents notice
durable workflow corrections, draft inspectable candidates when evidence is
real, and leave live skills, memory, policy, and methodology unchanged until
Cam explicitly accepts or promotes a candidate.

This rollout should not:

- introduce an always-on daemon or background learning service
- create a canonical shared harness repo
- require exact text identity across locally adapted skills
- promote candidates during ordinary closeout
- treat clean work, novelty, vibes, or generic process advice as candidate
  evidence

## Target Projects

| Repo | Rollout status |
| --- | --- |
| Dossier | Implemented in isolated worktree |
| Storybook | Implemented in isolated worktree |
| doc-web | Implemented in isolated worktree |
| CineForge | Implemented in isolated worktree |
| Board Game Ingester | Implemented in isolated worktree |
| Robo Rally | Implemented in isolated worktree |
| Echo Forge | Implemented in isolated worktree |

## Implementation Worktrees

Target repos were edited in isolated worktrees under:

`/Users/cam/.codex/worktrees/story008-reviewed-learning/`

Branch:

`codex/story-008-reviewed-learning-rollout`

Per-repo worktrees:

- Dossier: `/Users/cam/.codex/worktrees/story008-reviewed-learning/dossier`
- Storybook: `/Users/cam/.codex/worktrees/story008-reviewed-learning/storybook`
- doc-web: `/Users/cam/.codex/worktrees/story008-reviewed-learning/doc-web`
- CineForge: `/Users/cam/.codex/worktrees/story008-reviewed-learning/cine-forge`
- Board Game Ingester: `/Users/cam/.codex/worktrees/story008-reviewed-learning/boardgame-ingester`
- Robo Rally: `/Users/cam/.codex/worktrees/story008-reviewed-learning/roborally`
- Echo Forge: `/Users/cam/.codex/worktrees/story008-reviewed-learning/echo-forge`

## Implementation Result

Each target repo now has:

- `.agents/skills/learning-review/SKILL.md`
- `.agents/skills/learning-candidate/SKILL.md`
- `docs/learning-candidates/README.md`
- `docs/learning-candidates/template.md`
- `docs/learning-candidates/examples/candidate-user-correction.md`
- `docs/learning-candidates/examples/no-candidate-clean-validation.md`
- generated Gemini wrappers for `learning-review` and `learning-candidate`
- narrow reviewed-learning hooks in `/build-story`, `/validate`,
  `/finish-and-push`, and `/loop-verify`

The product-repo candidate contract is intentionally repo-local:

- local candidates may promote local skills, runbooks, methodology docs, story
  workflow, planning notes, or repo-local workflow surfaces
- files outside the repo and global memory are not promotion targets for
  repo-local candidates
- cross-project methodology promotion still routes through Conductor alignment
  or story approval before any affected project changes
- ordinary successful work still skips the detector

## Loop Verification Plan

Used `/loop-verify` over disjoint shards:

- Conductor supervisor artifacts and generated surfaces
- Dossier and Storybook rollout patches
- doc-web and CineForge rollout patches
- Board Game Ingester, Robo Rally, and Echo Forge rollout patches

Material findings reset the full loop. Minor wording or formatting cleanups do
not reset the full loop if the local check passes and the secondary effect is
confined to that shard.

Loop result: converged after Round 4.

- Round 1 found material stale Conductor wording, target wording, lifecycle,
  and README/skill mismatches.
- Round 2 found material promote-semantics and target-repo outside-repo routing
  issues.
- Round 3 found material repo-local validation-command and memory-promotion
  issues.
- Round 4 returned `RESULT: no-issue` across all four original shards.

Learning-review result for the loop: `RESULT: no-candidate`. The loop findings
were all rollout correctness issues already fixed directly in Story 008 scope,
not separate reusable workflow candidates.

## Validation Plan

Run the narrowest honest checks each repo supports, preferring existing skill
sync and methodology checks before broader lint/test commands:

- Conductor: `PYTHONDONTWRITEBYTECODE=1 make methodology-compile`,
  `PYTHONDONTWRITEBYTECODE=1 make methodology-check`, `make skills-check`,
  `PYTHONDONTWRITEBYTECODE=1 make lint`, `PYTHONDONTWRITEBYTECODE=1 make test`,
  `git diff --check`
- Dossier: `./scripts/sync-agent-skills.sh --check`,
  `PYTHON=/Users/cam/miniconda3/bin/python make methodology-check`,
  `git diff --check`
- Storybook: `./scripts/sync-agent-skills.sh --check`,
  `npm run methodology:check`, `npm run methodology:test`,
  `npm run triage:facts:check`, `npm run lint`, `git diff --check`
- doc-web: `make skills-check`, `make methodology-check`, `make lint`,
  `git diff --check`
- CineForge: `make skills-check`, methodology check, `git diff --check`
- Board Game Ingester: `make skills-check`, `make methodology-check`,
  `make lint`, `git diff --check`
- Robo Rally: repo-local validation command, `git diff --check`
- Echo Forge: skills, methodology, lint, triage-facts checks where available,
  `git diff --check`

Validation result: passed.

Known validation notes:

- Dossier methodology check reports existing non-local ADR/compromise and
  legacy-metadata warnings while confirming the graph is current.
- CineForge methodology check reports existing architecture audit and UI scout
  freshness warnings while confirming methodology outputs are current.
- Storybook and Echo Forge isolated worktrees use temporary symlinks to the
  primary checkout `node_modules` for validation; those symlinks are removed
  after the checks.

## Follow-Up

This alignment records the approved rollout scope and validated worktree
implementation. Landing the target worktrees still requires the normal
check-in/finish flow; this note does not imply the target branches have already
been committed, merged, or pushed.
