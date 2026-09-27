# Alignment 048 — pnpm Dependency Storage

Date: 2026-09-27
Status: Complete — both owner migrations landed and verified on remote main.
Authorization: Cam asked to research and implement where sensible, then explicitly
approved resolving validation blockers and landing these scoped migrations.
No deployment, primary-checkout replacement, or old-install cleanup is included.
Owner worktrees use `codex/pnpm-migration-20260927`, created from fetched
`origin/main`; existing dirty product work stays in its original checkout.

## Finding

The storage mechanism is real. npm normally installs separate dependency files
for each project/worktree; its content-addressed download cache does not make
those installed copies shared. pnpm uses a content-addressable store and imports
via copy-on-write clones or hardlinks, falling back to copying where necessary.
Multiple sessions in one checkout do not each allocate node_modules; multiple
installed worktrees do. Tens of GB is plausible with many duplicated installs,
not a guaranteed saving for this machine or for every repository.

On APFS, normal du output cannot attribute shared clone extents. Directory sizes
are installation footprint estimates, not measured physical reclaim. Migration
patches also do not reclaim old installations until those installations are
replaced or retired. Existing active worktrees must remain intact.

Sources checked on 2026-09-27:
- [pnpm motivation](https://pnpm.io/motivation)
- [pnpm 10 import](https://pnpm.io/10.x/cli/import)
- [pnpm 10 import methods and build controls](https://pnpm.io/10.x/settings)
- [npm cache](https://docs.npmjs.com/cli/v11/commands/npm-cache/)

## Selection

| Repository | Finding | Action |
| --- | --- | --- |
| CineForge | Root npm tooling plus npm UI; competing UI lockfiles | Migrate in isolated owner worktree |
| Echo Forge | npm React/Vite application with repeated installs | Migrate in isolated owner worktree |
| Storybook | Already pins pnpm 9.15.4 | Keep current manager; no unrelated version upgrade |
| RoboRally | No external npm dependencies | Keep; no storage benefit today |
| Dossier | Python tooling | No npm migration |
| Doc Web | Python tooling | No npm migration |
| Board Game Ingester | Python tooling | No npm migration |
| Conductor | No JS dependency manifest | No npm migration |
| AliExpress Capture | Small installed footprint (~26 MiB), no repeated installs established | Defer; small immediate saving |
| Canmore Town Council | No current node_modules; npm Docker build | Defer; no current installed storage to reclaim |
| RPG Map Projector | ~79 MiB installed, no repeated installs established | Defer; small immediate saving |
| Project Agent | Latest local commit in 2025; no evidence of current active npm installation | Defer inactive tooling |
| Legacy/template/upstream copies | Old backups, vendor and example projects | Preserve; no blanket migration |

This is a portable improvement, not a blanket tool-standardization exercise.
The migration pins pnpm 10.34.5 (verified latest 10.x via npm registry) for a
reproducible change. The installed 10.5.2 is too old to enforce CineForge's
existing minimumReleaseAge policy, so it was rejected before final validation. Preserve locked
package versions, review lifecycle-build requirements narrowly, and validate
frozen installation plus affected consumers. No Conductor ADR mandates npm.

## Execution evidence

| Owner | Isolated worktree | Base SHA |
| --- | --- | --- |
| Echo Forge | `/Users/cam/.codex/worktrees/pnpm-migration-20260927/echo-forge` | `d668707e25f6cfb2442f384e9f1f6d70c115133b` |
| CineForge | `/Users/cam/.codex/worktrees/pnpm-migration-20260927/cine-forge` | `f69909d8df04805fe47615a88d40bf84c839f052` |

Owner validation results and the final disk inventory are recorded below.
Docker was initially unavailable; approved close-out started Docker Desktop and
validated the actual changed build paths. See the close-out section for results.


## Measured storage opportunity

The expanded scan covers `/Users/cam/Documents/Projects` and
`/Users/cam/.codex/worktrees`, prunes `.git`, records `node_modules` and stops
recursing inside each recorded installation. It reports no traversal/size/marker
errors. [Inventory](evidence/pnpm-storage-20260927/inventory.json).
Excluding new migration worktrees, 95 directories total **6,961.5 MiB**
by independent `du`: npm **1,321.1 MiB**, pnpm **5,612.8 MiB**, unknown **27.5 MiB**.
Some unknown directories are workspace-level links/caches, not separate full
installs. The pnpm sum can count shared blocks repeatedly and is not a reclaim target.

Echo Forge has five npm installations totaling **954.6 MiB** allocated by `du`.
The parent independently hashed every regular file in those five directories:
**657,179,134 bytes (626.7 MiB)** of identical content repeats across installations
beyond the greatest multiplicity within any single installation. Symlinks are
excluded. [Raw overlap evidence](evidence/pnpm-storage-20260927/echo-content-overlap.json).
This demonstrates substantial reusable content; it is a content-overlap estimate,
not a promise to free 626.7 MiB physically. Store retention, differing versions,
platform binaries, APFS shared extents and metadata affect the actual result.

CineForge has one existing npm installation (~261.4 MiB); its migration prevents
additional full copies in future worktrees and removes inconsistent install
instructions/competing UI lockfiles. The measured npm footprint is only ~1.29 GiB
across the audited roots, so this machine does **not** support the quoted claim
of tens of GB immediately recoverable from replacing these npm installations.

Download caches are separate: an intermediate observation during this task found
npm cache ~746 MiB and the pnpm store ~1.27 GiB (v3 and v10). These were changing
while migration installs ran, are not part of the pre-migration baseline, and
have not been deleted. No recovered-disk-space claim is made for this task.


## Validation scope

Package-manager migration changes installation layout, so validation includes
exact pinned-manager frozen installs, npm-to-pnpm resolved-version comparison,
frontend typecheck/build, relevant tests, launch command forwarding, and current
install/deploy documentation. Dependency versions are not intentionally upgraded.
For Echo Forge, pnpm exposed an undeclared `zod` import: its already-locked exact
version is made a direct dependency, preserving the resolved package set.
No paid model evaluations are part of this validation.

The parent reviewed Docker/setup/launcher diffs. Claude permission scope remains
script-only, and CineForge retains its existing freshness policy. Current
pnpm script examples remove npm-only `--` separators where needed. Historical
eval output, changelogs and completed story evidence retain original commands.


### CineForge initial validation

Implemented and reviewed in the isolated worktree. Owner evidence:
[Story 223](/Users/cam/.codex/worktrees/pnpm-migration-20260927/cine-forge/docs/stories/story-223-pnpm-package-manager-migration.md).
Both independent projects pin 10.34.5 and preserve the 10,080-minute release-age
policy. Imported name/version sets exactly match npm: root 115/115, UI 802/802;
all 1 root and 43 UI direct dependency versions match. Competing npm locks are
removed. Frozen installs, UI lint/typecheck/build, 21 UI tests, four focused PDF
tests, actual synthetic Fountain-to-PDF export, Vite host/port + HTTP 200 smoke,
skill check, methodology check, and diff hygiene pass. The original `npx` product
PDF path remains unchanged and resolves its local pnpm-installed binary.

pnpm blocked `snyk`, `core-js`, `esbuild`, and `msw` dependency scripts; the tested
consumers worked without them, so no broad script allowlist was introduced.
A broader Python unit run passed 2,189 tests and failed five untouched
final-render provider-floor tests. Those failures were not investigated enough
to establish their cause; they are not a passing full-suite result. Docker image
execution remains unverified without a daemon. Story remains In Progress pending
that validation and authorized close-out; no landing claim.


### Echo Forge initial validation

Implemented and reviewed in the isolated worktree. Owner evidence:
[Migration report](/Users/cam/.codex/worktrees/pnpm-migration-20260927/echo-forge/docs/reports/pnpm-migration-2026-09-27.md).
Pins 10.34.5, imports the npm lock, removes the npm lock, and explicitly declares
already-resolved `zod@4.3.6`. All 270 distinct package name/version pairs match
the former npm lock. Frozen install, typecheck, build, methodology/skill checks,
scoped lint, local status command and diff hygiene pass. No ignored dependency
build scripts or pending builds were reported. Docker, setup, current skills,
runbooks, Codex launchers, and internal executable calls now use pnpm.

Full tests: five Node control-intent tests pass; Vitest reports 566 passing,
20 failing (non-App 449/450, App shards 60/68 and 57/68). Two failing cases pass
individually without parallelism; the other 18 App failures were not individually
rerun. Full-suite green is unproven and the cause is not established. Full lint
reports four errors in unchanged `scripts/control-intent-v1-mimo26.mjs` plus
seven warnings. The migration's changed JS/TS files pass scoped lint. Docker
image execution remains unverified. No private-asset sync or paid eval was run.

## Initial handoff

At the initial handoff both migrations were uncommitted in their isolated owner
worktrees, with existing primary installs and all unrelated edits preserved. No disk space has
been deliberately reclaimed. Conductor only adds this report, its inventory,
and scoped inbox/index entries. The practical benefit begins with pnpm installs
from these changes: later worktrees can share package content instead of adding
another npm installation. Resolve the recorded broad-check limits and run the
Docker builds before declaring a fully green release; committing/pushing/landing
required Cam's explicit request, subsequently provided below.


## Approved close-out

Cam approved resolving the recorded validation blockers and landing on 2026-09-27.
A dedicated Conductor worktree at
`/Users/cam/.codex/worktrees/pnpm-migration-20260927/conductor` is based on fetched
`origin/main` at `f278bc1`; only this task's report/evidence and inbox/index entries
are carried over from the shared primary checkout. Existing unrelated captures
and working edits remain intact. Both owner branches matched remote main at
preflight. All three remote main branches are unprotected; no repo CI workflow
was found for these owner branches.

Docker validation now passes:

- CineForge: actual `docker build --target frontend` passes for the changed
  pnpm/frontend stage. The unchanged Python runtime stage was not rebuilt.
- Echo Forge: required `pnpm run deploy:preflight` passes, followed by an actual
  full Docker build. The maintained preflight copies the private spell catalog
  only into its existing ignored local target; no data is committed or uploaded.
- Echo Forge's image starts and serves HTTP 200 for the root page, web manifest,
  PTT health endpoint, and private spell JSON. No provider call or production
  deployment was performed. The temporary smoke container is removed.
- [Image identities and commands](evidence/pnpm-storage-20260927/docker-validation.json)
  and [HTTP smoke evidence](evidence/pnpm-storage-20260927/docker-smoke.json).

### Validation blockers resolved

Echo Forge:

- Narrow ESLint declarations fix the four missing Node-global errors without
  changing the frozen evaluation script. Full lint passes with seven existing
  Fast Refresh warnings; final typecheck and frozen offline install pass.
- A serial diagnostic passes 583 of 586 Vitest assertions. Three multi-step UI
  tests exceed their old limits under load; measured isolated runtimes were
  3.907, 4.932 and 13.710 seconds against 5/5/15-second limits. Test-local limits
  are now 10/10/20 seconds, with assertions unchanged. All three pass with the
  final limits and final fallback command (22.14 seconds total).
- The direct Vitest fallback scripts now exclude Node-runner files exactly as
  the maintained sharded lane does, preventing false “No test suite found” errors.
- Passing evidence covers all 586 Vitest assertions across the serial diagnostic
  and focused reruns, plus five Node control-intent tests. This is explicitly
  **not** a claim of one final green full-suite invocation. The 583 unchanged
  passing assertions are reused under the close-out validation policy.

CineForge:

- The target validator retains byte/hash checks while normalizing the one omitted
  empty schema default, and resolves macOS `/var`/`/private/var` path aliases.
- The oversized transport module/function is split into the existing fingerprinted
  support module, preserving request/cost logic and keeping the original size
  gates. Standalone imports now run after repository path setup. Historical
  evidence/hashes remain unchanged; future runs identify the new implementation.
- Full `make test-unit` passes. Forty-eight standalone strict transport, benchmark
  and token-accounting tests pass; scoped Ruff passes. The parent independently
  confirmed that the moved Gemini function has an identical AST.
- Story 223 is Done after remote implementation landing was verified. Closure
  regenerated methodology views; methodology check and diff hygiene pass. Earlier
  UI, install and Docker evidence remains applicable to the unchanged consumers.

Independent final migration review found no actionable install/lock/Docker/argument
forwarding defects. Parent reviewed the scoped blocker fixes and explicit staging
allowlists. No paid model inference, deployment or old-install cleanup occurred.

### Verified landing

| Repository | Implementation | Final remote main | Result |
| --- | --- | --- | --- |
| CineForge | `3e0e16a62207f624abafcf70504df714e5297520` | `f4a0decd9b89a18756bfcf4a78b44fba5e71e58d` | Landed; second commit closes Story 223 |
| Echo Forge | `ef6bb1e535d5a0d9304f1f258700e15cb66e1ead` | `ef6bb1e535d5a0d9304f1f258700e15cb66e1ead` | Landed |

Both execution branches were pushed, both main updates were fast-forwards, and
`git ls-remote` confirmed the final identities above. Both owner worktrees are
clean. [Final reviewed file identities](evidence/pnpm-storage-20260927/owner-closeout-file-identities.json)
record the committed scope separately from the initial migration snapshot.
The task worktrees and branches remain available. Existing primary checkouts,
npm installations, npm cache and pnpm store were preserved. The migration enables
future storage sharing; it does not claim immediate physical disk reclamation.
