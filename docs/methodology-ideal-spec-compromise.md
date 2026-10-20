# The Ideal-First Methodology for Conductor

Conductor uses the same high-level methodology shape as the other projects, but
its subject is cross-project coordination rather than a product runtime.

Conductor also owns the canonical reusable skills and methodology package.
Projects adopt relevant guidance while retaining their product contracts,
harnesses, evidence, and justified adaptations. Model evaluations and skill
checks serve project improvement. See
[ADR-004](decisions/adr-004-canonical-skills-and-methodology.md).

## Artifact stack

1. `docs/ideal.md` — what the supervisor project should be with no unnecessary friction
2. `docs/spec.md` — the current operating constraints and workflow rules
3. `docs/methodology/state.yaml` — mutable planning truth for Conductor itself
4. `projects.yaml` — machine-readable registry of tracked projects
5. `docs/methodology/graph.json` — compiled story and surface index
6. `docs/stories.md` — generated backlog view
7. `docs/scout.md` / `docs/scout/` — external research memory
8. `docs/align-projects.md` / `docs/alignments/` — internal cross-project drift memory
9. `docs/decisions/` — hard-to-reverse workflow choices

## Core idea

The Ideal describes what cross-project coordination should feel like if AI made
it cheap:

- notes captured once
- drift investigated quickly
- external research reused across projects
- local variation preserved when useful

The Spec records what structure still exists because the ideal is not yet free:

- an inbox instead of perfect memory
- scout logs instead of instant retained insight
- alignment logs instead of effortless cross-project understanding
- stories and ADRs instead of fully self-justifying transient reasoning

## Ideal authoring boundary

The Ideal answers **what should be true for the user if technical capability
were no obstacle?** It is a concise north star with **zero implementation**.
Aim for one readable page, usually 200–500 words or fewer when sufficient.
Preserve distinct desired outcomes; keep detailed intake in its source.

Both product and execution ideals describe experiences and outcomes. Neither
prescribes architecture, technologies, file layouts, agent procedures, or proof steps.
User-valued properties such as privacy and fidelity belong here; mechanisms,
current limitations, compromises, delivery phases, and operating rules belong in
the Spec, ADRs, AGENTS/runbooks, stories, or evals. For each sentence ask whether
it would survive a completely different implementation delivering the same
experience. The kickoff skill and runbook supply the authoring contract and
examples; setup preflight checks this boundary even for an existing Ideal.

## Operating rule

Planning starts from:

- `docs/ideal.md`
- `docs/spec.md`
- `docs/methodology/state.yaml`
- `docs/methodology/graph.json`
- `projects.yaml`

Execution starts from the active story or specialized lane, but Conductor still
uses the graph/state layer to decide whether work belongs to alignment,
scouting, routing, or memory upkeep.

