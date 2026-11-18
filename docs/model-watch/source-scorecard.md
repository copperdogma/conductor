# Source scorecard

Baseline created 2026-08-26. Yield records qualifying leads, not routine
announcements. Cost is public-metadata search cost; this watch uses no paid
inference.

| Source | Role / cadence | Yield and uniqueness | Reliability / friction | Last checked | Last useful | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| OpenAI product/API release notes | Core daily | No new general-purpose model; August GPT-5.6 pricing remained economics-only | First-party; low friction | 2026-08-27 | 2026-07-09 | Keep |
| Anthropic news/model docs | Core daily | No August general-purpose API release; text-watermarking is policy, not a model lead | First-party; low friction | 2026-08-27 | 2026-07-24 | Keep |
| Google Gemini API changelog/model pages | Core daily | Reconfirmed prior Gemini 3.7 Flash GA; no material change | First-party, exact capability docs | 2026-08-27 | 2026-08-13 | Keep |
| xAI news/docs | Core daily | Grok 4.6 platform expansion only; existing model/route | First-party; low friction | 2026-08-27 | 2026-08-12 | Keep |
| DeepSeek API docs | Core daily | Current V4 Pro pricing table now lists Responses API support; older endpoint pages still contradict it, and the exact alias already has owner evaluation attempts | First-party but release pages can lag each other; documentation does not satisfy the recorded owner retry gates | 2026-08-28 | 2026-08-28 | Keep for monitoring; do not recommend a repeat from documentation alone |
| Qwen/Alibaba docs | Core daily | Unique qualifying Qwen3.8-Flash-Next launch and current managed `qwen3.8-flash` page found | First-party model page and launch post; medium friction | 2026-08-27 | 2026-08-27 | Promote to daily direct QwenCloud model/release pages |
| Moonshot/Kimi and Z.ai/GLM docs | Core daily | No new material lead surfaced | First-party but search indexing is uneven | 2026-08-27 | 2026-08-20 | Keep |
| Mistral news/docs | Core daily | Infrastructure/regional-inference update, not a new general-purpose challenger | First-party; low friction | 2026-08-27 | 2026-06-23 | Rotate |
| MiniMax official surfaces | Core daily | Music/video releases and prior M3 references only; no newly released maintained-lane challenger | Sparse indexed docs; medium friction | 2026-08-27 | — | Rotate |
| OpenRouter public catalog | Core daily access discovery | Independently exposed the new Alibaba `qwen/qwen3.8-flash` endpoint, with pricing/limits and public endpoint metadata | Useful access metadata; cannot prove strict contracts/privacy/quality | 2026-08-27 | 2026-08-27 | Keep |
| General web/API release-note search | Secondary, rotating | Found and primary-verified the Qwen release; otherwise no unique qualifying lead | Fast but noisy and index-lagged | 2026-08-27 | 2026-08-27 | Keep, rotate queries |

## Strategy changes

- **2026-08-26:** Baseline added. Keep the compact first-party core and
  OpenRouter catalog; rotate Qwen, Mistral, and MiniMax depth because today's
  discovery yield was low or non-qualifying. No source was retired because this
  is the first scored run.
- **2026-08-27:** Promoted direct QwenCloud model/release pages from rotating
  depth to the daily core: they supplied the primary identity, price, limits,
  and feature evidence for a newly available model, while OpenRouter supplied
  independently useful route metadata. Retain Mistral and MiniMax as rotating
  depth because today's result was non-qualifying.
- **2026-08-28:** Added a documentation-conflict rule for DeepSeek: the current
  V4 Pro pricing/model table lists Responses support, while cached endpoint and
  guide pages still exclude it. The evaluated-model ledger shows the exact
  alias already reached CineForge and Echo Forge owner attempts. Keep the direct
  docs in the core as monitoring evidence, but do not recommend re-evaluation
  unless current evidence satisfies the recorded strict-contract, privacy,
  latency, and cost trigger; documentation alone does not.


## 2026-09-07 run scorecard (supersedes older last-checked cells)

| Source group | Yield / uniqueness / timeliness | Reliability / cost or friction | Decision |
| --- | --- | --- | --- |
| OpenAI docs MCP | Current Astra only; zero new leads | First-party, low cost; fetched model guide | Keep core; last checked September 7 |
| Anthropic newsroom / model release | Sonnet pricing update, no new identity; owner search caught missing ledger row | Low friction; release age and exact owner history essential | Keep core; add owner-search safeguard |
| Google changelog + exact model/pricing | Gemini 3.8 Flash release; owner-worktree search later reconciled a prior exact campaign | High verification quality, low friction; central-ledger-only lookup was insufficient | Keep core plus owner-evidence search; last useful September 7 |
| xAI / DeepSeek / Qwen direct docs | Existing evaluated IDs and specialist churn | Low friction; no retry proof | Keep compact core; last checked September 7 |
| Moonshot / Tencent | No new verified successor | Partial search coverage, uneven indexing | Keep compact search; no promotion from non-results |
| Z.ai / Ollama / official HF card | GLM naming resolved as existing Ox Alpha preview; no new retry | Z.ai blog empty; card/provider page useful; AutoClaw freshness misleading | Keep identity checks; avoid treating app article date as release date |
| Mistral / MiniMax / Meta / Inception | Older or already evaluated releases; no unique actionable challenger | Mostly readable, low yield | Retain rotating depth; last checked September 7 |
| OpenRouter public catalog / exact endpoints | 430 models; corroborated Gemini dated checkpoint; no K2 Horizon | Public Python GET recovered web endpoint error; catalog status is metadata only | Keep core; last useful September 7 |
| Artificial Analysis releases + primary IFM/MBZUAI verification | Unique K2 Horizon lead, deferred for managed access | Useful lead index; benchmarks do not prove owner fit | Keep AA in rotation, add IFM exact-route monitoring; last useful September 7 |
| Hugging Face recent-model feed | No additional unique lead; derivative noise | High redundancy for broad recency, low value | Prefer exact first-party cards over broad feed next run |

No paid inference. Search/tool and orchestration usage were not separately
metered in currency. No source retired on one low-yield run. Missing post-August
28 daily files are a continuity limitation, not proof those searches never ran.


## 2026-09-08 run scorecard

| Source group | Yield / uniqueness / timeliness | Reliability / cost or friction | Decision |
| --- | --- | --- | --- |
| OpenAI docs MCP + official guide; Anthropic, Google, xAI, DeepSeek, Qwen official pages | Zero new qualifying identities; known releases and specialist churn | Readable core, low retrieval friction; high exact-ID verification value | Keep daily core; last checked September 8 |
| OpenRouter public catalog + exact IFM HF card | 426 entries, no Horizon route; HF still has no Inference Provider | Successful unauthenticated GET; count changes are not identity evidence | Keep daily access monitoring; no candidate-state change |
| Moonshot, Z.ai and Inception indexes | No unique new lead; indexes lag known models | Stale content limits recall; app-post date can mislead | Keep compact checks paired with model-specific sources; no promotion |
| Mistral / MiniMax news | Funding and known/specialist releases only | Low friction, zero unique frontier yield | Retain rotating depth |
| Arena open-source text leaderboard | Known Kimi/GLM variants only; September 2 page | Useful secondary discovery, no served-identity proof; some staleness | Keep rotation; next secondary slice Artificial Analysis |

No source retired from one zero-yield run. Search/orchestration currency cost
not separately metered; no paid inference. Detailed endpoints and limitations
are in the September 8 daily report.


## 2026-09-09 run scorecard

| Source group | Yield / timeliness / uniqueness | Quality / cost or friction | Decision |
| --- | --- | --- | --- |
| Core OpenAI, Anthropic, Google, xAI, DeepSeek, Qwen docs | Known identities, no retry proof | Successful low-friction primary retrieval | Keep core; checked September 9 |
| OpenRouter catalog and exact endpoints | 431 entries; unique Mercury GA and Nex routes | Timely access metadata; no inference or contract proof | Keep core; useful September 9 |
| Inception launch/model pages | GA verified; preview change unproven | Current blog; direct URL recovered failed web click | Promote temporarily to daily exact identity check |
| Nex official site/repo/HF | Primary bases establish derivative exclusion | HF web errors recovered by public GET; low cost | Targeted identity source, not daily expansion |
| Kimi/Z.ai/Mistral/MiniMax | Known IDs; stale smaller-provider indexes | Limited recall; zero qualifying yield | Keep compact checks |
| Artificial Analysis release rotation | Existing leads only | Secondary discovery, redundant today | Rotate Arena next; no retirement |
| Tencent | No new catalog/secondary lead | Fresh primary release coverage incomplete | Prioritize direct primary check next run |

No paid inference; search/agent currency cost unmetered. September 9 daily log
records exact endpoints, identity uncertainty and rejected retry framing.


## 2026-09-10 run scorecard

| Source group | Yield / timeliness / uniqueness | Quality / cost or friction | Decision |
| --- | --- | --- | --- |
| DeepSeek release/pricing/vision docs | Unique V4.1 Flash launch and alias-retirement facts | Primary verification high; web errors and search lag recovered with public GET | Keep daily exact pages; useful September 10 |
| OpenRouter public catalog/endpoints | 436 entries; unique dated V4.1 access and provider-contract differences | Low friction, timely; metadata only | Keep daily core; useful September 10 |
| OpenAI docs MCP, Anthropic, Google, xAI, Qwen | Known identities, no satisfied retry triggers | Low friction, high identity-check value | Keep compact daily core |
| Tencent primary org plus Kimi/Z.ai/Mistral/MiniMax/Meta sources | No new qualifying identity; Tencent gap addressed | Delegated public check; release indexes can lag; no new account value | Keep compact core, no promotion |
| Inception and IFM exact sources | No material Mercury preview change or Horizon managed access | Readable, zero new yield | Continue narrow checks, suppress unchanged leads |
| Arena text leaderboard | September 2 page, no unique timely lead | Redundant and stale for launch discovery | Rotate Artificial Analysis next run |

No sources retired. Discovery used no paid inference; search/orchestration
currency cost unmetered. Exact attempts and failures are in the daily report.


## 2026-09-12 run scorecard

| Source group | Yield / uniqueness / timeliness | Reliability / cost / friction | Decision |
| --- | --- | --- | --- |
| OpenRouter public catalog/endpoints | 445 entries; unique Ling VL hosted route; excluded Fugu/Schematron/alias churn | Fast public GET, high discovery value; metadata only | Keep daily core |
| inclusionAI exact HF card | Primary native vision identity and document-fit evidence | Readable card; original release date uncertain; hosted contract separate | Add targeted follow-up rotation; suppress unchanged lead |
| OpenAI docs MCP, Anthropic, Google, xAI, Qwen, DeepSeek | Known identities; no retry proof | Successful compact primary reads, low friction | Keep core |
| Kimi, Z.ai, Mistral, MiniMax, Tencent, Meta, Inception, IFM | No unique qualifying release | Some stale/family-limited indexes; cannot negate known successors | Keep compact coverage; pair Meta with Muse next run |
| Sakana / Inference.net primary posts | Verified scope exclusions | Strong identity-classification value; no sustained relevant yield | Targeted only; do not promote daily |
| Artificial Analysis plus exact lead searches | No additional AA lead; searches located useful primary cards | Broad Schematron search noisy, dates inconsistent | Rotate Arena next; retain exact-ID searches |

No source retired. Public discovery only, US$0 inference; search/orchestration
currency cost unmetered. Details and coverage limits in September 12 daily log.


## 2026-09-13 run scorecard

| Source group | Yield / timeliness / uniqueness | Reliability / cost / friction | Decision |
| --- | --- | --- | --- |
| DeepSeek exact changelog | Unique correction: V4 Pro service continues | Primary readable notice; no inference proof | Keep daily alias monitoring |
| OpenAI MCP, Anthropic, Google, xAI, Qwen | Known identities; no retry evidence | Successful low-friction primary reads | Keep compact core |
| OpenRouter catalog | 445 entries; newest 20 already known | Fast public GET; metadata only | Keep core |
| Moonshot, Z.ai, Mistral, MiniMax, Tencent | No qualifying new identity | Readable primary pages; index completeness limited | Keep compact checks |
| Meta Muse release | Known 1.3; closes Llama-only coverage gap | Primary verification successful | Retain Muse-specific source |
| inclusionAI, Inception, IFM | Existing leads; no new actionable evidence | Low friction, zero fresh yield | Keep narrow follow-up rotation |
| Arena text | September 11 snapshot; no unique lead | Fresher than prior snapshot, redundant | Rotate Artificial Analysis next |

No source retired or new account recommended. US$0 inference; search cost
unmetered. Exact retrievals and limitations in September 13 daily report.


## 2026-09-14 run scorecard

| Source group | Yield / uniqueness / timeliness | Reliability / cost / friction | Decision |
| --- | --- | --- | --- |
| OpenAI MCP, Anthropic, Google, xAI, DeepSeek | Known identities; DeepSeek Pro continuation reconfirmed | Successful primary retrievals, low friction | Keep compact core |
| QwenCloud releases and exact DeepSeek guide | September 13 V4.1 route documentation; unique monitoring value, zero qualifying leads | Primary verification high; no served-identity or retry proof | Keep core; useful September 14 |
| OpenRouter catalog | 445 entries, newest 22 known; no Horizon ID | Fast public GET; metadata only | Keep core |
| Moonshot, Z.ai, Mistral, MiniMax, Meta Muse | Known models/business updates | Successful primary reads; indexes may lag | Keep compact coverage |
| Tencent updates | No verified new finding | Follow-up retrieval failed; direct retry timed out | Recheck primary next run; coverage incomplete |
| Inception, IFM, inclusionAI exact cards | Existing leads, no material new evidence | Readable, low friction and redundant today | Keep narrow rotation |
| Artificial Analysis plus Agnes/Motif creator cards | No qualifying lead; useful preview/production distinction | Secondary-to-primary verification valuable; production access unresolved | Rotate Arena next; one targeted Agnes follow-up |

No source retired or provider account recommended. US$0 inference; search and
orchestration currency cost unmetered. Preserve exact checkpoint distinctions.

## 2026-09-19 run scorecard

| Source group | Yield / uniqueness / timeliness | Reliability / cost / friction | Decision |
| --- | --- | --- | --- |
| QwenCloud exact model/release/contract docs | Unique new Omni lead; timely September18 announcement | High primary value; generic guides lag, strict schema not explicit for Omni | Keep daily core; exact contract follow-up |
| Alibaba exact model guide | Regions and exact limits recovered | Web size-limit failure; alternate official public GET worked | Keep bounded fallback |
| OpenAI MCP, Anthropic, Google, xAI, DeepSeek | Known checkpoints and specialized/platform updates | Successful primary reads; no fresh qualifying yield | Keep compact core |
| OpenRouter catalog/endpoints | 447 entries; FlashX and excluded Pareto/Bonsai; no Omni route | Fast public metadata; no inference/strict proof | Keep daily core |
| BigModel Flash/FlashX Markdown | Useful serving-variant/ID evidence | Public GET succeeds where blog/rendered docs fail | Add exact Markdown fallback, no checkpoint-equivalence inference |
| Kimi configuration/changelog | Newly noticed K2.8 mutable coding alias | Primary readable; membership/owner fit unresolved | Retain targeted config page with Moonshot core |
| Mistral, MiniMax, Meta, Tencent | Known models/service updates | Public reads; Tencent access coverage recovered | Keep compact checks; no broad source expansion |
| Arena changelog | September13–14 known identities, redundant | Low friction, zero unique yield | Rotate Artificial Analysis next |
| Inception, Agnes creator card | No material held-candidate change | Readable; no new actionable yield | Rotate narrow follow-ups |
| Unbiased, PrismML creator pages | Verified exclusions | Primary evidence prevents wrapper/derivative alerts | One-off lead verification, not daily core |

No source retired or provider account recommended. US$0 inference; orchestration
cost unmetered. [Full retrieval outcomes](daily/2026-09-19.md), including failures.


## 2026-09-20 run scorecard

| Source group | Yield / uniqueness / timeliness | Reliability / cost / friction | Decision |
| --- | --- | --- | --- |
| HF exact model card + public provider mapping; Featherless exact model/docs | Unique changed Horizon managed access; incidental exact Qwen open route | High exact-ID metadata value, low GET cost; route launch date unknown. Context/plan mismatch and absent strict contract limit actionability | Add targeted daily access/contract follow-up, not broad model-feed scan; useful September20 |
| OpenRouter catalog | 446 entries; newest25 already known, misses HF-only Horizon route | Fast/low friction; high redundancy today, incomplete platform coverage | Keep core; pair held open checkpoints with HF provider mapping |
| OpenAI docs MCP, Anthropic, Google, xAI, DeepSeek | Existing models, platform/specialist updates; no retry repair | High primary verification value, low cost | Keep compact daily core |
| Qwen exact releases/model/structured-output docs | Existing Omni now owner-attempted; no new access | Schema page web error recovered by public GET; generic family schema cannot establish Omni contract | Keep targeted core and bounded fallback |
| Z.ai AutoClaw September20 post | Primary Ox Alpha identity corroboration, not new lead | Readable/timely article; older alias evidence already known | Keep compact primary check; do not promote article recency into checkpoint recency |
| Moonshot, MiniMax, Tencent | No new qualifying model; direct follow-up closes sparse search gaps | Forum/index and family-restricted searches incomplete; direct official pages recovered | Prefer exact current official model/update pages to broad search |
| Mistral, Meta, Inception | Known identities/specialists; no unique fresh yield | Readable, low cost, redundant | Retain compact checks/rotating depth |
| Artificial Analysis releases | No unique new release; evaluation/index activity | Useful breadth, redundant today | Rotate Arena next; no retirement |

No new provider account recommended. HF pass-through billing provides an
alternative to Featherless's direct subscription, but account access/strict
contract and exact route limits remain unverified. No inference; search and
orchestration currency cost unmetered. [Full retrieval audit](daily/2026-09-20.md).


## 2026-09-21 run scorecard

| Source group | Yield / uniqueness / timeliness | Reliability / cost / friction | Decision |
| --- | --- | --- | --- |
| OpenAI MCP, Anthropic, Google, xAI, DeepSeek | Known IDs/platform/specialist updates; zero qualifying yield | Primary high verification value; DeepSeek web error recovered with one public GET | Keep compact daily core |
| Qwen releases | Timely September20 duplex speech release; no maintained general-purpose fit | Low friction, exact release ID; Omni already attempted | Keep core; suppress unchanged Omni |
| OpenRouter | 446 entries, newest25 known, no Horizon/Omni/Agnes | Fast public metadata; redundant, incomplete platform coverage | Keep daily; pair held open checkpoint with HF |
| Horizon exact Featherless/HF mapping and HF guides | No changed access/contract; exact mapping still live | Model page readable; completions web error then HTTP403; generic guides cannot prove exact contract | Keep narrow check; stop repeated failed fetches today |
| BigModel Flash/FlashX Markdown | Known variant, no strict retry evidence | Web failed; public GET HTTP200 recovered authoritative text | Keep bounded Markdown fallback |
| Mistral changelog + exact model cards | Prevented false new-release alert for September2025 Magistral | Yearless headings misleading; exact cards authoritative and low friction | Keep; require exact model dates before qualifying |
| Kimi, MiniMax, Tencent, Meta | Known IDs and specialist products; no unique new lead | Delegated primary reads successful | Keep compact coverage |
| Arena changelog | Known checkpoint/effort additions; zero unique qualifying lead | Low friction, redundant; ranking not release evidence | Rotate Artificial Analysis next |

Checked September21. No source retired or new account recommended. US$0 inference;
search/orchestration currency cost unmetered. [Full audit](daily/2026-09-21.md).


## 2026-09-22 run scorecard

| Source group | Yield / uniqueness / timeliness | Reliability / cost / friction | Decision |
| --- | --- | --- | --- |
| xAI release/model/schema docs | New September21 Grok4.7, distinct base verified | High primary value, low cost; router dated suffix differs from public launch | Keep daily core; useful September22 |
| Xiaomi creator HF cards + router endpoints | Two new qualifying MiMo identities; UltraSpeed variant separated | Creator cards readable, launch JS page thin; managed/open served equivalence unproven | Add targeted near-term Xiaomi cards; useful September22 |
| OpenRouter | 444 entries; three MiMo routes and Grok4.7 new | Fast public GET, unique access yield; no contract/callability proof | Keep daily core |
| OpenAI MCP, Anthropic, Google, DeepSeek | Known models/platform updates; no retry trigger | High verification quality, low friction | Keep compact core |
| Qwen / BigModel | New specialist Omni Realtime excluded; known GLM variants | Web errors recovered by one public GET each; no strict repair | Keep bounded fallback, no broadening |
| Kimi, Mistral, MiniMax, Inception | Known identities/specialists | MiniMax follow-up web error recovered GET; others readable | Keep compact/rotating depth |
| Meta / Tencent | No new verified lead, partial freshness | Meta events thin redirect/blog July; Tencent updates head June | Target current model pages next run, do not claim exhaustive coverage |
| HF Horizon mapping + Featherless | Unchanged exact live route; no contract clarification | Low friction, redundant today | Retain narrow held-candidate monitoring |
| Artificial Analysis | MiMo Pro corroborating discovery | Low friction, overlapping router; rankings not owner proof | Rotate Arena next |

No source retired. No new account recommended. US$0 inference; orchestration
currency cost unmetered. [Full audit](daily/2026-09-22.md).


## 2026-09-23 run scorecard

| Source group | Yield / timeliness / uniqueness | Quality / cost / friction | Decision |
| --- | --- | --- | --- |
| OpenAI Docs MCP + exact cards/pricing | Two current identities; broad catalog intro lagged | High primary value, low cost; Learn Markdown404 recovered web | Keep daily; pair catalog with exact cards |
| Anthropic releases/overview/schema | Unique September22 Opus5.5 verification | Exact page errors/403; independent official pages cover key facts | Keep core, bounded fallback |
| OpenRouter catalog/endpoints |456 entries; new models, CommandA+ access, Omni correction | High timely route yield, public GET cheap; variants and limits require care | Keep core, never treat metadata as inference |
| Cohere exact card/release | Verified older checkpoint behind new route | High identity value; context disagreement retained | Add narrow route-contract follow-up, no account recommendation |
| Google/xAI/DeepSeek/Qwen/GLM | Known models; no retry repair | Mostly readable; GLM recovered GET200 | Keep compact core; coordinator dedupe rejected stale delegated leads |
| Kimi/Mistral/MiniMax/Meta/Tencent | No fresh qualifying ID; Meta coverage recovered | Kimi extraction partial; Tencent legacy migration makes coverage incomplete | Retain; target TokenHub next run |
| Xiaomi prior owner route evidence | September22 campaign now dedupe authority | No unchanged capacity probe warranted | Retain targeted monitoring, no automatic retry |
| Horizon/Inception | Unchanged holds; Mercury price not semantic repair | Low cost, redundant | Keep narrow rotation |
| Aion/Upstage creator pages | Prevented unsupported exact-ID alerts | Missing exact creator confirmation | Hold leads; no daily-feed promotion |
| Arena then Artificial Analysis | Arena failed; AA corroborates Opus | Two bounded web failures, fallback readable; ranking not owner proof | Use AA next, retry Arena on rotation |

No sources retired. No accounts, inference or owner edits. [Audit](daily/2026-09-23.md).


## 2026-09-24 run scorecard

| Source group | Yield / uniqueness / timeliness | Quality / cost / friction | Decision |
| --- | --- | --- | --- |
| OpenAI MCP/exact cards; Anthropic/Google/xAI | Existing IDs; zero new qualifying yield | High primary value, low friction; broad OpenAI intro still lags | Keep compact core |
| DeepSeek | Existing V4.1 | Web error recovered one public GET200 | Keep bounded fallback |
| OpenRouter catalog/endpoints |458 entries; four new observed IDs, none qualified | Timely route discovery, low cost; metadata-only limitations decisive | Keep daily core |
| Fireworks creator announcement/card | Verified derivative exclusion | Exact search recovered broad-query noise; readable primary evidence | Targeted only, no feed promotion |
| Alibaba Prime docs/pricing | Verified serving-mode distinction | High identity/contract value; no measured latency repair | One narrow follow-up, no retry alert |
| AutoClaw Flash article | Existing Ox Alpha alias, newly displayed date | Prevented false-new delegated recommendation; release-date drift | Keep alias checks, never use page date alone |
| Qwen/Kimi/Z.ai/Mistral/MiniMax | Known or specialist/product entries | Kimi API freshness limited; exact Mistral card prevents year error | Retain compact core |
| Tencent TokenHub dynamics | Fresh September23 page with known coverage | More timely than legacy index; no unique checkpoint | Prefer current TokenHub source |
| Meta | Thin home redirect | Fresh model coverage incomplete | Recover Muse-specific page next run |
| Inception/Horizon/Cohere | Existing holds and context discrepancy | Readable, redundant; no contract repair | Keep narrow rotation |
| Artificial Analysis / community exact-ID search | No additional qualifying lead | AA readable; Space Bunny identity speculation unsupported | Rotate Arena; avoid broad fingerprint feeds |

Checked September24; no retirement or new account recommendation. US$0 inference,
search/orchestration cost unmetered. [Full audit](daily/2026-09-24.md).


## 2026-09-25 run scorecard

| Source group | Yield / uniqueness / timeliness | Quality / cost / friction | Decision |
| --- | --- | --- | --- |
| OpenAI Docs MCP; Anthropic/Google/xAI | Known checkpoints; no qualifying new yield | Low friction, strong exact-ID evidence; billing/product updates excluded | Keep compact core |
| DeepSeek | Known V4.1 and V4 Pro continuation | Web error recovered by one GET200 | Keep bounded fallback |
| OpenRouter |458 entries, newest30 known | Low cost, useful coverage/dedupe; no identity or contract proof | Keep daily core |
| Qwen direct changelog/card/API | Unique specialist decision-model-preview discovery | Primary current source; delegated slice missed newest entry, coordinator caught it | Keep direct core; narrow later provenance check, no frontier alert |
| Kimi/Tencent | Existing K2.8/known model routes | Fresh coding/TokenHub docs outperform stale blog; candidate ledger prevented false-new result | Keep compact exact-ID checks |
| Z.ai/Mistral/MiniMax | Known models, specialists and product changes | Readable, redundant, no unique qualifying yield | Retain compact coverage |
| Meta research index/exact card | Recovered current coverage, known Spark1.3 | Muse URL failed; official research domain readable and dated | Prefer research index over failing/thin paths |
| Prime/Horizon/Inception | Existing holds; Mercury promotional rate observation | Useful monitoring, no measured retry repair | Keep narrow rotation, no repeated alert |
| Arena text leaderboard | No unique qualifying lead | Readable but redundant effort variants, no owner evidence | Rotate Artificial Analysis next |

Checked September25. No source retired or new account justified. US$0 inference;
search/orchestration currency cost unmetered. [Full audit](daily/2026-09-25.md).


## 2026-09-26 run scorecard

| Source group | Yield / uniqueness / timeliness | Verification / friction / cost | Decision |
| --- | --- | --- | --- |
| Official OpenAI/Anthropic/Google/xAI/DeepSeek | Known identities; zero new qualifying yield | Strong primary evidence, low friction; DeepSeek directly readable | Keep compact daily core |
| Qwen/Kimi/Z.ai/Mistral/MiniMax | Known/specialist/product releases | Delegated bounded pass, dated identity checks prevent repeats | Retain compact coverage |
| Tencent TokenHub/Meta research | Current known routes/Spark1.3 | Readable, redundant, low cost | Keep current sources |
| OpenRouter public catalog/endpoints |458 entries but two new observed IDs; Perceptron useful, Jev wrapper excluded | Cheap GET; count alone conceals identity changes | Keep core, inspect IDs |
| Perceptron creator/docs/privacy | Unique new visual candidate and strict-function caveat | Web exact-doc failures recovered GET200; primary card more precise than launch shorthand | Add targeted contract/card check, no broad feed |
| Artificial Analysis releases | Unique Step5 discovery beyond router coverage | Low friction; catalog dates/ranks not primary proof | Keep rotation; Arena next |
| StepFun exact international guide/pricing | Primary ID/limits/prices recovered via flagship link | Search-only/delegated pass missed exact guide; direct link high value | Add targeted guide and strict/privacy follow-up |
| Vercel exact Step5 route | Established alternative listing absent OpenRouter | Useful access metadata; output ceiling conflicts with creator | Add targeted route cross-check; no account recommendation |
| Horizon/Inception | Holds unchanged | Readable, redundant, no retry evidence | Keep narrow rotation |

Checked September26. No source retired. US$0 inference; orchestration currency
cost unmetered. [Full audit](daily/2026-09-26.md).


## 2026-09-27 run scorecard

| Source group | Yield / uniqueness / timeliness | Verification / friction / cost | Decision |
| --- | --- | --- | --- |
| OpenAI Docs / Anthropic / Google / xAI | Existing exact identities; zero new qualifying yield | Primary, low friction | Keep compact core |
| DeepSeek | Existing V4.1 and Pro continuation | Web failure recovered with one GET200 | Keep bounded fallback |
| Qwen / Kimi / GLM / Mistral / MiniMax | Existing models and specialists | Some failed indexes; exact official fallback succeeded | Keep compact coverage, avoid speculative results |
| OpenRouter catalog and exact endpoint |458 entries; unique Qwen Omni access correction | Cheap GET, no contract/served-identity proof | Keep daily; revisit held route IDs, not only counts |
| StepFun / Vercel / Perceptron | No new candidate; preserved limit/contract caveats | Two web errors recovered GET200; useful exact docs | Keep targeted follow-up |
| Tencent / Meta / Horizon / Inception | Known routes/identities and unchanged promotion | Readable, redundant, no retry proof | Retain narrow checks |
| Arena text | No unique qualifying lead; known effort variants | Readable, low friction, no owner evidence | Rotate Artificial Analysis next |

Checked September27. No source retired; no material strategy change or account
recommendation. US$0 inference; orchestration currency cost unmetered.
[Full audit](daily/2026-09-27.md).


## 2026-09-28 run scorecard

| Source group | Yield / timeliness / uniqueness | Verification / friction / cost | Decision |
| --- | --- | --- | --- |
| OpenAI Docs / Anthropic / Google / xAI | Existing exact identities, zero new qualifying yield | Primary, low friction; full catalog better than intro | Keep compact core |
| DeepSeek / Perceptron schema | Known identities/contracts | Web errors recovered by one GET200 each | Keep bounded fallback |
| Qwen / Kimi / GLM / Mistral / MiniMax | Known models, specialists and product updates | Official fallback pages readable; guessed Moonshot/Mistral paths failed | Keep compact core; prefer linked canonical pages |
| OpenRouter |458 entries; newest35 known | Cheap public GET, redundant today; no inference proof | Keep core; inspect exact identities |
| StepFun model/JSON guide / Vercel / privacy | Unique recovery of exact strict-schema documentation; not a new model | Linked guide succeeds after prior guessed-path failures; output conflict persists | Add exact guide pointer; no repeated candidate alert |
| Tencent / Meta / Horizon / Inception | Known identities and unchanged holds | Readable, low cost, no retry evidence | Retain narrow monitoring |
| Artificial Analysis models/releases / exact searches | No qualifying new lead; generic FAQ/search noise | Canonical releases page readable; guessed new-releases failed | Keep release view in rotation; Arena next |
| Agnes / Cohere creator cards | Existing preview distinction and small coding model | Primary identity checks useful, no new relevant access proof | Targeted only, no broad feed promotion |

Checked September28; no retirement, material strategy change or account
recommendation. US$0 inference; orchestration currency cost unmetered.
[Full retrieval and qualification audit](daily/2026-09-28.md).


## 2026-09-29 run scorecard

| Source group | Yield / timeliness / uniqueness | Verification / friction / cost | Decision |
| --- | --- | --- | --- |
| Anthropic release/card + owner ledger | Timely Sonnet5.5 launch, already attempted | High primary identity value; current ledger prevents duplicate recommendation | Keep compact core |
| OpenRouter catalog/exact endpoints |460 entries; two Sonnet route variants, no new unevaluated checkpoint | Cheap public GET; useful access metadata, not served identity or retry proof | Keep daily exact-ID checks |
| OpenAI Docs / Google / xAI / Tencent / Meta | Known IDs and platform changes | Readable, low friction, redundant today | Keep compact core |
| DeepSeek / Perceptron schema | Existing model/contract caveats | Web failures recovered one GET200 each | Keep bounded fallback |
| Qwen / Kimi / GLM / Mistral / MiniMax | Known models, specialists, product/news updates | Kimi blogs lag coding pages; AutoClaw article date drift risks false freshness | Keep canonical current pages and exact-ID dedupe |
| StepFun / Vercel / Horizon / Inception | Existing candidates, no new actionable evidence | Readable, low cost, no unique yield | Narrow monitoring only |
| Arena text | September25 snapshot; no unique lead | Readable but stale/redundant; rankings not owner proof | Rotate Artificial Analysis releases next |

Checked September29. No source retirement, material strategy change or provider
account recommendation. US$0 inference; orchestration currency cost unmetered.
[Full audit](daily/2026-09-29.md).


## 2026-09-30 run scorecard

| Source group | Yield / uniqueness / timeliness | Reliability / cost or friction | Decision |
| --- | --- | --- | --- |
| OpenAI exact Docs MCP/card + Anthropic/Google/xAI/DeepSeek | Sol6.1 fresh metadata, other known IDs; zero new qualifying yield | Primary, low friction; current owner ledger prevents duplicates | Keep daily core |
| Qwen/Kimi/Z.ai/MiniMax | Known models and specialist updates | Bounded lower-cost read-only pass, explicit dates | Keep compact coverage |
| Mistral canonical changelog/news | Newly observed September28 GLM5.3 hosting metadata | Useful route distinction; no callability/contract repair proof | Keep exact /resources/changelogs pointer |
| Tencent/Meta | Known routes and Spark1.3 | Readable, redundant, low friction | Retain compact check |
| OpenRouter catalog + Sol endpoints |464 entries; four newest Sol6.1 variants, not new owner candidates | Cheap public GET, exact IDs and descriptions essential | Keep core; no new account |
| StepFun/Vercel/Perceptron | Existing limits/strict-function caveats unchanged | Perceptron web error recovered GET200; medium friction | Suppress unchanged alerts |
| Artificial Analysis releases | Current Sol6.1/Sonnet5.5 but no unique qualifying yield | Low cost, redundant; rankings not owner evidence | Rotate Arena next |

All above last checked September30. No source retired or material strategy
change. See [daily report](daily/2026-09-30.md) for exact retrieval and decisions.


## 2026-10-01 run scorecard

| Source group | Yield / uniqueness / timeliness | Verification / friction / cost | Decision |
| --- | --- | --- | --- |
| Arena text + Google official announcement | Unique new Argon lead, September30 announcement; API changelog did not expose it | High primary verification after secondary discovery; low friction, access gated | Keep Arena rotation; add compact Google/DeepMind announcement check alongside API docs |
| OpenAI Docs MCP + other ten-provider core | Known IDs, specialist/hosting/retirement updates; no other qualifying lead | Readable public sources, bounded lower-cost agent scan; metadata not retry evidence | Keep compact core |
| OpenRouter |462 entries; newest35 known, no Argon route | Cheap unauthenticated GET; exact-ID inspection essential | Keep daily core |
| StepFun / Horizon / Inception / Perceptron | Existing candidates and holds | Perceptron web failure recovered GET200; no live contract evidence | Keep narrow follow-up, suppress unchanged alerts |
| Meta / Tencent | No additional qualifying lead | Readable but compact index coverage, no exhaustive claim | Retain compact monitoring |

Checked October1; no sources retired. Arena's useful discovery justifies retaining
rotation after earlier redundancy. Next secondary slice: Artificial Analysis.
US$0 inference; search/orchestration currency cost unmetered. [Full audit](daily/2026-10-01.md).


## 2026-10-02 run scorecard

| Source group | Yield / uniqueness / timeliness | Verification / friction / cost | Decision |
| --- | --- | --- | --- |
| OpenAI Docs MCP and ten-provider official core | Known models, existing gates; no new qualifying lead | Primary, low friction; current ledger catches October2 owner work | Keep compact core |
| Google announcement + API catalog/changelog | Argon still gated, no exact API slug established | Primary; search also returned irrelevant community material | Keep paired announcement/API checks; suppress unchanged alerts |
| OpenRouter catalog |464 entries; two newly observed derivative/composite routes | Cheap public GET; exact IDs more useful than count | Keep daily access discovery |
| Apodex creator card/docs; Unbiased announcement/overview | Unique provenance resolves both exclusions | Primary low-cost checks; raw HF error unnecessary to retry | Targeted only; no broad provider promotion |
| Meta/Tencent/Xiaomi/Cohere | Known identities/routes, no unique lead | Readable compact coverage; no callability or retry proof | Retain bounded monitoring |
| StepFun/Horizon/Inception/Perceptron | Prior candidates unchanged | Perceptron web error recovered one GET200 | Keep narrow follow-up, no repeated alerts |
| Artificial Analysis releases | Existing Argon/Sol/Sonnet and September models | Readable, redundant today; rankings not owner proof | Rotate Arena next |

Checked October2. No material strategy change, source retirement or new-account
recommendation. US$0 inference; orchestration currency cost unmetered.
[Full retrieval and qualification audit](daily/2026-10-02.md).


## 2026-10-03 run scorecard

| Source group | Yield / uniqueness / timeliness | Verification / friction / cost | Decision |
| --- | --- | --- | --- |
| OpenAI Docs MCP and official core | Known checkpoints; no satisfied retry trigger | Low-cost compact public checks; DeepSeek web error recovered GET200 | Keep daily core |
| OpenRouter exact catalog/endpoints |466 entries; new Ling3.1 access route, no LongCat2.5/M3.1/Argon | Cheap public GET; cannot prove creator provenance or strict contracts | Keep daily core |
| Vercel/Novita Ling launch and API pages | Earlier September30 access notice; promotion boundaries useful | Serving-platform primary evidence; creator repo/HF/X verification incomplete, search redundancy high | Keep rotating access source; narrow creator follow-up |
| TechNode and incidental community leads | Unique LongCat2.5 and MiniMaxM3.1 discovery prompts | Not claim authorities; recovered creator/API evidence for both | Retain small secondary rotation, require primary verification |
| LongCat creator changelog/API/pricing | Unique September25 preview and exact direct API; first seen October3 | Low friction, strong identity evidence; strict/privacy gaps | Add targeted next-run access/contract check |
| MiniMax API model index and tool guide | Unique restrictedM3.1 identity missed by broad blog | Explicit M Plan/Code-only access; plan/app rendering incomplete | Pair exact model index with blog; suppress unchanged preview |
| Arena / Meta / Xiaomi | No unique qualifying yield | Readable compact views, redundant today | Rotate AA next |
| Tencent TokenHub | No reliable finding | Web error; fallback compressed response decode failure | Next check gzip-aware public retrieval |

Checked October3. No sources retired, no accounts recommended. Search/orchestration
currency cost unmetered, inferenceUSD0. [Full audit](daily/2026-10-03.md).


## 2026-10-04 run scorecard

| Source group | Yield / timeliness / uniqueness | Verification / friction / cost | Decision |
| --- | --- | --- | --- |
| OpenAI Docs MCP and official provider core | Known identities; zero new qualifying yield | Strong primary identity evidence, compact checks; sparse Z.ai blogs recovered exact card | Keep core; prefer exact cards over empty blogs |
| MiniMax model index / LongCat changelog and API | Prior previews unchanged | Low friction; contract/access gaps still explicit | Keep narrow monitoring, suppress duplicate alerts |
| OpenRouter |466 entries, newest40 known; no new held-family route | Cheap public GET; exact IDs avoid count-only inference | Keep daily access discovery |
| Tencent TokenHub | Recovered known route coverage | Gzip-aware GET200 and cleaned HTML repair prior decode failure | Keep canonical page and robust decoding |
| DeepSeek | Known V4.1 / Pro continuation | Web error recovered one public GET200 | Keep bounded fallback |
| Meta / Xiaomi | Existing identities only | Readable compact indexes, redundant | Retain bounded checks |
| Artificial Analysis / Ling creator search | No qualifying lead; secondary1M/open-weight metadata unresolved | AA readable; exact creator search noisy, repository lacks3.1 match | Rotate Arena next; do not promote secondary claims |
| Mistral | Known GLM hosting/lifecycle metadata | Prior daily reconciliation prevents false-new delegated finding | Keep exact-ID/date dedupe |

Checked October4. No source retired or material strategy change. US$0 inference;
search/orchestration currency cost unmetered. [Full audit](daily/2026-10-04.md).


## 2026-10-05 run scorecard

| Source group | Yield / timeliness / uniqueness | Verification / friction / cost | Decision |
| --- | --- | --- | --- |
| Official OpenAI/Anthropic/Google/xAI core | Known checkpoints; zero new qualifying yield | Primary low-cost reads; exact ledger prevents duplicate proposals | Keep compact daily core |
| Qwen/Kimi/Z.ai/Mistral/MiniMax | Known identities, specialists and restricted preview | Five-source delegated pass succeeded; GLM owner history retains both access and latency stops | Keep exact cards/indexes; no new account |
| OpenRouter |466 entries; newest40 and held-family checks known | Cheap GET; exact IDs prevent count-only inference | Keep daily access metadata check |
| LongCat/Google Argon/MiniMax | Existing previews/access holds | Primary verification, no newly actionable evidence | Narrow follow-up; suppress repeats |
| DeepSeek/Tencent | Known releases/routes | One DeepSeek web failure recovered GET200; Tencent gzip-aware GET200 | Keep bounded fallbacks |
| Meta/Xiaomi | Known identities only | Readable compact indexes; no exhaustive freshness claim | Retain compact checks |
| Arena text | October2 snapshot, no unique lead | Readable, redundant; effort/rank/price metadata not owner proof | Rotate Artificial Analysis next |
| Ling creator repo/search | No primary3.1 identity confirmation | Repository readable; search dominated by route mirrors | Keep narrow provenance check; do not promote secondary claims |

Checked October5. No material strategy change or source retirement. US$0 inference;
search/orchestration currency cost unmetered. [Full audit](daily/2026-10-05.md).


## 2026-10-06 run scorecard

| Source | Yield / verification / timeliness | Cost / friction / decision |
| --- | --- | --- |
| Mistral model and news indexes / exact card | Unique Large4 launch primary confirmation today; changelog still September29, official-domain search empty | Low-cost direct reads; promote paired index/card checks alongside changelog |
| OpenRouter catalog / endpoints |465 entries, new exact Large4 dated route; public route limits/prices distinct from creator card | Cheap GET; human page web error recovered metadata; keep daily exact-ID core |
| Other official provider core / prior previews | Known identities and holds; no satisfied retry trigger | Compact readable checks; DeepSeek bounded fallback; keep core |
| Artificial Analysis | No additional verified unique lead; dynamic values incomplete | Redundant today; rotate Arena next |
| Meta / Xiaomi | Known-provider index coverage only | Retain bounded rotation; no exhaustive freshness claim |

Checked October6. No retirement or account recommendation. InferenceUSD0; orchestration currency cost unmetered. [Full audit](daily/2026-10-06.md).


## 2026-10-07 run scorecard

| Source group | Yield / uniqueness / verification | Cost / friction / decision |
| --- | --- | --- |
| Official provider core and exact preview pages | Known models; Large4 now deduped to completed owner work; no new qualifying yield | Low-friction public reads; keep compact primary core and paired Mistral indexes |
| OpenRouter public catalog |465 entries, newest40 known or excluded specialist; exact dated identities inspected | Cheap GET200; keep access metadata core, never infer callability/strictness |
| Arena text | Existing Argon/known families; no unique primary-verified lead | Readable, redundant today; rotate Artificial Analysis releases next |
| Kimi/Z.ai targeted search | No new primary-confirmed lead; Moonshot community noise | Prefer index/exact cards; retain bounded search only when needed |
| Ling creator / Meta / Xiaomi | No new verified lead; Ling3.1 provenance unresolved, Meta sparse extraction | Keep narrow monitoring; no promotion from missing evidence |

Checked October7. No source retired or material strategy change. USD0 inference; orchestration cost unmetered. [Full audit](daily/2026-10-07.md).


## 2026-10-08 run scorecard

| Source group | Yield / uniqueness / timeliness | Verification / friction / cost | Decision |
| --- | --- | --- | --- |
| Primary OpenAI/Anthropic/Google/xAI/DeepSeek/Qwen | Haiku launch already evaluated; other known identities, no retry proof | High primary verification; DeepSeek web error recovered one public GET200 | Keep compact daily core and ledger-first dedupe |
| OpenRouter catalog/exact Step5 endpoint |468 entries; unique new route observation, no new checkpoint | GET200 low friction; landing-page web error; strictness/served identity unproven | Keep exact endpoints; useful access metadata October8 |
| Kimi/Z.ai/Mistral/MiniMax/LongCat and creator follow-ups | Known releases and unchanged preview/provenance holds | Readable compact indexes, uneven freshness; AutoClaw date drift remains | Keep narrow checks; no expanded accounts |
| Artificial Analysis releases | Known Haiku/Large4/Ling, zero unique qualified leads | Low friction, redundant today; secondary metadata only | Rotate Arena next |

USD0 inference; search/orchestration currency cost unmetered. No material strategy change or retirement. Full retrieval limitations and dispositions in [daily audit](daily/2026-10-08.md).


## 2026-10-09 run scorecard

| Source group | Yield / verification / cost | Decision |
| --- | --- | --- |
| Primary provider core | Readable known identities; zero unique qualified leads; high verification, low public retrieval friction | Keep compact daily core and ledger-first dedupe |
| OpenRouter catalog | GET200,469 entries; newest30 already recorded; count churn has no checkpoint value | Keep exact IDs; no promotion from count or route metadata |
| Preview/creator follow-ups | Unchanged Argon/MiniMax/LongCat holds; Ling3.1 creator provenance unresolved | Keep narrow checks; no account recommendation |
| Arena / AA rotation | Arena internal error; AA readable redundant fallback, zero unique verified leads | Retry/rotate Arena; do not retire from one failure |
| DeepSeek updates | Web internal error recovered by public GET200; current September10 evidence | Keep one bounded HTTP fallback |

USD0 inference; orchestration/search currency cost unmetered. No material strategy change. [Full audit](daily/2026-10-09.md).


## 2026-10-10 run scorecard

| Source group | Yield / verification / timeliness / friction | Decision |
| --- | --- | --- |
| First-party core | Zero unique qualifying identities; readable exact catalogs/notes, high verification, low public cost; Google redirect correction and Inception pricing monitoring | Keep compact daily core; metadata does not repair owner gates |
| OpenRouter | GET200,458 entries; newest35 known. Count varies from prior469; no new checkpoint established | Keep exact identity inspection; do not classify change from count alone |
| Preview/creator follow-ups | Argon/MiniMax/LongCat unchanged; Ling3.1 provenance unresolved | Keep narrow checks; no account recommendation |
| Arena | Recovered prior error; known launches/rankings only, zero unique verified leads | Keep rotation; Artificial Analysis next |
| DeepSeek | Web readable without fallback today; known September10 release | Keep core and one fallback only if needed |
| Tencent/Meta targeted search | Existing indexed releases, Tencent crawl lag; low unique yield | Retain rotating depth; no promotion from freshness or non-results |

USD0 inference; search/orchestration currency cost unmetered. No material strategy change. [Full audit](daily/2026-10-10.md).


## 2026-10-11 run scorecard

| Source group | Yield / verification / timeliness / friction | Decision |
| --- | --- | --- |
| First-party core | Zero unique qualifying identities; readable known catalogs/notes, high verification, low public cost | Keep compact daily core; no retry from metadata |
| QwenCloud / Qwen blog | October9 image Turbo specialist excluded; notes readable, blog zero lines, indexed search redundant | Keep direct notes as priority; no promotion from specialist churn |
| Kimi / StepFun | Intro/wrong guide path inaccessible; official research/exact guide recovered known candidates | Keep exact documented pointers; entry-point failures do not mean model absence |
| OpenRouter | GET200,458 entries, newest35 known; no newly actionable held-preview route | Keep exact identity inspection; count is not change detection |
| Preview / creator follow-ups | Argon/MiniMax/LongCat holds unchanged; Ling3.1 provenance unresolved | Keep narrow checks; no new account recommendation |
| Artificial Analysis | Readable, known Haiku/Large4/Ling; zero unique verified lead, redundant ranking variants | Keep alternating rotation; Arena next |

USD0 inference; search/orchestration currency cost unmetered. No material strategy change. [Full audit](daily/2026-10-11.md).


## 2026-10-12 run scorecard

| Source group | Yield / verification / timeliness / friction | Decision |
| --- | --- | --- |
| First-party core | Zero unique qualifying identities; known catalogs/notes, high verification, low public retrieval cost | Keep compact daily core; no retry from metadata |
| Preview / creator checks | Argon/MiniMax/LongCat unchanged; Ling3.1 provenance still unresolved; exact Step5 guide readable | Keep narrow checks; no expanded accounts |
| OpenRouter generation catalog | GET200,458 entries; newest35 known; native Decisions coverage separate | Keep exact IDs and endpoint-family distinction; count/omission is not access proof |
| Arena text | Readable October8 snapshot; known identities, zero unique verified lead, redundant today | Rotate Artificial Analysis releases next |
| Tencent / Xiaomi / Inception | Direct readable known coverage; no repair evidence for owner gates | Retain bounded rotating depth; no promotion or retirement |

USD0 inference; search/orchestration currency cost unmetered. No material strategy change. [Full audit](daily/2026-10-12.md).


## 2026-10-12 — owner-requested decision-source coverage

Promote TypeSafe/JEV, OpenAI Decisions, Microsoft Foundry Decision, Perplexity Decisions/creator cards, Qwen decision API and OpenRouter's decision catalog to a compact daily core. Reason: Cam explicitly expanded scope; Microsoft was previously owner-nominated and the generation-only catalog omits native decision coverage. Historical owner scouts provide contract pointers, not measured discovery yield for this new core. Yield, timeliness, uniqueness and retrieval cost remain to be measured on subsequent runs; do not invent a successful check today. Public docs/catalogs only, no inference. Retain general-purpose rotation; dedupe both categories against evaluated-models.md.


## 2026-10-13 run scorecard

| Source group | Yield / verification / friction | Decision |
| --- | --- | --- |
| OpenRouter decision catalog |22 entries; uniquely exposed five verified creator families, generation catalog omits them; low-cost public metadata | Keep daily; creator contracts mandatory, metadata not quality |
| TypeSafe/OpenAI/Microsoft/Perplexity/Qwen native core | Readable existing identities, no justified repeat; high verification, redundant discovery today | Keep compact daily coverage |
| Cloudflare/Nace/Liquid/ScaleDown/Upstage | Creator-confirmed IDs and material modality/fallback/state/billing differences; ScaleDown/Hub web failures recovered GET200 | Add bounded creator rotation; avoid universal wrapper parity assumptions |
| General-purpose first-party core / AA releases | No unique qualifying release; public retrieval readable and redundant | Keep primary core; Arena next secondary rotation |

USD0 inference; search/orchestration currency cost unmetered. First complete expanded-category run demonstrates value of separate native catalog. [Full audit](daily/2026-10-13.md).


## 2026-10-14 run scorecard

| Source group | Yield / verification / timeliness / friction | Decision |
| --- | --- | --- |
| Meta creator/model/API docs | One frontier family newly primary-qualified; yesterday's catalog narrative missed it. High verification, readable, low public cost | Promote near-term direct model/availability check; explicit correction, not new release date |
| OpenRouter separate catalogs |462 generation/22 decision entries; no added decision ID, useful access and modality/price deltas, metadata only | Keep daily exact-ID comparison; catalog count/newest-known summaries insufficient |
| Native decision core | Existing JEV/Luna/Microsoft/Decider and held Qwen, redundant discovery but important dedupe | Keep compact daily; no retry from documentation |
| AutoTrust creator card/public Hub API | New deferred decision family, exact alias and deployment limits verified; incidental noisy search discovery | Add bounded creator follow-up; no broad Hub churn or GPU/account setup |
| Inception/Upstage creator follow-ups | Guessed Inception page error/index403, search noisy; Upstage readable but no Flash identity | Retain hold; use documented pointers next run, no repeated guesses |
| Other first-party general core / Arena | Known releases; Arena corroborates Wonder but effort labels are not model IDs | Keep primary core; AA next secondary rotation |

USD0 inference; search/orchestration currency cost unmetered. [Run audit](daily/2026-10-14.md). No model evaluation, target changes, account setup or adoption.


## 2026-10-15 run scorecard

| Source group | Yield / verification / friction | Decision |
| --- | --- | --- |
| Together and Respan creator sources | Two existing metadata-only families primary-qualified; exact native contracts differ materially from router/general catalog. Readable, public, low retrieval cost | Promote bounded creator rotation; no quality inference from vendor scores |
| OpenRouter separate catalogs |461 generation/newest40,23 decisions; Jev1.14 and Perplexity alias changes already evaluated. Useful access/identity metadata, redundant quality evidence | Keep daily exact-ID/sample-width-aware comparisons |
| Native decision and general first-party core | Known releases; no retry trigger. DeepSeek web error recovered one public GET200 | Keep compact core and one fallback; suppress owner-closed checkpoint |
| Artificial Analysis | Readable known models/effort variants; zero unique qualifying lead | Rotate Arena next; no source retirement warranted |
| Inception/Qwen targeted search | No useful new verification; noisy/redundant | Retain existing holds, no repeated guessed endpoints |

USD0 inference; search/orchestration currency cost unmetered. [Full audit](daily/2026-10-15.md).


## 2026-10-16 run scorecard

| Source | Yield / verification / friction | Decision |
| --- | --- | --- |
| Separate router catalogs |465 general/25 decision entries; two new typed models, NVIDIA general release and Meta identity/access lead. Public low-cost exact deltas, metadata only | Keep daily equal-width ID comparison |
| Liquid/Respan creator | October15 new decision checkpoints, exact native contracts; Liquid guessed docs/line-open errors, Respan successor now resolves | Promote near-term creator release checks; use linked paths, preserve historical redirect |
| NVIDIA/Meta creator | Timely new open multimodal releases, direct architecture/access evidence; Spark predecessor equivalence unresolved | Add bounded creator follow-up, no weights download or signup |
| Core official sources | Existing attempts/holds; Anthropic fast-mode GA metadata does not repair owner quality gates | Keep compact daily; no unchanged retries |
| Arena | Readable secondary slice, no unique additional primary-qualified lead | Rotate AA next; no retirement warranted |

USD0 inference; retrieval/orchestration unmetered. [Audit](daily/2026-10-16.md).


## 2026-10-17 run scorecard

| Source group | Yield / uniqueness / timeliness | Reliability / cost/friction | Decision |
| --- | --- | --- | --- |
| OpenRouter separate generation/decision catalogs and exact endpoints | Four new qualified checkpoints; alias does not add a model; equal-width delta also exposed excluded fine-tune/small churn | Six public GETs200, cheap; endpoint prices/precision differ substantially from model default; no callability/quality proof | Keep daily and pin endpoint before proposal |
| Perplexity native changelog/quickstart/API plus creator card | Unique new1.2/Flash checkpoint and dangerous old-name redirect; joint-question dependence verified | Native readable; guessed cards failed,27B actual card recovered; local/private-repo and hosted contracts differ | Promote quickstart/changelog pairing; last useful October17 |
| DeepSeek exact model/pricing table | Exact1017 successor versus stale changelog and closed predecessor | Direct pricing readable; announcement/card opens failed despite official indexed launch | Keep exact-table daily; no retry based only on metadata |
| Reflection creator model card/quickstart/weights | New family/current API verified; dated October5 announcement differs from October16 access docs | Readable first party, low friction; no native price/privacy or actual strict proof | Add rotating creator follow-up, no new account recommendation |
| Artificial Analysis releases | Beam corroboration, zero additional qualified checkpoint | Low cost, redundant with router today; scores not owner evidence | Keep rotation; Arena next |
| Other general/decision core, StepFun/LongCat/Meta | Existing evaluated models and unchanged holds, no justified repeat | Public documentation readable, low marginal cost | Keep compact daily core; suppress unchanged nominations |
| Elorian creator | Verified fine-tune provenance excludes Glimpse under general-purpose rule | Strong direct evidence, no need for deeper API/privacy research today | Retain excluded discovery record, do not promote source |

No source retired from one low-yield day. Public-only inference spendUSD0; orchestration unmetered. Full endpoints/failures and dates: [daily audit](daily/2026-10-17.md).


## 2026-10-20 run scorecard

| Source group | Yield / uniqueness / timeliness | Reliability / friction | Decision |
| --- | --- | --- | --- |
| Separate router generation/decision catalogs | Mercury3/MiniMaxGA discovery;27decision IDs unchanged | Public GET200; full snapshot inexpensive, MiniMax listing has empty endpoints | Keep daily; exact endpoint before route claims |
| Inception launch/model index/linked Decisions docs | October19 Mercury3 and unique qualification of prior Decide hold | High primary verification; guessed/.md paths fail, extensionless linked pages recover; privacy unavailable | Promote compact near-term native Decisions follow-up; last useful October20 |
| MiniMax creator blog/redirected guide/API reference | October19 GA/access and preview/SpaceBunny identity evidence | Direct low friction; no hosted immutable attestation; vendor gains unmeasured | Keep daily direct creator release checks; no signup |
| Other official general/decision core | Existing checkpoints/holds; no new retry proof | Readable public documentation; metadata not owner results | Keep compact; no promotion from unchanged metadata |
| Arena | No unique primary-qualified lead | Low friction/redundant today | Rotate AA next; no retirement on one low-yield day |

USD0 inference; retrieval/orchestration unmetered. [Attempted sources, failures and decisions](daily/2026-10-20.md). No scope/cadence or automation configuration change.


## 2026-10-21 run scorecard

| Source group | Yield / verification / uniqueness | Cost / friction | Decision |
| --- | --- | --- | --- |
| Separate router catalogs/exact endpoints |468 general/27 decisions, zero exact-ID additions/deletions; MiniMax public endpoint/owner-evidence discrepancy preserved | Web readable; sandbox DNS failed, one network-enabled public GET recovery succeeded; no inference | Keep daily, do not equate endpoint listing with actual owner access |
| General and decision official daily core | Existing identities and configuration updates only; no demonstrated retry gate | Mostly readable; Qwen blog empty, Foundry banner with readable body; inexpensive public metadata | Keep compact core; no unchanged nominations |
| Inception/Meta follow-up | Mercury3/Decide known; Spark Open lineage equivalence unresolved | Readable, no unique new lead | Retain holds, no account recommendation |
| Liquid/Respan/HF creator rotation | Known checkpoints only; exact saved links more reliable than guesses | Guessed paths failed; known Respan paths recovered, Liquid launch still unavailable | Keep linked creator rotation; no source promotion/retirement |
| Artificial Analysis releases | Zero unique primary-qualified lead; known October identities | Low friction, redundant today | Rotate Arena next |

Inference USD0; retrieval/orchestration unmetered. [Full attempted-source audit](daily/2026-10-21.md). No automation configuration change.


## 2026-10-22 source assessment

| Source | Yield / uniqueness | Reliability / friction / cost | Decision |
| --- | --- | --- | --- |
| Separate OpenRouter decision catalog | Three unique primary-qualified new checkpoints; general468 count concealed churn | Public GET200,30decision entries; empty Baseten endpoints limit access evidence; no inference | Keep daily full-ID deltas |
| Baseten creator launch/library/native decision docs | Two relevant trained decision models, dated October21 launch; exact IDs/contracts | Low retrieval cost; direct HF opens failed then linked cards recovered. Native8K/router16K Mammoth conflict, text library vs native image guide; marketing dates unreliable in search snippets | Add native docs/launch index short-term daily, reassess sustained yield before account recommendation |
| Nace specific Max guide + model table | New distinct checkpoint; input selector/image/alias constraints uniquely useful | Public readable, conflicting dates/state limits; native image vs router text | Targeted daily follow-up, retain discrepancies |
| General official core / Arena | Known checkpoints, no unique frontier lead; Arena timely October22 trends but redundant | Low friction; Liquid creator launch failed again, Respan readable | Keep primary core; rotate AA next, do not infer absence from failed Liquid retrieval |

Inference USD0; retrieval/orchestration unmetered. [Full attempted-source audit](daily/2026-10-22.md). No automation configuration change.


## 2026-10-23 source assessment

Separate catalogs:468 general/30 decision IDs unchanged; keep daily. Official web core and AA produced no unique qualifying checkpoint; rotate Arena. Baseten web failure recovered public HTTP200; Inception HTTP403 remains coverage gap. Other native HTTP checks prove reachability only, semantic coverage limited; prioritize native review next run. No source retirement or account recommendation. USD0 inference. [Audit](daily/2026-10-23.md).


## 2026-10-24 source assessment

Separate catalogs469/30: sole added general ID already evaluated Kimi3.1Pro; decision IDs unchanged. Keep daily full-ID dedupe. Native OpenAI GA/Claude Google Cloud/Baseten16K updates useful for endpoint/configuration distinctions, not retry proof. Inception linked index recovered; guessed Kimi path and Baseten web failures recovered from linked native page/public GET. Qwen blog empty; native releases fallback succeeded. Arena no unique qualified lead; rotate AA. Keep Baseten/Nace short-term core; no source retirement/account recommendation. USD0 inference, retrieval unmetered. [Audit](daily/2026-10-24.md).


## 2026-10-25 source assessment

Cloudflare WorkersAI creator changelog/model/concepts yielded unique Clairic typed-extraction preview (October19), absent from both router feeds; promote short-term daily native-index check, reassess sustained yield before account recommendation. Public readable/high verification, low cost, six-day discovery lag. Catalogs467/30: only LFM2.5 small general addition; full field deltas exposed Clef native/router price/context disagreement. Keep both daily; metadata is not task proof. Baseten web failure recovered directGET200; keep short-term Nace/Baseten. Other native core known identities only; AA redundant/Ling creator provenance unresolved, rotate Arena. No retirement or account recommendation. USD0 inference; retrieval unmetered. [Audit](daily/2026-10-25.md).


## 2026-10-26 source assessment

Catalogs466/30, no added IDs; decision rows unchanged, general metadata churn no retry proof. Keep daily exact/full-field comparisons. Bounded decision-paper search uniquely recovered FLock this-that family absent from both feeds; creator linked runtime exposed latest1.2 after older1.0 paper. Add creator cards/repo to secondary rotation, not daily core; good identity/contract verification, late discovery and unmeasured owner quality. Arena no unique qualifying checkpoint; rotate AA. Cloudflare Clairic already recorded; retain short-term native core. Baseten web failure recovered public GET200; Google October26 storage default relevant privacy context, not model lead. No retirement/account recommendation. USD0 inference; retrieval/agents unmetered. [Audit](daily/2026-10-26.md).


## 2026-10-27 source assessment

Catalogs463/29: four Terra processing/reasoning routes already covered by Scout103; decision free-route removal and Drex price change are metadata only. Keep exact full-row daily comparisons. AA current release view useful for dedupe but no unique qualifying lead; Ling creator identity remains unresolved, rotate Arena. Native core no verified successor; Qwen targeted timeout, Inception/Cloudflare direct403 recovered web, Baseten web failure recovered GET200. Keep short-term native monitoring, no promotion/retirement/account recommendation. USD0 inference; retrieval unmetered. [Audit](daily/2026-10-27.md).

### 2026-10-28 source observation

Liquid official decision library: unique creator verification of d1.1 and open typed-answer successors; high verification yield, low public retrieval cost. Promote short-term daily. Blog oversized fetch failed; library links recovered. Router decision feed uniquely surfaced d1.1. Search mirrors discarded. Arena redundant; rotate AA next.


## 2026-10-29 source assessment

Catalogs457/32: Particle fine-tune excluded via creator verification; Baseten routes already known. Google Carbon announcement already captured in October28 access hold. Partial native core coverage and failed guessed Liquid paths limit completeness; recover saved links and omitted providers next run. Keep cadence; no promotion/retirement. USD0 inference. [Audit](daily/2026-10-29.md).


## 2026-10-30 assessment

Decision catalog uniquely surfaced Joey; Baseten creator library verified native identity and typed contract. Keep both catalogs and Baseten daily temporarily. Broad search redundant; Zhipu/MiniMax guessed changelogs failed. Recover exact native links next run, rotate Arena. No source retirement. See daily/2026-10-30.md.


## 2026-10-31 assessment

Both catalogs succeeded, no additions; Clairic route removed, native status unknown. Arena redundant; keep cadence and rotate AA. Zhipu/MiniMax guessed paths failed again, Qwen empty: next recover official navigation instead of repeating guesses. Partial native semantic coverage limits absence claims. Baseten blog refines Joey launch to October29, no new candidate. [Audit](daily/2026-10-31.md).

### 2026-11-01 bounded watch

Both public catalogs succeeded,452/33, zero added IDs. AA rotation redundant; official grouped searches and six native pages yielded no unique qualified lead. Keep catalogs/native core; prioritize missing Microsoft/Alibaba decision and Zhipu/MiniMax/Moonshot navigation next run. Partial historical and native semantic coverage retained explicitly; no retirement justified. USD0 inference.


### 2026-11-02 assessment

Both catalogs succeeded451/33; one specialized Legal route, no qualifying frontier/decision lead. Microsoft/Alibaba native documentation recovered; metadata cannot clear owner retry gates. Arena redundant; rotate AA. Partial native/historical coverage remains; no promotion or retirement justified. [Audit](daily/2026-11-02.md).


### 2026-11-03 bounded assessment

Catalogs451/33 unchanged IDs; keep separate daily feeds. Native TypeSafe/OpenAI/Perplexity plus grouped official searches and AA yielded no unique primary-verified lead. Partial native and historical review limits completeness; prioritize omitted native decision sources and provider indexes next run, rotate Arena. No promotion/retirement justified; low public retrieval friction, USD0 inference. [Audit](daily/2026-11-03.md).


## 2026-11-04 source review

Both public catalogs yielded identity/contract holds (Morph Reflex, Tencent HY4); keep daily dual-category core. Native creator search successfully recovered Morph documentation; add targeted next-run contract review, not sustained daily promotion yet. Grouped official search and secondary launch index redundant for qualifying checkpoints today; keep rotation. Native semantic coverage partial; prioritize missing Alibaba decisions/exact Perplexity cards next. No source retired on this single pass.


## 2026-11-05 source assessment

Dual catalogs yielded new Ripple and clarified Hy4 identity via Tencent-issued primary release. Keep daily dual feeds; creator announcements add unique checkpoint distinction that catalog naming alone lacked. AA redundant today. Morph429/Z.ai404 increase friction; recover native navigation next, no retirement on one run. Partial semantic coverage retained. [Daily audit](daily/2026-11-05.md).


## 2026-11-06 assessment

Dual catalogs453/35: specialized Omni video addition, no decision additions; keep both daily. Creator Google announcement resolves scope. AA/launch trackers redundant today; rotate Arena. Native Anthropic/Moonshot403, Z.ai404, Morph429 persist: recover navigation/contract rather than assume absence; no retirement justified. Partial semantic coverage retained. USD0 inference. [Audit](daily/2026-11-06.md).


## 2026-11-07 assessment

Dual catalogs460/36 uniquely surfaced Parallel web-grounded service; creator verified launch/contracts but checkpoint provenance and maintained fit held. Keep daily catalogs. Native403/404/429 persist; do not interpret as absence. Secondary trackers redundant; rotate AA. Add Parallel targeted follow-up only when a maintained web-grounded lane exists; no daily promotion or retirement. Partial semantic coverage; USD0 inference. [Audit](daily/2026-11-07.md).


## 2026-11-08 daily observation

Catalog461/35: four batch-route additions, no decision additions; keep daily for exact-route discovery. Native Anthropic/Moonshot retrieval recovered200; semantic coverage partial, Z.ai404/Morph429 persist. Broad secondary search uniquely recovered GPT-6 Cyber official announcement, excluded specialist without maintained lane. Keep compact rotation, recover clean native decision text next. USD0 inference. [Audit](daily/2026-11-08.md).

### 2026-11-09 bounded daily check

Dual catalogs200,461/35, no added IDs; retain daily for exact deltas. Native core partial: Anthropic/Moonshot403,Z.ai404,Morph429; successful HTML is not complete semantic coverage. AA/broad search redundant today; rotate Arena and cleaner native decision cards next. Public receipts in daily report; USD0 inference.


### 2026-11-10 run assessment

Dual catalogs yielded465/36 with one new decision identity; retain daily. Nace creator guide uniquely verified Finance identity, no fallback and whole-request limits; rotate next run for privacy/fit. Anthropic release-note403 recovered through official announcement; exact Fable5.2 already evaluated. Moonshot403/Z.ai404 remain partial coverage. Secondary trackers yielded excluded small Ember; no cadence expansion. USD0 inference. [Receipts/report](daily/2026-11-10.md).


## 2026-11-11 observation

Dual catalogs466/36; no new decisions. Secondary search uniquely recovered official Qwen4 gated release; temporary daily Alibaba flagship-page rotation through November25. Anthropic/Moonshot403,Z.ai404 gaps persist; retain core, no broad source expansion. [Daily evidence](daily/2026-11-11.md).


## 2026-11-16 observation

Dual catalogs468/41 uniquely surfaced Qwen GA and five new decision identities; keep daily. Alibaba official launch verifies GA; decision creator searches empty, hold proposals. Anthropic/Moonshot403,Z.ai404 and partial semantic coverage remain gaps. Secondary launch tracker useful lead source; no promotion/retirement. Next prioritize decision creator cards and Qwen privacy/pricing. [Audit](daily/2026-11-16.md).


## 2026-11-17 observation

Dual catalogs470/43 uniquely surfaced Liquid route arrival; retain daily. Creator release verified IDs/contracts, not callability. AA redundant; rotate Arena. Anthropic/Moonshot403,Z.ai404 remain gaps; no retirement justified. [Audit](daily/2026-11-17.md).
