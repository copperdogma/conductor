# Scout 121 — Perplexity Decider v1.3 and Flash v1.3

November 22, 2026, America/Edmonton. Stage 1 complete. Owner selection pending.

## Native API

| Exact Perplexity selector | Parameters | USD per million input tokens |
| --- | ---: | ---: |
| `pplx-decider-v1.3` | 27B | 0.02 |
| `pplx-decider-flash-v1.3` | 4B | 0.01 |

Both exact selectors are listed for `POST https://api.perplexity.ai/v1/decisions`.
Outputs are free and standard mode has no per-request fee. The interface accepts
text, JSON state and inline images. It returns typed Noul, Choice or Score
answers, or Locate spans on plain text. Locate returns scored verbatim spans
with Unicode offsets. It cannot extract from images. Each proposed lane uses
one native Choice question in standard mode, with web grounding disabled.
Native default computation is the only documented setting for the proposed
arms. Flash is a separate checkpoint. No reasoning-level sweep is warranted.
[Release](https://www.perplexity.ai/en-GB/hub/blog/perplexity-decider),
[Decisions contract](https://docs.perplexity.ai/docs/decisions/decisions),
[pricing](https://docs.perplexity.ai/docs/getting-started/pricing#decisions-api-pricing).

Access remains unverified for both checkpoints. Use the explicit versions and
retain the provider mapping and response identity. The response echoes the
requested selector, so it cannot independently attest the served weights.
Check the exact Choice set, mapping and metered usage with eligible owner
fixtures. Keep a per-arm record of retries, 429s and first-attempt availability.
Prior v1.2 results remain separate. Neither exact v1.3 selector has an attempt
in the evaluated ledger. [v1.2 owner evidence](scout-098-perplexity-decider-v12-evaluation-routing.md#completed-owner-decisions--2026-10-17),
[evaluated ledger](../model-watch/evaluated-models.md).

Only authored synthetic fixtures and the specified licensed public assets are
eligible. Perplexity's API policy states no generative-model training by default,
subject to specific terms. Decisions-specific retention and account ZDR remain
unverified. For the router controls, effective account opt-ins and endpoint
retention are unverified. The Dossier control uses the owner's native OpenAI
route on synthetic rows. Owner restrictions apply at dispatch.
[Perplexity API privacy](https://docs.perplexity.ai/docs/resources/privacy-security),
[OpenRouter data collection](https://openrouter.ai/docs/guides/privacy/data-collection),
[OpenAI Decisions API](https://developers.openai.com/api/docs/guides/decisions).

## Evaluate now

Compare both Perplexity models in one campaign. Share one fresh incumbent call
per matched case and repeat. Freeze the case matrix, prompts, option order,
fixture provenance, scoring and confirmation inputs before inference. Score
with the maintained owner logic and review new goldens independently before
they enter the matrix. Use a zero-cost rendered preflight and per-owner
spend admission. Start with a qualifying request for each challenger before
bulk control spend. Stop only the affected arm after a decisive failure. Run
the first pass sequentially per Perplexity account until usage and rate-limit
behavior support safe concurrency. Report actual billed cost, paired latency
and first-attempt availability. All dollar limits include bounded recovery.

| # | Owner and first lane | Incumbent and replacement boundary | Decision and next action | Ceiling |
| --- | --- | --- | --- | ---: |
| 1 | Board Game Ingester, isolated asset orientation | Gemini Decision 1 in the reviewed orthogonal orientation job | Prior Deciders both missed DOCK. The incumbent repeatedly auto-kept a rotated public asset. Start with both failures and a mandatory hold. A safe winner advances to independent images and reviewed export. Awaiting selection. | $1.00 |
| 2 | Echo Forge, `control-intent-v1` | Liquid d1.2-ultra as sole operative playback intent classifier | v1.2 introduced false controls and both arms missed all ambiguity cases. Test whether the new checkpoints preserve command safety and improve ambiguity handling or speed. Awaiting selection. | $0.25 |
| 3 | Dossier, `evals.possible_identity.benchmark` | Native Luna Decisions for possible-identity questions under ADR-026 | Challenger reductions in false questions have yet to generalize with complete reliability and useful-question recall. Test both on the same three-repeat matrix and qualify any winner on independent synthetic pairs. Story 186 remains held. Awaiting selection. | $4.50 |

### 1. Board Game Ingester

Qualify the existing finite angle/review contract. Start with `f24-04`, DOCK
and a mandatory hold, then the balance of 14 authored cases and four reviewed
public cases. Preserve CC BY 4.0 attribution for 01 and 03, CC0 custody for 02
and 04, and the original and request hashes. Reuse the same documented lossless
PNG derivative across all arms and the incumbent high-image setting on Google
AI Studio. Even the prior enlarged maximum edge was 576 pixels, below the
Decider tile cap. Stop a candidate on an incorrect automatic transform or lost
mandatory hold. Require all determinate cases correct, with a hard-case gain
or at least 30% lower paired p95 including preprocessing at equal quality.
Track unnecessary review separately.

Advance qualifying arms to one independently reviewed eight-image authored
panel, then verify the normal reviewed job, forward and inverse pixel checks,
hold handling and export before preparing a sole-job replacement patch.
Up to 30 calls per arm cover qualification, panels and recovery. At 262,144
tokens for Gemini and an 8,192-token rendered bound for each Decider, the
reservation is US$0.7938048.
[Matched Google AI Studio rate](https://openrouter.ai/api/v1/models/google/gemini-decision-1/endpoints),
[source and prior owner results](scout-120-baseten-bison-groundhog-evaluation-routing.md#board-game-ingester-and-echo-forge-results).

### 2. Echo Forge

Use the actual runtime builder and 42 authored cases. Start with negation,
quotation, ambiguity and the previously observed hypothetical or revision
commands. The last full Liquid control reached 40/42 with no false controls
and 19/19 operative commands. Stop a candidate on a false control. Require
at least matched accuracy and recall, zero false controls, and improved
ambiguity handling or at least 30% lower paired component p95 at equal quality.
Absolute token savings are small. The relevant gain is safer classification
or a material reduction in the interactive classifier delay. End-to-end
push-to-talk time share is unmeasured.

Confirm on one 12-case independently authored panel, then exercise the actual
consumer and fault paths with the single-attempt deadline and manual review.
Prepare a replacement of the sole classifier only if those checks pass. Up to
60 calls per arm, with 65,536 tokens for Liquid and an 8,192-token rendered
bound for each Decider, reserve US$0.17989632.
[Liquid route](https://openrouter.ai/api/v1/models/liquid/d1.2-ultra/endpoints),
[full matched baseline](scout-118-microsoft-decision-11-evaluation-routing.md#owner-results),
[latest safety failures](scout-120-baseten-bison-groundhog-evaluation-routing.md#board-game-ingester-and-echo-forge-results).

### 3. Dossier

Qualify the four-choice native contract. Begin with the frozen 36-pair
diagnostic. Stop the arm for a decisive source-safety or contract failure.
Then run the maintained 1,191 synthetic pairs across three fresh repeats per
surviving arm. Fit each threshold on development only and score the separate
340-pair held-out set. Require the candidate's worst repeat to match Luna's
best on useful questions found and false questions, with a strict gain on at
least one. No opposite explicit identity assertion may pass.

Qualify promising arms on one fresh, independently authored and reviewed
synthetic panel of up to 120 pairs over three repeats, frozen before
inference, with fixed thresholds and ordinary, explicit-denial and
minimal-context namesake strata. Require matched useful-question recall
across strata, fewer false questions, precision at least 0.75, at most
0.20 false questions per chapter group, and complete evidence under the
owner's matrix rules. This can qualify an evaluation choice. Runtime
replacement awaits the Story 186 decision and approval of an eligible route
for real recipient data. Locate spans do not cover the evaluated identity
verdict or the existing extraction pipeline's provenance contract.

Allow up to 4,000 calls per arm, covering 36 diagnostic, 3,573 standing, 360
confirmation and 31 qualification or recovery slots. Rebind the owner
byte-size-plus-4,096 estimate to each actual request, cap admitted requests
at 8,192 tokens, and check meters and the uncached Luna pricing and
cache configuration. At combined US$0.13/M, reserve US$4.25984.
[Recent Dossier owner evidence](scout-120-baseten-bison-groundhog-evaluation-routing.md#dossier-continuation--november-21-2026),
[Luna Decisions pricing](https://developers.openai.com/api/docs/guides/decisions#pricing-and-availability).

**Campaign maximum US$5.75.** This is a proposed provider-spend ceiling.
Recheck base, fixtures, rates, exact request accounting and enforceable
aggregate admission before dispatch. Isolated worktrees would belong under
`/Users/cam/.codex/worktrees/perplexity-decider-v13-20261122/<project-key>`.
Stage 1 used public source checks and local read-only owner inspection. Inference
spend was US$0.

## Not recommended now

| Registered owner | Disposition |
| --- | --- |
| Storybook | Defer. The prior Decider component win remained unreachable in the independent relationship-capture cases. Reopen against a reachable consumer case set where the route can change persisted disposition. Photo grounding requires generated evidence fields. Diarization requires audio input. |
| Doc Web | Defer. Gemini Decision 1 leads the existing consistency component screen. A connected planner and fallback benchmark is still required to show a user-facing benefit. Page safety needs source-specific reasons, and current full-page fixtures exceeded the native tile cap in the earlier check. Crop geometry and literal table reconstruction require coordinates or generated structure beyond text Locate. |
| CineForge | Defer. Entity, ScriptBible and ordered-frame tasks require generated fields and source provenance. No maintained finite-choice or verbatim-span consumer surfaced. |
| Robo Rally | Do not evaluate. The maintained rules and simulator use deterministic oracles and depend on complete race event outcomes. |
| Ultima IV Web | Defer. The maintained walkthrough and gameplay evidence uses deterministic outcomes. No current finite-choice lane with independent scored gameplay consequences surfaced. |
| Financial Hub | Defer. Inspected `financial-reporting`. Household analysis needs private source material and lacks an eligible maintained synthetic decision comparison. |
| Financial Monthly Analysis | Defer. Inspected `financial-data`. No eligible maintained synthetic benchmark for private reconciliation, categorization or recommendation decisions surfaced. |
| VLC Thumbs | Do not evaluate. Inspected the standalone checkout. Its decoding, caching and scheduling contracts are deterministic. |

Within the selected owners, Board Game Ingester deskew, segmentation and
package extraction need different outputs or sources. Echo scene design
requires generation and separate source adjudication. Dossier full-history
extraction requires generated assertions and provenance. These surfaces are
outside the three numbered comparisons.

## Approved execution — November 22, 2026

Cam selected all three numbered lanes. The inclusive owner ceilings are
US$1.00 for Board Game Ingester, US$0.25 for Echo Forge and US$4.50 for Dossier.
Each lane has an isolated owner worker. The central credential helper confirmed
Perplexity and OpenRouter availability by name without reading credentials
into the campaign log. Dossier's Luna control uses the existing native route.
Consumer review patches are in scope for qualified orientation or playback
winners. Dossier remains synthetic and the Story 186 runtime hold remains.
Perplexity publishes a shared organization limit of 10 requests per second and
per-minute limits of 15M tokens for Decider and 4M for Flash. Start with a
sequential account probe and use an aggregate allowance below the published
limits for further traffic. [Perplexity rate limits](https://docs.perplexity.ai/docs/decisions/decisions#request-limits).

### Board Game Ingester — retain reviewed Gemini Decision 1

Both Deciders and the fresh pinned Gemini control automatically kept the
same licensed `f24-04` PNG at 0°. The source requires a 90° clockwise
correction. Each model produced one valid first-attempt response on an
identical image derivative. Both challengers stopped at the predeclared
wrong-transform gate. DOCK, mandatory hold, the rest of the screen and
independent confirmation remain unmeasured. The matched end-to-end case took
404 ms for Decider, 470 ms for Flash and 1,241 ms for Gemini, including
preprocessing. These single observations cannot estimate general latency or
reliability. Subject costs were US$0.00000832, US$0.00000416 and US$0.00014010
respectively. Total US$0.00015258 known, zero unresolved, against US$1.00.
The reviewed path still requires operator review on hard orientations.
Offline regrade, forward/inverse exact-pixel replay and reviewed export
records all verified. Focused validation passed 37 tests and 52 subtests.
Both temporary keys were removed and verified absent by variable name.
[Owner attempt](https://github.com/copperdogma/boardgame-ingester/blob/30adc23a0d2da90a65367db35857693fda4ffc93/docs/evals/attempts/20261122-scout121-perplexity-orientation.md),
[owner verdict](https://github.com/copperdogma/boardgame-ingester/blob/30adc23a0d2da90a65367db35857693fda4ffc93/benchmarks/results/scout121-perplexity-orientation/owner-verdict.json).

### Echo Forge — retain Liquid d1.2-ultra

Both candidates treated a hypothetical about lowering the wind as an
automatic playback control. Liquid returned no control. This decided the
safety gate on six fresh matched authored cases. The full 42-case screen,
independent confirmation and candidate consumer path remain unmeasured.
All 18 calls were valid on the first attempt, with no 429 or retries.
The scoped speed advantage of Flash cannot offset its false control.

| Arm | Exact | False controls | Ambiguity holds | Sample p95 | Subject USD |
| --- | ---: | ---: | ---: | ---: | ---: |
| Decider v1.3 | 3/6 | 1/3 | 0/2 | 480 ms | 0.000042660 |
| Decider Flash v1.3 | 4/6 | 1/3 | 1/2 | 250 ms | 0.000021330 |
| Liquid d1.2-ultra | 4/6 | 0/3 | 0/2 | 434 ms | 0.000090216 |

Spend was US$0.000154206 known, zero unresolved, against US$0.25. Receipt
replay, methodology checks and ten existing native, routing and fault/deadline
checks passed. The owner reused its scoped process-only OpenRouter access.
Temporary `PERPLEXITY_API_KEY` was removed and verified absent.
[Owner attempt](https://github.com/copperdogma/echo-forge/blob/744792a94e3b319c17817ecb9ccb8ed1851c1389/docs/evals/attempts/control-intent-v1/20261122-scout121-perplexity.md),
[owner verdict](https://github.com/copperdogma/echo-forge/blob/744792a94e3b319c17817ecb9ccb8ed1851c1389/docs/evals/evidence/scout121/owner-verdict.json).

### Dossier — retain Luna Decisions

Both native Deciders and the shared Luna control qualified on exact
four-choice responses and finished all 36 diagnostic pairs. The frozen
standing panel then completed all 1,191 synthetic pairs across three
fresh repeats per arm. Scores below are for the 340 held-out pairs per
repeat at development-only thresholds. Latency and costs cover the full
standing matrix.

| Arm | Development threshold | Useful questions found | False questions | Median / p95 | Standing subject USD |
| --- | ---: | ---: | ---: | ---: | ---: |
| Decider v1.3 | 0.80 | 17, 18, 17 of 18 | 2 each | 276 / 650 ms | 0.03089052 |
| Decider Flash v1.3 | 0.75 | 15 of 18 each | 3 each | 196 / 354 ms | 0.01544526 |
| Luna Decisions | 0.65 | 17 of 18 each | 10 each | 204 / 331 ms | 0.16287450 |

Decider led the standing comparison with matched or better recall and
80% fewer false questions. It cost 81% less than Luna on that matrix and
had nearly twice Luna's p95. Flash missed two useful questions relative to
Luna in every repeat. Independent readback also found one raw identity
assertion contradicting an explicit spousal relationship. Its confidence
was below the operating threshold. The predeclared raw source-safety gate
still ruled it out and it received no independent qualification calls.
[Decider standing comparison](https://github.com/copperdogma/dossier/blob/d2413dc64f86c2a71aed60e9da1f92c52642a074/docs/evals/artifacts/scout121-perplexity-decisions-20261122/standing-pplx-decider-v1.3-comparison.json),
[Flash standing comparison](https://github.com/copperdogma/dossier/blob/d2413dc64f86c2a71aed60e9da1f92c52642a074/docs/evals/artifacts/scout121-perplexity-decisions-20261122/standing-pplx-decider-flash-v1.3-comparison.json).

On the independent 120-pair synthetic panel, Decider found 14, 14 and 15
of 19 useful questions. It raised six false questions per repeat, or
0.375 per chapter group against the required maximum of 0.20. Precision
was 70.0%, 70.0% and 71.4% against a 75% minimum. It missed all three
useful explicit-denial contrasts and raised all three bare-name negatives
in every repeat. Luna found 19 of 19 and raised four false questions in
its first matched repeat. Its 0.25 false questions per group also exceeds
the candidate qualification bar. After Decider's failure settled the
replacement decision, Conductor stopped additional Luna dispatch. The 48
completed second-repeat control cells are preserved without imputation.
The controlled confirmation comparison therefore covers one complete
matched repeat and 48 additional matched cells. Story 186 stays held.
The owner replayed all 22,738 exchange files from the portable archive and
passed 97 focused tests, Ruff and methodology graph validation. Git contains
the archive custody manifest. The archive itself stays in protected storage.
[Independent confirmation](https://github.com/copperdogma/dossier/blob/d2413dc64f86c2a71aed60e9da1f92c52642a074/docs/evals/artifacts/scout121-perplexity-decisions-20261122/confirmation-pplx-decider-v1.3-comparison.json),
[owner attempt](https://github.com/copperdogma/dossier/blob/d2413dc64f86c2a71aed60e9da1f92c52642a074/docs/evals/attempts/048-scout121-perplexity-identity-20261122.md),
[owner report](https://github.com/copperdogma/dossier/blob/d2413dc64f86c2a71aed60e9da1f92c52642a074/docs/evals/artifacts/scout121-perplexity-decisions-20261122/README.md),
[exchange archive index](https://github.com/copperdogma/dossier/blob/d2413dc64f86c2a71aed60e9da1f92c52642a074/docs/evals/artifacts/scout121-perplexity-decisions-20261122/native-archive-index.json).

### Spend and custody

| Owner | First-attempt valid / dispatched | Metered USD | Unresolved USD | Ceiling USD |
| --- | ---: | ---: | ---: | ---: |
| Board Game Ingester | 3/3 | 0.000152580 | 0 | 1.00 |
| Echo Forge | 18/18 | 0.000154206 | 0 | 0.25 |
| Dossier | 11,358/11,358 | 0.219702970 | 0 | 4.50 |
| Total | 11,379/11,379 | 0.220009756 | 0 | 5.75 |

All measured arms used native Choice at default computation. No selectable
thinking levels or paid judges were used. Spend counts the fresh controls
once per case and excludes documented free catalog requests. The paid
receipts showed no failures or retry overhead. The temporary credentials
were removed and verified absent by name. Existing owner credentials were
used only for their authorized control routes.

| Owner evidence commit | Retained worktree | Branch | Verified remote base |
| --- | --- | --- | --- |
| [Board Game Ingester](https://github.com/copperdogma/boardgame-ingester/commit/30adc23a0d2da90a65367db35857693fda4ffc93) | `/Users/cam/.codex/worktrees/perplexity-decider-v13-20261122/boardgame-ingester` | `codex/perplexity-decider-v13-20261122-boardgame-ingester` | `d78c1a35b4a910bd27041bbe89ad89c195c2de4d` |
| [Echo Forge](https://github.com/copperdogma/echo-forge/commit/744792a94e3b319c17817ecb9ccb8ed1851c1389) | `/Users/cam/.codex/worktrees/perplexity-decider-v13-20261122/echo-forge` | `codex/perplexity-decider-v13-20261122-echo-forge` | `e7e394d1570647a7dfbc696c6d7b5c90e125e65d` |
| [Dossier](https://github.com/copperdogma/dossier/commit/d2413dc64f86c2a71aed60e9da1f92c52642a074) | `/Users/cam/.codex/worktrees/perplexity-decider-v13-20261122/dossier` | `codex/perplexity-decider-v13-20261122-dossier` | `b6ceb03f44abe27ceaed4c79f4a1beaeb8b83674` |

The three owners retain their evaluation adapters and durable
evidence in these isolated worktrees. The campaign recommends keeping Gemini
Decision 1 for reviewed orientation with operator inspection, Liquid
d1.2-ultra for playback intent, and Luna for possible-identity questions.
Neither challenger qualified for a replacement patch. Cam confirmed the
incumbents should remain and authorized publication of the evaluation evidence.
