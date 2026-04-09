---
name: triage
description: Choose the highest-leverage next supervisor action
user-invocable: true
---

# /triage [stories|inbox] [sub-arg]

`/triage` is the top-level router for Conductor.

## Routing

- `/triage` — full-sweep read-only recommendation
- `/triage stories` — delegate to `/triage-stories`
- `/triage inbox` — delegate to `/triage-inbox`
- `/triage inbox scan` — delegate to `/triage-inbox scan`

## Full-sweep mode

Read:

- `docs/ideal.md`
- `docs/spec.md`
- `docs/methodology/state.yaml`
- `docs/methodology/graph.json`
- `projects.yaml`
- `inbox.md`
- `docs/scout.md`
- `docs/align-projects.md`

Then:

1. summarize the most important open inbox pressure
2. summarize the strongest active story line, if any
3. summarize whether scout or alignment memory suggests a neglected follow-up
4. recommend one next action that the user can approve with `yes`

## Output

```markdown
## Triage

### Recommended Action
- ...

### Why
- ...
- ...

### Runner-Ups
- ...
- ...

### Health Flags
- ...

### Decision
- Reply `yes` to proceed with: ...
```

## Guardrails

- Unscoped `/triage` is read-only.
- Recommend one next action, not a grab bag.
- Prefer continuing a coherent active line over creating needless new work.

