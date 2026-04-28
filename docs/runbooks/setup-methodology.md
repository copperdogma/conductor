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
the exact skill file into the other product repos and regenerate wrappers.

The product setup skill must be sparse-safe for repos with no code yet:

- require real `docs/ideal.md` and `docs/spec.md` from `/init-project` or
  equivalent intake before setup fabricates package surfaces
- install upgraded `/triage`, packet-mode triage leaves, `/triage-health`, and
  `/loop-verify`
- mark code-dependent lanes as absent or deferred instead of treating missing
  UI scouts, eval attempts, architecture audits, or codebase reports as broken
- run cheap validation and wrapper checks rather than long subagent loops over
  evidence that cannot exist yet
