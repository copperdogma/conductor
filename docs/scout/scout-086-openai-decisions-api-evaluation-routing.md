# Scout 086 — OpenAI Decisions API evaluation routing

Date: 2026-10-06 (America/Edmonton)
Status: Complete — selected comparisons finished; Storybook integration landed, disabled

Cam nominated OpenAI's newly available Decisions API as the same task class as
JEV. Stage 1 used public documentation and read-only inspection of all eleven
registered owners. Lower-cost agents inspected owner contexts; the coordinator
reviewed newer attempts where primary summaries were stale. Stage 1 made no authenticated
catalog/probe, credential use, paid calls or target writes. Approved Stage 2
execution and results are recorded below; no defaults, commits or pushes.

## Current official contract

- [Decisions guide](https://developers.openai.com/api/docs/guides/decisions):
  public beta, only `gpt-6-luna`, native `POST https://api.openai.com/v1/decisions`.
  Text and inline base64 images; predicate probability, finite choice with
  probabilities/confidence, and ordered score. Input-only USD0.10/million tokens;
  no output/cache read/cache write charges. Regional and long-context premiums
  can apply. The approximately 10x speed statement is a vendor claim, unmeasured
  in these owners. Standard nonregional short-context requests are proposed.
- [Native reference](https://developers.openai.com/api/reference/resources/decisions/methods/create):
  user messages only, at most128 inline images, no hosted image URLs/file IDs,
  files, audio, tool calls or item references. Per-question refusal is possible.
  Request exposes no reasoning-effort/sampling/custom JSON schema/tool controls;
  do not import Responses settings or invent a generated explanation.
- [Data controls](https://developers.openai.com/api/docs/guides/your-data): no
  training by default; abuse-monitoring logs normally up to30 days. ZDR is
  available to eligible customers; not proven enabled here. GPU-local encrypted
  prompt-cache tensors may persist24 hours and image CSAM exceptions apply.
  Only explicitly synthetic or owner-established public inputs are proposed.
  ZDR is optional for those inputs unless an owner requires it. Private/unclear
  inputs remain excluded; no account-policy changes.

Announced/API-documented: yes. **Access: unverified** for this endpoint/account.
Existing Responses access does not establish Decisions callability. An immutable
Decisions checkpoint/snapshot is not documented by this evidence; record the
requested and returned model exactly without inventing equivalence.

The evaluated-model ledger already records `gpt-6-luna` through generative
Responses evaluations and `jev-1.13.0`. This is an explicitly nominated new
Decisions product/primitive comparison, **not a new Luna checkpoint** or evidence
that previous semantic failures disappeared. Label applicable work as an
endpoint/configuration re-evaluation. Do not repeat unchanged Responses effort
sweeps or reinterpret documentation as having satisfied a previous retry gate.
The subsequent explicit selection authorizes only the comparisons below.

## Stable execution handles

1. **Doc Web — Evaluate now; USD10 total.** First lane: Story233
   `jev-consistency` five-class projection,20 unique synthetic cases across two
   source documents, twice each (40 judgments, not40 independent cases).
   Fresh Decisions versus pinned GPT-4.1 projection; preserve current
   deterministic comparators and retained JEV evidence. Prior JEV24/40,
   GPT29/40, actual cascade33/40 with17 fallbacks and3 false-clean defects.
   Freeze the existing labels, conventions, source hashes and policy; no
   threshold tuning on evaluation outputs. Qualify Choice/refusal, then run
   the maintained cohort; semantic misses are reported rather than changing
   its original continuation rule. Compare false-clean, per-class recall,
   review coverage, latency and full cascade cost. A useful result must reduce
   false-clean defects or improve cost/latency without worsening them; the
   original relative-value contract has no invented perfection/50% gate.
   Only test the predeclared fallback policy, with real calls where required.
   This cannot replace convention generation, rationale or repair planning.

   Independently screen image lane `crop-page-level-deletion-gate`: two-image
   source/crop verdict using Attempt048's repaired prompt and latest
   source-adjudicated22-case truth, not old Attempt015/047 golds. First the
   neighboring-portrait and integrated-photo/cover differentiators, then22
   if admissible; fresh GPT5.5 control. Require zero false-safe, report false
   rejection and uncertainty separately;22/22 is only this bounded set.
   Decisions cannot generate the required source-grounded explanation.
   Preserve explanation/manual review and account for any incumbent call;
   this qualifies a verdict component, not full strict-schema drop-in parity
   or automatic publication. Stop this lane on a source-confirmed safety miss;
   that does not cancel the independent text lane. Do not reopen historical
   prompt contradictions or treat a valid source correction as model tuning.
   Public-cleared benchmark pages only; if any source is unclear, exclude it
   before calls and report coverage rather than substitute a private scan.

   Reservation feasibility:22 control calls at46K input/2048 output and
   USD5/30 per million reserve USD6.41168; Decisions image22 at46K reserve
   USD0.1012. Text40 at4096 input/160 output reserves USD0.37888 for GPT4.1
   at2/8, USD0.016384 for Decisions, plus up toUSD0.37888 for actual fallback.
   Sum USD7.287024 leaves USD2.712976 for qualification/recovery and conservative
   accounting. No paid judge; independent source review and deterministic
   scorers. Confirm rendered sizes and current rates before dispatch.
   Text fixtures explicitly synthetic; image provenance must bind the owner's
   public benchmark sources. Overall workflow stage share is unknown; reduce
   consistency review errors or an expensive safety subcall, not claim a total
   pipeline saving from token price alone.

2. **Echo Forge — Evaluate now; USD1 total.** First `control-intent-v1`:
   48 synthetic frozen inputs (20 control/22 noncontrol/6 ambiguous), native
   Choice yes/no/abstain versus fresh Gemini3.8Flash low. Retained JEV is a
   historical reference, not a fresh paired arm or production default. Prior
   broader run Gemini44/48,20/20 recall,1/22 false activation,p95 2597ms;
   JEV30/48,15/20 recall,1/22 false activation,p95 323ms. Current later
   runtime-shaped42-case intent evidence is a separate scope; do not pool it
   with48-case diagnostic evidence. The comparison can qualify a faster
   control-intent component, not soundscape generation or playback authority.
   Start native qualification, then representative negation/quoted/no-action
   cases; stop for invalid contract, then complete the frozen diagnostic matrix
   to compare error types. Preserve the owner relative-value policy: a faster
   candidate with worse false activation/recall is a tradeoff, not automatic
   promotion. Proposed promotion screen: no worse false controls/recall than
   the fresh comparator and >=30% lower p95; earlier150ms aspiration remains
   separately reported, not a retroactive rejection rule. No confidence tuning
   on these48 exposed cases. Standard8K input/2048 output Gemini reservation
   at0.75/3.75 isUSD0.65664 for48; Decisions48 at8K isUSD0.0384, leaving
   USD0.30496 for probes/recovery. No paid judge or playback. Fresh runtime
   confirmation would require a later separately selected scope.

   Omit scene-intent/full-proposal replay: its repaired local baseline achieves
   4/7 useful positives versus JEV2/7 with14/16 review. The remaining candidate,
   context and confidence limitation is a complete-workflow issue; the new
   endpoint does not justify another label-only win or same-corpus tuning.

3. **Board Game Ingester — Evaluate now; USD1 total.** `synthetic-orientation-v1`
   through maintained `asset-orientation`:14 authored synthetic images,
   including12 determinate rotations, symmetry and ambiguous-art review.
   Fresh Decisions versus GPT6.1Sol low, plus provider-free blind baseline.
   Prior Sol12/12 determinate, Luna Responses11/12, Gemini10/12; Story021
   explicitly deferred Decisions while access was unavailable. Qualify image
   input and Choice rotation0/90/180/270/unknown, then differentiators and full14
   if contract-valid. Preserve12/12 rotation and both symmetry/review gates,
   exact pixel/inverse/hash/provenance proof and no-downsample requirements.
   Target at least30% lower p95 or full-stage cost at equal qualified quality;
   report14-case limits. No deskew, private Robo Rally crops or real-source
   uploads. Existing reason field cannot be filled with invented visual
   rationale: qualify an honest benchmark provenance adapter, distinguish
   unavailable explanation from evidence, and retain incumbent/manual review
   if the complete owner contract requires a generated reason. A rotation-only
   win is not full production parity. Sol14 at4096 input (1.25x write reserve)
   and2048 output reservesUSD0.43008; DecisionsUSD0.0057344. Remaining
   USD0.5641856 admits qualification/recovery. No paid judge.

4. **Storybook — Evaluate now; USD2 total.** Story150/167 relationship-correction
   early-exit routing, using Attempt159's12 synthetic unique cases twice (24
   judgments), fresh Decisions versus optimized Haiku routing plus the real
   full interpreter fallback. Retained JEV provides historical context.
   Attempt159 supersedes old Attempt158 economics: JEV and optimized Haiku
   routing24/24; full Haiku and cascade22/24,20.64% complete-task cost savings,
   p95 4.45% worse. Eight noops avoid Haiku;16 cases retain generated rationale.
   The maintained decision can support safe no-op/confirmation routing, not
   generated correction operations/rationale or automatic graph mutations.
   Qualify candidate IDs/action/ambiguity, then full cohort; preserve exact
   identity/action/backing-set/ambiguity guards and fallback. Stop on invented
   identity, wrong target or unsafe action; retain pre-existing absent-target
   defects separately. Compare complete cascade quality and actual cost/p95,
   not just routing prices. Proposed value screen: same qualified decisions
   with >=30% routing-p95 improvement and no worse complete-task quality/cost;
   small results only justify a bounded integration proposal. No new confidence
   threshold tuning on observed golds. Existing75-call comparison costUSD0.1191
   within an admittedUSD1 plan; keep that original request/reservation envelope
   and case count, adding bounded Decisions input calls within anotherUSD1
   allowance. Reconcile fresh full fallback reservations before dispatch;
   no automatic increase in case/prompt/output bounds to fill the cap.
   Synthetic correction fixtures only; no private names, family records or
   application database access. No paid judge.

**Campaign maximum: USD14.** Caps are provisional operator proposals, becoming
hard limits on selection. Paid subjects, controls, fallback, qualification and
recovery all count. A provider failure is access/transport evidence, not a
semantic miss. Recovery of a soft harness/judge fault continues inside the
selected hard cap; no new product/default/rollout choice is implied.

## Not recommended now

| Registered owner | Disposition and concrete reason |
| --- | --- |
| Dossier | **Defer.** A maintained same/different-identity `stage-judge` (GPT4.1Mini) is a plausible finite decision, but current Mariner/cross-domain fixtures have not been established as public/synthetic eligible for this endpoint; family histories can be private/licensed. Acquaintance-pair repair has unit tests, not a separately reviewed semantic benchmark. Do not substitute generic extraction or send the full graph. Freeze eligible judgment examples and prove a current caller/benefit before a paid proposal. |
| CineForge | **Defer.** Ordered-frame and ScriptBible lanes generate frame-indexed claims, descriptions, canonical names and rationale beyond finite primitives. Entity-validity is a potential subdecision but lacks independent semantic gold and does not remove its incumbent canonicalization/rationale call. Build that lane and complete-workflow payoff before calls; image support alone does not repair output mismatch. |
| Robo Rally | **Do not evaluate.** Maintained rules/scenarios require deterministic legality and simulation; no maintained tactical model-choice quality benchmark. |
| Ultima IV Web | **Do not evaluate.** Active source-recovery/admission and game-fidelity work is deterministic; no maintained external decision-model runtime lane. |
| VLC Thumbs | **Do not evaluate.** Sampling/cache/scheduler/bookmark work is deterministic. Thumbnail pixels do not create a semantic-decision requirement. |
| Financial Hub | **Defer.** Household advisory context is private; no maintained eligible synthetic decision benchmark or endpoint-qualified owner privacy policy. |
| Financial Monthly Analysis | **Defer.** Private transactions/source reconciliation remain source-owned and owner-confirmed; no eligible synthetic finite-choice lane established. |

Additional matching tasks omitted inside recommended owners: Doc Web bounding-box
generation/OCR need arbitrary coordinates/text; layout classification lacks an
enabled measured caller. Board Game source-role routing includes counts/group
constraints and private source fixtures; do not extend orientation approval to
it. Storybook photo/OCR/persona require generated fields/text; identity merges
lack an independently reviewed false-merge lane and volume evidence. Optional
retrieval reranking has previously shown limited complete-workflow gain after
anchor rescue; no unchanged rerun is proposed. Conductor itself has skill-driven
triage but no maintained high-volume labeled runtime decision benchmark: defer.

## Owner evidence and execution boundaries

- Doc Web [Story233](/Users/cam/Documents/Projects/doc-web/docs/stories/story-233-jev-consistency-classifier-evaluation.md),
  [frozen plan](/Users/cam/Documents/Projects/doc-web/benchmarks/jev-consistency/plan.md),
  [decision model guidance](/Users/cam/Documents/Projects/doc-web/docs/decision-models.md),
  [Attempt048](/Users/cam/.codex/worktrees/docweb-thinking-safety-20260929/docs/evals/attempts/048-repaired-page-safety.md).
- Echo [control comparison](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/attempts/control-intent-v1/20260920-broad.md),
  [Scout072](scout-072-jev-classification-opportunities.md),
  [complete-proposal/repair follow-through](scout-081-jev-additional-decision-seams.md).
- Board Game [Story021](/Users/cam/Documents/Projects/boardgame-ingester/docs/stories/story-021-harden-orientation-goldens-and-decision-subject.md),
  [maintained subject](/Users/cam/Documents/Projects/boardgame-ingester/benchmarks/subjects/orientation_model_compare.py),
  [registry](/Users/cam/Documents/Projects/boardgame-ingester/docs/evals/registry.yaml).
- Storybook [Attempt159](/Users/cam/Documents/Projects/Storybook/storybook/docs/evals/attempts/159-story150-jev-relative-comparison.md).

Selection requires isolated current-base owner worktrees, owner instructions and
portable execution/custody protocols, zero-cost rendered-matrix/prompt/fixture/
price/reservation preflight, no hidden retries, exact identity/native receipts,
separate access/transport/reliability/capability/economics/adoption verdicts, and
temporary credential cleanup. If current owner context materially changes a
lane/privacy/cap, obtain that missing decision; do not silently widen approval.
No owner probe was performed in Stage1. The evaluated ledger is intentionally
unchanged until a selected owner attempt reaches authenticated qualification.

Reply `yes` to run all numbered evaluations, or `only do 1, 3` for a subset.

## Approved follow-through — 2026-10-06

Cam replied `yes`, selecting all four numbered owners: Doc Web USD10,
Echo Forge USD1, Board Game Ingester USD1, Storybook USD2; combined hard maximum
USD14. Separate owning-repo workers were dispatched before any root provider
call. The root coordinates and reviews evidence, with no duplicate owner calls.
Each worker creates a dedicated current-remote-base `codex/` worktree and uses
only its approved synthetic/public lanes and existing owner access. Presence-only
central custody inspection found no OpenAI provider entry; no central secret
was read, copied, imported or provisioned. Existing owner key reuse is within
the selected campaign; secret values remain owner-local. No defaults, deployment,
commits, pushes or merges are authorized. Final owner bases, attempts, spend,
stops, cleanup and layered verdicts will be appended here without rewriting
the original proposal as though it predicted results.

Coordinator verified the isolated branches and full base identities directly:

| Owner | Worktree | Branch | Fetched base |
| --- | --- | --- | --- |
| Doc Web | `/Users/cam/.codex/worktrees/decisions-docweb-20261006` | `codex/decisions-docweb-20261006` | `19b30b1d0db4a7f3b2e31614ba9846dfdb93355c` |
| Echo Forge | `/Users/cam/.codex/worktrees/decisions-echo-20261006` | `codex/decisions-echo-20261006` | `69631247146c0a9770a02e2ddd71c4d88628a901` |
| Board Game Ingester | `/Users/cam/.codex/worktrees/decisions-boardgame-20261006` | `codex/decisions-boardgame-20261006` | `ff1a9fe799744ac82ff8aca4b73301826c358600` |
| Storybook | `/Users/cam/.codex/worktrees/decisions-storybook-20261006` | `codex/decisions-storybook-20261006` | `12c293662dae45af95b34d5a6dd75f887f9d8cdb` |

The existing owner OpenAI credentials are reused without copying. Board Game's
authenticated catalog sees both exact requested IDs; this is discovery, not
Decisions callability or quality. Storybook's existing Anthropic and Echo's
existing Google credentials remain owner-local comparator access.


## Completed owner decisions — 2026-10-06

All four selected owners qualified the exact native `gpt-6-luna` Decisions
endpoint with their own existing access. This proves callable text/image Choice
for these owner contexts, not a newly identified checkpoint or universal access.
Fresh comparators used the same frozen eligible inputs. No paid judge, semantic
retry, confidence fitting, prompt tuning or golden change was performed.

| Maintained task | Decisions vs fresh incumbent | Economics and practical verdict |
| --- | --- | --- |
| Doc Web consistency,20 unique ×2 |22/40 exact vs GPT4.1 28/40;4 vs2 false-cleans. Actual cascade30/40 with3 false-cleans and26 fresh fallbacks. | Candidate p95 369ms vs1027ms, subject USD0.0021728 vs0.043432. Cascade p95 1387ms and USD0.0303648. **Retain GPT4.1**: extra missed defects defeat the cheaper/faster raw component; cascade also worsens safety/latency. |
| Doc Web crop safety,22 public page/crop pairs |17/22 vs GPT5.5 18/22; both0 false-safe,5 vs4 false-rejects. | Candidate p95 3295ms vs5848ms, subject USD0.0240819 vs1.283065. **Retain existing explanation/manual-review path**: verdict screen is faster/cheaper but adds rejection and supplies no rationale. No full workflow replacement or representative safety guarantee. |
| Echo control intent,48 synthetic cases |37/48 vs Gemini3.8Flash low45/48; both20/20 controls recalled,7 vs2 false activations,2/6 vs5/6 correct ambiguous abstentions. | Candidate p95 415ms vs5988ms, subject USD0.0022873 vs0.033855. **Retain Gemini**: five extra false controls fail the declared relative quality screen. |
| Board Game synthetic orientation,3 completed pairs |1/3 vs Sol/low3/3; blind baseline1/3 on this slice. Two source-confirmed wrong rotations trigger the semantic stop. | Candidate p95 777ms vs7520ms, subject USD0.0001011 vs0.005698. **Retain Sol**. Eleven remaining cases, including symmetry/review, are unmeasured; speed/cost are not qualified savings. |
| Storybook early-exit routing,12 unique ×2 |Decisions and optimized Haiku routing24/24. Actual serial cascade and full Haiku both20/24; six noops skip full interpretation and18 retain fresh full calls. | Route p95 395ms vs2831ms, subject USD0.0058152 vs0.034355. Cascade USD0.0808632 vs full0.092091 (12.19% saving); p95 4523ms vs4154ms (8.90% worse). **Conditional integration candidate for this narrow route**; retain full interpreter/rationale and guards. |

Subject costs exclude qualification and separate comparison arms; the inclusive
accounting below includes every paid request and actual serial fallback.
Nearest-rank p95 on these small serial cohorts is a sample measurement, not
throughput, statistical superiority, a billing invoice or a general model rank.

| Owner | Paid calls | Settled usage-priced USD | Unknown maximum USD | Hard ceiling USD | Authoritative isolated attempt |
| --- | ---: | ---: | ---: | ---: | --- |
| Doc Web |153|1.3866489|0|10|[Attempt063](/Users/cam/.codex/worktrees/decisions-docweb-20261006/docs/evals/attempts/063-decisions-api.md)|
| Echo |98|0.0367124|0|1|[Control diagnostic](/Users/cam/.codex/worktrees/decisions-echo-20261006/docs/evals/attempts/control-intent-v1/20261006-openai-decisions.md)|
| Board Game |6|0.0057991|0|1|[Orientation attempt](/Users/cam/.codex/worktrees/decisions-boardgame-20261006/docs/evals/attempts/20261006-decisions-orientation.md)|
| Storybook |75|0.1330764|0|2|[Attempt178](/Users/cam/.codex/worktrees/decisions-storybook-20261006/docs/evals/attempts/178-story150-decisions-native-relative.md)|
| **Total** |**332**|**1.5622368**|**0**|**14**|No paid judge or retry charges.|

### Source adjudication, recovery and strategic review

Coordinator independently reviewed Echo's false-control/ambiguity sources and
Doc Web's text mismatch families against the frozen policies: labels are
supported, without a scorer/golden repair. Direct visual inspection confirms
Board Game's DOCK output remains sideways while the required rotation restores
upright lettering. The HARBOR error is separately documented by the owner.
Board Game dispatched its third pair before source review confirmed the second
pair's error; both charges are retained and no further calls followed.

Coordinator also opened Doc Web's mismatch contact sheet:021000/021001 preserve
whole photos and exclude captions/neighbors;004000 includes the complete wagon
drawing. These are source-confirmed false rejections. Decisions supplies no
reason, so no visual explanation is attributed to its label. GPT5.5's generated
claim of missing horses on004000 is contradicted by the retained source/crop.

Storybook preserved one full Haiku response with unsupported operationType
`observe` as a contract failure, without semantic normalization. The harness
continued from saved row17 and finished the approved cohort without duplicate
paid calls. Full/cascade each have23/24 schema-valid outputs and20/24 end-to-end
passes; valid-only semantic score is20/23. Remaining misses include repeated
absent-target and negated-request failures, not unsafe Decisions routing.
One cascade duration is reconstructed from the actual serial native durations;
23 use wall timers. The slower complete-task p95 remains disclosed.

Strategic checkpoint: the original question is now resolved by task, rather than
by endpoint speed alone. Native finite choices fit Storybook routing, where
six safe exits actually avoid interpretation. They do not remove generated
rationale or repair full-interpreter defects. Confidence-only cascades do not
justify promotion where confidently wrong outcomes remain; no post-hoc
threshold or new tuning campaign is proposed. The established alternative is
the maintained full structured-output interpreter with source-grounded review,
as contrasted by the official Decisions guide and each owner contract.
Finish evidence review and stop paid work; integration is a separate decision.

### Custody, validation and next action

Owner manifests retain source/prompt/fixture/scorer identities, exact native
requests/raw envelopes, usage/latency, stop/recovery chronology and commands.
Echo's208 protected files and Board Game's94 manifest hashes were verified by
owners; coordinator separately reran Echo and Storybook provider-free replays successfully.
Doc Web's lossless receipt reconstruction independently restored/verified all306
request/response files; the coordinator temporary replay directory was removed.
Owner focused tests passed: Doc Web41, Echo9, Board Game43, Storybook14.
Doc Web's complete artifact manifest and deduplicated receipt archive bind
all153 native parses and source-safe original payloads; Storybook's88 artifact
hashes and75-receipt chronology/scoring replay passed.
Doc Web and Storybook retain full source-safe campaign artifacts in their
isolated worktrees. Per-owner focused tests, offline replay, scoped lint and
methodology checks supply validation; unchanged application suites add no
endpoint evidence. Coordinator synthesis receives a separate diff check.

Only existing owner credentials were reused in memory/wrappers. No central
secret was injected, no key was copied or provisioned, and temporary dependency
links were removed. Shared primary changes remain untouched. All worktrees and
durable evidence are retained for review; no archive, commit, push, merge,
product configuration, deployment or default change was made.

Recommended next step: prepare a bounded Storybook integration for Decisions
as the qualified early-exit component, retaining Haiku fallback, rationale and
all identity/action/ambiguity guards. Include the measured complete-task tail
latency regression and existing interpreter defects in its acceptance criteria.
Do not promote it as a full interpreter or spend again on exposed failed lanes.


## Approved bounded integration — 2026-10-06

Cam replied `yes` to the completed campaign's recommendation for a bounded
Storybook routing integration retaining Haiku fallback and existing safeguards.
Implementation continues in the same isolated Storybook worktree under owner
build-story context; no new paid calls, private payload qualification, activation,
deployment, commit or push. Explicit opt-in native Decisions mode-only routing
may shortcut a confident no-op; full interpretation owns all remaining details,
rationale and confirmation. Existing JEV settings and defaults remain intact.
This runtime request projection is narrower than the evaluation's full-input,
multi-question adapter; provider-free integration verification does not turn
historical24/24 semantic results into production parity proof.


Integration review: coordinator inspected native streaming bounds, exact
HTTP/model/question/distribution qualification, minimized mode semantics,
opt-in selection without router chaining, explicit-confirm preservation,
endpoint-specific cost identity and actual served-model records, captured-signal
consumer/persistence/budget tests, operator docs and provider inventory. A
post-read response-size check was replaced by a bounded streamed reader; an
unrelated OpenRouter privacy-status edit was restored. No remaining material
finding in the reviewed bounded scope. Native response controls include a
1.8-second deadline through reads,64KB streamed body cap and HTTP200-only
admission; no retry or redirect. All non-noops invoke Haiku, with safe explicit
confirmation preserved after fallback. Known usage survives semantic rejection.

The implementation is tracked by [Story191](/Users/cam/.codex/worktrees/decisions-storybook-20261006/docs/stories/story-191-decisions-relationship-routing.md)
and [operator documentation](/Users/cam/.codex/worktrees/decisions-storybook-20261006/docs/tech-stack.md#optional-decisions-relationship-routing-story-191).
This reduces implementation risk while preserving the quality limits from the
small exposed comparison. In particular, a structurally tested minimized
request and new confirmation guard do not revise Attempt178's measured20/24,
12.19% task saving or8.90% worsep95. Paid calls and unknown exposure remain
unchanged. Existing primary/runtime JEV settings remain untouched.


Final integration verification: [owner validation](/Users/cam/.codex/worktrees/decisions-storybook-20261006/docs/reports/story191-decisions-routing.md)
records227 distinct affected backend tests (including44 native and8 real
captured-signal consumer cases),12 environment/privacy tests, workspace
typecheck/lint, backend/frontend builds, provider inventory/privacy coverage,
methodology and actual provider-free HTTP200/DB-connected smoke. Coordinator
independently matched all10 final source hashes and the227-test receipt total,
and inspected the durable HTTP receipt. Unchanged Attempt178 replay still
verifies its8 frozen sources,75 receipts,24 rows and original spending. Existing
global provider-review expiry and frontend bundle warnings remain disclosed.
The task database was dropped with catalog count0; HTTP process/port and
its temporary receipt were cleaned. No credential/env copies, new API charges,
activation, private calls, commit, push or deployment. Shared primary HEAD
`14767978eeb5bed7ba8d04b1ec21f7c33a7b9387` and its two original dirty entries
remain untouched; this is isolated, validated and unlanded implementation.

Owner Story191 marked Done through its closure workflow after validation;
generated methodology/index and final diff checks passed. Integration remains
uncommitted, unlanded and disabled. Next step is scoped landing if Cam selects it.


## Authorized selected landing — 2026-10-06

Cam approved committing/pushing the Storybook integration and its Conductor
record. Two-repository preflight cleared before any push. Storybook's116-file
explicit allowlist includes Story191 runtime/docs/tests and prerequisite
Attempt178 source-safe evidence; prior227 backend/12 env/privacy tests apply to
the unchanged final source hashes. Fresh closure/privacy/replay/staged-diff
checks passed, including88 archive hashes,3 derived source hashes and75
no-header raw envelopes. No further paid calls or evaluation changes.

Storybook execution branch `codex/decisions-storybook-20261006` and remote
`main` were independently verified by `git ls-remote` at
[`ca442a3e62dd538bcd9f9160198b933783babdae`](https://github.com/copperdogma/storybook/commit/ca442a3e62dd538bcd9f9160198b933783babdae).
Landing fast-forwarded the unchanged fetched base12c29366; no merge or runtime
revalidation was needed. The isolated worktree is clean and retained. Its shared
primary HEAD14767978 and two unrelated dirty entries remain untouched.
[Canonical owner validation](https://github.com/copperdogma/storybook/blob/ca442a3e62dd538bcd9f9160198b933783babdae/docs/reports/story191-decisions-routing.md)
and [canonical evaluation](https://github.com/copperdogma/storybook/blob/ca442a3e62dd538bcd9f9160198b933783babdae/docs/evals/attempts/178-story150-decisions-native-relative.md)
retain the detailed evidence and limits.

Conductor records are prepared on clean current remote main48bca19 in
`codex/decisions-campaign-landing-20261006`. Only Scout086, its index entry,
matching inbox capture and native-endpoint ledger additions/row prefixes are
included. Newer remote historical ledger outcomes/retry cells are preserved
exactly; unrelated primary files and other-owner evaluation worktrees are not
landed by this narrower authorization. Relative history links use the canonical
remote filenames. Campaign links, four-file scope, whitespace, `make lint` and
`make methodology-check` passed. No product suites are required for these docs.

Storybook is landed **disabled**. Operator activation, deployment, fresh runtime
semantic qualification and other-owner evidence landing remain separate work;
this commit/push authorization changed none of them. Both task worktrees are
retained; no primary checkout synchronization or cleanup was requested.


## Explicit default activation — 2026-10-06

After the separate integration/landing, Cam instructed: “Just turn it on. No
flag. It’s fine.” This supersedes the prior disabled/opt-in adoption boundary
for Storybook's eligible relationship-routing component. The authorized outcome
is a code default without the Decisions enable flag or a JEV override, retaining
Haiku fallback, confirmation and capture/spend/native-contract safeguards, then
clean committed/main deployment and actual hosted-route verification. Existing
owner OpenAI access and standard development retention apply. Other owners'
model choices and existing unrelated production privacy/identity policy do not
change. Prior comparison scores remain historical; activation is not a new
semantic-quality claim.


### Hosted default verified

The approved default change landed on Storybook branch/main at
[`9fc5f34817a74cc1ce827e9e67e77e3d4c65b348`](https://github.com/copperdogma/storybook/commit/9fc5f34817a74cc1ce827e9e67e77e3d4c65b348)
and deployed as release42 from a separate clean main checkout. Native adapter,
frozen prompt meaning and pricing were unchanged; default factory selection
replaces both routing flags and retires the JEV runtime dispatch. Fresh122 backend
and9 environment/privacy tests, workspace typecheck/lint, production builds and
pinned Dossier install passed. Earlier validation receipts remain historical.

Exact deployed image is
`sha256:afdac98f4b24db364b5a27cfbf52ebd558f236afb85ad87fd1835dcc74a7a4ad`.
Enforced candidate media and PDF/OCR startup checks passed before bluegreen.
Rollback authority remains prior release41 image
`sha256:140d7e63d2a3c3be3c2bbb2b0ea9c0b71574f6765de81724f8b55f6db6088c96`.
Health200/DB connected/dependencies ready, root/login/bundle200 and authenticated
user.me200 (owner fields redacted) passed. Root independently refreshed the live
login browser and visually inspected it; error/warning logs were empty.

One fictional no-database-write smoke invoked the default factory inside the
exact deployed image with the actual owner key and no routing flags. It made one
native Decisions call: HTTP200, served `gpt-6-luna`, noop0.98,432 input/0 output,
998ms provider/1001ms total, zero fallback and zero unknown usage. Estimated cost
USD0.0000432 brings Storybook campaign plus activation smoke to USD0.1331196
within its USD2 ceiling. The smoke uses an explicitly synthetic fallback stub;
it qualifies live access/default selection, not full-consumer quality or fresh
semantic parity for the minimized request. No private replay or saved-data write.
[Owner deployment artifacts](https://github.com/copperdogma/storybook/tree/d9cb51527e4e5b16a3e406617da8e72caf1f1ba2/docs/reports/artifacts/story191-default-adoption-20261006)
and [deployment log](https://github.com/copperdogma/storybook/blob/d9cb51527e4e5b16a3e406617da8e72caf1f1ba2/docs/deploy-log.md)
retain release/topology, source/image hashes, bounded cost and checks.

Production topology is one active app/worker plus a stopped standby, all on the
new digest; standby association and production override checks passed. Worker
Dossier readiness/private approval and the existing USD30/day identity cap were
preserved. Incident delivery check passed; one preexisting processing incident
remains. Both shared primary checkout status/tracked/staged fingerprints match
the pre-landing snapshot exactly. No primary synchronization or cleanup occurred.

Owner deployment/closure receipts landed on verified branch and remote main at
`d9cb51527e4e5b16a3e406617da8e72caf1f1ba2`; follow-up commits are documentation
and sanitized evidence only. The running image source remains9fc5f348.
