---
name: triage-stories
description: Evaluate the Conductor story backlog and recommend what to work on next
user-invocable: true
---

# /triage-stories [story-number]

Read-only backlog triage.

## Steps

1. Read `docs/methodology/graph.json` and `docs/stories.md`.
2. Read candidate story files rather than relying on titles alone.
3. Score the candidate lines on:
   - leverage against recurring busywork
   - alignment with `docs/ideal.md`
   - readiness
   - continuity
   - whether the work is really a scout or alignment problem instead
4. Return one recommended next story action.

## Output

```markdown
## Triage Stories

### Ranked Problem Lines
- Story NNN — ... — recommended action: ...

### Bottlenecks / Concerns
- ...

### Recommended Action
- ...
```

## Guardrails

- Read-only.
- Prefer continuing the same line over fragmenting it into new stories.
- Do not recommend a build-ready story if its core substrate is still vague.

