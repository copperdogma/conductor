# Scout 079 follow-up — Dossier reasoning-effort value check

Date: 2026-09-29
Status: Historical comparison complete — its selected low-effort stage was later superseded by medium qualification and verified runtime-default promotion landed on Dossier remote main
Owner: Dossier, `standalone-semantic-value`
Related: [completed campaign](scout-079-gpt61-sol-evaluation-routing.md)

Cam approved preparing the Dossier promotion plan and requested consideration
of different thinking levels. This proposal incorporates that comparison.
No new provider calls, target-repo edits, credentials, or runtime changes were
made while preparing it. The previous campaign's unused ceiling is not a
standing authorization for this new matrix.

## Decision and prior evidence

Find the least expensive fully faithful GPT-6.1 Sol setting, then check whether
its advantage over Astra survives new source families and its own generated
history. Keep this benchmark in the standalone Dossier library; no Storybook
integration is part of the proposal.

[Attempt 018](/Users/cam/.codex/worktrees/gpt61-sol-eval-20260929/dossier/docs/evals/attempts/018-gpt61-sol-namesakes-value.md)
used **medium**, two snapshots of one exposed namesakes family, and authored
reference history. Sol and Astra both passed complete source-first reviews;
Sol cost $0.041416 versus $0.223230 and took 40.22s versus 62.76s. That result
does not measure low/high effort, unseen families, or generated-history drift.

The [current official model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
confirms `low`, `medium`, `high`, `xhigh`, and `max`; `none` and `minimal` are
unsupported. Standard rates per million tokens are $2 input, $0.10 cache read,
$2.50 cache write and $10 output. Lower effort is a hypothesis about value,
not a guarantee of lower total cost. Reasoning tokens, visible output, input
cache behavior and latency must all be recorded.

## 1. Recommended execution — maximum USD 25

Use direct exact `gpt-6.1-sol` low/medium/high and fresh `gpt-6-astra` medium.
Use native strict Responses, the unchanged semantic prompt/compiler, serial
dispatch, Standard service, and the owner 240-second completion bound.
Start every subject arm at **8,192 maximum output tokens**, including reasoning,
to avoid constraining high effort to the previous 4,096-token allowance.
Preserve the previous run as historical evidence, not a fresh control.

| Phase | Inputs and history | Arms | Maximum primary calls |
| --- | --- | --- | ---: |
| Preparation | Three newly authored synthetic families, two chronological snapshots each; independently review source obligations and compile reference graphs before inference | No subject calls | 0 |
| Effort calibration | One development family: identity/name ambiguity and correction; identical authored reference history for every arm | Sol low, medium, high; Astra medium | 8 subjects + 8 independent reviews |
| Confirmation | Two separately frozen families: chronological identity correction; attribution/actor boundaries and uncertainty. Each arm uses its own earlier compiled graph as history | One frozen Sol setting; fresh Astra medium | 8 subjects + 8 independent reviews |

The confirmation families are unexposed to the evaluated subjects before this
phase, not private data or proof of broad real-world coverage. Freeze all source
text, obligations, references, prompts, review contracts and hashes before the
first subject call. Do not tune on confirmation answers or replace difficult
cases after seeing results. One repeat per family is an initial bounded check;
do not infer production failure rates or latency percentiles from it.

Use the same blind cross-provider `claude-opus-4-6` review for every output,
covering every source obligation and every emitted row, with subject identity,
effort, cost and the other answer hidden. Coordinator source review resolves
demonstrable judge/reference defects symmetrically; retain original evidence
and rejudge saved outputs instead of repeating subjects.

### Selection and stop rules

- Native identity, terminal completion, schema and canonical compilation must
  pass before semantic scoring. Truncation or an adapter fault is an operational
  problem, not a semantic failure; repair within the reserve and disclose any
  changed output allowance. Do not quietly compare differently constrained arms.
- An effort qualifies only with **zero minor or material source-meaning
  defects**, including omissions, unsupported inventions, actor/identity merges,
  uncertainty loss and history drift. Compilation alone is insufficient.
- Review snapshot one before advancing an arm. A source-backed semantic failure
  disqualifies that effort; continue other independent arms. If no Sol effort
  qualifies, stop before confirmation and retain Astra.
- Among fully accepted efforts, select the lowest measured complete-task cost
  with no observed task-latency regression against fresh Astra. Show the full
  quality/cost/latency tradeoff if no single arm dominates. Prefer medium if
  lower effort has no clear measured benefit; do not declare a tiny one-run
  difference a stable advantage. Freeze this choice before opening confirmation.
- On confirmation, require both chronological snapshots in both families to
  remain fully faithful, and compare complete sequential task cost and latency
  against Astra. Report failures and stop the affected arm's dependent history;
  do not silently insert an authored graph after failure.
- Report billed usage estimates, cache-normalized economics, and cost per
  accepted complete case, including failed subject work. Separate subject cost
  from reviews and operational recovery. No artificial cache warming or output
  caching; balance arm order across cases.

### Budget feasibility

The existing owner reservation conservatively bounds input tokens as four times
native request bytes plus 4,096. With a **30,000-byte native-request limit** and
8,192 output tokens, input allowance is 124,096 tokens, priced at the higher
input/cache-write rate. The source size limit is checked before inference;
never truncate semantic content to make an oversized request fit.

| Reservation | Count | Maximum each | Total USD |
| --- | ---: | ---: | ---: |
| Sol subjects | 10 | 0.39216 | 3.92160 |
| Astra subjects | 6 | 1.96080 | 11.76480 |
| Opus reviews, 38,000 request bytes / 8,192 output | 16 | 0.39992 | 6.39872 |
| Primary matrix | 32 | | **22.08512** |
| Qualification and evidence-driven recovery allowance | | | **2.91488** |
| Hard campaign maximum | | | **25.00000** |

These are conservative reservations, not expected charges. The prior eight-call
run cost $0.500636, but this larger/new-source matrix has no measured cost yet.
Before any paid run, the owner must render every fixed-history request, compile
references, size the review packets, and validate complete-matrix feasibility.
Generated history changes sizes: reserve each actual next request and its review
before dispatch. Unknown billing remains reserved. If a size/transport repair
cannot fit the hard cap, stop at the genuine boundary without dropping required
reviews or reporting incomplete work as a promotion pass.

## Verified owner substrate and preparation scope

Read-only inspection used isolated base
`6500993e8528fcfd418ae7d0e2703566a42e0b17` and Attempt 018 artifacts.
At execution, refresh the remote base and preserve the completed campaign;
create a separate isolated worktree if reuse would mix scopes.

- `evals/semantic_benchmark/runner.py` supports `history_mode=reference|candidate`;
  candidate history appends each compiled graph and skips dependent snapshots
  after a failure. Its `preflight` renders native requests and verifies references.
- `evals/semantic_benchmark/corpus.py` selects cases, constructs history and
  requires explicit holdout admission. New source families and their complete
  reviewed obligations still need authoring in the owner repo after selection.
- Reuse the existing native adapter, independent review machinery and shared
  reservation ledger. Register the new attempt/configuration and preserve raw
  requests, responses, review packets, costs, hashes and offline reproduction.
- Existing owner credentials are preferred; eligible fixtures are newly authored
  synthetic material only. Standard retention/no-training default applies; ZDR
  remains unverified. No private genealogy records or consumer conversations.

The plan authorizes evaluation preparation and the bounded experiment if selected,
not a production change. A passing result supports a narrow setting recommendation
for the tested workload. It does not establish a safe low-to-high fallback:
semantic omissions can pass the compiler, and an offline reviewer is not a
runtime routing signal. Broader default adoption remains a separate decision.

## Other thinking levels and projects considered

Defer `xhigh` and `max` in this value pass: low/medium/high already measure the
cheaper-setting hypothesis and one higher-effort quality point. Their capability
is unmeasured, not presumed worse. Reconsider only for a concrete remaining task
whose quality benefit could justify additional cost/latency.

Doc Web, CineForge, Storybook and Echo all used Sol **low**, already the minimum.
They have no lower-effort savings experiment. Higher effort could improve quality,
but would need its own bounded task proposal. Keep Doc Web's detector integration
check second in portfolio priority; do not implicitly reopen its failed safety
screen, disputed handwriting reference, or the other completed owner comparisons.

## Approval boundary

Cam subsequently replied `Yes` to the complete proposal. Item 1 is selected
with its USD25 all-provider ceiling, synthetic-only fixtures, isolated owner
execution and no runtime/landing changes. The proposal below is retained as
the historical approval boundary; no second routine approval is required.

Reply `yes` to run item 1 under the USD25 all-provider hard ceiling. This is a new
paid matrix beyond the completed campaign. The invoked
[evaluate-model skill](../../.agents/skills/evaluate-model/SKILL.md) requires
“spend up to each disclosed per-repo ceiling” within the selected scope; the
current approval was to prepare this plan. No commit, push, default change or
deployment is included.

## Selected execution log

- Cam selected item 1 with `Yes`; USD25 remains the hard all-provider ceiling.
- Fresh owner base: `6500993e8528fcfd418ae7d0e2703566a42e0b17`.
- Isolated worktree: `/Users/cam/.codex/worktrees/gpt61-sol-effort-promotion-20260929/dossier`.
- Branch: `codex/gpt61-sol-effort-promotion-20260929`.
- The original Attempt 018 worktree remains separate. Existing owner-managed
  access is preferred; central vault presence/integrity checks passed without
  reading or transferring a secret.
- Coordinator independently reviewed all six authored source snapshots,
  obligations and reference rows before subject exposure. Corrected discovery/
  signature dates, evidence provenance, tentative-name attribution and the
  distinction between unproven actor identity and proven nonidentity. Owner
  compiled all six references. Approved corpus SHA256:
  `c6b552cf34c333326c408b4ede102d58cbcb9b4c3f72b4214c005e8b06f5ad54`.
- Zero-call matrix review passed: eight arm/family plans, identical calibration
  histories, candidate-history confirmation, 8,192 output on all arms, six
  reviewed references, paired review reservations and USD22.08512 full bound.

### Calibration result

All arms passed both snapshots with zero minor or material source defects in
complete independent reviews. Subject costs exclude judging.

| Arm | Accepted snapshots | Subject USD | Sequential seconds |
| --- | ---: | ---: | ---: |
| Sol low | 2/2 | 0.035770 | 26.9273 |
| Sol medium | 2/2 | 0.047330 | 48.1899 |
| Sol high | 2/2 | 0.062080 | 75.6889 |
| Astra medium | 2/2 | 0.215700 | 48.5980 |

Selected **low** before confirmation. It was 24.4% cheaper than medium and
42.4% cheaper than high, with matched reviewed quality on this development case.
Selection SHA256:
`b798337f01ee46198594ea0ba49769efa566bdfafb82ceb5bda73a7d59224dbd`.
This single-case calibration does not establish universal effort rankings.

### Confirmation result and recommendation

**Carry GPT-6.1 Sol low forward as the preferred setting for this tested
Dossier semantic workload.** More thinking added cost and latency without a
calibration quality gain. The low setting then passed both separately frozen
families using its own generated history. This is a bounded promotion-check win,
not authorization or broad evidence to change every runtime default.

| Candidate-history family | Sol low | Fresh Astra medium | Subject USD, Sol / Astra | Sequential seconds, Sol / Astra |
| --- | --- | --- | --- | --- |
| River survey correction | 2/2 fully acceptable | 2/2 fully acceptable | 0.042816 / 0.236580 | 37.0617 / 59.6893 |
| Clock ledger attribution | 2/2 fully acceptable after contract-correct adjudication | 1/2; second snapshot material attribution error | 0.028390 / 0.176800 | 22.4384 / 43.8153 |
| Confirmation total | **4/4; 2/2 complete cases** | **3/4; 1/2 complete cases** | **0.071206 / 0.413380** | **59.5001 / 103.5047** |

Confirmation subject cost was 82.8% lower and elapsed time 42.5% lower for Sol,
with better reviewed quality on these cases. Including failed subject work,
cost per accepted complete confirmation case was USD0.035603 for Sol versus
USD0.413380 for Astra; the latter denominator is one because clock failed.
Across calibration plus confirmation, low passed 6/6 snapshots and 3/3 cases;
Astra passed 5/6 snapshots and 2/3 cases. These are descriptive counts from one
repeat per synthetic family, not population accuracy or reliability estimates.

The coordinator verified that each confirmation arm's second context matches
its own first compiled graph through the unchanged owner `compact_context`
projection. The projection deliberately removes historical actor bindings;
no authored history was substituted and no authority was inherited. The clock
second snapshot had no current actor offer and no new actor binding in either arm.

### Saved-answer adjudication

The original clock-second review marked low as having a minor gap for an
assistant-attributed `asserted` claim and for not repeating the earlier user
negation. Coordinator inspection found a demonstrated judge/contract mismatch:
the schema permits only `asserted`, `possible`, `negated` (not the judge's
suggested `inferred`), the runtime permits represented assistant claims with
assistant attribution, and explicitly says not to repeat facts retained
unchanged in history. This was not a reason to rerun a subject.

Both original anonymous saved answers received the same neutral contract
addendum and one new independent Opus review. The corrected review accepted Sol
without minor or material defects. Astra remained a material failure: it made
the ledger the subject of `attributes_clock_construction_to` the account holder,
fabricating the ledger's attribution. Its assistant attribution was present;
the failure is the wrong ledger relationship, not absence of attribution or an
unauthorized actor binding. Separate local Sela/account entities do not establish
that they are different real people; neither source nor conclusion claims that.

Both initial grades, unchanged packets, new prompts and corrected grades remain
in owner evidence. Two saved-answer review repairs cost USD0.120670. No subject
reruns, prompt tuning, source/golden changes after freeze or provider fallback.

### Final accounting and evidence review

| Provider work | Calls | Usage-priced USD |
| --- | ---: | ---: |
| Subjects, including calibration variants and fresh controls | 16 | 0.845466 |
| Initial independent reviews | 16 | 1.024215 |
| Symmetric saved-answer adjudication | 2 | 0.120670 |
| **Total** | **34** | **1.990351 / 25.00 cap** |

Unresolved exposure: USD0. Prices are receipt-derived estimates, not reconciled
invoices. Coordinator independently decoded all 16 native subject envelopes,
verified exact served identities and completed states, and repriced their usage
to USD0.845466. The shared ledger reconciled all 34 paid calls without unresolved
dispatches. No subject cache reads/writes were reported; cache normalization
does not change the observed comparison. Calibration reasoning-token telemetry
was 0 at low, 605 at medium and 1,868 at high; this describes provider-reported
usage, not a claim that low disables reasoning generally.

Owner evidence: [Attempt 019](/Users/cam/.codex/worktrees/gpt61-sol-effort-promotion-20260929/dossier/docs/evals/attempts/019-gpt61-sol-effort-promotion-20260929.md)
and the artifact bundle at
`docs/evals/artifacts/gpt61-sol-effort-promotion-20260929/` in the isolated owner.
Owner offline receipt/review/history verification, 96 focused benchmark tests,
Ruff undefined-name/import checks, YAML parsing and whitespace checks passed.
General lint still has long-line warnings in the fixture builder; the scoped
F/I checks passed. Coordinator independently verified every hash and byte size
in the 321-file [final manifest](/Users/cam/.codex/worktrees/gpt61-sol-effort-promotion-20260929/dossier/docs/evals/artifacts/gpt61-sol-effort-promotion-20260929/final-manifest.json).
Manifest SHA256:
`83bd5afeb12d084f62b77e04aa390726291d0bbaeaa783274d0f8dffe0fb2c2d`.
The [owner report](/Users/cam/.codex/worktrees/gpt61-sol-effort-promotion-20260929/dossier/docs/evals/artifacts/gpt61-sol-effort-promotion-20260929/README.md)
records exact reproduction commands and evidence limits. No runtime defaults,
commits or pushes changed. Existing owner-managed credentials needed no temporary
copy or cleanup.

This low-effort selection is historical and was superseded by the broader
medium qualification recorded in
[Scout 079 broader acceptance](scout-079-dossier-broader-acceptance.md). Cam
later selected Dossier's medium runtime-default promotion. With `capacity_profile`
omitted, `sol_medium_long` now supplies exact Sol medium in foreground mode,
with 32,768 output tokens, a 30,000-byte request limit, and a 420-second bound.
Explicit Astra profiles remain available and no fallback is configured. The
canonical prompt, graph schema and compiler are unchanged. Contract v4 requires
consumer pin renewal. Validation passed 2,595 unit and 60 focused tests, lint,
and methodology checks; unrelated full-suite legacy failures and the Gemini
default-evidence mismatch remain. The operator guide is
[semantic-sol-medium-runtime.md](/Users/cam/.codex/worktrees/gpt61-sol-effort-promotion-20260929/dossier/docs/semantic-sol-medium-runtime.md).
No new provider calls or consumer updates occurred. Owner changes are prepared
and landed on verified remote main. Campaign totals remain
USD20.227699 known and USD22.210424/25 conservative exposure.


### 2026-09-29 broader acceptance selection

Cam subsequently selected broader acceptance. The [concrete follow-through](scout-079-dossier-broader-acceptance.md)
covers all 11 maintained non-scale synthetic cases, including both long narratives,
with low versus fresh Astra medium. The USD85 proposal was withdrawn: it summed
simultaneous maximum reservations rather than expected settled spend. Cam approved
serial staged execution under the existing USD25 cumulative ceiling. The linked
follow-through records paid progress, retained timeout exposure, and complete
independent review. Runtime defaults remain unchanged.

Broader comparison now complete: Sol low10/11 accepted cases after a material
dialogue-attribution failure; Astra11/11 under the material-error gate, with one
disputed minor caption-layout rating. The earlier narrow low preference does
not authorize broader promotion. Retain Astra. Cumulative confirmed spend
USD14.727474; conservative exposureUSD16.710199/25 includes the original
unresolved timeout maximumUSD1.982725. The linked follow-through preserves
complete quality, usage, review coverage and operational-repair provenance.


## Final disposition

The early low preference was superseded by broader rejection and clean medium
qualification. Cam selected Sol medium as the direct semantic default. The
[final closeout](scout-079-dossier-broader-acceptance.md#final-closeout--2026-09-29)
records verified owner main commits, unchanged costs, and validation limits.
