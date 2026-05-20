# Runbook: Setup Methodology

Conductor uses a lean methodology package:

- `docs/ideal.md`
- `docs/spec.md`
- `docs/methodology/state.yaml`
- `projects.yaml`
- `docs/methodology/graph.json`
- `docs/stories.md`
- `docs/scout.md`
- `docs/align-projects.md`
- `AGENTS.md`

Use `/setup-methodology` when the project structure or public surfaces drift.

## Greenfield checklist

1. Create the ideal and spec
2. Create the state file and project registry
3. Install inbox, scout, and alignment logs
4. Install story surfaces and compile the graph
5. Install AGENTS and the local skill surface
6. Run:
   - `make methodology-compile`
   - `make methodology-check`
   - `make skills-sync`
   - `make skills-check`

## Shared Product-Repo Setup Rule

Conductor is not the canonical copy of every product skill, but the tracked
product repos should keep the portable `/setup-methodology` skill identical.
When the product setup package changes, upgrade one product worktree, then copy
the exact skill file into the other product repos and refresh canonical
`.agents/skills` compatibility links.

The product setup skill must be sparse-safe for repos with no code yet:

- require real `docs/ideal.md` and `docs/spec.md` from `/init-project` or
  equivalent intake before setup fabricates package surfaces
- install upgraded `/triage`, packet-mode triage leaves, `/triage-health`, and
  `/loop-verify`
- mark code-dependent lanes as absent or deferred instead of treating missing
  UI scouts, eval attempts, architecture audits, or codebase reports as broken
- run cheap validation and skill-surface checks rather than long subagent loops
  over evidence that cannot exist yet

## Local Runtime Allocation

When a tracked repo has a local browser UI, API, internal authoring server, or
other human/AI runtime, setup should install a repo-local launcher that reads
Conductor's `local-dev-ports.json` allocation. Repos should not invent their
own port ranges.

Runtime launchers should:

- keep primary-checkout ports stable for human bookmarks and OAuth-style flows
- assign worktree slots by absolute path in `~/.codex/local-dev-ports.json`
- derive all worktree ports inside the project's assigned Conductor ranges
- use strict port binding so collisions fail loudly
- report status with project, checkout root, slot, ports, owning PIDs, and
  health
- stop only same-checkout services by default

Repos without a local runtime should still mention their reserved range in the
README and defer launcher implementation until a real service exists.

## Codex Worktree Bootstrap

Codex environment setup is a dependency bootstrap, not a server launcher. When a
tracked repo needs local packages before validation or Run actions work,
`.codex/environments/environment.toml` should point `[setup].script` at one
repo-owned command such as `./scripts/codex-setup`.

Setup hooks should:

- keep package-manager logic in the repo script rather than long TOML commands
- use lockfile-respecting installs such as `npm ci`, `pnpm install
  --frozen-lockfile`, or `uv sync --locked`
- restore ignored dependency artifacts such as `node_modules`, `.venv`, or
  `.runtime`
- avoid changing source files, lockfiles, generated methodology outputs, or
  user data
- avoid starting local servers; Run/status actions own runtime launch
- verify `.codex/environments/environment.toml` is visible to git, or add a
  narrow unignore rule when the repo ignores `.codex/`

Repos without local dependency needs can keep setup check-only or explicitly
defer the hook until a real validation/runtime surface exists.
