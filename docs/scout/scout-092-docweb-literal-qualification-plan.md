# Scout092 — Doc Web literal-reader qualification plan

Date: 2026-10-13. Status: reviewed plan; execution selected 2026-10-13.

Cam's subsequent `yes` approved the bounded implementation and execution below.
[Execution record](scout-092-docweb-literal-qualification.md) tracks offline
readiness, source freeze, spend and the actual owner verdict. The planning
validation remains historical preparation evidence, not runtime acceptance.

Cam approved preparing this plan after the completed Argon thinking-level
calibration. This approval covers planning, not another paid run or runtime
activation. No provider calls, credential inspection, owner edits or spend
occurred during preparation.

## Decision and expected benefit

Qualify **Google native `gemini-4-argon`, medium thinking**, as an explicitly
selected source-only literal-table reader against fresh **OpenAI `gpt-6-astra`,
medium reasoning**. Keep the initial OCR model, literal policy, prompts, goldens,
source pixels and builder rules fixed. Low/high are not additional arms.

The initial three-case reader screen preserved 36 clear cells and ambiguity
holds at 88.47% lower reader cost. The later level comparison preserved quality
but exposed large timing variation: medium took 3.740, 210.425 and 7.869 seconds;
low saved 10.96% but was slower in all three pairs. Existing cases are exposed
regressions, not independent qualification. Reader agreement cannot by itself
establish literal truth.

The desired outcome is a source-faithful, cheaper reader that the actual guarded
export path can consume within an acceptable batch delay. Upstream OCR remains
required. Measure its contribution separately; do not apply the reader saving
percentage to the whole pipeline. Invocation volume, maintenance cost and human
review time are currently unknown, so no annual savings or avoided-review value
is assumed.

## Verified implementation boundary

The real opt-in consumer is
`configs/recipes/recipe-pdf-literal-tables-html.yaml` →
`literal_table_review_v1` → `build_chapter_html_v1`, with
`require_literal_fidelity: true`. Each three-page batch means three serial, single-image OCR POSTs, followed by
three reader POSTs; there is no multi-page API request or `batch_size` flag.
Current `SourceOnlyReader` rejects models other than Astra. Independently,
`literal_fidelity_bundle.py` requires Astra/OpenAI-specific native receipts.
An injected benchmark callback therefore cannot qualify final exported HTML.

Execution must first implement a small, explicitly selected Google reader and
provider-aware source authority profile. Preserve the Astra default and its
existing validations. The Argon profile must bind the exact requested/served
model, terminal response, schema/policy, full lossless image, native raw bytes,
parsed source table and final report lineage. Never label a Google response as
an OpenAI response or bypass the bundle verifier. No automatic fallback to a
different model, prompt correction or ambiguity inference is permitted.

The current source reader reserves USD 1.50 cumulatively per request without
settling usage. A new campaign ledger must account for actual underlying POSTs
and settlement while retaining the owner safeguards; merely increasing that
local budget or wrapping an injected callback is insufficient. Capture actual
request topology and SDK retries before spending.

Refresh remote/base state at execution and use an isolated current-base
`codex/` worktree. Preserve the completed Scout092 worktree, Attempts071/072,
their raw evidence and closed ledgers. Allocate unused owner story/attempt
numbers at execution rather than assuming that the next number remains free.

## 1. Recommended bounded qualification

### A. New source panel and offline acceptance

Independently author and source-review **eight new synthetic table pages**:
six clear pages and two expected-hold pages. These are new campaign holdouts,
not a claim that the model has never seen similar material during training.
Use new layouts and text, not renamed or lightly edited Attempt062/071/072
fixtures. Keep authoring/gold review independent of provider answers and tuning.

| Stratum | Pages | Required distinction |
| --- | ---: | --- |
| Native-text source PDF | 3 | Case-sensitive identifiers, punctuation, entities, literal misspellings; merged headers and row/column ownership; surrounding prose and multiple tables |
| Image-only source PDF | 3 | Different raster/font/layout families; faint but independently legible text; dense cells, blank versus dash, spans and footnote ownership |
| Expected uncertainty | 2 | Genuinely indistinguishable glyphs; source loss that prevents one or more literal cells from being established |

Keep pages modest (target at most 40 cells per page and at most eight tables per
three-page positive batch) but retain meaningful ownership/span complexity.
Use design IDs N1–N3 for native pages, R1–R3 for raster pages and A1–A2 for holds.
N1/R1 are sparse, N2/R2 medium-density, and N3/R3 dense or multiple-table pages.
Set the eight page IDs, table/cell truth, uncertainty
locations, order and four repeat IDs before any model answer. Include at least
one page from each stratum in the repeat set: preselect N3, R1, R3 and A1.
The opening screen is N1 and A1. Visual source review must establish
which cells are clear versus ambiguous before using them as gold. Native PDF
text is supporting provenance, never unquestioned visual truth. Freeze PDFs,
lossless renders, golds, prompts, schemas, recipes, model settings and source
hashes. No private scans, personal documents, copyright-unclear material or
downstream Ingester inputs are added.

Before paid execution, replay saved/mocked envelopes through the actual CLI,
review module, verifier and builder. Test both valid provider profiles and
rejection of wrong model/terminal state, altered raw output/image/policy hashes,
missing receipt, forged provider identity, OCR/source disagreement, ambiguous
cells and export-path overwrite. Verify exact final table text, spans and
ownership; initial OCR/raw HTML stays inspectable. Use fresh output directories.
Expected-hold cases must not publish a qualified bundle. Existing exposed cases
can supply these regression checks, separately from the new panel's results.

Stop before spending if the real Google dispatch/receipt path, independent
source truth, privacy, full-input token bounds or budget admission is unproven.

### B. Fresh common OCR and paired reader measurements

The current repo has no identified unseen panel with eligible frozen upstream
OCR. Freeze all eight sources offline, then produce common initial OCR
progressively: only N1/A1 and their paired reader calls first (six scheduled
POSTs); admit each remaining page's OCR and readers only after the screen passes.
Produce each admitted page's OCR once with the unchanged literal recipe/model,
preserving its real native receipts and lossless renders.
Both reader arms consume exactly those same artifacts. Source readers see only
the source image and their maintained instruction; never OCR output or gold.
Record upstream defects rather than fixing them to make reader agreement pass.

Run each fresh reader through the real review module, with real-driver resume
into the guarded builder path. Execute the clear pages as the two three-page groups;
run expected-hold pages separately so a correct hold cannot prevent unrelated
clear pages from reaching export. One provider arm must not consume the other's
reader result. No monkeypatch-only acceptance or cached subject response.

The opening screen and pairwise order must not add hidden reader calls. Offline
preflight must demonstrate pagewise review and safe driver resume using the same
immutable upstream/source identities: each scheduled reader observation is
generated once, then the positive group's three fresh page receipts feed its
actual builder run without reinference. Offline CLI proof must produce both
original three-page positive groups for both arms using that receipt topology,
with no manually forged lineage. All six clear pages remain required in the
live export denominator. A source-correct reader plus defective common OCR may
correctly hold, but leaves full-path qualification incomplete; do not omit that
page or redefine it as ineligible. If the real driver cannot consume that
topology with intact lineage, stop and revise the plan before paid execution;
do not quietly substitute callback-only proof or add a second batch of calls.
The batch reader-time gate sums those three page observations; separately
report final driver wall time, which is not a contiguous API batch latency.

Start with one clear page and one expected-hold page; both arms must clear their
per-page source/hold and receipt gates, and Argon must clear its per-page latency
gate, before expanding to the remaining six. Then, only if the complete
first panel clears quality and the provisional value/latency gates below,
repeat the four preselected page pairs once. These are repeatability observations
on now-exposed pages, not four more independent sources. No extra repeat may be
selected after seeing a favorable or slow response.

Pair by source and execution window, with provider order balanced and frozen
before calls. Initial order is N1, A1, N2, N3, R1, R2, R3, A2; Astra leads
N1, N3, R3 and A2, while Argon leads N2, R1, R2 and A1. Reverse each page's
provider order for repeats; run serially and avoid knowingly
overlapping this campaign with another campaign using the same account. Record
timestamps, retries, source size and cache usage. Account-wide contention and
provider queue conditions remain unmeasured. Do not change image resolution or
output limits to improve timing. Preserve native Argon 32,768 combined output
headroom and the maintained Astra 8,192 output allowance, medium reasoning,
original image detail, strict schema and `store:false`. Use zero SDK retries.
The common Astra OCR likewise uses 8,192 output tokens, medium/original and one
initial attempt per page. Keep the eight-page corpus within the validated input
envelopes; no truncation or output-limit reduction to fit the budget.

### C. Decision gates

| Gate | Required outcome |
| --- | --- |
| Access/transport | Exact native requested/served identities, valid terminal completion and output schema, complete raw receipt/usage and source binding |
| Source fidelity | Every clear cell, span and ownership relation exact; zero harmful or silent substitutions; both uncertainty cases explicitly held |
| Consumer behavior | Both original three-page clear groups export through the real verifier for each arm, with all six clear pages retained; source/OCR disagreement or uncertainty blocks qualified export and prevents full-path qualification; no provider spoof or bypass |
| Repeatability | All preselected repeat observations retain those same quality/hold outcomes; every attempted case remains in the denominator |
| Economics | At least 30% lower cold-normalized reader cost on the full panel and repeat subset, with total measured stage/path costs also reported; retain a useful margin at December Argon prices |
| Latency | Proposed new gate: each initial three-page positive reader stage ≤300 seconds, every attempted Argon reader page ≤180 seconds, and Argon summed reader time ≤1.5× matched Astra for each positive batch. Repeat subset must also stay within the per-page bound and ≤1.5× its paired Astra sum. No population-p95 claim |

The 180-second transport timeout exists in the owner code; the batch and relative
latency criteria above are newly proposed for approval, not an existing SLA.
Retain provider-native transport timeouts (Astra 180 seconds; the existing
Google nonstreaming wrapper allows up to 1,200 seconds). The 180-second Argon
acceptance limit is a separate performance gate: a complete later answer can be
source-scored but cannot pass latency or justify further paid expansion.
Record full transport/parse/recovery time and real-driver wall time separately.
A transport deadline breach fails operational latency even if source quality is
unmeasured; a later retry cannot erase it or unlock panel expansion/repeats.
This plan includes no diagnostic recovery after a failed latency gate. Preserve
all initial observations.

A valid source/consumer failure or a completed initial latency/value-gate failure
stops paid expansion. Preserve a better isolated
reader result separately if a common upstream OCR or incumbent defect prevents
full-path qualification. Do not silently replace the comparator, patch the gold,
rerun a semantic failure, weaken uncertainty handling or lower a threshold.
Operational failures have separate validity/reliability outcomes and retain
unknown cost reservations. Any incomplete or conflicting result retains the
current reader choice. Passing supports a bounded opt-in implementation
recommendation, not default activation or downstream acceptance.

## Budget and execution boundary

**Proposed additional hard inclusive ceiling: USD 3.** This includes all OCR,
reader, probe, retry and unknown exposure; no paid judge. Maximum planned native
inference attempts: eight common OCR + sixteen initial reader + eight conditional
repeat reader = 32, with at most one additional operational recovery (33 total).
Use the first scheduled requests as native qualification rather than adding
unnecessary probes. A known failed semantic answer has no retry allowance.

| Per-POST reservation | October USD | Basis |
| --- | ---: | --- |
| Common Astra OCR | 0.734600 | 26,000 bounded input × worst-case USD 12.50/M cache-write rate + 8,192 output × USD 50/M |
| Astra source reader | 1.500000 | Retain the maintained conservative source-reader bound; preflight proves its actual native payload fits |
| Argon source reader | 0.379680 | 26,000 bounded input × USD 2/M + 32,768 output/thinking × USD 10/M |

The 26,000 input ceiling is an admission condition, not a claim already proved
for uncreated fixtures. Preflight must bound each complete native prompt plus
actual image dimensions/tokenization using supported counting or a conservative
provider-specific calculation. If it cannot establish the bound, stop before
spending; do not infer image tokens from PNG byte size or shrink sources.
The ordinary cold OCR bound is USD 0.669600; reserve the larger USD 0.734600
unless the native contract proves the cache-write premium cannot apply. Astra's
USD 1.50 reader bound exceeds that envelope. Recheck exact
native settings, provider rates and any size-tier surcharge before first POST.
These reservations assume standard global service, with no Fast/priority,
regional or other paid modifier. If the actual route differs, recompute a
conservative reservation within the same USD 3 cap before admission.

Use rolling admission before each underlying POST: settled charges + unknown
exposure + in-flight reservations + next-call bound must fit USD 3 and the
original owner/campaign caps. Save locked reservation before exclusive request
creation and raw response before parsing; settle known usage before another
POST. Intercept both actual Astra and Google HTTP transports, including common
OCR. Unknown delivery/usage retains its full bound. One transient 502 or proven
harness repair can receive the single recovery attempt only if admission permits
and no semantic/latency stop has fired, with unchanged semantic request and
preserved original failure. Recovery cannot restore a failed latency gate. No
hidden SDK retries, automatic continuations or recovery after a semantic stop.

Twelve fresh readers per arm would cost about USD 0.87–0.89 if they repeated
prior small-fixture usage; this is a reader-only estimate. Eight new common OCR
calls have no representative cost estimate yet. The USD 3 ceiling admits each
planned call individually and is a bounded attempt, not a guarantee that all
future calls fit. Denied admission produces incomplete qualification and stops
spending; no automatic cap increase. Do not sum every future maximum as if all
serial calls were simultaneous liabilities.

Doc Web prior conservative exposure is USD 0.866677250; this proposal caps it at
**USD 3.866677250 / original 15**. Full campaign prior exposure USD 3.877369745
would be at most **USD 6.877369745 / original 35**. No spend transfer. Initial
and calibration ledgers stay closed; the new qualification has its own ledger.
Actual and cold-normalized costs are both reported. At December same-usage
rates, Argon's standard input/output prices double; require the 30% reader
saving gate then too. Recompute reservations if execution occurs after that
change. Provider invoices and agent/Codex use remain separate from usage-priced
benchmark charges.

Planning prices were checked against [Google pricing](https://ai.google.dev/gemini-api/docs/pricing)
and [OpenAI pricing](https://developers.openai.com/api/docs/pricing) on 2026-10-13.

No credentials are needed for this planning task. Later selected execution uses
the owner's configured Google/OpenAI access under its existing custody rules;
do not reuse the former BGI injection or change provider accounts. Public and
synthetic eligibility does not establish private-payload/ZDR eligibility.

## Research and applicability

The general problem is paired quality and latency qualification under variable
provider load. [NIST randomized blocking](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm)
supports holding nuisance conditions together while comparing treatments. Adapt
that by matching source/time windows, balancing order and reversing repeat order;
it reduces some confounding without measuring hidden provider queues.
[Google's evaluation guidance](https://cloud.google.com/blog/products/ai-machine-learning/how-to-evaluate-your-gen-ai-at-every-stage)
also distinguishes reference-based judgments and application-level evaluation.
Here deterministic literal/ownership comparison and independent source review
remain authoritative; no new paid automatic judge is proposed.

Plan validation checks matrix counts/order, reservation arithmetic and local
links. The native mock/driver acceptance tests above belong to execution and are
not claimed as completed by this planning task.

The continuing strategic reviewer judged the eight-source design proportionate
and requested three clarifications, now incorporated: progressive upstream OCR,
all six clear pages retained in both real export groups, and no recovery that
erases a latency stop. Opening provider order is balanced across the two screen
pages; initial and repeat sets are also balanced. Requested reviewer
configuration is GPT-6 Astra ultra; served agent identity was not independently
verified. This review is an execution-plan assessment, not source/capability or
runtime acceptance. [Offline plan validation](evidence/scout092-docweb-literal-plan-validation.json)
records the abstract matrix and exact arithmetic; no new fixture truth is claimed.

## Evidence to return

Owner story/attempt, source eligibility and frozen manifest; producing code and
request hashes; every raw OCR/reader receipt; complete request/driver timing;
accepted and held outputs; cold/actual and October/December costs; one inclusive
spend ledger; source-backed per-case verdicts and replayable evidence manifest.
Record configuration, transient failures, unmeasured cases and the actual
consumer boundary. No commit, push, deployment or default change is included.

Prior evidence: [initial campaign](scout-092-gemini4-argon-evaluation-routing.md),
[thinking calibration](scout-092-argon-thinking-levels.md),
[closed cumulative ledger](evidence/scout092-argon-thinking-reconciliation.json).


## Owner evidence and freshness

The read-only owner investigation found the campaign worktree and its local
`origin/main` at `91cd9bb19b174247349f1e83b9aaa869eb08ccc7`; primary checkout is
clean but older at `19b30b1d0db4a7f3b2e31614ba9846dfdb93355c`. Remote freshness
was not fetched during planning and remains an execution prerequisite.

- [Actual recipe](/Users/cam/.codex/worktrees/scout092-argon-docweb-20261013/configs/recipes/recipe-pdf-literal-tables-html.yaml:11)
- [Reader model restriction](/Users/cam/.codex/worktrees/scout092-argon-docweb-20261013/modules/common/table_source_review.py:22)
- [Independent bundle authority check](/Users/cam/.codex/worktrees/scout092-argon-docweb-20261013/modules/common/literal_fidelity_bundle.py:34)
- [Adapter hold exit](/Users/cam/.codex/worktrees/scout092-argon-docweb-20261013/modules/adapter/literal_table_review_v1/main.py:48)
- [Existing fixtures are exposed](/Users/cam/.codex/worktrees/scout092-argon-docweb-20261013/docs/stories/story-245-preserve-literal-table-text.md:358)

No owner files or fixtures were changed by this planning task. Implementation,
independent source authoring, live comparisons and real-driver acceptance remain
part of the proposed execution. A later approval authorizes that bounded work,
while activation, landing and downstream rollout remain separate.
