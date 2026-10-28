# DreamHost

Use for static HTML/assets/WASM and compatible PHP applications. Existing
shared hosting is not the recipe for a persistent Node/WebSocket server.

## Existing access and examples

Profiles: `dreamhost-onward`, `dreamhost-copper-dog-dnd`, `dreamhost-alain-book`.
Each holds only `DREAMHOST_SFTP_HOST`, `DREAMHOST_SFTP_USERNAME` and
`DREAMHOST_SFTP_PASSWORD`. Host and username are kept with the private access
bundle. Do not copy `DREAMHOST_SITE_PATH` or `DREAMHOST_DEPLOY_SOURCE_DIR` to a
new site: they select an existing site's destination/build output.

Working examples under `/Users/cam/Documents/Projects`:

- `alain-lessard-book/scripts/deploy_static_site.py`: existing Python/pexpect
  SFTP deployer, environment overrides, planning and manifest-aware publishing.
- `escape-rooms-calgary/docs/runbooks/deploy.md`: recoverable static publish,
  private staging, previous-root preservation and HTTP hash verification.
- `ultima-iv-web/docs/runbooks/browser-edition.md`: static/WASM publishing.
- `ultima-iv-web/docs/runbooks/account-saves.md` and `web/server/README.md`:
  PHP 8.3/PDO SQLite with config/data outside webroot and off-host backups.

Observed sites include `escape-rooms.copper-dog.com` and `u4.copper-dog.com`.
These are local documented configurations, not a fresh provider health check.

## New site recipe

1. Use the existing DreamHost account if its plan fits. Create/select the new
   domain's hosting entry, intended shell/SFTP user and **new** webroot. Confirm
   access and domain-specific assigned server/IP in the panel; do not reuse an
   old site's IP merely because it uses the same account.
2. At the authoritative DNS provider, add the required records. Existing
   Cloudflare examples use DNS-only records. Configure HTTPS with DreamHost and
   verify issuance before switching public traffic.
3. Build locally; use the owning project's maintained deployer after reviewing
   its dependencies, excludes, deletion behavior and plan. Preserve provider
   ACME entries. A staging/root rename pair has a brief non-atomic gap; inspect
   receipts before retrying a partial publish.
4. Keep private PHP releases/config/session files/databases outside frontend
   swaps and webroot. Plan backups/restore before publishing persistent state.
5. Verify HTTPS, expected content hashes and application behavior. Keep the
   previous root until the release is accepted; record rollback instructions.

No DreamHost API key was copied. SFTP access does not grant API/panel access.
For automated account operations, create a separate API key selecting only
needed commands in the panel; do not include the key in logged request URLs.
The API's command selection and key mechanism were checked against
[DreamHost's API guide](https://help.dreamhost.com/hc/en-us/articles/4407354972692-Connecting-to-the-DreamHost-API)
on 2026-10-28. Site publishing itself was not performed for this catalog.
