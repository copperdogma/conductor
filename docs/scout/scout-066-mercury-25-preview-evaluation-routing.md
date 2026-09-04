# Scout 066 — Inception Mercury 2.5 Preview Evaluation Routing

**Source:** Inception first-party model and privacy pages plus OpenRouter model,
endpoint, reasoning, and privacy metadata; checked 2026-09-04.
**Status:** Do not adopt
**Stage:** Stage 2 owner campaign complete.
**Candidate:** `inception/mercury-2.5-preview`
**Projects reviewed:** conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Identity, access, economics, and privacy

Inception lists Mercury 2.5 Preview as its most intelligent reasoning dLLM,
with structured output, tool use, a 260K context window, and first-party list
pricing of US$0.20/M input, US$0.02/M cached input, and US$0.75/M output.
OpenRouter lists exact alias `inception/mercury-2.5-preview`, canonical checkpoint
`inception/mercury-2.5-preview-20260831`, a 65,536-token completion limit, and
one Inception endpoint. Both public and authenticated catalogs advertised low,
medium, high, and no-reasoning modes plus strict structured-output parameters.

OpenRouter's endpoint was temporarily priced at US$0.04/M input and US$0.15/M
output. The route did not document a zero-data-retention guarantee or collection
restriction, and Inception's privacy policy does not support treating arbitrary
private owner data as eligible. The campaign therefore used only checked-in,
repo-authored public/synthetic fixtures with `data_collection=allow` and made no
ZDR claim.

Official sources:

- <https://www.inceptionlabs.ai/models>
- <https://www.inceptionlabs.ai/privacy-policy>
- <https://openrouter.ai/inception/mercury-2.5-preview>
- <https://openrouter.ai/api/v1/models/inception/mercury-2.5-preview/endpoints>
- <https://openrouter.ai/docs/guides/best-practices/reasoning-tokens>

## Selected owner evaluation

Cam approved one bounded owner evaluation:

1. **Echo Forge — `scene-to-soundscape-golden`, US$0.10 ceiling.** Use the
   maintained public/synthetic Tavern fixture first. Require exact Inception-only
   strict transport, semantic `1/1`, at most 5 seconds, and at most US$0.01
   before advancing to Dungeon or a fresh incumbent.

## Stage 2 owner result

- **Execution surface:** isolated sparse worktree
  `/Users/cam/.codex/worktrees/mercury-25-echo-forge/echo-forge`, branch
  `codex/mercury-25-eval`, base
  `b15d2b7fd1b7d4f9ab0beb7991e7064290e02bc1`. Sparse checkout was required
  because the full repository's large audio library could not fit in the
  available local disk space.
- **Access and transport:** exact alias, canonical checkpoint catalog mapping,
  exact served provider `Inception`, terminal `stop`, provider-accepted strict
  JSON Schema, deterministic normalization, and version-3 provenance qualified.
- **Reliability and capability:** the one Tavern request was terminal-valid but
  failed the maintained semantic gate (`0/1`) on mood, default intensity, the
  explicit no-auto-tension constraint, two expected layers, and two Sound
  Actions. Full two-fixture capability is unmeasured.
- **Economics:** Tavern completed in **2,544 ms** and cost **US$0.00042627**
  from returned OpenRouter usage, clearing both dated operational gates. The
  spend was US$0.00042627 of the US$0.10 ceiling.
- **Decision:** **do not adopt** for Echo Forge's scene-outline lane. The
  progressive ladder stopped before Dungeon and the fresh incumbent because
  quality failed despite excellent speed and cost.
- **Owner evidence:** decision contract, attempt report, protected response,
  v3 fixture artifacts, registry, and generated methodology graph in the
  isolated Echo Forge worktree.

## Portfolio synthesis and retry condition

Mercury 2.5 Preview is a credible low-latency, low-cost strict-output transport,
but this dated low-reasoning arm did not preserve enough of Echo Forge's
table-control semantics. No private data was transmitted and no runtime default
or deployment changed. Temporary credential material was removed and verified
absent; the scoped owner evidence and this Conductor closeout were then checked
in without absorbing unrelated checkout work.

Do not repeat this unchanged arm. Re-evaluate only for a material Mercury
checkpoint, a newly supported reasoning/transport configuration that plausibly
addresses the semantic misses, or a source-backed owner contract change.
