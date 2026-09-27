# Scout 076 — GPT-6 Sol and Luna evaluation routing

Date: 2026-09-26
Status: Closed by Cam on 2026-09-27; delivered work complete, billing uncertainty retained as a documented exception.

## Current recommendation

**Use Luna for Storybook's main persona calls and CineForge's inspected headless
ordered-frame analysis. Dossier's Luna-first/Astra-fallback library pilot is qualified by replay.
Retain the current models for Doc Web crop runtime, Echo control intent and
Storybook photos.** Sol improves persona quality over Haiku, but Luna matches
its independently reviewed quality at much lower subject cost.

| Owner/task | Evidence-backed decision | Practical reason |
| --- | --- | --- |
| Storybook main persona | Adopt Luna; integration `8637fde` deployed in release v29 from `ef0c86a` | Independent review: Luna11/12, Sol11/12, Haiku8/12. Luna12-turn subject costUSD0.00114811 versus HaikuUSD0.035099. Keep other roles unchanged. |
| CineForge headless ordered frames | Prefer Luna; qualification landed as `f69909d8df04805fe47615a88d40bf84c839f052` | Corrected v4 comparison0.5986 versus Gemini0.4313, six of six case wins, about5.7x cheaper. Both miss0.80; this is inspected analysis, not autonomous QA. No product inference call exists to switch. |
| Dossier extraction | Opt-in library pilot implemented and replay-qualified; Astra remains default | Prior history-seam measurement55.5% cheaper but19.85s slower. Compiler rejection is observable; semantic omissions can still compile. |
| Doc Web crop runtime | Retain Gemini | Luna leads13-case detector benchmark, but actual runtime raw geometry clips seal/signatures. Safety ownership also remains separate. |
| Echo control intent | Retain Gemini | Runtime-shaped42 cases: Luna37, Sol38, Gemini38 correct. Luna adds a false control; the small savings do not justify that regression. |
| Storybook photo/OCR | Retain Gemini2.5FlashLite | Persona evidence does not qualify the separate photo contract. |

Completed evaluation plus Storybook qualification and CineForge source-truth
repair cost **USD3.784318290** in usage-rated estimates, including judges.
All owner ceilings were respected, with zero unresolved exposure at that
checkpoint. The later Dossier validation deviation has **USD11.039940 unresolved
conservative exposure**, and the Storybook deployment smoke has additional
unquantified exposure. Both are separate from that settled evaluation estimate;
see the accounting exceptions below. Final cap compliance cannot be certified.
This is provider evaluation accounting, not Codex orchestration quota.

Initial proposals, superseded stops and intermediate accounting below are
historical evidence. Current outcome and landing records take precedence.

## Initial Stage 1 identity and route (historical)

OpenAI announced both on September 22. Exact direct API IDs/current snapshots
are `gpt-6-sol` and `gpt-6-luna`. At Stage1 both were API-listed and owner access was unverified; subsequent
owner calls below proved exact native access.
Neither exact subject appeared in the evaluated-model ledger or inspected owner
attempts before this campaign. Earlier Astra and GPT-5.6 results are different candidates. Agent model
labels are not evidence of subject inference. No dated direct snapshot is inferred
from a router name, and no router substitution is proposed.

Both accept text/images and emit text, support structured outputs, and list
1,050,000 context, 922,000 maximum input and 128,000 maximum output tokens.
Reasoning supports none/low/medium/high/xhigh/max, with medium the default.
Responses supports function calls; Chat Completions function calls require none.
Use direct foreground Responses, Standard processing, `store:false`, no hosted
tools. Preserve owner prompts and actual output contracts. API support is not
proof that a particular owner adapter works.

Standard USD per million tokens, at up to 272K input tokens:

| Candidate | Input | Cached input | Cache write | Output |
| --- | ---: | ---: | ---: | ---: |
| GPT-6 Sol | 2.00 | 0.20 | 2.50 | 10.00 |
| GPT-6 Luna | 0.10 | 0.01 | 0.125 | 0.50 |

Long-context requests cost 2x input/cache and 1.5x output; none are proposed.
Luna's listed rates are one twentieth of Sol's, but task cost and latency remain
unmeasured. Reservations must include image accounting, reasoning, cache writes,
qualification, controls and judges. Token prices alone do not prove task value.

API data is not used for training by default. Standard abuse logs may retain
content up to 30 days, with exceptions. ZDR requires approval and has endpoint/
feature limitations; account status is unverified. `store:false` is not ZDR;
prompt-cache state can persist up to 24 hours. Only owner-established public or
synthetic fixtures are proposed. Private, licensed-restricted or unclear inputs
remain excluded. No account-setting changes.

Official pages fetched today:
- [Release](https://developers.openai.com/api/docs/changelog#september-2026)
- [Sol](https://developers.openai.com/api/docs/models/gpt-6-sol)
- [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna)
- [Pricing](https://developers.openai.com/api/docs/pricing)
- [Data controls](https://developers.openai.com/api/docs/guides/your-data)

## Stable execution handles

Every numbered item includes both candidates, qualified independently, and fresh
same-input controls. Each owner cap includes all subject/control/judge exposure.
A cap is a maximum, not a promise to complete downstream stages. Reserve the full
next request before dispatch; unknown billing retains its reservation. No automatic
retries, effort sweeps, cap transfers, other candidate models or default changes.
One candidate's failure does not cancel the other candidate or independent lanes.

1. **Dossier — Evaluate now; USD2.00.** First lane
   `standalone-semantic-value`, Story170, limited to native qualification and
   correction/withdrawal's two chronological snapshots, against fresh
   `gpt-6-astra` medium. Both candidates use medium. Test whether cheaper models
   can preserve the current source-meaning contract; canonical schema/compiler,
   terminal identity and source fidelity remain mandatory. Use identical reference
   histories and the repaired explicit fail-fast runner, 4096 output policy,
   serial dispatch and owner deadline. Stop immediately on contract/compiler or
   budget failure; truncation is transport evidence. Synthetic corpus only.
   Generate model/price-blind source-review packets. There is no maintained
   cross-provider judge: semantic acceptance remains pending independent operator
   review, with no hidden paid judge. OpenAI reviewing OpenAI does not satisfy
   this independence rule. No expansion beyond the correction pair, adoption or
   general superiority claim is authorized by this initial diagnostic.
2. **Doc Web — Evaluate now; USD3.00.** First lane `image-crop-extraction`:
   qualify integer-coordinate image/schema contract, Image011, then full13 and
   fresh Gemini 3 Flash if admitted; require 13/13 and overall >=0.95.
   Independently test `crop-page-level-deletion-gate`: page-122-001 first,
   then full22 versus fresh GPT-5.5 Responses if admitted; require 22/22,
   stop on any false-safe decision. Candidates medium for detector, none for
   safety; fresh controls retain owner settings. Public benchmark images only.
   Compare IoU, grouping, text exclusion, safety, latency and total cost. Detector
   failure does not cancel page safety. Existing exposed safety examples cannot
   authorize removing C5 or promotion without separately frozen held-out truth.
3. **CineForge — Evaluate now; USD1.50.** First lane `video-understanding`
   v3, six source-backed synthetic cases with five ordered JPEGs each; fresh
   Gemini 3.5 Flash-Lite comparison reference, not a passing adopted incumbent.
   Candidates low reasoning. Qualify all five images and output schema, then
   first case, then six only if admitted. Targets overall >=0.80, <=15 seconds,
   <=USD0.02 per subject call. Explicitly retain the maintained cross-provider
   `claude-opus-4-6` rubric judge; verify its price and bound it before dispatch.
   Stop on contract, clear quality or operational/value failure. Current registry
   identifies the repaired six active cases and decision-grade HOLD evidence;
   older broad runbook quarantine language must not reactivate contaminated rows.
   Zero-cost source/scorer preflight must confirm v3 validity or stop unmeasured.
   This evaluates ordered frames, not native video or audio.
4. **Storybook — Evaluate now; USD1.50.** First lane `luna-persona`, 12
   synthetic/golden turns, versus fresh `claude-haiku-4-5-20251001`. Both
   candidates none reasoning, preserving the current prompt and conversation
   grouping. Native qualification, one representative case, then the maintained
   matrix if admitted. Target all assertions passing, <=5 seconds and <=USD0.01
   per turn. The newer-GPT trigger and lower prices justify reopening the value
   question; this is not a retry of the old GPT-5.5 subject. Freeze any maintained
   rubric judge and its cost in preflight; no implicit judge selection.
   Independently run `story056-photo-understanding`: synthetic FS-001 photo,
   then FS-006 scan, versus fresh Gemini 2.5 Flash-Lite. Candidates none reasoning;
   actual JSON/local validation, all assertions, <=5 seconds and <=USD0.001 per
   turn. Sol may stop at the value gate; token price alone is not a reason to
   omit its one-case screen. Reserve actual image/output bounds first. Persona
   and photo/OCR conclusions stay separate. No private photos or transcripts.
5. **Echo Forge — Evaluate now; USD2.00.** First lane `control-intent-v1`,
   frozen48 synthetic cases versus fresh Gemini 3.8 Flash low. Candidates none
   reasoning; qualify strict JSON, positive/negative/ambiguous admissions, then
   full48 while gates and budget hold. Preserve 2048 output and15s deadline;
   stop each candidate on clear false activation, schema failure or timeout.
   Compare exactness, control recall, false activations, abstention, p50/p95 and
   total cost. Judge spend is zero. This can identify a cheaper responsive option
   against current Gemini; historical Grok4.6 is context, not a fresh superiority
   comparison. Code retains target/action/permission. Shared controls may be
   reused across these two candidates only on identical frozen inputs/settings.

**Campaign maximum: USD10.00.** These are progressive ceilings, with zero-cost
resolved matrix, image-token and next-call reservation checks before spending.
Potential worst-case full-matrix totals do not authorize exceeding an owner cap;
stop incomplete when the next full reservation cannot fit. Fresh controls are
needed before comparative conclusions, even when old results are available.

## Owner evidence and omitted lanes

Three lower-cost agents inspected all seven owners read-only; coordinator checked
current official sources, the central ledger, key owner configs and recent failed
campaigns. Primary checkouts are shared/dirty; selected execution uses isolated
current-base worktrees and reconciles maintained eval code without touching them.

- Dossier: [Story170](</Users/cam/.codex/worktrees/opus55-eval-20260926/dossier/docs/stories/story-170-standalone-semantic-value-benchmark.md>),
  [recent report and fail-fast repair](</Users/cam/.codex/worktrees/opus55-eval-20260926/dossier/docs/evals/artifacts/opus55-semantic-20260926/README.md>).
  Defer full semantic/long-narrative/scale screens until independent review of
  this diagnostic; ordinary EntityGraph extraction is a separate older decision.
- Doc Web: [registry](</Users/cam/Documents/Projects/doc-web/docs/evals/registry.yaml>),
  [page gate](</Users/cam/Documents/Projects/doc-web/benchmarks/tasks/crop-page-level-deletion-gate.yaml>).
  Crop-only validation adds no independent page-context decision here; general
  HTML/OCR pipeline quality is not measured by these maintained crop contracts.
- CineForge: [registry](</Users/cam/Documents/Projects/cine-forge/docs/evals/registry.yaml>),
  [frame task](</Users/cam/Documents/Projects/cine-forge/benchmarks/tasks/video-understanding.yaml>),
  [recent source adjudication](scout-073-grok47-evaluation-campaign.md#cineforge-offline-adjudication-complete).
  Defer ScriptBible pending a prospectively settled evidence/journey scoring
  contract. Screenplay QA/second-corpus privacy and truth gates remain separate;
  do not route private screenplays. No audio generation modality match.
- Storybook: [registry](</Users/cam/Documents/Projects/Storybook/storybook/docs/evals/registry.yaml>),
  [persona comparator](</Users/cam/Documents/Projects/Storybook/storybook/packages/backend/src/ai/evals/luna-persona-openai-chat-latest.eval.yaml>).
  Downstream Story060 fusion and separate linking/clustering/correction models
  require their own contract decisions; first establish persona and image value,
  without treating these results as evidence for those downstream tasks.
- Echo Forge: [current comparison corpus](</Users/cam/.codex/worktrees/opus55-eval-20260926/echo-forge/tests/fixtures/golden/control-intent-v1/fixtures.json>),
  [latest attempt](</Users/cam/.codex/worktrees/opus55-eval-20260926/echo-forge/docs/evals/attempts/control-intent-v1/20260926-anthropic-claude-opus-5-5.md>).
  Defer larger scene-to-soundscape extraction: separate output contract and
  unresolved eligibility of some narratives; control intent is the active value
  decision. Neither text classification nor text scene extraction generates audio.

## Not recommended now

- **Board Game Ingester — Defer.** Matching crop/orientation/source-role,
  inventory and rulebook/OCR tasks exist, but current scans include private or
  licensed RoboRally assets without established upload eligibility. Tideglass's
  package contract fixture does not establish an eligible visual corpus. Need
  owner-approved public/synthetic visual fixtures first; ZDR is not permission.
  [Owner registry](</Users/cam/Documents/Projects/boardgame-ingester/docs/evals/registry.yaml>).
- **Robo Rally — Do not evaluate.** Maintained behavior is deterministic game
  and rules execution; no maintained model-owned inference benchmark was found.
  Its private rulebook is not an eligible substitute corpus.
  [Owner instructions](</Users/cam/Documents/Projects/roborally/AGENTS.md>).

No subject calls, credentials, target mutations, runtime defaults, commits or
pushes occurred. The evaluated-model ledger stays unchanged until execution.

Reply `yes` to run all five items, or select numbered items and/or one candidate.
Selection is required by the evaluate-model skill: "Do not run a paid benchmark
or mutate a target repo yet."

## Approved execution — 2026-09-26

Cam replied `Yes`, selecting items1–5 with both exact candidates and the
USD10 total: Dossier2, DocWeb3, CineForge1.50, Storybook1.50, EchoForge2.
Five isolated Sol owner agents were dispatched before any coordinator provider
call. The coordinator does not duplicate owner inference. Each owner uses a
dedicated `codex/gpt6-sol-luna-eval-20260926` branch beneath
`/Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/`, based on current
fetched origin main, and reports exact base, requests, spend and stop evidence.

Credential-custody and portable owner protocols read completely. Central
presence-only status/check passed; no direct OpenAI mapping exists in that
vault. Owners use already-authorized existing process/normal-wrapper credentials
where present; missing direct access stops that owner without a router substitute.
No central key has been injected. Existing owner credentials remain unchanged.
The explicitly invoked evaluate-model selection authorizes this reuse; no new
key creation, copying of whole environment files or account changes are allowed.

The original proposal above remains the frozen scope. Dossier stops after two
correction snapshots and produces independent-review packets; its semantic
acceptance remains pending. No runtime defaults, commits, pushes or rollout.

Verified current-origin base identities:

| Owner directory | Base SHA | Cap USD |
| --- | --- | ---: |
| dossier | `0ba2825b97ea564e72f88c12a0267fee13e9712c` | 2.00 |
| doc-web | `92f341e169f7e81775a7f006ae39757303a8e88f` | 3.00 |
| cine-forge | `163bcb1ecd36de97b76e5ad83298048c9211a4d7` | 1.50 |
| storybook | `7ec2ac667b111bce269e0d56d81305c95518bdec` | 1.50 |
| echo-forge | `031857e0c8b8cee06cf5e28473887d1029461640` | 2.00 |

## Owner results — 2026-09-26

Results are appended as owners finish; the approved proposal above is preserved.

- **Dossier:** Eight total receipts (two native candidates plus two chronological
  harness snapshots each for Sol, Luna and fresh Astra) have exact identity,
  completed/default status and valid usage. Both snapshots compile for all three.
  Root independently decoded receipts and recalculated USD0.1892687, with zero
  unresolved exposure and zero cache writes. This is contract/economic evidence;
  all six blind source-review packets remain pending independent review.
  [Owner artifacts](</Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/dossier/docs/evals/artifacts/gpt6-sol-luna-semantic-20260926/>).
- **Echo Forge:** Both candidates stopped on `control-015`, incorrectly labeling
  a new-content correction in empty playback state as management of existing
  playback. Fresh Gemini makes the same error. All three score14/16 on the same
  prefix, with8/8 control recall,1/6 false activations and1/2 ambiguous abstentions.
  Sol/Luna/Gemini costs are USD0.012886/0.0006443/0.011508; total USD0.0250383
  of2, no unresolved exposure. Luna p50/p95 is955/2604ms versus Sol1133/3834ms
  and Gemini1324/6352ms. All48 calls are native-contract valid. Remaining32cases
  per arm and production Sol/Luna adapter parity are unmeasured. Root reran the
  offline105-file receipt/hash/ledger replay and source-checked the decisive case.
  No adoption; cheaper/faster findings apply only to the exposed16-case prefix.
  [Report](</Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/echo-forge/docs/evals/attempts/control-intent-v1/20260926-openai-gpt6-sol-luna.md>),
  [manifest](</Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/echo-forge/docs/evals/attempts/control-intent-v1/20260926-openai-gpt6-sol-luna.manifest.json>).
- **Doc Web:** All three fresh detector arms pass13/13. Sol mean0.9783077,
  USD0.110163, mean3.404s; Luna mean0.9875538, USD0.00582015, mean3.077s;
  Gemini3Flash mean0.9612385, USD0.0562295, mean6.805s. Luna is the strongest
  value signal on this exposed13-case detector screen, not a broad accuracy or
  promotion claim. Both candidates independently return false-safe `pass` on
  page122001; page22/control stay unmeasured under the stop gate. Root viewed
  source and crop and confirmed the separate neighboring portrait is included.
  Four native probes, four screens and three full13 matrices cost USD0.201644875
  of3, including cache-write rates; no retries or unresolved exposure reported.
  Root checked34 unique candidate raw receipts and13 distinct fresh Gemini
  responses (`gemini-3-flash-preview`), exact frozen case coverage, scores and
  costs. Candidate totals including qualification/screens: Sol0.1379775,
  Luna0.007437875; Gemini0.0562295.
  [Raw manifest](</Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/doc-web/docs/evals/evidence/042-gpt6-sol-luna-crop-manifest.md>).
  [Attempt042 and commands](</Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/doc-web/docs/evals/attempts/042-gpt6-sol-luna-crop-evaluation.md>).
- **CineForge:** Both native direct five-JPEG contracts pass. Sol's owner
  parity case scores deterministic0.4383/rubric0.35/combined0.39415 and stops.
  Root viewed first/last images and confirmed enlargement missed by Sol parity's
  unchanged-scale claim. Tone tags are subjective, and lexical `closer` matching
  is ambiguous; do not treat every scorer deduction as source-proven model error.
  Luna native deterministic0.5983 cannot reach0.80 under the maintained
  equal-weight aggregate even with a perfect rubric; it stops without a second
  subject call. Given scorer ambiguity and absent owner parity/rubric, Luna is
  **defer/inconclusive**, not a demonstrated semantic rejection. Both full6 and
  fresh Gemini are unmeasured. Total USD0.035800575 of1.50 includes USD0.023165
  judge usage estimate; subject charges0.012635575. No unknown request charge.
  Sol's initial Promptfoo CLI grader invocation failed before a provider call;
  corrected invocation used the explicit task judge. No hidden inference retry.
  [Attempt041 and commands](</Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/cine-forge/docs/evals/attempts/041-gpt6-sol-luna-video-understanding-first-case-stop.md>),
  [manifest](</Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/cine-forge/docs/evals/story-222-gpt6-sol-luna-video-evidence.json>).
- **Storybook:** Sol completes12 persona subject turns within operational gates:
  11 graded passes and1 ungraded turn because the frozen GPT-5 rubric judge used
  its entire1024-token limit on reasoning without a grade. This is judge
  transport failure, not a Sol semantic miss. Luna scores3/4 on its admitted
  prefix and stops at warmth-progression turn2. Its answer carries forward the
  restaurant but does not repeat Friday-night wording in turn2. Root found
  explicit Friday context in turns1 and3 plus restaurant continuity in turn2;
  the rubric asks to show remembered context, not literal repetition. Preserve
  the original0.6/fail and progressive stop as a judge/rubric interpretation
  ambiguity, not a source-proven memory failure. No rescoring or paid completion.
  All persona subjects finish <=3.630s and <=USD0.01/turn. Remaining Luna8 and
  fresh Haiku are unmeasured. OpenAI judge shares subject provider; no marginal
  superiority/adoption conclusion rests solely on it.
  PhotoFS001: Sol passes local assertions at4.795s but USD0.0072135 exceeds
  USD0.001. Luna takes2.774s/USD0.000362175 but misses two lexical assertions
  and asserts cake/candle details not clearly grounded in the abstract image.
  This combines a grounding concern and scorer ambiguity. NeitherFS006 nor fresh
  Gemini runs. No retry or judge-budget increase. Total USD0.108652980 of1.50:
  persona subjects Sol0.017525600/Luna0.000474755,16judge requests0.082988750,
  native text probes0.000088200, photos0.007575675. The exhausted judge is
  retained and priced at0.010583750; no unresolved reservation.
  Root independently reconciled20 candidate receipts and16 judge usage records
  to the same total, inspected the ungraded condition and read the Luna
  conversation/rubric. Full raw judge HTTP envelopes are not exposed by Promptfoo;
  complete result bundles retain grading prompt/reason/usage. Judge identity is
  configured, not independently response-echoed. The cost is usage-estimated.
  [Persona Attempt169](</Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/storybook/docs/evals/attempts/169-luna-persona-gpt6-sol-luna.md>),
  [Photo Attempt170](</Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/storybook/docs/evals/attempts/170-story056-gpt6-sol-luna-photo.md>),
  [Manifest](</Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/storybook/docs/evals/artifacts/gpt6-sol-luna-20260926/manifest.json>).

## Campaign accounting and practical decision

| Owner | Usage-priced USD | Unresolved exposure USD | Cap USD |
| --- | ---: | ---: | ---: |
| Dossier | 0.189268700 | 0 | 2.00 |
| Doc Web | 0.201644875 | 0 | 3.00 |
| CineForge | 0.035800575 | 0 | 1.50 |
| Storybook | 0.108652980 | 0 | 1.50 |
| Echo Forge | 0.025038300 | 0 | 2.00 |
| **Total** | **0.560405430** | **0** | **10.00** |

These are usage-priced estimates, including CineForge's explicit0.023165 judge
estimate, not an invoice. Every owner remains within cap. No temporary key was
injected, so no injected-key cleanup was required; owner-managed keys remain
unchanged. All paid work stopped; no automatic retries or use of unused budget.

Luna is a promising cheap detector challenger: on the same exposed13 images it
has the best continuous score and lower measured cost/latency. That does not
clear Doc Web's separate page-context safety/promotion gate. Echo's cheap prefix
and Dossier's compiled outputs similarly do not prove full semantic acceptance.
Keep current defaults. The next Dossier step is independent source review of
the six existing blind packets, requiring no new subject inference. Broader
tests, scorer decisions, judge repair/reruns and rollout remain separate scope.

## Validation and retained work

Owner records retain exact commands, current-origin base identities above,
executed code/config/fixture hashes, raw custody and layered verdicts. Both exact
candidates are now indexed in the central evaluated-model ledger; future metadata
changes do not silently authorize a repeat. All five owner worktrees remain
uncommitted, with primary checkouts untouched.

- Dossier:78 focused semantic runner/accounting/adapter/review tests, Ruff,
  registry parse, methodology check and custody verification passed.
- Doc Web:41 focused tests, Ruff, methodology and whitespace checks passed.
- CineForge:68 focused tests, Ruff, eval-registry checks, methodology compilation
  and whitespace checks passed.
- Echo Forge:4 focused mocked runner tests, raw/ledger replay, corpus/registry,
  ESLint and whitespace checks passed. Executed source retained separately from
  later cache-write accounting hardening; all observed writes were zero.
- Storybook:2 focused adapter tests, Promptfoo config, runtime-prompt byte parity,
  backend typecheck, ESLint, YAML/privacy coverage, methodology and custody/whitespace
  checks passed. Global provider-review status is pre-existing expired; this
  synthetic-only campaign does not refresh or authorize private-data handling.

Conductor evidence-only validation uses lint, whitespace checks, local evidence
link existence and decimal cap/total reconciliation; all passed. No paid replay or unrelated
product-wide test suite was run by the coordinator.

## Dossier independent review follow-through — 2026-09-26

Cam selected the recommended review of six saved packets. Direct Anthropic
`claude-opus-4-6` independently judged each anonymous snapshot in an isolated
request, without subject identity, price or other answers. All six were
acceptable: Sol, Luna and fresh Astra each preserved the tentative name,
withdrawal and corrected opening date. No new subject inference occurred.
Two whole-snapshot identifier aliases required documented offline normalization;
all semantic judgments and raw responses are preserved. No judge retry.

Judge cost USD0.215125; Dossier cumulative USD0.4043937 / 2; portfolio cumulative
USD0.775530430 / 10, with zero unresolved exposure. Eleven owner review tests,
all 12 obligations/33 rows, request hashes, receipts, and three source-bound
reports passed. See the [owner review record](/Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/dossier/docs/evals/artifacts/gpt6-sol-luna-semantic-20260926/independent-review/README.md).

This supersedes the earlier pending-review status only. It supports promising
Luna economics on this exposed correction pair, not broader equivalence or
adoption. Keep current defaults. Recommended next step: prepare a bounded
broader Dossier comparison proposal, prioritizing Luna; obtain selection before
any wider inference. Work remains uncommitted and unpushed.

## Proposed broader Dossier screen — awaiting execution selection

Cam's latest `yes` selected preparation of this proposal, not new inference.
No provider calls or target-repository edits were made while preparing it.

1. **Dossier: Luna versus fresh Astra on the remaining maintained short screen.**
   Re-evaluation expanding semantic coverage after both models independently
   passed the saved correction pair. Exact direct IDs `gpt-6-luna` and
   `gpt-6-astra`, medium reasoning, Responses, Standard/default, foreground,
   `store:false`, canonical strict SemanticGraph contract, 4096 output tokens,
   serial, one repeat, identical authored reference history. Reuse existing
   same-contract access evidence; the first selected case serves as current
   harness qualification. No separate duplicate access calls.

   Case order and snapshot counts:
   - `source-attribution` (2): imported/assistant statements cannot acquire
     account-holder authority; preserve source attribution across turns.
   - `namesakes` (2): keep the two Minas distinct, preserve relationship
     negation and tentative naming.
   - `photo-alternatives` (2): preserve competing identities and later resolve
     the same photographed person without merging alternatives. This is a
     textual semantic case, not a vision test.
   - `plans-negation` (1): rescheduled versus cancelled; conditional plan versus
     completed event.
   - `rescue-report` (1): events and links among animals, organizations,
     locations and artifacts.

   At most 16 subject calls and 16 direct `claude-opus-4-6` independent review
   calls. The judge gets separate anonymous packets, frozen source-first rubric,
   strict Review schema and 8192 output tokens, thinking disabled. Bind the
   whole-snapshot identifier in the outgoing schema before calls to avoid the
   previous identifier-only cleanup. Judge every obligation and emitted row;
   retain raw receipts, failed reviews, costs, request hashes and exact code.
   No retries or alternate reasoning/prompt arms. Existing six correction
   packets remain historical accepted evidence and are not rerun or pooled
   into a claimed fully fresh ten-snapshot comparison.

   Progress one complete case at a time, running both arms and independent
   reviews before opening the next case. Stop on transport/compiler failure,
   invalid/incomplete judge output, unresolved materiality, any material
   semantic failure in either arm, or insufficient remaining reservation.
   Preserve observed minor gaps; they cannot establish clean equivalence or
   justify selection without independent pattern adjudication. Completion
   requires all 8 planned snapshots per arm to be independently acceptable.
   Record latency and subject task cost separately from judge overhead; the
   practical value target is at least 10x lower Luna subject cost with no
   observed semantic regression, not a hard latency/SLO claim from eight samples.

   **Incremental Dossier and campaign maximum: USD4.00**, inclusive of both
   subjects, independent judging and any charged failures; zero retry allowance.
   Maintain a shared ledger across providers. Reserve the next whole case's
   subject calls plus bounded review overhead before dispatch, and stop if it
   cannot fit. Review-packet estimates must include the bounded generated graph,
   not merely the smaller source. A cap stop means incomplete evidence, never
   permission to omit reviews or exceed the budget. Prior portfolio spending
   USD0.775530430 is separate, so cumulative maximum would be USD4.775530430.

   All five families are explicitly synthetic, exposed development/regression
   fixtures. Standard OpenAI/Anthropic API retention is acceptable for these
   inputs; no ZDR or private-data permission is inferred. Existing credentials
   may be used under owner custody; no account changes. Execution stays in the
   dedicated Dossier branch/worktree on base `0ba2825b97ea564e72f88c12a0267fee13e9712c`
   after checking current remote state. The primary checkout is older
   (`0f4edc20522fc5e2e958f7831194287ea2cd90b1`) with unrelated dirty work and must
   remain untouched. Reconcile any upstream change before freezing requests.

   Decision supported: whether Luna merits separately proposed held-out,
   full-length and candidate-history evaluation. This screen cannot choose a
   production replacement. Dossier requires newly authored, independently
   reviewed and frozen unseen families before a model-selection campaign;
   those fixtures and paid tests are outside this proposal.

Not recommended in this increment: Sol (defer while testing Luna's larger
potential savings; not a quality rejection), long narratives and scale stress
(defer until the short semantic gate passes), candidate-generated histories
(defer to a separate accumulation test), new held-out families (required before
selection, but not needed to decide whether to invest in that next stage), and
other repositories (outside the requested Dossier follow-through). No runtime
change, commit, push or rollout is included.

Current official pricing checked during preparation:
[Luna](https://developers.openai.com/api/docs/models/gpt-6-luna) USD0.10/0.50,
[Astra](https://developers.openai.com/api/docs/models/gpt-6-astra) USD10/50,
[Opus4.6](https://platform.claude.com/docs/en/about-claude/pricing) USD5/25
per million ordinary input/output tokens. Exact prior native responses establish
account callability; listed prices alone do not. Existing correction-pair costs
are planning evidence, not a guaranteed cost for the new families.

Reply `yes` to execute item1 under the USD4 incremental ceiling.

## Broader Dossier execution selection — 2026-09-26

Cam selected item1 with `yes`: Luna versus fresh Astra on the five additional
short-screen families, independent Opus4.6 reviews, USD4 incremental shared
ceiling, zero retries, and the declared progressive stop gates. The dedicated
owning-repo worker verified fetched origin/main remains `0ba2825b`; the primary
checkout is untouched. Prior artifacts remain immutable. Results follow below.

## Broader screen result — invalid review stop

The first `source-attribution` case ran both snapshots for Luna and fresh Astra.
All four subject responses completed and canonically compiled. Luna subject
cost was USD0.0025518; Astra USD0.1648300. The first independent Opus4.6 review
completed but used source-unit IDs (for example `actor-1`) in per-row
`evidence_row_ids`, which the maintained contract restricts to emitted graph-row
IDs. Its obligation and combined-effect citations used graph rows, and its
narrative judgments were positive, but that does not make the review valid.
The owner validator rejected it; no semantic acceptance is credited.

The frozen invalid-review gate stopped all further calls. One judge cost
USD0.0455000, giving **USD0.2128818 / 4** incremental spend, zero unresolved
exposure, and no retries. Total Dossier spend across this thread is
USD0.6172755; portfolio cumulative spend is USD0.988412230. These are usage-rated
estimates, not invoices. Three source-attribution reviews and all four later
families remain unmeasured; neither model failed semantically on this evidence.
The next case also exceeded the conservative whole-case admission bound
(USD4.023982 before prior actual spend), independently limiting this proposal.

Root independently inspected the rejected raw review against the packet row
inventory and confirmed the source-ID/graph-row-ID mismatch. See the
[owner follow-through](/Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/dossier/docs/evals/artifacts/gpt6-sol-luna-semantic-20260926/broader-screen/README.md).
The next useful action is a bounded judge-contract repair and independent review
of these four saved answers, constraining citation IDs in the request schema.
No new subject inference is needed. No defaults, commits or pushes changed.

The zero-call review repair is prepared in `broader-screen/review_repair_preflight.py`.
It constrains each judgment ID to its proper inventory, all evidence citations
to the packet's graph-row IDs, and the combined-effect ID to its exact value.
Four rebuilt requests fit the frozen 38,000-byte limit (actual10,413–11,696
bytes) with no source/graph truncation. Root inspected each inventory. Proposed
judge-only continuation: four calls, no retries, cap USD1.60 within the original
USD4 authorization ceiling; actual plus maximum follow-up USD1.8128818. New
selection is needed because the approved plan explicitly stopped on an invalid
review and allowed zero retries. No additional subject inference, later case,
or rollout is proposed.

## Attribution review-only continuation selected — 2026-09-26

Cam approved the four-review schema repair continuation at a USD1.60 ceiling
within the original USD4 follow-through cap. Exact frozen repaired request
hashes are checked before dispatch; no subject call or later-case run is part
of this selection. The failed review and all prior artifacts remain unchanged.

### Attribution continuation result

All four repaired blind Opus4.6 reviews were acceptable, covering10 obligations
and28 rows. Both Luna and fresh Astra now accept the complete attribution pair;
no source IDs leaked into graph-row citations. No subject calls, judgment edits
or additional retries. Added USD0.197765; broader follow-through USD0.4106468/4;
Dossier cumulative USD0.8150405; portfolio cumulative USD1.186177230. All usage
settled. The original invalid response remains charged and preserved.

Root verified all four frozen request hashes, exact standard-tier completed
judge receipts, unchanged raw reviews, both source-bound owner reports and all
58 original custody hashes. Luna's saved pair cost about64.6x less than Astra's,
with somewhat longer observed latency. This and the previous correction pair
are narrow exposed-case evidence; four proposed families remain unrun and
production adoption is not supported. Current [owner report](/Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/dossier/docs/evals/artifacts/gpt6-sol-luna-semantic-20260926/broader-screen/review-resume/README.md).

Next useful work is the four remaining families, after a feasible whole-case
budget is frozen; no additional inference is authorized by this completed
review-only selection. No defaults, commits or pushes changed.

## Remaining four families — execution approved

Cam explicitly raised the broader Dossier ceiling to **USD6 total**, including
USD0.4106468 already spent, and selected execution of namesakes,
photo-alternatives, plans-negation and rescue-report in that order. The new
run's remaining cap is USD5.5893532, including at most12 subject snapshots and
12 repaired blind Opus4.6 reviews. Medium reasoning,4096 subject output and
8192 judge output, source-first obligations and whole-case conservative
reservation remain frozen. No repetition of accepted correction/attribution
cases. The discarded USD4 preflight is preserved as unexecuted; exact execution
boundary is in the owner remaining-screen artifacts. No retries or rollout.

### Remaining-family result — exact-citation stop

Luna's first namesakes response completed with exact served identity and valid
usage but failed the canonical evidence compiler: narrator quote `me` was
nonunique, with occurrence:null. Root replayed the original output offline and
confirmed four exact source substring matches (summer, placement, name, final
me). The maintained contract requires a witness selection for such a quote.
The second snapshot was skipped and the controller stopped before Astra,
judges, or any later case. This is an output citation-contract failure, not
an independently established semantic-quality loss; prior accepted pairs stand.

Added USD0.001094, zero unresolved exposure. Broader follow-through total
USD0.4117408/6; Dossier cumulativeUSD0.8161345; portfolioUSD1.187271230.
No retry, fallback, output cleanup, runtime change, commit or push. Owner
Attempt009, Story170 and [full evidence](/Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/dossier/docs/evals/artifacts/gpt6-sol-luna-semantic-20260926/remaining-screen/README.md)
record the honest unmeasured remaining surfaces. Keep the current default;
Luna has not qualified as a drop-in replacement across the short screen.
Any paid continuation needs a separately selected causal citation-contract
improvement or explicit fresh retry, not automatic repeated attempts.


## Decision-completion continuation — 2026-09-26

Cam explicitly requested identification of the remaining useful evaluations
under the strengthened skill, an active goal, and execution to completion.
This selection supersedes earlier assistant-imposed zero-retry and repeated
selection requirements for recoverable operational issues. It does not erase
real model failures or authorize production changes, private fixtures, or
exceeding the existing owner spending ceilings.

Five owner workers are auditing and completing decision-bearing gaps:

- **Doc Web:** qualify Luna detector value separately from the failed page-safety
  role; inspect adapter parity, held-out coverage, and the combined stronger
  safety path.
- **Storybook:** recover Sol's saved ungraded persona answer, compare a fresh
  incumbent, adjudicate Luna's borderline rubric stop, and complete independent
  useful photo evidence.
- **CineForge:** source-adjudicate the lexical/scorer-bound Luna stop and finish
  a fair comparison if the original stop did not establish model failure.
- **Echo Forge:** distinguish aspirational gates from relative incumbent value;
  complete representative comparison where useful while retaining the shared
  false activation in the score.
- **Dossier:** evaluate useful independent coverage or a compiler-triggered
  stronger-model fallback, using an observable contract failure rather than
  post-hoc case labels to select models.

Starting usage-rated portfolio estimate is USD1.187271230, with no unresolved
exposure. Existing total ceilings remain Doc Web USD3, Storybook USD1.50,
CineForge USD1.50, Echo Forge USD2, and Dossier broader continuation USD6
(including USD0.4117408 already spent in that continuation). Owner records keep
separate actual costs and reservations; ceilings are not pooled. Historical
results and raw artifacts remain immutable. The goal is a ranked, evidence-backed
recommendation for each task, including defensible mixed-model roles.


### Decision-completion findings (owner close-out underway)

The continuation separates task winners from deployment readiness:

- Storybook full blind paired persona review: Sol11/12, Luna11/12,
  Haiku8/12. Original maintained GPT5 grades remain separately recorded
  (Sol11/12, Luna10/12, Haiku9/12). Luna's twelve subject calls cost
  USD0.00114811 versus Sol0.0175256 and Haiku0.035099. Recommend selecting
  Luna for the persona migration; production streaming/provider metering is
  a concrete remaining adoption step, not a missing benchmark result.
- Echo's full48 enriched-context comparison is complete, then the evaluation
  was repaired to match actual production-visible input. Twenty-eight exact
  prior requests were reused;14 eligible cases were rerun through the real
  request builder;6 context-dependent golds were excluded before new outputs.
  On42 eligible cases Sol/Gemini38, Luna37; all recall19/19, false positives
  Sol/Gemini2/20 versus Luna3/20. Retain Gemini default. Luna wins cost and
  latency, but saves only USD0.0246339 over42 calls and adds a false control
  classification that can suppress a desired new-sound suggestion. This does
  not authorize playback; deterministic code still controls actions.
- CineForge's repaired-scoring full6 comparison favors Luna on5/6 cases:
  mean0.5299 versus fresh Gemini0.4188, about5.7x lower subject cost.
  Neither clears the maintained0.80 threshold. Luna is the better next
  quality-improvement candidate; no unreviewed production promotion follows.
- Dossier's remaining cases all reached source-bound independent verdicts:
  Astra rescues the saved namesakes compiler rejection; both models accept
  photo alternatives and plans/negation; rescue reporting is acceptable with
  minor gaps for Luna and acceptable for Astra. The compiler boundary is
  observable, while semantic quality still needs its own gate.
- Doc Web's runtime continuation discovered a coordinate-parser defect in
  Gemini's control, a broken shared layout-model cache, and a grouping-prompt
  conflict with image-count expectations. These are being resolved or
  explicitly adjudicated before translating its13-page detector win into
  a production recommendation.


### Completed owner decisions and evidence

**Storybook — recommend Luna for the main persona-chat migration; retain Gemini
for photo/OCR.** The persona evidence supports a task-specific model change,
not a repository-wide replacement. Luna ties Sol's independent review at a
fraction of its cost; Sol has no economic reason to win this role. The known
continuity miss remains visible, and the maintained12/12 target is not met by
any arm. The next implementation must qualify AI SDK streaming, persistence
ordering and OpenAI metering in the two main chat paths. Welcome and unrelated
calls retain their existing models. No invented held-out prerequisite was added.
See [Attempt171](/Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/storybook/docs/evals/attempts/171-luna-persona-gpt6-continuation.md)
and [Attempt172](/Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/storybook/docs/evals/attempts/172-story056-gpt6-photo-continuation.md).
Full Storybook campaignUSD0.439122385/1.50, zero unresolved exposure. Adapter
and prompt/history parity tests, backend typecheck, lint, config/registry,
privacy-coverage, methodology and frozen-artifact checks passed; the global
privacy-review-expired warning was preexisting, and only synthetic inputs ran.

**Echo Forge — retain Gemini; Luna wins cost/latency but not the default choice.**
The42-case production-input comparison is sufficient to decide this lane:
Luna's extra false classification buys too little absolute savings to justify
additional interrupted sound requests. Sol costs more than Gemini at the same
exactness. Do not invent a router selecting known successful case IDs. The
full48 enriched-context diagnostic and42 eligible production-input comparison
remain separate; all186 calls were native-contract valid. See the
[completed report](/Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/echo-forge/docs/evals/attempts/control-intent-v1/20260926-openai-gpt6-sol-luna.md).
Full Echo campaignUSD0.09187605/2, zero unresolved exposure. All three raw
replays, six focused tests, lint, corpus/registry/methodology and diff checks
passed. No further paid comparison is justified for the unchanged configuration.


**CineForge — select Luna as the next ordered-frame research/reference model,
not an unreviewed production replacement.** Complete six-case comparison gives
Luna0.5299 versus Gemini0.4188, with5/6 case wins,5.7x lower subject cost and
slower mean latency (3675ms versus2470ms). A confirmed rooftop golden defect
incorrectly demanded increasing size although source frames preserve the
runner's dimensions. Excluding that case offline still favors Luna0.52432
versus0.42334 on4/5 cases. Both remain below the maintained0.80 gate throughout;
Luna's explicit prop-continuity misclassification is real. Sol's first-case
source-backed miss remains a do-not-advance result. Thus Luna has a useful
relative win, while source/rubric repair and quality improvement remain necessary
for promotion. [Attempt042](/Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/cine-forge/docs/evals/attempts/042-gpt6-luna-repaired-six-case-comparison.md)
preserves original and repaired scores, sensitivity analysis and source review.
Full CineForge campaignUSD0.390639095/1.50 including usage-rated judge estimates.
One earlier Luna first-parity raw envelope was overwritten by the later full-six
first call; its tracked result retains output/identity/usage/hash, but the full
original envelope is unavailable. All six comparative Luna raw envelopes were
preserved separately, so the main paired result remains auditable. This custody
limitation is disclosed rather than calling every historical raw file intact.

CineForge close-out passed47 focused tests, Ruff, eval-contract/methodology and
whitespace checks,68 evidence hashes and exact full-six receipts. No runtime
default changed. Per-arm cumulative accounting: SolUSD0.0352519,
LunaUSD0.178253895, GeminiUSD0.1771333, including their reviews and prior probes.


**Dossier — advance a Luna-first extraction pilot with Astra on canonical compiler
rejection; retain Astra for workflows needing stronger fidelity.** The complete
six-family screen preserves Luna's accepted cheaper outputs and its genuine
namesakes citation failure. Compiler rejection is an observable fallback trigger;
it cannot catch the minor missing rescue-location assertion in a graph that
compiled successfully. [Attempt010](/Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/dossier/docs/evals/artifacts/gpt6-sol-luna-semantic-20260926/mixed-fallback/README.md)
records every case and the repaired conservative duplicate-ledger overcount.

The follow-up [Attempt011](/Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/dossier/docs/evals/artifacts/gpt6-sol-luna-semantic-20260926/history-seam/README.md)
then tested the actual candidate-history seam: saved failed Luna first output
rejected by the compiler, accepted Astra first graph supplied to fresh Luna and
Astra second requests, both independently acceptable. No first output was
retried. The measured sequence Luna-rejection→Astra-recovery→Luna cost
USD0.0838253 versus Astra-onlyUSD0.1884800 (55.5% less), but took52.52s versus
32.67s. Those latency and cost numbers include the failed Luna call. This is a
qualified synthetic handoff, not a deployed router or general semantic-quality
guarantee. Production integration and representative full-path validation belong
to adoption work; no unchanged repeat of these exposed cases is warranted.

Dossier cumulative campaignUSD2.3386408, of which broader continuationUSD1.9342471
is inside its hardUSD6 ceiling. All usage settled. Full-source review, exact-wire
replay, focused review tests, Ruff, YAML, custody and diff checks passed. The
historical inflated intermediate accounting and false conservative budget stop
remain explicitly superseded by reconciled distinct-ledger totals. Current
results do not silently relax semantic gates or change defaults.


**Doc Web — retain Gemini in production; preserve Luna's detector benchmark win.**
Luna remains the13-page measured detector leader at0.987554 versus Sol0.978308
and fresh Gemini0.961238, and its detector calls were about9.7x cheaper than
Gemini. Production-equivalent four-page calls revealed different constraints:
Gemini coordinate parsing needed source-backed repair; an isolated official
layout-model cache restored the missing trim component; caption output bounds
were raised symmetrically and truncated responses rejected with raw retained.
The recovered final Luna/Gemini split produced7 crops versus Gemini's9.

Count alone is not the defect: the runtime prompt explicitly allows adjacent
seal/signature grouping despite metadata listing4 separate regions. The decisive
failure is Luna's raw page12 composite rectangle [.12,.686,.718,.843], which
already excludes part of the seal and signatures before any layout or caption
trim. Root independently inspected the raw output, source page and final crop.
A remaining truncated Gemini caption-assist call at2048 tokens cannot fix that
upstream geometry; it is recorded as a separate limitation, not the reason for
stopping. Gemini's final control receipts completed, but its signature crops
still contain printed labels. No count-only fallback can claim clean end-to-end
acceptance from these artifacts. Retain the default and existing GPT5.5
page-context regression model; do not relabel it a production safety stage.
No further unchanged paid attempt is justified by the source-confirmed raw-box
failure. [Owner Attempt043](/Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/doc-web/docs/evals/attempts/043-gpt6-luna-detector-runtime-qualification.md)
and its raw receipt inventory preserve all diagnostics.
Doc Web cumulativeUSD0.382724960/3, includingUSD0.181080085 for this runtime
followthrough, with42 retained native runtime receipts.

### Final accounting and completion

| Owner | Entire campaign estimate USD | Relevant ceiling |
| --- | ---: | --- |
| Dossier | 2.338640800 | Initial phase2; broader phase6 (broader actual1.9342471) |
| Doc Web | 0.382724960 | 3 |
| Storybook | 0.439122385 | 1.50 |
| CineForge | 0.390639095 | 1.50 |
| Echo Forge | 0.091876050 | 2 |
| **Total** | **3.643003290** | Owner ceilings remain separate, not pooled |

Current-turn incrementUSD2.455732060 over the priorUSD1.187271230. These are
usage-priced estimates, not invoices. Failed and recovered calls remain charged;
no unknown billing exposure remains. The justified evaluation gaps have reached
a decision: recovered judge/scorer/runtime-input/budget-accounting defects,
completed comparative matrices, and tested observable fallback history.
Remaining work is concrete adoption integration or source-backed product/eval
quality improvement, not another unchanged tournament. Board Game Ingester
remains deferred for an eligible public/synthetic corpus; Robo Rally has no
model-owned lane warranting this campaign.

Recommended next implementation is an isolated Storybook main-persona OpenAI
streaming/metering adapter using Luna, preserving unrelated model choices and
recording the known continuity miss against the current12/12 target. No default
migration or relaxation of that owner target is implied by this evaluation.


Final validation: Doc Web passed95 focused tests, Ruff, registry YAML,
methodology and diff checks;42 runtime raw hashes verified. Conductor lint,
skill compatibility links, methodology currency and whitespace checks passed.
All five owner close-outs are complete. The active decision-completion goal is
achieved; adoption implementation remains separately selectable.

### Selected follow-up: Storybook persona integration

Cam selected the recommended Luna persona integration after the campaign closed.
Implementation and qualification are complete in the existing isolated
Storybook worktree under
[Story 169](/Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/storybook/docs/stories/story-169-gpt6-luna-persona-chat-migration.md).
The selected scope is main text persona chat, preserving other model roles;
landing and deployment remain separate actions. The historical evaluation totals
above remain unchanged. Qualification spend is recorded separately below.

The runtime adapter uses exact `gpt-6-luna`, Responses streaming, no reasoning,
`store=false`, default service tier and no automatic POST retry. User turns are
saved before dispatch. A request-scoped native terminal receipt supplies cache
pricing and known/unknown accounting; complete assistant turns are saved only
after terminal acceptance. HTTP completion is explicitly gated because the
installed SDK swallows errors from its `onFinish` callback. Dependent Knowledge
work starts after persona settlement to avoid a same-request pending-charge
collision. Welcome, summaries, titles, photo/OCR and other routes retain their
existing model choices.

One synthetic main-chat tRPC proof saved both turns and a known Luna receipt
(2,375 input, 31 output tokens, USD0.000313). Retrieval and embedding added
USD0.000006 each: **implementation qualification USD0.000325**, all three calls
known, no pending/unknown exposure. Native cache categories are tested in the
adapter fixtures but are not separately retained in the live `ai_calls` schema.
Storybook evaluation plus this qualification is USD0.439447385 of its USD1.50
ceiling; all-owner evaluation plus qualification is USD3.643328290. No private
conversation was used for the proof.

Validation: 49/49 focused chat and adapter tests, backend typecheck, changed-file
ESLint, production build, provider-privacy coverage, methodology compile/check
and whitespace checks passed. The global privacy review date is already expired
and remains disclosed; coverage success does not refresh that date. The known
11/12 persona continuity result remains a quality limitation, not a rewritten
golden or a perfect-score claim. Recommend landing this scoped integration;
no commit, push or deployment has occurred.

### Selected follow-up: CineForge ordered-frame qualification

Cam selected source-backed benchmark repair and qualification of the actual
ordered-frame integration on 2026-09-26. Execution remains in the isolated
CineForge campaign worktree, under its original USD1.50 ceiling (prior spend
USD0.390639095; remaining USD1.109360905). Other model roles remain unchanged.

Runtime inspection corrected an important premise: this lane is a maintained
headless Promptfoo benchmark, not a production inference call. `VideoAnalysis`
objects are registered schemas; no product module, recipe, service or API invokes
the ordered-frame analyzer. Story 030 explicitly chose this benchmark substrate
instead of adding a second runtime. Gemini 3.5 Flash-Lite's production ScriptBible
role is a different task and was not qualified by these frame results. The
selected work therefore repairs source truth, re-evaluates saved comparative
outputs where valid and qualifies the existing headless path. It does not
invent a new product QA subsystem or silently swap the ScriptBible model.

The source-backed v4 truth overlay preserves the original targets, model outputs,
prompts and all submitted JPEG bytes. It corrects rooftop's false size-growth
and acceleration expectations, allows bedside's ambiguous object interpretations,
and excludes the ambiguous camera mechanism for dialogue while still requiring
visible figure growth. Negation-safe equivalent-wording checks prevent the
summary scorer from penalizing valid descriptions or crediting negated claims.

The derived comparison uses the same twelve saved subject responses, new
structural scoring on all six cases, and six new pinned Opus 4.6 judgments for
the three corrected references across both models. The other three paired
rubric scores retain their unchanged reference judgments. Luna leads **6/6**:
**0.5986 versus Gemini 0.4313**, compared with historical v3's 0.5299/0.4188.
This is a corrected-reference regrade, not fresh model performance or another
subject trial. Original subject means remain 3.675s/USD0.000481 for Luna and
2.470s/USD0.002731 for Gemini.

**Recommendation: use Luna as the preferred model for CineForge's current
headless ordered-frame analysis/reference runs.** Both models remain below the
maintained 0.80 adoption threshold. The revised score is not fully
objective: the judge still penalizes some permitted bedside interpretations and
subjective tone choices, and calls a visible ground line potentially invented.
Root source review nevertheless corroborates Luna's advantage: it reports the
actual figure enlargement and fixed backgrounds where Gemini misses enlargement
or invents camera tracking. Both still label the red-to-blue prop change
`intact`, so neither should own automatic continuity approval. No ScriptBible or
other production-model replacement follows from this result.

Six new judge receipts returned exact `claude-opus-4-6`, terminal `end_turn`,
unique IDs and complete usage with zero cache-read/write tokens. Root verified
the original subject-result hashes and the USD0.140990 incremental judge cost.
CineForge cumulative spend is **USD0.531629095/1.50**; no new subject calls or
unsettled charges. With the separately qualified Storybook integration,
all-owner evaluation and qualification spend is now **USD3.784318290**.

[Owner Attempt043](/Users/cam/.codex/worktrees/gpt6-sol-luna-eval-20260926/cine-forge/docs/evals/attempts/043-video-understanding-source-truth-v4-headless-qualification.md)
contains the source review, exact reproduction commands, paired derived scores,
judgment limitations and hash-pinned receipts. Root verified all 23 call-time
frozen files still match, in addition to the six receipts and saved-output
hashes. Do not repeat the same subjects merely to chase the absolute gate.

Owner validation passed 72/72 focused tests, the 13-file target-overlay check,
immutable eval-contract v14 checks, methodology compilation and whitespace
checks. The offline regrade reproduced the same derived-result hash. No
production default, private-input processing, commit, push or deployment was
performed. Conductor lint and whitespace checks also passed.

Final closeout also preserves byte-exact call-time script snapshots and a
separate post-run provenance manifest for mechanical lint cleanup. The original
freeze and evidence manifests remain unchanged. Current active scripts pass
Ruff without suppressions; the final focused suite is **73/73**, current eval
contract **v15** passes, and the cleaned scripts reproduce the identical derived
result. This supersedes the earlier 72-test/v14 validation count without any
new provider call or spend.


## Authorized closeout and future work — 2026-09-26

Cam approved the remaining owner check-ins, Storybook deployment, a Dossier
Luna-first/Astra-fallback pilot, and an analysis of evaluation time/quota.
The active goal covers these outcomes together; future work is kept distinct
from the completed comparative evaluation.

| Owner | Verified remote-main landing | Scope |
| --- | --- | --- |
| Storybook integration | `8637fdedcbdc40501d18990ccdd858c9942d0bf1` | Evaluation plus main-persona integration, Story169. |
| Storybook release checks | `ef0c86ac3c9d85218f1665536982c98257b13468` | Five test/config/script fixes; source for deployed release v29. |
| Storybook deployment/accounting | `9340cdcacc62ad8bd8f216c416ea3ba990685a4c` | Includes release record41cdd9e, accounting exception and existing bounded-smoke runbook correction. |
| CineForge | `f69909d8df04805fe47615a88d40bf84c839f052` | Source-truth v4 and headless qualification; no product default switch. |
| Echo Forge | `d668707e25f6cfb2442f384e9f1f6d70c115133b` | Evaluation evidence and reproducible tooling; retain Gemini default/Grok option. |
| Dossier evaluation | `ab4f15f2accaf2c36e55c29cdd23cfc1ee927015` | Frozen evaluation and history-seam evidence. |
| Dossier pilot | `543fecd0c7b9de144390a827cceb9bd742a7db0a` | Opt-in library coordinator, exact saved-response replay, Story173, accounting deviation preserved. |
| Doc Web | `ed70d32205004bb6117780529684f68396c8a750` | Stories235/236, Attempts042/043, opt-in tooling fixes and runtime evidence; Gemini default retained. |

Owner worktrees and frozen evidence are retained. Unrelated dirty primary
checkouts are untouched. Applicable implementation evidence is reused through
landing; documentation/commit bookkeeping alone does not trigger paid reruns
or repeated product suites.

See the [efficiency review](scout-076-evaluation-efficiency-review.md) for
measured orchestration usage, limits and concrete recommendations.

### Dossier opt-in library pilot

Story173 implements `dossier.extract_semantic_pilot(request, dispatch=...)`:
foreground Luna first, one Astra fallback only on canonical
`PassageReferenceError`, then the accepted graph as next-snapshot history.
The host callback owns durable WAL, authorization, every dispatched charge and
unknown-delivery reconciliation. No host adapter or production Engine default
is changed. Provider errors, malformed envelopes and unsettled usage stop
without fallback; compiling semantic omissions remain outside this trigger.

The exact saved namesakes sequence now runs through the new code: rejected
Luna, accepted Astra, then Luna using Astra history. All three generated request
byte strings and resulting graph hashes match the previously charged records.
This qualifies the library routing by replay, not a fresh live or unseen-source
pilot. Its intended replay adds no provider spend. Final 37 focused tests, Ruff,
methodology and diff checks passed; prior 2,588 unit tests passed before the final
pilot-only request-parity change. The separate accidental live-test exposure
below is not hidden in this replay claim. Canonical source review remains necessary
before broader unattended adoption. The runbook is
`dossier/docs/runbooks/semantic-luna-pilot.md` in the owner worktree.

### Accounting exception: unintended live Dossier validation

After passing offline unit checks and an explicit coordinator instruction to
run only final focused checks, the owner mistakenly ran unfiltered `pytest -q`.
It entered two Anthropic integration module fixtures using the public synthetic
passage: Haiku4.5 Engine extraction and Sonnet4 extraction. Engine produced a
new cache artifact; the seven Sonnet setup errors reused one failed fixture.
The command was interrupted. No private fixture was identified.

Exact dispatched calls and usage were not retained, and the complete exception
tail was lost to tool-output truncation. Zero charge cannot be claimed. With
three Instructor attempts and up to two SDK retries, each fixture admits at
most9 HTTP attempts. A deliberately loose reservation uses the200k standard
context ceiling and21,333 output tokens per request: Sonnet4USD8.279955 plus
Haiku4.5USD2.759985 = **USD11.039940 unresolved exposure**. This is not a billed
amount or a likely-cost estimate. It exceeds theUSD4.0657529 remaining broader
Dossier allowance, so the final campaign cannot be represented as proven within
all caps. No additional inference is authorized to investigate this deviation.

Settled planned evaluation/qualification remainsUSD3.784318290; adding this
reservation yields **USD14.824258290 before the separately unquantified
Storybook smoke**. This is not a total upper bound. Provider
billing reconciliation is still required for the accidental calls. The pilot's
intended qualification used saved-response replay and required no new calls.

### Storybook deployment

Production release v29 (`e03j7MNppPA38TQyMMZVl8DAg`) runs source
`ef0c86ac3c9d85218f1665536982c98257b13468`, image
`sha256:99286ebab4bd2b6de2c139ca19beeb14a448e0584c506ff82fe5407e312576db`.
App-only blue-green rollout took 81 seconds; the new app machine is
`2872d0ea549628`. API health reports connected DB and ready dependencies;
root/login/bundle return 200 and Playwright login rendering has no console errors.
The active v26 worker remains running, standby v26 remains stopped, and their
configs exactly match predeployment. Existing feature/privacy holds remain.

The stored production smoke token returned 401, so authenticated Tier 3 and a
production Luna persona message were not tested. The prior isolated synthetic
live Luna conversation remains the functional proof. No production chat
inference was made. The required public synthetic Dossier deployment smoke
passed; its artifact lacked exact provider cost. The direct package command
bypassed the existingUSD1 guarded launcher. Instructor retries and response-driven
identity/repair fanout prevent reconstructing a trustworthy call-count bound.
Exact spend and compliance with the sameUSD1.060552615 remaining Storybook
allowance are uncertified; no higher allowance was approved. A prior matched
fixture run costUSD0.010297, but that is historical reference, not this run's
charge. The owner runbook now directs cost-controlled smokes through the
existing bounded launcher. No inference was repeated for this audit. The expired global privacy-review date remains documented,
not silently refreshed by this deployment.


### Final closeout verification

All five owner records are on remote main; the opt-in Dossier pilot and
Storybook deployment are complete within the scope described above. Remaining
billing uncertainty is an execution/accounting exception, not an unevaluated
model-quality lane. Read-only checks found the Claude console requires sign-in
in both available browser sessions; there is no available usage connector.
No credentials or account settings were changed. Exact billing cannot be
reconstructed from the retained artifacts, and no zero-charge claim is made.

Conductor validation: reviewed task-specific skill changes and owner receipts,
39 local evidence links checked, compatibility skill links and methodology graph
current, scoped staged diff check. Existing owner runtime test evidence is
retained rather than replaying paid evaluations. Dirty primary checkouts remain
untouched; task worktrees and raw artifacts are retained.


### User-approved campaign closure — 2026-09-27

Cam approved closing the campaign with the two billing uncertainties documented.
Exact charge reconciliation is no longer a completion requirement. This does
not establish the actual charges, certify historical cap compliance, or authorize
additional spending. Evaluation, implementation, deployment and the efficiency
review are complete within the recorded scope. No additional provider calls,
billing investigation or sign-in are required for this campaign. Remaining
workflow optimization recommendations are separate future work.
