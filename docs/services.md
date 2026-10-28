# Shared services: start here

When Cam says “host it like the other project” or “use our Google login,” read
this catalog before searching another project's environment. This is the central
map of existing service setups and local access, not a whole-project template.

| Need | Recipe | Existing examples |
| --- | --- | --- |
| Static site, WASM, or small PHP backend | [DreamHost](services/dreamhost.md) | Escape Rooms, Ultima IV, Alain's book |
| Persistent Node server, WebSockets or workers | [Fly.io](services/fly.md) | RoboRally Web, Storybook |
| Domains, DNS, verification records | [Cloudflare](services/cloudflare.md) | `copper-dog.com` subdomains |
| Google identity or Google API authorization | [Google Auth](services/google-auth.md) | Ultima IV identity; Storybook OAuth |

## Local credentials

The actual copies live at
`/Users/cam/Documents/Projects/conductor/.private/service-credentials.json`.
The directory is Git-ignored and mode `0700`; the file is mode `0600`.
It is local plaintext protected by filesystem permissions, **not encrypted**,
not an off-host backup, and not included when Conductor is cloned. Other agents
on this Mac can use it through the helper. Another host needs a separate secure
transfer/provisioning step. Do not paste the vault or its contents into chat,
logs, documentation, commits, prompts to remote services, or a new repository.

List profile names, variable names, provenance, scope and copy dates safely:

```bash
cd /Users/cam/Documents/Projects/conductor
python3 scripts/service_credentials.py list
```

[Inventory](services/inventory.json) records the initial copy's metadata.
The helper's live list is authoritative for local availability. Copies were
checked against their source values on 2026-10-28; provider validity, permissions,
OAuth registrations and expiry were **not** tested. Source files were unchanged.
Profiles are intentionally separate even where credentials might be identical.

Available initial profiles: three DreamHost SFTP profiles, four Google OAuth
profiles, and one Fly CLI session profile. No Cloudflare API token was found in
the bounded local environment/config search. No API-provider eval keys,
databases, application session secrets, user OAuth grants/refresh tokens,
SSH private keys, browser cookies or backup environments were copied.

## Use in a new project

1. Choose a recipe that matches the runtime. Identify the destination app,
   domain, service account, persistent data needs and authentication flow.
2. Inspect metadata and choose one relevant profile. A copied credential does
   not establish its resource scope or current validity. Confirm the intended
   account/resource with a bounded read-only check before making changes.
3. Prefer a dedicated credential for the new app where supported. Reuse the
   existing account/organization; choose an app/zone-specific token, site webroot
   or OAuth client as appropriate. Existing deployment paths and client callbacks
   are examples, not defaults for a new project.
4. For selected access, first add a private JSON destination to the target repo's
   ignore rules, then export **only** the needed keys to a new file:

   ```bash
   python3 /Users/cam/Documents/Projects/conductor/scripts/service_credentials.py \
     export-json dreamhost-onward \
     --key DREAMHOST_SFTP_HOST --key DREAMHOST_SFTP_USERNAME \
     --key DREAMHOST_SFTP_PASSWORD \
     --target /absolute/target-repo/.service-credentials.json
   ```

   The helper refuses tracked, non-ignored, existing and symlink destinations.
   It creates a `0600` JSON file. Load it with a JSON parser into the deployment
   process environment; never `source`/`eval` it. For example, in a local wrapper:

   ```python
   import json, os, subprocess
   from pathlib import Path
   selected = json.loads(Path(".service-credentials.json").read_text())
   env = {**os.environ, **selected}
   # Add this NEW site's reviewed webroot; never copy a previous site's target.
   env["DREAMHOST_SITE_PATH"] = "/home/REVIEWED_USER/NEW_DOMAIN"
   subprocess.run(["python3", "scripts/deploy_static_site.py", "--help"],
                  env=env, check=True)
   ```

   Replace `--help` with the owning deployer's reviewed plan/dry-run arguments
   first. Do not run a command that prints the environment or credentials. Keep
   secrets server-side and out of static build output. This catalog does not
   authorize a deployment or account change by itself.
5. Record the chosen service, public resource identities, callback URLs, secret
   names and deployment/rollback procedure in the new project's own runbook.
   Keep its application secrets and data project-owned.

## Import or refresh selected access

The helper accepts explicit allowlisted variables, never a whole environment:

```bash
python3 scripts/service_credentials.py import-env cloudflare-new-zone \
  --service cloudflare --source /private/path/selected.env \
  --key CLOUDFLARE_API_TOKEN --scope 'DNS edit for the named new zone only'
```

Use a new versioned profile name for refresh; existing profiles are not
overwritten. Values are parsed as single-line literals without execution or
variable expansion. Unsupported/multiline values fail closed; no values appear
in helper output. Do not pass a secret as a CLI argument. If a token expires,
rotate through the provider and import the replacement; updating a source file
does not automatically refresh this copy or any exported files. Revoke unused
provider credentials separately from deleting local copies.

## Evidence and coverage

This setup used read-only inspection of current local project runbooks/configs,
selected `.env` assignments and the local Fly CLI config. Project environment
discovery covered `/Users/cam/Documents/Projects` to four directory levels,
excluding generated/dependency directories, examples and backup imports. It was
not a scan of remote hosts, Git history, CI secrets, every worktree or every disk.
Cloudflare and Fly account state were not changed. Local parser/permission/export
tests are in `tests/test_service_credentials.py`; recorded checks are in
[validation](services/validation.md). Future setup should recheck provider docs
and local scope before reuse.
