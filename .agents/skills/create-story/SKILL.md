---
name: create-story
description: Create a new supervisor story when warranted
user-invocable: true
---

# /create-story [title]

Create a new story in `docs/stories/` when a new story is honestly warranted.

## Steps

1. Check whether the work should instead:
   - continue an active story
   - reopen a recent story
   - become a scout or alignment log first
2. If a new story is warranted, run:

```bash
.agents/skills/create-story/scripts/start-story.sh <slug> [priority]
```

3. Fill in:
   - goal
   - acceptance criteria
   - tasks
   - tracked projects
   - spec refs
   - decision refs
4. Run `make methodology-compile`.
5. Verify the new story appears in `docs/stories.md` and `docs/methodology/graph.json`.

## Guardrails

- Story ids are identifiers, not priority.
- Prefer one coherent story line over needless fragmentation.
- Do not create a story when the work is still too vague to score honestly.

