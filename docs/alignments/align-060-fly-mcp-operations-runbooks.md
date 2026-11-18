# Alignment 060 — Fly MCP operations and deployment runbooks

Date: 2026-11-06. Scope: Cam requested a durable write-up of the MCP experiment,
inspection of Fly-deploying repos, and recommendations for their runbooks.
**Completed:** shared Conductor runbook update and read-only owner comparison;
subsequently approved Storybook-only documentation patch committed and landed.
**Not applied:** other target rollouts, membership/runtime changes or deployment.

## Decision

Prefer the official Fly.io plugin for authorized interactive inventory and
bounded CPU/RAM diagnostics. Keep each owner's CLI/scripts for build/deploy,
migrations, immutable image/release evidence, rollback and CI. This is a
**portable operations improvement**, not a replacement deployment mechanism.
Local deployment gates, state preservation and authorization are intentional
adaptations. Do not replace them with generic MCP Machine mutations.

The [official MCP guide](https://mcp.fly.io/guide.md), retrieved on this date,
explicitly excludes deployment workflows and app creation. Its memory-read and
exec tools support the locally demonstrated route; no general historical CPU/RAM
query appeared in the checked catalog. Full Machine configuration can contain
sensitive data; read summaries first. CLI-only features such as release/image
history and app logs still require their appropriate existing route. Do not
invent a general log, health, release or deploy tool from the plugin name.

## Durable experiment record and shared changes

Updated [shared Fly runbook](../services/fly.md) and [service entry point](../services.md).
[Scout 106](../scout/scout-106-fly-mcp-and-cost-opportunities.md) retains the
actual sequence, permissions and uncertainty:

- Host allowlisting initially hid `get_machine_memory` and
  `exec_machine_command`; refreshing the installed plugin exposed them.
- Bounded direct MCP `/proc/meminfo` and five-second `/proc/stat` sampling on
  Storybook's already-running worker succeeded: ~384 MiB RAM used, ~1.55 GiB
  available, ~0.4% CPU busy. Quiet sample only; no peak-sizing conclusion.
- The memory tool returned 2048 MiB for both limit and availability, differing
  from guest available RAM. Interpret those surfaces separately; do not claim
  verified semantics for the control-plane field.
- The independent Prometheus route returned 401. That did not block MCP
  diagnostics and did not justify abandoning the MCP experiment.
- The server OAuth grant is broader than host tool policy. Current host policy
  exposes inventory plus memory and exec diagnostics, with exec prompting.
  Permission to diagnose does not authorize mutation, private payload reads,
  application processing or load generation.
- No Fly resource was reconfigured, restarted, resized or deleted.

Cam also requested that this be remembered; a small ad-hoc memory note points
to these maintained documents without copying credentials.

## Repo and runbook inventory

Paths in this table are relative to `/Users/cam/Documents/Projects`.
These are source/working-copy observations, not proof each repo is currently
deployed or that a documented procedure is freshly exercised.

| Owner / checkout | Fly target and current source mechanism | Existing documentation | Recommendation |
| --- | --- | --- | --- |
| Storybook — `Storybook/storybook` | `withered-shape-5801`; `/deploy` invokes CLI blue-green deploy, migrations, override/standby checks and smoke gates | `.agents/skills/deploy/SKILL.md`; `docs/decisions/adr-014-ai-operated-deployment/adr.md`; `docs/deploy-log.md` | Add MCP inventory/diagnostic subsection; preserve Dossier/identity/privacy gates, immutable rollback image and standby pairing. Keep CLI log/release/override helpers. |
| CineForge — `cine-forge` | `cineforge-app`; CLI through local deploy skill; persistent `cineforge_data_v2` at `/app/output` | `.agents/skills/deploy/SKILL.md`; `docs/deployment.md`; `docs/deploy-log.md` | Add MCP target/volume inspection and bounded diagnostic option; preserve durable project/run/artifact storage and secret handling. |
| Echo Forge — `echo-forge` | `echo-forge-app`; CLI deploy skill, static PWA plus server-side provider use | `.agents/skills/deploy/SKILL.md`; `docs/deployment.md`; `docs/deploy-log.md` | Add brief operations section; retain preflight, image build and smoke/log flow. Static UI does not mean provider secrets are public. |
| RoboRally Web — `roborally-web` | `roborally-copper-dog`; `make deploy` runs asset/build tasks and `flyctl deploy --remote-only --ha=false` | `docs/runbooks/deploy.md:1`; `Makefile:43` | Add MCP discovery/status/diagnostics; keep single-Machine/in-memory-room and shared-login semantics. Deployment ends active games. Engine repo `roborally` is a distinct owner. |
| El Capitan Web — `el-capitan-web` | `el-capitan-copper-dog`; checks/assets/build then `fly deploy` | `docs/runbooks/deploy.md:1`; `AGENTS.md` | Add brief MCP operations section. Runbook records standing deploy approval; AGENTS contains older per-deploy wording. Preserve actual owner authorization and flag wording conflict rather than inventing a new gate. Rooms are volatile. |
| Canmore Town Council — `canmore-town-council` | `canmore-town-council-app`; CLI deploy skill with preflight/status/smoke/log steps | `.agents/skills/deploy/SKILL.md`; `docs/deployment.md`; `docs/deploy-log.md` | Add operations section if maintained; keep existing setup/DNS/certificate/secrets boundaries and deploy authorization. |
| D&D Monsters — `dnd-5e-monsters` | `dnd-5e-monsters`; README uses `flyctl deploy`; static nginx image | `README.md:37`; `fly.toml`; `Dockerfile` | A short deploy/operations runbook would clarify both publishing routes. MCP can inspect the direct Fly app; custom `dnd.copper-dog.com` is published from the separate DreamHost umbrella. |
| Financial source/tooling — `financial-data` | Root `financial-monthly-analysis-private` and `sure-overlay/runtime/production/fly.toml` target `financial-monthly-sure-private`; guarded scripts/CLI | `docs/runbooks/deploy-private-report.md`; `docs/runbooks/monthly-handoff.md`; `AGENTS.md` | Keep source facts and historical operator tooling here; add only an ownership pointer if a rollout is selected. Do not route current consumer deployment here merely because its Fly config is present. |
| Financial consumer — `financial-reporting` | Owns Sure deployment/publication; maintains release builder and monthly-delivery controller; uses some source-repo tooling/worktrees | `AGENTS.md:11`; `docs/runbooks/private-report-runtime-release.md`; `docs/runbooks/monthly-source-handoff.md`; `docs/runbooks/monthly-delivery-runner.md` | Add MCP summaries/diagnostics here, preserving exact targets, backups/clone rehearsal, native state, viewer/access protections and routine-delivery authorization. Do not substitute generic exec for the qualified controller or public-code image builder. |
| AI Calendar Helper — `ai-calendar-helper` | `ai-calendar-helper`; npm/CLI instructions with Prisma release migrations | `README.md:193`; `docs/stories/story-028-deployment.md`; `fly.toml` | Old/unverified candidate. README's supposedly authoritative `docs/deployment/flyio.md` is missing; resolve actual ownership/status before updating deployment guidance. Do not rerun first-time setup or migrations. |
| Mike's website — `mike-website` | `mike-epoxy`; Vite/nginx build then `fly deploy --depot=false --yes` | `docs/deployment.md:1` | Add MCP inspection guidance if this is the maintained source. No Git repo detected; identify durable source ownership before treating it as a managed rollout target. |

No GitHub Actions deployment path was identified in the bounded relevant
searches; this does not assert that no remote CI or uninspected script exists.
Current source instructions use CLI directly or wrap it in skills/scripts.

### D&D boundary confirmed separately

`copper-dog-dnd-site/README.md` describes a DreamHost static site built from
pinned `dnd-spells` and `dnd-5e-monsters` submodules. Its build copies monster
HTML/JSON/assets into `/druid-shape-change-beasts/`; it does not link/proxy the
Fly app. A Fly deployment alone cannot update that site. Preserve reproducible
commit handoff to the umbrella, auth and its narrow asset bundle. This repo
does not need a Fly deployment migration.

## Membership and discovery evidence before any rollout

`projects.yaml` was compared with the current Codex project list and bounded
local Git/config discovery. No enrollment/removal was inferred.

Full current registry (unchanged):

| Key | Registered checkout | Observation |
| --- | --- | --- |
| dossier | `/Users/cam/Documents/Projects/dossier` | Present |
| storybook | `/Users/cam/Documents/Projects/Storybook/storybook` | Present |
| doc-web | `/Users/cam/Documents/Projects/doc-web` | Present |
| cine-forge | `/Users/cam/Documents/Projects/cine-forge` | Present |
| boardgame-ingester | `/Users/cam/Documents/Projects/boardgame-ingester` | Present |
| roborally | `/Users/cam/Documents/Projects/roborally` | Present; engine, distinct Web repo |
| echo-forge | `/Users/cam/Documents/Projects/echo-forge` | Present |
| ultima-iv-web | `/Users/cam/Documents/Projects/ultima-iv-web` | Present |
| financial-hub | `/Users/cam/Documents/Projects/financial-hub` | Missing; current renamed consumer is Financial Reporting |
| financial-monthly-analysis | `/Users/cam/Documents/Projects/financial-monthly-analysis` | Missing; current renamed source is Financial Data |
| vlc-thumbs | `/Users/cam/Documents/Projects/ultima-iv-web/vlc-thumbs` | Missing; no replacement inferred |

Plausible Fly-owner additions/replacements for a later membership decision:

| Checkout | Available activity evidence | Suggested treatment |
| --- | --- | --- |
| `/Users/cam/Documents/Projects/financial-data` | App-listed Git project; commit `6325524`, 2026-11-06 | Replace stale source registry path/key only with Cam's selection |
| `/Users/cam/Documents/Projects/financial-reporting` | App-listed Git project; commit `142a4bc`, 2026-11-05 | Replace stale consumer path/key only with Cam's selection |
| `/Users/cam/Documents/Projects/roborally-web` | Git commit 2026-10-26; current Fly app already verified | Add as distinct Web owner if selected |
| `/Users/cam/Documents/Projects/el-capitan-web` | Git `97f57e3`, 2026-10-30; October hosting runbook | Candidate addition; not the engine/Web equivalent of another repo |
| `/Users/cam/Documents/Projects/dnd-5e-monsters` | App-listed Git project; November 6 work/commits | Candidate addition with separate umbrella publishing route |
| `/Users/cam/Documents/Projects/canmore-town-council` | App-listed Git project; last commit 2026-07-18 | Candidate; maintenance priority unconfirmed |
| `/Users/cam/Documents/Projects/ai-calendar-helper` | Git last commit 2025-07-22; configured target absent from previously authorized app list | Defer until owner/activity is confirmed |
| `/Users/cam/Documents/Projects/mike-website` | App-listed directory and Fly app; no Git history detected | Resolve source/versioning first; do not auto-enroll |
| `/Users/cam/Documents/Projects/copper-dog-dnd-site` | App-listed Git umbrella with pinned monster source | Optional non-Fly owner; keep DreamHost route |

Discovery covered 75 distinct Git common directories in a shallow primary-repo
pass and a separate Fly-config scan to four directory levels, pruning dependencies,
generated/runtime outputs and archives. It is not exhaustive disk inventory.
Finance source worktrees under Reporting resolve to Financial Data's common Git
directory and are not new projects. D&D source submodule is an embedded upstream
copy, not another independent rollout target. Storybook legacy/legacy-noauth
copies are separate Git directories but historical; not selected. App-provided
outside-root projects were checked for relevant naming/context; private medical,
tax and unrelated repositories were not inspected for infrastructure.

## Next route, validation and limits

Initial comparison: shared runbook updated; owner repos unchanged. Recommended next route
is targeted documentation only, once Cam selects membership/targets: add short
MCP operations guidance to existing maintained docs/skills, retain all deployment
commands/gates, and link the shared diagnostic caveats. No broad skill copying,
new deploy framework or runtime work is justified. Correct broken/stale ownership
pointers as selected, not as an implicit portfolio cleanup.

No temporary worktrees were created during the initial comparison. Approved target edits use dedicated
branches/worktrees under `/Users/cam/.codex/worktrees/<task>/<project-key>` and
account for retained evidence at handoff. No commit or push is authorized here.

Validation: shared-doc whitespace and local Markdown link checks; the diagnostic
proof reuses this chat's successful unchanged MCP calls. No new production samples,
builds, provider calls, tests or deployments needed for this documentation pass.
No secrets or private records were inspected. Technical confidence is high for
checked docs/current catalog, limited for deployment freshness of old candidates.

## Approved Storybook-only patch — 2026-11-06

Cam replied `yes` to preparing a Storybook-only runbook patch in an isolated
worktree, retaining all deployment commands/gates. This explicitly selects the
existing Storybook owner; no registry changes, other owner edits or deployment.

Prepared files:

- `docs/runbooks/fly-mcp-operations.md`: local target/role discovery, host versus
  server grant, bounded resource-counter sampling, historical metric limits,
  control-plane memory caveat, dated quiet sample and sizing caution.
- `.agents/skills/deploy/SKILL.md`: optional runbook reference only. Programmatic
  comparison proves removing that two-line reference restores the exact base
  skill, preserving every deployment command/gate. No new prerequisite.

Worktree accounting:

- Owner: this Conductor Fly.io operations chat.
- Path: `/Users/cam/.codex/worktrees/fly-mcp-runbook-20261106/storybook`.
- Branch: `codex/fly-mcp-runbook-20261106`.
- Base: freshly fetched `origin/main`, `4e6775a3e1f9e1e2600dafec3a4a87183ab3e2b5`.
- State: retained, two uncommitted doc changes for review; no staging/push/merge.
  Sparse documentation checkout is about 2.8 MiB; no dependencies, runtime,
  credential files or provider evidence copied. Continue with explicit `git -C`
  or workdir; main checkout remains on its existing active branch.
- The app managed-worktree request did not return a path/operation ID and was
  stopped after repeated waits. Git inventory showed no new worktree from it.
  Used standard Git `worktree add --no-checkout` plus sparse checkout under the
  approved root instead. Initialized the new worktree index with `read-tree -mu
  HEAD` before editing; final status has only the intended skill/runbook changes.
  Sources: [Git worktree](https://git-scm.com/docs/git-worktree) and
  [sparse checkout](https://git-scm.com/docs/git-sparse-checkout). No speculative
  deletion/pruning of other worktrees. No app attachment path was returned.

Checks: `git diff --check`; new-file whitespace and four relative Markdown links
(sparse-missing targets verified in the base Git tree); exact deployment-procedure
preservation; `bash scripts/sync-agent-skills.sh --check` passes (39 skills).
An extra optional `--check-aliases` attempt reported missing `align.toml`;
`git ls-tree HEAD .gemini/commands` confirms no generated aliases are maintained
in this base, so that optional check is not applicable. No aliases generated.
No methodology inputs/generated views or product code changed, so no methodology
compilation, product tests, runtime restoration or build is required for this
documentation-only patch. Existing runtime diagnostic proof was reused, not rerun.

Ready for review/authorized landing, not already installed in primary checkout.

### Storybook landing completed

Cam then explicitly approved committing/pushing this Storybook-only patch.
Applied the owning finish-and-push workflow, added the required changelog entry,
reviewed the inbox for related unhandled capture (none found), and reused the
unchanged documentation/skill proof. Changelog and final file identities were
freshly checked; no product code, methodology inputs or generated aliases changed.

Commit `bfd37384836c233cd0a21e36d82a7b2d8daa342b` (`Document Fly MCP inspection
and diagnostics`) contains exactly the new runbook, two-line deploy-skill link,
and changelog entry (three files, 109 insertions). Pushed execution branch
`codex/fly-mcp-runbook-20261106`, refreshed origin/main, and fast-forward pushed
`HEAD:main`. `git ls-remote` verifies both remote refs at that exact commit.
Worktree status is clean, including ignored/untracked inspection.

Retained worktree at the path above, owner this chat, same branch, now landed on
remote main; no cleanup was requested. Primary Storybook checkout/active branch
and unrelated changes remain untouched. No Fly operations or deployment ran.
Conductor's local documentation records were updated but are excluded from this
Storybook-only commit/push scope.


## Recovered record status

The Storybook-only runbook landed at `bfd3738` as the dated receipt above records.
Other portfolio rollout was not selected. This is historical diagnostic evidence,
not a current utilization sample or permission to resize a service.
