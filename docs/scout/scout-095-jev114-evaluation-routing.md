# Scout 095 — Jev 1.14 evaluation routing

Date: 2026-10-14 (America/Edmonton)
Status: Selected evaluations complete; both owner evidence commits landed and verified.
The original Stage1 recommendation and its revision are preserved below.

Cam invoked evaluate-model on https://typesafe.ai/blog/jev-1-14.
Inspected all eleven registered projects, Conductor planning surfaces and the
evaluated-model ledger. Two read-only economical workers assisted; coordinator
checked their conclusions against current owner source and corrected unsupported
visual admission, budget and consumer conclusions. No credentials/catalog probes,
owner mutations, inference, commits, pushes or defaults changed. Dirty primary
checkouts were preserved. Owner remote-tracking refs are locally available
snapshots, not a claim of freshly fetched server heads; Stage 2 must refresh.

## Verified public contract

- [Release](https://typesafe.ai/blog/jev-1-14), dated October14: new checkpoint
  `jev-1.14.0`, now behind preview; improved general judgments/multilingual support
  are vendor claims. Experimental images, boxes and longer context are distinct
  features, explicitly below the provider's production quality standard.
- [Models](https://docs.typesafe.ai/models): API-listed exact `jev-1.14.0`, native
  `POST https://api.typesafe.ai/v1/systemone`. USD.042/M input, output free;
  default64k/request and32k/question. `jev-preview` points to1.14;
  `jev-latest` still1.13 today. Pin exact ID and verify response.model.
  **Access: unverified**; public documentation is not a successful owner call.
- [API](https://docs.typesafe.ai/api): typed Choice/Noul/Score, experimental Box;
  no documented selectable thinking effort or general generated-text/tool-call
  contract. Use native default computation; no effort sweep. Long-context flag
  remains off for this short-input campaign.
- [Images](https://docs.typesafe.ai/images): explicit
  `TypeSafe-Danger-Zone-Images: true`, PNG/JPEG, each axis256–1568 and area
  >=78,400pixels,16MiB/image and32MiB body/expanded limits. Multiple stills can
  be labeled in order; no direct audio/video generation. Image input tokens
  are billed at text rate; tokenizer guidance is not yet supplied.
- [Box](https://docs.typesafe.ai/primitives/box): one normalized rectangle per
  question, no absent-target output. A separate presence/count decision is needed;
  probability concentration is not source completeness or calibrated safety.
- [Data policy](https://docs.typesafe.ai/legal): no training on customer data;
  ZDR is offered for enterprise, not established for this owner/account.
  Ordinary retention remains unverified. Selected synthetic fixtures may be
  retained; no private records, scans or account-setting changes authorized.

Ledger match: only pinned `jev-1.13.0` previously attempted (latest Sept30).
Moving aliases do not collapse the new checkpoint into those attempts. Historical
Jev speed/low cost but control-recall/abstention deficits motivate a new-checkpoint
comparison, not a repeat of unchanged1.13. No ledger evaluation row is added
before an authenticated Stage2 attempt.

## 1. Evaluate now — Echo Forge control intent — USD1 inclusive

Owner lane: `control-intent-v1`, **42 current-runtime-shaped synthetic cases**,
against fresh native `gemini-3.8-flash`, low thinking,2048 total output tokens.
Jev1.14 native default computation, one Choice yes/no/abstain; no confidence
threshold tuning, long context, image feature, soundscape generation or playback.

Maintained consumer: `server/control-intent.mjs`, documented in
`docs/control-intent-runtime.md`. The caller consumes exactly one control label;
it does not require generated rationale, target or audio. Code retains operation,
source identity, permissions, stale-response guards and manual/executor rules.
This makes a finite challenger meaningful even though Jev is not the incumbent.

Use the existing source-adjudicated current-input42 definition from
`docs/evals/attempts/control-intent-v1/20260926-openai-gpt6-sol-luna.md`
and `scripts/control-intent-v1-gpt6-production-replay.mjs`. Preserve the original
48case diagnostic separately; exclude008/009/019/024/027/045 whose original gold
requires context omitted by the product. Freeze current source/request/gold
mapping before calls. If source changed, recheck applicability offline; no
invented prior dialogue or favorable post-result case selection.

Why now: materially new checkpoint meets the prior owner's retry trigger;
the actual caller already supports this decision. The Oct13 portfolio screen
do not establish a current Jev1.14 result. Prior richer48 Gemini44/48 versus
typed challengers31–41/48 shows the quality bar matters. Prior1.13 was fast and
cheap but missed controls. Test whether1.14 closes that gap. Whole-PTT time/share
is unknown; classify-only latency/cost and manual interruptions are the outcomes.
Prior Gemini richer48 subject cost .03639375 makes absolute dollar savings small;
latency and safe recognition must justify another provider's maintenance.

Progression: offline rendered matrix/parity/admission first, then positive,
negative/quoted and ambiguous native qualification, then all42 fresh matched
independent requests in balanced order. Verify exact served checkpoint, complete
state, native typed envelope/usage and deterministic projection into control.
An adapter is required; no claim of HTTP drop-in parity. Contract/access failures
stop affected calls, semantic labels remain evidence. Complete the fixed screen
despite isolated classification errors so relative safety can be judged; executable
output or broken action boundary stops. Preserve failures and bounded operational
recovery under the hard cap; no semantic retries or prompt/gold changes.

Useful result requires no worse exact accuracy, control recall, false-control
rate or ambiguous handling than the fresh comparator, plus >=30% lower p95 as a
soft practical improvement target. Report paired errors and sample limits;
150ms remains aspirational, runtime15s deadline is operational. A numerical tie
does not establish broad reliability; no rollout follows this exposed synthetic
screen. No paid judge: existing scorer and independent source review suffice.
No additional thinking arms,1.13 subject arm or conditional confirmation proposed.

Reservation feasibility, using current
[Google standard rates](https://ai.google.dev/gemini-api/docs/pricing):
42 Gemini calls × (8192input×.75/M +2048output×3.75/M)=USD.580608;
42 Jev calls conservatively reserving full64,000input×.042/M=USD.112896.
Three extra qualification calls per arm reserveUSD.049536; subtotalUSD.743040,
leavingUSD.256960 recovery/unknown exposure withinUSD1. Default per-question
limit remains enforced. Actual short-state cost should be much lower; these are
admission bounds, not predicted charges. Recheck rendered tokens/prices before
sending. Do not spend comparator-only if candidate access is unavailable.

**Campaign maximum: USD1.00.** Agent usage is separate from provider spend.

## Not recommended now — every other registered owner

| Owner | Disposition and task-specific reason |
| --- | --- |
| Doc Web | **Defer.** All22 maintained page/crop safety pairs fail native Jev image admission: every source page is2000px tall; several crops much larger. Owner070 requires exact source geometry/no resizing. Detector pages face the same admission problem; one Box is also not its variable-count/generated-description contract. OCR/literal reading generates novel text/cells, unsupported by Jev. Text consistency is a measured finite lane but its optional sidecar retains the full planner and adds cost; useful connected review/consumer benefit is still missing. No unchanged projection rerun recommended. |
| Board Game Ingester | **Defer.** Existing synthetic-orientation-v1 is a valid finite angle/review task, not a Box task. Native144×176/176×144 crops (25,344pixels) violate both axis and area minima; public fixtures include256×256 and still smaller crops, also below area minimum. Owner prohibits resize/upscale qualification rescue. Need independently frozen eligible native-resolution corpus, not a paid transport failure or bigger padded copy. Retain Sol/review; segmentation/counting/deskew has separate contracts/private inputs. |
| CineForge | **Defer.** Five ordered640×360 synthetic frames are admissible, but maintained13-key visual understanding requires generated evidence/continuity descriptions; no finite-only consumer or scorer/payoff yet. Entity adjudication also generates canonicalization/aliases/reasons; classification alone does not remove its call. No image-format incompatibility asserted. |
| Dossier | **Defer.** Active semantic extraction generates entities/spans/provenance; stage judge needs evidence/reasoning and private fixtures are excluded. Acquaintance-pair heuristic is a possible semantic seam, but no current independently labeled finite lane or measured repair gap makes a new adapter worthwhile yet. |
| Storybook | **Defer.** Current Decisions mode selector + Luna interpretation is a relevant typed seam, but Attempt182 grounding deferrals and downstream completion acceptance need resolution first. Retirement of Jev is not itself disqualification. Photo/OCR/persona generate content; no maintained eligible finite visual consumer. Passage ranking's exact-anchor rescue limited practical gain. |
| Robo Rally | **Do not evaluate.** Maintained deterministic rules/legality/simulation; no model-owned finite perception caller. |
| Ultima IV Web | **Do not evaluate.** Original/rebuilt fidelity and earned adaptive-play evidence; no maintained Jev-compatible runtime/oracle. |
| VLC Thumbs | **Do not evaluate.** Native decoding/cache/scheduling/bookmarks and image/performance proof; no AI semantic caller. |
| Financial Hub | **Defer.** Private household material; no maintained eligible synthetic decision corpus or selected provider policy. No private content read. |
| Financial Monthly Analysis | **Defer.** Private source reconciliation; same eligibility/maintained-lane gap. No private content read. |

Conductor itself: defer, no maintained labeled runtime classifier. No new model
tournament, gameplay classifier or synthetic visual benchmark invented.

## Evidence and applicability checks

Read owner AGENTS/Ideal/spec/eval context through workers; checked current
origin/main source where primary checkouts lag. Snapshot origins: Dossier
f5433ff, Storybook2b6ee04, DocWeb790da90, Echo1dc25e4, CineForge3a02901,
BoardGame dd775b6, RoboRally1f95fdf, Ultima a49648d, FinanceHub c945fe5,
Monthly6254f5d. VLC is nested under Ultima; owner source inspected separately.

Key owner records at those refs:
- Echo `docs/control-intent-runtime.md`, `server/control-intent.mjs`, Sept26
  current-input attempt, Oct13 Scout091 attempt/applicability manifest.
- DocWeb `docs/evals/attempts/070-scout091-five-decision-models.md` and
  `docs/evals/evidence/070-scout091/image-topology.json`: coordinator parsed
  every native source/crop dimension against Jev's documented bounds;
  **0/22 fully admissible pairs**. Zero-cost local applicability check.
- Board `benchmarks/fixtures/synthetic-orientation-v1/input-manifest.json`,
  `docs/evals/attempts/20261013-scout091-orientation.md`, Oct13 Argon public
  orientation attempt; Cine `docs/evals/registry.yaml` ordered-frame task.
- [Scout091](scout-091-five-decision-models-evaluation-routing.md) provides
  direct durable owner pointers and latest portfolio consumer trace; [Scout081](scout-081-jev-additional-decision-seams.md)
  preserves the failed Echo full-proposal usefulness boundary.

Validation: public contract/alias/ledger checks, source dimension admission,
runtime finite consumer trace, reservation arithmetic and scoped link/whitespace
review. Documentation only; no product suites or paid tests needed.

Practical result: one small test can decide whether faster control recognition
preserves Gemini's accuracy. The new vision features do not justify resizing
frozen owner fixtures or claiming that typed geometry replaces OCR/generation.

Reply `yes` to run evaluation1 withinUSD1, or decline/defer it.
Selection is required by evaluate-model/SKILL.md Stage1; no further ceremonial
approval is needed for this exact scope once selected.

## Revised recommendation — existing decision callers, 2026-10-14

Cam asked whether the new version should be compared with other decision models
already in place. **Yes.** The initial Storybook deferral was too broad: shared
downstream grounding defects constrain complete-task adoption, but do not prevent
a useful isolated mode-quality comparison against the deployed decision caller.
Retirement of1.13 is not evidence against1.14. This addendum supersedes that
Storybook disposition; all other dispositions and item1 remain unchanged.

### 2. Evaluate now — Storybook relationship mode — USD0.50 inclusive

Compare native pinned `jev-1.14.0` with fresh native `gpt-6-luna` Decisions on
the existing independently reviewed24 synthetic Attempt182 scenarios, up to two
passes (48 observations per arm;24 independent cases). Use the actual minimized
runtime state, existing mode instructions/choices, existing confidence policy,
1800ms runtime deadline and strict identity/envelope/usage validation.
Neither route has a selectable thinking setting in this contract; no effort sweep.
Only public/synthetic authored inputs are eligible; ordinary provider retention
is disclosed, ZDR unverified. No real family material, model defaults or deployment.

First zero-cost preflight the current runtime adapter, state coverage, case/gold
mapping, native projection and complete resolved request/cost matrix. Qualify
representative noop/confirmation/correction native cases before the paid matrix.
First pass measures raw mode correctness, accepted correctness/coverage, dangerous
confident noop, clarification preservation, fallback frequency, cost and latency.
Stop expansion on source-confirmed unsafe confidently accepted routing, invalid
identity/contract or breached budget. Run the fixed second pass only if first-pass
quality is no worse than fresh incumbent with no new unsafe accepted mode;
measure disagreement without tuning thresholds or replaying semantic failures.
Operational repair remains allowed inside the cap with failures retained.

Useful advancement requires no worse accepted-mode correctness and dangerous
misses/review coverage than fresh Luna, plus a material >=30% decision-stage cost
or latency improvement. Lower token prices alone do not qualify. Known grounding
deferrals remain separate. This is explicitly a finite-router comparison, not a
fresh full interpreter/cascade, postguard/persistence or deployed quality claim.
No paid Haiku interpreter or judge is included; retain existing offline consumer
boundary regressions and report which downstream outcomes are unmeasured.
Moving noop/fallback boundaries would require a later complete-path promotion
check; this selection does not authorize that or runtime changes.

Feasibility: conservatively48Luna calls×24,000input tokens×USD.10/M=.115200;
48Jev calls×32,000state-plus-question tokens×USD.042/M=.064512.
Six additional admission calls per arm reserve.022464; subtotalUSD.202176,
leavingUSD.297824 for bounded operational recovery and unknown exposure.
The24,000-byte runtime body bound is a conservative token reservation, not an
expected payload size. Native current Luna rate is recorded in owner pricing and
runtime cost tests; refresh route/price and resolved tokens before dispatch.
No full-interpreter output reservation is hidden in this finite-only proposal.

Current owner proof: origin/main
`packages/backend/src/ai/prompts/decisions-relationship-routing.ts` pins Luna and
builds one mode Choice; `packages/backend/src/ai/decisions-relationship-router.ts`
enforces the runtime contract. Story191 records the actual default deployment.
Attempt182 and Conductor's
[owner boundary evidence](/Users/cam/.codex/worktrees/storybook-scout095-jev114/docs/evals/attempts/183-story150-jev114-finite-mode.md)
keep component, postguard and persistence claims distinct. No new source/golds,
private fixture use or benchmark weakening is proposed.

Doc Web remains deferred: Jev/Perplexity consistency paths are optional advisory
sidecars after the required planner, not an adopted replacement whose lower
classification cost removes that planner. Solar and Microsoft evaluations are
not deployments. A new checkpoint permits a new test where an actual decision
can change; it does not supply a missing worthwhile consumer or resolve visual
native-size constraints.

**Revised stable handles:**1EchoUSD1;2StorybookUSD0.50.
**Revised campaign maximum: USD1.50.** Prior provider spend remainsUSD0.
Reply `yes` to run both, or `only do 1` / `only do 2` to select a subset.
Cam's question requests reconsideration, not a provider-spend selection.

Validation: read current owner native prompt/router/default deployment and
Attempt182/boundary correction, checked component scope and reservation sums.
No provider calls, owner changes or product tests.

## Selected execution — 2026-10-14

Cam replied `yes` to the revised two-item proposal: EchoUSD1 and
StorybookUSD0.50, combined hard inclusiveUSD1.50. Two isolated owning-repo
workers dispatched before any coordinator provider call. Each refreshes the
owner base, reads local rules and the complete portable execution/custody
protocol, freezes current task inputs and reserves bounded spend before dispatch.
Central presence-only status/check confirms TypeSafe configured and custody
permissions valid; this is not callability evidence. Prefer owner access, inject
only one temporary TypeSafe key if absent and remove it at finish. No new
credentials/account changes, private payloads, commits, pushes, defaults or
rollout selected. Outcomes and spend pending owner receipts.

## Completed owner outcomes — 2026-10-14

**Retain Gemini in Echo Forge and native Luna Decisions in Storybook.** Jev1.14
is genuinely much faster in these fresh paired screens, but neither owner meets
the predeclared no-worse quality requirement. A newer model is not necessarily a
better router for these tasks. No runtime default, rollout, commit or push changed.

| Owner / finite task | Fresh paired quality | Candidate vs incumbent subject cost / p95 | Action |
| --- | --- | --- | --- |
| Echo current-input control intent,42 unique synthetic cases | Jev34/42exact vsGemini39/42; recall18/19tie; falsecontrols4/20vs1/20; ambiguityabstention0/3vs2/3 | USD.001101366 /211ms vsUSD.030341250 /5727ms | Retain Gemini; speed does not offset false controls or ambiguity overcommitment. |
| Storybook deployed mode decision,24 unique reviewed synthetic cases,1pass | Jev21/24 vsLuna23/24; effectiveaccepted10/10vs12/12; dangerousconfidentnoop0both; explicitconfirmation6/8vs7/8; fallback20vs19 | USD.001420776 /147.945ms vsUSD.001940300 /233.535ms | Retain Luna;37%p95 improvement but worse raw modes/clarification and more interpreter requests. Fixed second pass not admitted. |

Costs in the table are decision-subject cohorts, not total workflow costs.
Echo candidate p95 improves96.3%; Storybook36.65%; neither licenses inferred
end-to-end latency or full-cascade economics. Storybook's measured component
cost saving26.78% is below30%soft cost target, though latency passes. Its broader
8/8review-not-suppressed proxy is distinct from explicitconfirm6/8vs7/8.
No full interpreter, paid judge, actual operation, database mutation or live
traffic was exercised. Exposed synthetic small samples are not unseen promotion.
No supported runtime-observable mixed-model subset was qualified; successful
case IDs or self-confidence cannot supply a new safe routing rule.

Configuration: exact native`jev-1.14.0`, default computation, one Choice;
Gemini exact`gemini-3.8-flash` low2048; Luna exact native Decisions`gpt-6-luna`,
default. No within-task effort comparison, alternative Jev effort, old1.13
subject, images or longcontext. Neither selected Jev/Luna typed contract offers
selectable effort; a higher-effort rescue arm is not available.

### Provenance, costs and owner verdicts

| Owner worktree / branch | Exact fetched origin base | KnownUSD | Unknown maxUSD | HardcapUSD |
| --- | --- | ---: | ---: | ---: |
| `/Users/cam/.codex/worktrees/jev114-control-echo-20261014` / `codex/jev114-control-20261014` | `1dc25e4674805436dac5bf217194eb619d94c3ee` | .035093364 | 0 | 1 |
| `/Users/cam/.codex/worktrees/storybook-scout095-jev114` / `codex/scout095-jev114` | `2b6ee0464a1728554b272a70efd9a3217e602b75` | .003644786 | .002400000 | .50 |

**Campaign knownUSD.038738150; unknownUSD.002400000; conservative
exposureUSD.041138150 ofUSD1.50.** Usage-priced accounting, not provider invoice
settlement or agent orchestration spend. No cap transfers or increases.

Echo90/90valid attempts:84semantic plus6qualification, no retries/unknowns;
qualificationUSD.003650748, subjectsUSD.031442616. Story55POSTattempts:
48semantic valid firstattempt,6valid qualifications and1initial Luna1800ms
qualification timeout followed by bounded recovery. Timeout remains unknown
reservedUSD.0024; no successful retry erases it. Known qualificationUSD.000283710,
subjectsUSD.003361076. Jev has no observed transport failures in these samples;
population reliability/concurrency remain unmeasured.

Layered verdicts: candidate access available, exact native task transports
qualified in both owners; bounded reliability measured as above; task capability
worse versus each fresh incumbent on frozen quality; economics cheaper/faster
at decision stage; **do not adopt for either tested task**. Current choices stay.

Owner evidence:
- [Echo attempt](/Users/cam/.codex/worktrees/jev114-control-echo-20261014/docs/evals/attempts/control-intent-v1/20261014-typesafe-jev114.md),
  [manifest](/Users/cam/.codex/worktrees/jev114-control-echo-20261014/docs/evals/attempts/control-intent-v1/20261014-typesafe-jev114.manifest.json),
  [frozen preflight](/Users/cam/.codex/worktrees/jev114-control-echo-20261014/docs/evals/attempts/control-intent-v1/20261014-typesafe-jev114-preflight.json).
  Protected raw/source/ledger root `/Users/cam/.local/share/echo-forge-evals/jev114-control-20261014`.
- [Storybook Attempt183](/Users/cam/.codex/worktrees/storybook-scout095-jev114/docs/evals/attempts/183-story150-jev114-finite-mode.md),
  [summary](/Users/cam/.codex/worktrees/storybook-scout095-jev114/docs/evals/artifacts/story150-jev114-20261014/summary.json),
  [manifest](/Users/cam/.codex/worktrees/storybook-scout095-jev114/docs/evals/artifacts/story150-jev114-20261014/manifest.json),
  [ledger](/Users/cam/.codex/worktrees/storybook-scout095-jev114/docs/evals/artifacts/story150-jev114-20261014/ledger.json).

Only authored synthetic payloads sent under disclosed ordinary retention.
Each owner temporarily received one selected TypeSafe credential through the
custody helper because owner TypeSafe was absent; both injected variables removed
and absence verified. Existing Gemini/OpenAI credentials retained through normal
owner wrappers. No whole vault or private material copied.

Root independently reviewed both rendered native adapters/current runtime
contracts, all Storybook union-error source/golds and Echo differing predictions.
Wrong-case labels remain source-supported; no scorer/gold changes. Independent
verification checked193Echo protected raw/source hashes, Storybook executed-source
hashes and55-row ledger, quality/cost and aggregate cap arithmetic. Owner replay,
and final71-file Storybook artifact inventory verified independently. Echo7focused
and5existing runtime-boundary checks, Storybook73router/operationguard checks,
focused lint/syntax, privacy where applicable, methodology and whitespace pass.
Storybook leading-comment-only lint hygiene preserves paid source hashes/snapshots
and verifies unchanged executable lines. Both temporary dependency link sets
removed; owner primary dirty states preserved. Detailed commands and scope are
recorded in the linked attempts. Coordinator local links/whitespace/arithmetic pass.
No product suites/paid reruns required for coordinator documentation closeout.

Practical result: this recheck prevents trading control and clarification quality
for faster inexpensive labels. Recommended next action is to keep both existing
callers; no further unchanged paid Jev sweep is justified. A material new
checkpoint or separately source-backed contract/configuration can reopen a lane.


## Authorized check-in and push — 2026-10-14

Cam requested “thanks,. check in and push”, authorizing scoped closeout across
Conductor and both linked owner worktrees. All three repositories cleared
completion, scope, validation, remote-base and branch-protection preflight before
the first push. No paid evaluations, runtime defaults or deployments selected.

Owner branches and remote main independently verified at:

- Echo Forge: [`832cd20`](https://github.com/copperdogma/echo-forge/commit/832cd20ffbfe27565819d7f87f3c1964f39053aa),
 11scoped files, normal fast-forward from evaluation base.
- Storybook: [`ab63f223`](https://github.com/copperdogma/storybook/commit/ab63f223e4da5273e7dba270f144584c33377853),
 81scoped files, normal fast-forward from evaluation base.

[Landing receipt](evidence/scout095-landing.json) preserves exact commits, refs,
validation reuse and fresh record checks. Owner evidence landed before this
supervisor completion record. Conductor extracts only Jev095 additions from its
shared dirty checkout onto a fresh current-base worktree; earlier unrelated
ledger, inbox, scout, skill and project work remains untouched. Historical
pre-closeout “uncommitted/no landing” statements above preserve their dated scope.

Conductor methodology/lint, scoped local links, credential-pattern, accounting and
whitespace checks pass. Owner executable/fixture/runtime/lock inputs unchanged:
reuse applicable7+5Echo and73Storybook checks, with final artifact/cost/inventory
replay and changed record checks refreshed. No generic product-suite or provider
rerun. Scoped changelogs, registries, worklogs and generated records included.
Completed owner stories071/191 retain their status; no unrelated story closed.

Temporary keys/dependency links already removed; worktrees and branches retained.
Learning review: no-candidate, because the component-quality versus complete-task
distinction is already required by the existing evaluation skill. No live
workflow, memories or target defaults changed as a side effect of closeout.
