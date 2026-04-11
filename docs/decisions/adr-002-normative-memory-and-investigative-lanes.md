# ADR-002 — Normative Memory and Investigative Lanes Stay Separate

## Status

Accepted

## Context

Conductor already has two different kinds of durable artifacts, but the
distinction has been implicit rather than named.

Normative artifacts define what a project is trying to be and what it has
decided:

- `docs/ideal.md`
- `docs/spec.md`
- `docs/decisions/`
- `docs/stories/`

Investigative artifacts record what an agent or operator learned by examining a
bounded target through a specific lens:

- `docs/scout.md` + `docs/scout/`
- `docs/align-projects.md` + `docs/alignments/`
- repo-local lanes such as `ui-scout`, architecture audits, or eval review

The repeated pattern is:

1. investigate a bounded target through one lens
2. document evidence and the current judgment
3. propose the smallest honest next action
4. route that action to the right artifact
5. leave durable memory so the next pass does not restart from zero

This is useful across creation and review work. A scout can prepare creation
work. A UI or architecture audit can review existing work. The important split
is not "build" versus "review"; it is normative memory versus investigative
memory.

Without that distinction, new lanes risk being handled inconsistently:

- useful investigative loops look ad hoc and easy to forget
- lane-specific outputs get flattened into vague "review" work
- state graphs and triage can accumulate fake pressure for lanes that are not
  solving any real repeated problem yet

## Decision

Conductor will treat bounded, repeatable investigate -> document -> propose ->
route loops as first-class **investigative lanes**.

Each investigative lane must define:

- its trigger condition
- its memory surface
- its lane-specific decision/output shape
- its routing rule for follow-up work

Investigative lanes are intentionally distinct from normative artifacts.
Investigative work may recommend stories, ADRs, alignments, or repo-local
changes, but it does not become a requirement just because the lane exists.

Conductor will use these rules:

- Keep normative memory in ideals, specs, ADRs, and stories.
- Keep investigative memory in lane-specific logs and records.
- Reuse the shared workflow skeleton across lanes, but do not force identical
  result taxonomies. A scout, eval, UI audit, and security audit answer
  different questions and should keep lane-specific output contracts.
- Only promote a lane into shared methodology defaults, state-graph pressure,
  setup surfaces, or recurring triage expectations when it is solving a real,
  repeated problem.
- New lanes may be incubated in Conductor first as portable skills or
  supervisor memory before any cross-project sync is attempted.

First application of this decision:

- `/security-audit` is an optional investigative skill incubated in Conductor.
- It is not a default triage lane, not a required state-graph category, and not
  a mandatory setup-methodology module until real recurring security-review
  pressure exists.

## Consequences

- Conductor can intentionally grow reusable investigative lanes without
  pretending every lane is a live portfolio-wide concern.
- Scout, alignment, UI review, architecture review, eval review, and future
  security review can share a common operating pattern while preserving
  different decision outputs.
- State and graph surfaces stay lighter because they only absorb lanes that
  have proven recurring value.
- Portable review skills can be designed in Conductor, tested on real repos,
  and only then promoted into shared methodology or setup flows.
