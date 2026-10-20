---
name: triage-health
description: Find the most consequential current health risks in a product repository and return a read-only evidence packet
user-invocable: true
---

# /triage-health [scan]

Use this skill to identify operational or process risks that could undermine
the product, its evidence, or its ability to change safely. It recommends work;
it does not perform repairs.

## Read

1. Read the repository's `AGENTS.md` and identify its declared sources of truth.
2. Read the relevant Ideal, Spec, and methodology state/graph when present.
3. Inspect current status and existing evidence before proposing a new check.
   Use a repo-provided facts/status command only if `AGENTS.md` documents one.
4. Check only health lanes that have an actual source in this repository, such
   as incidents, evaluation health, architecture audits, security or dependency
   findings, user-facing quality reviews, or codebase scans.

## Decide

- Prefer observed user impact, data loss, reliability, security, or evidence
  integrity risks over cosmetic process gaps.
- Rank candidates by severity, likelihood, reach, evidence strength, and the
  smallest useful next action. State uncertainty and missing evidence.
- Do not infer a failure from an absent optional lane. Mark lanes absent,
  deferred, or not evidenced; do not recommend creating them just to fill a list.
- Reuse current applicable findings. Do not rerun expensive, destructive, or
  externally connected checks as part of triage.
- Keep the packet neutral: describe evidence and options, then recommend at most
  one first move. Do not silently change state or create work items.

## Full-triage packet mode

When `/triage` requests a packet, return up to three neutral health candidates
with evidence, product value, why now, next action, stop condition, blockers,
and reasons not now. Do not choose a lane winner, write a kickoff, or make the
overall project recommendation. Direct invocation may recommend one first move.

## Output

Return a concise report:

```markdown
## Health Triage
- Scope and sources inspected: ...
- Highest-risk candidates: ...
- Absent or deferred lanes: ...
- Recommended first action: ...
- Why now and evidence: ...
- Stop condition or missing decision: ...
```

If no material risk is supported, say so and name the most relevant sources
checked. Keep the next action specific enough for the owner to accept or decline.
