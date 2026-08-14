# Alignment 044 - Eval Validity and Incumbent Parity

**Date**: 2026-08-13
**Classification**: Portable evaluation-validity discipline with repo-local repairs
**Source**: [Scout 054](../scout/scout-054-gemini-37-flash-deepseek-v4-pro-api-eval-routing.md)
**Story**: [Story 028](../stories/story-028-eval-validity-audit-and-repair.md)
**Projects Reviewed**: conductor, cine-forge, doc-web, echo-forge

## Focus

Audit the recurring outcome in which dozens of newer models fail to replace
historical winners. The goal is not to promote a challenger by weakening a
valid safety gate. It is to ensure that every no-adoption conclusion identifies
which layer actually failed:

1. source or factual golden truth
2. prompt and scorer contract agreement
3. calibration, selection, and regression-set independence
4. incumbent and challenger measurement parity
5. semantic capability
6. latency, cost, reliability, privacy, or other adoption constraints

The shared problem is evaluation validity, not identical harness text. Each
product repo remains the owner of its fixtures, risks, thresholds, and runtime
defaults.

## Portable Validity Contract

| Layer | Required evidence | Invalid shortcut |
| --- | --- | --- |
| Source truth | Independent source-first review, with ambiguous preferences separated from required facts. | Treating an incumbent-shaped golden as ground truth because an old winner matches it. |
| Prompt/scorer agreement | Every hard-scored requirement is stated by the subject prompt or independently required by the product consumer. | Rejecting a semantically valid answer for an unstated exact wording or exact numeric choice. |
| Set provenance | Cases are labeled as calibration, untouched selection/confirmation, or retained safety regression. | Using a case to tune the incumbent prompt and later counting that same case as untouched proof of model superiority. |
| Comparator parity | Current incumbent and challenger use the same decision contract, or retained outputs are demonstrably sufficient for honest current-scorer replay. | Naming an old-contract score the winner after declaring its evidence contaminated or superseded. |
| Capability result | Per-case semantic findings and uncertainty are reported separately from transport and value. | Calling capability worse when the only blocking failure is latency, cost, privacy, or route reliability. |
| Adoption result | Product safety, quality, latency, cost, reliability, and privacy gates remain explicit. | Promoting a model merely because a repaired scorer raises its semantic score. |

## Set Roles

- **Calibration** cases may guide prompt, schema, adapter, or effort selection.
  Their results explain configuration behavior but cannot independently prove
  generalization.
- **Selection or confirmation** cases remain untouched until the configuration
  is frozen. A configuration chosen from them needs a newly held-out or
  predeclared repeated confirmation before promotion.
- **Safety regression** cases preserve known product failures and may retain a
  perfect hard gate. If the incumbent was directly tuned on one, it still
  protects production but no longer supplies independent comparative evidence.

A case can change roles over time, but its provenance cannot be erased. Small
corpora should disclose when a clean held-out promotion claim is impossible
rather than silently recycling every case.

## Initial Differences

| Project | Initial evidence | Classification | Repair direction |
| --- | --- | --- | --- |
| CineForge | Current QA challengers are scored on a repaired two-case contract, while the registry marks historical rows contaminated yet still labels an old-contract GPT-4.1 Mini `1.0` the production winner. The subject prompt asks for a substantive judgment summary; the golden additionally requires three particular anchors. | Methodology conflict plus unclear product-contract drift. | Establish the production consumer requirement, align prompt/scorer/golden, add adversarial coverage, and measure the actual incumbent and challenger on one current contract. |
| Echo Forge | The prompt asks for short crossfades, but the scorer requires each duration to lie within `0.5` seconds of the exact golden. DeepSeek V4 Pro passed every other maintained semantic check and scored `0/2` solely on that hidden preference. | Portable scorer repair. | Derive supported duration semantics from product code/spec, test boundaries, and regrade retained incumbent/challenger outputs while preserving the independent latency/cost rejection. |
| doc-web | Manual source review supports the `page-126-000` fail label, but the case repeatedly acts as the sole challenger veto and was used in an incumbent prompt-tightening pass. | Valid safety regression with selection-contamination risk. | Preserve the visual safety case, disclose its calibrated role, establish an untouched comparison surface or block general superiority claims, and treat the hard safety decision separately from capability ranking. |

## Execution Isolation

| Project | Worktree | Branch | Base |
| --- | --- | --- | --- |
| CineForge | `/Users/cam/.codex/worktrees/gemini37-deepseek-v4pro-eval/cine-forge` | `codex/gemini37-deepseek-v4pro-eval` | `b2f9002` |
| Echo Forge | `/Users/cam/.codex/worktrees/deepseek-v4-pro-eval/echo-forge` | `codex/deepseek-v4-pro-eval` | `538c086` |
| doc-web | `/Users/cam/.codex/worktrees/eval-validity-audit/doc-web` | `codex/eval-validity-audit-doc-web` | `c69a2e1` |

The doc-web worktree path is the required destination for the prior uncommitted
Gemini 3.7 evidence; its primary checkout must remain unchanged. CineForge and
Echo Forge continue from their existing isolated evaluation worktrees so their
retained outputs and attempt lineage remain available.

## Repo Outcomes

### Echo Forge — historical capability downgraded; future capture repaired

- Product/runtime evidence established that exact transition seconds belong to
  the downstream Executor rather than scene-understanding quality. Candidate-
  close review rejected the first replacement `0.5`–`5` second range because
  neither endpoint was source-backed; that post-hoc preference is being removed
  rather than substituted for exact-golden matching.
- Symmetric frozen regrading preserved manual and `gpt-5.4-mini` at `2/2`, Kimi
  K3 at `1/2`, and Gemini 3.5 Flash-Lite, Gemini 3.6 Flash, and DeepSeek V4
  Flash at `0/2`. DeepSeek V4 Pro alone changed from `0/2` to `2/2`.
- Corrected conclusion: V4 Pro's retained normalized outputs pass every measured
  non-duration semantic check (`2/2`) as a **diagnostic only**. Strict-output
  compliance, quality qualification, and decision-grade capability are
  unmeasured because raw assistant content was not retained. V4 Pro remains an
  independently supported **operational reject**.
  Its scoreable calls averaged `66.889` seconds and `$0.016126` per fixture,
  with two empty initial router envelopes. Retain executable `gpt-5.4-mini`;
  no default changed and this repair made no paid provider calls.
- Candidate-close also found provider-agnostic reasoning/max-token flags whose
  requested values could be recorded even when non-OpenRouter handlers ignored
  them, plus stale `--force` metadata reuse. Those future-run configuration
  paths now fail closed and record effective sent configuration.
- A subsequent full-scope review confirmed those repairs but found the same
  evidence-integrity class deeper in the chain: nonempty wrong model/error
  status and unbound output bytes could pass reuse. Echo therefore remains in a
  bounded systemic provenance audit rather than claiming candidate-close.
- The systemic audit then exposed an irrecoverable historical-evidence gap:
  raw pre-normalization assistant JSON was never retained, and one normalized
  output no longer satisfies the strict schema because normalization removed a
  provider-returned null. Future captures can bind raw bytes, strict validation,
  normalization, and normalized output; the existing V4 bundle cannot be
  upgraded retroactively and its semantic `2/2` must remain diagnostic rather
  than decision-grade. The latency/routing operational rejection is independent
  and still supported.
- Future public/synthetic v3 captures retain exact assistant-content bytes
  without provider envelopes, headers, credentials, or hidden reasoning. Reuse
  recomputes strict raw schema, request/config/identity/status/provider binding,
  deterministic normalization, raw/normalized hashes, and fixture/response
  completeness; missing/tampered/drifted evidence fails closed. Focused `47/47`
  and full `520/520` validation passed, and a fresh final reviewer returned
  `RESULT: no-issue`.

### doc-web — safety result retained; winner claim blocked

- Manual source review and frozen regrading preserve Gemini 3.7 at `39/40` and
  confirm `page-126-000` as a real production-safety miss. The golden and
  configured runtime provider did not change.
- All `40` crop-only and `22` page-context cases have been exposed during
  prompt/provider selection, challenger tuning budgets were asymmetric, and
  the recorded crop-only `40/40` incumbent result is stale. The corpus can
  enforce regressions but cannot establish an unbiased model winner.
- Existing unscored output inventory has only three pass-style crops, two from
  already exposed source pages. Creating a nominal held-out set from them would
  provide neither failure balance nor source-page independence, so no false
  confirmation set was created.
- Selection status is now `blocked_pending_held_out_truth`. The frozen next
  contract requires `12` natural production crops balanced `6 pass / 6 fail`
  from at least eight unused source pages, independently reviewed and
  hash-frozen before calls; insufficient natural failures trigger fixed
  four-page expansion rather than synthetic or model-guided cherry-picking.
- Gemini 3.7 remains unpromoted. The strict integer detector remains credible
  at `13/13`; the two real handwriting fixtures remain below `0.99`. These
  conclusions are separate from crop-validator selection validity.
- Follow-up repair spend was `$0`. Focused tests, parsing, Ruff, Prettier,
  methodology, full lint, frozen regrade, and diff checks passed in the
  isolated worktree; the primary checkout remained byte/status unchanged.
- A first independent candidate-close review found fail-open regrader and
  prompt-provenance defects. After systemic repair, a fresh full-scope review
  adversarially verified partitions, malformed/duplicate/overlap/coverage
  failures, selection eligibility, every recorded hash, the raw `39/40`
  result, unchanged goldens/defaults, and primary isolation; it returned no
  material findings.

### CineForge — contract repaired; current winner withdrawn

- Two source-first independent passes removed the unsupported requirement that
  a successful QA summary recite three selected events and corrected the
  authoritative `RUDDY & GREENE` spelling. The positive fixture is otherwise
  faithful and all eight negative defects remain source-backed.
- The former error-count gate was invalid: overlapping defects could receive
  duplicate credit and both four- and six-count thresholds could omit critical
  identity/plot/conflict feedback. The maintained contract now owns six
  non-overlapping families: metadata, cast/identity, summary/plot,
  beats/events, tone, and candidate-confidence calibration.
- Each negative family requires a field-owned affirmative candidate-defect
  relation plus an independently affirmative source correction. Bounded
  deterministic checks fail closed on sparse keywords, adjective/anchor
  stuffing, generic summaries, negation, material contrast, modality/hedging,
  source-correct-only statements, double negation, and cross-clause token
  borrowing. The production `QAResult` schema remains unchanged.
- All `29` pre-final-contract QA score rows are explicitly non-decision-grade;
  the generated QA `latestScore` is `null`. Story 213's manifest now binds the
  current prompt, scorer, golden, validator, provider, Attempts 024–026, five QA
  results, DeepSeek evidence, registry/story evidence, and regression tests.
- The paid identical-runtime calls predate the final prompt/contract and retain
  only transport evidence: GPT-4.1 Mini averaged `3.148s` and `$0.000955/call`;
  Gemini 3.7 averaged `2.340s` and `$0.003324/call`. Under the final frozen
  scorer, GPT-4.1 Mini is `0.832475` and Gemini 3.7 is `0.834975`; both fail.
  Fresh final-contract semantic parity is unmeasured, so the GPT default stays
  only by inertia and no challenger is adopted.
- DeepSeek V4 Pro remains a separate CineForge operational reject: its tiny
  strict probe was already too slow/expensive and the cheaper route stalled;
  full-script semantic quality remains unmeasured.
- Final validation passed `168` focused scorer/golden/manifest tests, golden
  validation, Ruff, registry/truth-ledger/manifest/methodology/diff checks, and
  the proportional full unit suite. A fresh final structural reviewer returned
  `RESULT: no-issue`.

## What Should Sync

- Sync the six-layer validity classification and explicit set-role provenance.
- Sync the rule that contaminated or superseded evidence cannot remain the
  decision-bearing incumbent comparison.
- Sync scorer repairs through adversarial regression tests and frozen-output
  regrades before new paid calls.
- Keep product-specific hard safety thresholds, visual review procedures,
  schemas, and latency/cost limits local.

## Human Judgment Boundary

No runtime default changes are authorized by this alignment. If a repaired
contract shows a challenger is semantically better but the existing product
gate still blocks it for latency, cost, or a known safety regression, record
that split result and request a separate product decision rather than folding
it into the repair.

## Final Cross-Project Decision

- No evaluated model is promoted and no runtime default changed.
- The original pattern of repeated incumbent wins was not trustworthy: one
  challenger was falsely failed by an unstated preference, one incumbent table
  mixed incompatible contracts, and one safety corpus had no untouched
  selection evidence.
- Correcting those defects did not reveal a production-ready replacement. It
  changed the honest answer from “the incumbents keep winning” to three bounded
  conclusions: doc-web selection is blocked pending held-out truth; CineForge
  final-contract QA parity is unmeasured; Echo V4 capability is diagnostic-only
  while its operational rejection remains supported.
- Future model campaigns should start from these repaired contracts rather than
  the superseded rankings.
