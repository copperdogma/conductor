# Scout 106 — Fly MCP and hosting cost opportunities

Date: 2026-11-05. Source: Cam's pasted Fly.io newsletter.
Current decision (2026-11-06): **Adopt the verified MCP inspection/diagnostic
route; retain CLI deployments and current hosting. Review representative resource
utilization before migrations or commitments.** Initial proposal was a scoped
plugin trial; completed setup and experiment evidence follows below.

Follow-through: MCP diagnostics now locally verified; maintained operating
guidance is in the [shared Fly runbook](../services/fly.md), and the
[owner/runbook comparison](../alignments/align-060-fly-mcp-operations-runbooks.md)
records where to add MCP operations while retaining existing CLI deployments.

## Offering and recommendation

The official [Fly MCP guide](https://mcp.fly.io/) documents OAuth access to existing
apps, Machines, volumes, secrets, Sprites and Managed Postgres. Resource consent
and scopes determine access. IP/certificate inspection is read-only. MPG tools
cannot delete resources or change/return passwords. App creation and deployment
workflows are excluded, so existing owner deployment runbooks still matter.
The public catalog currently says 93 tools; newsletter counts are a dated snapshot.

Prefer the **Fly.io** plugin over the original Sprites plugin or a duplicate bare
MCP connection. Its [official repository](https://github.com/superfly/sprites-codex-plugin)
includes focused resource/Sprite skills and documents:

```sh
codex plugin marketplace add superfly/sprites-codex-plugin
codex plugin add fly@flyio
```

Restart and complete browser consent, selecting only intended apps and read-only
operations initially. The repository says marketplace presence does not imply
publication in the OpenAI directory; connected plugin search did not return a
matching Fly entry. Raw Fly plugin README, skill, MCP manifest and marketplace
manifest were also inspected from official GitHub main. No installation or
authorization changes occurred. [Official OpenAI MCP documentation](https://developers.openai.com/codex/mcp)
confirms HTTP OAuth, tool allowlists and per-tool approval policies.

Fly says credentials for underlying operations are minted server-side and
short-lived in its [design post](https://fly.io/blog/feng-shui-for-robots/).
This improves credential handling; it does not make all tool output non-sensitive:
full Machine configuration and SQL query text can contain private material.

## Read-only local/live evidence

Authenticated installed Fly CLI, checked on this date. App discovery found 14
apps in the personal organization. Focused machine/volume/IP inspection covered
the following apps; no runtime logs, database rows, environment values or secrets
were read. State is a snapshot, not month-long utilization or invoice evidence.

| App / owner | Observed state | Implication |
| --- | --- | --- |
| `roborally-copper-dog` / RoboRally Web | One stopped shared CPU 512 MB Machine, yyz; stop/start and min=0; no volumes | Already idle-saving; leave hosting alone |
| `withered-shape-5801` / Storybook | Suspended 512 MB web Machine; started 2048 MB worker and stopped 2048 MB worker; no volumes | Worker memory/utilization and reliable wake-up are best first review |
| `prod-storybook-db` | Started shared CPU 1024 MB Machine, sjc; attached 1 GB Postgres volume | Existing self-managed DB, not MPG |
| `dev-storybook-db` | Stopped 256 MB Machine, sjc; attached 1 GB volume | Already stopped; retained data still has value |
| `cineforge-app` | Stopped shared 2 CPU / 512 MB Machine, ord; attached 1 GB `cineforge_data_v2`, detached 1 GB `cineforge_data` | Check detached-volume provenance if cleanup is later authorized |
| `echo-forge-app` | Stopped shared CPU 256 MB Machine, ord; no volumes | Already small and stopped |
| `financial-monthly-sure-private` | Started shared CPU 2048 MB Machine, yyz; attached 1 GB volume | Review utilization/availability contract before changing |
| `financial-monthly-sure-db` | Started shared CPU 1024 MB Machine, yyz; attached 1 GB Postgres volume | Existing self-managed DB; do not disrupt finance |

Inspected public-facing IP allocations used shared IPv4 and IPv6; inspected DB
apps used private IPv6. No dedicated IPv4 savings established. RoboRally IP types
were not resolved in the delegate's bounded check. `flyctl mpg list -o personal`
reported no managed clusters. Other organizations were not audited.

Other discovered apps: canmore-town-council-app, dnd-5e-monsters,
el-capitan-copper-dog, financial-monthly-analysis-private,
fly-builder-snowy-grass-8762, mike-epoxy (all app summaries suspended).
These were not individually cost-audited. Discovery does not make them disposable.

Local owner pointers: `docs/services/fly.md`,
`/Users/cam/Documents/Projects/roborally-web/fly.toml`,
`/Users/cam/Documents/Projects/Storybook/storybook/fly.toml` and Storybook's
`docs/stories/story-030-production-deploy.md`. Registry still names historical
finance directories; live resource identity was used without editing membership.

## Cost decisions

All prices USD; current official sources checked on this date.

- [Machines pricing](https://docs.fly.io/about/pricing): 512 MB shared-1x costs
  $3.69/30 days in cheapest regions; regions differ. Stopped rootfs and provisioned
  volumes cost $0.15/GB/month. CineForge's detached 1 GB volume is therefore only
  about $0.15/month, excluding snapshots. No deletion recommended from attachment
  state alone. Shared compute reservations offer $5/month credit for $36/year,
  region-specific, with no rollover. Consider only after measuring stable spend
  and completing rightsizing; $24/year maximum saving on that block.
- [Autostop documentation](https://docs.fly.io/launch/autostop-autostart): proxy
  traffic can wake web Machines. Queue workers need their own reliable waking
  mechanism; do not simply stop the Storybook worker based on an empty snapshot.
- [MPG](https://docs.fly.io/postgres): Basic starts at $38/month plus storage,
  currently $0.28/GB-month of used storage for v2 (older v1 provisioned storage).
  Evaluate as a reliability/maintenance upgrade, not a savings proposal against
  current single-Machine Postgres. No migration recommendation now.
- [Sprites pricing](https://fly.io/sprites/): CPU $0.0385/CPU-hour, RAM
  $0.021875/GB-hour, hot storage $0.000683/GB-hour and cold $0.000027/GB-hour.
  At 720 active hours, 1 GB RAM alone is $15.75/month before CPU/storage; sleeping
  compute is free but retained storage remains billable. Suitable future public
  Linux test/build sandbox, especially to relieve Mac disk use. Not proven cheaper
  for current apps. WebSockets/open TCP, stdout and in-flight requests can prevent
  sleep. Fly's four-hour coding example is $0.23 infrastructure, excluding model
  charges. Defer a paid trial until there is a specific Linux task.
- [Tigris](https://www.tigrisdata.com/pricing/): standard object storage
  $0.02/GB-month, first 5 GB free and free egress, with request charges/allowances.
  Worth comparing for future generated media/assets. It cannot replace Postgres
  or a POSIX volume without application changes. Current volume sizes provide no
  persuasive migration case.

## Portfolio disposition and landing

| Projects | Decision |
| --- | --- |
| Conductor/shared services | Recommend scoped Fly.io plugin pilot, then read-only inventory test; no rollout yet |
| Storybook | Recommend owner-led worker utilization/RSS/queue wake-up review first; retain database |
| CineForge | Retain Machines; tiny detached-volume provenance check belongs in any later approved cost audit |
| RoboRally Web, Echo Forge | Retain existing cheap idle behavior |
| Financial Data/Reporting and historical finance registry entries | Retain current runtime; utilization review only with owner/privacy boundaries |
| Dossier, Doc Web, Boardgame Ingester | Defer Sprites until a named public/synthetic Linux workload justifies a test |
| Robo Rally engine, Ultima IV Web, VLC Thumbs | No adoption now; no need to move local/static workloads |

No owner-specific future task was dispatched: recommendations above need a
selected next scope; there is no authorized target implementation. No target
repo edits, worktrees, resource changes, deployments, purchases, commits or pushes.
Saved scout/index/intake only. Existing unrelated Conductor changes preserved.

Confidence: high in documented capabilities and resource snapshot; medium in
potential savings; no invoice, historical utilization, queue backlog, peak RSS,
backup quality, reservation eligibility or runtime migration test was inspected.
Recommended next step: install/authorize only Fly.io for intended apps with
read-only tools, verify discovery, then use the evidence for a bounded savings
proposal before any billable-resource or runtime change.

## Approved plugin setup follow-through — 2026-11-05

Cam replied `yes` to the scoped read-only plugin setup and verification proposal.
Added official marketplace `superfly/sprites-codex-plugin` (`flyio`), then installed
`fly@flyio` version `1.0.0` using the installed Codex CLI 0.162.1. CLI plugin
listing confirms installed/enabled. Cache:
`/Users/cam/.codex/plugins/cache/flyio/fly/1.0.0`.

Read the installed Fly skill and resource reference. Added a user-config policy
at `plugins."fly@flyio".mcp_servers.fly` in `/Users/cam/.codex/config.toml`:
19 read-only inventory/context/machine/volume/IP/certificate/MPG tools only,
with `default_tools_approval_mode = "prompt"`. Excludes writes, execution,
secret metadata, sensitive Machine configurations and SQL query text. TOML
parse/readback verified; other parsed settings and direct MCP definitions
preserved. No duplicate bare MCP server registered.

**Incomplete:** no Fly tools appeared in this already-running chat, and the
computer-use tool refused access to the Codex app for safety reasons. Did not
work around that restriction or start a separate login. User must restart Codex,
connect the installed Fly.io plugin and select intended apps/read-only access in
browser consent. Then verify using `get_fly_context`, `list_apps` and summary
inventory tools. Host tool allowlisting is verified; server-side OAuth scope
and successful MCP discovery remain unverified. No Fly resources changed and
no purchase, commit or push occurred.

## Storybook worker cost review — 2026-11-06

Cam approved a read-only worker-cost/savings review. **Decision: retain the
always-available 2 GB worker for now; no demonstrated safe reduction.**

### Evidence and practical interpretation

- Current checked-out `fly.toml` assigns shared 1 CPU / 2048 MB to
  `slow_lane_worker`, with HTTP/autosuspend restricted to the separate 512 MB
  `app` group. Initial CLI evidence above confirmed deployed worker sizing;
  current MCP summaries do not expose sizing/process groups. Git blame traces
  2048 MB to `06d3b368f`, and role isolation to `e4e4bc2c3`.
- Storybook `docs/stories/story-116-replay-processing-isolation-architecture.md`
  lines 65–88 record the April 29 replay incident: 512 MB and then 1024 MB
  suffered OOM/crash-loop symptoms; 2048 MB restored health. This predates process
  isolation and subsequent bounded dispatch. It is historical risk evidence,
  not proof that today's worker still needs 2 GB. The same story's verification
  plan explicitly calls for production-like replay memory/CPU measurements.
- Current `packages/backend/src/slow-lane-worker.ts` polls audio every 5 seconds,
  document understanding every 30 seconds, and retries/cleanup/incident sync
  every 60 seconds. Private-object cleanup precedes provider readiness and
  continues in maintenance-only mode. Stopping the whole worker affects this
  work as well as extraction. Its disabled mode deliberately keeps the process
  alive, so disabling processing alone does not stop compute charges.
- Story 199's shared slow-lane dispatcher limits checkpoints to two local slots,
  with correction retries and replay maintenance each single-flight; these are
  not a process-wide measured
  RAM ceiling. Audio/document/maintenance paths also exist. Audio processing
  loads original bytes into a Buffer; average idle memory would not qualify
  peak-work sizing.
- Successful MCP machine listing still shows two started Machines and one
  stopped Machine. The known worker `865109fe407158` is started in sjc; its
  returned lifecycle history contains launch/start/uncordon on October 25 and
  no subsequent exits. This is not an OOM-free historical utilization proof.
  The stopped standby does not incur running CPU/RAM charges; rootfs remains
  billable. It is not a second running worker charge to eliminate.

### Established options and costs

The general problem is sizing a durable background processor with bursty peak
memory and maintenance duties, not HTTP idle scaling. Checked official
[worker autoscaling](https://docs.fly.io/launch/autoscale-by-metric): Fly supports
queue metrics and an independently running autoscaler. Adapting it here would
need wake-up coverage for every job/cleanup lane, due-time semantics and safe
draining. Extra controller cost and complexity make it unattractive at this bill.
Combining worker and web would undo Story 116's outage isolation; defer.

[Official pricing](https://fly.io/pricing/), fetched with `Accept: text/markdown`,
documents sjc multiplier 1.192 on both CPU and RAM, baseline shared-1x/256 MB
about $2.19 per 30 days, and extra RAM $6/GB-month. Derived approximate
always-running estimates (USD, no taxes/credits/traffic/rootfs):

| Worker RAM | Compute / 30 days | Saving against 2 GB |
| --- | --- | --- |
| 2 GB | $15.13 | — |
| 1 GB | $7.98 | $7.15 |
| 512 MB | $4.40 | $10.73 |

These use displayed rounded base rates; not an invoice quote. Region migration
to cheapest compute would save only about $2.44/month on this worker, before
cross-region DB traffic/latency or moving the DB. No region change recommended.
One region-specific $36/year reservation credit block yields at most $24/year
in savings; defer commitments until sustained eligible billed usage is checked.

### Metrics limitation and recommendation

The read-only MCP allowlist has no CPU/RAM history or billing tools. Explicitly
disclosed using the existing CLI session to query the official Prometheus API
for this exact app/worker only. Existing-token output stayed inside Python and
was neither printed nor persisted. Eight bounded memory/CPU/up/OOM queries
returned HTTP 401. A format-only check confirmed a single-line token with no
FlyV1/Bearer prefix; no retry with speculative credentials, new token, login or
permission changes. No metrics were obtained.

[Official monitoring docs](https://docs.fly.io/monitoring/metrics) describe free
managed metrics with about 15-day retention, per-instance memory availability,
CPU and exit/OOM data. A future sizing decision needs accessible recent metrics
plus a representative replay/audio/document peak, including Python child memory
and simultaneous jobs. Sampling only quiet production periods is insufficient.
An isolated synthetic smaller-memory test could qualify a later change; no
provider calls, local harness execution, private data access or production load
test were run in this review. No new test of an unchosen scaling approach was
appropriate in a read-only task.

Recommendation: keep the current worker. Potential ~$7/month RAM saving is not
qualified against prior failures. Fix metrics access as part of the next real
operations task rather than creating an optimization rollout now. No target
repo edits or worktrees; report recorded here only. No infrastructure changes,
resource deletion, reservations, deployments, commits or pushes.

## MCP verification completed — 2026-11-06

### Diagnostic experiment completed after restart — 2026-11-06

Cam restarted and asked to check again. `get_machine_memory` and
`exec_machine_command` now load. Reconfirmed the exact Storybook worker
`865109fe407158` is started; the web Machine is suspended, standby stopped.
The memory tool returned `available_mb=2048, limit_mb=2048`. Do **not** interpret
that as guest free RAM: a direct MCP execution of `cat /proc/meminfo` returned
2015880 KiB total and 1623208 KiB available. The tool result may reflect the
Machine memory-control interface rather than guest available memory; semantics
remain unverified. No limit/reclamation tool was invoked.

A bounded read-only `node -e` diagnostic through `exec_machine_command` then
read `/proc/stat` twice five seconds apart and `/proc/meminfo` once. Result:
CPU busy 0.3992%, steal 0.1996%; total 2015880 KiB, available 1622672 KiB,
used excluding available/reclaimable memory 393208 KiB (~384 MiB); no swap.
This includes the short-lived diagnostic process. It is a quiet five-second
snapshot, not representative load/peak evidence or process RSS history.

The first richer command (with explicit timeout) returned generic invalid
tool/arguments, request ID `GOWpvXg3GoGthoUAA7zR`; smaller commands without the
optional timeout succeeded. Exact cause not isolated; no claim that timeout
alone caused it. No retry of a potentially mutating command, app workloads,
private data, secret/configuration reads, file writes, or lifecycle changes.

**Corrected capability conclusion:** MCP can obtain current CPU/RAM via bounded
OS diagnostics even though the separate Prometheus API auth failed. Current
low usage justifies considering representative sizing measurement, but does
not invalidate the recorded historical OOMs or qualify a production downsize.

### Earlier setup stages (before the completed diagnostic above)

The following records retain the earlier limited catalog and pre-refresh state.
They do not supersede the successful bounded OS diagnostic above.

Later diagnostic correction: Cam asked to test the MCP itself for CPU/RAM after
the CLI metrics failure. The initial allowlist excluded `get_machine_memory`.
Current official `https://mcp.fly.io/guide.md` documents it as a read of current
memory limit/availability, despite requiring Machine write scope. It also
documents `exec_machine_command`, which can run a bounded read-only OS metrics
sample. Neither supplies historical Prometheus data. Enabled those two tools
in the existing plugin policy for this experiment; command execution has an
explicit per-tool `prompt` policy. No other mutating tools enabled. These tools
have not yet appeared in the active tool catalog, so user plugin refresh is
needed before the MCP experiment can run. No CPU/RAM measurements obtained yet.
The earlier conclusion should not imply the MCP was fully tested for current
usage: the initial host allowlist prevented that test.

After Cam connected the plugin, direct `mcp__fly` tools loaded. Successful
`get_fly_context`, `list_apps` (organization `cam-marsollier`) and summary
`list_machines` calls for Storybook and RoboRally verify actual MCP access.
The authorized app listing returned ten apps, including CineForge, Storybook,
Echo Forge, both finance web apps and RoboRally. It does not establish that
other resources absent from this grant no longer exist.

Current snapshot: Storybook has two started Machines and one stopped Machine
in sjc; RoboRally has one started Machine in yyz. Summary tools do not report
process group or memory. Earlier CLI sizing/process evidence is dated above;
do not infer a new configuration from current lifecycle state.

The server-side OAuth grant is **broader than the read-only pilot**: it includes
write, delete, exec and sensitive Machine read scopes for the authorized apps
and an organization binding. No Sprites or MPG grant was returned. Local host
allowlisting is effective in this chat: exactly 15 exposed Fly tools, all from
the configured read-only inventory set; the four MPG tools are absent. No
write/exec/configuration/SQL/secret tools are exposed. Do not describe OAuth
itself as read-only. Narrowing server consent remains a separate improvement.

Only four read-only MCP calls were made; no resources were started, stopped,
modified or deleted. Setup and discovery verification are complete, with the
server-grant breadth caveat. No provider spend, target edits, commits or pushes.
