# ADR-001 — Conductor Is a Supervisor, Not a Canonical Core

## Status

Accepted

## Context

The tracked projects share a large AI methodology and skill surface, but those
surfaces are intentionally adapted locally. The problem to solve is recurring
busywork around comparison, scouting, and distribution of useful changes.

A traditional "shared core" or canonical master copy would force uniformity
where local adaptation is often correct. It would also add overhead that this
project is explicitly trying to reduce.

## Decision

Conductor will operate as a recommendation-first supervisor project.

It will:

- track the active projects and their comparison surfaces
- compare those distributed surfaces when asked
- recommend what should sync and what should remain local
- preserve memory for scouting and alignment work
- prepare stories, ADRs, or notes for the target projects

It will not:

- become the canonical source of all skills
- force exact textual identity across projects
- treat every difference as drift

## Consequences

- Alignment work focuses on meaning and intent, not exact file sameness
- Project-specific adaptations stay owned by the target projects
- Conductor can stay lightweight while still reducing repeated comparison work

