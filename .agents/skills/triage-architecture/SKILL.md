---
name: triage-architecture
description: Review an architecture area against current product needs and recommend a bounded decision or audit next step
user-invocable: true
---

# /triage-architecture [area]

Read-only architecture triage. Use it when architecture has become a real
decision or risk, not as a recurring demand to create architecture records.

## Steps

1. Read `AGENTS.md`, the relevant Ideal/Spec, methodology state/graph when
   present, and applicable decision records.
2. If the repo defines architecture audit cadence or domain state, inspect it.
   If it does not, do not invent a schedule or state schema.
3. Inspect only enough implementation and evidence to answer whether the area
   is causing a user, reliability, security, delivery, or changeability problem.
4. Separate observed behavior from inference. Consider the simplest viable
   alternatives and existing constraints; do not prescribe a stack by habit.
5. Recommend a bounded next step: continue an accepted decision, gather
   evidence, prepare an ADR, defer, or no-op. Leave the choice to the owner when
   it depends on product values or an unresolved tradeoff.
6. Prefer a small, discriminating investigation over broad architecture
   inventory. Name the assumption that result would confirm or reject.

## Full-triage packet mode

When `/triage` requests a packet, return up to three neutral architecture
candidates with evidence, product value, why now, next action, stop condition,
blockers, and reasons not now. Do not choose a lane winner, write a kickoff, or
make the overall project recommendation. Direct invocation may recommend one
first move.

## Output

```markdown
## Architecture Triage
- Area and reason reviewed: ...
- Current evidence: ...
- Constraints or prior decisions: ...
- Options or unresolved question: ...
- Recommended next step: ...
- Absent/deferred audit capability: ...
```

Do not edit architecture, state, or decisions in this skill. Do not infer that
an optional audit lane is overdue merely because no audit metadata exists.
