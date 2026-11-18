# Search playbook

## Daily core

1. Read `evaluated-models.md`, `source-scorecard.md`, the most recent daily
   report, `candidates.md`, and recent model scouts before searching. Match each
   lead against canonical IDs, aliases, and dated checkpoints before proposing
   owner work. An existing match suppresses a new-eval recommendation.
2. Check first-party release notes, model catalogs, API references, pricing,
   and official announcement accounts for OpenAI, Anthropic, Google/DeepMind,
   xAI, DeepSeek, Alibaba/Qwen, Moonshot/Kimi, Z.ai/GLM, Mistral, and MiniMax.
   For Qwen, check both the Qwen release blog and the matching QwenCloud model
   page: the former can name the open-weight release while the latter can
   establish the managed API ID, price, limits, and documented features.
3. Query OpenRouter's public `GET https://openrouter.ai/api/v1/models` for
   model IDs, routing, modalities, token limits, and advertised parameters.
   Treat it as discovery/access metadata only.
4. Rotate one small secondary slice: API release-note search, a credible
   technical-news/launch tracker, a model hub, a leaderboard, or an official
   account. Verify any material lead at a primary source.

## Search patterns

- `site:<provider-domain> "August" "2026" model API release`
- `<provider> API changelog latest model`
- `site:openrouter.ai <exact model family>`
- provider-specific model catalog and pricing endpoints documented in the
  relevant source; do not authenticate or call inference for discovery.

Use Twitter Scraper for X URLs/accounts and YouTube Transcripts for YouTube
sources when those connectors are available. Otherwise prefer official web
pages over search snippets.

## Cadence and failure handling

Check the core daily; rotate 2–4 secondary sources and replace low-yield,
redundant sources only after recorded evidence. Search results can lag primary
pages; a vendor benchmark proves neither quality in a maintained lane nor
production contract. Catalog `supported_parameters`, a generic JSON mode, or
HTTP success does not prove strict JSON Schema, enforced tools, served identity,
privacy, reliability, or callability for Cam's account/region.

Provider documentation can also lag or disagree across pages after a release.
When a release note, pricing table, and endpoint reference disagree, record the
exact conflict, use the newest model-specific API table only as documentation
evidence, and require an owner-side contract probe before treating the route as
callable or strict-contract qualified.

For an already evaluated model, a newly documented endpoint, price, feature, or
aggregator route is a monitoring update, not a new evaluation recommendation.
Recommend a clearly labeled re-evaluation only when current evidence satisfies
the exact retry condition recorded in `evaluated-models.md`. Documentation or
metadata does not by itself satisfy a callability, strict-contract, privacy,
reliability, latency, cost, or capability trigger.


## 2026-09-07 retrieval refinements

- Use the current month in searches (for example September 2026), but inspect
  official release dates; freshly crawled pages can describe old checkpoints.
- If the central ledger has no exact match, search existing owner attempt
  records before declaring a first evaluation. Sonnet 5's June attempt was
  absent centrally. Record gaps as corrections without editing this watch's
  read-only evaluated ledger.
- If web retrieval of a public catalog endpoint fails, one unauthenticated
  direct HTTP GET may recover the metadata; record both outcomes.
- Rotate Artificial Analysis release discovery, then verify at exact official
  model cards. Prefer those cards over Hugging Face's noisy global recency feed.
- Monitor exact K2 Horizon managed-route appearance; do not repeat its open-weight
  announcement or incur hosting/setup work while access remains unchanged.


## 2026-09-21 date disambiguation

Yearless changelog headings are not evidence of a current-year launch. Check
exact model cards and checkpoint dates first: Mistral's September17 Magistral
2509 entry sits below December2025 releases, while both exact cards identify
September18 2025 and current deprecation. Preserve the minor date discrepancy;
do not convert retrieval freshness or missing year into a new-release alert.


## 2026-09-28 exact retrieval pointers

- StepFun's model page links to [JSON Mode / JSON Schema](https://platform.stepfun.ai/docs/en/guides/developer/json-mode). Use that exact path after earlier failed guesses; documented strict mode still requires owner-contract qualification.
- Artificial Analysis release discovery is [models/releases](https://artificialanalysis.ai/models/releases), not `/models/new-releases`. Prefer the release view over noisy indexed comparison pages and generic speed FAQs.


## 2026-10-01 gated-announcement coverage

Pair Google's API changelog with a compact official Google/DeepMind announcement
check. Argon's September30 announcement appeared in Arena before the checked API
release notes, and restricted access still qualifies for discovery. Record the
public name without inventing a model slug; separate output limits from context
metadata. Suppress unchanged gated announcements until exact access or contract
evidence makes owner proposal work actionable.


## 2026-10-03 preview and access-index refinements

- Pair MiniMax's blog with its [API model index](https://platform.minimax.io/docs/guides/models-intro): the latter explicitly distinguishes M Plan/Code-only previews from ordinary API availability. A tool landing page with an ID does not override this restriction.
- Include a targeted [LongCat changelog](https://longcat.ai/platform/docs/ChangeLog.html) check next run; its September25 preview was absent from OpenRouter and missed by the previous core.
- Vercel release posts can lead OpenRouter. Track promotional standard versus fail-closed free aliases separately; serving-platform announcements verify access metadata, not creator checkpoint provenance or owner strictness.
- On a public GET returning compressed bytes, inspect Content-Encoding/decompress before UTF-8 decoding. Preserve failure evidence; do not treat decode failure as source absence.


## 2026-10-06 retrieval refinement

Pair [Mistral model index](https://docs.mistral.ai/models) and [news index](https://mistral.ai/news/) with changelog: Large4 launched October6 while changelog still September29 and official-domain search returned empty. Confirm exact cards and route endpoints directly. Preserve creator1M versus router512K context and promotional versus base prices; neither a newest-entry count nor generic structured-output parameter proves access/contract or immutable checkpoint.


## 2026-10-12 — explicit decision-model daily core

Cam added decision models as a first-class watch category. Existing owner evaluations are tracked, but prior general-purpose-only search did not guarantee daily decision-source coverage. This scope update supersedes earlier specialist/small/derived exclusions for decision models with plausible maintained-lane fit.

Check a compact daily core alongside general-purpose sources:

| Source | Retrieval / purpose |
| --- | --- |
| [TypeSafe models](https://docs.typesafe.ai/models) | JEV pinned versions, moving aliases, native System One contracts and releases |
| [OpenAI Decisions](https://developers.openai.com/api/docs/guides/decisions) | Official Docs MCP first; supported exact models, native endpoint and release changes |
| [Microsoft Foundry Decision docs](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision), [announcement](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/) | Exact Microsoft checkpoints, deployments and typed contracts |
| [Perplexity Decisions](https://docs.perplexity.ai/api-reference/decisions-post), [Decider creator card](https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b) | Hosted versus open checkpoint/revision, endpoint-specific terms and new releases |
| [Qwen decision API](https://docs.qwencloud.com/api-reference/decision-model-api), [release notes](https://docs.qwencloud.com/changelog/models) | Decision service identities and material contract/access changes |
| [OpenRouter decision catalog](https://openrouter.ai/api/v1/models?output_modalities=decisions), [API discovery](https://openrouter.ai/skills/) | Public decision metadata separately from generation catalog; discover successors and providers |

Follow current source links to successor cards/catalogs rather than assuming these recorded checkpoints stay latest. General generation-catalog absence does not imply decision-model absence. Keep model ID, served revision, deployment and endpoint/configuration separate; protocol similarity does not prove shared weights. A new endpoint on an already evaluated model is a possible endpoint/configuration re-evaluation subject to its recorded gate, not a first evaluation.

Track Noul/predicate, finite Choice, ordered Score, probabilities/calibration, abstention, text/image eligibility, fallback behavior, actual task latency/cost and endpoint-specific retention/privacy. Typed confidence is not correctness; generic chat ZDR does not prove Decisions coverage. Strongest existing owner fits: Storybook routing/confirmation, Doc Web consistency/uncertainty review and Echo control-intent; Board Game orientation only for eligible image contracts. Preserve owner-specific gates and no unchanged repeat recommendations. No paid probes or owner changes in the watch.


## 2026-10-13 decision-route safeguards

Use the separate decision catalog;22 entries revealed untracked creator families despite unchanged generalist coverage. Rotate Cloudflare/Nace/Liquid/ScaleDown/Upstage creator docs rather than querying every new slug daily. Nace direct drex-v2.0 substitutes1.5 beyond8,192 state/16,384 row tokens despite nominal131k request limits; router131k does not establish same behavior. ScaleDown /v1/scaledown reads only state.text/state.document, unlike arbitrary Jev state; keep its /classify image contract separate. Liquid per-question input billing can reverse per-token economics. Creator multimodal weights do not prove router modality support. Reject silent substitutions or lossy state projection before owner quality comparison. [Dated evidence](daily/2026-10-13.md).


## 2026-10-14 catalog narrative safeguard

Compare the saved newest-ID slice individually with current candidate and evaluated ledgers, then primary-verify unfamiliar names even when they were already present in yesterday's snapshot. Muse Wonder was present October13 but omitted from its narrative; primary verification October14 recovered it. Preserve discovery/verification/release dates separately. For Meta distinguish API Wonder from subscription-only Full and request max effort. For independent open decision heads distinguish TypeSafe namesakes, weight-preserving renames, local serving contracts and costly deployment requirements; derived models remain eligible, but no automatic download/rental/evaluation follows discovery.


## 2026-10-15 creator-contract and sampling safeguards

Promote held decision candidates only after creator verification. Together Tev1 uses finite letters on Chat Completions; Respan uses native behavior probabilities on /api/v1/scores. Neither implies generic SystemOne Choice/Score parity. Respan generic model catalog Chat examples and context differ from scorer docs; keep those endpoints separate. Compare newest slices at equal widths; expanding35 to40 is not five new releases. A sidebar successor name whose link returns predecessor documentation is not verified successor identity. [Evidence](daily/2026-10-15.md).


## 2026-10-17 successor identity and joint decisions

Perplexity native old1.1/v1 names now select1.2; response `model` echoes the requested name. DeepSeek native Flash aliases now map1017 while changelog lags. Pair exact current model tables with dated cards; preserve old owner served identities and classify genuinely new checkpoints separately from forbidden unchanged retries. Beam October5 announcement versus October16 API/weight docs demonstrates why announcement, access and discovery dates remain separate.

Perplexity1.2 joint questions can change each other's answers; freeze grouping, use Flash one question/request by default, and distinguish hosted image/token/question limits from creator local runtime. Confidence/calibration claims do not prove safe abstention. Compare exact router endpoint price/precision/context/output, not just catalog default. [Run evidence](daily/2026-10-17.md).


## 2026-10-20 retrieval refinements

- MiniMax preview URLs now redirect to GA; retain historical preview identity and compare exact GA API name. A free catalog row with an empty endpoint list is not verified routable access.
- Inception `/llms.txt` links decision capability/API docs; when `.md` retrieval fails, one extensionless linked-page recovery works. Do not infer absence from guessed `/mercury-decide` or failed privacy pages.
- If scheduler last-run metadata has no local report, name the evidence gap and compare against the latest actual snapshot; never reconstruct a missing report as fact.


## 2026-10-22 decision-source additions

After unique creator-verified yield, include [Baseten decision docs](https://docs.baseten.co/inference/model-apis/decision-models) and [launch changelog](https://www.baseten.co/resources/changelog/) in short-term daily core; reassess sustained value. Use [Nace Max guide](https://console.nace.ai/docs/drex/guides/drex-max) alongside [model table](https://console.nace.ai/docs/drex/reference/models): selector/resize behavior and aliases differ from general advertised context. Preserve native/router limits and modality disagreements. A free catalog listing with empty endpoint array is not a usable-route proof; native `latest` is not a pinned checkpoint. General counts can stay unchanged while IDs/promotional routes change.


## 2026-10-25 typed-extraction discovery gap

Include [Cloudflare WorkersAI changelog](https://developers.cloudflare.com/changelog/product/workers-ai/) and [extraction-model concepts](https://developers.cloudflare.com/workers-ai/concepts/extraction-models/) in short-term daily native core. Clairic is a non-generative typed-value model absent from both generation and decision router catalogs. Do not infer source completeness from those two filters. Preserve extraction versus Noul/Choice/Score contracts; source spans/null handling can fit maintained extraction tasks, but estimates/computation must not silently become literal source evidence. Record per-pass versus headline-context disagreements before recommending owner fixtures. [Discovery audit](daily/2026-10-25.md).


## 2026-10-26 local decision checkpoints

Rotate [FLock creator runtime](https://github.com/FLock-io/this-that-model) and linked checkpoint cards: papers can describe older checkpoints while loaders still default to them. Preserve explicit checkpoint, weight revision, backend and precision when proposing owner work. Public local weights can qualify a decision lead without a hosted router listing; generic hosted brand names do not establish exact identity/privacy. Do not mistake classification distributions for validated abstention or native Noul/Score protocol compatibility. [Discovery](daily/2026-10-26.md).
