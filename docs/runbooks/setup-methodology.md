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

