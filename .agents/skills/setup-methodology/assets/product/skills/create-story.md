---
name: create-story
description: Create a product story when a distinct outcome needs ownership, acceptance criteria, and proof
user-invocable: true
---

# /create-story [title]

Create one coherent product story only when the work needs a durable execution
home. Read `AGENTS.md`, the relevant Ideal/Spec, state/graph, decisions, inbox,
and existing stories before choosing a boundary.

## Decide whether a story is warranted

- Continue or reopen an existing line when it owns the same outcome and proof.
- Use a small direct action for an obvious, indivisible change that does not
  need lifecycle tracking.
- Route unresolved technical research to the project's research/eval surface,
  or a hard-to-reverse choice to an ADR, before promising implementation.
- Keep one story around a coherent outcome and validation boundary. Split only
  for distinct ownership, runtime seams, risks, or independently useful proof.
- Use bounded evidence gathering or ideation only when it resolves real
  uncertainty; the main thread chooses whether a story is warranted and owns it.

## Create and complete

1. Check story numbering and search for overlap. Use the installed
   `.agents/skills/create-story/scripts/start-story.sh` helper when available;
   inspect its output path before editing. If absent, follow local conventions
   without overwriting an existing file.
2. Write a concise goal, user-visible outcome, acceptance criteria, explicit
   out-of-scope boundary, tasks, dependencies, relevant Ideal/Spec/decision
   references, and proof/verification expectations.
3. Use the repository's supported status and priority vocabulary. The installed
   story template starts at `Draft`; preserve that unless substrate and local
   rules justify another status. Never make uncertain work build-ready by
   default.
4. Regenerate generated indexes/graphs with the documented local command and
   confirm the story appears in the expected writable/generated surfaces.

The story must retain its workflow gates: build complete; validation complete
or explicitly skipped by the user where allowed; and marked done through
`/mark-story-done`. Do not treat a drafted story as implementation approval.

Do not infer acceptance from the existence of a story. Report the created path,
why this boundary is durable, and the next appropriate action. Do not commit or
push unless asked.
