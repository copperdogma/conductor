---
name: mark-story-done
description: Close a product story only after its completion gates and applicable evidence are satisfied
user-invocable: true
---

# /mark-story-done [story-id]

Close a validated product story. Read the story, its current implementation and
work log, the relevant methodology state/graph, and local completion rules.

## Verify before closing

1. Confirm the story's build gate is complete and each acceptance criterion has
   applicable evidence for the current candidate.
2. Confirm validation is complete, or was explicitly skipped by the user where
   local policy permits. Record what remains unverified; do not convert a skip
   into a pass.
3. Check mandatory repository gates and generated views that changed. Reuse
   unchanged evidence only when inputs and configuration still match.
4. Confirm there is no remaining implementation, evidence, or decision work
   hidden in the story. A follow-up story alone does not make this one done.
5. If completion changes a local constraint or state, update only the owning
   source of truth and its generated view as required. Do not widen closeout to
   unrelated cleanup.
6. Do not hold a bounded story open for unrelated future improvements or an
   optional lane that the project has explicitly deferred.

If any gate is unmet, leave the story open or recommend one honest disposition:
keep open, rescope, or blocked with a named blocker and unblock condition.

## Close

When all gates are met, update the story status and completion checklist using
the repository's conventions, append a concise evidence-based closeout note, and
regenerate/check methodology views if required. Verify the final story and
generated index agree.

Do not commit, push, publish, or close unrelated work. Report evidence paths,
residual limitations, and the user-visible result plainly.
