# Scout 091 — Five decision-model evaluation proposals

Date: 2026-10-13 (America/Edmonton)
Status: Completed selected owner campaign — 2026-10-13; no runtime promotion

Cam requested independent judgment on Clef-omni, Drex2.0, Liquid d1,
ScaleDown Classify-1 and Solar Decide. Supplied fit annotations were not treated
as requirements or conclusions. Current public sources and every registered
owner were inspected; a read-only owner worker assisted. No credentials,
authenticated catalogs, inference, target edits, defaults, commits or pushes.
Existing shared-checkout changes preserved. This is scouting/routing under
Conductor's Ideal/spec and methodology graph, not a shared runtime rollout.

## Public identity and contract

All five are announced and API-listed; **access: unverified** for each.
The evaluated-model ledger has no exact candidate/alias prior attempt. Known
Jev/Luna/Microsoft/Perplexity attempts remain references, not new nominations.
[Fresh public router snapshot](evidence/scout-091-public-models-20261013.json)
preserves exact canonical IDs, advertised modalities and prices.

| Candidate | Proposed exact router identity | Input USD/M, output free | Judgment |
| --- | --- | ---: | --- |
| Clef-omni | cloudflare/clef-omni-20261009 | .15 | Most interesting new visual classifier; short text remains worth measuring despite higher unit price than Jev. |
| Drex2.0 | nace-ai/drex-v2.0-20261009 | .06 | Useful short-state challenger; long-context identity must fail closed. |
| Liquid d1 | liquid/d1-20260930 | .04 | Strong economical text lead and direct visual lead; per-question billing matters. |
| ScaleDown Classify-1 | scaledown/classify-1-20260928 | .04 | Worth qualifying, with explicit state preservation and image-route admission. |
| Solar Decide | upstage/solar-decide-20260928 | .05 promotional | Include in short-text screen: large context is not a reason to presume weak routing or defer an inexpensive comparison. |

[Cloudflare announcement](https://blog.cloudflare.com/clef-faster-cheaper-multimodal)
and [model reference](https://developers.cloudflare.com/workers-ai/models/clef-omni/):
Workers AI `@cf/cloudflare/clef-omni`, typed Noul/Choice/Score, text/image/audio/video.
Router currently text/image,64K. Direct media billing/resizing is model-owned;
images capped1024tokens, text can truncate after media admission. Preserve all
source bytes and inspect actual admission; no silent state truncation. Vendor
latency/benchmark results are leads, not owner proof. No prose/rationale,
geometry, arbitrary generated schema, tools or reasoning-effort parity.
[Cloudflare data usage](https://developers.cloudflare.com/workers-ai/platform/data-usage/)
says no training without consent; its stale generic claim that Cloudflare does
not create models conflicts with this release. Do not infer endpoint ZDR from it.

[Nace reference](https://console.nace.ai/docs/drex/reference/models): direct
`drex-v2.0`, POST `/v1/systemone`, USD.06/M. Despite nominal131K listing,
actual2.0 supports state8192 and state+longestquestion16384; longer requests
serve1.5. Keep payloads within both, validate served identity and forbid
model substitution. Router context131K is not proof that its exact2.0 route
avoids substitution. [Nace privacy](https://console.nace.ai/privacy) allows
training by default and up to30day input/output retention; DeepInfra/router
is a different route whose policy must be recorded, not inferred from direct.

[Liquid release](https://www.liquid.ai/blog/d1-decision-model): direct `d1`,
POST `https://api.liquid.ai/decisions/v1/systemone`, text/images, USD.04/M;
router text-only64K. Every question bills its text and shared images again.
[Current model docs](https://docs.liquid.ai/lfm/models/decision-models) distinguish
hosted d1 from d1-3B and d1-omni-600M; do not substitute those weights/checkpoints.
Direct account callability, immutable hosted revision and retention/ZDR unknown.

[ScaleDown contract](https://docs.scaledown.ai/api-reference/decisions-overview)
was recovered by one unauthenticated GET after web retrieval failed. Direct
`classify-1`, `/v1/scaledown` is a typed facade over its own classifier.
Only state.text/state.document consumed; lossless stable JSON serialization into
state.text is an explicit adapter, not arbitrary-state drop-in parity. Each
question becomes a classify call, usage summed. Image-direct `/classify` is
separate; router advertises text/image/file1M but actual typed image transport
must qualify. No silent text/OCR substitute or dropping owner fields.
Retention/ZDR unresolved; direct price not assumed equal to router promotion.

[Upstage reference](https://console.upstage.ai/docs/models/solar-decide) and
[API](https://console.upstage.ai/api/systemone): direct `solar-decide`,
`https://api.upstage.ai/v1/systemone`, text/JSON512K, USD.10/M, beta schema;
2–26 Choice options, no generated prose. Proposed router promotion is.05/M.
Direct claims no training, storage exceptions for service delivery; full
router/provider retention and ZDR remain unverified.

All selected fixtures below are explicitly synthetic or owner-classified public.
Route may retain/train on them; stricter owner policy prevails. No private family,
health, household finance or licensed private rulebooks. No account settings
changes or new-account setup is authorized. Missing eligible access stops only
that route; no comparator-only paid run. Exact canonical identity, usage billing,
lossless state/modality admission precede semantic work. Public metadata is not
served-weight attestation. No automatic alternative model fallbacks.

## Stable execution handles — Evaluate now

Fresh same-input incumbents, frozen independent request topology, maintained
scorers and independent source review; no paid judge. Recover harness faults
within hard caps, preserve unsuccessful probes, no semantic retry/tuning.
Predeclare all finite-output projections before calls; generated rationale
remains explicitly unqualified. Different confidence calibration must be tested
under the existing owner policy, not presumed interchangeable.

1. **Echo Forge — USD2.** All five candidates on `control-intent-v1`,48 unique
   synthetic cases:20controls/22noncontrols/6ambiguous, versus fresh
   Gemini3.8Flash low. First qualify Choice yes/no/abstain, identity, usage,
   negation/quotation/no-action. Complete valid semantic screens to avoid
   favorable subsets; unsafe executable behavior stops that candidate path.
   Measure exact accuracy, control recall, false activation, ambiguity,
   median/p95 and actual task cost. Retain incumbent unless equal-or-better
   safety/accuracy and useful latency/cost improvement; seek >=30% lower p95
   as a soft practical screening threshold. Grok4.6 remains historical accuracy
   reference, not another paid arm.48Gemini reservations at8192input/2048output,
   .75/3.75 rates total.663552; five48-case candidate arms bounded8192 tokens
   at rates totaling.40/M reserve.1572864; combined.8208384 leaves1.1791616
   qualification/recovery. Single consumed question avoids repeated-state bills.
   No soundscape generation, scene-proposal repair or playback authorization.

2. **Doc Web text — USD4.** All five on Story233
   `jev-document-consistency-classification`/`jev-consistency`:20 unique
   reviewed synthetic cases on2 documents ×2 repeats; fresh pinned
   gpt-4.1-2025-04-14 status projection and actual per-candidate serial fallbacks.
   Preserve explicit uncertain review and existing .8 policy; do not tune it.
   First qualify five-class Choice and exact structured state. Measure false-clean,
   class recall/macroF1/review coverage and complete cascade cost/p95. Fewer
   dangerous misses, or no worse misses plus meaningful economics can justify
   a next promotion check; no automatic full-planner replacement. Worst240GPT
   baseline/fallback calls at4096input/160output and2/8perM reserve2.27328;
   200typed calls at8192input and summed rates.40/M reserve.131072. Combined
   2.404352 leaves1.595648 qualification/recovery. Shadow runtime validation
   remains a separate promotion boundary after this classifier comparison.

3. **Doc Web visual — USD8.** Clef-omni and ScaleDown router image paths,
   Liquid direct vision if eligible configured access exists; first lane
   `crop-page-level-deletion-gate`,22 owner-public source-page/crop cases,
   source-adjudicated Attempt048 contract/golds, fresh GPT5.5 Responses
   none/2048. Start two-image admission and known neighboring-content/safety
   differentiators; stop an arm on source-confirmed false-safe. Preserve
   uncertainty/manual review veto, source image bytes and pixel geometry;
   record provider internal resolution. Require zero unsafe acceptance and
   no worse safe acceptance/rejection against fresh control, report relative
   latency/cost. Finite safety verdict only: generated reasons and production
   replacement unqualified.22GPT at46000input/2048output, owner5/30perM rates,
   reserve6.41168; three22-case typed arms at64000tokens and total.23/M reserve
   .32384, subtotal6.73552;1.26448 remains for admission/recovery. Price refresh
   and rendered sizes must admit this matrix before sending. Liquid repeated
   input reservation assumes one consumed question. No downsampling to rescue
   transport, no OCR substitute, no private genealogy uploads.

4. **Board Game Ingester — USD2.** Same three vision candidates on
   `asset-orientation`/`synthetic-orientation-v1`,14 synthetic images versus
   fresh selected gpt-6.1-sol low. First classify0/90/180/270/review with no
   golden cues, then ambiguity/symmetry and direction cases; stop a candidate
   on confirmed wrong determinate rotation or unsafe ambiguity. Aim12/12
   determinate and correct symmetry/review, exact pixel/inverse proofs, and
   material measured latency/cost saving. Predeclare finite projection of
   status/angle/review; no fabricated rationale or full schema parity. Native
   pixel executor remains authoritative.14Sol calls at32768input (including
   1.25 cache-write reservation multiplier)/2048output and owner2/10perM rates
   reserve1.4336. Three14-case typed arms at64000input and summed.23/M reserve
   .20608; subtotal1.63968 leaves.36032 qualification/recovery. Current public
   pricing and exact image admission are refreshed before calls; no oversized
   reservation or changed product output allowance can silently exceed the cap.
   Only synthetic corpus, not seven private real-source crops; broader physical
   package/deskew readiness remains unmeasured.

**Per-owner ceilings:** Echo2, Doc Web12 (text4 + visual8 independently bounded),
Board Game Ingester2. **Campaign maximum USD16.** Numbers select lanes; selecting
both Doc Web items dispatches one owner worker with separate lane ledgers.
No blanket cap retry, paid judge, private upload, commits/default/rollout authority.
Whole-workflow shares are unknown except prior Storybook routing economics;
input rates alone establish no product saving. Repeats are reliability evidence,
not additional independent samples. Tiny clean orientation corpus cannot prove
real-source parity; successful visual routing still needs its missing rationale
or an explicitly approved new consumer contract before adoption.

## Not recommended now — remaining owners

| Owner | Disposition and concrete reason |
| --- | --- |
| Storybook | Defer: latest Attempt182 postguard replay17/24vs16/24 exposes seven shared code-owned grounding deferrals. Repair benchmark was completed; guard remains unchanged. A five-model mode-routing tournament cannot fix this downstream acceptance boundary. Resolve grounding acceptance first; photo/OCR/persona require generated fields/prose, finite artifact selection's prior completed path violated rejection and stopped; fix that completion boundary before another selector comparison. Synthetic photo/place-object tests include finite propositions but no independently maintained finite-only consumer or demonstrated payoff; preserve generated caption/OCR/followup/identity safeguards. Retrieval anchor rescue limits practical value. |
| Dossier | Defer: maintained stage-judge matrices exist, but their generated reasoning/evidence and private-fixture eligibility are not qualified as a finite-only consumer. A new verdict-only projection is not the same judge decision. Graph extraction needs generated entities/spans/provenance; private histories excluded. |
| CineForge | Defer: maintained ordered-frame lane needs13-key generated evidence, not probabilities alone. Finite visual labels cannot replace evidence agreement/grounding; no production call currently exists to move. Freeze independent finite consumer/golds/payoff before diagnosing Clef audio/video or image scoring. Text config/ScriptBible likewise generates data/rationale. |
| Robo Rally | Do not evaluate: maintained deterministic legality/simulation has no external model-owned finite lane. |
| Ultima IV Web | Do not evaluate: fidelity/reconstruction/gameplay evidence lacks maintained decision-model runtime/oracle; a visual model demo is not earned-replay proof. |
| VLC Thumbs | Do not evaluate: native decode/cache/scheduler/bookmarks deterministic, no maintained AI consumer. |
| Financial Hub | Defer: private household data, no eligible synthetic typed corpus plus provider-qualified owner policy. |
| Financial Monthly Analysis | Defer: private reconciliation/recommendations; no maintained eligible synthetic decision corpus. |

Conductor itself: Defer, no maintained labeled runtime classifier. Doc Web OCR,
crop geometry and generated planning/repair fields are output-contract mismatches;
matching binary page safety is separately proposed. Board segmentation/counting/
deskew need different generated contracts/private inputs. Echo scene-intent
label-only improvements previously failed complete proposal usefulness: context,
asset eligibility and review coverage precede another classifier comparison.
Liquid router cannot cover vision; only direct listed in visual items. Drex/Solar
text-only routes have no visual items. No audio generation is implied by omni.

## Validation / next action

Public source/canonical price/modality checks, exact ledger match, every owner
context, relevant maintained tasks and recent isolated evidence inspected.
Reservation arithmetic checked; fresh rendered per-call admission remains
mandatory. No target tests required for a recommendation-only document.

Reply `yes` to run all numbered evaluations, or `only do 1, 3` for a subset.
Stage1 selection before paid execution is required by evaluate-model/SKILL.md;
Stage2 still requires no second ceremonial approval for this exact scope.

## Approved owner execution — 2026-10-13

Cam replied `yes`, selecting items1–4: EchoUSD2, DocWebtextUSD4,
DocWebvisualUSD8, BoardGameIngesterUSD2; totalUSD16 inclusive. Three isolated
owning-repo workers dispatched before any owner provider call. Each reads
owner rules, portable protocol, actual contract and frozen fixtures; resolves
current remote base; runs independently bounded native qualification and
progressive matched evaluation. Root remains coordinator/artifact reviewer.

Central custody helper reports OpenRouter configured and vault permission check
passed. Provider-presence checks disclosed names only. Owners prefer existing
keys, otherwise temporary one-provider injection into ignored owner env and
cleanup; Liquid direct is not centrally configured and is eligible only with
existing owner access. Missing direct vision access does not authorize account
setup, another model or a router text substitute. No target private uploads,
commits/pushes, runtime defaults or deployment selected.

## Completed owner decisions — 2026-10-13

**Solar remains the most promising conditional batch lead; establish its
consumer and uncertainty boundary before further paid evaluation. Retain current
interactive Echo and selected Sol orientation paths. No visual safety winner.** Solar's classifier/cascade quality and economics lead is real
on this bounded screen; it does not erase its source-gap false-clean or slow
tail, nor qualify the full planner/rationale workflow. No runtime promotion.

| Owner/lane | Fresh matched evidence | Economics | Recommendation |
| --- | --- | --- | --- |
| Echo original richer-state48 | Gemini44/48; Clef31, Drex33, Liquid36, ScaleDown36, Solar41. Gemini20/20controls,2/22falsecontrols,4/6ambiguity; Solar20/20,2/22,1/6. | Semantic48cost Gemini.03639375; candidates.00070308–.00299205. Gemini p955206ms; Solar12021ms, other typed321–953ms. | Retain interactive Gemini; no challenger clears original48 quality. This is richer-state diagnostic evidence, not full current-runtime proof. |
| Echo exact current-input28, offline source-selected applicability | Preexisting independent input-byte criterion: Solar26/28vsGemini25/28,16/16controlrecallboth, falsecontrols1vs2, ambiguity0/1both.14rebuilt current-input cases remain unmeasured. | Solar.00085270/p9510249ms vsGemini.02142675/6086ms. | Narrow Solar quality/economy headroom; slower tail and incomplete actual42runtime coverage prevent promotion. No favorable-case selection or new calls. |
| Doc Web synthetic consistency20unique/two sources×2 | Solar cascade33/40,macroF1.82087 vsGPT30/40,.73725. Confirmed-defect clean0vs3, uncertainty-clean1vs0; combined dangerous-clean1vs3. | Solar cascade.0082638 vsGPT.043392 (80.96%less);p9517319msvs1111ms (15.59x). Includes6realSolarfallbacks,notwholeplanner savings. | Conditional batch lead; defer paid qualification until a useful connected consumer/source boundary is identified. Retain existing planner/manual review. Missing-source maintenance09 confidently clean on repeat1 remains a real failure. |
| Doc Web visual page/crop safety | Clef1/2vsfreshGPT5.5 1/2: both incorrectly accepted visibly clippedsealpage012001; known048source gold439inliers/~21%missingsealheight.20casesunmeasuredafterstop. | Paired2Clef.0008805/p951487ms vsGPT.051778/p952767ms. | No qualified automatic safetywinner; preserve review. No generatedrationale or confidence routing qualified. |
| Board Game synthetic orientation14 | FreshSol12/12determinate,symmetry1/1,review1/1. Clef clearrotation1/1,ambiguousreview0/1;12unmeasured. All16 measured pixel/inverse proofspass. | FullSol14.02396/p958537ms; paired2Clef.0001281/p95.755s vsSol.002482/6.905s. | RetainSol. Reject current Clef automaticreview projection; no wrong pixelrotation occurred because Clef selected0/noop. |

Other Doc Web cascades: Clef28/40 with3dangerousclean,cost.0448407/p951851ms;
Drex22/40 with12dangerousclean (4defect+8uncertainty),.01438376/1115ms;
Liquid31/40 with4dangerousclean (2+2),.00727784/1139ms;
ScaleDown31/40 with2dangerousclean (2+0),.04250792/1682ms.
ScaleDown's small quality benefit comes with38/40fallbacks,2.04%costsaving
and51.42%slowerp95: lowerpriority than Solar, not a blanket capability rejection.
Liquid's cheap cascade fails no-worse dangerous-clean; reject this automatic
policy. Clef/Drex do not merit unchanged reruns for these text tasks.

All five exact router identities were callable on text. ScaleDown image
state-array requests rejected400 in bothvisual owners, before a valid answer;
documented state.document path delegates OCR text extraction and cannot preserve
the selected pixel-native visual contract. Capability remainsunmeasured,
not model-wrong. DirectLiquid vision had no eligible existing ownercredential;
no account/keysetup, alternatecheckpoint or text-only visual substitute. Clef
imageChoice qualified, but finite safety/review judgments failed preservedgolds.
No threshold fitting, semantic retries, gold/prompt tuning or paidjudge.

### Owner provenance and accounting

| Owner worktree/branch | Exact current remote base | Inclusive knownUSD | Unknown boundedUSD | CapUSD |
| --- | --- | ---: | ---: | ---: |
| /Users/cam/.codex/worktrees/scout091-echo-20261013; codex/scout091-echo-20261013 |31fb8e97d5de587d0eec384c00e4708916039557|.04478373|0|2|
| /Users/cam/.codex/worktrees/scout091-docweb-20261013; codex/scout091-docweb-20261013 |5917251340e9c39fbfa69f62d6d31fa8eb8e7d56|.21462848|.00256|12 (text4/visual8)|
| /Users/cam/.codex/worktrees/scout091-boardgame-20261013; codex/scout091-boardgame-20261013 |a1ee431ad19a877cf1d8d5dc57f4a709c9cd90c2|.02408810|.00256|2|

**Campaign knownUSD.28350031; unresolved exposureUSD.00512; conservative total
USD.28862031 ofUSD16.** DocWebtext.16196998/4,visual.05265850+.00256/8.
Unknowns are two ScaleDown400responses with no usage; never silently zeroed.
Usage-derived costs, not invoice proof.668providerattempts/666valid;
0paidjudges/semanticretries. Subject versus qualification/fallback costs are
separate in ownerledgers. Fullplanner/workflow savings and private eligibility
remainunmeasured. Repeats do not increase independent document/case sample size.

Durable direct owner records:

- [Echo attempt](/Users/cam/.codex/worktrees/scout091-echo-20261013/docs/evals/attempts/control-intent-v1/20261013-scout091-five-decision-models.md),
  [manifest](/Users/cam/.codex/worktrees/scout091-echo-20261013/docs/evals/attempts/control-intent-v1/20261013-scout091-five-decision-models.manifest.json),
  [source-selected applicability](/Users/cam/.codex/worktrees/scout091-echo-20261013/docs/evals/attempts/control-intent-v1/20261013-scout091-applicability.json).
- [Doc Web attempt](/Users/cam/.codex/worktrees/scout091-docweb-20261013/docs/evals/attempts/070-scout091-five-decision-models.md),
  [text summary](/Users/cam/.codex/worktrees/scout091-docweb-20261013/docs/evals/evidence/070-scout091/text-summary.json),
  [visual summary](/Users/cam/.codex/worktrees/scout091-docweb-20261013/docs/evals/evidence/070-scout091/image-summary.json).
- [Board Game attempt](/Users/cam/.codex/worktrees/scout091-boardgame-20261013/docs/evals/attempts/20261013-scout091-orientation.md),
  [owner verdict](/Users/cam/.codex/worktrees/scout091-boardgame-20261013/benchmarks/results/synthetic-orientation-v1/20261013-scout091/owner-verdict.json).

Existing ownercredentials used only through normal wrappers. Board's one
temporarily injectedOPENROUTER_API_KEY removed/absence verified; no Echo/DocWeb
injections or secretcopies. Primarycheckouts preserved, all ownerworktrees and
scaffolding retained uncommitted; no commits/push/rollout/defaultchanges.

Root independently reviewed rendered Echo/DocWeb/Boardpreflights and arithmetic,
ran Echo saved-native replay, verified618Echo rawartifacthashes and122Board
manifestentries, inspected Board inputcontactsheet and DocWeb clippedseal
source/cropcontactsheet. Initial Echo zero-cost draft differed from finalfreeze;
paidnative executioncode42a67cde... and preflight716a2e46... are preserved exactly.
Later applicability/replay tools are independentlyhashed; no post-call subject
code change claimed to produce prior scores. Board initialexecutionrunner and
later offline reporting denominators likewise retained separately. DocWeb typed
usage parser repair reused saved rawreplies, never resent qualification calls.

Practical result: avoids an inaccurate cheap interactive route and automatic
visualreview clearance, while identifying one economical batchquality lead
without claiming wholeworkflow savings. Solar's source-aware batch role is a conditional lead, not an immediate new
paid experiment; other unchanged challenger lanes have no demonstrated reason
to rerun.

### Final strategic checkpoint — first review

At the approximately30minute closeout checkpoint, a separate bounded read-only
reviewer was dispatched with raw owner results before root recommendations.
Requested configuration:gpt-6-astra/ultra, strongest eligible advertised
configuration; servedidentity independentlyunverified. Review scope: whether
these task-level decisions satisfy Cam's independent new-model inquiry, practical
payoff vs nominal token savings, small-sample/current-input limitations and
whether another experiment is justified. No provider call, accountchange,
scopeextension or schedule authorized by review. Earlier root reviews corrected
usage parsing withoutresends, separated source-gapclean fromdefectclean, and
exposed original48vsactualruntimeinput applicability. Reviewer verdict: continue closeout, stop this paid campaign and defer another
paid Solar screen. Requested reviewer gpt-6-astra/ultra; independently verified
served identity unavailable.
Root also restored/hashverified all702DocWeb rawreceipts and53manifestentries;
scopedConductor whitespace/arithmetic/local evidence links passed. All paid
owner processes finished; no newcalls needed to close the selected campaign.


#### Strategic disposition and bounded consumer trace

Initial independent review from raw results agrees the authorized goal is
handled: useful uncertainty resolved, no substitution justified at current
runtime boundaries. Root accepts its change from immediate Solar advancement
to conditional batch lead. Original recommendations/results preserved above;
this dated disposition controls the next action. No new selection or paid run
is offered merely to find a favorable winner.

General problem class: reliable acceptance under incomplete evidence. A
meaningfully different established mechanism is selective prediction/abstention
with controlled error-vs-coverage, rather than a broader model tournament:
[Gangrade et al., Selective Classification via One-Sided Prediction](https://proceedings.mlr.press/v130/gangrade21a.html).
The primary paper supports the abstention mechanism, not these providers'
self-confidence calibration or a transferable threshold. Do not train a new
threshold on exposed cases or infer a working veto from gold/fixture IDs.

Root performed one bounded read-only current-owner consumer trace, no provider
calls/artifact execution or target modifications:

- [Planner main](/Users/cam/.codex/worktrees/scout091-docweb-20261013/modules/validate/plan_onward_document_consistency_v1/main.py:1290)
  calls the full generative planner, builds outputs and saves canonical artifacts
  before optional Jev shadow and disabled Perplexity eval sidecars. There is no
  Solar caller or classifier early exit replacing the required planner.
- [Current source guards](/Users/cam/.codex/worktrees/scout091-docweb-20261013/modules/validate/plan_onward_document_consistency_v1/pplx_shadow.py:355)
  already preserve observable source incompleteness, authoritative uncertainty,
  explicit uncertainty and deterministic layout review. The planner's output
  guard also preserves finding uncertainty and the defined unresolved source
  context. This code establishes an existing mechanism, not proof Solar's new
  synthetic maintenance09 error is caught by the real path; that mapping is
  unmeasured.
- Therefore replacing the narrow classifier could save approximatelyUSD.88 per
  1000classifications, but adding Solar at this existing sidecar seam retains
  full planner cost and adds candidate latency/cost. Whole-workflow cost/quality,
  generated reasons/repair and useful review savings are unmeasured.

**Final next action: stop new paid work.** Reopen Solar only when the owner names
an actual worthwhile batch consumer, defines source-grounded uncertainty/reasons
and shows the output can change useful review or task cost. Then produce one
connected qualification plan with frozen independent eligible inputs, preserved
acceptance and bounded spend; no confidence tuning, defaults or rollout implied.
The current report/ledger is complete. No new approval package, schedule or
unnecessary benchmark extension is warranted now.

[Coordinator verification](evidence/scout-091-coordinator-verification.json) records
final caps, evidence checks, strategic disposition and cleanup.


## Scoped check-in and push — 2026-10-13

Cam requested check-in and push after the completed evaluation. Finish-and-push
covers the three linked owner worktrees and this supervisor record. All four
repositories are preflighted before any push; owner evidence lands before the
Conductor record. Runtime defaults and evaluation verdicts remain unchanged.
No paid evaluations are rerun. Existing focused checks are reused where their
input hashes still match; closeout/integration changes get affected checks.

Conductor landing uses a fresh worktree from remote main at
92f8db652d4d52457dd016bf2cbe1263be4af8fc, branch
codex/scout091-conductor-closeout-20261013. Only Scout091 report, two evidence
JSON files, its evaluated-model ledger section, scout index entry and reviewed
inbox capture are included. Older unrelated primary-checkout edits are excluded.
Conductor lint, methodology freshness, scoped whitespace, JSON and evidence
link checks passed. Owner landing states will be recorded below after remote
verification; no worktree cleanup is requested.


### Verified owner landings

| Repository | Remote main and execution-branch commit | Validation |
| --- | --- | --- |
| echo-forge | [8d2e539](https://github.com/copperdogma/echo-forge/commit/8d2e539f06adc7eae0a66fc829484f5c6e192b8a) | 6 focused tests and fresh-clone portable unit proof; ESLint, methodology and native replay |
| doc-web | [91cd9bb](https://github.com/copperdogma/doc-web/commit/91cd9bb19b174247349f1e83b9aaa869eb08ccc7) | 41 applicable focused tests, Ruff, methodology and 702-receipt reconstruction |
| boardgame-ingester | [23ad2cf](https://github.com/copperdogma/boardgame-ingester/commit/23ad2cf8ba8e08fe82d1c28bcb1abb85999a74ab) | Applicable focused tests, lint, methodology, manifest and exact pixel/inverse checks |

All owner remote refs were independently checked using git ls-remote. Each
landing was a normal fast-forward from its evaluated base; no integration
changes or force pushes were needed. Worktrees are clean and retained, with
ignored evidence preserved. Primary checkouts and unrelated captures/private
inputs remain untouched. Doc Web closeout made tests archive-portable and
protected closed preflights from overwrite; original paid execution snapshots
remain intact. Echo proved default unit portability in a fresh temporary clone
with network, protected receipts and owner environment reads forbidden.

Conductor's campaign-only commit follows these owner landings. Its exact commit
identity is provided by the Git history containing this record, avoiding a
self-referential commit hash inside its own content. Root verifies its execution
branch and remote main after push. No extra provider calls, model defaults,
rollout or deployment are part of check-in.
