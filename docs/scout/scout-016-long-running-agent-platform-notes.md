# Scout 016 — Evaluate Long-Running Agent Platform Notes for Portable Infrastructure Ideas

**Source**: multiple inbox items
**Status**: Defer
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

This bundle does not resolve to one clear "adopt a long-running agent platform"
decision. It breaks into three different shapes:

- a hosted long-horizon service with durable session, harness, and sandbox
  interfaces (`Anthropic Managed Agents`)
- build-it-yourself orchestration guidance and frameworks (`OpenAI practical
  guide`, `Google ADK`, `OpenAI Swarm`)
- low-signal note drift (`OpenAIDevs` PDF-RAG tweet, vague `II-Agent`
  benchmark note)

That matters because the tracked repos already carry the strongest portable
ideas from this bundle in local forms:

- Storybook already commits to fire-and-forget async now, a queue escalation
  path later, session-scoped working memory, and explicit deferral of richer
  worker-mesh orchestration until evals prove it necessary.
- CineForge already has a centralized long-running action system and explicit
  runtime/UI feedback rules for work that takes time.
- doc-web already treats durable pipeline runs and partial resume as first-class
  workflow concerns through `driver.py` and run metadata.
- Dossier's current pressure is still bounded extraction/eval orchestration,
  not multi-hour autonomous execution infrastructure.

So the external sources are useful design-reference material, but they do not
justify a new shared substrate, a framework import, or a repo story right now.

## Project Relevance

- **dossier**: `Reject`. The portable value here is mostly generic advice about
  evals, tool boundaries, and orchestration discipline that Dossier already
  carries locally. It does not have a real managed-agent substrate gap today.
- **storybook**: `Defer`. This is the clearest conceptual fit, but current
  Storybook spec already encodes the honest posture: thin async lanes now,
  queue escalation when scale proves it, and no richer worker mesh until evals
  show it is worth the added complexity.
- **doc-web**: `Defer`. Durable runs, pipeline metadata, and partial resume are
  directionally aligned with the source bundle, but they already belong to
  doc-web's driver-first pipeline architecture. Nothing here justifies a pivot
  to an external agent platform.
- **cine-forge**: `Defer`. Anthropic's separation of durable session,
  stateless harness, and execution environment is relevant in principle for
  future long external media jobs, but CineForge already has the stronger
  immediate truth: consistent operator-visible feedback for long-running work.

## Recommendation

- Keep this at `Defer`.
- Do **not** create a Conductor story or a target-repo story from this scout
  alone.
- Do **not** create a target-repo inbox handoff yet. The ideas are still too
  broad and too mixed to deserve new ambient pressure in Storybook or
  CineForge.
- Treat Anthropic Managed Agents as the strongest architecture reference in the
  bundle:
  1. durable event/session log outside the harness
  2. explicit separation between orchestration layer and execution environment
  3. credentials kept out of the sandbox itself
- Treat OpenAI's practical guide as confirmation of an existing local bias, not
  as a new direction:
  1. start with a single agent where possible
  2. use evals before premature architecture growth
  3. add multi-agent orchestration only when tool and workflow complexity
     really demand it
- Treat Google ADK as a credible code-first framework reference, not a
  portfolio substrate recommendation. It is broad, capable, and model/deploy
  agnostic, but it would add another framework layer the tracked repos do not
  currently need.
- Treat Swarm as educational reference material only. Its own README positions
  it that way, and its stateless handoff model is better for learning patterns
  than for selecting a production long-running substrate here.
- If this bundle becomes concrete later, reopen it under the owning repo rather
  than as a cross-project sync line:
  1. Storybook if a real multi-hour Luna/background-agent lane appears
  2. CineForge if external media jobs outgrow the current run-tracking/runtime
     model
  3. doc-web only if durable remote execution becomes a bottleneck that
     `driver.py` and partial resume can no longer absorb

## Confidence

- Medium-high. The judgment is grounded in primary vendor sources plus current
  Storybook, CineForge, and doc-web architecture surfaces. I did not run any of
  the hosted or framework systems directly.

## Evidence

- `https://www.anthropic.com/engineering/managed-agents`
- `https://x.com/openaidevs/status/2021725246244671606?s=12&t=uFZE-MuhgWdh1YErEZzLtQ`
- `https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf`
- `https://github.com/google/adk-docs`
- `https://github.com/openai/swarm`
- `https://x.com/OpenAIDevs/status/1900221731563798716`
- Inbox notes: `Google ADK`, `building agents update`, `Swarm framework`,
  `II-Agent benchmark`, and `Storybook fine-tuning-agent`
- Local overlap evidence:
  - `/Users/cam/Documents/Projects/Storybook/storybook/docs/spec.md`
  - `/Users/cam/Documents/Projects/Storybook/storybook/docs/decisions/adr-016-email-channel/adr.md`
  - `/Users/cam/Documents/Projects/cine-forge/docs/stories/story-101-long-running-action-system.md`
  - `/Users/cam/Documents/Projects/cine-forge/AGENTS.md`
  - `/Users/cam/Documents/Projects/doc-web/docs/spec.md`
  - `/Users/cam/Documents/Projects/doc-web/AGENTS.md`

## Open Questions

- If Storybook eventually needs a real multi-hour agent lane, should it extend
  its existing queue/session surfaces or split out a separate resumable-run
  service?
- If CineForge starts orchestrating many external media providers, does it need
  a durable run-event log separate from the current UI feedback substrate?
- Was the `II-Agent benchmark` note pointing at a real source with materially
  better long-horizon evaluation ideas, or was it just noisy inbox residue?
