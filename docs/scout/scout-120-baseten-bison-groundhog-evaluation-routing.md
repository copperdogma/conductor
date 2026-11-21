# Scout 120 — Baseten bison-1 and groundhog-1

November 21, 2026, America/Edmonton. Closed with all three incumbents
retained. Cam declined further Bison qualification after the two-repeat result.

The initial proposal found no matching checkpoint or owner attempt in the
evaluated-model ledger.

## API and fixture scope

Baseten announced both checkpoints on November 20. Direct System One uses
`POST https://inference.baseten.co/v1/systemone` with moving selectors
`decision-models/baseten-bison-latest` and
`decision-models/baseten-groundhog-latest`. Baseten documents 131,072 tokens
per question, text/image state, and typed Choice, yes/no and ordinal scores.
The direct Model APIs policy specifies zero retention of customer input/output
and no training on customer content, subject to the stated exceptions.
[Release](https://www.baseten.co/resources/changelog/bison-1-and-groundhog-1-available-on-baseten/),
[security practices](https://www.baseten.co/security-practices).

Propose the OpenRouter Decisions API at `POST /api/alpha/decisions` for all
challenger arms. Its public catalog and endpoints identify the following routes.

| Model | Router ID | Catalog checkpoint | Router context | USD per million input/output tokens |
| --- | --- | --- | ---: | ---: |
| bison-1 | `baseten/bison-1` | `baseten/bison-1-20261120` | 32,768 | 0.10 / 0 |
| groundhog-1 | `baseten/groundhog-1` | `baseten/groundhog-1-20261120` | 16,384 | 0.035 / 0 |

Both list one BaseTen backend. Use the default single-pass native Choice
contract throughout. The routes expose typed probabilities and lack selectable
reasoning effort, generated rationale, tool calls, or coordinate output in the
documented contract. Access remains unverified. The router keeps the same
interface as recent owner comparisons and these fixtures fit its shorter
contexts. Qualify the exact served checkpoint, provider, required choice set,
probability semantics, usage and supported image representation before scoring.
Pin the listed backend and disable fallback to other models/providers.
[Public catalog](https://openrouter.ai/api/v1/models?output_modalities=decisions),
[Bison endpoint](https://openrouter.ai/api/v1/models/baseten/bison-1/endpoints),
[Groundhog endpoint](https://openrouter.ai/api/v1/models/baseten/groundhog-1/endpoints),
[multimodal contract](https://openrouter.ai/docs/guides/community/multimodal-decisions).

Use only the listed owner-authored synthetic cases and the specific licensed
public orientation assets. OpenRouter has opt-in content logging and
improvement settings and safety/legal exceptions. Effective account settings
and exact endpoint retention remain unverified. Apply owner privacy controls
before dispatch. Direct Baseten's published ZDR commitment covers its own
service. [OpenRouter data collection](https://openrouter.ai/docs/guides/privacy/data-collection).

## Evaluate now

Both candidates share one fresh incumbent run per frozen case and repeat.
Evaluate each against the incumbent independently. Freeze criteria, request
semantics, fixture hashes, judging and all independent panels before outputs.
Use deterministic owner scores and independent source review. Report measured
task cost, paired latency and provider failures. Reserve all allowed calls in
each owner before dispatch, count unknown exposure, and stop the affected arm
on an incompatible contract or mandatory safety failure.

| # | Owner and maintained lane | Incumbent and replacement boundary | Evidence and decision | Ceiling |
| --- | --- | --- | --- | ---: |
| 1 | Board Game Ingester, isolated asset orientation | Gemini Decision 1, just the reviewed orthogonal orientation job | Scout 118 and 119 exposed a repeatable wrong automatic keep. Screen both Baseten vision arms for a safe correction, then validate the winner in the reviewed transform/export path. Awaiting selection. | $1.00 |
| 2 | Echo Forge, `control-intent-v1` | Liquid d1.2-ultra, the sole operative playback intent classifier | Incumbent scored 40/42 on the last matched panel with zero false controls. Test improved ambiguity handling or materially faster decisions with the same safety and recall. Awaiting selection. | $0.45 |
| 3 | Dossier, `evals.possible_identity.benchmark` | Native Luna Decisions, the possible-identity question judge selected in ADR-026 | Previous challengers traded away useful-question recall on independent sources. Test whether either Baseten arm preserves recall and reduces false questions. Story 186 remains held. Awaiting selection for synthetic evidence. | $8.00 |

### 1. Board Game Ingester

Use the 14 maintained authored cases and four previously reviewed licensed
public cases with attribution and source hashes preserved. Start with the
source-backed `f24-04` rotation, the difficult Mahjong fixture where present
in the standing panel, and a mandatory hold. Both Microsoft and Gemini chose
automatic keep on `f24-04`, whose source transform requires 90° clockwise.
Neon also missed it. Use the same frozen PNG bytes across arms and preserve
source and derivative hashes. If required by the qualified image route, reuse
the recorded lossless integer enlargement. Retain Gemini's reviewed high-image
setting and pin the Google AI Studio control route used in Scout 118.

Stop an arm for any wrong automatic rotation or missed mandatory hold.
Require all determinate cases correct and a hard-case gain or at least 30%
lower paired p95 including preprocessing at equal quality. Advance qualifying
arms to one eight-case independent authored panel. Validate the normal
reviewed job, exact/native and inverse pixel checks, hold handling and export
before preparing a review patch that retires the superseded job provider path.
Allow up to 30 requests per arm, including qualification and bounded recovery.
Full router contexts at input-only rates reserve US$0.9019392. Disable search
and other separately billed features.
[Microsoft and Gemini owner evidence](scout-118-microsoft-decision-11-evaluation-routing.md#owner-results),
[Neon follow-through](scout-119-gemini4-neon-evaluation-routing.md),
[Google AI Studio endpoint](https://openrouter.ai/api/v1/models/google/gemini-decision-1/endpoints).

### 2. Echo Forge

Use the actual request builder and 42 authored `control-intent-v1` cases.
Start with negation, quotation and prior ambiguous commands. Stop for a false
playback control. Require at least incumbent exact accuracy and operative
recall, zero false controls and improved ambiguity handling or at least 30%
lower paired component p95 at equal quality. Advance qualifying arms to one
12-case independently authored confirmation panel and actual consumer/fault
checks with the single-attempt deadline and manual review. Prepare a
sole-classifier replacement patch for a qualified winner. Up to 60 requests
per arm at full router contexts and confirmed input-only rates reserve
US$0.39616512, including qualification and bounded recovery.
[Scout 118 owner results](scout-118-microsoft-decision-11-evaluation-routing.md#owner-results),
[Liquid endpoint](https://openrouter.ai/api/v1/models/liquid/d1.2-ultra/endpoints).

### 3. Dossier

Qualify the four-choice contract and first use the frozen 36-pair diagnostic.
Stop an arm for an incompatible contract or a decisive source-safety failure.
Run the maintained 1,191 synthetic pairs across three repeats per surviving arm
with the development/340-pair held-out split intact. Fit each threshold on
development only. Use explicit non-reused caching configuration on the Luna
control and check usage for all arms. The candidate's worst repeat must match
the incumbent's best on useful questions and false questions, with a strict
gain on at least one metric. No opposite explicit identity assertion may pass.

If a candidate clears the screen, confirm on up to 120 new, independently
reviewed synthetic pairs with fixed thresholds across three repeats. Include
ordinary cases, explicit source denials and minimal-context namesakes. Require
matched useful-question recall in both strata, fewer false questions, precision
of at least 0.75, at most 0.20 false questions per chapter group, and the
owner's complete-matrix requirement. The result can qualify an eval choice.
Story 186 decisions and approval of a provider for real recipient material
remain prerequisites for a runtime patch. No private data is in scope.

The standing Scout 118 preflight's largest bound was 7,262 tokens. Rebind
exact requests using the owner byte-size-plus-4,096 method and cap each at
8,192 tokens. At most 4,000 calls per arm cover 36 diagnostic calls, 3,573
standing calls, 360 confirmation calls and 31 qualification/recovery slots.
At combined input rates of US$0.235/M this reserves at most US$7.70048.
The owner must enforce aggregate admission and meter usage before continuing.
[Prior independent Dossier decision](scout-118-microsoft-decision-11-evaluation-routing.md#independent-result),
[Luna Decisions pricing](https://developers.openai.com/api/docs/guides/decisions#pricing-and-availability).

**Combined maximum US$9.45.** Stage 1 used public catalog and local read-only
owner checks, with US$0 spend. Before paid dispatch, reverify current owner
bases, provider terms, metering and aggregate admission. Use isolated owning
worktrees under `/Users/cam/.codex/worktrees/baseten-decisions-20261121/`.

## Other registered owners

| Owner | Disposition |
| --- | --- |
| Storybook | Defer. Its relationship-mode benchmark has no working independent capture path for the improvements observed in the last screen. Photo grounding needs generated evidence fields and diarization needs audio input. |
| Doc Web | Defer. Consistency sidecars already have a component leader and need a connected planner/fallback test to show value. Page safety requires source-specific reasons and the crop/table lanes need coordinates or generated cells. |
| CineForge | Defer. Maintained entity, ScriptBible and ordered-frame lanes require generated fields with evidence, and no reviewed finite-choice consumer surfaced. |
| Robo Rally | Do not evaluate. Deterministic rules and simulation oracles cover the maintained decisions. |
| Ultima IV Web | Defer. The maintained licensed-game playthrough evidence uses deterministic outcomes, with no independent finite-choice model benchmark located. |
| Financial Hub / Financial Reporting | Defer. Private category/reconciliation inputs lack an eligible maintained synthetic decision comparison. Inspected the current `financial-reporting` checkout. |
| Financial Monthly Analysis / Financial Data | Defer. Private household categorization and recommendation inputs lack an eligible maintained synthetic decision comparison. Inspected the current `financial-data` checkout. |
| VLC Thumbs | Do not evaluate. The separate `vlc-thumbs` checkout's decode, cache and scheduling contracts are deterministic. |

[Storybook and Doc Web owner evidence](scout-112-gemini-decisions-evaluation-routing.md#current-owner-decisions--2026-11-16).

## Approved execution — November 21, 2026

Cam selected all three lanes for both challengers. The inclusive owner limits
are US$1.00 for Board Game Ingester, US$0.45 for Echo Forge and US$8.00 for
Dossier, for US$9.45 combined. Each isolated owner will enforce its own
admission ledger. Dossier remains synthetic evidence only. Board Game
Ingester and Echo Forge may prepare reviewable replacement patches if their
progressive gates pass. Activation and landing remain outside the selection.

### Board Game Ingester and Echo Forge results

- **Board Game Ingester retains the reviewed Gemini Decision 1 job.** On one
  matched CC0 image, the source required 90° clockwise. Bison requested review
  and missed the determinate-case requirement. Groundhog and Gemini both took
  the wrong automatic keep action. Observed times including preprocessing were
  0.531 s, 0.539 s and 1.191 s, with respective subject costs of US$0.00009160,
  US$0.00003206 and US$0.00014010. One case per arm gives no broad latency or
  reliability estimate. All three exact native Choice responses validated.
  The initial adapter incorrectly equated top-level confidence with the
  chosen option's probability. The owner verified these fields are distinct
  in the public contract and corrected the parser by replaying saved replies.
  The other 17 screening cases, eight confirmations and consumer path were
  gated off. Temporary OpenRouter credential removal and absence of its
  campaign env file were verified. Focused validation passed 21 tests and
  52 subtests, including source and receipt verification.
  [Owner verdict](/Users/cam/.codex/worktrees/baseten-decisions-20261121/boardgame-ingester/benchmarks/results/scout120-baseten-orientation/owner-verdict.json),
  [attempt and replay](/Users/cam/.codex/worktrees/baseten-decisions-20261121/boardgame-ingester/docs/evals/attempts/20261121-scout120-baseten-orientation.md).
- **Echo Forge retains Liquid d1.2-ultra for operative playback intent.**
  Bison scored 5/8 against matched Liquid 6/8 and treated a hypothetical
  adjustment as a command. Groundhog scored 12/15 against matched Liquid
  13/15 and treated a revision of a proposed sound as an instruction to
  manage existing playback. Both incurred one false control versus zero for
  their matched control. Small-slice p95 was 388 versus 430 ms for Bison
  and 358 versus 430 ms for Groundhog. Matched subject costs were
  US$0.000300200 versus US$0.000120078 and US$0.000196595 versus US$0.000223734.
  The control was shared, and actual owner spend includes it once.
  All 38 responses validated. The rest of the 42-case screen, 12 confirmation
  cases and consumer checks were gated off. Offline replay verified all
  receipts, and ten focused server tests passed. The owner used its
  existing process-local OpenRouter access.
  [Owner verdict](/Users/cam/.codex/worktrees/baseten-decisions-20261121/echo-forge/docs/evals/evidence/scout120/owner-verdict.json),
  [attempt and replay](/Users/cam/.codex/worktrees/baseten-decisions-20261121/echo-forge/docs/evals/attempts/control-intent-v1/20261121-scout120-baseten.md).

### Dossier results and resumption

**Retain Luna Decisions for Dossier. The challenger comparison is waiting
for funded OpenRouter access.** Both challengers and native Luna passed exact
default four-choice transport and the 36-pair diagnostic. An initial review
lookup omitted the diagnostic's source ID prefix. Rechecking the saved
answers found no opposite explicit identity assertion on the three intended
source checks. No extra inference was necessary. Groundhog's one `ask` on
an explicitly matched pair remains recorded.

Only Bison and Luna have one complete matched standing repeat. On its 340
held-out pairs, both found 17 of 18 useful questions. Bison raised three false
questions versus Luna's ten, with single-repeat development thresholds of
0.50 and 0.65. Bison's 0.333 false questions per group exceeds the independent
qualification reference of 0.20 on this reused panel. Across the 1,191 matched
pairs, Bison cost US$0.0539348 versus US$0.0542915, with median 317 versus
178 ms and p95 521 versus 309 ms. The single repeat provides a quality lead
for follow-through. The approved three-repeat gate and independent panel
remain untested for both candidates. Groundhog completed no matched standing
repeat. All three Luna standing repeats completed.

Four OpenRouter requests returned credit-related HTTP 402. No semantic score
was assigned to those events. The approved backup also lacked positive
credit and mapped to the same creator account. The temporary variable was
removed and its ignored file was absent after cleanup. OpenRouter documents
this error source as a balance limit. [OpenRouter limit guidance](https://openrouter.ai/blog/tutorials/llm-api-rate-limits/).

Resume the same pinned route when funded access is available. The ledger
identifies 5,758 untouched standing calls and four 402 cells eligible only
after confirming the earlier charge and recovery conditions. Reserve
US$2.043254805 for the untouched OpenRouter calls plus US$0.001252885 for any
eligible replacement calls. Allow up to US$0.272058615 in additional
challenger reservation for the conditional 120-pair panel. The remaining
native Luna confirmation is conditional and uses its separate existing
route. These reservations remain within the original inclusive Dossier cap.
Keep the shared current Luna control, frozen request matrix and the independent
source review. Story 186 remains held pending a qualifying result and its
existing owner decisions.
[Owner verdict](/Users/cam/.codex/worktrees/baseten-decisions-20261121/dossier/docs/evals/artifacts/scout120-baseten-decisions-20261121/owner-verdict.json),
[Attempt](/Users/cam/.codex/worktrees/baseten-decisions-20261121/dossier/docs/evals/attempts/047-scout120-baseten-identity-20261121.md),
[matched first repeat](/Users/cam/.codex/worktrees/baseten-decisions-20261121/dossier/docs/evals/artifacts/scout120-baseten-decisions-20261121/bison-repeat1-diagnostic.json),
[resume preflight](/Users/cam/.codex/worktrees/baseten-decisions-20261121/dossier/docs/evals/artifacts/scout120-baseten-decisions-20261121/openrouter-resume-preflight.json),
[spend ledger summary](/Users/cam/.codex/worktrees/baseten-decisions-20261121/dossier/docs/evals/artifacts/scout120-baseten-decisions-20261121/spend.json).

### Spend and evidence custody

| Owner | Valid / physical calls | Known USD | Unresolved upper USD | Cap USD |
| --- | ---: | ---: | ---: | ---: |
| Board Game Ingester | 3 / 3 | 0.00026376 | 0 | 1.00 |
| Echo Forge | 38 / 38 | 0.000720529 | 0 | 0.45 |
| Dossier | 4,960 / 4,964 | 0.22597064 | 0.001252885 | 8.00 |
| **Combined** | **5,001 / 5,005** | **0.226954929** | **0.001252885** | **9.45** |

Maximum exposure on dispatched calls is US$0.228207814. No paid judge calls.
Both Baseten checkpoints metered one output unit per valid decision with
zero output charge in the measured routes. No selectable reasoning effort
or effort sweep was used.

| Owner | Retained worktree under `/Users/cam/.codex/worktrees/baseten-decisions-20261121/` | Branch | Base |
| --- | --- | --- | --- |
| Board Game Ingester | `boardgame-ingester` | `codex/scout120-baseten-orientation` | `25b9aa865f12fc85c5fc6438348758ee669ffd3b` |
| Echo Forge | `echo-forge` | `codex/scout120-baseten-intent` | `689a02df65dd8257cb01fdbbdf1f77932015d316` |
| Dossier | `dossier` | `codex/scout120-baseten-identity` | `0c8418a13f4dad6fc967dd47f478bc1c7ceeeaaf` |

The worktrees preserve uncommitted owner evidence and evaluation harness
changes. The Dossier tree also preserves the frozen inputs for resumption.
Dossier passed 87 focused tests, Ruff, registry and artifact checks, exact
request and response replay, and byte verification of 9,946 protected
archive members.
Final decisions for the current evidence are to retain Gemini for reviewed
orientation, Liquid for operative intent and Luna for possible identity.
Dossier's approved comparison remains open.

## Dossier continuation — November 21, 2026

Cam replenished OpenRouter credits and asked to resume. The continuation uses
the same approved BaseTen routes, frozen decision matrix, synthetic confirmation
panel and completed direct Luna control, under the original inclusive US$8 Dossier
ceiling. Any candidate that clears the standing gate advances to the frozen
independent panel. Board Game Ingester and Echo Forge decisions above still apply.

**Retain Luna Decisions. Groundhog failed the standing false-question gate.
Bison remains a quality lead with an incomplete standing matrix.**

| Challenger | Fresh matched standing evidence | Useful questions per held-out repeat, challenger / Luna | False questions per repeat, challenger / Luna | Subject cost, challenger / Luna | Median / p95 latency, challenger vs Luna |
| --- | --- | ---: | ---: | ---: | --- |
| Groundhog | All 1,191 pairs × three repeats | 18 / 17 of 18 | 23 / 10 | $0.05663154 / $0.16287450 | 299 / 396 ms vs 179 / 313 ms |
| Bison | 1,191 pairs × two complete repeats. Third repeat partial. | 17 / 17 of 18 | 3 / 10 | $0.1078696 / $0.1085830 | 314 / 456 ms vs 181 / 314 ms |

Development-only thresholds were 0.50 for the two challengers and 0.65
for Luna on their reported complete-repeat comparisons. The held-out set
contained 340 pairs per repeat. Groundhog cost 65% less but produced 13 more
false questions per repeat to recover one useful question. Bison cut false
questions by 70% at similar cost, with higher latency. The first two complete
Bison repeats are descriptive. The third has 430 valid responses, 748 untouched
cells and 13 unresolved HTTP 429s, seven in development and six in held-out.
Repeated route throttling continued after cooldown, lower rate and
one-in-flight dispatch. There was no retry/reset header. Groundhog finished
on the same provider account. No candidate qualified for the frozen
independent panel or a change to Story 186.

The four original router credit rejections were reconciled at zero after
checking the saved pre-inference envelopes and the provider's failed-attempt
billing guidance. Their physically attempted replacements returned valid
responses. The 13 usage-less rate-limit responses remain reserved and do
not count as quality observations. [Provider billing policy](https://openrouter.ai/pricing#faq).

| Owner | Valid / physical calls | Known USD | Unresolved upper USD | Cap USD |
| --- | ---: | ---: | ---: | ---: |
| Board Game Ingester | 3 / 3 | 0.000263760 | 0 | 1.00 |
| Echo Forge | 38 / 38 | 0.000720529 | 0 | 0.45 |
| Dossier, both phases | 9,961 / 9,978 | 0.351164140 | 0.007805700 | 8.00 |
| **Campaign to date** | **10,002 / 10,019** | **0.352148429** | **0.007805700** | **9.45** |

Dossier continuation added US$0.125193500 in known spend. Maximum campaign
exposure so far is US$0.359954129. The control was shared and is counted
once in spend. Native default Choice remained the evaluated configuration.
[Groundhog standing result](/Users/cam/.codex/worktrees/baseten-decisions-20261121/dossier/docs/evals/artifacts/scout120-baseten-decisions-20261121/continuation-standing-groundhog-1.json),
[Bison two-repeat result](/Users/cam/.codex/worktrees/baseten-decisions-20261121/dossier/docs/evals/artifacts/scout120-baseten-decisions-20261121/bison-two-complete-repeat-comparison.json).

At the end of live work, Bison's remaining identity comparison depended on
same-route capacity. The prepared resumption plan required the exact route to have
a documented quota reset or sustains a bounded, one-in-flight run of up to
25 untouched cells. The 748 untouched repeat-three cells consist of 434
development and 314 held-out cells and reserve US$0.4260694. If the standing
gate qualifies, reserve a further US$0.4050978 for Bison and a fresh Luna
control on the frozen independent panel. The completed standing control and
valid challenger cells remain reusable. Keep unresolved 429 receipts
unscored and reserved.
[Bison resumption requirements](/Users/cam/.codex/worktrees/baseten-decisions-20261121/dossier/docs/evals/artifacts/scout120-baseten-decisions-20261121/bison-rate-limit-reopen.json).

The Dossier worktree and branch above retain the uncommitted continuation.
The owner verified native receipt replay, scores, 87 focused tests, Ruff,
registry and links, 55 artifact bindings and all 10,050 continuation archive
members. The original protected archive was preserved and hash-verified.
[Continuation verdict](/Users/cam/.codex/worktrees/baseten-decisions-20261121/dossier/docs/evals/artifacts/scout120-baseten-decisions-20261121/owner-verdict-continuation.json),
[owner record and reproduction](/Users/cam/.codex/worktrees/baseten-decisions-20261121/dossier/docs/evals/artifacts/scout120-baseten-decisions-20261121/continuation.md).

## Final decision — November 21, 2026

Cam closed the Bison follow-up. Two matched repeats found seven fewer false
questions with the same useful-question recall, at similar cost and higher
latency. That measured gain did not justify another round for this role.
The third repeat, independent confirmation and deployment fitness remain
unmeasured. Preserve the completed evidence and close the approved wallet.

Retain Luna Decisions for Dossier possible-identity questions, the reviewed
Gemini Decision 1 job for Board Game Ingester orientation, and Liquid
d1.2-ultra for Echo Forge operative playback intent. Story 186 remains held.

### Owner evidence commits

Verified each owner commit on remote `main` and its evaluation branch.

| Owner | Evaluation commit | Evidence |
| --- | --- | --- |
| Board Game Ingester | [d78c1a35](https://github.com/copperdogma/boardgame-ingester/commit/d78c1a35b4a910bd27041bbe89ad89c195c2de4d) | [Orientation attempt](https://github.com/copperdogma/boardgame-ingester/blob/d78c1a35b4a910bd27041bbe89ad89c195c2de4d/docs/evals/attempts/20261121-scout120-baseten-orientation.md) |
| Echo Forge | [e7e394d1](https://github.com/copperdogma/echo-forge/commit/e7e394d1570647a7dfbc696c6d7b5c90e125e65d) | [Playback intent attempt](https://github.com/copperdogma/echo-forge/blob/e7e394d1570647a7dfbc696c6d7b5c90e125e65d/docs/evals/attempts/control-intent-v1/20261121-scout120-baseten.md) |
| Dossier | [b6ceb03f](https://github.com/copperdogma/dossier/commit/b6ceb03f44abe27ceaed4c79f4a1beaeb8b83674) | [Identity continuation and operator closure](https://github.com/copperdogma/dossier/blob/b6ceb03f44abe27ceaed4c79f4a1beaeb8b83674/docs/evals/artifacts/scout120-baseten-decisions-20261121/continuation.md) |
