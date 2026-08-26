# Scout 059 — Ox Alpha Portfolio Evaluation Recommendation

**Stage:** Stage 2 — selected owner campaigns completed
**Source:** OpenRouter public model/endpoint metadata and current API, routing,
reasoning, structured-output, and privacy documentation, initially checked
2026-08-22 and refreshed 2026-08-25.
**Status:** force-fresh drift rerun complete / callable / strict structured output blocked / no consistent improvement
**Candidate:** `stealth/ox-alpha` through OpenRouter

## Candidate verification

OpenRouter's public catalog lists exact model ID and canonical slug
`stealth/ox-alpha`, created 2026-08-20. The only listed endpoint is
`Stealth | stealth/ox-alpha`; the maker and a direct first-party API are not
disclosed. Model-family guesses and model self-identification are not evidence.

The catalog reports text, image, and video input; text output; a 1,048,576-token
context window; a 131,072-token maximum completion; and current preview pricing
of `$0` for input and output. Reasoning is mandatory, defaults to `max`, and
supports `max`, `high`, and `low`; default sampling is `temperature=1` and
`top_p=0.95`.

The model metadata lists `response_format`, `tools`, and `tool_choice`, but
omits OpenRouter's distinct `structured_outputs` capability flag. Provider-
enforced strict JSON Schema is therefore unverified and must be proved before
semantic scoring on any structured lane.

The endpoint currently has no published data-policy record. OpenRouter says an
unknown endpoint policy is treated conservatively as retaining and training.
Every selected owner must first try fail-closed routing with
`data_collection="deny"`, `zdr=true`, `require_parameters=true`, and model and
provider fallbacks disabled. If no eligible endpoint remains, only public or
synthetic fixtures may proceed after owner-policy review; private inputs remain
ineligible.

Sources:

- <https://openrouter.ai/api/v1/models>
- <https://openrouter.ai/api/v1/models/stealth/ox-alpha/endpoints>
- <https://openrouter.ai/docs/guides/overview/models>
- <https://openrouter.ai/docs/guides/features/structured-outputs>
- <https://openrouter.ai/docs/guides/best-practices/reasoning-tokens>
- <https://openrouter.ai/docs/guides/routing/provider-selection>
- <https://openrouter.ai/docs/guides/privacy/provider-logging/>
- <https://openrouter.ai/docs/guides/features/zdr>
- <https://openrouter.ai/docs/faq>

Public metadata proves **API-listed**, not callable. No target credential,
authenticated catalog, provider inference, or benchmark was used in Stage 1.

## Evaluate now

### 1. Dossier — C5 extraction value/default-candidate screen

- **Lane:** `compromise-C5-cost-optimization`, extraction quick-smoke first.
- **Incumbent:** `gemini-3.1-flash-lite`; fresh quality ceiling
  `gpt-5.3-chat-latest`.
- **Decision:** whether a currently zero-price challenger can enter Dossier's
  verified extraction default-candidate window without weakening quality,
  completion, latency, reliability, or privacy.
- **Why now:** C5 explicitly reopens for a cheaper subject model. The current
  same-run evidence keeps Gemini as balanced/value winner and GPT-5.3 as raw
  quality winner; Ox Alpha's price and long-context reasoning form a concrete
  challenger hypothesis rather than generic frontier prestige.
- **Progressive gate:** qualify exact identity, terminal completion, strict
  extraction contract, reasoning/output budget, and harness parity on one
  synthetic case. Then compare default `max` versus `low` on a calibration
  case, freeze one arm, and run the three-fixture quick smoke against fresh
  incumbent and ceiling. Require entry into the current 5% quality window, no
  fixture-floor or schema failures, latency at most `60s`, and cost at most
  `$0.50`; advance to high-confidence T1 only if the screen passes.
- **Fixtures/privacy:** synthetic or clearly public owner-approved fixtures
  only while the upstream policy is unknown.
- **Provider-spend ceiling:** **US$1.00**.

### 2. doc-web — image-crop-extraction detector screen

- **Lane:** `image-crop-extraction` first; later crop-safety gates remain
  conditional.
- **Incumbent:** `gemini-3-flash-preview`, maintained best `13/13`, overall
  `0.9703`; the newer Gemini 3.7 arm matched aggregate quality but failed the
  downstream crop-only safety gate.
- **Decision:** whether Ox Alpha's image path deserves advancement as a crop
  detector challenger. This screen cannot by itself change the runtime because
  the exposed corpus lacks held-out model-selection truth.
- **Why now:** the exact OpenRouter route declares image input, supports tools
  and response formatting, and is currently free. doc-web has a mature public
  checked-in image corpus, strict integer bbox contract, scorer, and progressive
  safety ladder.
- **Progressive gate:** first prove lossless image transport and provider-
  enforced strict integer `0-1000` bbox output on a generated image, then
  PromptFoo parity. Run one representative case before the 13-case detector.
  Require `13/13`, overall at least `0.95`, exact identity, zero schema/provider
  errors, and competitive latency. Only then run `crop-validation` (`40/40`)
  and the page-context gate (`22/22`); do not claim promotion without the
  separately frozen held-out slice.
- **Fixtures/privacy:** public checked-in fixtures only; no private books or
  unpublished documents.
- **Provider-spend ceiling:** **US$0.75**.

### 3. CineForge — exact-runtime `script-bible` value screen

- **Lane:** default-driving two-corpus `script-bible`, beginning with the
  synthetic Open Frequency runtime case.
- **Incumbent:** provisionally configured `gemini-3.5-flash-lite`; historical
  production value reference `grok-4.1-fast-reasoning`.
- **Decision:** whether an exact strict-schema Ox Alpha configuration can clear
  CineForge's repaired runtime-shaped quality, latency, and cost gates and earn
  a fresh two-corpus comparison.
- **Why now:** this lane is explicitly waiting for fresh exact-contract evidence.
  Ox Alpha's current zero price and 1M context could change the value result if
  mandatory reasoning remains fast and the anonymous route truly enforces the
  `ScriptBible` schema.
- **Progressive gate:** pin exact model/provider with no fallbacks, prove strict
  `ScriptBible` output and PromptFoo parity, then run only Open Frequency.
  Require overall at least `0.90`, deterministic assertions/hard assertions,
  latency at most `30s`, and subject cost at most `$0.01`. Stop on any absolute
  gate; run the second screenplay and fresh incumbent only after the first case
  passes.
- **Fixtures/privacy:** synthetic Open Frequency first. The second repo-owned
  screenplay requires owner confirmation that its payload is eligible for the
  resolved endpoint.
- **Provider-spend ceiling:** **US$0.75**.

### 4. Echo Forge — scene-outline eligibility, then extractor value

- **Lane:** `scene-to-soundscape-golden` two-case eligibility gate; conditional
  continuation to `soundscape-extractor-value` across 34 goldens.
- **Incumbent:** `gpt-5.4-mini`, recorded production value winner at roughly
  `65-69%` quality, about `2.1s`, and approximately `$0.0001` per extraction.
- **Decision:** whether Ox Alpha can become the production scene extractor or
  a smarter-generator candidate while improving value without losing grounded
  soundscape semantics.
- **Why now:** both maintained evals explicitly reopen for a new model/provider.
  Recent strict-schema challengers reached only `0/2` or `1/2`; a free
  mandatory-reasoning model is a real new value hypothesis if it can reach
  `2/2` without excessive latency.
- **Progressive gate:** qualify strict schema/version-3 raw-output provenance
  and harness parity, then run the two maintained scene fixtures. Require `2/2`
  and complete raw-to-normalized evidence before touching the 34-case value
  benchmark. On the broader lane, freeze the current prompt/scorer/judge,
  compare fresh incumbent and candidate symmetrically, and require at least the
  incumbent's quality with better three-axis value; mandatory-reasoning latency
  remains decision-bearing even at zero subject price.
- **Fixtures/privacy:** checked-in public/synthetic or otherwise owner-approved
  scene fixtures only.
- **Provider-spend ceiling:** **US$1.50**.

**Campaign maximum: US$4.00.** This covers all four owner lanes, their bounded
transport probes, fresh comparators, permitted retries, and judge calls. Each
owner stops independently on its first absolute gate; unused budget is not
transfer authority for broader experiments.

## Stage 2 follow-through

Cam approved all four numbered evaluations on 2026-08-22. Each owner ran from a
fresh `origin/main` worktree with one temporary repo-local OpenRouter credential,
public or synthetic inputs only, fail-closed privacy routing, and no authority
for commits, pushes, deployments, private payloads, or default changes.

All four owners reached the same terminal result before inference. The exact
model remained catalog-visible, but OpenRouter returned HTTP 404 because its
sole `Stealth` endpoint could not satisfy the required combination of provider
pinning, disabled fallbacks, `require_parameters=true`,
`data_collection="deny"`, and ZDR. Strict-schema capability, reliability,
semantic quality, latency, and production economics therefore remain
unmeasured. This is provider-route/privacy-contract evidence, not a model-wrong
result.

| Owner | Base | Progressive result | Spend | Adoption verdict |
| --- | --- | --- | ---: | --- |
| Dossier | `4ab33e38` | Exact catalog match; strict synthetic C5 probe rejected before inference. No quick-smoke fixture ran. | `$0.00 / $1.00` | Do not adopt; retry only with an equally strict eligible route. |
| doc-web | `009afed4` | Provider-free adapter checks passed; strict text and generated-image probes were rejected before inference. No 1/13/40/22-case lane ran. | `$0.00 / $0.75` | Defer; capability not measured. |
| CineForge | `94861914` | Strict `ScriptBible` probe failed; removing only the schema still produced an explicit no-ZDR-endpoint rejection. No screenplay, judge, or incumbent call ran. | `$0.00 / $0.75` | Defer; privacy route ineligible. |
| Echo Forge | `17f9733a` | Provider-free 2/2 preflight passed; live strict-schema probe was rejected before inference. No scored 2-case or conditional 34-case lane ran. | `$0.00 / $1.50` | Defer; privacy route ineligible. |

**Campaign spend: US$0.00 of US$4.00.** No owner default changed. The owner
worktrees retain uncommitted adapter/configuration scaffolding, sanitized
failure evidence, registry updates, and validation results for review. The
temporary injected credential variables were removed after each owner finished.

## 2026-08-22 correction — payload-dependent privacy and rerun

Cam clarified that Dossier's family-history stories are publicly available and
that The Mariner is Cam's own screenplay, so neither has a privacy issue. The
first Stage 2 campaign had incorrectly treated ZDR, provider data-collection
denial, and exact endpoint pinning as universal evaluation gates. The
`evaluate-model` skill and owner protocol were corrected to classify fixtures
first, make retention/ZDR controls payload-dependent, require exact model rather
than unnecessary provider identity, and permit a bounded diagnostic relaxation
on approved public/synthetic data without misrepresenting it as production
parity.

Cam then selected a force-fresh rerun of doc-web, CineForge, and Echo Forge,
explicitly excluding Dossier. Each rerun omitted ZDR and data-collection denial,
did not pin the sole Stealth endpoint, required exact requested/served
`stealth/ox-alpha`, and configured no alternate-model fallback.

| Owner | Corrected result | Spend | Verdict |
| --- | --- | ---: | --- |
| doc-web | Strict schema plus `require_parameters=true` still produced router 404. After retaining the complete response and removing only a whole-response Markdown fence, the exact-model diagnostic produced valid crop JSON: the maintained 13-case lane scored `13/13` structurally with mean `0.915146`, below the `0.95` gate and `0.9703` incumbent. Mean latency was `8.539s`; manual review confirmed bounding-box undercoverage. The gated 40/22-case follow-ons did not run. | `$0.00 / $0.75` | Access available; strict crop transport blocked; diagnostic capability measured below gate and incumbent; do not adopt. |
| CineForge | Strict `ScriptBible` plus parameter enforcement still produced router 404. A retained exact-model Open Frequency response remained malformed JSON after whole-response fence removal because of an unescaped embedded quotation, and took `47.799s` against the `30s` gate. No repair, scorer, judge, Mariner case, or incumbent ran. | `$0.00 / $0.75` | Access available; strict runtime transport blocked; diagnostic also fails syntax and latency gates; non-drop-in and defer. |
| Echo Forge | Strict schema plus parameter enforcement still produced router 404. The retained Dungeon diagnostic reached exact Ox Alpha/Stealth but took `150.129s`, exhausted all `8,000` completion tokens, and ended with `finish_reason=length`. It opened a JSON fence without closing it, so wrapper-only cleanup could not produce a parseable payload. Tavern and the conditional 34-case lane did not run. | `$0.00 / $1.50` | Access available; strict version-3 transport blocked; diagnostic truncated before schema or semantic scoring; defer. |

**Corrected rerun spend: US$0.00 of US$3.00.** The privacy correction changed
access from blocked to callable and isolated the actual shared blocker:
OpenRouter's Stealth endpoint does not qualify `response_format` under
`require_parameters=true`. Complete raw-response retention plus wrapper-only
cleanup then separated adapter friction from capability: doc-web obtained a
valid but below-gate score, while CineForge still failed JSON syntax and its
latency gate, and Echo Forge exhausted its response budget before producing a
complete payload. No result supports a runtime-default change. All temporary
credential variables were removed after the reruns.

## 2026-08-25 force-fresh drift rerun

Cam requested the same three owner evaluations again to test the claim that Ox
Alpha learns live and improves day by day. The campaign repeated the preserved
2026-08-22 candidate configuration, maintained public/synthetic fixtures,
progressive gates, no-cache execution, exact served-model requirement, and
repo-local spend ceilings. It was candidate-only: the result can detect
behavioral drift under the opaque `stealth/ox-alpha` slug, but cannot identify
whether a change came from online learning, new weights, routing, serving, or
sampling. OpenRouter still publishes no snapshot/version identifier or claim
of daily live learning for this route.

| Owner | Same-contract 2026-08-25 result | Change from 2026-08-22 | Verdict |
| --- | --- | --- | --- |
| doc-web | Strict routing still returned 404. The exact-model 13-case diagnostic scored `12/13`, mean `0.880846`, with one source-confirmed empty-crop miss; mean latency `7.248s`. | Quality regressed from `13/13` and `0.915146`; mean latency improved from `8.539s`. | Do not adopt. The 40/22 follow-ons remained gated off. |
| CineForge | Strict routing still returned 404. The exact-model Open Frequency diagnostic again produced malformed fenced JSON; provider latency was `96.146s` and PromptFoo total was `217.675s`. | Still syntactically invalid and provider latency was `48.347s` slower than the prior `47.799s` result. | Defer / non-drop-in. No scorer, Mariner, judge, or incumbent ran. |
| Echo Forge | The identical Dungeon request returned terminal `stop` and complete bare JSON, but failed the unchanged strict schema with 51 errors; latency was `189.202s`. | Completeness improved from truncated `length` output, while latency worsened from `150.129s` and the response still could not enter semantic scoring. | Defer. Tavern and the 34-case lane remained gated off. |

The candidate calls again reported `$0`. doc-web also disclosed `$0.0073287`
from seven excluded one-case calls started by an interrupted command-shape
mistake; they did not enter the Ox Alpha score and the campaign stayed within
its US$3.00 ceiling. A narrow Echo Forge parser repair now accepts valid bare
JSON as well as a single complete Markdown fence, preserving the initial
harness rejection while allowing offline schema diagnosis. No default changed,
and all temporary owner credentials were removed after completion.

**Portfolio conclusion:** Ox Alpha exhibited behavioral drift, not consistent
improvement. Two lanes regressed or remained invalid and slower; the one clear
improvement was Echo Forge response completeness, which still missed the
production schema by 51 errors. A single repeat also cannot prove or disprove
the provider's hidden update mechanism. Continued daily reruns would need a
predeclared repeated-measures design and a stable provider snapshot signal to
support more than an endpoint-behavior trend.

## Not recommended now

- **Storybook — Defer.** The direct photo-understanding and evidence-fusion
  lanes already score `1.0` with `gemini-2.5-flash-lite` inside `2.5-4.1s` and
  at tiny cost. Ox Alpha's anonymous upstream cannot currently clear
  Storybook's absolute private-media provider boundary, so a synthetic win
  would not support production adoption. Reconsider only after endpoint
  identity and retention/training policy are acceptable, or a concrete
  Storybook-owned failing golden appears that Dossier/doc-web does not own.
- **Board Game Ingester — Defer.** Its remaining top-level gap is package review
  and downstream readiness, while source routing, crop, inventory, relationship,
  matching, and export seed stages already pass. Private scanned rulebooks also
  make the anonymous endpoint ineligible. Reconsider after a public/licensed
  model-owned rulebook or asset golden exposes a specific failure that doc-web
  does not own.
- **RoboRally — Do not evaluate.** Its maintained evals are deterministic game
  behavior and replay scenarios, not a model-selection surface, and its
  canonical rules source is private. Ox Alpha cannot change a maintained
  provider decision there today.

The selected target repos were modified only in isolated worktrees to retain
uncommitted evaluation scaffolding and evidence. Nothing was committed, pushed,
deployed, promoted, or run with a private payload.
