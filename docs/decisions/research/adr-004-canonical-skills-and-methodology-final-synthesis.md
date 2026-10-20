# ADR-004 — Source and applicability notes

## Evidence and disposition

Cam explicitly clarified on 2026-10-17 that Conductor improves projects,
evaluates models on their behalf, and maintains canonical reusable skills and
methodology for new projects. Cam further clarified that project-local versions
will evolve: generic, non-overfit improvements should return to the maintained
baseline rather than every local difference being forced into uniformity.

Local inspection found conflicting current language in AGENTS, Spec `spec:2.1`,
the setup runbook, and ADR-001. Those surfaces are reconciled; ADR-001 is
partially superseded with its original reasoning retained. ADR-003 continues to
govern evaluation credential custody and project-owned benchmark evidence.

## Applicability and remaining uncertainty

This establishes ownership and source-selection behavior. It does not prove the
current package contains all reusable portfolio improvements, that every skill
is portable, or that downstream repos have adopted the changed guidance.
Promotion needs local evidence and an applicability review; downstream changes
need a scoped alignment pass. No upstream API facts or technical obstacle
required web research for this owner decision.

## Local validation

Use `make methodology-compile`, `make methodology-check`, `make skills-check`,
`make lint`, whitespace checks, and direct inspection of current source-role
claims. Product tests and provider calls are not relevant to this docs-only
ownership change.
