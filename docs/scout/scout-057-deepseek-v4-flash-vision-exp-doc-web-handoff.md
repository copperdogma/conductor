# Scout 057 — DeepSeek V4 Flash Vision Exp Portfolio Routing and Handoff

**Source:** DeepSeek first-party API documentation and current doc-web eval,
runtime, and provenance surfaces, checked 2026-08-21.
**Status:** Superseded
**Candidate:** `deepseek-v4-flash-vision-exp` on the direct DeepSeek API
**Projects reviewed:** conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

> **Superseded on 2026-08-21:** This file preserves the initial direct-provider
> routing analysis. [Scout 058](scout-058-deepseek-v4-flash-vision-exp-eval-routing.md)
> is the authoritative portfolio selection and campaign record. It narrowed
> immediate execution to doc-web and CineForge, recorded the actual OpenRouter
> transport investigation, and now governs retries. Do not execute this file's
> older three-repo shortlist or its held-out prerequisite. Story 029 separately
> records that doc-web's hand-authored crop goldens are the authoritative
> normative benchmark rather than a mandatory new held-out set.

## Portfolio routing

The model deserves three repo-local eval offers, each on one maintained lane;
it does not deserve a portfolio-wide sweep or default-model campaign.

1. **doc-web — Evaluate first.** Use the maintained crop-detector ladder and
   the new held-out validity contract described below. This is the strongest
   direct fit for the model's new native image understanding and can change the
   production `gemini-3-flash-preview` detector route.
2. **Storybook — Evaluate second, photo lane only.** Run
   `story056-photo-understanding` first against incumbent
   `gemini-2.5-flash-lite`; if it passes, run the materially distinct
   `story060-artifact-evidence-fusion` lane. Story 056 requires `1.0`, latency
   at most 5,000 ms, and cost at most `$0.001`; Story 060 separately requires
   `1.0`, latency at most 7,000 ms, and cost at most `$0.0003`. Use only the
   existing synthetic/public image fixtures until DeepSeek privacy terms are
   approved. Do **not** evaluate this model as Storybook's Luna/chat default:
   its relevance is grounded photo and scanned-document understanding.
3. **CineForge — Evaluate third, repaired frame-packet comprehension only.**
   Use the source-clean, image-packet lane established by the visual-modality
   truth repair, not the mislabeled native-video/audio claim and not the
   text-only script-bible lane. Require exact image payload inspection,
   decision-eligible fixtures, source-grounded evidence, and the lane's current
   latency/cost gates. Do not infer native video support: DeepSeek documents
   image input, not video input.
4. **Board Game Ingester — Defer with a concrete trigger.** Its rulebook/image
   pipeline has plausible source-role, component-inventory, crop-review, and
   asset-matching lanes, but current records say to wait until a broader
   model-owned image/package story opens. When that happens, this model is a
   credible bounded VLM subject; do not interrupt deterministic seed/package
   readiness now.
5. **Dossier — No direct vision eval.** Dossier intentionally delegates raw
   PDF, OCR, and image parsing to doc-web and consumes attributable text or
   document artifacts. Re-evaluate only if a maintained Dossier decision lane
   begins accepting native images; do not duplicate doc-web's ownership.
6. **Echo Forge — Defer.** Its maintained model decision surfaces are audio
   and structured scene-to-soundscape mapping. UI/icon visual review notes do
   not yet form a decision-bearing subject-model eval.
7. **Robo Rally — Reject.** No current decision-bearing API vision lane.
8. **Conductor — Route only.** Preserve this ranked recommendation and create
   approved owner-repo handoffs; do not execute their benchmarks here.

**Offer:** after Cam approves the shortlist, create separate isolated
owner-repo tasks for doc-web, Storybook, and CineForge. Each task must begin
with its own access/strict-contract/privacy probes and stop independently on
its first absolute gate. Board Game Ingester remains an offered later trigger,
not an immediate task.

## Decision and owner

Route one bounded evaluation to doc-web's maintained crop-detector surface.
The adoption question is whether exact experimental model
`deepseek-v4-flash-vision-exp` can replace the production Onward detector,
currently `gemini-3-flash-preview`, without weakening source fidelity,
structured-output enforcement, artifact traceability, latency, cost, or the
separate GPT-5.5 page-context safety boundary.

This is the smallest decision-bearing portfolio fit because the release adds
native image understanding. Do not route it first to CineForge's prior
text-only `script_bible_v1` lane: DeepSeek V4 Flash already failed that lane's
latency/reliability gates before semantic scoring, and that evidence says
nothing about the new model's vision quality.

The current 13-case detector corpus is calibration plus production-regression
evidence, not held-out selection evidence. Attempt 026 predeclares the missing
decision surface: 12 natural production crops, balanced `6 pass / 6 fail`,
from at least eight previously unused source pages, independently reviewed and
hashed before model calls. Do not claim candidate superiority or change the
runtime from the exposed 13 cases alone.

## External evidence and call contract

Checked 2026-08-21:

- DeepSeek's changelog announces the experimental multimodal model and exact
  slug `deepseek-v4-flash-vision-exp` on the DeepSeek API. DeepSeek claims
  text capability near V4 Flash and reports large gains on vision-dependent
  agent benchmarks; those vendor results are routing evidence only.
- The first-call and pricing pages list direct base URL
  `https://api.deepseek.com`, OpenAI and Anthropic compatibility, 1M context,
  maximum 384K output, thinking and non-thinking modes, JSON output, tools,
  Responses API, Anthropic API, and concurrency limit 2,500.
- Peak prices are `$0.44/M` cache-miss input and `$1.32/M` output; off-peak is
  `$0.22/M` and `$0.66/M`. Image tokens are billed as input. Each image is
  resized to about an 800x800-pixel budget and capped at 384 image tokens.
- JPEG, PNG, GIF, and WebP are accepted. Chat Completions accepts images in
  user messages only. Inline requests are capped at 48 MiB; an inline or URL
  image is capped at 32 MiB. Responses uses `input_image` parts and also
  supports tool-output images.
- Official JSON Output is `response_format={"type":"json_object"}` and can
  occasionally return empty content. The Chat API reference does not expose
  response-level `json_schema`; it separately documents beta strict function
  tools. Therefore prompt-only JSON or `json_object` alone does not qualify
  doc-web's strict bbox contract.
- Thinking defaults to enabled. Supported documented controls are high/max;
  compatibility low/medium values map to high. Thinking mode ignores sampling
  parameters, so the adapter must not infer that `temperature=0` controls it.
- DeepSeek automatically uses disk context caching. Public documentation says
  caches are account-isolated and unused entries are cleared after hours to
  days, but it does not establish zero-data retention or non-training terms
  suitable for private fixtures.

Sources:

- <https://api-docs.deepseek.com/updates/>
- <https://api-docs.deepseek.com/>
- <https://api-docs.deepseek.com/guides/vision/>
- <https://api-docs.deepseek.com/quick_start/pricing>
- <https://api-docs.deepseek.com/guides/thinking_mode/>
- <https://api-docs.deepseek.com/guides/json_mode/>
- <https://api-docs.deepseek.com/api/create-chat-completion/>
- <https://api-docs.deepseek.com/news/news0802/>

## Access and privacy

**Access: unverified.** Official docs establish public API availability, not
callability with doc-web credentials. A safe name-only inspection found a
repo-scoped OpenRouter credential but no direct DeepSeek credential. No key was
read or copied and no provider call was made. Search did not establish an
OpenRouter route for this exact vision slug, so do not substitute the text-only
`deepseek/deepseek-v4-flash` route.

The owner should use an ignored repo-scoped direct credential only after Cam
authorizes it. Until DeepSeek's payload retention/training terms are pinned,
send only checked-in public or synthetic images. Do not send private books,
family material, unpublished documents, signed URLs, or reusable uploaded
files. Disable/reject cache reuse where the API permits it; otherwise record
automatic cache behavior as a privacy limitation.

## Transport qualification

Before any scored case, retain sanitized raw request/response evidence and
fail closed at each step:

1. Confirm the exact slug is authorized with the intended repo credential.
2. Make one minimal direct text call; require terminal success, exact returned
   model identity when exposed, complete content, and valid usage.
3. Send a generated 128x128 black-square image through the intended direct
   endpoint. Require the expected visual answer, terminal success, exact
   identity, usage, and image-token evidence.
4. Probe the production bbox contract using a forced named function with
   `strict=true` and the integer `0-1000` crop schema. Reject ordinary
   `json_object`, prompt-only JSON, empty content, schema-invalid arguments,
   or a provider path that cannot force the tool. Treat failure here as
   compatibility/transport evidence, not model quality.
5. Add the smallest repo adapter that preserves image bytes/content blocks,
   forced strict tool choice, served identity, terminal state, usage, and raw
   evidence. Send the same synthetic case through PromptFoo and compare it to
   the native response. Do not start scoring until parity passes.

The adapter must reject malformed envelopes, multiple choices, fallback or
wrong identity, incomplete output, invalid usage, non-integer/out-of-range
boxes, and any unproven normalization. If strict tool mode is unsupported for
this model or incompatible with image input, stop with `transport: blocked`
and `capability: not measured`.

## Predeclared configuration matrix

**Freshness:** new uncached candidate evidence. Existing exposed fixtures may
be used only for calibration/regression. If the candidate reaches the frozen
held-out gate, rerun both candidate and incumbent once on the same new inputs;
do not reuse stale incumbent evidence for a superiority claim.

**Aggregate paid-call cap:** US$5, including probes, both candidate arms,
candidate/incumbent held-out calls, and one bounded transport repair. Stop and
ask before exceeding it. Start at concurrency `1`; concurrency is not part of
this capability decision.

| Phase | Candidate configuration | Comparator / stop rule |
| --- | --- | --- |
| Native and parity probes | Direct DeepSeek, exact slug, one generated image, forced strict bbox tool, no cache | Stop on access, identity, terminal-state, strict-contract, privacy, or parity failure |
| Calibration | Arm A: non-thinking; Arm B: documented default thinking/high. Same prompt, schema, image detail, and output budget | Use one representative public case plus only the known differentiating exposed cases needed to choose an arm; freeze the winner before broader scoring |
| Exposed regression gate | Frozen arm, maintained integer-coordinate detector prompt/scorer/golden, no cache, `-j 1` | Must reach `13/13` and `overall >= 0.95`; this can veto but cannot prove superiority |
| Held-out decision gate | Frozen candidate and fresh `gemini-3-flash-preview` incumbent on the same predeclared 12 cases | Require source-verified `12/12`, no material crop/text-exclusion regression, valid artifacts, and symmetric opportunity |
| Production-parity confirmation | Only after the held-out gate: same bounded `driver.py` path and exact production recipe except model/provider | Preserve cover bypass, high-resolution mapping, upstream metadata, caption/layout behavior, provenance, and the independent GPT-5.5 validator |

The two candidate arms are the complete configuration budget. One
request-shape repair is allowed before scoring only when it changes no prompt,
reasoning level, image detail, or output budget. Any content-affecting repair
is a new declared experiment and needs owner approval. Do not add max-thinking,
multiple image-detail sweeps, prompt variants, or retries after seeing scores.

## Gates and evidence ownership

- Freeze and hash the candidate adapter, effective rendered prompt, forced
  tool schema, task, scorer, golden, fixture manifest, image bytes, and held-out
  provenance before decision calls.
- Preserve the current detector grouping and text-exclusion rules, including
  the known seal/signature and caption-contamination boundaries. Do not change
  goldens or scorers to rescue the candidate.
- Record raw terminal state, served identity, request ID, usage including
  reasoning/image tokens when exposed, latency, calculated cost at the actual
  peak/off-peak rate, cache state, and every failed attempt.
- Compare conditional semantic quality separately from end-to-end reliability,
  latency, and retry overhead. One valid retry does not erase an initial error.
- The production detector may change only if held-out and driver artifacts
  pass and the candidate is operationally competitive with the fresh
  incumbent. The exact latency/value promotion rule must be frozen before the
  held-out calls; absent a stronger owner rule, require no worse latency or
  cost without a source-visible quality gain.
- Keep `crop-page-level-deletion-gate` pinned to GPT-5.5. Run it with the
  candidate only as a separately declared follow-on after detector promotion
  evidence; its hard gate remains `22/22`.
- Write raw artifacts only to doc-web's ignored/protected result locations and
  track hashes, sizes, safe commands, model/provider IDs, pricing source/date,
  and exact evaluated code identity in a new doc-web attempt. Conductor owns
  only this handoff.

## Evaluation record

1. **Decision and owner:** doc-web crop detector; candidate direct DeepSeek
   Vision Exp versus production `gemini-3-flash-preview`.
2. **External evidence:** exact official slug and multimodal API contract
   checked 2026-08-21; vendor benchmark claims are not repo evidence.
3. **Configuration matrix:** non-thinking and default/high calibration arms,
   then one frozen arm; US$5 aggregate cap; fresh candidate and symmetric
   held-out incumbent calls.
4. **Access:** unverified.
5. **Transport:** inconclusive until direct strict-tool and repo parity probes.
6. **Reliability:** not measured.
7. **Capability:** not measured.
8. **Economics:** official list prices known; repo latency, cost, and retry
   overhead not measured.
9. **Adoption:** not evaluated — target-repo handoff required.
10. **Evidence limits and next step:** first authorize a repo-scoped direct
    credential and public/synthetic-only payload policy; then qualify access,
    vision, forced strict tool output, and harness parity. If all pass, freeze
    the 12-case held-out contract before decision calls.

No provider probe, target benchmark, target-repo edit, credential transfer,
private-payload use, default change, commit, or push occurred in Conductor.
