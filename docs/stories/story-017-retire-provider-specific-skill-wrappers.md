---
title: "Retire Provider-Specific Skill Wrappers"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I4"
  - "I5"
spec_refs:
  - "spec:2.1"
  - "spec:2.2"
  - "spec:3.2"
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

# Story 017 — Retire Provider-Specific Skill Wrappers

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: None

## Goal

Simplify the distributed skill surface now that Google Antigravity and Gemini
CLI support standard `SKILL.md` skills under `.agents/skills`.

The current package still treats generated Google-specific command wrappers as
part of skill sync. That creates unnecessary churn, stale generated files, and
provider-specific variant logic for what is now a standard skill location.

This story should make `.agents/skills/<skill>/SKILL.md` the only canonical
repo skill surface across Conductor and tracked repos. Provider-specific
surfaces should become either cheap compatibility links or explicitly optional
command aliases. The setup/skill-creation guidance should stop telling agents
to create provider-specific skill variants unless a specific tool still proves
it needs one.

## Acceptance Criteria

- [x] Conductor has an alignment log that records the new skill-surface
      contract from Scout 037: `.agents/skills` is canonical; provider-specific
      wrappers are optional compatibility, not required skill sync.
- [x] `scripts/sync-agent-skills.sh` in Conductor validates canonical
      `.agents/skills` plus cheap compatibility links, and no longer requires
      `.gemini/commands/*.toml` parity as the default skill check.
- [x] If slash-command aliases are still useful, they are separated into an
      explicit optional generator/check instead of being described as skill
      wrappers.
- [x] Conductor's `setup-methodology` guidance no longer says cross-CLI wrapper
      generation is a required public-skill-surface step.
- [x] Conductor's setup checklist, setup runbook, repo checks, and any
      skill-creation or learning-candidate guidance no longer require
      provider-specific skill variants when standard `SKILL.md` discovery is
      sufficient.
- [x] The build inventories each tracked repo for local skill-sync scripts,
      setup-methodology variants, skill-creation/setup guidance, generated
      `.gemini/commands` files, and existing checks that count Gemini wrappers.
- [x] Each tracked repo receives the same meaning-preserving contract update in
      an isolated worktree: canonical `.agents/skills`, optional aliases, and
      no mandatory provider-specific skill variants.
- [x] Repo-local checks pass, or pre-existing unrelated failures are recorded
      with exact commands and boundaries.
- [x] At least one Google-side smoke is attempted after workspace trust is
      handled: Gemini CLI or Antigravity CLI should list workspace skills from
      `.agents/skills`, or the blocker should be recorded precisely.
- [x] Conductor methodology outputs are regenerated and checked.

## Out of Scope

- Creating a central canonical harness repo or making Conductor the source of
  all skill text.
- Removing provider-specific command aliases from a repo that proves it still
  needs them for typed slash-command UX.
- Changing the behavior of individual skills except where they discuss skill
  sync, provider-specific variants, or setup/creation of skills.
- Updating user-level global skills outside the tracked repos.
- Landing target-repo branches, commits, or pushes without an explicit closeout
  request.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, Scout 037, and ADR context.
- [x] Inventory Conductor skill surfaces:
  - [x] `scripts/sync-agent-skills.sh`
  - [x] `Makefile` and `scripts/repo_checks.py`
  - [x] `.agents/skills/setup-methodology/SKILL.md`
  - [x] `.agents/skills/learning-candidate/SKILL.md`
  - [x] setup checklist and setup runbook surfaces
  - [x] any local guidance that tells agents to create provider-specific skill
        variants or generated skill wrappers
- [x] Define the new public skill contract:
  - [x] canonical skill package: `.agents/skills/<name>/SKILL.md` plus optional
        `scripts/`, `references/`, `assets/`, and templates
  - [x] compatibility links: cheap symlinks only where a tool still benefits
  - [x] optional aliases: command wrappers are named and checked separately
  - [x] validation wording distinguishes canonical skills, compatibility links,
        optional aliases, and drift
- [x] Patch Conductor scripts, skills, runbooks, and checks to match the new
      contract.
- [x] Create or update alignment memory and index entries for the
      cross-project recommendation.
- [x] Run a local Google-side smoke after workspace trust is handled, or record
      the exact trust/install blocker.
- [x] Create isolated target-repo worktrees for Dossier, Storybook, doc-web,
      CineForge, Board Game Ingester, Robo Rally, and Echo Forge.
- [x] In each target repo, patch local skill-sync scripts, setup skills,
      runbooks/checklists, package scripts, and generated surfaces as needed.
- [x] Run required Conductor checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] `make skills-check`
  - [x] `make test` if scripts or repo checks changed
  - [x] `git diff --check`
- [x] Run each target repo's native skill/methodology checks plus
      `git diff --check`.
- [x] Search docs and update any related references to "Gemini wrappers",
      "cross-CLI wrappers", provider-specific skill variants, or wrapper parity.
      Historical docs still mention older wrapper rollouts where that history
      is the record, but live skills, setup, runbook, fact, and graph surfaces
      now use canonical skills, compatibility links, and optional aliases.
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

- `scripts/sync-agent-skills.sh` — stop making Gemini wrapper parity the
  default skill-sync proof; preserve only canonical skills and cheap
  compatibility links unless aliases are explicitly requested.
- `Makefile` and `scripts/repo_checks.py` — keep repo checks aligned with the
  new skill-sync contract.
- `.agents/skills/setup-methodology/SKILL.md` — remove mandatory wrapper-sync
  language and update package setup guidance for standard `.agents/skills`.
- `.agents/skills/learning-candidate/SKILL.md` — replace "sync generated
  wrappers if needed" with the new canonical/compatibility/alias distinction.
- `docs/setup-checklist.md` and `docs/runbooks/setup-methodology.md` — update
  setup proof language.
- `docs/alignments/` and `docs/align-projects.md` — record the cross-project
  recommendation and rollout evidence.
- `docs/stories/story-017-retire-provider-specific-skill-wrappers.md` — source
  of truth and work log.
- Generated methodology surfaces after compile: `docs/stories.md` and
  `docs/methodology/graph.json`.
- Target repo equivalents only where local inventory proves the surface exists.

## Notes

- Trigger: Scout 037 found that Google Antigravity and Gemini CLI now support
  standard `SKILL.md` skills under `.agents/skills`, so the old
  `.gemini/commands/*.toml` wrapper generation is no longer needed for skill
  discovery.
- The local Gemini smoke during the scout was inconclusive because this
  worktree was not trusted by Gemini CLI; the build should handle trust or
  record that blocker before treating the smoke as failed.
- ADR-001 still applies: Conductor supervises and compares distributed
  surfaces; it does not become a canonical harness core.
- ADR-002 still applies: record the portable recommendation in alignment
  memory, then let target repos own their local adaptation.
- The user's explicit scope includes both existing skills and the skill/setup
  surface that creates skills or provider-specific variants. If a repo has no
  such local skill-creation surface, record it as absent rather than inventing
  one.

## Plan

Build plan approved by Cam's "proceed with building the story" instruction:

1. Refresh the Conductor worktree from `origin/main` and preserve the existing
   Story 017 / Scout 037 edits.
2. Patch Conductor first: script/check contract, setup-methodology,
   learning-candidate, checklist/runbook wording, and alignment memory.
3. Run Conductor compile/checks and one Google-side skill discovery smoke.
4. Inventory target repos from isolated worktrees and apply the same semantic
   contract only to surfaces that exist locally.
5. Validate each repo with its own skill/methodology checks and whitespace
   check.
6. Update this story and the alignment log with exact rollout evidence.

## Work Log

20260519-2257 — story-created: created Story 017 from Scout 037 and Cam's
follow-up request. Scope is provider-specific skill wrapper retirement across
Conductor and tracked repos, including setup/skill-creation guidance that still
creates or requires provider-specific skill variants.

20260519-2310 — main-refresh: stashed local Story 017 / Scout 037 edits, fetched
`origin/main`, moved the detached worktree from `e85a7ba` to `7cf737e`, resolved
the scout index conflict by preserving upstream Scout 035/036 and renumbering
the Antigravity scout to Scout 037, then created branch
`codex/retire-provider-specific-skill-wrappers` for the build.

20260519-2320 — conductor-contract-patched: removed Conductor's required
`.gemini/commands/*.toml` command wrappers, updated
`scripts/sync-agent-skills.sh` so default checks validate canonical
`.agents/skills` plus compatibility links, added optional alias sync/check
modes, refreshed setup-methodology, learning-candidate, setup checklist, and
setup runbook wording, and created Alignment 035.

20260519-2328 — google-smoke: `gemini --skip-trust skills list` discovered all
17 workspace skills from `.agents/skills`. A temporary `.gemini/skills` symlink
caused duplicate-skill conflict warnings, proving Gemini already reads
`.agents/skills`; the default contract keeps Google support direct and does not
create that symlink.

20260519-2337 — target-rollout: created isolated worktrees on
`codex/skill-wrapper-retirement-20260519` for Dossier, Storybook, doc-web,
CineForge, Board Game Ingester, Robo Rally, and Echo Forge. Each target now
keeps `.agents/skills` as canonical, refreshes only the cheap compatibility
links by default, ignores `.gemini/commands/` as optional generated alias
output, and removes the tracked mandatory `.gemini/commands/*.toml` files.
Patched each repo's `create-cross-cli-skill`, setup-methodology,
learning-candidate, triage/fact, runbook, and graph/test surfaces where local
inventory proved those surfaces existed.

20260519-2346 — target-validation: target checks passed with exact boundaries:
Dossier `make skills-check methodology-compile methodology-check
triage-facts-check` plus `git diff --check` using the Dossier venv; Storybook
`pnpm methodology:compile`, `scripts/sync-agent-skills.sh --check`,
`pnpm methodology:check`, `pnpm triage:facts:check`, and `git diff --check`;
doc-web `make skills-check methodology-compile methodology-check
triage-facts-check lint` and `git diff --check`; CineForge `make skills-check
triage-facts-check`, `npm run methodology:compile`, `npm run
methodology:check`, and `git diff --check`; Board Game Ingester `make
skills-check methodology-compile methodology-check triage-facts-check lint`
and `git diff --check`; Robo Rally `npm run methodology:compile`, `npm run
methodology:check`, `npm run skills:check`, `npm run triage-facts:check`, and
`git diff --check`. Echo Forge passed `npm run methodology:compile`, `npm run
methodology:check`, `npm run skills:check`, direct text/JSON
`node scripts/triage-facts.mjs` smokes, and `git diff --check`; its configured
`npm run triage-facts:check` is blocked in this worktree because `vitest` is
not installed.

20260519-2350 — conductor-validation: ran `./scripts/sync-agent-skills.sh`,
`make methodology-compile`, `make methodology-check`, `make lint`, `make
skills-check`, `make test`, and `git diff --check`. All passed with the new
canonical-skill/compatibility-link contract and regenerated Conductor
methodology outputs.

20260519-2359 — validate-loop-fixes: `/loop-verify` and `codex review
--uncommitted` found material closeout gaps. Patched Conductor
`scripts/sync-agent-skills.sh` so default checks verify compatibility-link
targets and `--check-aliases` verifies alias names plus content, not just file
counts. Restored generated Python bytecode noise, checked the parent Conductor
validation task, and patched doc-web's `scripts/methodology_graph.py` so its
active-surface list includes `create-cross-cli-skill`. Re-ran Conductor
`sync-agent-skills`, methodology, lint, skills, test, and diff checks; re-ran
doc-web methodology, triage facts, lint, combined methodology/triage tests, and
diff checks. All passed.

20260520-0014 — strict-validation-close: ran a fresh strict `/loop-verify`
candidate-close round after the material fixes. Conductor/story, target
skill-sync, target generated-output, and worktree-hygiene shards returned no
material Story 017 findings. `codex review --uncommitted` also returned no
actionable regressions after the link-target and alias-content fixes. The
expanded Dossier unit probe found an unchanged main-branch drift in
`tests/unit/test_methodology_graph.py`: `python -m pytest
tests/test_triage_facts.py tests/unit/test_methodology_graph.py -q` fails
because the test still expects W8 retry triggers
`["architecture-change", "new-subject-model"]` while the current graph and
generator use `["materially-new-local-helper",
"seed-pass-reuse-with-quality-preservation"]`. The affected test, generator,
and graph files have no Story 017 diff against `origin/main`, so this is
recorded as a pre-existing Dossier follow-up and not a blocker to the skill
wrapper retirement rollout.

20260520-0022 — story-closed: marked Story 017 Done after validation confirmed
the build met its acceptance criteria. Closeout evidence: final Conductor
`make methodology-compile`, `make methodology-check`, `make lint`, `make
skills-check`, `make test`, and `git diff --check` passed; strict loop-verify
found no remaining Story 017 material issues; residual Echo Forge and Dossier
items are recorded as target-local environment/test drift outside this rollout.

20260520-0038 — target-main-landed: `/finish-and-push` committed and pushed the
seven linked target repos, then fast-forwarded each target `main`: Dossier
`6f309fd`, Storybook `e295fa3`, doc-web `99450a3`, CineForge `0b5ae05`, Board
Game Ingester `b822102`, Robo Rally `a0d8029`, and Echo Forge `7766b8e`.
Storybook's untracked GEDCOM import and CineForge's existing
`docs/deploy-log.md` edit were left untouched as unrelated primary-worktree
state.
