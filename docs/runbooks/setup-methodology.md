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

When creating or refreshing `AGENTS.md`, include a concise, portable research
rule: for nontrivial obstacles with an uncertain next step, inspect local
evidence, name the general problem class, reuse applicable prior research, or
check a few relevant primary sources before choosing a small local applicability
check. Record reusable sources, the decision, result, and uncertainty in
existing notes. Obvious fixes need no ceremony; preserve domain reuse limits
and acceptance criteria.

## Greenfield checklist

1. Run `/init-project` against the preserved seed, usually
   `docs/initial-concept.md`.
2. Discuss the kickoff brief with the user and get approval for a named setup
   plan.
3. Create real, project-specific `docs/ideal.md` and `docs/spec.md`; review
   them against the seed for coverage, contradictions, and late Ideal material.
4. Create the state file and project registry when the chosen package warrants
   them.
5. Install inbox, scout, and alignment logs when they fit the project shape.
6. Install story surfaces and compile the graph.
7. Install AGENTS and the local skill surface.
   - Include the research rule in `AGENTS.md` and adapt its reuse boundaries to
     the project.
   - For long-running work, wire optional `/loop-review` at existing strategic
     checkpoints where the approach merits periodic reconsideration. Ensure
     `/loop-verify` checks progress and repeated assumptions at round
     boundaries; for long active runs without a user cadence, add a checkpoint
     after about 30 active minutes or three substantive rounds, whichever comes
     first. Preserve cadence across interruptions, remain proactive when proxy
     metrics improve, reuse recent research only when it still applies, and
     keep research within existing budgets and hard stops. Do not add a
     scheduler or require these loops for routine work.
   - Add a short common staffing/wait policy, with dispatch details in
     `/loop-review`: dynamically resolve strongest eligible model and highest
     supported effort, record requested versus verified served identity, and
     use one bounded read-only reviewer only when needed. Preserve authority,
     budgets, deadlines and clean stops. Workers use the cheapest capable
     configuration when overhead is justified, bounded packets and artifacts,
     and native completion/message-aware waits. Keep child mailboxes distinct
     from human-authorized user-chat messaging and supported continuation.
   - Apply focused leaf changes only where needed; retain tiny-lane coverage,
     plan gates, evaluator subject/judge settings, actual spend gates and
     sparse/no-code exceptions. Existing delegation authorization is sufficient
     for the same bounded ideation/ADR packet; respect user opt-outs.

8. Run:
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

- require real `docs/ideal.md` and `docs/spec.md` from an interview-first
  `/init-project` or equivalent intake before setup creates package surfaces
- install upgraded `/triage`, packet-mode triage leaves, `/triage-health`, and
  `/loop-verify`
- install `/triage-adr` as the lightweight helper for existing ADRs whose
  remaining decisions, maturity, or next route are unclear
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
