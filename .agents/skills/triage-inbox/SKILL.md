---
name: triage-inbox
description: Scan or process inbox items into stories, scout missions, or alignment work
user-invocable: true
---

# /triage-inbox [scan]

Use this skill to process `inbox.md`.

## Modes

- processing mode: `/triage-inbox`
- scan mode: `/triage-inbox scan`

## Steps

1. Read `inbox.md`.
2. For each item, search:
   - `docs/stories/`
   - `docs/scout/`
   - `docs/alignments/`
   - `docs/decisions/`
3. Classify the item:
   - stale
   - live
   - partially handled
4. Recommend the right landing zone:
   - existing story
   - new story
   - scout mission
   - alignment pass
   - ADR
   - reject/defer

## Scan mode

Return a compact report only. Do not edit files.

## Processing mode

After user confirmation:

- create the right artifact
- remove or rewrite the processed inbox item
- keep the inbox short and current

## Guardrails

- `scan` is read-only.
- Raw links are allowed in the inbox, but they should not stay unresolved forever.
- Do not create a story when a scout or alignment pass is the more honest first move.

