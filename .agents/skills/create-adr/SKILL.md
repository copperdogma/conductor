---
name: create-adr
description: Create a new Architecture Decision Record with lightweight research scaffolding. Use when a Conductor workflow, methodology, routing, or cross-project supervision choice is hard to reverse and deserves a durable decision record.
user-invocable: true
---

# /create-adr <number> <short-name> "<title>"

> Alignment check: Before choosing an approach, verify it aligns with
> `docs/ideal.md`, `docs/spec.md`, `docs/methodology/state.yaml`,
> `docs/methodology/graph.json`, `projects.yaml`, and relevant records in
> `docs/decisions/`. If none apply, say so explicitly.

Create a new Conductor ADR with flat-file scaffolding plus lightweight research
notes.

Use `/ideation` before decision closure when the ADR's considered options are
thin, all options are same-neighborhood variants, or the sticky choice needs a
stronger divergent option set. If the user has explicitly authorized
delegation, a bounded ideation subagent is a good fit for generating the option
packet. `/create-adr` still owns the decision, ADR text, and follow-up route.

Use `/triage-adr` on an existing ADR when the conversation has become unclear,
when it is not obvious what decisions remain, or when the ADR appears mature
but the next route is uncertain. `/triage-adr` inventories remaining
human-owned decisions, technical recommendations, evidence gaps, and alignment
work before `/create-adr` creates more decision surface or `/align-projects`
propagates the result.

## Example

```text
/create-adr 003 review-lanes "Review Lanes and Escalation Policy"
```

## Steps

1. Run the bootstrap script:

   ```bash
   .agents/skills/create-adr/scripts/start-adr.sh <number> <short-name> "<title>"
   ```

   This creates:
   - `docs/decisions/adr-NNN-<name>.md`
   - `docs/decisions/research/adr-NNN-<name>-research-prompt.md`
   - `docs/decisions/research/adr-NNN-<name>-final-synthesis.md`

2. Fill in the ADR file.
   - Replace all placeholders with real content.
   - Name the irreversible or sticky choice clearly.
   - State the supervisor context, decision, and consequences plainly.
   - Link the most relevant ideal/spec/state/decision references.
   - If the decision changes cross-project methodology expectations, say which
     lane would need follow-up: alignment, scout, setup, or story prep.

3. Fill in the research prompt.
   - Make the prompt stand alone.
   - Ask concrete questions that would change the decision, not generic
     background questions.

4. Show the created files for review.

5. Recommend the next honest follow-up.
   - keep local if the ADR is Conductor-only
   - `/triage-adr` if an existing ADR is ambiguous, stale, or nearly decided
   - `/align-projects` if the decision likely affects tracked repos
   - a story if the decision now needs implementation work

## Guardrails

- Never overwrite an existing ADR or research note.
- ADR numbers should stay sequential. Check existing `docs/decisions/adr-*`
  files before assigning a number.
- Keep Conductor ADRs lightweight. Use the flat file layout already present in
  `docs/decisions/`, not the directory-heavy ADR structure used in some product
  repos.
- Never commit or push without explicit user request.
