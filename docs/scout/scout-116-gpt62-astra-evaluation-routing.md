# Scout 116 — GPT-6.2 Astra evaluation routing

Historical record: the bounded table option landed at `0a9dc60`, then was
superseded on November17 by the normal Sol6.2 table reader at `4376bb7`.
[Current replacement](scout-117-gpt62-sol-evaluation-routing.md#full-replacement-landed--2026-11-17).
No direct Sol-versus-Astra6.2 superiority claim follows from those separate runs.

2026-11-17, America/Edmonton. **Stage 1 complete; selection pending.**
Cam invoked evaluate-model with `gpt6.2-astra`. No authenticated discovery,
credentials, inference, target mutations or worktrees. Two read-only Sol
delegates inspected seven model-owning repos; coordinator inspected remaining
registered owners, current central context, dedupe ledger and official sources.
Existing unrelated changes remain intact. No commits/pushes.

## Verified candidate and route

Canonical provider-qualified `openai/gpt-6.2-astra`; native exact
`gpt-6.2-astra`, publicly released/API-listed November17. Distinct from GPT6
Astra, Sol6.2 and Terra6.1; no exact prior attempt in evaluated-models.md.
**Access: unverified.** Presence in Codex's agent menu does not establish an
owner's paid API access. No new credential provisioning is assumed.

- [Model](https://developers.openai.com/api/docs/models/gpt-6.2-astra): text/image
  inputs, text outputs, structured outputs; 1,050,000 context/922,000 input/
  128,000 output. No native audio/video generation or native video-input claim.
- [Migration](https://developers.openai.com/api/docs/guides/latest-model):
  Responses and Chat Completions; tool calling requires Responses. Use native
  `https://api.openai.com/v1/responses` for these owner comparisons, actual strict
  schema/tool contract where required. Remove unsupported sampling parameters.
- [Reasoning](https://developers.openai.com/api/docs/guides/reasoning):
  `reasoning.effort`; low/medium/high/xhigh described, model-dependent other
  levels must not be inferred from Codex. `none` explicitly rejected. Provider
  recommends medium initially; high here tests difficult source fidelity, low
  only for bounded rotation. Explicit effort avoids relying on an inferred
  model default. Standard execution; no pro/multi-agent/hosted-tool experiment.
  Hidden reasoning counts toward output allowance and output billing.
- [Pricing](https://developers.openai.com/api/docs/pricing): Standard short
  context USD8/M input,40/M output,.40/M cache read,10/M 30-minute cache write.
  Above272K input the whole request uses16/60 input/output. Use Standard and
  <=272K, with no cache/Batch/background discounts assumed; conservatively
  reserve10/M input to cover possible writes. No Fast/Ultrafast.
- [Data controls](https://developers.openai.com/api/docs/guides/your-data): API
  data not trained on by default unless opted in; standard abuse logs up to30
  days with exceptions, caching/state caveats. Use `store:false`; this alone
  is not ZDR. Approved organizations/features may use ZDR; owner account posture
  remains unverified. No account-setting changes.

Only owner-identified public/permissively licensed or authored synthetic sources.
No private interviews/family photos, household finance, restricted game scans or
unclear licensed screenplay payloads. ZDR optional for eligible public/synthetic
fixtures unless the owner requires it. Unclear classifications fail closed.

## Stable numbered proposal

Ceilings include controls, blind reviews where required, output reservations and
bounded recovery. They are maximum exposure, not expected bills. No transfers
between owners or independent pools. Contract/access failure is not a semantic
miss. Stop valid decisive failing arms while continuing independent tasks.

1. **Dossier — standalone-semantic-value; USD16; screening only.**
   Two authored namesake snapshots, then full synthetic Story184v4
   `long-history-two-families/follow-1`. Fresh maintained Astra medium4096
   namesake reference and executable Sol6.1 medium16384 continuation reference:
   freeze the exact selector, since `life-follow-1` instead selects older Astra.
   Start candidate **high8192** namesakes/**high32768** full continuation.
   Preserve canonical graph compilation, complete blind Opus4.6 source review
   of every obligation/emitted row/whole-source effect, corrected facts,
   attribution and namesake uncertainty. No material unsupported assertions.
   A useful lead is source-quality improvement, or >=20% lower total cost with
   parity and no latency regression. Sol's narrow namesake win is not a broad
   pipeline winner. This tests direct graph construction versus maintained
   semantic jobs, not permission to delete extraction/adjudication/judging.
   Bound3 pairs,6 blind reviews and1 subject recovery. Complete non-scale cohort,
   independent histories/families and consumer proof remain unselected. BigFish
   source/license and raw-JSON C2 boundaries stay deferred.

2. **Storybook — complete interview extraction/linking; USD20; screening only.**
   First LC026 two-Sarahs, then LC001/016/027 against fresh maintained Opus4.7
   complete-job controls (normal12000/LC02716000). Start **high65536** because
   complete meaning, linkage and uncertainty are the valuable deficiencies:
   Hydrogen previously passed1/4 versus Opus0/4, preserving useful headroom.
   Freeze all-source blind Haiku4.5 review plus source adjudication. Structural
   and semantic>=.90, LC026 linkageF1>=.90, no inflated certainty, attribution
   loss or material source error. Independent LC041 expected-entity oracle and
   connected C2-only consumer are not ready; do not claim adoption or delete
   retrieval/stores/safeguards. Production currently uses Dossier, so comparison
   to the single-call Opus benchmark is not whole-product savings.

3. **Doc Web — handwriting, literal tables and full source-preserving detector;
   USD64 (12/10/42 independent pools).** Start **high32768** throughout: fidelity
   and earlier source-loss failures justify strong reasoning before optimizing.
   Handwriting: public LOC Barney then Alverson versus exact current recipe
   Gemini3.8 and landed Hydrogen opt-in. Require>=.99 transcription fidelity
   plus useful accuracy/operational advantage, preserving all wording/lettering.
   Tables: authored Bakery23 clear cells, then native digital13 and genuine
   uncertainty controls versus maintained Astra reader; exact clear cells and
   justified holds, zero substitutions/harmful changes.
   Detector: Image011 seal/signature and exposed portrait, then full13 versus
   exact executable Gemini detector. Overall>=.95/pass_rate>=.90 AND original
   source audit: preserve integral signatures/seals/lettering, exclude outside
   captions. Numeric geometry alone cannot pass. Actual assisted driver with
   genuine OCR captions/Paddle cleanup and final pixel crops is required.
   Useful passing roles advance to one independently frozen confirmation batch,
   normal image/PDF/HTML/provenance consumer replay and bounded default-off or
   opt-in review patch, without changing defaults. Finite candidate limits:
   handwriting4, tables5, detection16 including recovery/consumer sends. Reuse
   saved responses for deterministic replay. No paid semantic judge.

4. **Board Game Ingester — orientation plus physical scanner contours;
   USD38 (10/28 independent pools).** Orientation **low8192**, CC0/authored frozen
   rotations including pub012270-degree, pub014 required hold, hard sideways
   lettering/f24-04. Fresh Sol6.1 and landed Gemini Decision1 Choice references.
   Zero wrong automatic rotations, all mandatory holds and correct reliable
   anchors; exact native dimensions/inverse/source custody/materialize/export.
   A useful win needs hard-case quality gain or>=30% lower paired p95 at parity;
   merely tying Google's22/22 small panel at higher cost is insufficient.
   Contours **high65536**, six authored scanner scenes versus Sol low8192:
   start fragile outline, then remainder only if useful. Zero material/rim loss
   or definite-background leakage; correct holes/contact/topology and continuous
   loss metrics. Prior Hydrogen and Sol both lost source material, so this has
   quality headroom independently of economics. Passing roles advance to one
   independently frozen confirmation batch and actual generic copied-consumer/
   native inverse/export checks, with bounded review patch. Orientation<=14
   candidate sends, contours<=7 including operational recovery. No paid judge.
   This does not qualify whole joint intake, deskew, quantity, restoration,
   Builder readiness or private game-engine delivery.

5. **CineForge — video-understanding ordered-frame benchmark; USD14;
   screening/reference decision only.** Six authored v4 cases, five original
   ordered JPEGs each. Start **high16384**, ample relative to prior first-case
   Hydrogen1920 total output, with fresh Sol6.1 low4096/Luna6 low1400 controls
   and fixed blind Opus4.6 judge/source-first review. Strict13 keys,
   structural>=.70, rubric/combined>=.80, no unsupported motion/source facts;
   separately report15s/USD.02 operational targets. Start the discriminator,
   then remaining5 only on useful evidence. Bound8 candidate requests including
   recovery,12 controls/18 judge requests. No shipped video analyzer exists to
   replace; ordered JPEGs do not qualify native MP4/audio or generated boards.
   Whole-workspace collapse deferred pending scene-gap ID/consumer semantics
   and independent completeness oracle; Carbon's diagnostic quality did not
   overcome full-source failure or roughly764s versus163s pipeline timing.

**Campaign maximum USD152 =16+20+64+38+14.** No paid work is authorized yet.

## Reservation feasibility and effort stopping

Candidate reserve uses10*input/1e6 +40*total_output/1e6, including potential cache
writes; exact rendered counts must be <= these conservative input bounds.

| Pool | Candidate worst-case finite allowance | Residual for controls/reviews |
|---|---|---|
| Dossier16 |2x16K/8192 +2x110K/32768 =5.7968 |10.2032: controls<=3, reviews<=7 |
| Storybook20 |5x26K/65536 =14.4072 |5.5928: controls<=2, reviews<=3 |
| Doc handwriting12 |4x106K/32768 =9.48288 |2.51712 |
| Doc tables10 |5x26K/32768 =7.8536 |2.1464 |
| Doc detection42 |16x106K/32768 =37.93152 |4.06848 |
| BGI orientation10 |14x26K/8192 =8.22752 |1.77248 |
| BGI contours28 |7x106K/65536 =25.77008 |2.22992 |
| Cine14 |8x20K/16384 =6.84288 |7.15712: controls<=.60, judges<=5.4864 |

The canonical detector fixtures previously had maximum913190 image bytes and
2000px-high JPEGs. Count the exact full prompt/image on the native route before
dispatch; byte size alone is not token count. Tables'26K includes rendered
images. All source counts and judge tariffs must be qualified by zero-cost
matrix/count preflight. If an original payload exceeds the stated bound, stop
that pool before spending and present the exact revised reservation requirement;
other pools remain independent. Do not resize or reduce source truth to admit it.

Finite allowances include at most one independent confirmation batch per useful
Doc/BGI role; freeze cases before first output and ensure all required proof fits
the slots. Additional affordable sends are not automatically authorized. Reuse
saved answers for deterministic replay and judge repair. If a prospective fresh
source cannot fit the declared slots/envelope, preserve a screening verdict and
prepare its exact prerequisite rather than claim adoption-ready.

No semantic effort sweep selected: high is a source-fidelity capability question;
low orientation targets an interactive bounded task. Medium/xhigh/max/pro are
unmeasured, not failures. A complete valid high failure stops that arm; do not
tune upward until favorable. Output truncation/adapter/judge faults allow the
smallest evidence-backed operational repair within the same finite allowance
and cap; disclose content-affecting changes. Further effort optimization needs
a specific measured token/quality hypothesis and new bounded selection.

Before paid multi-case work freeze source/prompt/schema/scorer hashes, full
resolved independent case matrix, comparator/judge identities/settings, exact
prices, cache keys/concurrency and reproduction command. Full unresolved request
reservations count against caps. No model fallback. No private payloads or
defaults, commit/push/deployment/landing. Selected useful Doc/BGI roles include
bounded consumer qualification/review patches; the other three are explicitly
screens, not unfinished promises of unselected adoption work.

## Not recommended now

Every remaining registered project gets one disposition; stale registry routes
are resolved read-only and not rewritten.

| Registered owner | Disposition |
|---|---|
| Echo Forge | **Defer.** d1.2 sole intent classifier landed62ba420f; reviewed Ember outline job passed independent Clockmaker/Ferry2/2 and actual matcher atUSD.00125755/5.485s. Same independent Mini sources averaged2211input/1191.5output; illustrative Astra8/40 cost is.06535 before reasoning, versus.01 target. Exact token counts unmeasured; not proof candidate cannot be better. No remaining representative quality defect/consumer payoff currently warrants premium comparison. Licensed34-room broader input eligibility unresolved. No audio/STT/executor replacement from text/image model. |
| RoboRally | **Do not evaluate.** Deterministic authoritative engine takes~.2–2ms; frontier model historical3-case full-contract reference already exists. Hydrogen's exact38-event causal lead still took57.687s and failed full schema. A new premium checkpoint has no plausible runtime economics; another offline capability panel needs a separately valued question. |
| Ultima IV Web | **Defer.** Live/adaptive creator contracts exist, but full scored cohorts/runner and source permissions are not interchangeable with product fidelity tests. Old four-frame static32/32 results do not establish earned gameplay. Current focus is completed Story025 product; freeze an eligible outcome-grounded current player comparison and active budget before reopening older experiments. |
| Financial Hub -> Financial Reporting | **Defer.** Registered path absent; inspected financial-reporting. Household sources private; no maintained eligible synthetic decision-quality corpus, source approval or new route policy proof. |
| Financial Monthly Analysis -> Financial Data | **Defer.** Registered path absent; inspected financial-data. Reconciliation inputs private and mock transport/security tests cannot judge source quality. Need eligible maintained benchmark/payload policy. |
| VLC Thumbs | **Do not evaluate.** Registered nested path absent; inspected /Users/cam/Documents/Projects/vlc-thumbs. Native decode/cache/bookmarks have no model-owned runtime decision. |

Conductor itself: defer; deterministic catalog collection and no maintained
labeled model-runtime replacement lane.

Matching tasks omitted within recommended owners:

- Storybook persona: prior Astra narrow warmth costUSD.02307/turn at2.686s,
  while Luna is much cheaper; same-family20% token-rate decrease alone leaves
  about.01846, over.01. Token behavior is not measured for6.2, so this is a payoff
  estimate, not an incompatibility finding. Existing synthetic persona coverage
  is narrow; complete extraction has more valuable measured source defects.
  Photo: current exact descriptions/OCR require source-image+prompt counts far
  above125 tokens; at8/M even125 input costs.001 before output, exhausting the
  owner.001/photo gate. Prior Hydrogen9/9 preserved a quality lead but failed
  that floor. Defer premium photo job pending changed operational contract;
  no private photos. Mode/clarification/ranking component leads currently lack
  useful reachable consumers, not another task for a premium model sidecar.
- DocWeb safety: Attempt081 informational consumer decision unresolved; later
  Ember/Hydrogen both failed genuine S3 mandatory uncertainty hold. No new
  full22 safety run; crop-validation40/40 cheap reference already. Detection
  does not remove page safety/manual veto. Consistency sidecars need connected
  useful consumers; reference resolution is deterministic12/12+491 real targets,
  layout5/5 and born-digital/source-driver paths have no relevant new subject
  decision. Private Onward corpus remains excluded.
- BGI whole AI-led intake/Builder is private on current ElCapitan/Robo sources;
  freeze eligible full package/consumer first. Inventory, sides, quantities and
  game-specific contracts are separate from isolated orientation/contours.
- Dossier identity questions: recent independent d1.2 qualification rejected
  fixed policy versus Luna; premium generative model is not a new efficient
  scalar decision arm. Assertion/occurrence sidecars lack adopted consumers or
  require separate closed source/policy boundaries. Preserve independent wins.
- CineForge text ScriptBible/full workspace has incomplete eligible source and
  end-to-end oracle/consumer semantics. No image generation, native video/audio
  or media judge claims from the ordered-frame screen.

## Evidence and next action

Owner root instructions/Ideal/spec, registries/local evaluation guidance and
recent attempts were inspected read-only. Key durable pointers:

- [Dossier runbook](/Users/cam/Documents/Projects/dossier/docs/runbooks/model-benchmarking.md)
  and evals/semantic_benchmark/README.md; Story184 synthetic v4 continuation.
- Storybook local evaluation skill, provider privacy, registry and Scout111
  LC026/001/016/027 complete-source review; independent LC041 oracle gap.
- [DocWeb Hydrogen fidelity attempt](/Users/cam/.codex/worktrees/hydrogen-20261115/doc-web/docs/evals/attempts/094-hydrogen-source-fidelity.md).
- [BGI Hydrogen attempt](/Users/cam/.codex/worktrees/hydrogen-20261115/boardgame-ingester/docs/evals/attempts/20261115-scout111-hydrogen.md),
  landed optional Google orientation95c481c, d1.2 f24-04 wrong-auto evidence.
- CineForge v4 ordered-frame manifest/registry, Attempts036/046/047 and Scout111.
- [Echo Ember adoption](/Users/cam/.codex/worktrees/ember-20261111/echo-forge/docs/evals/attempts/scene-to-soundscape-golden/20261111-ember-adoption.md).
- [Hydrogen campaign](scout-111-gemini4-hydrogen-evaluation-routing.md),
  [d1.2 follow-through](scout-113-d12-ultra-evaluation-routing.md),
  [previous Qwen routing](scout-114-qwen4-max-evaluation-routing.md).

After selection create dedicated owner codex branches/worktrees only under
`/Users/cam/.codex/worktrees/gpt62-astra-20261117/<project-key>`, refresh current
remote base/comparators without polluting primary checkouts, obey credential
custody/owning-repo protocols and preserve all prior closed wallets. Account for
every tree at handoff. No evaluated-ledger entry yet: no authenticated attempt.

Reply `yes` to run all numbered evaluations, or `only do 1, 3, and 5` for a subset.

## Selected execution — 2026-11-17

Cam replied `yes`, selecting all five numbered owners and the disclosed
USD152 combined ceiling. The five isolated owners were assigned before any
paid provider requests. There is no native OpenAI key mapping in the central
custody helper. Each owner uses its own eligible configured credential path.

| Owner | Selected decision and condition for advancing | Cap (USD) |
|---|---|---:|
| Dossier | Direct semantic graph screen against Astra and Sol, then report quality and total economics | 16 |
| Storybook | Complete extraction/linking screen against Opus 4.7 | 20 |
| Doc Web | Independent handwriting, table and detector lanes, with consumer proof and opt-in patches for useful wins | 64 |
| Board Game Ingester | Independent orientation and contour lanes, with native materialization/export proof for useful wins | 38 |
| CineForge | Ordered-frame benchmark against Sol and Luna | 14 |

### CineForge ordered-frame screen

Retain Sol and Luna as headless benchmark references. One fresh matched case
qualified the exact native strict five-frame contract and maintained adapter.
Astra high/16384 reached .6991 combined in 14.720s at USD.051434, versus Sol
.7127/6.563s/USD.0099535 and Luna .57645/5.003s/USD.000547175. Astra described
motion better than Luna on this case, but Sol grounded the same concrete facts
and identified teal. The structural, rubric, combined and cost gates failed.
The remaining five cases are unmeasured. Six valid POSTs cost USD.121894675
including USD.059960 for blind judging, zero unresolved exposure. No further
effort arm was tested. [Owner attempt](/Users/cam/.codex/worktrees/gpt62-astra-20261117/cine-forge/docs/evals/attempts/061-astra62-ordered-frame-screen.md).

### Board Game Ingester orientation and contours

Retain the existing roles, including the landed optional Google orientation
job. Astra low/8192 and Sol low/2048 each pass 2/3 fresh orientation cases.
Both issued a wrong automatic rotation on the hard sideways fixture. Astra
median 4.375s/total USD.014008 versus Sol 5.358s/USD.008012. The fresh Google
control was rejected for its owner credential, so its established optional
job evidence remains separate. Astra high/65536 materially improved the one
matched contour, with 16 material pixels lost and zero background leakage
versus Sol's 1,582 and 713, but missed the zero-loss gate. Its 21.362s/$.059724
also exceeded Sol's 7.795s/$.0096335. Native inverse-pixel checks passed.
Further cases and promotion are unmeasured. Eight valid and one rejected POST
account for USD.0913775 known plus .0262144 unresolved against USD38.
[Owner attempt](/Users/cam/.codex/worktrees/gpt62-astra-20261117/boardgame-ingester/docs/evals/attempts/20261117-scout116-astra.md).

### Storybook complete extraction and linking

Retain the full pipeline. The fresh matched two-Sarahs C2 pair gave Astra
high/65536 .79445 structure/.92 semantic/.67708 linkage versus Opus
.93985/.92/.86857. Both miss the linkage gate. Astra had higher reference
recall and avoided inventing Oliver's surname. The separate LC001 C1 pair
gave Astra .48963 structure versus Opus .63834, with .92 semantics both.
Astra retained source uncertainty and detail but emitted collective people
nodes in violation of the owner contract. Its subject cost/latency were
USD.428244/112.007s on C2 and .270884/70.620s on C1 versus Opus
.210050/66.585s and .106595/35.970s. Stop before two other cases. All 16
generations valid, subject USD1.015773 plus blind judges .129276, total
USD1.145049/20, no unresolved exposure or retries.
[Owner attempt](/Users/cam/.codex/worktrees/gpt62-astra-20261117/storybook/docs/evals/attempts/202-gpt62-astra-complete-extraction-screen.md).

### Dossier direct SemanticGraph screen

Retain both references. On the two fresh namesake snapshots, high/8192 tied
older Astra medium/4096 at 6/6 meanings and no material errors. Subject totals
were USD.227456/61.340s versus .254670/34.635s. Lower cost did not clear the
20% parity target, and latency regressed. On the full fresh synthetic
two-family continuation, high/32768 tied Sol medium/16384 at 5/5 meanings,
costing USD.731952/52.242s versus .175348/26.916s. Exact native schema, graph
compiler and full blind source review qualified. Six subjects and six blind
reviews cost USD2.787186/16, zero unresolved exposure. Independent histories
and actual runtime replacement were outside the selected screen.
[Owner attempt](/Users/cam/.codex/worktrees/gpt62-astra-20261117/dossier/docs/evals/attempts/041-scout116-gpt62-astra-20261117.md).

### Doc Web source fidelity and rollout recommendation

Recommend the separate reviewed Astra 6.2 table-reader recipe for the bounded
OpenAI role. Four fresh pairs including a newly authored held-out source
gave 56/56 clear cells and both required uncertainty holds for each model.
Astra 6.2 high/32768 cost USD.247616 and averaged 6.205s, versus older Astra
medium/8192 at .314920 and 7.437s. That is 21.37% lower source-reader cost
and 16.56% lower mean latency. The held-out call alone was slower. The normal
SDK replay matched the frozen wire and the actual driver exported an exact
20-cell table with its qualification receipt. The ambiguity control held and
blocked export. The opt-in reader checks the native request token count against
its USD2 per-dispatch reservation before inference. Doc Web passed 297 focused
tests and methodology validation. Keep existing upstream OCR and publishing safeguards. This
does not rank the historically cheaper Argon option or quantify whole-workflow
savings. The patch is retained for review.

Reject the tested handwriting arm. On Barney, Astra .962170/USD.119454/67.836s,
Hydrogen .988497/.049185/36.967s, Gemini3.8 .982406/.02393175/48.259s. All three
missed the .99 threshold on this fresh case. Retain the previously qualified
reviewed Hydrogen option with observed variation and leave Alverson unmeasured.

Retain the assisted detector and manual crop review. Astra .9972/.9940 on two
geometry cases versus Gemini's tolerant .9839/.9829, with axis-order differences.
Astra cost USD.090208/4.297s mean versus .012685/9.084s. The raw seal/signature
box included printed captions. The exact original-pixel assisted request hit
33,120 patches against the 30,000 API limit before generation. The canonical
original sources have the same blocker. No final assisted crop, remaining 11
cases or replacement claim. Reopen only for a source-preserving exact-route
change allowing the original input under the maintained consumer contract.

15/15 valid paid generations cost USD.85799975/64, no paid judge or unresolved
exposure. No within-task Astra 6.2 effort comparisons.
[Owner attempt](/Users/cam/.codex/worktrees/gpt62-astra-20261117/doc-web/docs/evals/attempts/097-gpt62-astra-source-fidelity.md)
and [opt-in and rollback](/Users/cam/.codex/worktrees/gpt62-astra-20261117/doc-web/docs/runbooks/astra62-literal-table-reader.md).

### Campaign accounting and worktree custody

58 generation POSTs, 57 valid plus one rejected BGI Google control. Known
USD5.003506925, plus USD.0262144 unresolved reserve, maximum accounted
USD5.029721325 of 152. Native catalog/token-count requests are separate.
All selected replacement decisions are settled. Other effort levels were
unmeasured and no semantic calibration or unselected comparison was run.

All five isolated trees are retained uncommitted for evidence and review, at
`/Users/cam/.codex/worktrees/gpt62-astra-20261117/<key>`. No temporary keys
were injected. Owner reports retain replay commands, usage, raw custody,
and focused validation. The Doc Web patch is the only adoption candidate.

| Key | Branch | Base |
|---|---|---|
| dossier | codex/gpt62-astra-dossier-20261117 | 19d772d78372f0da7664ef8db9b05333911ff539 |
| storybook | codex/gpt62-astra-20261117-storybook | eaa1a9e9569b791855d75d8bbe64143c9eea6211 |
| doc-web | codex/gpt62-astra-20261117 | 56564d95cd2cf9ce498aaaca84537a64b1e89f31 |
| boardgame-ingester | codex/gpt62-astra-20261117 | 95c481c17d91735eb20bf2252989205a5e005a86 |
| cine-forge | codex/gpt62-astra-20261117-cine | accb76dd6377d1a6a1ce65c2ac04f66e1458eb3e |

### Doc Web landing — 2026-11-17

Cam separately approved landing the opt-in table reader. Doc Web Story 273
closed and remote main verified at `0a9dc6055e5ebe8e30f1b8ce3549050251bdb1a1`.
Close-out used the SDK's public request method for the same native count
endpoint to cover the locked 1.109.1 SDK. A provider-free replay confirmed
the held-out export, ambiguous export hold, and over-budget refusal before
inference. The 124 affected regression tests passed. The Doc Web worktree
remains for evidence. Other owner worktrees remain uncommitted. No new paid
provider calls. [Doc Web commit](https://github.com/copperdogma/doc-web/commit/0a9dc6055e5ebe8e30f1b8ce3549050251bdb1a1).
