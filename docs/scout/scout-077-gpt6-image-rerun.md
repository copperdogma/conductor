# Scout 077 — GPT-6 Sol and Luna image rerun

Date: 2026-09-27. Status: complete; fresh owner decisions recorded, no production changes.

Cam explicitly requested rerunning image-processing tasks after a reported OpenAI fix. The [official API changelog](https://developers.openai.com/api/docs/changelog) confirms a September 25 image-encoding correction for `gpt-6-sol` and `gpt-6-luna`, affecting image understanding in API and Codex. It recommends rerunning affected evaluations. Our prior September 26 calls postdate the notice: these fresh calls are replication evidence, not a controlled before/after measurement of the fix. Backend rollout identity is unavailable.

## Frozen scope and controls

Three owner-local workers use isolated current-main worktrees, maintained image fixtures, prompts and scorers; fresh incumbent calls; public/synthetic inputs; native direct providers; saved raw responses before parsing; per-request reservations including judges/recovery; and no implicit retries. Only explicitly selected offline checks may run with provider access disabled. No runtime defaults, deployments, commits or pushes are authorized by this rerun.

| Owner | Maintained image lane | New-run ceiling USD |
| --- | --- | ---: |
| Doc Web | 13-case crop detection, independent page safety, actual page-12 crop geometry | 2.50 |
| CineForge | Six ordered-frame cases with corrected v4 source truth | 1.50 |
| Storybook | FS001 photo understanding and FS006 scan/OCR | 1.00 |

Total ceiling USD5.00, disclosed before inference. This is separate from the closed Scout076 accounting and does not reopen its billing investigation. Exact checkpoint IDs are `gpt-6-sol` and `gpt-6-luna`; owner receipts record reasoning, image detail, comparator, code identity and actual usage. Standard <=272K prompt pricing verified from official model pages: Sol USD2 input/0.20 cached read/2.50 cache write/10 output per MTok; Luna USD0.10/0.01/0.125/0.50 respectively.

[Prior campaign](scout-076-gpt6-sol-luna-evaluation-routing.md) remains intact. Dossier and Echo Forge maintained selected lanes are text-only. Robo Rally has no maintained model inference benchmark. Board Game Ingester has image tasks but its current Robo Rally scans still lack established public/synthetic upload eligibility; the Tideglass package contract fixture is not a visual evaluation corpus. No private scan upload is inferred from this request.

## Results

**Recommendation:** use Luna for inspected CineForge frame analysis; recognize Sol as the fresh Doc Web detector-quality leader and a useful human-selected CineForge scale-check reference. Retain Storybook Gemini photo/OCR and Doc Web runtime configuration. Neither candidate qualifies for autonomous visual QA or page-safety approval. These are distinct task decisions, not a blanket model ranking.

All selected lanes reached a decision. Total usage-derived accounting **USD0.944566325 / USD5.00** across 122 paid calls (including probes, controls, judges and recovery); no unresolved reservations. This is token-based accounting, not provider-invoice reconciliation. The evaluation changed no runtime defaults or deployment. Cam subsequently approved scoped commits and pushes; landing is tracked below. Board Game Ingester remains deferred for eligible visual fixtures; it was not evaluated.

| Owner/task | Winner and practical decision |
| --- | --- |
| CineForge inspected frames | Luna value winner: six of six wins over Gemini, about 5x cheaper. Sol higher aggregate and observed scale-change advantage, but 17.4x Luna cost. |
| Doc Web detector | Sol quality leader (.992731); Luna value leader (.987162 at 10.1x lower cost than Gemini). Neither alone establishes publication-ready crops. |
| Doc Web page safety | Keep maintained GPT-5.5 auto-detail route: both candidates false-safe on the portrait case; fresh configured control rejects it. |
| Storybook photo/OCR | Keep Gemini: correct note transcription across all three, fastest/cheapest control; literal photo assertion gains do not establish a semantic adoption win. |

Fresh responses differ from the prior run, but the dated notice and declared contract differences prevent attributing those differences to the fix. Small fixture counts also limit confidence. No unchanged repeat is recommended.

### Storybook — complete; retain Gemini for photo/OCR

[Attempt173](/Users/cam/.codex/worktrees/storybook-gpt6-image-rerun-20260927/docs/evals/attempts/173-story056-gpt6-image-fresh-rerun.md), base `9eafe535c00239d774ba303e39b0ea75efeb9987`. One fresh sample per task/model (six calls), synthetic FS001/FS006, maintained prompt and scorer. OpenAI none reasoning/high image detail/1024 output uses strict owner-schema JSON; previous attempts used JSON-object mode, so the changed response constraint prevents treating this as an otherwise identical longitudinal experiment. Gemini uses the unchanged production adapter. All six returned terminal valid owner-schema responses; no retries or paid judges.

| Task | Sol checks / ms / USD | Luna checks / ms / USD | Gemini checks / ms / USD |
| --- | --- | --- | --- |
| Photo | 9/9 / 7208 / .007371 | 8/9 / 2901 / .000365050 | 7/9 / 2241 / .000185400 |
| Scan/OCR | 10/11 / 5741 / .007423500 | 10/11 / 3508 / .000362675 | 11/11 / 2520 / .000158600 |

Sol wins the literal photo assertions, but exceeds both owner limits (USD.001 and 5s) on both tasks. Luna no longer invents a cake/candle in the illustration. Its and Gemini's photo misses concern where keywords occur; all three transcribe the scanned note accurately. OCR differences likewise reflect lexical field placement, while Gemini's unsupported “handwritten” description escapes the matcher. Therefore Sol's numerical photo lead is not a demonstrated adoption-grade semantic win, and Luna offers no measured OCR advantage at roughly twice Gemini's cost and slower latency. Keep Gemini for these calls; this does not alter the separate deployed Luna persona decision. Native OpenAI production-adapter parity and broad reliability remain unmeasured.

Usage-priced total USD0.015866225; unknown/pending reservations zero. Owner's targeted offline validation, lint, methodology checks and evidence checks passed. Raw artifacts and dispatch source preserved; no runtime/default/deployment changes or commits.

### CineForge — complete; Luna value win, Sol narrow scale-check benefit

[Attempt044](/Users/cam/Documents/Projects/cine-forge-gpt6-image-rerun-20260927/docs/evals/attempts/044-gpt6-image-fresh-v4-rerun.md), base `f4a0decd9b89a18756bfcf4a78b44fba5e71e58d`. Six fresh synthetic ordered-frame cases per model plus 18 independent Opus rubric judgments (36 calls total); frozen v4 source truth and high image detail. Raw results: [fresh matrix](/Users/cam/Documents/Projects/cine-forge-gpt6-image-rerun-20260927/benchmarks/results/video-understanding-gpt6-image-rerun-20260927.json). Both candidates beat fresh Gemini on the combined mean; Luna wins all six paired cases against Gemini again.

| Model | Combined mean | Deterministic mean | Rubric mean | Mean subject ms | Mean subject USD |
| --- | ---: | ---: | ---: | ---: | ---: |
| Sol | .6080 | .5994 | .6167 | 7221 | .0095235 |
| Luna | .5902 | .6138 | .5667 | 3876 | .000546342 |
| Gemini | .3861 | .3922 | .3800 | 2637 | .002731483 |

**Recommend Luna for inspected headless frame analysis.** It costs about one-fifth of Gemini and wins all six comparisons, though it is slower. Sol wins four of six against Luna and detects dialogue body enlargement missed by Luna/Gemini, but the small aggregate gain (.0178) costs 17.4 times as much, takes longer, and partly depends on ambiguous tone judgments. Sol is a useful human-selected scale-check reference; one observed example does not validate an automatic subset router. Luna better describes the rooftop rise and descent; Sol misses that arc, while Gemini invents camera tracking. All three call a red-to-blue prop change consistent, disqualifying autonomous continuity approval. All combined case scores remain below .80. Sol has one assertion-level pass, which is distinct from the combined gate.

There is no current product frame-analysis call to replace. This result does not evaluate ScriptBible. Total usage-derived cost USD.50574295: subjects .07680795, judges .428935. All 36 responses terminal, no retries, no unknown reservations. No new subject calls for judge or rubric repair.

CineForge validation: 44 targeted checks with sockets disabled, frozen truth/media verification, scoped Ruff, all 36 settled receipts and cap-rejection checks, registry/methodology and diff checks passed. The exact call-time runner is archived separately from style-only postrun cleanup.

### Doc Web — complete; Sol detector-quality win, no runtime promotion

[Attempt044](/Users/cam/Documents/Projects/doc-web-gpt6-image-rerun-20260927/docs/evals/attempts/044-gpt6-image-fix-rerun.md), owner base `ed70d32205004bb6117780529684f68396c8a750`, isolated `/Users/cam/Documents/Projects/doc-web-gpt6-image-rerun-20260927`. Thirteen fresh detector cases per model all pass. Detector settings preserve medium reasoning/high image detail for OpenAI.

| Model | Detector mean | Mean latency ms | 13-case subject cost USD |
| --- | ---: | ---: | ---: |
| Sol | .992731 | 4096 | .110803000 |
| Luna | .987162 | 3087 | .005787150 |
| Gemini | .962615 | 7447 | .058284500 |

Sol leads detector quality, including an actual page12 output with a complete seal and separate signature boxes. Luna is faster and about 10.1x cheaper than Gemini, but its actual raw composite still clips the seal. Root and owner inspected the delivered [Sol crop sheet](/Users/cam/Documents/Projects/doc-web-gpt6-image-rerun-20260927/docs/evals/evidence/044-sol-page12-crops.jpg), [Luna crop sheet](/Users/cam/Documents/Projects/doc-web-gpt6-image-rerun-20260927/docs/evals/evidence/044-luna-page12-crops.jpg), and owner-reviewed [Gemini sheet](/Users/cam/Documents/Projects/doc-web-gpt6-image-rerun-20260927/docs/evals/evidence/044-gemini-page12-crops.jpg): Sol retains printed officer labels and neighboring caption text; Luna retains labels and loses seal content; Gemini falls back to CV after an ambiguous no-caption array is rejected, combines the signatures, and retains printed labels. **No arm establishes publication-ready crops on this regression.** Keeping the current runtime is a no-promotion decision, not a claim that its fresh crop output passed.

Independent page safety: Sol stops on a source-confirmed false-safe screen. Luna's initial screen rejects the page for the wrong explanation, then its full matrix scores21/22 and falsely accepts the same neighboring-portrait case. Fresh GPT-5.5 with the maintained automatic image-detail setting correctly rejects it. A separate high-detail GPT-5.5 diagnostic falsely accepts it; both are retained, and only the maintained configuration serves as control. No full22-case incumbent superiority is claimed. Do not replace page safety with either candidate.

A loader basename mismatch was repaired before paid runtime inference. The 400-token caption allowance caused truncation; one predeclared symmetric8192-token recovery completed for all three. It reused exact saved detector envelopes with hash-verified replay (three zero-cost replays), dispatching only three new caption calls. No geometry, scorer or prompt tuning, and no duplicated paid detector requests. All80 paid requests are accounted: **USD0.422957150 / USD2.50**, pending/unknown reservations zero.

Doc Web validation: 33 focused provider-free tests plus two exact-replay/rejection checks, scoped Ruff, methodology and whitespace checks passed. No production module changed. Maintained Gemini detector ambiguity is an adapter/fallback outcome, not a semantic model rejection.

## Closure and next action

The three owner receipts preserve source/code identity, raw responses, fresh control results, costs and focused offline validation. The coordinator reused that validation and independently inspected decisive Doc Web crops rather than rerunning the suites. This campaign stays separate from Scout076's closed billing exceptions and text-model decisions.

No more same-slice evaluations are needed. Cam approved scoped evidence and harness closeout across the four worktrees on September27. Current defaults remain unchanged. Broader image corpora or product integrations would be distinct future work.

Coordinator validation: `make lint`, `make methodology-check`, and `git diff --check` pass. Owner decision numbers were reconciled against their receipts and the closed Doc Web ledger (80 calls plus three zero-cost replays).

## Approved landing — 2026-09-27

Preflight covers all four repositories before the first push. Owner code checks are reused where tested inputs remain unchanged; changed evidence and generated records are checked directly. No paid evaluation, production smoke or deployment is part of closeout. Primary checkouts and retained ignored run artifacts remain untouched. Reviewed primary Conductor inbox capture is already represented on current main; stale campaign status is not copied back over newer closure records.

All four preflights passed before the first push. No integration, required review or CI blocker was found. Owner execution branches and remote main were fast-forwarded without force and verified by fresh remote refs:

| Repository | Verified remote-main commit | Closeout validation |
| --- | --- | --- |
| Storybook | [`b943df960fe4430257b58d3a6ca30ec7710fe6c1`](https://github.com/copperdogma/storybook/commit/b943df960fe4430257b58d3a6ca30ec7710fe6c1) | Changed runner offline checks and lint; artifact hashes, ledger, privacy/methodology records |
| CineForge | [`a3ac35743c94e253e0406fafe6ee4964a0330bf3`](https://github.com/copperdogma/cine-forge/commit/a3ac35743c94e253e0406fafe6ee4964a0330bf3) | Reused44 unchanged offline tests; fresh no-ledger redispatch rejection,36 receipt hashes, lint and methodology |
| Doc Web | [`747b3764005189bdd493356fb1c512ce93aa11ea`](https://github.com/copperdogma/doc-web/commit/747b3764005189bdd493356fb1c512ce93aa11ea) | Reused33+2 offline checks; fresh253-file reconstruction including all236 original manifest members and67 exact-base references; lint and methodology |

Conductor's four-file supervisor record is based on `6166b9c4b8fb629605f173ddc1695d8e07c19efd`; documentation links, lint, methodology and staged whitespace checks pass. Owner changes landed before this completion record.

Scoped closeout fixes preserve the original measured results: Storybook rejects mismatched served identity before price settlement and enforces reserved model/fixture slots; CineForge prevents redispatch of the completed run even when a fresh clone lacks the ignored ledger. Native receipts are retained in Git rather than relying on local ignored files. Doc Web's original pre-format guard bytes were not separately snapshotted: original hashes, normalized AST identity and final source are retained, so exact byte-for-byte recovery of that formatting-only version is unavailable. This provenance limit is explicit and does not turn a later source snapshot into the original bytes.

Doc Web's lossless payload-deduplicated bundle is76,832,188bytes, split into two files below50MiB; all80 request/response pairs reconstruct byte-for-byte. Only task-owned intermediate packaging was replaced. All task worktrees and valuable ignored artifacts are retained; unrelated primary work remains untouched. No additional provider calls, runtime defaults or deployments occurred during closeout. This evaluation campaign is complete; no follow-up is required.
