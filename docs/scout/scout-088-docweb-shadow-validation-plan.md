# Scout 088 — Doc Web independent shadow-validation plan

Date: 2026-10-06
Status: Complete — safety stop after first document; do not promote frozen workflow
Owner: Doc Web; Conductor coordinates only
Cam approved execution with `yes` after the completed plan handoff. Hard inclusive cap USD4; synthetic only. Initial preparation spend: zero. Approval does not activate runtime defaults.

## Decision and expected benefit

Determine whether native `pplx-decider-v1.1-27b` merits an opt-in advisory
classification sidecar on Doc Web's real consistency-planning path. Do not
replace convention generation, repair planning, source-aware extraction or
runtime defaults. A sidecar is useful only if it finds actionable supported
misses or reduces a measured later task without introducing unsafe acceptance.
Cheap classification alone does not justify maintaining another provider.

Attempt064 matched aggregate75% accuracy with94.18% lower classification-cascade
cost and31.85% lower p95 against the narrow GPT projection, but confidently
accepted missing-evidence maintenance09. Those20 exposed cases across2sources
cannot establish independent quality or full-planner savings.

## Verified owner substrate

Read-only primary and campaign worktree both have base
`19b30b1d0db4a7f3b2e31614ba9846dfdb93355c` at planning time. Re-resolve current
remote base before implementation; preserve the completed campaign artifacts.
Owner context: Ideal, methodology state `document_structure_and_consistency`,
graph, Story233/234 and registry `jev-document-consistency-classification`.

- `modules/validate/plan_onward_document_consistency_v1/main.py` builds the
  dossier, calls the full planner, normalizes outputs and writes canonical
  `pattern_inventory`, `consistency_plan`, `conformance_report` and primary report.
- Its existing `jev_shadow.py` runs afterward, using compact extracted evidence
  and the planner's conventions. It is advisory only, default-off, max3requests,
  16KiB state,2s caller deadline, `.8` confidence, explicit uncertainty review,
  conflicting-policy skip and deterministic layout guard. It preserves planner
  uncertainty and otherwise falls back to the already-computed planner verdict.
- Story220 recipes configure `gpt-4.1`; the older Story144 recipe configures
  `gpt-5`. Pin the actual selected full-planner ID/settings in the run manifest;
  do not accidentally select the historical recipe as the incumbent.
- Story234 recorded an ambiguous case lost during compaction and later exposed
  convention contradictions. Existing recheck artifacts and evidence-contract
  tests cover these failure classes; they are regression diagnostics, not new
  held-out evidence.

The full planner is required upstream of this shadow. Its cost cannot be
subtracted as avoided fallback. Any future classifier-first design would need
a separate validated source of conventions and a separately approved comparison.

## 1. Recommended bounded re-evaluation

Execute one Doc Web owner campaign, hard inclusive **USD4 maximum**, synthetic
text/HTML only. This is a re-evaluation prompted by Attempt064's uncertainty
failure and the untested runtime evidence/convention seam, not another run of
the unchanged projection benchmark. No Jev/OpenAI Decisions tournament.

### A. Offline contract and source coverage first

Create a dedicated current-base `codex/` worktree; carry only the necessary
nonsecret adapter/evidence work from the completed campaign, recording hashes.
Create the owner story/eval entry before implementation. Reuse the native
Decisions adapter, but keep the new sidecar separate from existing Jev activation
and credentials. Use a distinct default-off eval switch and distinct run IDs.

Build6new synthetic genealogy documents,3chapters each:18new chapter cases.
Balance3cases each of conformant, format-only, row-semantic, mixed, missing
source evidence, and ambiguous attachment; the latter two map to `uncertain`.
Distribute cases across documents; include legitimate convention variations so
memorized seven-column heuristics are insufficient. No equipment-card claim
on a genealogy-specific runtime. Hand-authored convention oracle stays in the
reviewer/scorer files; the full planner must infer conventions normally.

Independently review source/gold/conventions before freezing. Use a bounded
read-only reviewer with no provider answers available; owner/root resolves
source-backed disagreements. Freeze source HTML, page/chapter JSONL, golds,
strata, recipe, prompts, adapters, thresholds and scorer hashes before calls.
Do not count authored mutations as18independent source documents.

Trace every chapter through `driver.py` to its dossier and compact shadow state.
Assert critical evidence survives: dates/notes availability, attribution,
headers, permitted variants, page-break context and source completeness.
Exercise existing Story234 regression cases separately using saved/mocked
responses. No dropped chapter may disappear from the denominator. Unavailable
or unsupported context yields a recorded skip/review, never confident clean.
Do not inject gold labels or oracle conventions into candidate state.

Replay mocked native envelopes through the real driver and schemas. Confirm
shadow disabled makes zero calls; enabled writes a separate sidecar; timeout,
malformed response, missing key, conflict, input limit and run limit fail safely.
Compare canonical artifact hashes for identical planner responses with shadow
on/off. Shadow output must never feed repair or overwrite authoritative files.
This is the small local applicability test for the proposed design; it remains
execution work, not evidence already obtained by this planning task.

Stop before spending if source visibility, convention consistency, privacy,
isolation, reservation feasibility or stamped artifact integrity fails.

### B. Fresh paired runtime shadow observation

Run each of6documents twice through a minimal real driver recipe loading the
synthetic extraction artifacts and invoking the actual full planner. Maximum
12full-planner calls and36chapter-level Decider calls, plus at most2native
qualification calls. Both arms see the same actual dossier/evidence; the
candidate sees only its permitted compact state and generated conventions.
No cached full-planner response for the live measured cohort. Driver runs
preserve real planning latency, schemas and provenance. Repair is not executed.

Report four outputs separately: raw full-planner result, normalized authoritative
result, raw Decider label/confidence, and guarded advisory result. Reuse existing
uncertainty/layout/conflict safeguards; freeze any necessary evidence-completeness
checks before inference. Do not tune `.8` against these outputs. Diagnostic
risk-versus-coverage plots at other thresholds may be reported but cannot select
an adoption threshold from this same holdout.

Screen the first2documents, then continue only if guards prevent all unsafe
acceptances and state fidelity holds. A valid raw semantic miss remains recorded;
a guarded confident-clean on a true defect/unknown stops promotion and further
paid expansion. Transport failures are infrastructure evidence, not wrong labels.
At most one retry per transient operational failure within the global ledger;
no semantic retries. Failed delivery retains its worst-case reservation.

### C. Predeclared verdict gates

| Gate | Required evidence |
| --- | --- |
| Contract | Exact requested/reported native ID, complete validated envelope/usage, frozen native question semantics; alias echo is not an immutable weight hash. |
| Source and policy | All18chapters accounted for at every stage; no gold leakage; contradictions and unavailable context recorded; no missing-evidence case silently accepted. |
| Safety | Zero guarded false-clean answers on confirmed defects or either uncertainty stratum; retain planner uncertainty; no authoritative mutation. Report raw misses even when guards catch them. |
| Utility | Compare paired source-backed corrections and regressions, per-stratum accuracy, accepted accuracy/coverage, review burden and extra calls. Require at least one independently confirmed useful correction with no unsafe acceptance before proposing any further advisory trial. |
| Economics | Report incremental sidecar cost, full-planner cost, all-in driver cost/p95 and review burden. Full planner remains required, so this shadow adds cost; do not claim the projection's94% savings transfers to this workflow. |
| Handoff | Inspect sidecar plus canonical artifacts and source examples; reconcile receipts/unknowns; remove injected key; return separate access, reliability, quality, economics and adoption verdicts. |

A small synthetic pass permits at most a recommendation for a scoped opt-in
trial. It does not prove broad reliability, privacy eligibility or production
benefit. If no useful correction appears, stop and retain the existing planner;
do not broaden merely because budget remains.

## Spend reservation and privacy

Proposed campaign maximum USD4 includes qualification, retries and unknown
liability. Before approval execution, refresh official native prices and reserve
per request using the serialized input upper bound and full output allowance.
Planning feasibility at the recorded GPT4.1 rates USD2/M input and USD8/M output:
12planner calls each bounded at64,000input tokens +8,000output tokens reserve
USD2.304;36Decider calls bounded at64,000input tokens atUSD.02/M reserveUSD.04608.
Qualification and an explicit recovery pool fit within the remainingUSD1.64992.
Enforce both request-count and dollar gates before dispatch. If any real input
or documented price cannot fit, stop before calling; do not silently truncate,
change model, lower the output contract or increase the cap. Any hidden owner
retry model must be disabled or included in the same explicit reservation.

Only newly authored synthetic HTML/JSONL goes to Perplexity. Decisions retention/
training posture remains unresolved; no family records, scanned private pages,
account changes or production traffic. Use the safe central helper to inject
only `DOC_WEB_PERPLEXITY_API_KEY` into the isolated ignored env when needed;
prefer existing owner OpenAI access, retain its custody. Remove temporary
candidate key on all exits. No secrets in logs, hashes or artifacts.

## Deliverables and proportional validation

Owner story, eval-registry attempt, frozen reviewed corpus, exact executable
command/recipe, preflight reservation ledger, safe requests/raw envelopes,
source-to-dossier-to-state lineage, canonical artifact invariance proof, paired
metrics, per-case adjudication, latency/cost decomposition and final manifest.
Run focused shadow/evidence-contract/planner/schema tests and the real synthetic
driver path; inspect resulting artifacts manually. Preserve old20case evidence
and report it separately from the new cohort. No defaults, deployment, commits,
pushes or private-data trial included.

## Bounded research and remaining uncertainty

Problem class: evaluation/serving mismatch plus selective classification under
missing evidence. Adopt the existing owner shadow pattern and log exact runtime
features, following [Google's Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml)
on serving-feature fidelity. Measure error together with abstention coverage,
following [Selective Classification via One-Sided Prediction](https://proceedings.mlr.press/v130/gangrade21a.html).
These establish evaluation methods, not Decider quality guarantees.

Local inspection confirms the upstream planner dependency, guard paths, max3
chapter bound and opt-in sidecar. Offline driver testing is the next local
experiment. Unknowns: held-out utility, compaction coverage, generated-policy
quality, whole-path latency/cost, and whether any safely separable call could
later be avoided. None are resolved by Attempt064's component economics.

Reply `yes` to execute item1 in an isolated Doc Web worktree, synthetic only,
with a hard inclusive USD4 ceiling. Execution approval does not activate it.


## Execution log

- 2026-10-06: Cam selected item1. Assigned isolated Doc Web owner execution; root independently reviews frozen source/gold and reservation before paid dispatch. Central Perplexity key presence/check passed by provider name only; no owner copy yet. Current primary is clean at19b30b1; owner will refresh remote base.

- Execution worktree: `/Users/cam/.codex/worktrees/pplx-docweb-shadow-20261006`, branch `codex/pplx-docweb-shadow-20261006`, fresh remote base `19b30b1d0db4a7f3b2e31614ba9846dfdb93355c`.
- Current official prices rechecked: [Perplexity pricing](https://docs.perplexity.ai/docs/getting-started/pricing) USD.02/M input, free output/no fee; [GPT4.1](https://developers.openai.com/api/docs/models/gpt-4.1) USD2/M input, USD8/M output, USD.50/M cached input. Native response model echo does not establish hosted weight hash.
- Offline owner inspection found the normal compact evidence path drops ordinary values/source prose and page-break context. Owner is preparing a distinct default-off eval evidence path retaining actual observed source/extraction content and availability metadata. This declared configuration tests proposed integration, not unchanged runtime parity. Ordinary runtime must remain equivalent with the eval switch off. Root review/freeze remains pending; no provider calls yet.

- Root independently reviewed all18source/extractionpairs and confirmed golds before provider outputs; review lives in owner `benchmarks/pplx-shadow/root-source-review.json`.
- Root blocked initial offline preflight after direct rendered payload inspection found all18source contexts empty. Required `page` field was absent from synthetic PageHtml rows; driver stamping silently excluded them. Owner preserved invalid preflight as zero-spend harness evidence, repaired schema metadata directly from unchanged reviewed sourceHTML, and strengthened stage-by-stage assertions. Root verified15valid supplied pages/3intentionally missing, byte-identical source content, preserved attributes and real pagebreak, and candidate-state fidelity.
- Final offline canonical hash equality holds with shadow off/on/timeout/malformed;44focused tests passed. Root verified70frozen source hashes, manifest SHA256 `3d35768999163f35edd8349f95f5d58cbedc4000251183629376b85b2aa95f2c`, reservationUSD2.54336/headroomUSD1.45664. Temporary candidate key injected through custody helper into ignored owner env. Paid qualification/progressive screen released under originalUSD4 cap; no runtime activation.


## Runtime screen outcome

The approved early-stop gate fired after doc01, before doc02 or the second
repeat. No extra calls are justified by cap headroom. Exact native access and
transport qualified;5completecalls (2qualification,1fullplanner,2candidate),
usage-priced USD0.02588316, unknownUSD0 of hardUSD4. Ten exact request/response
receipt hashes independently verified by root. No paid judges/retries/errors.

| Chapter | Gold | Full planner | Raw Decider | Final guarded path |
| --- | --- | --- | --- | --- |
| doc01/ch1 | conformant | conformant | conformant,confidence.99606 | accepted conformant |
| doc01/ch2 | format_drift | format_drift | not called: conflicting generated conventions | planner fallback format_drift |
| doc01/ch3 | row_semantic_issue | conformant | row_semantic_issue,confidence.42031 | low-confidence fallback conformant; unsafe inherited miss |

Root independently rechecked source1876 versus extracted1881 birth year, both
present in the actual full-planner prompt and candidate state. Native Decider
correctly selected row_semantic_issue; probability.53625 is distinct from
confidence.42031. The frozen `.8` rule rejected it and retained the planner's
incorrect clean result. This is evidence against the proposed combined routing
policy, not a demonstrated Decider semantic failure or newly introduced error.
The ch2 planner convention contradiction prevented a valid candidate judgment;
do not count that skip as a candidate miss.

Raw candidate2/2correct conditional on valid responses; final workflow2/3correct.
Only1/3chapter outcomes used an accepted candidate decision. No useful accepted
correction;1inherited finalfalseclean,0newlyintroducedfalsecleans. Tiny screen,
not independent cohort superiority: remaining15unique cases and all second
repeats are unmeasured. Missing-evidence and ambiguous strata have offline
coverage only. Stop promotion of this frozen workflow; keep current defaults.
Whole-path economics add a sidecar to a required planner; projection savings
remain inapplicable. Inspect owner report for observed timings/decomposition.

Root removed the sole temporarily injected DOC_WEB_PERPLEXITY_API_KEY via the
custody helper and independently verified absence by variable name. Existing
owner OpenAI custody unchanged. All changes remain isolated and uncommitted.

Smallest useful follow-up: offline-only review of preserving low-confidence
candidate/planner disagreements as explicit review warnings. Do not lower `.8`
on this exposed screen or promote a new routing rule without separate evidence.


## Final owner closeout

[Attempt065](/Users/cam/.codex/worktrees/pplx-docweb-shadow-20261006/docs/evals/attempts/065-perplexity-runtime-shadow.md),
[owner report](/Users/cam/.codex/worktrees/pplx-docweb-shadow-20261006/docs/evals/evidence/065-pplx-shadow/report.md),
[final manifest](/Users/cam/.codex/worktrees/pplx-docweb-shadow-20261006/docs/evals/evidence/065-pplx-shadow/final-manifest.json).
Story246 closed under the declared early-stop evaluation contract; no adoption
or landing.55focused tests, scoped Ruff, methodology build/check and whitespace
pass. Offline replay verifies70frozen sources,10native receipts,2guard replays
and exactcanonical hashes with zero network. Final manifest188entries verified,
SHA256 `a6d369a974a4b5b237d9aebdde50ef0b4d94b339f757ea480371cdaea8e33e31`.

FullplannerUSD.025706, sidecarUSD.00007228 (+.28118%), qualificationUSD.00010488.
Observed driver11.186s/fullplanner8.065s/candidate474and457ms. One document
cannot establish stable p95 or product benefit. No source-private uploads,
defaults, deployment, repairs, commits or pushes. Primary checkout untouched.


## Approved offline routing follow-up — complete

Cam selected an offline-only test after the safety stop. New isolated owner
worktree `/Users/cam/.codex/worktrees/pplx-disagreement-offline-20261006`, branch
`codex/pplx-disagreement-offline-20261006`, base19b30b1. Original paid campaign
and its188entrymanifest unchanged;22nonsecret saved evidencefiles copied with
source/hash/size custody. No env or credentials copied. Network blocked during
replay;0providercalls/USD0newspend.

[Attempt066 owner report](/Users/cam/.codex/worktrees/pplx-disagreement-offline-20261006/docs/evals/evidence/066-offline-disagreement/report.md):
valid low-confidence candidate/planner disagreement at unchanged.8threshold
becomes advisoryreview/uncertain with both labels/confidence preserved. On saved
3chapters/1document: falseclean1→0, review0→1, determinateoutputs3→2; exactfive-way
labels2/3unchanged, candidateaccepted1/3unchanged. No new semantic correction.
Existing agreement/threshold/failure/skip/review paths unchanged; authoritative
verdict untouched. Only the pure offline policy is implemented, not runtime.

16boundarytests, scopedRuff, methodologycompile/check and whitespace pass.
Tenreceipthashes/2exactnativecandidate replays/4canonicalhashes verified;
final33entrymanifest verified. Story247 closed for offline experiment only.
This is post-hoc exploratory evidence on exposed outputs; remaining15unique
chapters and allsecondrepeats still unmeasured. Highconfidence mistakes,
missingresponses and contradictory conventions remain separate risks.

Recommended next step: integrate the warning rule solely into the default-off
experimental sidecar with offline regression proof. Fresh held-out evaluation
remains necessary before adoption; no new spending, defaults, commits or pushes
are authorized by this offline test.


## Approved experimental warning integration — complete

Cam selected integration into the default-off experimental sidecar with offline
regressions. New isolated worktree `/Users/cam/.codex/worktrees/pplx-warning-integration-20261006`,
branch `codex/pplx-warning-integration-20261006`, base19b30b1. Necessary nonsecret
experimental substrate carried; original Attempt065/066 artifacts and manifests
preserved. No credentials/.env or providercalls/newspend.

[Attempt067 report](/Users/cam/.codex/worktrees/pplx-warning-integration-20261006/docs/evals/evidence/067-warning-integration/report.md):
valid native low-confidence disagreement now emits advisoryreview/uncertain plus
both labels/confidence in warning. Authoritative label retained; same-label
fallback and existing guard precedence unchanged, threshold stays.8. This is
integration only, no fresh modelquality/calibration/adoption claim. The original
full-planner dependency and private-data eligibility restrictions remain.

62focusedtests, scopedRuff, methodologybuild/check and whitespace pass. Saved
replay verifies10native receipts/2exactanswers/4priorcanonicalhashes; realdriver
mocked sidecaron/off emits warning with all4canonicalhashes identical. Durable
artifacts `docs/evals/evidence/067-warning-integration/driver-artifacts/` inspected.
Final99entrymanifest verified, SHA256
`2585c0317d05057005b360866f20c85c96a693a0c93a319b9352e8f57efe3f72`.
Story248 closed. Default-off switches remain unset, primary untouched; no
activation, deployment, commits or pushes. Fresh held-out safety/utility evidence
is the next adoption prerequisite; no further spending approved by integration.


## Campaign close-out decision — 2026-10-06

Stop the campaign and retain current model choices. The completed comparisons
do not demonstrate a reason to adopt Perplexity Decider in any evaluated lane.
Doc Web's follow-up identified a fallback-policy problem and verified an
advisory warning in the experimental sidecar using saved responses and mocked
driver runs; it does not establish fresh model quality or whole-pipeline savings.
The experimental sidecar remains disabled. No further paid evaluation is planned.

Cam authorized scoped check-in and push of the four owner records and Conductor
summary, including the disabled Doc Web experimental integration. Historical
no-commit/no-landing statements above describe their original milestones.
Final remote landing identities are recorded below after owner verification.
