# `/setup-methodology` modes

All modes begin after project-specific Ideal/spec intake. If those artifacts
are missing or generic, route through `/init-project`; do not fabricate them
from this checklist.

## `greenfield`

Use for a new or lightly scaffolded project after the owner has reviewed its
Ideal and initial Spec. Install the relevant package around those authored
truths. Add only evidence surfaces that the project can honestly exercise;
record why and when a root eval/golden is deferred.

## `retrofit`

Use when meaningful code, documentation, evidence, stories, or decisions
already exist. Inspect them first, preserve source and decision history, and
normalize only the needed package surfaces. Recover existing evidence before
creating new scaffolding.

## `adr-021-migration`

Use only when an existing project intentionally adopts the ADR-021
Ideal-first, category-aligned Spec, and state/graph structure. Read its
decision record and preserve local product contracts while migrating.

## `refresh`

Use when the project already has the methodology package and needs a bounded
sync or reference repair. Inspect current files and refresh only stale
instructions, links, checklists, or evidence guidance; do not redo intake or
recreate evidence without a changed decision need.

## Supervisor and sparse-project adaptation

For Conductor or another supervisor project, use the mode that describes the
repo state, then preserve its own routing/research evidence surfaces. Product
goldens and runtime evals are not implied by installing the shared package.
For a sparse product repo, keep its first proof surface small and mark
unrunnable evidence as deferred with a concrete trigger rather than inventing
sample passes or mandatory dashboards.
