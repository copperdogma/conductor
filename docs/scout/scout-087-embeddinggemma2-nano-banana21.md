# Scout 087 — EmbeddingGemma 2 and Nano Banana 2.1

Date: 2026-10-06 (America/Edmonton)
Status: Research complete; user-selected CineForge direct adoption landed on main, embeddings deferred

## User-directed follow-through

Cam subsequently explicitly selected direct adoption without a quality comparison.
CineForge Story 230 in the isolated `scout087-cine-forge-20261006` worktree now
implements native NB2.1 image transport and storyboard/design-study/render-backfill
defaults, UI/readiness updates and reference caps. Backend unit 2256 passed before
a final grid-aspect fix; 65 affected tests passed after it, plus 10 integration
tests, UI tests/build/lint and desktop/mobile selector verification. Closure
revalidated 83 focused backend tests against current main. Story 230 is Done;
commit `d358224da24e0ca5a6774c92287d70cf69389864` is verified on remote main and
the task branch. No paid inference or deployment. Original recommendation below is retained
as research history, not a pending requirement or claim of model superiority.

## Decision

Prioritize a bounded CineForge Nano Banana 2.1 image-generation comparison.
Defer EmbeddingGemma 2 migration in Storybook; keep Echo Forge audio retrieval
as a future trigger. No paid inference, model installation, credential access,
runtime changes, commits or pushes occurred in this scout.

## Verified upstream offering

Primary sources checked on the date above:

- [Gemini release notes](https://ai.google.dev/gemini-api/docs/changelog): October 6 GA,
  exact stable model ID `gemini-nano-banana-2.1`. Public API documentation is
  confirmed; this account's access and actual returned model remain untested.
- [NB2.1 model card](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1):
  image generation/editing, 1K/2K/4K, claimed improved visual quality, typography,
  prompt following and multi-turn character consistency. Up to14 reference
  images, up to4 characters/10 objects; panoramic tiling fixes. These are vendor
  claims, not locally demonstrated fidelity. Thinking minimal/medium/high,
  default medium; no structured outputs. Text/image/video/PDF inputs do not
  make this an audio model or a replacement for the frame-understanding lane.
- [Image generation guide](https://ai.google.dev/gemini-api/docs/image-generation)
  and [GenerateContent guide](https://ai.google.dev/gemini-api/docs/generate-content/image-generation):
  native Gemini generation routes, distinct from Imagen predict. Search grounding
  and14 references existed in NB2; do not present them as new2.1 capabilities.
- [Pricing](https://ai.google.dev/gemini-api/docs/pricing): standard NB2.1 image
  output approximately USD0.0336/1K,0.0504/2K,0.113/4K, versus NB2
  0.067/0.101/0.151. Input USD1.50/million versus0.50, text/thinking output
  USD7.50/million versus3.00. Batch image output0.0168/0.0252/0.0567.
  Image-only savings are not total-task savings, especially with many references,
  medium thinking by default, retries or grounding. Recheck exact pixel/token
  accounting before reserving spend. Grounding may incur extra search charges.
- [Deprecations](https://ai.google.dev/gemini-api/docs/deprecations) lists NB2
  shutdown October29,2026, while the October6 changelog says no shutdown date
  announced. Official pages disagree; verify before claiming a firm deadline.
  CineForge inspected defaults are GPT Image2/Imagen, so no NB2 shutdown exposure
  was established here.
- [EmbeddingGemma docs](https://ai.google.dev/gemma/docs/embeddinggemma) and
  [developer guide](https://developers.googleblog.com/embeddinggemma-2-the-developer-guide/):
  `google/embeddinggemma-2`, Apache2.0 open weights, unified text/code/image/audio/video
  embeddings; modular270M text/code up to740M full model,8192-token text context,
  768 dimensions with128/256/512 truncation options. Distinct from hosted
  `gemini-embedding-2`. Similarity retrieval is not generative reasoning.
- [AI Edge guide](https://developers.googleblog.com/en/google-ai-edge-with-embeddinggemma-2/):
  reported approximately191MB text-only/567MB full active RAM on Pixel11Pro;
  device/runtime-specific figures, not measured on Cam's hardware. ML Kit
  integration is promised in coming weeks, not established shipped support.

## Local fit and evidence

Read-only inspection used current primary checkouts, which may include concurrent
uncommitted work. An inexpensive delegated reader inspected owner instructions
and code; coordinator confirmed key implementation and maintained evaluation
records. These observations are not deployed-state claims.

### CineForge — Spike now (highest value)

`src/cine_forge/modules/visualization/storyboard_v1/support.py:12` uses
`gpt-image-2`; generic `src/cine_forge/ai/image.py:32` and design-study API
`src/cine_forge/api/routers/design_study.py:277` use Imagen4. Dispatch at
`ai/image.py:407-455` only accepts GPT Image or Imagen models: NB2.1 needs a
native Gemini route, not a model-string substitution.

The Ideal explicitly requires character/location/prop references and recurring
identity. `benchmarks/tasks/storyboard-generation-quality.yaml` and
`docs/evals/registry.yaml` maintain runtime generation, retained media,
reference transport and quality judgment. Historical entries show identity,
readable-text leakage, latency and cost weaknesses; some older evidence is
explicitly contaminated/non-decision-grade. Use the latest retained-media
packet and current owner verdict contract, not an old headline score.
NB2.1 typography improvements alone are not success: storyboard output should
avoid readable text. Test prevention of unwanted text as well as identity.

Recommended next work: owner story for a native adapter and matched, capped
comparison against the current GPT Image2 storyboard lane, with Imagen4 as a
secondary design-study comparator only if separately scoped. Use owner public
or synthetic fixtures; retain source references, exact request/returned ID,
parameters, output media/hashes, failures, latency and total cost including
thinking/references/judges. Start one reference-conditioned sequence, stop for
transport/fidelity failures, then run the maintained matrix if promising.
Keep reference count within supported limits (14 total,4 characters/10 objects);
current benchmark records include15 direct refs in some historical packets, so
choose a common valid reference subset before comparison, never silently drop
inputs. Separate input-capacity tradeoffs from quality results.
No numerical campaign budget or paid authorization is implied by this scout;
prepare owner-based conservative reservations before requesting an eval selection.

### Storybook — Defer embedding replacement

`packages/backend/src/ai/embedding.ts:1-28` explicitly ships derived-text-first
retrieval with hosted `gemini-embedding-2`, asymmetric query/document prefixes;
chat messages, transcripts and artifact descriptions enter the index.
`packages/db/src/schema.ts:1714-1741` uses768-dimensional pgvector/HNSW.
Native raw-media embeddings are intentionally unshipped. Storybook does embed,
but there is no established need to replace its model today.

A new768-dimensional model still defines a different vector space: re-embed
both documents and queries, version the index, preserve source-revision/deletion
eligibility and benchmark retrieval/context usefulness before cutover. Local
embeddings may improve privacy/offline operation but do not make Storybook's
other hosted AI calls local. Reopen for a concrete offline/privacy requirement,
measured embedding cost/latency bottleneck or approved raw-media retrieval story.

### Echo Forge — Defer; stronger future multimodal use than a random text swap

`docs/decisions/adr-004-hybrid-sound-matching-retrieval/adr.md:47-58` and
`src/soundscape/soundMatcher.ts` retain metadata/simple scoring with a later
embedding seam. Text-to-audio retrieval could eventually match sound by acoustic
content rather than filenames/tags. Reopen on demonstrated metadata retrieval
misses and an owner sound-query relevance corpus; similarity never authorizes
playback/control actions. No current embedding implementation to replace.

### Remaining tracked projects

- Dossier: defer; semantic extraction/conflict graphs need typed meaning and
  provenance, not a new vector model. No measured retrieval bottleneck identified.
- Doc Web: no current adoption; NB generates images while the product preserves
  and extracts source imagery; Gemma does not replace crop/OCR safety checks.
- Board Game Ingester: no current adoption; generated components are not faithful
  source extraction, and no measured local multimodal-retrieval need established.
- Robo Rally: defer visual asset experiments until a concrete art requirement;
  no current reason to introduce this provider into game logic.
- Ultima IV Web: defer; original-game fidelity and controls remain the task,
  generated art is not source behavior evidence.
- Financial Hub and Financial Monthly Analysis: no current adoption; local
  retrieval might be interesting under a future explicit requirement, but does
  not justify touching private reconciliation/classification or sending data.
- VLC Thumbs: no current adoption; thumbnail sampling requires decoded source
  frames, not generated imagery. Semantic moment search would be a separate
  product story, not part of hover thumbnails or durable bookmarks.

## Routing and validation

Prepared owner inbox notes in isolated `codex/scout087-google-models-20261006`
branches (uncommitted, primary checkouts untouched):

- `/Users/cam/.codex/worktrees/scout087-cine-forge-20261006/docs/inbox.md`
- `/Users/cam/.codex/worktrees/scout087-storybook-20261006/docs/inbox.md`
- `/Users/cam/.codex/worktrees/scout087-echo-forge-20261006/docs/inbox.md`

These are prepared handoffs, not landed owner backlog or implementation.
Conductor scout/index/intake and owner inbox-only diffs were inspected with
whitespace checks; no product suites are warranted for these prose additions.
Confidence high in documented interfaces and inspected code; model superiority,
account callability, local resource requirements and end-to-end economics remain
unmeasured. Recommended next step: prepare CineForge's scoped comparison story
and spend proposal before running paid generation.
