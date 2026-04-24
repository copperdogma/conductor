# Alignment 016 — Local Dev Port Contract

**Date:** 2026-04-24

## Focus

Stop the active UI apps from silently colliding on local dev ports, and make the
Codex Run action simple enough for Cam to use without asking an agent to start a
server.

Surfaces compared:

- Storybook `scripts/dev-gauth.mjs`
- Storybook `scripts/storybook-env.mjs`
- Storybook `packages/frontend/vite.config.ts`
- CineForge `src/cine_forge/api/__main__.py`
- CineForge `ui/vite.config.ts`
- Echo Forge `package.json`
- Echo Forge `vite.config.ts`
- Echo Forge `scripts/sound-catalog-server.mjs`
- Robo Rally current docs-only project shape

## Port Contract

| App | Server | UI | Run action command |
| --- | ---: | ---: | --- |
| Storybook | `3001` | `5173` | `pnpm dev:gauth` |
| CineForge | `8000` | `5174` | `./scripts/dev-local` |
| Echo Forge | `3002` | `5175` | `./scripts/dev-local` |
| Robo Rally | `3003` | `5176` | Future `./scripts/dev-local` |
| Board Game Ingester | `3004` | `5177` | Future `./scripts/dev-local` if a UI lands |

Storybook is the special case. It uses Google OAuth locally, and the
Google-auth-safe launcher already pins `localhost:5173` and `localhost:3001`.
Other apps should move away from that pair rather than asking Storybook to move.

## Observations

- Storybook already owns the right shape: one command, current-worktree runtime
  resolution, explicit frontend/backend URLs, and strict Vite port binding.
- CineForge has fixed default ports (`8000` backend, `5174` UI), but the launch
  path is manual and the Vite API proxy target was hard-coded.
- Echo Forge's active Vite scaffold defaulted to `5173`, which conflicts with
  Storybook's Google-auth-safe UI port. It also has a local catalog-review
  server defaulting to `4174`, which is not part of an app-wide port convention.
- Robo Rally has no app runtime yet; reserving ports now avoids creating the
  next collision when the UI lands.

## Classification

- **Intentional adaptation:** Storybook keeps `5173/3001` because Google auth is
  already configured around those localhost URLs.
- **Portable improvement:** Every UI app should expose a repo-local
  `./scripts/dev-local` launcher so Codex's Run action can use a relative,
  worktree-safe command.
- **Portable improvement:** Vite apps should use `strictPort: true` so a port
  collision fails loudly instead of shifting to another app's expected URL.
- **Intentional adaptation:** Echo Forge can reserve a server port through its
  catalog-review server today even though its main app is currently UI-only.
- **Intentional adaptation:** Robo Rally and Board Game Ingester only need
  reserved future ports until a real UI/server exists.

## Recommended Actions

1. Keep Storybook as-is and set its Codex Run action to `pnpm dev:gauth`.
2. Add CineForge `./scripts/dev-local` and make its Vite proxy target
   environment-driven.
3. Move Echo Forge's UI default to `5175`, reserve `3002` through
   `./scripts/dev-local`, and keep the command relative to the current worktree.
4. When Robo Rally gets a UI, give it `3003/5176` from the start.
5. When Board Game Ingester gets a UI, give it `3004/5177`.

## Human Judgment

No new decision is needed unless Cam wants multiple simultaneous worktrees of
the same app running at once. This contract prevents cross-app collisions. A
separate per-worktree slot override can be added later if same-app parallel
runtime becomes common.

## Result

Story 004 implemented the first rollout slice:

- Storybook remains unchanged; its Run action command is `pnpm dev:gauth`.
- CineForge landed commit `e0c5c41` on `main`, adding `./scripts/dev-local`,
  root `npm run dev:local`, and env-driven Vite UI/API port config.
- Echo Forge landed commit `fb8501b` on `main`, adding `./scripts/dev-local`,
  `npm run dev:local`, and strict Vite defaults on `5175` so it no longer
  competes with Storybook's `5173`.
- Robo Rally and Board Game Ingester are reserved in the contract only because
  they do not currently have active UI/server runtime surfaces needing patches.

Validation evidence:

- CineForge: `bash -n scripts/dev-local`, `./scripts/dev-local --help`, package
  JSON parse, `git diff --check`, `npm run methodology:check --silent`,
  `pnpm --dir ui install --frozen-lockfile`, `pnpm --dir ui run lint`,
  `pnpm --dir ui run build`, and bounded `timeout 12 ./scripts/dev-local`.
- Echo Forge: `bash -n scripts/dev-local`, `./scripts/dev-local --help`,
  package JSON parse, focused `git diff --check`, `npm run methodology:check
  --silent`, `npm run typecheck`, `npm run build`, `npm run lint`, and bounded
  `timeout 8 ./scripts/dev-local`.

## Practical Impact

Cam can save relative Run action commands instead of remembering port and
worktree details. The apps now fail loudly when their assigned ports are busy,
which should make the actual conflict obvious instead of letting Vite silently
hop to a different port.
