# Alignment 032 — Portfolio Local Runtime Allocation

**Date:** 2026-05-15

## Focus

Upgrade Alignment 016 from fixed primary-checkout ports into a portfolio local
runtime contract that stays safe when multiple agents run multiple worktrees of
the same app.

Surfaces compared:

- Conductor Alignment 016 local dev port contract
- Echo Forge worktree `/Users/cam/.codex/worktrees/c370/echo-forge`
- Echo Forge `scripts/local-service.mjs` pilot
- Echo Forge local service health endpoints for Registry QA and Studio
- Storybook `scripts/storybook-env.mjs`, `scripts/dev.mjs`, and `dev:gauth`
- CineForge `scripts/dev-local` and Vite/API launch path
- tracked project README and `/setup-methodology` surfaces

## Contract

Conductor owns `local-dev-ports.json` as the canonical allocation file. Target
repos should not invent project ranges. Repo-local launchers read this file,
derive their own ports, and fail loudly when allocation is unavailable or a
port is owned by another checkout.

Primary checkout ports remain stable for human bookmarks, OAuth redirect
configuration, and existing Run actions:

| Project | UI | Service/API |
| --- | ---: | ---: |
| Storybook | `5173` | `3001` |
| CineForge | `5174` | `8000` |
| Echo Forge | `5175` | `3002` catalog, `4177` registry QA, `4178` studio |
| Robo Rally | `5176` reserved | `3003` reserved |
| Board Game Ingester | `5177` reserved | `3004` reserved |

Worktree ports derive from non-overlapping ranges:

| Project | UI range | Service range |
| --- | ---: | ---: |
| Storybook | `5200-5299` | `3200-3299` |
| CineForge | `5300-5399` | `3300-3399` |
| Echo Forge | `5400-5499` | `3400-3499` |
| Robo Rally | `5500-5599` | `3500-3599` |
| Board Game Ingester | `5600-5699` | `3600-3699` |
| Dossier | `5700-5799` | `3700-3799` |
| Doc Web | `5800-5899` | `3800-3899` |

Worktree slots are persisted by absolute worktree path in
`~/.codex/local-dev-ports.json`. Ports derive as:

`range_start + slot * slotStride + service_offset`

The current slot stride is `10`, leaving room for several named services per
worktree.

## Classification

- **Portable improvement:** Echo Forge's named `status` / `start` / `stop`
  service launcher is the right pattern for repos with live local runtime
  surfaces.
- **Portable improvement:** launchers should report project, checkout root,
  slot, computed ports, owning PIDs, process cwd, open URLs, and service
  health.
- **Portable improvement:** write-capable local services should expose a health
  endpoint that identifies the service and checkout-local data path.
- **Portable improvement:** Vite and equivalent dev servers should use strict
  fixed ports rather than silently falling through to a random free port.
- **Intentional adaptation:** Storybook keeps `5173/3001` for the primary
  checkout because Google auth and local smoke paths already depend on that
  pair.
- **Intentional adaptation:** Dossier, Doc Web, Robo Rally, and Board Game
  Ingester should get reserved ranges and setup guidance now, but only repos
  with a real local runtime should receive a live launcher immediately.

## Target Execution Plan

Execute Story 015 in isolated target worktrees under:

`/Users/cam/.codex/worktrees/local-runtime-allocation/<project-key>`

Initial rollout scope:

- Conductor: allocation file, alignment/story/runbook/setup-methodology update
- Storybook: switch worktree port derivation to Conductor allocation, add
  `local:*` scripts and README guidance
- CineForge: add a `local:*` launcher surface using Conductor allocation, keep
  existing `dev:local` as a lower-level compatibility path
- Echo Forge: land the service-launcher pattern from the c370 worktree and make
  it read Conductor allocation
- Dossier, Doc Web, Robo Rally, Board Game Ingester: update README and
  setup-methodology guidance now; defer live launchers until each repo has a
  real local web/API runtime to launch

## Rollout Evidence

Implementation work happened in isolated worktrees on branch
`codex/local-runtime-allocation`:

- `/Users/cam/.codex/worktrees/local-runtime-allocation/storybook`
- `/Users/cam/.codex/worktrees/local-runtime-allocation/cine-forge`
- `/Users/cam/.codex/worktrees/local-runtime-allocation/echo-forge`
- `/Users/cam/.codex/worktrees/local-runtime-allocation/dossier`
- `/Users/cam/.codex/worktrees/local-runtime-allocation/doc-web`
- `/Users/cam/.codex/worktrees/local-runtime-allocation/roborally`
- `/Users/cam/.codex/worktrees/local-runtime-allocation/boardgame-ingester`

Applied changes:

- Conductor added `local-dev-ports.json` as the machine-readable allocation
  source and taught `/setup-methodology` to propagate the pattern.
- Storybook switched worktree port derivation to Conductor allocation and added
  `pnpm local:app`, `pnpm local:status`, and `pnpm local:stop`.
- CineForge added the same allocation-backed local service surface while
  preserving `scripts/dev-local` as a compatibility entrypoint.
- Echo Forge adopted the c370 service-launcher pattern, reads Conductor
  allocation, exposes health/root pages for Registry QA and Studio, and adds
  Codex app actions for the named local services.
- Dossier, Doc Web, Robo Rally, and Board Game Ingester document reserved
  ranges and defer live launchers until real local runtimes exist.

Validation evidence:

- `node --check` passed for the new local launcher/helper scripts in Storybook,
  CineForge, and Echo Forge.
- Dry `local-service.mjs status` runs passed with a temporary allocation/slot
  file, proving worktree port derivation without mutating
  `~/.codex/local-dev-ports.json`.
- Setup-methodology skill copies matched Conductor byte-for-byte across all
  seven target worktrees.
- Repo-native methodology/skill checks plus `git diff --check` passed for all
  seven target repos. Dossier required its primary virtualenv Python because
  the ambient `python3` lacked PyYAML.
- 2026-05-16 rebase refresh: Conductor and all seven target worktrees are
  rebased to current `origin/main` with `HEAD...origin/main` at `0 0`. Main's
  new Algorithmic Complexity Detector work now owns Alignment 031 / Story 014,
  so this rollout is Alignment 032 / Story 015. Echo Forge main already carried
  the local launcher pilot; this branch now layers in Conductor allocation
  lookup and the portfolio setup/readme contract.
- 2026-05-16 landing evidence: target repos landed to `main` as Dossier
  `998db9c`, Storybook `e2348f6`, Doc Web `0000863`, CineForge `16cb6be`,
  Board Game Ingester `75491af`, Robo Rally `673c979`, and Echo Forge
  `1a8afec`. Echo Forge was rebased once more after its remote `main` advanced
  during landing, then its methodology/skills/script/status checks were rerun
  before the fast-forward push.

## Human Judgment

No product decision is needed for the port blocks. The open judgment is when to
promote launchers into currently headless or no-runtime repos. The recommended
rule is conservative: reserve ranges now, add launchers when the repo first
creates a local web/API surface.

## Practical Impact

Cam and parallel agents can ask a repo what is running without guessing which
terminal started it. Worktree servers will stop stealing each other's ports, and
write-capable internal tools will be less likely to point at the wrong checkout
data.
