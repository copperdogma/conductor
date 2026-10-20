---
name: triage
description: Prioritize product work from local intent, constraints, evidence, and available project lanes
user-invocable: true
---

# /triage [stories|inbox|evals|health] [sub-arg]

Use this product variant in a product repository. Read-only triage finds the
highest-leverage next move; it does not build a portfolio recommendation.

## Shared frame

1. Read the repo's `AGENTS.md`, Ideal, Spec, methodology state/graph, and
   relevant decisions. Follow local source ownership and privacy rules.
2. Read current facts from a documented local facts/status command when one
   exists. Treat command errors as unknown evidence, never as empty lanes.
3. Inspect the inbox, authored stories, eval records, and recent work only as
   needed to establish what is live, blocked, redundant, or changed.
4. Compare candidates by user/product impact, Ideal/Spec fit, evidence,
   actionability, dependencies, continuity, and cost of waiting. Activity or
   backlog age alone does not establish priority.

## Routing and packets

- A scoped lane hands off to the matching installed leaf skill. If absent,
  explain that and return the best direct next step without fabricating a lane.
- Full triage may request up to three neutral packets from available story,
  inbox, eval, or health lanes. Include architecture or UI only when installed,
  supported by real project surfaces, and relevant to the current decision.
- Delegate bounded read-only evidence gathering only when allowed, useful, and
  safe for the checkout; otherwise gather sequentially. Packets report facts,
  alternatives, stop conditions, blockers, and reasons not now. They do not rank
  the project or decide the final action.
- Optional lanes marked absent or deferred create no maintenance pressure.
  Do not run evaluations, audits, fixes, or write artifacts during full triage.

## Output

Return the top three actionable candidates at most, then one recommendation:

```markdown
## Product Triage
- Primary gap and Ideal/Spec fit: ...
- Recommended next action and why now: ...
- Evidence and uncertainty: ...
- Runner-ups: ...
- Absent/deferred lanes: ...
- Stop condition or human decision: ...
- Boundary: Go after yes | Needs human judgment | Blocked — ...
```

End with one concrete yes-ready next step. A bare yes authorizes only that
bounded step, not deployment, account changes, provider spend, or commits unless
the recommendation names them and the user has authorized them.
