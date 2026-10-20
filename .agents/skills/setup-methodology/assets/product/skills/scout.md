---
name: scout
description: Research an external source for its value and applicability to one product repository
user-invocable: true
---

# /scout [source]

Investigate a source because it may answer a real product question. This is a
product-local research task, not a cross-project portfolio comparison.

## Research

1. Identify the source and decision question. Read the repository's
   `AGENTS.md`, relevant Ideal/Spec, decisions, and existing research first.
2. Use a matching source connector when available. For drift-prone technical
   claims, prefer current first-party documentation, release notes, or official
   repositories. Distinguish what the source says from local evidence.
3. Compare the source with product needs, constraints, privacy/reuse limits,
   existing implementation, and applicable evaluation evidence. Do not assume
   that novelty, capability, or benchmark results imply local value.
4. Classify the result: adopt, adapt, defer, reject, or run a bounded spike.
   Explain assumptions, uncertainty, tradeoffs, and what evidence would change
   the recommendation.
5. Record useful sources and findings in `docs/research/` or the repository's
   established research surface, preserving source scope and date. Update any
   local index if that surface requires one.

## Boundaries

- Research does not authorize installing code, changing dependencies or runtime
  defaults, making provider calls, or modifying external services.
- Do not copy completed implementations when local reuse restrictions prohibit
  it. Reuse general techniques only within the project's stated boundaries.
- If a source is inaccessible, say so and use a clearly identified fallback;
  never present secondary commentary as primary-source verification.
- Route concrete implementation work to an existing or new product story only
  when warranted. Do not write to Conductor's portfolio registry or inbox.

Return a concise source summary, local applicability, recommendation, evidence
and uncertainty, and one bounded next step.
