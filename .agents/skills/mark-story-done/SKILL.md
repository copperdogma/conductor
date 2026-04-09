---
name: mark-story-done
description: Close a completed Conductor story safely
user-invocable: true
---

# /mark-story-done [story-number]

Close a validated Conductor story.

## Steps

1. Read the story.
2. Confirm:
   - `Build complete` is checked
   - `Validation complete or explicitly skipped by user` is checked
   - the remaining work is only close-out
3. If complete:
   - set status to `Done`
   - check `Story marked done via /mark-story-done`
   - append a close-out work-log entry with evidence
   - update `CHANGELOG.md` if needed
   - run `make methodology-compile`
4. If not complete:
   - recommend exactly one disposition: `Keep open`, `Rescope then close`, or `Mark blocked`

## Guardrails

- Never hide remaining implementation gaps.
- Never mark done without current-pass evidence.
- Do not treat the existence of a follow-up story as sufficient reason to close.

