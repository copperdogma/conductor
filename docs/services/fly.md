# Fly.io

Use for containerized applications, Node/WebSocket servers and worker processes.
An existing organization and CLI login can bootstrap a new app; an old app's
configuration, volume and deploy token must retain their own identities.

## Existing access and examples

`fly-local-cli` contains a copy of `access_token` from `~/.fly/config.yml`, mapped
to `FLY_API_TOKEN`. This is a potentially broad **personal CLI session** with
unverified validity/expiry. Prefer the installed CLI's existing session for
interactive local work. Do not put this copy into CI or every new app.

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
