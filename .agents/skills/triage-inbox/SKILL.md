---
name: triage-inbox
description: Review a product repository's raw inbox and recommend where live notes belong
user-invocable: true
---

# /triage-inbox [scan]

Route captured notes to the repository's existing source of truth. The inbox is
raw input, not automatically a backlog or a request to implement everything.

## Steps

1. Read `AGENTS.md`, the relevant Ideal/Spec, and the inbox path it declares.
   If there is no inbox, report that and stop; do not invent one.
2. Read the methodology state/graph, story index and candidate story files,
   relevant decisions, or other destinations named by local instructions.
3. Classify each item as live, partially handled, stale/duplicated, or needing
   clarification. Preserve its meaning and uncertainty.
4. Recommend its best destination: existing work, a new story, an ADR, a
   research/evaluation record, another named repo surface, or defer/reject.
5. Group items only when they express the same decision or investigation.

## Modes and boundaries

- `scan` is read-only: report candidates and proposed destinations without
  editing the inbox or creating artifacts.
- Ordinary triage is also proposal-first. Do not delete raw notes, silently
  rewrite capture, or create/modify destination artifacts unless the user
  explicitly asks for that processing in the current task.
- Do not turn a mention of a link, tool, model, or feature into authorization
  for external research, provider calls, or implementation.
- If the item depends on current external facts, name that dependency and route
  it to an appropriate research/evaluation step; do not guess.

## Full-triage packet mode

When `/triage` requests a packet, return up to three neutral inbox candidates
with evidence, product value, why now, next action, stop condition, blockers,
and reasons not now. Do not choose a lane winner, write a kickoff, or make the
overall project recommendation. Direct invocation may recommend one first move.

## Output

```markdown
## Inbox Triage
- Live items and proposed destinations: ...
- Already handled or stale: ...
- Clarification needed: ...
- Recommended next action: ...
```

Keep the report brief. Explain why the recommended destination fits the local
workflow and identify any unresolved human choice. Leave low-value capture
deferred instead of creating process to empty the inbox.
