---
title: "Local Dev Port Contract"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I5"
spec_refs:
  - "spec:1.1"
  - "spec:2.2"
  - "spec:4.2"
  - "spec:5.1"
decision_refs:
  - "ADR-001"
depends_on: []
category_refs:
  - "registry-routing"
  - "alignment"
  - "story-prep"
  - "memory"
tracked_projects:
  - "storybook"
  - "cine-forge"
  - "echo-forge"
  - "roborally"
  - "boardgame-ingester"
---

# Story 004 — Local Dev Port Contract

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001
**Depends On**: None

## Goal

Stop active UI apps from stealing each other's local dev ports by recording a
small portfolio-wide port contract and giving target repos stable run commands
that Codex's Run action can invoke from whatever worktree is active.

## Acceptance Criteria

- [x] Conductor records the chosen local port assignments and the Storybook
  Google-auth exception.
- [x] CineForge has a worktree-safe launcher that starts its API and UI on its
  assigned ports.
- [x] Echo Forge has a launcher/config update that moves its UI off Storybook's
  Google-auth port and reserves its local server port.
- [x] The run-action command for each current UI app is explicit.
- [x] Target repo checks pass for the touched files.

## Out of Scope

- Changing Storybook's Google-auth-safe ports; those are intentionally fixed at
  frontend `5173` and backend `3001`.
- Implementing a full shared Conductor daemon or global port broker.
- Giving Robo Rally a UI before the project is ready for one.
- Changing target apps beyond the narrow launcher/config surfaces needed for
  the port contract.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and alignment context.
- [x] Confirm Storybook's Google-auth launcher and ports from source.
- [x] Create/update alignment memory for the local dev port contract.
- [x] Inspect target repo working states and choose isolation where practical.
- [x] Implement the needed launcher/config changes.
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] Target repo narrow checks
- [x] Search docs and update any related surfaces.
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

- `docs/alignments/align-016-local-dev-port-contract.md` — durable alignment
  record for port assignments and run-action commands.
- `docs/align-projects.md` — alignment index entry.
- `docs/stories/story-004-local-dev-port-contract.md` — story evidence and
  outcome log.
- `/Users/cam/.codex/worktrees/local-dev-port-contract/cine-forge/scripts/dev-local`
  — CineForge launcher for API + UI.
- `/Users/cam/.codex/worktrees/local-dev-port-contract/cine-forge/ui/vite.config.ts`
  — CineForge env-driven UI port and API proxy target.
- `/Users/cam/.codex/worktrees/local-dev-port-contract/cine-forge/package.json`
  — expose `npm run dev:local`.
- `/Users/cam/Documents/Projects/echo-forge/scripts/dev-local` — Echo Forge
  launcher for UI + local catalog server reservation.
- `/Users/cam/Documents/Projects/echo-forge/vite.config.ts` — Echo Forge
  env-driven UI/preview ports with strict binding.
- `/Users/cam/Documents/Projects/echo-forge/package.json` — expose
  `npm run dev:local`.

## Notes

Confirmed Storybook's Google-auth-safe launcher in
`/Users/cam/Documents/Projects/Storybook/storybook/scripts/dev-gauth.mjs`.
It hard-pins frontend `5173`, backend `3001`, `localhost` URLs, and
`VITE_API_URL=http://localhost:3001`. Storybook's frontend Vite config uses
`strictPort: true`, so this pair should remain reserved.

Primary target repo state at start:

- Storybook primary checkout is dirty on active Story 112 work; no change is
  needed because `pnpm dev:gauth` already solves the run action.
- CineForge primary checkout is dirty on benchmark/provider work; patch in an
  isolated worktree at
  `/Users/cam/.codex/worktrees/local-dev-port-contract/cine-forge`.
- Echo Forge's Vite app scaffold is uncommitted in the primary checkout, so an
  isolated worktree from `main` would not contain the UI. Keep the Echo edit
  narrowly scoped to launcher/config files in the active checkout.
- Robo Rally is not a git repo and has no UI yet; reserve ports in the
  alignment record only.

Chosen local port contract:

| App | Server | UI | Run action command |
| --- | ---: | ---: | --- |
| Storybook | `3001` | `5173` | `pnpm dev:gauth` |
| CineForge | `8000` | `5174` | `./scripts/dev-local` |
| Echo Forge | `3002` | `5175` | `./scripts/dev-local` |
| Robo Rally | `3003` | `5176` | Future `./scripts/dev-local` |
| Board Game Ingester | `3004` | `5177` | Future `./scripts/dev-local` if a UI lands |

## Plan

1. Record the port contract and run-action guidance in Conductor alignment
   memory.
2. Add a CineForge launcher that resolves the current git worktree root,
   chooses the repo-local or primary-checkout Python interpreter, checks the
   assigned ports before launch, and starts the API plus Vite UI.
3. Update CineForge Vite config so the assigned UI/API ports can be driven by
   the launcher without editing files per worktree.
4. Add an Echo Forge launcher that checks and starts its assigned UI port plus
   the local catalog-review server on the reserved server port.
5. Update Echo Forge Vite config so default dev no longer competes with
   Storybook's Google-auth port.
6. Run narrow syntax/config checks plus Conductor methodology checks.

## Work Log

20260424-1654 — story-created: created Story 004 after the user approved the
local dev port/run-action plan. Evidence: confirmed Storybook's `dev:gauth`
launcher pins `localhost:5173` and `localhost:3001`; inspected target repo
states and chose an isolated CineForge worktree while noting Echo Forge's active
UI scaffold only exists in the dirty primary checkout. Next step: patch
CineForge and Echo Forge launchers.

20260424-1716 — implementation: added CineForge `scripts/dev-local` in isolated
worktree `/Users/cam/.codex/worktrees/local-dev-port-contract/cine-forge`,
updated its Vite config to accept `CINE_FORGE_UI_PORT` and
`CINE_FORGE_API_URL`, and exposed root `npm run dev:local`. Echo Forge gained
`scripts/dev-local`, `npm run dev:local`, and strict Vite defaults on UI port
`5175` plus preview port `4175`, while its catalog server is started on the
reserved server port `3002` by the launcher. Target checks passed:
CineForge `bash -n scripts/dev-local`, `./scripts/dev-local --help`,
`node` package JSON parse, `git diff --check`, `npm run methodology:check
--silent`, `pnpm --dir ui install --frozen-lockfile`, `pnpm --dir ui run lint`,
and `pnpm --dir ui run build` (existing chunk-size warning only). Echo Forge
passed `bash -n scripts/dev-local`, `./scripts/dev-local --help`, `node`
package JSON parse, `git diff --check -- package.json vite.config.ts
scripts/dev-local`, `npm run methodology:check --silent`, `npm run typecheck`,
`npm run build`, and `npm run lint`. Bounded launch smokes passed with
`timeout`: CineForge stayed up on `8000/5174`, Echo Forge stayed up on
`3002/5175`, and post-smoke `lsof` confirmed those ports were free again. Next
step: recompile/check Conductor surfaces.

20260424-1720 — conductor-checks: regenerated Conductor methodology outputs and
verified the supervisor repo. Evidence: `make methodology-compile`, `make
methodology-check`, `make lint`, `make test`, and `git diff --check` passed.
The test target regenerated a tracked Python bytecode artifact, which was
restored to keep the diff limited to intended files. Next step: hand off for
review/validation without committing or pushing.

20260424-1734 — validation and close-out: validated the current Conductor diff
against the story and Alignment 016. Story requirements are met: the port
contract is recorded, Storybook's Google-auth exception is preserved, CineForge
and Echo Forge have checked worktree-safe launchers, and the run-action
commands are explicit. Marked Story 004 done and regenerated methodology
surfaces for final check-in.

20260424-1754 — target landing: after Conductor close-out, landed the narrow
target repo patches from isolated worktrees. CineForge commit `e0c5c41` added
the local dev launcher on `main`; Echo Forge commit `fb8501b` added the same
port-contract launcher/config on `main`. Echo Forge's primary checkout still
has unrelated active Story 003 documentation changes, so the target commit was
made from `/Users/cam/.codex/worktrees/local-dev-port-contract/echo-forge`
instead of staging the dirty primary checkout.
