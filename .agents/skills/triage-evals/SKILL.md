---
name: triage-evals
description: Audit existing evaluation evidence and recommend which product-quality question needs attention next
user-invocable: true
---

# /triage-evals [eval-id]

This is a read-only review of evaluation coverage and evidence. It does not run
evaluations, call providers, spend credits, or change defaults.

## Read

1. Read `AGENTS.md`, the Ideal and relevant Spec constraints.
2. Locate the repo's declared evaluation registry and inspect relevant result
   artifacts, fixtures, and prior attempts. Read methodology state/graph and
   decisions when they define the affected requirement or gate.
3. Identify the decision each evaluation is meant to inform and what counts as
   sufficient evidence. Distinguish a harness check from product-quality proof.

## Assess

- Prefer existing, applicable evidence. Mark it stale only when inputs,
  implementation, criteria, or environment have materially changed.
- Identify gaps in coverage, unclear thresholds, invalid or weak fixtures,
  unclassified mismatches, and redundant evaluations.
- Keep discovery/benchmark evidence separate from adoption or runtime proof.
  A model or tool result does not authorize a provider call or product change.
- Rank no more than three candidates by decision impact, evidence gap, and
  actionability. State when an absent eval lane is optional or deferred.
- Recommend the smallest next evidence step, including a no-op when the
  current ledger answers the decision. Do not execute it.

## Full-triage packet mode

When `/triage` requests a packet, return up to three neutral evaluation
candidates with evidence, product value, why now, next action, stop condition,
blockers, and reasons not now. Do not choose a lane winner, write a kickoff, or
make the overall project recommendation. Direct invocation may recommend one
first move.

## Output

```markdown
## Evaluation Triage
- Evidence sources inspected: ...
- Decision and current evidence: ...
- Top candidates: ...
- Missing/deferred coverage: ...
- Recommended next step and why: ...
```

Name the relevant evaluation and evidence paths when available. State whether
the recommendation needs fixture/criteria work, a fresh run, or owner judgment;
do not imply that any unrun evaluation passed.
