# Fly.io

Use for containerized applications, Node/WebSocket servers and worker processes.
An existing organization and CLI login can bootstrap a new app; an old app's
configuration, volume and deploy token must retain their own identities.

## Choose MCP or CLI

Checked 2026-11-06. Prefer the official **Fly.io** plugin (`fly@flyio`, endpoint
`https://mcp.fly.io`) for authorized agent inspection and bounded live diagnostics.
Keep each project's existing CLI/scripts for builds, image publication, release
migrations, deployment, rollback and CI. The current MCP does not implement a
complete deployment workflow or app creation. Creating a Machine from an image
is not a substitute for a project's deploy procedure.

| Task | Route |
| --- | --- |
| Identify authorized organization/apps | MCP `get_fly_context`, then `list_apps` |
| Inspect Machine status/events, volumes/snapshots, IPs/certificates | MCP summary tools first |
| Current CPU/RAM diagnostics on an already-running Machine | MCP bounded `exec_machine_command`; see below |
| CPU/RAM history, utilization peaks, billing | Existing Fly metrics/dashboard/API workflow; MCP has no general historical Machine metrics query in the checked catalog |
| Build/deploy, migrations, release/image capture, rollback, CI | Owning repo CLI/script/runbook with its existing gates |
| Resource mutation or secret management | Only within the task's explicit scope and owner runbook; an available tool is not permission |

Conductor's cross-project comparison and proposed owner-runbook changes:
[Alignment 060](../alignments/align-060-fly-mcp-operations-runbooks.md).
Detailed source/experiment record: [Scout 106](../scout/scout-106-fly-mcp-and-cost-opportunities.md).

## Connection and permission checks

Use the installed plugin's own tools; do not create a second bare MCP connection
or copy a CLI/Sprites token into it. Plugin sign-in uses browser OAuth. Setup on
a new host follows the [official plugin repository](https://github.com/superfly/sprites-codex-plugin):

```sh
codex plugin marketplace add superfly/sprites-codex-plugin
codex plugin add fly@flyio
```

Restart/refresh the host if needed and complete plugin consent for intended
resources. Recheck current commands/help before a new installation. The bundled
Fly skill is the operating guide; use its direct tools and current schemas.

1. Call `get_fly_context` and resolve the exact app and organization. The checked
   organization slug is `cam-marsollier`; do not substitute the CLI alias
   `personal` into MCP arguments requiring a concrete slug.
2. List Machines and select the intended running instance. Summary tools omit
   configuration/secrets. Re-resolve after deployment; IDs and standby pairings
   can change. Do not start a stopped app just to inspect usage without scope.
3. Check both **server consent** and the **host tool allowlist**. Our initial
   allowlist hid diagnostic tools even though the OAuth grant permitted them.
   A successful sign-in or loaded skill alone does not prove tools are callable.
4. If tools are absent, refresh/reconnect the installed plugin; do not bypass
   denied access through another identity or connection. After a real scope
   failure, correct the intended grant rather than repeatedly retrying.

On this Mac, `~/.codex/config.toml` configures this plugin under
`plugins."fly@flyio".mcp_servers.fly`. It currently allows inventory tools plus
`get_machine_memory` and `exec_machine_command`; command execution has an
explicit `prompt` approval policy. These are host-local settings, not portable
repo configuration. The observed OAuth grant also includes write/delete/exec
and sensitive-read scopes: **do not call the server grant read-only**. The host
allowlist restricts available tools, while each task still limits use.

## Live CPU/RAM diagnostics through MCP

Locally demonstrated on Storybook's already-running worker on 2026-11-06:
`exec_machine_command` with `body.command=["cat", "/proc/meminfo"]` succeeds.
Pass an explicit argv array; no implicit shell is used. Restrict diagnostics to
resource counters. Do not read environment, command arguments, user payloads,
credentials, databases or logs as a shortcut to metrics.

For a Node-based image, a bounded CPU sample was also verified by invoking
`node -e` with code that reads `/proc/stat`, waits five seconds, reads it again,
and reads `/proc/meminfo`. Use the installed runtime appropriate to that image;
do not install diagnostic packages or generate application work for an inspection.
The [experiment record](../scout/scout-106-fly-mcp-and-cost-opportunities.md)
identifies the Machine, measured interval, successful route and failed attempt.
For a repeatable CPU calculation:

- Read the aggregate `cpu` row's first eight counters (user through steal) twice;
  do not add guest counters again. Compute their deltas and total delta.
- CPU busy fraction is `(total - idle - iowait - steal) / total`; report steal
  separately. Bound the interval and handle a zero total delta honestly.
- Guest RAM used excluding available/reclaimable memory is
  `MemTotal - MemAvailable` from `/proc/meminfo`. Values are KiB; divide by 1024
  for MiB. This is VM-level memory, not summed process RSS.

Observed sample: ~0.4% busy CPU over five seconds, ~384 MiB used, ~1.55 GiB
available, no swap. The diagnostic itself contributes some resource use.
These observations do not measure extraction/audio peaks or prove 1 GB is safe;
Storybook has historical OOM evidence at 1 GB before its later process isolation.

`get_machine_memory` returned `limit_mb=2048, available_mb=2048` while guest
`MemAvailable` was ~1585 MiB. Treat that control-plane response as distinct from
guest RAM counters; its availability semantics were not verified. Never infer
that the entire VM is free from that response, or call memory limit/reclaim tools
merely to measure usage. The read query requires Machine write scope upstream,
which does not authorize other writes.

The first richer exec request returned generic invalid-tool/arguments; smaller
requests without the optional timeout succeeded. The exact cause is unknown:
do not claim timeout is broken. A bounded read can be simplified after a schema
check; a timed-out write requires result inspection before any retry.

The separate Prometheus API attempt returned HTTP 401 with the existing CLI
session. That did not prevent MCP diagnostics. Keep authentication/transport
failures separate from conclusions about infrastructure cost or safe sizing.

## Existing access and examples

`fly-local-cli` contains a copy of `access_token` from `~/.fly/config.yml`, mapped
to `FLY_API_TOKEN`. This is a potentially broad **personal CLI session** with
unverified validity/expiry. For CLI-only workflows, prefer the installed CLI's
existing session; use plugin OAuth for MCP inspection. Do not put this copy into
CI or every new app.

Local references under `/Users/cam/Documents/Projects`:

- `roborally-web/fly.toml`, `Dockerfile`, `docs/runbooks/deploy.md`: app
  `roborally-copper-dog`, region `yyz`, one machine, in-memory game rooms,
  idle stop/start, `/health`, Fly TLS at `roborally.copper-dog.com`.
- `Storybook/storybook/fly.toml`, `AGENTS.md`,
  `docs/stories/story-030-production-deploy.md`: app `withered-shape-5801`,
  region `sjc`, separate app/worker processes, Postgres and migrations,
  `storybook.chat`. Check current owner deployment policy before adapting it.

## New app recipe

1. Confirm local CLI identity and available organizations using read-only
   `flyctl auth whoami` and `flyctl orgs list`. Choose the intended organization
   explicitly before creating resources; no org identity was verified here.
2. Prepare the new app's Dockerfile and `fly.toml` with a unique name, correct
   internal port, health checks, region, CPU/RAM, machine count and idle policy.
   Use `flyctl launch --no-deploy` only within an authorized setup task and check
   current CLI help. It can create provider resources even without deployment.
3. Plan volumes/database/backups and release migrations if state persists.
   One-machine in-memory rooms lose games at deploy; multiple machines require
   an explicit shared-state/routing design.
4. Store per-app runtime secrets with Fly's secret mechanism through a private
   input path, not command arguments containing literal values. Keep the new
   app's own database/session secrets independent of existing projects.
5. Configure domain ownership/TLS records from Fly's output in Cloudflare.
   Existing RoboRally uses a DNS-only CNAME plus ACME CNAME and ownership TXT.
6. Deploy through the owning runbook and verify health, domain/TLS and key user
   flows. Account for migrations and active sessions in the rollback plan.

For CI, create a named, expiring **app-scoped deploy token**, e.g. the current
`fly tokens create deploy` command with explicit `--app` and `--expiry` options
(check installed help). Capture generated output directly into a protected
destination rather than chat/logs. For a new app, an existing app-scoped token
cannot be assumed to provision or deploy it.

[Fly's access-token guidance](https://docs.fly.io/security/tokens), checked
2026-10-28, distinguishes scoped deploy/org tokens from the short-lived personal
login token. Token generation, token validity and provider deployment were not
tested during catalog setup.
