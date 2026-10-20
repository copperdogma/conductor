---
name: triage-stories
description: Rank product stories by user value, readiness, evidence, and continuity
user-invocable: true
---

# /triage-stories [story-id]

Read-only backlog triage for a product repository. Recommend work that closes
an important, actionable gap; do not treat story count as progress.

## Steps

1. Read `AGENTS.md`, the relevant Ideal/Spec, and methodology state/graph when
   present. Distinguish authored stories from generated indexes.
2. Read the generated story view if available, then inspect candidate story
   files, prerequisites, decision references, and recent evidence. Do not rank
   from titles or status labels alone.
3. Compare candidates on user impact and Ideal fit, evidence/readiness,
   dependencies and blockers, continuity with an active line, and whether a
   smaller direct action, research, evaluation, or decision is more honest.
4. If a requested story is blocked by missing substrate, name the evidence
   needed to make it actionable instead of recommending speculative build work.
5. Keep optional or deferred lanes from becoming artificial backlog pressure.

## Output

For direct use, return no more than three ranked candidates and one first move:

```markdown
## Story Triage
- Ranked candidates: {story, gap, evidence, recommended action}
- Bottlenecks or missing substrate: ...
- Recommended next action and why: ...
- Stop condition / human decision: ...
```

When called by full `/triage`, return a neutral packet with evidence,
actionability, stop condition, blockers, and reasons not now. Do not choose the
overall project priority in packet mode.

## Guardrails

- Keep a coherent active line when leverage is comparable; do not fragment work
  into micro-stories unless it isolates a real risk or proof boundary.
- Story IDs are identifiers, not priority. A pending status is not proof that
  prerequisites or implementation substrate exist.
- Do not edit stories, state, or indexes during triage.
