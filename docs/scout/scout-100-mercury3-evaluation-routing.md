# Scout 100 — Mercury 3 evaluation routing

2026-10-20 recommendation, America/Edmonton. **Stage 2 complete 2026-10-21; retain defaults.**

## Original Stage 1 recommendation — historical

Recommend four bounded owner campaigns, **US$11.50 maximum**. No credentials,
authenticated discovery, inference, target modifications, defaults, commits or
pushes. Two economical read-only portfolio workers assisted; coordinator
corrected stale-context recommendations against current owner evidence.
Existing shared-checkout dirt is preserved.

## Current identity, contract and privacy

- [Creator announcement](https://www.inceptionlabs.ai/blog/introducing-mercury-3)
  dates the distinct Mercury 3 release October19. Native `mercury-3` at
  `https://api.inceptionlabs.ai/v1/chat/completions`;
  router `inception/mercury-3`. Announced and API-listed; **access: unverified**.
  No exact Mercury3 attempt in `docs/model-watch/evaluated-models.md`.
  September's Mercury2.5 Preview attempt is a distinct checkpoint, not coverage
  of this candidate. Today's discovery-only watch is not an evaluation.
- [Models](https://docs.inceptionlabs.ai/get-started/models): text input/output,
  1M context, 131072 maximum completion; tools and structured outputs documented.
  No image/audio/video input or generation. Voice application examples describe
  integration, not native audio modality.
- Public unauthenticated GET of
  [router endpoints](https://openrouter.ai/api/v1/models/inception/mercury-3/endpoints)
  returned one Inception endpoint named `Inception | inception/mercury-3-20261019`,
  1M context, 131072 output, precision unknown, strict/schema and forced-tool
  parameters advertised. This is route metadata, not enforcement, inference or
  immutable served-weight attestation. Prefer this existing router access path,
  pin Inception for reproducible pricing/privacy and record exact requested and
  returned identities. No different-model fallback. Do not silently substitute
  native or another checkpoint if qualification fails.
- [Reasoning](https://docs.inceptionlabs.ai/capabilities/reasoning-efforts):
  native instant/low/medium/high; Mercury3 defaults low. The generic API field
  table says medium, so explicitly set effort rather than rely on that conflict.
  Qualify router effort passthrough before scoring; never equate router `none`
  with native `instant` without evidence. This proposal uses low/medium/high only.
- [Chat contract](https://docs.inceptionlabs.ai/api-reference/chat/create-a-chat-completion):
  `max_completion_tokens` includes visible and reasoning tokens; deprecated
  `max_tokens` is superseded by it. Native default allowances vary with effort:
  instant8192, low24576, medium65536, high131072. Set explicit adequate bounds
  below; truncation is an operational failure requiring bounded repair, not a
  semantic miss. Count billed reasoning output; verify actual usage accounting.
  Temperature0.5–1.0, default1; out-of-range values reset with warning. Use1
  explicitly; do not assume temperature0 parity with an owner control.
- [Structured outputs](https://docs.inceptionlabs.ai/capabilities/structured-outputs)
  document JSON Schema; qualify each owner's actual runtime contract first.
  Metadata is not drop-in proof. One bounded safe diagnostic relaxation can
  isolate a failed schema route; save the complete raw response before parsing.
  Such results are capability-only, not production parity.
- Launch USD0.10/M input,0.35/M output,0.01/M cache; regular0.20/0.70/0.02.
  Discount expiry unknown. Reserve at regular rates with no caching assumption;
  recheck exact endpoint before spending. Vendor speed/quality claims motivate
  tests but do not establish owner superiority or end-to-end savings.
- [Privacy policy](https://www.inceptionlabs.ai/privacy-policy) permits service
  improvement including training/refinement and retains personal data as needed.
  No selected-route ZDR/no-training guarantee is established. Retention/training
  may occur. Selection covers only the identified authored-synthetic fixtures;
  no private genealogy, family photos, household records, speech, restricted
  game material or unclear payloads. Stricter owner policy controls. No account
  settings change is authorized or required by this proposal.

## Stable execution handles — Evaluate now

1. **Echo Forge — US$2.50 inclusive.** First `control-intent-v1`:42 maintained
   authored-synthetic current-input cases, fresh native Gemini3.8 Flash low2048,
   actual runtime input/request builder. Preserve exclusion of008/009/019/024/027/045
   whose answers require unsent context. Qualify001/016/006 before expansion.
   Require no worse exact accuracy, control recall, false controls and ambiguity
   abstention; hard15s, seek30% p95 or task-cost reduction at quality parity.
   Start **low/32768**: short interactive classification with negation/ambiguity
   warrants some reasoning; instant is deferred until quality is established.
   Independently `scene-to-soundscape-golden`: Tavern then Dungeon, fresh
   GPT5.4 Mini4000; candidate **low/32768**, require2/2 full role/music/negative
   constraints, <=USD.01/subject; report soft5s target. Prior Mercury2.5 Preview
   was fast but missed seven Tavern requirements; this distinct checkpoint can
   settle whether those semantic deficits persist. Current Mini also misses a
   scene golden, so it is not an automatic winner. No paid judge, generated
   audio, playback, full licensed proposal assembly or private speech.

2. **Storybook — US$1.50 inclusive.** `luna-persona`: no-advice discriminator,
   then12 authored-synthetic turns in seven actual reset/history groups
   (1/1/1/1/3/3/2), fresh GPT6 Luna none512; fixed blind GPT5-2025-08-07 review.
   Use the actual Test User production prompt and own-arm conversation history.
   Require every source/continuity/inference-firewall/no-therapy assertion,
   <=5s and <=USD.01/turn; seek30% stage-cost or latency improvement at parity.
   Start **low/32768** for responsive persona turns with subtle inference rules.
   Recent MiniMax tied narrow rubrics but violated a forbidden source phrase;
   source review must catch this before advancing. Candidate could improve
   latency or cost without changing Luna's behavior contract. Private personas,
   photos and books excluded. A small pass prioritizes independent qualification,
   not family-data adoption.

3. **Dossier — US$6 inclusive.** `standalone-semantic-value`, authored-synthetic
   Story184v4 `long-history-two-families/follow-1`, full frozen321KB continuation
   against fresh GPT6.1 Sol medium16384. Two independent blind native Opus4.6
   full-obligation/full-row reviews. Require compilable graph, all five meanings,
   exact supported attribution, documentary basis, provenance/correction lifecycle,
   uncertainty and zero material errors; retain minor defects. Start
   **high/32768**, reserving bounded truncation recovery to65536: long-history
   meaning preservation tests capability before minimal compute. Recent Sol
   control costUSD.177918 and45.865s; a cheap fast candidate has measurable
   stage-value headroom. At quality parity seek30% task-cost or inference-latency
   improvement. n=1 exposed development case can prioritize independent
   qualification, never broad adoption. No private genealogy, vision extraction,
   history expansion or broad generic extraction tournament.

4. **Doc Web — US$1.50 inclusive.** `onward-document-consistency-planning`,
   full production generative planner on Story234's frozen anonymous six-HTML
   cohort: retained48-row DOM structure, regenerated fictional text and injected
   mutations. Use current exact planner prompt/schema/dossier/normalization,
   fresh GPT-4.1-2025-04-14 control, including generated conventions, findings,
   issue typing, source evidence and uncertainty, not only a five-label projection.
   Start **medium/65536**: policy creation and cross-chapter reasoning are harder
   than a status classifier but have greater latency headroom than interactive
   turns. Full raw and normalized source review; require all six expected
   dispositions, full manual-format coverage, no source-incomplete case cleared,
   correct row-semantic separation and no self-contradictory accepted convention.
   Preserve all current source/layout/uncertainty guards. Stop on a material
   source/contract failure; source review before any recovery/expansion. No paid
   judge; deterministic checks plus blind coordinator source adjudication.
   Historical full planner costUSD.029740/29.176s for this cohort; shadow added
   cost rather than saving it. Seek30% planner-stage latency or cost reduction
   at no-worse quality; contradictory policy has independent quality value.
   One aggregate document/cohort is a development screen, not six independent
   document trials or held-out promotion proof. No narrow classifier-only rerun,
   original Onward text/images, OCR, repair calls or private genealogy.

**Campaign maximum US$11.50.** Ceilings include subject/control/judge/probe and
bounded operational repair; they become hard on selection and cannot transfer
between owners. No paid work has run. Stage shares in the whole product workflows
are unmeasured; report stage savings without claiming equal workflow gains.

## Effort, fairness and progressive execution

One candidate effort per task; no semantic effort sweep or automatic rescue arm.
High is unnecessary for bounded intent/scene/persona until evidence shows a
specific benefit; instant could compromise their nuance and is not the first
quality screen. Dossier low/medium and DocWeb low/high remain unmeasured: first
establish one plausible quality/economics frontier before optimizing effort.
Do not call any untested effort a failure. A later useful configuration needs
a separately bounded selection; remaining dollars alone are not authorization.

After selection: read owner/custody protocols completely; dispatch one isolated
current-remote-base worktree worker per selected owner before coordinator calls.
Reconcile maintained prompts/fixtures with current base rather than silently
copying unrelated unlanded work. Freeze request topology, source bytes, golds,
schema, explicit subjects/judges/rates and reservations in a zero-cost rendered
preflight. Make fresh matched calls for relative claims. Do not alter criteria
after outputs or repeat semantic failures until favorable. Stop only the affected
task; finish independent selected tasks. Recover demonstrated adapter/judge faults
within cap, rejudge saved outputs, preserve failures and layered verdicts. No
runtime changes, rollout, commits, pushes, merge or deployment.

## Reservation feasibility

Candidate bounds use regular USD0.20/0.70 per million, no cache. Input bounds
are token reservations, not KB-to-token conversions. Final exact packets and
all provider/judge rates must be admitted before POST; never shrink source data
to fit. Unknown charges retain full reservations.

| Owner | Inclusive reservation topology (USD) |
| --- | --- |
| Echo2.50 |45 intent candidate8192/32768=1.10592;45Gemini controls.684288;2scene candidate16K/32768=.0522752;2Mini controls.097728;total1.9402112, remainder.5597888 for repair. Qualification included in45. |
| Story1.50 |12candidate26K/32768=.3376512;native controls.15;3GPT whole-panel reviews incl repair.62076;total1.1084112, remainder.3915888. No photo subject reservations. |
| Dossier6 |2full candidate330K/65536=.2237504;2probe8K/65536=.0949504;Sol allowance.70;3Opus full reviews incl repair4.7076;total5.7263008, remainder.2736992. Two ordinary reviews plus one review repair; second subject reserved for operational recovery, not semantic retry. |
| Doc1.50 |3candidate full-cohort<=100Kinput/65536output=.1976256;3GPT full-cohort controls<=100K/16384 at conservative2/8 per M=.993216;total1.1908416, remainder.3091584. One primary paired cohort; two additional slots only bounded qualification/operational recovery, no favorable repeats. No paid judge. |

## Not recommended now

Each other registered repository has exactly one disposition:

| Repository | Disposition and concrete reason |
| --- | --- |
| CineForge | **Defer.** Exact-runtime synthetic ScriptBible matches text, but Attempts035/038 and current Scout099 preserve unresolved source-faithful theme-evidence scorer ambiguity. Resolve this comparison contract before another subject screen. Other text entity tasks retain separate contamination/runtime-alignment holds. Ordered-frame understanding and image generation require unsupported modalities. Price alone is not the deferral reason. |
| Board Game Ingester | **Defer.** Current eligible orientation and dense physical-outline tasks require images. Text source-role/rules/inventory lanes use licensed/private source packages; no current maintained eligible synthetic textual lane identified. Wait for a real public/synthetic text decision, not fabricated substitute geometry evidence. |
| Robo Rally | **Do not evaluate.** Registry owns deterministic game/scenario/replay proof, with no implemented candidate-facing LLM comparator. Canonical private rules PDF excluded. |
| Ultima IV Web | **Do not evaluate.** Current earned fresh-to-victory and original/recovered-engine proof is not an interchangeable text-model benchmark; prospective model tasks lack an implemented comparable lane. |
| Financial Hub | **Do not evaluate.** Private source-bound household analyst workflow has no maintained eligible inference-comparison corpus. Synthetic security tests do not establish model quality. |
| Financial Monthly Analysis | **Defer.** Plausible AI reconciliation/proposal work uses private household records; no maintained eligible synthetic comparator and selected-provider payload policy established. |
| VLC Thumbs | **Defer.** Registered `/Users/cam/Documents/Projects/ultima-iv-web/vlc-thumbs` is absent; cannot inspect current owner/caller. Historical native-product status is not current model-task evidence. |

Additional matching-task omissions: Storybook relationship-mode replay did not
reach the classifier on the selected real consumer inputs (Scout098); another
component score cannot fix that. Interpreter product correctness needs its own
source-evidence contract. Photo/scrapbook tasks need vision. Dossier generic
extraction is lower priority than the maintained current long-history decision,
whose measured cost gives this bounded screen a practical target. DocWeb narrow
classification adds cost at the existing sidecar boundary; full planner is the
decision-bearing alternative selected here. Literal tables, crop detection,
deletion safety, handwriting and OCR need images; deterministic born-digital
conversion offers no model replacement. Echo audio retrieval/generation and
licensed full proposal assembly are outside these eligible text contracts.
Conductor coordinates these comparisons rather than duplicating owner harnesses.

## Current evidence pointers and validation

- [Today discovery](../model-watch/daily/2026-10-20.md), evaluated ledger;
  [Mercury2.5 owner result](scout-066-mercury-25-preview-evaluation-routing.md).
- [Latest portfolio/owner follow-through](scout-099-minimax-m31-flash-ga-evaluation-routing.md),
  including Dossier Attempt035, Echo current-input/scene record and Storybook
  Attempt192 in their linked October20 isolated worktrees; files verified present.
- DocWeb current registry `onward-document-consistency-planning` and
  `jev-document-consistency-classification`; primary owner
  `docs/evals/artifacts/story234-evidence-contract-recheck/report.md` gives
  fictional-text eligibility, full-cohort contract, cost and actual topology.
  [Prior consumer trace](scout-091-five-decision-models-evaluation-routing.md)
  demonstrates why classifier-only savings do not save the full planner cost.
- Current CineForge registry `script-bible` explicitly preserves proxy mismatch
  and scorer ambiguity; other registered owners inspected read-only through
  root instructions, Ideal/spec and registry/maintained surfaces as available.
- Documentation-only check: new report whitespace and reservation arithmetic;
  no changed runtime inputs warrant tests. No evaluated-ledger update: Stage1
  has not reached an authenticated probe, provider call or owner access stop.

Reply `yes` to run all numbered evaluations, or `only do 1, 3` for a subset.

## Selected execution — 2026-10-21

Cam replied `Yes`, selecting all four positive items without scope changes:
Echo2.50, Storybook1.50, Dossier6, DocWeb1.50; aggregate hardUSD11.50.
The original recommendation above remains historical. All four owner workers
were dispatched before any coordinator provider call; coordinator makes none.
Each owner uses its own current fetched remote-main base and isolated worktree:

| Owner | Worktree | Exact starting base |
| --- | --- | --- |
| Echo Forge | `/Users/cam/.codex/worktrees/scout100-echo-20261021` | `bb91a27bf410375e5bc03b2c7dd30a770a14b217` |
| Storybook | `/Users/cam/.codex/worktrees/scout100-storybook-20261021` | `ae3c0625132545c25ebd2ba4303c106b93990fb7` |
| Dossier | `/Users/cam/.codex/worktrees/scout100-dossier-20261021` | `62ba22ba6bdd3e7a81be20cc7e76ec2672faf442` |
| Doc Web | `/Users/cam/.codex/worktrees/scout100-docweb-20261021` | `8dfd934d53e23d5e8ee2e396167d3e2975a3102a` |

Native provider [models](https://docs.inceptionlabs.ai/get-started/models) and
[reasoning](https://docs.inceptionlabs.ai/capabilities/reasoning-efforts)
rechecked October21: Mercury3 remains text-only, low default, launch pricing
and four reasoning settings as documented above. Central provider presence and
vault permissions pass the safe helper check. This is access infrastructure,
not callability or private-payload permission. Owner checks and current route
receipts control the actual calls. No private inputs or runtime changes.

## Completed owner comparisons — 2026-10-21

**Prioritize independent Doc Web full-planner qualification; retain current
runtime choices.** Mercury3 wins the tested full generated-policy/cost screen
against GPT4.1, with a slower response. It does not preserve required ambiguity,
persona behavior or exact documentary attribution on the other selected tasks.
These are task/configuration verdicts, not a blanket model-quality claim.

| Owner/task, tested configuration | Fresh matched quality and decision | Candidate versus comparator subject economics |
| --- | --- | --- |
| [Doc Web report](/Users/cam/.codex/worktrees/scout100-docweb-20261021/docs/evals/evidence/082-scout100/report.md), medium65536 full planner |One aggregate constructed six-chapter cohort: both raw/normalized6/6 dispositions,3/3format mutations, correct child-note/uncertain cases. Mercury coherent full policy passes; GPT4.1 permits fragmentation while flagging it and canonicalizes fused headers while calling them defects. Independent coordinator blind source review agrees: **measured full-policy/cost winner; prioritize independent qualification**. Minor candidate unsupported preview-truncation wording retained. |USD.00409646 versus.027820;85.28% cheaper at launch, regular-price equivalent70.55% cheaper.23.937s versus10.931s,119%slower. No speed win, no whole-workflow savings claim. |
| [Dossier Attempt036](/Users/cam/.codex/worktrees/scout100-dossier-20261021/docs/evals/attempts/036-mercury3-long-history-20261021.md), high65536 long-history |One321KB authored-synthetic continuation: Mercury4/5 obligations preserved plus1minor versus Sol5/5. Candidate10rows reviewed (9preserved/1reasonable), Sol19/19preserved; zero material errors. Missing structured landing-papers attribution remains only in navigable source evidence. Minor severity does not satisfy hard all5/exact-basis gate. **Retain Sol medium16384; reject tested direct replacement.** |USD.01160811 versus.178118;93.48% cheaper.23.901s versus51.146s;53.27% faster. Faster subject does not erase lost structured meaning or qualification instability. |
| [Echo intent](/Users/cam/.codex/worktrees/scout100-echo-20261021/docs/evals/attempts/control-intent-v1/20261021-scout100.md), low32768 |13matched:11/13 versus Gemini13/13; both8/8control recall,0false controls on measured slice, ambiguity0/2 versus2/2. Best possible candidate1/3 ambiguity cannot meet comparator already-proven2/3;29remaining per arm unmeasured. **Retain Gemini3.8 Flash low2048.** |USD.00143930 versus.01014750;85.8%cheaper. Complete-body measured p951.385s versus9.974s;86.1%faster. Small progressive sample does not establish population tail latency. |
| Echo scene mapper, low32768 |Tavern0/1 exact for both: Mercury only fixed intensity default2versus1; Mini music/mood mismatches. Candidate roles/music/negative constraints otherwise pass. Intensity is a maintained default-contract mismatch, not numeric source contradiction. Mood ambiguity retained. **No demonstrated scene winner; retain mapper.** Dungeon unmeasured because2/2gate impossible. |USD.00213505 versus.008643;75.3%cheaper.10.384s versus8.475s;22.5%slower, both above soft5s. No fresh Mercury2.5 predecessor comparison. |
| [Storybook Attempt193](/Users/cam/.codex/worktrees/scout100-storybook-20261021/docs/evals/attempts/193-scout100-mercury3-persona.md), low32768 persona |3matched turns:Mercury2/3 versus Luna3/3. Explicit forbidden phrase plus inferred emotional meaning violates production Inference Firewall; fixed blind GPT5 concurs. Source-stop prevented further dispatch;9turns/all multi-turn continuity unmeasured. **Retain Luna none512.** |USD.00081833 versus.00041610,96.7%more expensive. Mean1.386s versus2.351s,41.0%faster;both within5s/.01 gates. Latency gain does not justify behavior regression. |

No mixed-model route is qualified. Echo's missed ambiguity cannot be selected
after the answer or by unvalidated confidence; keep Gemini for the full intent
call. Storybook retains Luna persona, Dossier retains Sol long-history extraction.
DocWeb's measured full planner is the maintained explicit GPT4.1 route, while
configured GPT5primary is unrun: no primary-call replacement or combined-path
savings claim. Any promotion must identify the actual intended call boundary,
retain source/layout/uncertainty guards and test the configured incumbent on
independent eligible material. No calls move in this campaign.

### Access, transport, reliability and effort

All owners received exact `inception/mercury-3` from Inception; catalog maps
dated20261019. Immutable served-weight revision/quantization remain unattested.
Strict required schemas qualified for Echo and Dossier; Storybook qualifies
plain text and DocWeb the actual JSON-object full-planner contract. No diagnostic
relaxation or semantic prompt/golden/scorer change was needed.

Echo28/28 calls, Storybook10/10, DocWeb2/2 terminal-valid on their bounded
serial samples; no broad reliability-rate claim. Dossier high32768 native
qualification compiled once but identical-wire parity exhausted32768 reasoning
without final output. The approved65536 allowance repair compiled, then full
candidate and control compiled. Preserve this operational failure/charge; it
is not a semantic miss. Full Dossier verdict is **high65536**, not an unreported
32768 quality pass. No thinking-level comparison: requested low for interactive,
medium for policy and high for history; reported nonzero reasoning supports
enabled thinking but is not independent internal-level attestation. Instant and
other unselected efforts remain unmeasured, not rejected. No rescue sweep.

### Spend and custody

Inclusive usage-based recorded spend **USD1.40800617/11.50**, unknown exposure0.
Candidate subjects.02009725; comparator subjects.22514460; independent judges
1.13630500; extra qualification/recovery.02645932. Native control/judge figures
are maintained-rate usage accounting, not provider account invoices. Dossier
includes the failed parity charge. No overhead is hidden in subject savings.

| Owner | Recorded USD / cap | Custody |
| --- | --- | --- |
| Echo |.02236485 /2.50 |Existing owner providers used. A temporary central OPENROUTER_API_KEY copy was removed before first POST; name-only absence verified, owner keys preserved. |
| Storybook |.04716998 /1.50 |One temporary central OPENROUTER_API_KEY injected safely into ignored isolated.env, removed after calls/name-only absence verified; owner native keys preserved. |
| Dossier |1.30655488 /6 |Existing owner router/OpenAI/Anthropic resolver; no temporary injection. |
| Doc Web |.03191646 /1.50 |Existing owner router/OpenAI normal wrapper with read-only env override; no temporary injection. |

All fixtures remained within the selected authored-synthetic scope. No private
provider eligibility, account/privacy changes, runtime defaults, deployment,
commits, pushes or landing. All four worktrees retained uncommitted.

### Evidence review and validation

Owner paths above retain exact commands, request/runtime/golden/source identities,
full raw envelopes, usage/finish/model receipts, frozen producing-code snapshots,
blind review packets and safe manifests. Starting base identities are in the
selection table. Coordinator reviewed actual owner reports and saved responses,
verified Echo archive and78manifest entries and DocWeb34manifest entries against
SHA256/size, performed blind full-policy source review before identity/economics,
and reconciled disjoint spend categories. Storybook's initial summary included
probes under subjectCostUsd; offline producer/summary/verification was corrected
to subjects.00123443 plus probes.00002055, preserving total/raw/ledger and exposing
the correction. No paid rerun.

Owner focused evidence/tooling checks: Echo5runtime boundary tests plus complete
raw/source/schema/scorer/ledger replay; Storybook42evidence entries plus7producing-source hashes/10raw envelopes/
10requests, source-stop/closed-ledger checks, lint/privacy/methodology; DocWeb11
source/uncertainty tests, Ruff and methodology. Dossier's focused corpus/runner/
review tests96pass, final artifact validator73JSON and94manifest files verified.
Full unrelated
product suites are inapplicable: changes are owner eval tooling/evidence, no
product runtime. Detailed final coordinator validation is saved alongside this
report: [final coordinator verification](evidence/scout100-coordinator-validation.json).

**Next recommended move:** prepare a bounded independent DocWeb full-planner
qualification with fresh authored-synthetic structure/evidence cases and the
actual intended configured consumer comparator. Freeze complete policy/reasons/
uncertainty criteria before outputs; include minor evidence wording and latency
tradeoff, not just status labels. Do not repeat this exposed cohort or add a
narrow sidecar. This requires a separate selection; no additional paid work or
runtime change is implied.
