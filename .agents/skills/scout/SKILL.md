---
name: scout
description: Investigate an external source and map its value across tracked projects
user-invocable: true
---

# /scout [source]

Use this for external links, repos, papers, whitepapers, threads, or tools.

## Inputs

- source or link
- optional focus question

## Steps

1. Read the source carefully enough to understand the real offering.
2. Compare it against:
   - `docs/ideal.md`
   - `docs/spec.md`
   - `projects.yaml`
   - recent scout memory in `docs/scout.md`
3. Decide per tracked project:
   - relevant or not
   - likely leverage
   - adopt, adapt, defer, reject, or spike
4. Write a scout entry under `docs/scout/`.
5. Update `docs/scout.md`.
6. If warranted, recommend or create follow-up stories.

## Output shape

- summary of the source
- project-by-project relevance
- recommended next actions
- confidence and open questions

## Guardrails

- Do not treat "interesting" as "worth doing."
- Distinguish universal ideas from project-specific ones.
- Record a decision, not just notes.

