---
title: "Codex Worktree Environment Bootstrap"
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
  - "spec:2.1"
  - "spec:2.2"
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

# Story 018 — Codex Worktree Environment Bootstrap

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: None

## Goal

Turn the missing-dependency pain in fresh Codex worktrees into a repo-owned
setup contract.

Today several tracked repos have `.codex/environments/environment.toml`, but
their `[setup].script` values are empty. Some repos also have no Codex
environment file at all. That leaves each agent to rediscover missing
`node_modules`, virtualenvs, `vitest`, `pnpm`, or Python test dependencies and
decide ad hoc whether `npm ci`, `pnpm install`, `uv sync`, or another install
command is safe.

This story should make worktree setup explicit, idempotent, and local to each
repo while preserving Conductor's recommendation-first role.

## Acceptance Criteria

- [x] Alignment 036 records the current Codex environment drift and explains
      why missing test binaries in new worktrees are expected with empty setup
      scripts.
- [x] Conductor setup-methodology/runbook guidance distinguishes dependency
      bootstrap from local runtime allocation and recommends a repo-owned setup
      hook for Codex worktrees.
- [x] Each tracked repo is inventoried from current `origin/main` for
      `.codex/environments/environment.toml`, package/lock files, ignored
      dependency artifacts, local runtime actions, and native validation
      commands.
- [x] Target repo edits happen only in isolated worktrees, not dirty primary
      checkouts.
- [x] Repos with active validation/runtime needs receive or explicitly defer a
      non-empty Codex setup hook that calls a repo-owned command rather than
      embedding long install logic in TOML.
- [x] Setup commands are idempotent, lockfile-respecting, and limited to
      dependency/tool restoration; they do not rewrite source, lockfiles,
      methodology outputs, or user data.
- [x] Runtime-heavy repos keep or gain useful Run/status actions only where a
      real local runtime exists.
- [x] Validation proves the setup hooks with bounded install/check commands, or
      records exact pre-existing blockers and deferred reasons.

## Out of Scope

- Creating a central harness or making Conductor the canonical copy of target
  repo setup scripts.
- Running background installs automatically outside an explicit Codex setup
  hook.
- Forcing Run actions into repos that have no real local browser/API/runtime
  surface.
- Changing product code beyond setup scripts, Codex environment config, and
  closely related docs/check surfaces.
- Committing, pushing, or landing target repo changes without an explicit
  closeout request.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Read Alignment 016, Alignment 032, and Alignment 036
- [x] Decide the shared setup-hook shape:
  - [x] command naming
  - [x] package-manager behavior
  - [x] no-source-mutation guardrails
  - [x] how setup relates to Run/status actions
- [x] Patch Conductor setup-methodology/runbook guidance if the shared contract
      needs to be durable beyond this story
- [x] Create isolated target worktrees under
      `/Users/cam/.codex/worktrees/codex-worktree-env-bootstrap/`
- [x] In each target repo, inspect current branch/status before editing
- [x] Patch `.codex/environments/environment.toml`, setup scripts, package
      scripts, README/setup docs, or deferred notes only where warranted
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: `make test`
- [x] Run each touched target repo's native setup/skill/methodology checks plus
      `git diff --check`
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

- `docs/alignments/align-036-codex-worktree-environment-bootstrap.md` —
  alignment decision and current evidence.
- `docs/align-projects.md` — alignment index entry.
- `docs/stories/story-018-codex-worktree-environment-bootstrap.md` — story
  source of truth and work log.
- `.agents/skills/setup-methodology/SKILL.md` — likely shared setup guidance if
  Codex setup hooks become part of the setup package.
- `docs/runbooks/setup-methodology.md` — likely operator-facing setup summary.
- Target repo `.codex/environments/environment.toml` and repo-owned setup
  commands only after isolated worktrees are created.

## Notes

- Triggered by the `inbox.md` note asking why agents often report missing local
  binaries in fresh Codex worktrees and whether Codex is being used wrong.
- Read-only alignment evidence on 2026-05-20 found Dossier, Storybook,
  CineForge, and Echo Forge environment files with empty setup scripts. Doc Web,
  Board Game Ingester, Robo Rally, and the Conductor checkouts inspected here
  had no `.codex/environments/environment.toml`.
- Storybook and Echo Forge already expose useful Codex Run/status actions, but
  those actions do not solve dependency hydration because setup remains empty.
- Board Game Ingester and Echo Forge primary checkouts are currently active
  workspaces; do not edit them in place for this supervisor rollout.
- Recommended target branch: `codex/codex-worktree-env-bootstrap`.

## Plan

Plan prepared 20260520-0926. Implementation remains behind the build-story plan
gate.

1. Keep this Conductor work on branch
   `codex/codex-worktree-env-bootstrap`.
2. Patch Conductor's setup-methodology and setup runbook with a short Codex
   worktree bootstrap contract:
   - dependency bootstrap is separate from local runtime allocation
   - `.codex/environments/environment.toml` should call one repo-owned setup
     command, not embed long package-manager logic
   - setup commands must be idempotent and lockfile-respecting
   - setup commands may restore ignored dependency artifacts only; they must not
     rewrite source, lockfiles, methodology outputs, or user data
3. Add Conductor's own minimal `.codex/environments/environment.toml` and
   `scripts/codex-setup` if local evidence confirms the setup can be a no-op or
   cheap Python/check bootstrap. This gives Conductor the same surface it is
   recommending.
4. Create target worktrees under
   `/Users/cam/.codex/worktrees/codex-worktree-env-bootstrap/` from each repo's
   current `origin/main` on branch `codex/codex-worktree-env-bootstrap`.
   Primary checkout evidence gathered before planning:
   - Dossier clean at `6f309fd`, matching `origin/main`
   - Storybook clean except untracked
     `input/Family-1-19-May-2026-011553514.ged`, matching `origin/main`
   - Doc Web clean at `99450a3`, matching `origin/main`
   - CineForge has local `docs/deploy-log.md` edits, matching `origin/main`
   - Board Game Ingester primary checkout is on active
     `codex/story-014-seed-asset-inventory-matching-eval`; `origin/main` is
     `b822102`
   - Robo Rally clean at `a0d8029`, matching `origin/main`
   - Echo Forge primary checkout is active Story 053 with many modified and
     untracked files; `origin/main` is `7766b8e`
5. In each target worktree, add the smallest repo-local setup hook:
   - Dossier: `scripts/codex-setup` calls the existing locked dependency path,
     likely `uv sync --locked --extra dev`, and `.codex/environments` points to
     it.
   - Storybook: add a `codex:setup` package script or `scripts/codex-setup`
     that runs `pnpm install --frozen-lockfile`; keep existing Run/status
     actions.
   - Doc Web: add a Python setup hook around the existing package constraints,
     likely using `.venv` plus `python -m pip install -r requirements.txt` or
     `python -m pip install -e .[driver]` depending on local evidence in the
     worktree; add environment config without Run actions.
   - CineForge: add a setup hook that restores both Python deps and Node deps
     needed by its root/local-service and `ui` workspace; preserve local runtime
     actions if available on `origin/main`.
   - Board Game Ingester: if no external dependencies are needed, add a
     no-op/check-only setup hook or explicitly document deferral in the
     alignment/story evidence rather than inventing dependency work.
   - Robo Rally: add a Node setup hook using the lockfile/package state found
     on `origin/main`; keep runtime actions deferred because no UI runtime
     exists yet.
   - Echo Forge: add `scripts/codex-setup` with `npm ci`, wire
     `.codex/environments`, and preserve the existing local app/auditor/studio
     actions.
6. Validate each target patch with bounded setup proof and repo-native checks:
   - setup script syntax or direct dry/real run as appropriate
   - native methodology/skill checks where those scripts exist
   - `git diff --check`
   - avoid heavy product tests unless a setup script change makes them the
     narrowest honest proof
7. Update Alignment 036 and this story with exact target worktree paths,
   branch bases, setup commands, validation evidence, and any deferred repos.
8. Run Conductor checks:
   - `make methodology-compile`
   - `PYTHONDONTWRITEBYTECODE=1 make methodology-check`
   - `PYTHONDONTWRITEBYTECODE=1 make lint`
   - `make skills-check` if setup-methodology changes
   - `make test` if scripts or repo checks change
   - `git diff --check`
9. Leave the story `In Progress` with Build complete checked after
   implementation. Target repo branches stay uncommitted/unpushed unless Cam
   explicitly asks for closeout.

Manual inspection points:

- Confirm generated-looking `.codex/environments/environment.toml` files remain
  in the current accepted shape: `version`, `name`, `[setup].script`, and
  optional `[[actions]]`.
- Confirm every setup hook prints what it is doing and does not silently start
  local servers.
- Confirm runtime action commands are present only for repos with a real local
  runtime.

## Work Log

20260520-0000 — story-created: created Story 018 from Alignment 036 and the
Codex setup inbox note. The comparison found that existing Codex environment
files have empty setup scripts, while local runtime allocation guidance covers
ports/actions rather than dependency bootstrap. Next step: build the story from
isolated target worktrees if Cam approves.

20260520-0926 — build-plan: read Story 018, Ideal/spec/state, ADR-001,
ADR-002, setup-methodology local runtime guidance, current environment TOML
files, package/lock surfaces, primary checkout status, and branch bases. No
external upstream docs were needed for this plan; the current evidence is the
local Codex app environment file shape already generated in tracked repos.

20260520-0930 — conductor-contract: added Conductor's own
`.codex/environments/environment.toml` and check-only `scripts/codex-setup`,
then patched `.agents/skills/setup-methodology/SKILL.md` and
`docs/runbooks/setup-methodology.md` so the durable setup package now treats
Codex setup as dependency bootstrap, not runtime launch. The hook compiles
Conductor's Python entrypoints in memory without writing bytecode and passed
locally.

20260520-0948 — target-rollout: created isolated worktrees at
`/Users/cam/.codex/worktrees/codex-worktree-env-bootstrap/<project>/` from
current `origin/main`, all on branch `codex/codex-worktree-env-bootstrap`.
Patched each repo with the shared setup-methodology contract plus a repo-owned
`scripts/codex-setup` and `.codex/environments/environment.toml` where needed.
Dossier and CineForge also gained narrow `.gitignore` unignore rules for the
environment TOML because their local ignore surfaces hid `.codex/`. Runtime
actions were preserved for Storybook and Echo Forge, added for CineForge's
existing local-service app/status commands, and left absent for repos without a
real local runtime.

20260520-0950 — target-validation: direct setup hooks passed in all touched
target worktrees. Dossier used `uv sync --frozen --extra dev` with Python 3.12;
Storybook used `pnpm install --frozen-lockfile`; Doc Web created `.venv` with
Python 3.12 and installed `requirements.txt`; CineForge installed `.[dev]`,
root `npm ci`, and UI `npm ci` after the hook stripped active Conda metadata
from pip install to avoid the stale OTIO/pybind include path; Board Game
Ingester used a non-writing syntax-check hook, Robo Rally used a check-only
Node hook; Echo Forge used `npm ci`.
Native checks passed: Dossier, Storybook, Doc Web, CineForge, Board Game
Ingester, and Echo Forge each passed methodology-check, skills-check,
triage-facts check, and `git diff --check`; Robo Rally passed full
`npm run validate` with 61 tests.

20260520-0957 — conductor-validation: Conductor setup hook passed, then
`PYTHONDONTWRITEBYTECODE=1 make methodology-compile`,
`PYTHONDONTWRITEBYTECODE=1 make methodology-check`,
`PYTHONDONTWRITEBYTECODE=1 make lint`, `make skills-check`,
`PYTHONDONTWRITEBYTECODE=1 make test`, and `git diff --check` all passed.
Generated Python bytecode noise from the checks was removed so the remaining
diff is limited to the intended setup, alignment, story, runbook, inbox, and
generated methodology surfaces. Build gate is complete; `/validate` remains the
next workflow gate.

20260520-1003 — guardrail-tightening: learning-review found no separate
candidate because the only reusable gap was small enough to address inside this
story. Updated setup-methodology and the setup runbook to require checking that
`.codex/environments/environment.toml` is visible to git, with a narrow
unignore rule when a repo ignores `.codex/`. Resynced that skill text into all
target worktrees, reran target methodology compiles where applicable, and
reran target methodology-check, skills-check, and `git diff --check` across the
touched worktrees. Final Conductor rerun also passed methodology-compile,
methodology-check, lint, skills-check, test, and `git diff --check`.

20260520-1012 — validation: ran `/validate` with a full current diff/status
review plus `codex review --uncommitted`. Accepted the advisory finding that
Conductor's original `py_compile` setup check dirtied the repo because this
checkout tracks one `scripts/__pycache__` file. Replaced it with an in-memory
Python syntax check and made the same check-only improvement for Board Game
Ingester. Fresh proof after the fix: Conductor setup hook left git status clean
apart from intended files, Board Game Ingester setup/methodology/skills/
triage-facts/diff checks passed, and the validation gate is complete. Next
workflow gate is `/mark-story-done`.

20260520-1042 — closeout: marked Story 018 done after landing all linked
target repo worktrees on `main`. Target commits: Dossier `3d7527f`,
Storybook `0328dd8`, Doc Web `37ef4af`, CineForge `2a39893`, Board Game
Ingester `d3d5142`, Robo Rally `40b82fe`, and Echo Forge `5bec49b`.
Conductor closeout will carry the alignment/story/runbook/changelog evidence
and local setup contract.
