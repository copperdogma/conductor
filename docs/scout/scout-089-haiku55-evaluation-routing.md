# Scout 089 — Claude Haiku 5.5 evaluation routing

Date: 2026-10-07 (America/Edmonton)
Status: Stage 2 completed; original Stage 1 recommendation preserved below.
Six owner campaigns plus approved public orientation follow-through,
USD1.501511115 combined maximum accounted exposure; no model rollout.
Evaluation-time authorization statements below are historical; the later
finish-and-push request authorizes the scoped landing recorded at the end.

## Verified candidate at Stage 1

- Anthropic [release](https://www.anthropic.com/claude-haiku-5-5) and
  [model catalog](https://platform.claude.com/docs/en/models/overview): announced
  October 7 and API-listed as `claude-haiku-5-5`, native Messages API
  `POST /v1/messages`. **Access: unverified**. No authenticated discovery.
- Text/image input, text output, 1M context and 128K maximum output. Ordered
  images can exercise frame understanding; no native video/audio inference or
  generation is established. [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
  lists Haiku 5.5 for JSON schema and strict tools; owner contract still needs qualification.
- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort):
  low/medium/high/xhigh/max, default medium, adaptive thinking. Thinking can be
  disabled at high or below. Proposed fixed arms: medium adaptive for semantic,
  document and frame tasks; low/disabled for persona, photo, intent and orientation.
  Reserve thinking within total output; do not inherit Haiku 4.5 parameters.
- USD per million tokens: input/output **0.10/0.50 up to 100K input**, **0.50/2.50
  above 100K**; cache reads 0.01/0.05. Tokenizer changes mean per-token savings
  are not measured task savings. Reprice and reserve actual rendered requests.
- [Retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention):
  no training without express permission; organization/feature controls govern
  retention and ZDR. Account ZDR is unverified; do not assert enabled. Only
  explicitly synthetic or owner-cleared public inputs below are selected.
  No private/licensed-restricted/unclear payload or account changes authorized.

No matching Haiku 5.5 attempt in `docs/model-watch/evaluated-models.md`.
Haiku 4.5 and Sonnet 5.5 are distinct candidates. Their failures identify
challenging cases, not a reason to reject this checkpoint unmeasured.

## Stable execution handles

Fresh matched controls, exact prompts/fixtures/contracts and independent source
review apply throughout. Stop only the affected lane on a valid decisive miss;
retain other independent lanes. Owner instructions control stricter gates.

1. **Storybook — Evaluate now; USD2.00.** First `luna-persona`: 12 synthetic
   turns/seven independent groups versus fresh GPT-6 Luna none. Preserve all
   assertions, continuity/no-therapy/source boundaries, <=5s and <=USD0.01/turn.
   Then independent `story056-photo-understanding`: FS-001 and FS-006 synthetic
   photo/letter stand-ins versus Gemini 2.5 Flash-Lite; actual prompt-only JSON
   plus Zod, all assertions, <=5s and <=USD0.001/photo. Stop each lane on its own
   source-confirmed boundary failure. Prior 2325-input/674-output shape implies
   about USD0.00057 at new prices, so old Claude cost exclusions no longer apply.
   Two easy images establish screening only. Persona candidate 12 at8K input/
   2048 output reserve0.021888; Luna control0.02; paired GPT5 judgments with
   prior16K-input/4096-output bounds reserve0.7315. Photo subjects/controls0.10
   allowance. Also independently compare Story150/167 relationship-correction
   routing on12 synthetic cases twice, against optimized Haiku4.5 with the
   real full interpreter fallback: preserve identity/action/ambiguity guards,
   no worse complete-task quality/cost, target>=30% routing-p95 reduction.
   Reserve0.30 for full paired routing/fallback based on prior75-call0.1191
   evidence, leaving >0.82 for qualification/recovery. Do not shorten outputs
   merely to manufacture a per-photo cost pass.
2. **Echo Forge — Evaluate now; USD1.50.** `control-intent-v1`, 42 frozen
   synthetic runtime-shaped cases versus fresh Gemini3.8 Flash low:19 controls,
   20 negatives,3 ambiguous. Strict one-label JSON,15s deadline, deterministic
   scoring/no paid judge. Start admission differentiators then full42. Preserve
   recall and do not worsen false activation/ambiguity; compare quality, p95
   and cost. Recent Gemini40/42 leaves headroom. Candidate at6K input/2048
   output reserves0.06821; prior fresh-control reservation0.5116 leaves >0.92
   for qualification/recovery. Independently run `scene-to-soundscape-golden`
   on its two owner-cleared public scene texts versus fresh GPT5.4 Mini,
   medium adaptive candidate: strict maintained schema and both semantic
   goldens, stop on hard omitted/misread layers. No paid judge; reserve0.20
   for paired subjects/probes, leaving >0.72 for remaining recovery. The
   registry explicitly admits a new model/provider; prior2/2 control is small
   and does not preclude this comparison. No action execution. Whole soundscape workflow
   share unknown; this is a latency-sensitive control subcall comparison.
3. **Doc Web — Evaluate now; USD10.00.** First `image-crop-extraction`,
   Image011 then13 public-cleared pages versus Gemini3 Flash:13/13, score>=0.95,
   source-complete geometry as well as numeric IoU. Independent repaired
   `crop-page-level-deletion-gate`, differentiators then22 versus GPT5.5:
   zero false-safe and22/22 bounded qualification; preserve uncertainty/source
   review and historical versus adjudicated labels separately. Independent
   `handwritten-notes-transcription`, two public LOC pages versus Gemini3.7:
   fidelity>=0.99/page, source-valid goldens first. Also synthetic Story233
   consistency40 judgments/20 unique cases versus GPT4.1 with maintained actual
   fallback: reduce false-clean or equal quality with useful complete-task
   economics; no invented perfection gate. Detector/OCR stop does not cancel
   safety/text. Candidate bounds26K/4096 detector,46K/8192 safety,26K/16384 OCR,
   4096/2048 text reserve about0.297 total; controls/fallback approximately
   0.329+6.412+0.162+0.758=7.661, leaving >2.04 for probes/recovery. No paid
   judge. Full-pipeline stage share unknown; no total-book savings claim.
4. **Dossier — Evaluate now; USD5.00.** `standalone-semantic-value`, two
   synthetic namesakes snapshots/shared authored histories versus fresh GPT6
   Astra medium, the lane comparator. Current extraction default is a separate
   decision. Strict SemanticGraph/compiler then full source-meaning reviews:
   no material omission/unsupported assertion, compiler validity insufficient.
   Independent Opus4.6 reviews both arms. Astra bound2.4003 plus four reviews
   at0.39992 leaves1.00002 for candidate subjects/probes/recovery; candidate
   two100K-input/16K-total-output reservations0.036 fit comfortably. Seek
   complete meaning at lower task cost; two exposed snapshots cannot support
   broad production promotion.
5. **CineForge — Evaluate now; USD3.00.** First `video-understanding` v4,
   six synthetic cases/five ordered JPEGs versus fresh GPT6 Luna low. Qualify
   actual five-image/schema transport; first case then six if admitted.
   Overall>=0.80,<=15s,<=USD0.02/subject; report source-grounding and paired
   quality. Headless research reference, no shipped analyzer to replace.
   Independent runtime-shaped `script-bible` starts authored Open Frequency,
   then The Mariner if admitted versus current Gemini3.5 Flash-Lite reference:
   actual production schema/prompt,>=0.90,<=30s,<=USD0.01/subject. Do not use
   historical one-screenplay aggregates as current parity. Six frame candidate
   reservations106K input/8192 total output at long tier total0.441; two bible
   candidates at100K/16K reserve0.036. Controls0.40 and cross-provider Opus
   judging1.50 allowance leave0.623 for probes/recovery. Exact resolved matrix
   and judge reservations must fit before dispatch. Other character/scene/
   screenplay-QA corpora require separate runtime/corpus eligibility, so no
   unbounded creative-model tournament or audio/image generation comparison.
6. **Board Game Ingester — Evaluate now; USD1.00.** `asset-orientation` /
   `synthetic-orientation-v1`:14 authored images,12 determinate rotations plus
   symmetry/ambiguous-art review, versus fresh GPT6.1 Sol low and provider-free
   blind baseline. Preserve12/12 and both review gates, actual reason field,
   native resolution/inverse/pixel/hash/provenance proof. Target>=30% lower p95
   or stage cost at equal quality. Candidate14 at4096 input/2048 output reserves
   0.022 with1.25x input reserve; prior Sol reservation0.43008 leaves >0.54
   for probes/recovery. Add the native Anthropic subject adapter; current
   runner supports OpenAI/Gemini only, so qualify schema and generated reason.
   Different from physical deskew or licensed Robo Rally inputs; private real
   crops previously approved for OpenAI are not approved for Anthropic.

**Campaign maximum: USD22.50.** These are inclusive hard ceilings on selection,
not invoice forecasts; no inter-owner transfers. Reconcile current rates,
rendered case matrix, prompts, exact subjects/judges, full reservations, caches
and independent grouping before paid batches. Unknown exposure stays reserved.
Recoverable harness/judge defects can be repaired within scope/cap; never tune
quality gates. Full adoption needs more than a small screen.

## Not recommended now

- **Financial Hub — Defer:** private transactional inputs; no maintained
  eligible synthetic model comparison established. No private data authorization.
- **Financial Monthly Analysis — Defer:** private reconciliation/proposal
  workflow; no maintained eligible synthetic provider-comparison lane.
- **Robo Rally — Do not evaluate:** deterministic rules/bots/replay, no
  maintained model inference decision; private rulebook excluded.
- **Ultima IV Web — Do not evaluate:** original-runtime recovery/differential
  testing, no maintained product model comparison.
- **VLC Thumbs — Do not evaluate:** native decoding/cache/bookmarks, explicitly
  no product inference requirement.

Conductor itself has no maintained labeled inference benchmark. Matching tasks
omitted within positive owners: Storybook fusion/linking/identity merging need
separate frozen source-eligible false-merge/rationale contracts. Selected routing
requires full-fallback economics and cannot be inferred from persona. Dossier long
extraction/recovery/scale need broader accepted histories; tiny namesakes cannot
qualify them. Echo's selected scene/soundscape lane remains independent of
intent; generated audio itself is a modality mismatch. Board Game source roles,
counts/member admission/cropping lack an eligible representative synthetic
inference lane; Tideglass package tests alone do not qualify real-source work.
Doc Web whole-book/table generation is separate corpus scope, reference
resolution is deterministic. Neither model marketing nor Git presence clears
private/licensed fixtures.

## Evidence and scope

All eleven `projects.yaml` owners inspected read-only, including instructions,
Ideal/spec and maintained registries where present. Lower-cost owner inspectors
supplemented coordinator review; coordinator corrected stale Board Game
orientation omission using Story021 and yesterday's actual campaign.

- [Previous full owner bounds and recent measured results](scout-084-mistral-large4-evaluation-routing.md)
- [Current synthetic orientation/consistency campaign](scout-086-openai-decisions-api-evaluation-routing.md)
- [Dossier owner registry](/Users/cam/Documents/Projects/dossier/docs/evals/registry.yaml)
- [Storybook owner registry](/Users/cam/Documents/Projects/Storybook/storybook/docs/evals/registry.yaml)
- [Doc Web owner registry](/Users/cam/Documents/Projects/doc-web/docs/evals/registry.yaml)
- [CineForge owner registry](/Users/cam/Documents/Projects/cine-forge/docs/evals/registry.yaml)
- [Board Game Story021](/Users/cam/Documents/Projects/boardgame-ingester/docs/stories/story-021-harden-orientation-goldens-and-decision-subject.md)
- [Echo owner registry](/Users/cam/Documents/Projects/echo-forge/docs/evals/registry.yaml)

Selection authorizes isolated owner evaluation/temporary selected-provider key
custody only, not private inputs/defaults/deployment/commit/push. Ledger remains
unchanged until authenticated owner qualification. No account access has been
tested. This recommendation is preserved so execution handles remain stable.

Reply `yes` to run all numbered evaluations, or name a subset.

## Approved execution — 2026-10-07

Cam selected all six and explicitly requested different thinking settings where
useful to find the best value. Inclusive owner ceilings remain Storybook2,
Echo1.50, Doc Web10, Dossier5, CineForge3, Board Game1; totalUSD22.50.
Six isolated owner workers were dispatched before any owner paid call was
authorized. Coordinator read the custody and portable execution protocols
completely. Central helper presence/check passed; no direct Anthropic provider
is configured there. Prefer existing owner direct credentials; only selected
OpenRouter eval access may be temporarily injected if an owner lacks direct
access. No credential values are recorded or transferred through messages.

Owners predeclare up to three meaningful effort configurations: low/disabled,
medium/adaptive and high/adaptive where warranted. Calibration is fixed before
scores; freeze a best-value arm for independent remaining cases or predeclared
confirmation, and label reused exposed fixtures exploratory. A low-arm failure
does not cancel an already predeclared higher arm. No tuning of quality gates,
private uploads, runtime defaults, deployment, commits or pushes authorized.

All six owners report existing direct Anthropic credentials via their sanctioned
owner wrappers; no central injection was needed. Coordinator independently
verified these isolated branch bases:

| Owner | Worktree | Fetched base |
| --- | --- | --- |
| Storybook | `/Users/cam/.codex/worktrees/haiku55-storybook-20261007` | `c46a4d14f2a29ce8a82d65700836d6fb22abf82e` |
| Echo Forge | `/Users/cam/.codex/worktrees/haiku55-echo/echo-forge` | `16856a0310eeb185b1dcba847b75faa4cbb4dba7` |
| Doc Web | `/Users/cam/.codex/worktrees/haiku55-eval-20261007/doc-web` | `cff6771a01ba202b8eb39e13a604a932708e2278` |
| Dossier | `/Users/cam/Documents/Projects/dossier-haiku55-eval-20261007` | `fbf88cda785ccaa0bafdfb56d89e09a79e6212b5` |
| CineForge | `/Users/cam/Documents/Projects/cine-forge-haiku55-eval` | `d358224da24e0ca5a6774c92287d70cf69389864` |
| Board Game Ingester | `/Users/cam/Documents/Projects/boardgame-ingester-haiku55-eval` | `151c13fc01deb1fefc193264f4435fc8946e27f4` |

Opus is same-provider for Haiku subjects; those grades are supportive only.
Coordinator cross-provider Codex source reviews will independently adjudicate
decision-bearing Haiku semantic/Bible/frame evidence under the owner contracts.

## Closing strategic checkpoint — 2026-10-07

Aligned; finish the bounded comparisons and stop paid exploration. No earlier
strategic checkpoint recommendation was found in this campaign record. The
approved six-owner plan and effort comparisons were executed, with source
inspection correcting misleading apparent wins before adoption decisions.
Cam can now prioritize one orientation promotion check and avoid five
quality-losing replacements. More exposed-case effort trials would displace
representative orientation qualification without changing the rejected arms.

The general problem is evaluation validity: a rubric pass may omit required
source facts, while a lexical failure may reject an acceptable paraphrase.
[Anthropic's evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
compares deterministic, model and human graders and recommends evaluating
outcomes as well as traces. We adopted complementary deterministic proofs and
cross-provider source review rather than relying on judge consensus; an
alternative is broader repeated held-out evaluation. That alternative is useful
for orientation promotion, but cannot repair a demonstrated missing-name or
false-safe failure by averaging it away. Local discriminators: Board Game's49
independent pixel/inverse checks; Dossier producer-contract inspection;
CineForge first/final pixels and source script; Doc Web crop overlays.
These checks changed concrete verdicts without changing goldens or prompts.

Disposition: close this campaign, preserve disputed grades and operational
failures, prioritize representative orientation evidence. No new schedule,
runtime rollout or paid retry is authorized by this checkpoint. Reassess only
on a separately approved promotion package or a narrow ledger retry trigger.

## Completed owner decisions — 2026-10-07

**Prioritize Haiku adaptive medium for a bounded orientation promotion check;
retain the current models for the other tested tasks.** The orientation win is
synthetic-only, not permission to upload private scans or change defaults.
Every comparison below uses fresh matched subject/control requests except the
explicitly diagnostic scene lane; later cases stopped by valid gates remain
unmeasured. Configuration-selection fixtures are exposed and not held out.

| Owner/task | Effort comparison and quality | Measured task economics/latency | Action |
| --- | --- | --- | --- |
| Storybook persona | Medium2/2 calibration; fresh3 confirmation turns:1 paid pass,1 disputed interpretation,1 clear advice failure vs Luna3/3. Low passes exposed no-advice diagnostic but initial follow-up lexical rubric conflict retained. | Medium3 $.0015861/p952.856s vs Luna $.00013581/p953.753s. Remaining9 unmeasured. | Retain Luna; no high arm warranted by original task contract. Initial favorable calibration does not establish repeat reliability. |
| Storybook photo/OCR | Both low/medium accurate caption/text on2 synthetic fixtures; all arms including Gemini fail FS001 lexical detail-placement check; FS006 all assertions pass. | FS006 low $.0005047/3.407s, medium $.0007519/6.654s vs Gemini $.0001586/3.339s. Medium exceeds5s. | Retain Gemini; low best Haiku but3.18x OCR cost. Preserve source-grounded lexical dispute, not hallucination finding or full production parity. |
| Storybook relationship route/full cascade | Low misses absent-target confirmation without inventing IDs/unsafe action. Medium fixes it, freezes before12x2; both medium/current modes24/24 and complete cascades24/24, no unsafe/invented IDs. | Medium actual complete path $.0737514 vs current $.0742064 (0.61% less), p957.238s vs4.541s (59.4% slower); predicate p953.890s vs.448s. | Retain current native Decisions endpoint with full Haiku fallback/confirmation guard. High not admitted after medium semantic success.12 unique synthetic cases/two repeats, exposed differentiator selection disclosed. |
| Board Game orientation | Low2/4 determinate calibration; medium12/12 plus both holds, ties fresh Sol; high fixes one low miss but adds no medium quality. Medium frozen before8 remaining cases,8/8 each. | Medium14 subject calls $.0038286 vs Sol $.02363; p95 5.561s vs7.760s:83.8% cheaper,28.3% lower p95. | Prioritize promotion check; cost clears30% gate, latency alone does not. Only14 authored images, holds used in calibration. |
| Echo intent | Low3/5, medium4/5, high4/5 exposed calibration; frozen medium37/42 vs Gemini40/42,2 vs1 false controls,0/3 vs2/3 ambiguity holds. | Medium42 $.0044911 vs $.0291525; p95 2.239s vs4.770s. High calibration39.8% costlier than medium with identical labels. | Retain Gemini; cheaper/faster fails quality. No high full42 after failed improvement gate. |
| Echo scene | Native schema numeric constraints/grammar compilation block parity; original-validator Tavern diagnostic medium2 policy misses, high1. | Medium $.0025171/18.895s; high $.0030836/23.246s. Fresh GPT and Dungeon unmeasured. | Retain GPT5.4mini operationally; no relative quality claim or qualified fallback. |
| Doc Web detector | Image011 medium.5435, low invalid bounds, high.9242 but source clipping; Gemini.9826 source-complete. | Medium $.0005549/2.514s; low $.0006108/2.591s; high $.0007714/4.620s vs Gemini $.0045395/7.895s. Full13 unmeasured. | Retain detector; high fixes grouping but clips logo/seal. |
| Doc Web safety | All3 effort arms1/2, each falsely clears amputated source; fresh GPT2/2. | Medium2 $.0019452/median3.651s; low $.0019755/3.653s; high $.0022662/5.307s vs GPT $.06419/4.619s. Full22 unmeasured. | Retain GPT safety; separate from detector failure. |
| Doc Web handwriting | Barney medium.959162, low.945640, high.942693 vs Gemini.980617; all below.99. | Medium $.0009911/7.672s; low $.000422/3.457s; high $.0012986/9.642s; Gemini $.0073575/7.482s. | Retain current OCR provisionally; neither current nor candidate qualifies this calibration. Alverson unmeasured. |
| Doc Web consistency | All3 arms4/5 calibration; frozen low25/40 (.625), macroF1.58745 vs GPT29/40 (.725),.71169. False-clean format defects3 vs4. | Low $.0041735 vs $.043392; median1.1535s vs.8575s, p951.371s vs1.976s.20 unique cases/two synthetic sources, repeated twice. | Retain planner; overall quality lower. Fresh Jev/cascade unmeasured: owner key absent, unselected-provider injection prohibited. No invented confidence route. |
| Dossier namesakes | Strict native grammar too large. Prompt-only diagnostic low invalid enum; medium two snapshots and high first omit required familiar-name facts. Fresh Astra preserves names. | Successful medium pair $.0054471/28.739s vs Astra $.25817/60.792s; including medium truncation $.0085238/47.806s. Different schema enforcement prevents parity claim. | Retain Astra; no quality tie. High continuation stopped when high calibration omission established. One synthetic family, authored identical histories, no wider reliability proof. |
| CineForge ordered frames | All3 arms miss source-visible enlargement in first of6 cases; Luna identifies it. Independent Sol combined low.5253/medium.5303/high.57665 vs Luna.795; all below absolute.80. | Haiku $.0006536–.0010302/3.806–6.777s vs Luna warm $.00023967/5.311s.5 later cases unmeasured. | Retain Luna reference; no absolute winner or production frame caller. |
| CineForge runtime Bible | Low/medium aggregate.75995, high.77495 vs Gemini.75995; all hard deterministic.6999. High improves partition but invents source facts; Gemini also has source errors. | Low $.0013002/12.804s; medium $.0014643/12.338s; high $.0022213/19.381s vs Gemini $.0030376/5.525s. | Retain current config provisionally; no qualified winner. Mariner unmeasured. Lexical theme ambiguity kept separate from actual unsupported facts. |

Medium is the tested value choice for orientation and the best tested Haiku
intent arm; low is cheapest for the exposed Doc Web classifier calibration.
High improves selected structures but does not justify a global high setting.
There is no qualified mixed-model routing package: identifiable production
boundaries exist, but their candidate quality/contract gates failed. Orientation
is already a separate runtime task and is the one promising boundary.

Source review preserved and corrected initial grades rather than overwriting
history. In Dossier, both paid supportive reviews and initial blind Codex reviews
accepted the authored three obligations while missing familiar-name completeness;
producer-contract supplements control the final verdict. Display labels cannot
substitute for affirmed has_name facts. In CineForge, favorable Opus Bible grades
missed breed/location inventions; independent source review prevents promotion.
Same-provider Opus grades are supportive only. The independent Codex reviewer
used GPT6Astra max, consumes session usage, and made no benchmark-provider call.

### Owner evidence and validation

- [Storybook Attempt180](/Users/cam/.codex/worktrees/haiku55-storybook-20261007/docs/evals/attempts/180-haiku55-portfolio.md):179 settled calls; exact native usage/scorer replay;11 focused tests, syntax/methodology/diff passed. Global privacy review is pre-existing expired; this synthetic-only campaign does not qualify private uploads. Evaluation-completion manifest audit verified697 artifacts plus5 final source files; close-out adds offline validation records and binds700 artifacts plus6 final source files. Current fetched base's Story191 uses native OpenAI Decisions routing, superseding the proposal's historical Haiku4.5 comparator assumption; controls use the actual current caller, not a stale substitute. Persona judge disagreement and low routing's safe UNKNOWN are preserved separately from valid failures. Derived low calibration summary was reconstructed from untouched original grades, with overwritten tail-only aggregate preserved.
- [Board Game owner attempt](/Users/cam/Documents/Projects/boardgame-ingester-haiku55-eval/docs/evals/attempts/20261007-haiku55-orientation.md):35 valid calls plus one zero-cost400;43 focused tests/lint/compile/methodology. Coordinator verified185 manifest files,49 exact pixel/inverse derivations, usage-priced arm sums and p95.
- [Echo owner attempt](/Users/cam/.codex/worktrees/haiku55-echo/echo-forge/docs/evals/attempts/control-intent-v1/20261007-anthropic-claude-haiku-5-5.md):113 attempts/106 valid receipts;8 focused tests, receipt replay/syntax/methodology. Four recovered Gemini503s and accidentally imported CLI's five duplicate calls plus one interrupted call are retained; duplicates excluded from quality, import-safe guard tested with zero dispatches.
- [Doc Web Attempt068](/Users/cam/.codex/worktrees/haiku55-eval-20261007/doc-web/docs/evals/attempts/068-haiku55-maintained-evaluation.md):110 dispatches/109 unique successful IDs;13 focused tests, Ruff, methodology; lossless356-file archive independently reconstructed. Startup temperature400 is adapter failure, not semantic loss. Coordinator source overlay review independently confirms clipping.
- [Dossier Attempt025](/Users/cam/Documents/Projects/dossier-haiku55-eval-20261007/docs/evals/attempts/025-haiku55-namesakes-20261007.md):10 subject/transport records,11 canonical reviewed artifacts,3 focused tests. Original generic passes retained; fresh source-contract supplements formally grade medium0/high0/medium1 material_failure. Final148-file custody independently hash/size verified. Two grammar400s and both token-budget truncations retained; adequate output recovery did not change effort or gates.
- [CineForge Attempt049](/Users/cam/Documents/Projects/cine-forge-haiku55-eval/docs/evals/attempts/049-haiku55-thinking-value.md):23 settled calls;34 focused tests, Ruff, offline parity/schema/freezes, methodology. Coordinator read exact saved Bible outputs/source and viewed first/final frames. Some independent task calls overlapped, so global serial execution is not claimed.

All six owners qualified exact direct Anthropic `claude-haiku-5-5` access through
existing owner credentials. No central key injection/copy/cleanup was needed.
Text/image response contract support is task-specific: simpler native strict
schemas worked, while Dossier and Echo scene strict grammar limits remain
blocked. Prompt-only diagnostics do not establish production parity. No
private/licensed payloads or account-settings changes occurred. All worktrees
remain uncommitted; runtime defaults, deployment and primary owner checkouts
were not changed.

[Coordinator verification](evidence/scout-089-coordinator-verification.json)
binds independent manifest audits, source-review hashes, actual spend and scope.
The four first completed owner manifests cover843 exact hash/size matches;
Board Game adds185 and49 independently checked pixel derivations. Final
Storybook and supplemented Dossier evidence are checked at closeout as recorded
in that receipt: evaluation-completion total1736 hash/size entries passed; close-out verifies1740 entries after four Storybook tooling/validation additions. Owner focused tests and source inspections are reused on
unchanged inputs; Conductor documentation/link/whitespace checks require no
product suite. An unrelated pre-existing historical ledger link is unavailable
and is identified in the receipt, not silently repaired by this campaign.

### Inclusive spend and stopping boundary

All amounts are USD usage-priced estimates, not reconciled invoices. Unknown
requests retain their conservative full reservation, even HTTP400/503s with no
usage. Subjects, fresh controls, paid judges, qualification and operational
overhead are included; session Codex usage is separate from these provider caps.

| Owner | Settled estimate | Unknown reserved | Maximum exposure | Hard cap |
| --- | ---: | ---: | ---: | ---: |
| Storybook | .40534642 | 0 | .40534642 | 2 |
| Echo | .04124850 | .08690650 | .12815500 | 1.50 |
| Doc Web | .13654200 | .01144200 | .14798400 | 10 |
| Dossier | .58463090 | .01174625 | .59637715 | 5 |
| CineForge | .190395745 | 0 | .190395745 | 3 |
| Board Game | .02880340 | 0 | .02880340 | 1 |
| **Total** | **1.386966965** | **.11009475** | **1.497061715** | **22.50** |

Judge/overhead separation matters: CineForge subjects/qualification $.013299245
versus paid judging $.1770965; Dossier subjects $.2736009 versus Opus reviews
$.31103; Storybook paid judges $.1278705. Echo/Doc Web/Board Game use no paid
judge. Cheap subject prices do not imply the whole campaign costs equally little.
No further paid call is needed to settle this unchanged selected campaign.

Recommended next package: Board Game owner only, same direct Haiku medium and
fresh Sol low, maximumUSD1 inclusive, isolated existing evaluation worktree.
Before any call, freeze12 new independently sourced public/owner-cleared
orientation assets plus symmetry/ambiguous holds, provenance and source ground
truth, excluding every exposed selection fixture and private/licensed-restricted
scan. If sufficient eligible representative assets cannot be established, stop
without uploading substitutes. Preserve zero wrong rotations, both holds,
generated reason/schema, pixel/inverse/provenance proof, and>=30% stage-cost
or p95 improvement. Report real-source quality and workflow share before any
runtime change. This package requires a new explicit selection; no defaults,
private payloads, commit/push or deployment are included.

## Approved representative orientation follow-through — 2026-10-07

Cam replied `Yea` to the explicit USD1 orientation promotion package above.
This selects Board Game only and supplies a new incremental hard inclusive
ceiling; prior synthetic campaign costs/evidence remain separate. Reuse the
existing isolated `codex/haiku55-eval-20261007` owner tree; coordinator current
remote read confirms main still151c13fc01deb1fefc193264f4435fc8946e27f4.
The owner worker reads current instructions, establishes source eligibility,
freezes14 new cases before any inference and returns full local artifacts.
Haiku medium is already frozen from prior synthetic selection; no new effort
tournament or replacement synthetic fixtures. Stop before inference if enough
representative source-eligible assets cannot be established. Existing owner
credentials remain owner-managed; no central injection is planned. All prior
privacy, source fidelity, no-default/no-landing boundaries continue.

Pre-call coordinator source review passes: four Game_assets_66 single-letter
tiles (B/F/G/R,256x256), four Kenney human/house/car/sailboat pieces (64x64),
four distinct /dev/urandom Mahjong tile faces (native24x48 crops of one sheet),
Kenney circular equivalence hold and garrick stone-texture ambiguity hold.
Creator pages explicitly identify CC0 and game/board-game use. These are12
distinct designs in three creator groups plus a fourth hold creator, not12
independent games/scans. Corrections are balanced three each0/90/180/270.
Ambiguous dual-ended animal cards were discarded prospectively before any
inference, without judging model quality. Native image dimensions are preserved;
clean digital art is a new public-source screen, not scanner-robustness proof.
Coordinator independently reproduces14 exact source/crop/alpha-composite/input
pixel transformations,12 inverse corrections, and zero old-fixture hash overlap.
[Promotion verification](evidence/scout-089-orientation-promotion-verification.json)
records creator URLs and byte identities. The distinct public controller must
retain the original authored-fixture guard and qualify native schema/parity;
28 planned calls reserveUSD.616448, leavingUSD.383552 for bounded recovery.

### Representative public check result — stopped at second case

**No promotion winner; retain current Sol configuration and source review.**
Both models correctly keep the first letter tile upright. At second frozen case
pub-012, both return needs_review/null rather than required270. This is a safe
abstention and an automatic-orientation coverage failure, not a wrong rotation
or unsafe action. Native24x48 source tile is rotated90 clockwise into48x24;
the Chinese east glyph 東 has a source-visible asymmetric upright orientation.
Coordinator viewed both exact native images and confirmed unchanged determinate
ground truth; low readability does not retrospectively make the golden ambiguous.
Neither model receives the canonical reference or source context in its request.

| Frozen arm | First two matched cases | Actual two-call cost | Observed latency range |
| --- | --- | ---: | ---: |
| Haiku adaptive medium |1 correct automatic orientation,1 safe abstention |USD.0003614 |2.627–3.283s |
| Sol low |1 correct automatic orientation,1 safe abstention |USD.0040880 |3.512–9.781s |

All four native receipts have exact identities, terminal success, strict schema,
generated reason and valid usage. Independent coordinator price replay matches
the owner amounts. **Incremental settledUSD.0044494 ofUSD1, unknown0; no paid
judge or retry.** Prior synthetic orientationUSD.0288034 remains separate.
Initial portfolio maximum exposureUSD1.497061715 plus this approved follow-up
equalsUSD1.501511115 acrossUSD23.50 total separately authorized ceilings.
The initial six-owner scope and its USD22.50 cap remain unchanged.

Both affected arms stop under the prospective complete-automation quality gate.
Ten other determinate assets and both holds remain unmeasured; no full14 pass,
full-corpus cost/latency saving, Haiku regression versus Sol, scanner robustness,
workflow-share or production promotion claim follows. Four public native model
calls are not a held-out14-case success. No upscale, extra context, changed
effort, repeated subject, tuned golden or replacement case rescues the result.
The previous synthetic value win remains valid within that earlier evidence.
No additional unchanged paid test is recommended. The practical result is that
the cheaper candidate has not demonstrated the coverage needed to replace Sol;
explicit human-review handling remains necessary even for the incumbent.

[Owner follow-through attempt](/Users/cam/Documents/Projects/boardgame-ingester-haiku55-eval/docs/evals/attempts/20261007-haiku55-public-orientation.md),
[spend ledger](/Users/cam/Documents/Projects/boardgame-ingester-haiku55-eval/benchmarks/results/public-orientation-v1/20261007-haiku55-promotion/spend-ledger.json),
[source/input/both outputs](/Users/cam/Documents/Projects/boardgame-ingester-haiku55-eval/benchmarks/results/public-orientation-v1/20261007-haiku55-promotion/pub012-source-input-haiku-sol.png).
Coordinator independently verifies all116 final manifest hashes/sizes and18
output pixel/inverse/hash proofs, alongside the14 source transformations and12
ground-truth inverses already checked before inference. Five fresh public
controller tests pass, including preservation of unknown400 reservations;
43 unchanged native/scorer/executor tests are reused. Compile/lint/methodology/
whitespace checks pass. Small/rotated/non-Latin vision limitations are researched
in the owner attempt as plausible explanations, not established causal proof or
permission to alter the frozen inputs. No defaults, private uploads, account
changes, commits or pushes. No additional unchanged paid call recommended.

## Authorized finish-and-push — 2026-10-07

Cam subsequently requested “Thanks. Finish and push”, authorizing scoped commits,
execution-branch pushes and fast-forward main landings. All seven repositories
were preflighted before the first push. The six owners below are now landed;
coordinator `git ls-remote` independently verifies both remote main and the
`codex/haiku55-eval-20261007` execution branch at each exact commit. Task
worktrees are clean and retained; unrelated primary checkout work is preserved.

| Owner | Verified remote main commit |
| --- | --- |
| Storybook | `1f27f14c0c2a36cbe22314e5adde7a8b1834092d` |
| Echo Forge | `cfeedd4e902c158065d1ae3447ac5bafa52857ba` |
| Dossier | `caae23221af6f145fbf6fae970509bb40a785d2b` |
| CineForge | `1c759686544a2ec85b6c8808f3b4a3966bf8d86e` |
| Doc Web | `3a7bc2c01543c6c2f96cf3febe3dc8234331427b` |
| Board Game Ingester | `7c910d1b1dfe8ece2c704fb90169cef146e113d5` |

[Landing receipt](evidence/scout-089-landing.json) records integration and
validation. Mechanical lint/diagnostic fixes, required changelogs and guarded
evidence-writing entrypoints were checked offline. Original measured requests,
responses, judgments and spend remain preserved; final tooling identities are
bound separately where needed. Board Game integrated concurrent Story039 at
`5d4c4c426bc568e453128dc1e2a8acdb8bb03bf1`; ten focused tests and regenerated
methodology checks pass. Narrow Git attributes preserve raw public license HTML
bytes, with non-raw whitespace checks separate. The updated coordinator audits
verify1740 initial-campaign entries and116 public-follow-up entries; Dossier
final tooling36/36 and Doc Web final mapped sources/allowlist46/46 also pass.

Conductor close-out is limited to this scout, evidence receipts, the Haiku
ledger/index/inbox entries and changelog in a clean integration worktree. Its
lightweight lint/test, methodology, JSON, local-link and whitespace checks pass.
No paid model calls, model-default changes or deployment action accompanied
close-out. Retain incumbents; no additional unchanged paid evaluation is
recommended. Historical authorization and no-landing statements above describe
their original evaluation milestones and are superseded only for this scoped
landing by the subsequent user request.
