---
name: create-story
description: Create a new supervisor story when warranted
user-invocable: true
---

# /create-story [title]

Create a new story in `docs/stories/` when a new story is honestly warranted.

## Optional Sidecar Evidence

For non-trivial or cross-project story creation, the main thread may use
subagents or sidecar agents to gather bounded evidence before deciding whether
to bootstrap. Useful packets include codebase impact scans, recent story or
alignment lookup, source-specific research, and edge-case completeness checks.

- Sidecars are optional and evidence-only. They do not decide whether a story is
  warranted, choose the story boundary, set the initial status, or write the
  final story artifact.
- Do not default story creation to `/loop-verify`; reserve repeated verify
  loops for later validation or unusually broad/high-risk planning surfaces.
- If subagents are unavailable, unsafe for the checkout, or explicitly disabled
  by the user, run the same evidence checks sequentially and state that
  fallback in the handoff.

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
