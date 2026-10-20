# Conditional runtime and dependency setup

This is a project adaptation recipe, not an installed or validated runtime.
Use it only when the target has a real web/API/service or dependency need.
No-code projects record absent/deferred with the trigger rather than acquiring
servers, packages, or fake readiness checks.

## Local runtimes

Read Conductor's `local-dev-ports.json` for an existing allocation. If the target
is not allocated, prepare a proposed allocation and resolve it before launch;
do not invent a port or mutate the registry during package installation.
Reuse the target's own launch/status/stop implementation if it meets the setup
skill's contract. Useful local source examples are `scripts/local-dev-ports.mjs`
and `scripts/local-service.mjs` in product repos where present; review their
current dependencies and product assumptions before adapting.

The project launcher must read its allocation, bind strictly, identify the
checkout in health/status, reuse only a healthy same-checkout service, refuse
another checkout's listener, stop only its own service, and persist a stable
worktree slot under `~/.codex/local-dev-ports.json`. Primary ports remain stable.
Test with a tiny project-local health endpoint and a deliberate occupied-port
case before describing the launcher as working. Follow project rules for
browser-visible verification. Documentation alone is not runtime proof.

## Dependencies and Codex setup

If validation or runtime tools need dependencies, use one idempotent repo-owned
setup command and point `.codex/environments/environment.toml` `[setup].script`
at it. Keep package-manager implementation in that command. Restore only ignored
dependency artifacts using the project's lockfile; do not mutate source,
lockfiles, generated methodology outputs or user data, or start a server.
Confirm that the environment file is tracked or explicitly intentionally local.
Verify on a fresh disposable worktree; no install command belongs in routine
triage. Framework/provider-specific commands need current official documentation
when those interface facts are at issue. The portable package itself needs only
Python 3 and Bash for its provided tooling.
