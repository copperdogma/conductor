# Project operating guidance

Read `docs/ideal.md`, `docs/spec.md`, `docs/methodology/state.yaml`, and the
compiled `docs/methodology/graph.json` before planning. These are project-owned
truths; setup must preserve and review them. Implementation starts from the
active story and relevant spec/category slice.

The Ideal is a concise north star of desired outcomes unconstrained by today's
technical limits, with zero implementation. Current constraints, mechanisms,
delivery stages, operating procedures and proof contracts belong in their
owning Spec, ADR, runbook, story or eval. Product and execution ideals, when
both useful, describe experiences and outcomes only.

Use `/triage` for read-only prioritization; `/create-story`, `/build-story`,
`/validate`, and `/mark-story-done` for coherent story work. Optional evidence,
architecture, codebase and UI lanes apply only when installed and supported by
real project surfaces. See `.agents/skills/setup-methodology/references/product-workflow.md`.
Do not copy Conductor's project registry, portfolio inbox, or supervisor lanes
into this product. Preserve source provenance and justified adaptations;
consider generic local improvements for promotion back into Conductor.

For an unfamiliar material obstacle, diagnose locally, name the general problem
class, reuse applicable research or consult a few primary sources, then choose
a small local applicability check. Record reusable sources, result and
uncertainty in existing research notes. Obvious fixes need no research ceremony;
repeated failures call for reframing before more retries. Preserve acceptance
and project reuse restrictions. Verify drift-prone external interfaces with
current first-party docs before changing them.

Protect unrelated checkout work and private data. Use isolated worktrees for
Conductor-directed changes to existing projects. No implicit commit, push,
deployment, provider spend, or external account action. `/build-story` keeps
its plan approval gate; existing explicit authorization remains valid.

Package checks: `make methodology-compile`, `make methodology-check`,
`make skills-check`, `make facts`, `make package-check`.
These validate scaffolding, not product behavior. Add the project's real tests,
proof commands, privacy gates and runtime instructions as they become available.
The portable tooling needs Python 3 and Bash, no third-party Python packages.
