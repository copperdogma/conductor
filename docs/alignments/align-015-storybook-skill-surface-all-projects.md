# Alignment 015 — Storybook Skill Surface Across Tracked Apps

**Date:** 2026-04-24

## Focus

Compare all six tracked apps against Storybook's recent methodology skill
updates, with special attention to:

- `.agents/skills/init-project/SKILL.md`
- `.agents/skills/setup-methodology/SKILL.md`
- `.agents/skills/triage/SKILL.md`
- `.agents/skills/create-eval/SKILL.md`
- `.agents/skills/improve-eval/SKILL.md`
- `.agents/skills/triage-evals/SKILL.md`
- `.agents/skills/triage-stories/SKILL.md`
- `.agents/skills/create-story/SKILL.md`
- `.agents/skills/build-story/SKILL.md`
- `docs/runbooks/setup-methodology.md`
- `docs/runbooks/triage.md`
- `.gemini/commands/*.toml`
- `scripts/sync-agent-skills.sh`

Projects compared:

- Dossier
- Storybook
- Doc Web
- CineForge
- Board Game Ingester
- Echo Forge

## Observations

Storybook has three recent portable methodology improvements:

1. `init-project` now owns greenfield idea intake before setup. It interviews
   for project meaning, preserves raw intake, drafts `docs/ideal.md` and
   `docs/spec.md`, checks late-arriving ideas for Ideal/spec placement, and
   only then hands off to `setup-methodology`.
2. `triage` now runs a completion-sanity check before accepting a
   "nothing ready" or maintenance-only recommendation. It must not imply a repo
   is feature-complete while v1/MVP, input-coverage, future/unplanned, or inbox
   gaps still prove otherwise.
3. The setup, triage, eval, story, and build skills now preserve the eval
   ladder before creating implementation backlog. The portable rule is: keep a
   root Ideal eval or explicit deferral, record parent failures, create child
   evals when failure modes are vague, and only package story work once the
   next ladder node is clear.

All six projects have coherent cross-CLI wrapper generation:

- Dossier: `skills-check: OK (27 skills, 27 gemini wrappers)`
- Doc Web: `skills-check: OK (25 skills, 25 gemini wrappers)`
- CineForge: `skills-check: OK (32 skills, 32 gemini wrappers)`
- Storybook: `skills-check: OK (31 skills, 31 gemini wrappers)`
- Board Game Ingester: `skills-check: OK (25 skills, 25 gemini wrappers)`
- Echo Forge: `skills-check: OK (29 skills, 29 gemini wrappers)`

The drift is content-level methodology guidance, not broken sync tooling.

Several target checkouts are in active local work:

- Doc Web is behind `origin/main` by two commits.
- CineForge, Storybook, Board Game Ingester, and Echo Forge have dirty working
  trees.
- Dossier is clean.

Any cross-repo sync should therefore use isolated task worktrees for target
repo edits unless the user explicitly asks to work in the primary checkout.

## Project Matrix

| Project | Current skill surface | Classification | Recommendation |
| --- | --- | --- | --- |
| Storybook | Source of the current changes: greenfield `init-project`, setup Ideal/spec preflight, completion-sanity triage, and eval-ladder guidance across setup/triage/eval/story/build skills. | Source / keep local | No sync needed except as the reference implementation. |
| Echo Forge | Has `init-project`, setup Ideal/spec preflight, generated wrappers, and completion-sanity triage. It lacks Storybook's newest eval-ladder guidance in init/setup/triage/eval/story/build surfaces. | Portable improvement, partial sync | Port eval-ladder additions only; keep Echo Forge-native wording and selective Storybook import boundary. |
| CineForge | Has an older `init-project` that bootstraps a repo from reference patterns and an older setup package. It lacks completion-sanity triage and the new eval-ladder guidance. | Portable improvement, adapted sync | Update `init-project` toward the intake-first boundary, add completion-sanity triage, and port eval-ladder guidance across setup/triage/eval/story/build while preserving CineForge's sidequest, provider, UI-scout, and film-pipeline language. |
| Dossier | Has setup/eval/story/triage skills but no `init-project`, no completion-sanity triage, and no eval-ladder guidance. | Portable improvement, adapted sync | Add completion-sanity and eval-ladder guidance across triage/eval/story/build. Decide during implementation whether Dossier should add `init-project` or keep its existing `retrofit-ideal` lane as the local intake equivalent. |
| Doc Web | Has setup/triage/eval/story skills but no `init-project`, no triage runbook, no completion-sanity triage, and no eval-ladder guidance. | Portable improvement plus unclear local surface gap | Add completion-sanity and eval-ladder guidance. Consider adding `docs/runbooks/triage.md` because the triage skill has no runbook companion; decide separately whether `init-project` belongs here. |
| Board Game Ingester | Has setup/eval/story/triage skills and wrappers, but no `init-project`, no triage runbook, no completion-sanity triage, and no eval-ladder guidance. | Portable improvement, sync now with adaptation | Add/adapt `init-project`, update setup to require authored Ideal/spec for greenfield work, add completion-sanity triage, add eval-ladder guidance across setup/triage/eval/story/build, and keep board-game benchmark/rulebook/component/golden-fixture language. |

## Classification

- **Portable improvement:** Storybook's `init-project` before
  `setup-methodology` boundary should be available where a repo may seed new
  methodology projects or rebuild incomplete bootstrap surfaces.
- **Portable improvement:** Storybook's completion-sanity triage should sync
  across the projects that can otherwise drift to maintenance work while real
  product scope remains undecomposed.
- **Portable improvement:** Storybook's eval-ladder guidance should sync to
  every repo with AI/eval/story planning surfaces, with local wording for each
  product's golden/eval substrate.
- **Intentional adaptation:** Echo Forge's selective Storybook import should
  remain Echo Forge-native. Do not copy Storybook product language or assume
  every optional Storybook lane is required.
- **Intentional adaptation:** CineForge should keep provider, pipeline,
  sidequest benchmark, and UI-scout specifics rather than copying Storybook
  surface text exactly.
- **Intentional adaptation:** Dossier and Doc Web do not automatically need
  Storybook's full `init-project` skill if their local intake/setup lanes solve
  the same problem with less overhead.
- **Intentional adaptation:** Board Game Ingester should keep its
  board-game-specific benchmark/golden guidance. The sync target is the
  methodology shape, not exact Storybook prose.
- **Unclear drift:** `docs/build-map.md`, `docs/scout.md`, and `docs/scout/`
  are registered comparison surfaces for the two newly added projects, but this
  skill-surface pass did not verify whether absence is intentional. Handle that
  in a later broader alignment pass, not in this skill-surface sync.

## Recommended Actions

Create one Conductor supervisor story for the rollout, then implement target
repo changes in isolated worktrees because several primary checkouts are dirty
or behind.

Recommended scope for that story:

1. Use Storybook as the source implementation.
2. Update Echo Forge with eval-ladder guidance only.
3. Update CineForge with completion-sanity triage plus eval-ladder guidance and
   adapt its older `init-project` toward the intake-first boundary.
4. Update Dossier with completion-sanity and eval-ladder guidance; decide
   whether `init-project` is needed or whether `retrofit-ideal` is the local
   equivalent.
5. Update Doc Web with completion-sanity and eval-ladder guidance; consider
   adding the missing triage runbook.
6. Update Board Game Ingester with the full adapted package: `init-project`,
   completion-sanity, setup preflight, and eval ladder.
7. Run each repo's sync wrapper check and repo-native methodology check before
   claiming the target repo is aligned.

## Human Judgment

- **Dossier:** Keep `retrofit-ideal` as the local intake equivalent for this
  pass. Add completion-sanity and eval-ladder gates without adding a second
  greenfield bootstrap skill.
- **Doc Web:** Do not add `init-project` in this pass. Add the missing triage
  runbook plus completion-sanity and eval-ladder gates for the existing mature
  document-pipeline surface.
- **Board Game Ingester:** Add a smaller board-game-specific `init-project`
  variant rather than copying Storybook's full flow verbatim.

## Result

The rollout was implemented from isolated target-project worktrees and pushed
directly to each target repo's `main` branch:

| Project | Commit | Result |
| --- | --- | --- |
| Dossier | `eabc640` | Added completion-sanity triage, eval-ladder gates across setup/triage/eval/story/build surfaces, and kept `retrofit-ideal` as the local intake equivalent. |
| Doc Web | `aca1922` | Added completion-sanity triage, eval-ladder gates, and a new `docs/runbooks/triage.md`; did not add `init-project`. |
| CineForge | `3ae6a0b` | Added completion-sanity triage, eval-ladder gates, and an intake/root-eval boundary to the existing `init-project` surface. |
| Board Game Ingester | `c9d1337` | Added adapted `init-project`, completion-sanity triage, eval-ladder gates, and a new triage runbook. |
| Echo Forge | `5bf1aba` | Added eval-ladder guidance while preserving the Echo Forge-native selective-import setup. |

Validation evidence:

- Dossier: `PYTHON=/Users/cam/miniconda3/bin/python make methodology-compile`,
  `PYTHON=/Users/cam/miniconda3/bin/python make methodology-check`,
  `make skills-check`, `git diff --check`
- Doc Web: `make methodology-compile`, `make methodology-check`,
  `make skills-check`, `git diff --check`
- CineForge: `npm run methodology:compile --silent`,
  `npm run methodology:check --silent`, `make skills-check`,
  `git diff --check`
- Board Game Ingester: `make methodology-compile`, `make methodology-check`,
  `make skills-check`, `git diff --check`
- Echo Forge: `npm run methodology:compile --silent`,
  `npm run methodology:check --silent`, `npm run skills:check --silent`,
  `git diff --check`

## Practical Impact

Adding Board Game Ingester and Echo Forge to `projects.yaml` makes them visible
to future Conductor alignment and scout runs. The full six-app alignment shows
where Storybook's newest bootstrap, completion-sanity, and eval-ladder lessons
should travel without pretending every project should become text-identical.

The target-project rollout is now applied, so future triage in those repos has
an explicit guard against maintenance-style recommendations hiding unfinished
product scope, and AI-capability work has a clearer route through root, parent,
and child eval evidence before it becomes backlog.
