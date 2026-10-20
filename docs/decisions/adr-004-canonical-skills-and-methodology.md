# ADR-004 — Conductor Owns Canonical Reusable Skills and Methodology

## Status

Accepted — explicit owner clarification, 2026-10-17.
Partially supersedes [ADR-001](adr-001-conductor-as-supervisor-not-canonical-core.md).

## Context

Cam uses Conductor to improve other projects, assess their progress and skill
behavior, and roll out selected improvements. Model evaluation serves that
same goal. Cam also points new-project agents here to obtain useful skills and
methodology through kickoff and setup. The earlier denial of any canonical
source role conflicts with this responsibility.

## Decision

Conductor maintains the canonical reusable skills and methodology baseline.
Projects can select relevant guidance here rather than rediscover it.

Canonical means the best reviewed reusable baseline, not an assertion that
Conductor always has the latest or best version of every skill. Skills evolve
in projects. Review useful local improvements for promotion back into Conductor
when their value is generic, supported by local evidence, and not overfit.
Preserve the source, rationale, and applicability boundaries when promoting.

Projects retain their product requirements, harnesses, fixtures, evidence,
adoption decisions, and justified adaptations. Keep project-specific mechanisms
local. Source ownership neither forces textual uniformity nor authorizes a
rollout. Reusable skills can be copied exactly where they fit; local differences
need judgment, not automatic replacement.

New-project intake remains `/init-project`, followed by `/setup-methodology`
for the relevant package. Cross-project comparison, promotion recommendations,
and authorized adoption use `/align-projects` and target-repo isolation rules.

## Consequences

- Conductor must curate reusable guidance and learn from project experience,
  alongside supervision and model evaluation on projects' behalf.
- Agents must stop interpreting ADR-001 as a prohibition on canonical guidance.
- Canonical source changes and demonstrated target adoption remain separate.
- This decision changes ownership and guidance locally; it does not establish
  that every useful project-local skill has already been collected or tested
  for portability. Inventory and adoption remain evidence-bearing work.

## Alternatives

- Keep the supervisor-only boundary: rejected by Cam's stated use and intent.
- Make every project identical to one master: rejected; adaptation is useful
  and local evolution supplies improvements to the baseline.
- Maintain a reviewed reusable baseline with project-owned adaptations:
  selected by Cam.

## Alignment and follow-up

- Ideal: project improvement, reusable guidance for new projects, and I1–I5.
- Spec: `spec:2.1`; model evaluation remains governed by `spec:3.3` and ADR-003.
- State/graph: existing alignment, story-prep, and memory categories; no new
  runtime, eval lane, or recurring schedule is introduced.
- Local entrypoints and runbooks are updated with this decision. Further
  project adoption belongs to the alignment lane and needs its own scope.
- [Source and applicability notes](research/adr-004-canonical-skills-and-methodology-final-synthesis.md).
