# Scout 084 — Mistral Large 4 evaluation routing

Date: 2026-10-06 (America/Edmonton)
Status: Complete — all five selected owners evaluated, reviewed and landed; retain existing models

## Access and identity

The central presence-only helper reports OpenRouter configured and direct
Mistral absent. No target credential was inspected or used. Existing access
infrastructure makes OpenRouter the first route to qualify, without a new
account. **Access: unverified** until selected owner inference succeeds.

Sources checked publicly today:

- [Creator card](https://docs.mistral.ai/models/mistral-large-4-0): public preview,
  October 6, direct `mistral-large-4`, 1M context, structured outputs and tools.
- [Router card](https://openrouter.ai/mistralai/mistral-large-4-0) and
  [exact public endpoints](https://openrouter.ai/api/v1/models/mistralai/mistral-large-4-0/endpoints):
  `mistralai/mistral-large-4-0`; endpoint names include dated `20261006`.
- [OpenRouter ZDR](https://openrouter.ai/blog/insights/zero-data-retention/):
  request-level `provider.zdr` enforcement is distinct from account policy.
- [Existing launch research](/Users/cam/Documents/Projects/conductor/docs/model-watch/daily/2026-10-06.md).

Public endpoint GET returned three Mistral routes: default, `mistral/zdr`,
and `mistral/eu`. Default/ZDR posted USD0.68 input, 0.07 cache read and 2.09
output per million tokens; EU 0.748/0.077/2.299. Creator card crosses out
1.36/0.14/4.18 base prices. Promotion duration unknown; do not assume permanent
prices. Proposed caps below use current default/ZDR rates with an enforced
price boundary and full-call reservation before dispatch.

Router context is 524288 and maximum output 262144, distinct from creator's
1M context. Text/image input and text output; no native audio/video established.
Metadata advertises `structured_outputs`, `response_format`, tools, and required
and named function choice. This is not exact owner schema-enforcement proof.
No reasoning control appears in current endpoint parameters; do not send an
unsupported effort or invent parity between reasoning settings across providers.
Requested/served exact identity and dated route must be recorded; aliases and
immutable served checkpoint equivalence remain unverified.

ZDR-tag availability is public routing evidence, not proof of our account's
eligibility or a blanket private-data authorization. Only owner-established
public/synthetic inputs below are proposed. Default route retention/training
posture is unverified; use the advertised ZDR route if the owner requires it,
and fail closed for private/unclear material. No account changes authorized.

No exact prior attempt matched in the evaluated-model ledger. Large 3 and other
Mistral checkpoints are distinct. This is a new candidate, not an unchanged
retry; recent incumbent successes do not themselves disqualify it.

## Portfolio and stable execution handles

All eleven registered owners were inspected read-only with lower-cost delegated
review. Recent owner worktree records supplement older primary registry rows;
they do not prove landing or current defaults. Coordinator rejected stale
generic extraction suggestions and retained maintained task-specific lanes.
Current owner base, prompt/fixture identities and required repairs must be
reconciled in isolated worktrees before execution. No target writes occurred.

1. **Doc Web — Evaluate now; USD11.00.** First `image-crop-extraction`:
   exact image/integer-coordinate contract, Image011 then full13 versus fresh
   Gemini3 Flash. Require13/13 and overall>=0.95 to qualify detector value;
   compare IoU, grouping, text exclusion, latency and task cost. Independently
   test `crop-page-level-deletion-gate` on the current repaired/source-adjudicated
   contract from Attempt048, first neighboring-content differentiator then22
   versus fresh GPT5.5, requiring22/22 and zero false-safe. Preserve original
   frozen and source-adjudicated scoring separately; do not revive the older
   contradictory prompt or claim a pass removes source review/C5. Independent
   `handwritten-notes-transcription` uses public LOC Barney/Alverson pages and
   fresh Gemini3.7, target>=0.99 per page. Verify source-valid OCR golds before
   dispatch, retaining prior wording concerns; a disputed scorer is an eval
   defect, not a model miss. OCR/safety remain independent if detector stops.
   Eligible public benchmark images only, no private scans. Bound candidate
   input26K per detector/OCR,46K per safety; output4096 detector/safety and16384
   OCR. At posted candidate rates, full subjects reserve approximately0.341,
   0.877 and0.104; fresh controls0.329,6.412 and0.162, total8.23. Remaining2.77
   covers qualification/recovery; deterministic scoring, no paid judge. A
   visual grounding gain could reduce manual crop cleanup; safety must be
   qualified separately. End-to-end stage share and savings remain unknown.
2. **CineForge — Evaluate now; USD3.00.** `video-understanding` v4, six
   synthetic cases with five ordered JPEGs, fresh GPT6 Luna low control.
   Qualify all five images and actual schema, then first case and full6 if
   admitted. Target overall>=0.80, <=15s and<=USD0.02 per subject. Luna's prior
   0.621792 leaves measured sequence-understanding headroom. This is a headless
   research reference, not a shipped analyzer replacement. Freeze Opus4.6
   cross-provider judge and source-first adjudication, reuse saved answers for
   judge repairs. Six106K-input/4096-output candidate reservations total0.484;
   control<=0.10, judge allowance1.10, remaining1.316 qualification/recovery.
   Synthetic owned frames only; ordered images do not prove native video/audio.
3. **Dossier — Evaluate now; USD5.00.** `standalone-semantic-value`, two
   synthetic namesakes snapshots with the same authored reference histories,
   fresh GPT6 Astra medium comparison. Qualify strict SemanticGraph/compiler
   contract then full source-meaning acceptance, including familiar-name
   preservation. Stop material omission, unsupported assertion or contract
   failure; compiler acceptance alone is insufficient. Independent Opus4.6
   source-first reviews for both arms. Astra subject bound2.4003 plus four
   review bounds0.39992 each leave1.00002 for candidate subjects/qualification/
   recovery. Candidate4K output and bounded short synthetic request easily
   fit that residual at posted rates; actual serialized bounds must be frozen
   before spending. This asks whether an inexpensive new checkpoint preserves
   difficult meaning; it does not repeat an old Mistral identity or prove
   broader adoption. Broader families, long narratives, scale and private data
   omitted from this small comparison.
4. **Storybook — Evaluate now; USD1.50.** `luna-persona`,12 synthetic turns
   in seven independent groups, fresh GPT6 Luna none control. Test continuity,
   warmth and Inference Firewall/no-therapy boundaries; require all assertions,
   <=5s and<=USD0.01 per turn. Native plain text, not invented strict schema.
   Start representative boundary cases; stop valid boundary failure. Candidate
   output1024 (plain text; no advertised reasoning setting), control512;
   preserve actual production prompt/grouping. At8K input, candidate full12
   reserves0.0911, control<=0.02;12 paired GPT5 judgments at16K input/4096
   output reserve0.7315, leaving0.6574 for qualification and saved-answer judge
   recovery. Judge shares the control's provider; source-check decisive grades.
   This measures a possible quality/latency tradeoff, not cheaper replacement
   of Luna: prior Luna cost around0.00005/turn is already far lower. Benefits
   are uncertain and this is lower priority than the two visual lanes.
5. **Echo Forge — Evaluate now; USD1.50.** `control-intent-v1`,42 frozen
   source-valid production-input synthetic cases, fresh Gemini3.8 Flash low.
   Strict one-label JSON,2048 total output,15s deadline, independent serial
   calls and deterministic scorer/no paid judge. Qualify positive/negative/
   ambiguous admission slice then full42. Preserve19-control recall and
   compare exactness,20-negative false activations and3 ambiguity cases,
   p50/p95 and cost. Prior matched Gemini39/42 leaves specific headroom.
   Reject recall regression or worse quality/value; aspirational targets alone
   do not erase relative useful gains. At6K input/2048 output, candidate0.3512
   plus control0.5116 reserve0.8628; remaining0.6372 covers qualification and
   recovery. Model judges intent only; deterministic code retains action,
   target, permission and manual review. No routing from post-hoc winning cases.

**Campaign maximum: USD22.00.** Operator caps become hard limits on selection;
no transfers between owners. They are conservative reservation ceilings, not
expected invoices. Reprice subjects/judges and render full matrix before paid
multi-case runs. Public platform output maxima are not eval allowances.
Unknown call exposure retains its reservation. Routine recoverable harness/judge
faults may be repaired within scope/cap; never weaken owner gates.

## Omitted matching tasks and remaining owners

- Doc Web whole-book/table HTML and reference resolution: separate contracts;
  current reference resolution is deterministic/no model call. Crop-only
  validation overlaps selected stronger page-context gate. No native video.
- CineForge ScriptBible/screenplay QA: separate corpus eligibility/scoring
  prerequisites; frames do not cover these. No audio-generation support.
- Storybook photo/OCR: **Defer these tasks** on maintained economics. Prior2325
  input tokens alone implyUSD0.001581 at current candidate input rate, exceeding
  USD0.001/call before output, with only two easy fixtures and no harder eligible
  case established. This tokenization estimate is not a new measured model cost.
  Fusion/linking/correction require their own frozen contract and fixture scope;
  persona cannot qualify them.
- Echo scene-to-soundscape: separate contract/source eligibility; intent results
  cannot qualify extraction. Audio generation mismatches output modalities.
- **Board Game Ingester — Defer.** Representative RoboRally package is
  `private_local_package`; no permitted upload eligibility. Synthetic Tideglass
  tests deterministic package semantics, not representative inference quality.
  Visual crop/orientation/source-role/asset matching need eligible owner fixtures.
- **Financial Hub — Defer.** Private transactional inputs and provider policy;
  no maintained eligible public/synthetic comparison established. No finance data
  leaves the owner and no classifications/rules/runtime changes are authorized.
- **Financial Monthly Analysis — Defer.** Private source reconciliation and
  source-only proposals; no eligible synthetic decision lane established.
- **Robo Rally — Do not evaluate.** Deterministic game rules, state-aware bots
  and replay; no maintained model inference lane. Private rulebook is not an
  eligible substitute.
- **Ultima IV Web — Do not evaluate.** Original-game reconstruction/differential
  testing and controls have no maintained model inference decision.
- **VLC Thumbs — Do not evaluate.** Native sampling/cache/hover/bookmarks have
  no maintained model inference task.

## Owner evidence

Current owner registries/instructions/Ideal/spec are authoritative. Recent
task-specific evidence used to avoid stale primary summaries:

- [Prior full routing and bounds](/Users/cam/Documents/Projects/conductor/docs/scout/scout-078-gpt61-sol-evaluation-routing.md)
- [Current effort and safety repair follow-through](/Users/cam/Documents/Projects/conductor/docs/scout/scout-079-thinking-level-coverage.md)
- [Dossier namesakes](/Users/cam/.codex/worktrees/sonnet55-eval-20260928/dossier/docs/evals/attempts/017-sonnet55-namesakes-fallback.md)
- [Doc Web registry](/Users/cam/Documents/Projects/doc-web/docs/evals/registry.yaml)
- [CineForge registry](/Users/cam/Documents/Projects/cine-forge/docs/evals/registry.yaml)
- [Storybook persona](/Users/cam/.codex/worktrees/sonnet55-eval-20260928/storybook/docs/evals/attempts/174-luna-persona-sonnet55.md)
- [Echo production-input comparison](/Users/cam/.codex/worktrees/gpt61-sol-eval-20260929/echo-forge/docs/evals/attempts/control-intent-v1/20260929-openai-gpt-6-1-sol.md)

Selection is required by evaluate-model Stage1 before provider calls or target
mutation. Selection authorizes only isolated owner evaluation and temporary
OpenRouter eval-key injection/cleanup, not defaults, private data, deployment,
commit or push. No probe occurred; do not enter this recommendation as an
evaluated-model attempt. Documentation-only validation checks claims, bounds,
links and whitespace; product suites are inapplicable.

Reply `yes` to run all five, or `only do 1 and 2` for the strongest initial fit.

## Approved execution — 2026-10-06

Cam replied `yes` to all five. Hard inclusive caps remain Doc Web11,
CineForge3, Dossier5, Storybook1.50 and Echo Forge1.50; totalUSD22.
Five isolated owner workers were dispatched before any coordinator provider
call; the coordinator will review source validity, receipts, accounting and
layered verdicts. Each owner fetches current remote default base and creates
`codex/mistral-large4-eval-20261006` under
`/Users/cam/.codex/worktrees/mistral-large4-eval-20261006/`.
Primary checkouts and unrelated dirt remain untouched. No runtime/default,
private-data, deployment, commit or push authorization.

Coordinator read both portable owner protocol and credential custody fully.
Central presence-only status/check passed. Doc Web and CineForge have existing
owner-managed OpenRouter credentials via their normal wrappers; no copy made.
Dossier needed central OpenRouter injection: ignored worktree `.env`, variable
`OPENROUTER_API_KEY`; helper copied exactly that provider only, cleanup required
at owner closeout. No credential value is recorded. Remaining owner access
and exact provider callability are pending qualification.

Initial bases: Doc Web`fc558e2e924d0d598f31c69ee86fd5255f696f86`,
CineForge`2e148974583e731bedd32e4896b282a94134aeff`,
Dossier`15ac295ea705a9fdd00590b2e5855b34ee05a256`,
Storybook`fedc582e` (full identity in owner evidence),
Echo Forge`95b176e11b7760e7ca2472552a418cd5d413ce27`.
Additional helper injections: Storybook ignored `.env.local` variable
`OPENROUTER_API_KEY`; Echo Forge ignored `.env` variable
`ECHO_FORGE_OPENROUTER_KEY`. Both lacked owner-managed OpenRouter access.
Existing comparator/judge credentials remain owner-managed and are read through
normal owner wrappers, never copied into Conductor or whole-env transferred.
All three injected variables require removal at campaign closeout.

## Owner results — 2026-10-06

**Retain the existing models/processes for all tested tasks.** Exact Large4
access works through OpenRouter and the measured contracts qualified. Lower
cost and occasional faster responses did not compensate for source-faithfulness
losses. Doc Web's detector clears its numerical gate but clips logo content;
this changes the initial promising numerical result into a quality tradeoff,
not a qualified replacement. No further unchanged run is recommended.

Every comparison used fresh subjects and maintained frozen/source-valid inputs.
Small progressive screens are not full-benchmark or production conclusions.
No post-hoc winning subset or confidence-based routing was invented.

| Owner / task | Measured quality and winner | Subject economics / latency | Recommended action |
| --- | --- | --- | --- |
| Doc Web detector,13 paired pages | Both13/13; Large4 score0.957992 vs Gemini3 Flash0.958646. Image011 source review finds Large4 clips the logo's right lettering; Gemini preserves it. Numeric aggregate near-tie is not source-faithfulness equivalence. | Full13 Large4USD0.02739909 vs Gemini0.04639550; mean5.137s vs6.739s. SavingUSD0.01899641/13 pages; approximatelyUSD0.00146/page. Latency descriptive with overlap caveat below. | Retain Gemini. Small absolute saving does not justify cropped-content/manual-review risk or new integration maintenance. |
| Doc Web page safety | Large4 neighboring-portrait screen correct; full source-adjudicated4/5 then false-safe cut seal. Historical frozen labels5/5 preserved separately. Fresh GPT5.5 screen correct then cover0/1 false-reject. Remaining17/21 full rows unmeasured. No qualified full22 winner. | Large4 five full callsUSD0.01883546,mean10.532s; GPT5.5 one full call0.082910,7.372s. Different stopped samples are not a relative economic win. | Reject Large4 safety; retain existing source-review/C5 process. Existing control false-reject is also preserved. |
| Doc Web handwriting | Barney1 paired page: Large4 fidelity0.939957 vs Gemini3.7 0.978830; both below0.99. Large4 source-visible substitutions confirmed. Alverson unmeasured after progressive lane stop; source golden precheck valid. | Large4USD0.00171341/12.896s vs Gemini0.00692625/5.960s. | Retain Gemini; reject Large4 for this fidelity lane. |
| CineForge ordered frames | One paired five-image case: repaired combined0.3492 vs Luna0.72285; both below0.80. Large4 falsely describes complete stillness where figures visibly enlarge. Original combined0.3992/0.70785 retained;5later cases unmeasured. | Scored Large4USD0.00288914/5.047s vs Luna0.00021067/8.018s. Luna scored input cache-warmed by required native qualification; cold native costs0.00297065/0.000565175 respectively. | Reject Large4; Luna wins measured screen, not a full-six or autonomous-QA qualification. |
| Dossier namesakes | One paired current-v5 snapshot: Large4 compiler-valid but asserts placement supervised_by narrator without source support; Astra fully source-accepted. Both second snapshots unmeasured. | Large4USD0.00579429/8.65s vs Astra0.109940/25.79s. | Retain Astra; cheaper graph is not value-eligible under unsupported-assertion gate. |
| Storybook persona | Six grouped paired turns: Large4 5/6 vs Luna6/6. Large4 invents mother's behavior/Marco feelings and omits Friday context; automatic stop before later6turns. | Mean turnUSD0.00049687 vs Luna0.00004950; median1.997s vs1.655s. Large4 max6.427s also misses5s gate. | Retain Luna; reject Large4 persona. |
| Echo Forge control intent | Full42 fresh pairs: Large4 35/42 vs Gemini3.8 40/42; recall17/19 vs19/19, false activations2/20 vs1/20, ambiguity0/3 vs2/3. Source-proven keep/prohibit commands missed. | Full42 Large4USD0.01085586 vs Gemini0.02996625; p50/p95 0.923/3.279s vs2.648/11.475s. Gemini includes44attempts/two recovered15s timeouts. | Retain Gemini; recall losses outweigh faster/cheaper calls. |

Detector's stage share in complete book-processing cost/time remains unknown;
the observed page-call savings are not an end-to-end benefit estimate. A
detector-only split retaining another safety model is identifiable by pipeline
stage, but combined quality/manual-review load was not qualified. Source
clipping plus small absolute savings make that integration unjustified now.
Independent task failures are not a blanket claim about the model's abilities.

### Spend and durable owner evidence

Usage/accounted amounts, not reconciled provider invoices. All fixed caps were
respected without transfer. Subject costs above exclude qualification/judges.

| Owner | KnownUSD | Unknown reservationUSD | Conservative exposureUSD | CapUSD | Evidence |
| --- | ---: | ---: | ---: | ---: | --- |
| Doc Web |0.274576170|0|0.274576170|11|[Attempt061](/Users/cam/.codex/worktrees/mistral-large4-eval-20261006/doc-web/docs/evals/attempts/061-mistral-large4-maintained-evaluation.md), [manifest](/Users/cam/.codex/worktrees/mistral-large4-eval-20261006/doc-web/docs/evals/evidence/061-mistral4-manifest.json) |
| CineForge |0.053050635|0|0.053050635|3|[Attempt048](/Users/cam/.codex/worktrees/mistral-large4-eval-20261006/cine-forge/docs/evals/attempts/048-mistral-large4-v4-first-case-stop.md), [final manifest](/Users/cam/.codex/worktrees/mistral-large4-eval-20261006/cine-forge/docs/evals/story-229-mistral-large4-evidence-v2.json) |
| Dossier |0.276104290|0|0.276104290|5|[Attempt024](/Users/cam/.codex/worktrees/mistral-large4-eval-20261006/dossier/docs/evals/attempts/024-mistral-large4-namesakes-20261006.md), [custody](/Users/cam/.codex/worktrees/mistral-large4-eval-20261006/dossier/docs/evals/artifacts/mistral-large4-namesakes-20261006/custody.json) |
| Storybook |0.076870475|0|0.076870475|1.50|[Attempt177](/Users/cam/.codex/worktrees/mistral-large4-eval-20261006/storybook/docs/evals/attempts/177-luna-persona-mistral-large4.md), [manifest](/Users/cam/.codex/worktrees/mistral-large4-eval-20261006/storybook/docs/evals/artifacts/mistral-large4-persona-20261006/manifest.json) |
| Echo Forge |0.041076780|0.024481500|0.065558280|1.50|[attempt](/Users/cam/.codex/worktrees/mistral-large4-eval-20261006/echo-forge/docs/evals/attempts/control-intent-v1/20261006-openrouter-mistral-large-4.md), [manifest](/Users/cam/.codex/worktrees/mistral-large4-eval-20261006/echo-forge/docs/evals/attempts/control-intent-v1/20261006-openrouter-mistral-large-4.manifest.json) |
| **Total** |**0.721678350**|**0.024481500**|**0.746159850**|**22**|All five selected owners accounted |

The campaign made162 inference attempts:40 Doc Web,8 CineForge,5 Dossier,
22 Storybook and87 Echo Forge.160 returned complete responses; two timed-out
Echo comparator calls retain unknown-charge reservations. Zero-cost catalog,
receipt GETs and a pre-dispatch SDK failure are excluded from inference counts.
Separate judge overhead: CineForge0.046415 (including two saved-answer repairs),
Dossier0.160370 (including one repair), Storybook0.070717250. Doc Web/Echo use
deterministic scorers. No subject was rerun to tune a favorable quality result.

### Layered verdicts, operational limits and validation

Access available and exact canonical model/provider recorded for all five.
Measured native/harness contracts qualified: integer image crops, paired-image
safety, actual image OCR driver, five ordered images/schema, plain-text persona,
strict intent JSON and current-v5 semantic graph. Dossier's eval Chat projection
does not qualify a drop-in production Responses substitution. Served alias
does not prove an immutable snapshot. Default route retention/training remains
unverified; no private fixture or account-policy change occurred.

Preserved defects and recoveries:

- Doc Web accidentally overlapped safety-native and final detector dispatches,
  overwriting one native ledger/numbered request record. A complete parsed
  native envelope survives and supplies identity/usage/cost, but original
  native HTTP request/response bytes and ledger bytes were lost. Reserialized
  parsed envelope and reconstructed request/lost latency are labeled, not
  intact historical proof. Captured production safety screen proves actual strict flags.
  Cross-process lock was repaired and actual two-process dispatch tested.
  Detector latency is descriptive, not controlled concurrency/variance proof.
  OCR control first Python3.14 start lacked Google SDK before dispatchUSD0;
  existing Python3.11 SDK supplied the same actual driver under a new run ID,
  with exact system/user/image parity; runtime-version difference disclosed.
- Dossier optional generation-receipt GET404 caused adapter failure after a
  valid native answer; official nativeusage.cost accounting recovered the saved
  subject, no replacement inference. Initial Opus review misresolved entity IDs;
  saved-answer endpoint-tracing repair detected wrong supervisor relation.
  Even its minor-severity grade cannot waive the hard unsupported-assertion gate.
- CineForge source-unfounded color penalty in original Opus grade was repaired
  symmetrically with saved subjects. Original and repaired grades/costs remain
  distinct; source-growth omission independently governs candidate stop.
- Echo Forge Gemini timeout charges remain conservatively reserved. Full42
  continued after recall failure was established, contrary to the ideal early
  stop; tail evidence is ancillary and does not confer adoption eligibility.
  No hidden retry or retrospective winning subset was introduced.
- Storybook stopped automatically on a valid source-boundary failure; no retries,
  judge faults or later subjects.

Coordinator independently checked Storybook87 artifact hashes/cost22 calls,
Dossier74 custody hashes/5 settled ledger entries, CineForge42 final hashes,
Echo181 protected production hashes and its two decisive request/response
contradictions, and Doc Web132 artifacts plus31MB archive/40unique IDs/cost sum.
Coordinator viewed original first/final CineForge frames, complete Storybook
histories, Dossier source/graph endpoints, Doc Web clipped logo and cut seal.
Source conclusions are independent of automatic grades.

[Coordinator verification](evidence/scout-084-coordinator-verification.json)
records the final owner manifest identities, verified file counts, campaign
accounting, local-link check and temporary-key absence.

Focused owner validation: Storybook6 runner+3 maintained adapter/prompt tests;
Dossier129 semantic/adapter/closed-campaign tests; CineForge72 tests plus v4
builder/registry/manifest checks; Echo9 tests plus replay/lint/methodology.
Doc Web43 focused tests plus changed-source Ruff, methodology and whitespace pass.
Current owner records retain exact commands, full base SHAs and executed source
identities. Unrelated architecture/UI/legacy methodology warnings were not
converted into model failures or broader repair scope.

All three temporary keys removed with helper and absence confirmed by variable
name only: DossierOPENROUTER_API_KEY, StorybookOPENROUTER_API_KEY,
EchoECHO_FORGE_OPENROUTER_KEY. Doc Web/CineForge existing owner keys untouched.
At evaluation completion, primary checkouts were preserved and isolated work
was uncommitted. The subsequently authorized closeout is recorded below.
No model defaults, deployment or private-payload rollout changed.

Retry only for a new exact checkpoint or an evidenced owner-contract/capability
change addressing these source failures, or an explicit fresh reproduction
request. Documentation/route/price metadata alone does not reopen failed
quality lanes. No further unchanged paid work or runtime promotion recommended.

## Authorized closeout — 2026-10-06

Cam requested “check in and push.” All six repositories passed scoped completion,
validation, ownership and integration preflight before any push. Owner evidence
landed first; both remote main and the execution branch were verified at each
commit below. No provider calls were made during closeout.

| Owner | Verified remote main and execution commit |
| --- | --- |
| doc-web | [bb9d7c7accb68bdf309a9c26a98c7447640ff142](https://github.com/copperdogma/doc-web/commit/bb9d7c7accb68bdf309a9c26a98c7447640ff142) |
| cine-forge | [4fce5f32e30eb48b1a5d90e5abeb346fd9daa17f](https://github.com/copperdogma/cine-forge/commit/4fce5f32e30eb48b1a5d90e5abeb346fd9daa17f) |
| dossier | [0f13198b5831fb232b8467d410cb15515716ea20](https://github.com/copperdogma/dossier/commit/0f13198b5831fb232b8467d410cb15515716ea20) |
| storybook | [d8f886c3623d01f99ed75c16d747d82184d43a5d](https://github.com/copperdogma/storybook/commit/d8f886c3623d01f99ed75c16d747d82184d43a5d) |
| echo-forge | [8b01d6d34bb3e4ecbb317ad610490b84851267e1](https://github.com/copperdogma/echo-forge/commit/8b01d6d34bb3e4ecbb317ad610490b84851267e1) |

Conductor carries only this campaign’s report, coordinator verification,
evaluated-model row, candidate follow-through, scout index and inbox capture.
Unrelated dirty primary work was preserved using an isolated integration
worktree. Prior launch/history links point to their retained local records
where those captures have not landed. Owner worktrees and protected local
receipt custody are retained; Dossier and Echo raw files remain local, while
their committed manifests preserve custody identities.

Focused code validation was reused because executed inputs remained unchanged.
Fresh record, manifest, source-custody, methodology and whitespace checks passed.
Doc Web’s 31 MB receipt archive is hash verified; Storybook’s artifact-local
Git attributes preserve original raw response keepalive whitespace. Existing
model choices are unchanged. No further unchanged evaluation is recommended.
