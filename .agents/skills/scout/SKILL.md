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

## Source handling

Before doing generic web reading, choose the narrowest honest retrieval path for
the source:

- X/Twitter URL, tweet ID, or account: use `Twitter Scraper`
- YouTube URL: use `YouTube Transcripts` for transcript and video info
- Obsidian project-doc or note reference: use `Project Agent`
- everything else: use the normal web/document-reading path

## Steps

1. Pull the source through the best matching connector when one applies.
2. Read the source carefully enough to understand the real offering.
3. Compare it against:
   - `docs/ideal.md`
   - `docs/spec.md`
   - `projects.yaml`
   - recent scout memory in `docs/scout.md`
4. Decide per tracked project:
   - relevant or not
   - likely leverage
   - adopt, adapt, defer, reject, or spike
5. Decide the landing path after the scout:
   - `Reject` -> keep it in Conductor scout memory only
   - `Defer` with no clear owning repo -> keep it in Conductor scout memory only
   - `Defer` or `Spike` with a clear owning repo -> append a concise note to
     that repo's `docs/inbox.md` so the repo can triage it when the time is
     right
   - `Adopt` or `Adapt` with a concrete next implementation step -> create or
     recommend the target repo story instead of leaving it as ambient future
     pressure
   - cross-project methodology implications -> route back into Conductor
     alignment or story-prep rather than a single target repo inbox
6. Write or update the scout entry under `docs/scout/`.
7. Update `docs/scout.md`.
8. If warranted, recommend or create follow-up stories.

## Output shape

- summary of the source
- project-by-project relevance
- recommended next actions
- confidence and open questions

## Guardrails

- Do not treat "interesting" as "worth doing."
- Distinguish universal ideas from project-specific ones.
- Record a decision, not just notes.
- Prefer source-specific connectors over generic browsing when they exist for
  the source type.
- If a connector fails, say so explicitly and use the next honest fallback.
- Do not let Conductor accumulate repo-specific "maybe later" pressure forever.
  If a future idea clearly belongs to one tracked repo, hand it off to that
  repo's `docs/inbox.md` unless the work is already concrete enough for a
  target-repo story.
