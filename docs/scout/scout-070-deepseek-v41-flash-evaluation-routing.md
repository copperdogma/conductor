# Scout 070 — DeepSeek V4.1 Flash Evaluation Routing

Date: 2026-09-12; completed 2026-09-13. Status: All selected evaluations complete with rejection verdicts; retry automation paused.

The proposal and dated execution entries below preserve what was known and
authorized at each stage. Final outcomes appear under Heartbeat3; check-in
authorization and landing evidence follow that entry.

## Identity and route

The [September 10 release](https://api-docs.deepseek.com/news/news260910/) and
[pricing](https://api-docs.deepseek.com/quick_start/pricing/) verify direct
`deepseek-flash` as DeepSeek-V4.1-Flash, a new checkpoint absent from the evaluated
ledger. Text/image input, text output, 1M context, up to 384K output; Chat
Completions, Responses and Anthropic compatibility, JSON output and tools.
Direct base: `https://api.deepseek.com`. Per-million direct prices: off-peak
$0.15 input / $0.60 output / $0.003 cached input; peak twice those prices.
[Thinking controls](https://api-docs.deepseek.com/guides/thinking_mode/) expose
enabled/disabled and low/high/max, default high. Freeze one provider-valid arm
before scoring; prefer explicitly supported nonthinking for interactive lanes.

Proposed OpenRouter Chat Completions endpoint:
`https://openrouter.ai/api/v1/chat/completions`, request
`deepseek/deepseek-v4.1-flash`, pinned `deepinfra/fp8`.
[Public endpoint metadata](https://openrouter.ai/api/v1/models/deepseek/deepseek-v4.1-flash/endpoints)
attributes this to `deepseek/deepseek-v4.1-flash-20260910`, with 1,048,576 context,
131,072 output, $0.20/M input, $0.60/M output, $0.006/M cache reads; strict
outputs and required/named tools advertised. Pinning matters because endpoint
contracts and prices differ. These are metadata claims, not served-identity or
strict-enforcement proof. **Announced/API-listed: yes; access: unverified.**

Direct old Flash/Vision Exp aliases now serve V4.1; do not rewrite historical
attempts or infer old router IDs changed. Release/pricing pages conflict about
Pro's September 14 transition; avoid Pro aliases. New V4.1 is not a rerun of
the old Flash 0731, Pro 0813 or Vision Exp evaluations.

## Execution boundary

[DeepInfra policy](https://docs.deepinfra.com/account/data-privacy) says ordinary
inference is in memory and not used for training, but permits limited debugging/
security content logging. End-to-end router/account retention is unverified.
Public/synthetic owner fixtures only, accepting residual logging uncertainty;
no unconditional ZDR claim, private/licensed-restricted payloads or account changes.
Stricter owner policy controls. All caps include probes, diagnostics/retries,
controls and judges. No credentials, authenticated calls or target mutations so far.

After selection: isolated current-remote-base owner worktrees; exact identity,
terminal native contract and harness parity before scoring; offline resolved
prompt/case/judge topology preflight before multi-case spend. Freeze prompts,
goldens and scorers, disallow model substitution, reserve conservative per-call
cost within cap. Safe transport diagnostics cannot establish production parity.
No defaults, commits, pushes or deployment authorized.

## Numbered proposal

1. **Doc Web — Evaluate now; US$0.50.** `image-crop-extraction`, maintained
   `conservative-count`: synthetic strict vision/parity then Image011 seal/
   signature grouping. Stop on failure; otherwise 13-case detector, requiring
   13/13, overall >=0.95, zero transport/schema errors. Fresh incumbent
   `gemini-3-flash-preview` follows only after qualification and budget preflight;
   maintained reference 13/13, 0.9703. Native vision and price offer crop-quality/
   value headroom. Public owner-identified images only. Detector-only: separate
   GPT-5.5 page-context safety remains unselected/unmeasured.
2. **Storybook — Evaluate now; US$0.30.** Current repaired `luna-persona`
   topology: one isolated warmth case, four-case single-turn slice, remaining
   multi-turn evidence and fresh `claude-haiku-4-5-20251001` only after prior
   gates pass. Require all maintained assertions, 1.0 pass rate, <=5 seconds,
   <=$0.01 per turn and no reasoning leakage. Incumbent 10/12 leaves quality
   headroom; low Flash pricing makes interactive value plausible. All 12 turns
   are repo-authored synthetic. Preserve production prompt parity and corrected
   conversation grouping. No clearance for real family material.
3. **Echo Forge — Evaluate now; US$0.10.** `scene-to-soundscape-golden`:
   strict version-3 contract, Tavern then Dungeon; stop at first hard miss.
   Require 2/2, <=5 seconds and <=$0.01 per fixture; fresh `gpt-5.4-mini` only
   after candidate clears both. Old Flash was cheap/fast but 0/2 semantically;
   a new checkpoint warrants this tiny screen. Public/synthetic only; no real
   user/campaign material or 34-case expansion.

**Campaign maximum: US$0.90. Actual spend: US$0.00.**

## Not recommended now

- **Dossier — Defer.** C1/C3 deletion requires Mariner/Big Fish whose provider
  eligibility is unclear; only the tiny synthetic control is clearly eligible.
- **CineForge — Defer.** Muse/Astra accurate paraphrases hit an unresolved
  ScriptBible lexical evidence gate. Resolve the owner evidence-form contract
  from frozen outputs before another text run. Frame QA is a separate possible lane.
- **Board Game Ingester — Defer.** Vision could help orientation, but current
  private/protected scans lack external upload eligibility and a VLM subject adapter.
- **Robo Rally — Defer.** Deterministic scenarios exist; model rules extraction
  lacks a ready frozen contract and eligible source artifacts.
- **Conductor — Do not evaluate.** Routing owner, not a duplicate product harness.

## Current owner evidence

All seven registered owner instruction/Ideal/spec and relevant eval surfaces
were inspected read-only. Primary checkouts can lag owner worktrees; recheck
current bases/contracts before spend and surface material scope changes.

- Doc Web registry and Qwen Attempt035 under
  `/Users/cam/.codex/worktrees/qwen38-max-0902-20260906/doc-web/docs/evals/attempts/`;
  Scout068 preserves Image011/public-input and downstream-safety boundaries.
- Storybook Attempt140 and current registry under
  `/Users/cam/.codex/worktrees/gpt6-astra-20260905/storybook/docs/evals/` preserve
  repaired isolated progression, synthetic provenance and current incumbent.
- Echo Forge registry and September 3 decision under
  `/Users/cam/.codex/worktrees/gemini-38-flash-20260903/echo-forge/docs/evals/attempts/scene-to-soundscape-golden/`.
- CineForge registry and Scout064/067 owner follow-through preserve repeated
  scorer ambiguity; synthetic Open Frequency alone does not resolve it.
- Dossier registry C1/C3 and Story105; Board Game Ingester registry/Stories015–016;
  Robo Rally spec, root-private-race registry prerequisites and source policy.

No evaluated-ledger update until an approved attempt. No revival of the cancelled
DeepSeek Vision retry schedule. Existing model-watch edits remain untouched.

## 2026-09-12 approved execution

Cam replied `yes`, selecting items 1–3: Doc Web $0.50, Storybook $0.30,
Echo Forge $0.10, total $0.90. Three isolated owner workers were dispatched
before any root provider call. Central OpenRouter credential presence and vault
permissions were checked by name only through the custody helper.

At 16:45 UTC, refreshed public endpoint metadata changed DeepInfra FP8 status
from 0 to -2, with unchanged pricing/schema metadata. Owners were notified to
classify the pinned route using bounded native qualification; no unapproved
provider fallback or semantic scoring of access errors.

### Owner results

All four native requests (one Doc Web, two Storybook, one Echo Forge) returned
HTTP 429 with `engine_overloaded` and `upstream_provider_shared_pool` from
DeepInfra. No terminal model answer or usage was returned. Root inspected the
raw/sanitized error envelopes and owner evidence. Catalog attribution does not
prove served checkpoint identity. No other provider was substituted.

| Owner | Base SHA | Native requests | Reported generation spend | Conservative unreconciled exposure / cap |
| --- | --- | ---: | ---: | ---: |
| Doc Web | `5e2de62842f3e15313bdb74d9d41b84b40abec96` | 1, 737 ms | $0 | $0.0106144 / $0.50 |
| Storybook | `42be9acccebb6a00bc5395d226c8dc5e17c1aa18` | 2, 364 and 358 ms | $0 | $0.0020000 / $0.30 |
| Echo Forge | `ede96d83cf65ee4bec1b386e6fdb9ffff85b9372` | 1, 499 ms | $0 | $0.0046892 / $0.10 |

Total reported generation spend is **$0**; billing was not independently
reconciled. Conservative aggregate possible exposure is **$0.0173036**, below
the approved **$0.90**. Rejection latency is not inference performance.

Each owner uses branch `codex/deepseek-v41-flash-eval-20260912` in its own repo,
under `/Users/cam/.codex/worktrees/deepseek-v41-flash-20260912/`:

- `doc-web`: Attempt036 and Story207, plus budgeted native-probe/harness scaffold.
- `storybook`: Attempt148, Story166, registry and artifact/privacy manifests.
- `echo-forge`: `20260912-openrouter-deepseek-v41-flash-decision.md`, Story069,
  registry and attempt directory under `docs/evals/attempts/scene-to-soundscape-golden/`.

Layered verdict for all three: access constrained by shared-pool capacity;
production transport unqualified; request availability failed in this sample;
model semantic reliability/capability and inference economics unmeasured;
adoption **defer**. Image011/full detector, Luna warmth/all persona cases,
Tavern/Dungeon and all fresh incumbents/judges remain unmeasured.

The exact route should be revisited only after dated owner inference evidence
of recovery, an explicit fresh access request, or a separately selected revised
provider proposal. A catalog status change alone is not proof of recovery.
No automatic retry schedule was created or revived. Owner work remains
uncommitted; no primary checkout or runtime defaults changed.

### Closeout validation and custody

Follow-up authorization: Cam requested fresh retries every six hours until
completion or 30 hours elapsed. Heartbeat `retry-deepseek-v4-1-evaluations`
was created ACTIVE, attached to this task, with hard deadline
**2026-09-13 23:54:06 UTC** (17:54:06 America/Edmonton). This supersedes the
earlier no-schedule state and explicitly permits bounded fresh access attempts.
Original cumulative owner/campaign caps and unresolved exposure remain in force.
One native probe per pending owner per wake; on recovery continue its approved
progressive lane. Completed owner verdicts are not rerun. Pause on all-owner
completion, deadline, exhausted budget or missing new authority. Stay quiet on
unchanged capacity errors; notify meaningful progress or final stop. This is a
new finite V4.1 campaign schedule, not revival of the cancelled Vision Exp watch.

Doc Web passed 20 offline adapter/budget-guard tests; Echo Forge passed 55
strict-transport/provenance tests and the expected 2/2 fixture check. Storybook
passed syntax, privacy coverage and artifact/source-manifest checks. Each owner
passed methodology consistency and diff checks. Root independently checked raw/
source hashes and sizes plus all three temporary-variable absences:
`DOC_WEB_OPENROUTER_API_KEY`, `OPENROUTER_API_KEY`,
`ECHO_FORGE_OPENROUTER_KEY`. Existing owner credentials were not removed.

Raw errors are retained in durable ignored owner storage; tracked manifests
contain hashes, sizes, code identity and reproduction commands. Post-run budget
or storage hardening is labeled separately from the code that made each request.
No provider calls were repeated to validate those offline repairs.

Direct owner records:

- [Doc Web Attempt036](/Users/cam/.codex/worktrees/deepseek-v41-flash-20260912/doc-web/docs/evals/attempts/036-deepseek-v41-flash-evaluate-model.md)
- [Storybook Attempt148](/Users/cam/.codex/worktrees/deepseek-v41-flash-20260912/storybook/docs/evals/attempts/148-luna-persona-deepseek-v41-flash-access.md)
- [Echo Forge attempt](/Users/cam/.codex/worktrees/deepseek-v41-flash-20260912/echo-forge/docs/evals/attempts/scene-to-soundscape-golden/20260912-openrouter-deepseek-v41-flash.md)

## Heartbeat1 — 2026-09-12 23:55 UTC onward

Explicit six-hour retry authorization was exercised once per pending owner at
its failed native gate, with fresh immutable artifacts in the preserved isolated
worktrees. Bases and pinned model/provider are unchanged. Catalog status had
recovered to 0 at unchanged pricing; actual owner evidence differed by request.

- **Doc Web — completed; do not adopt the frozen detector.** Native synthetic
  strict vision and identical-input harness parity succeeded on exact public
  model ID and DeepInfra, 12,516/12,460 ms, $0.000526/$0.000358368. The first
  maintained Image011 case returned valid strict output but scored **0.5551,
  0/1**, with zero transport/schema errors. It correctly grouped two regions
  but placed incorrect boxes: logo `[.35,.03,.65,.14]` and combined seal/signatures
  `[.12,.72,.82,.94]`, against source-backed goldens ending at `.231061` for the
  logo and spanning `[.119804,.686061,.876863,.896667]` for the combined region.
  Owner and coordinator visually inspected the source; the logo is cut off and
  lower content undercovered. Maintained-case latency 67,804 ms, cost $0.0018894.
  Full detector, fresh incumbent and page-context remain unmeasured. This is a
  semantic rejection, not a reason to retry the same configuration.
- **Echo Forge — completed; operationally reject the frozen route/configuration.**
  Native strict synthetic owner schema returned exact public ID and DeepInfra
  in **55,375 ms**, $0.0013294. A narrow source-backed mapping of pinned endpoint
  slug to returned display name repaired owner validation offline; wrong model,
  provider and alternative endpoint tags still fail. Identical-input harness
  parity then hit its **60-second abort limit** without a complete envelope
  (exact elapsed finish time was not captured). Native
  schema qualified; harness parity remains unqualified. Repeated contract-path
  latency is unsuitable for the five-second interactive lane; Tavern, Dungeon,
  incumbent and semantic capability remain unmeasured. Do not rerun on future wakes.
- **Storybook — pending.** Its one new native request returned the same 429
  `engine_overloaded` / `upstream_provider_shared_pool` in **401 ms**. No output,
  usage, persona, harness or judge calls. Keep only this owner eligible for the
  next scheduled fresh access probe, before the existing hard deadline.

### Cumulative accounting after heartbeat1

| Owner | Reported generation spend | Unreconciled maximum | Total accounted upper bound | Cap | Scheduled state |
| --- | ---: | ---: | ---: | ---: | --- |
| Doc Web | $0.002773768 | $0.0106144 | $0.013388168 | $0.50 | Completed, never rerun unchanged |
| Storybook | $0 | $0.0030000 | $0.0030000 | $0.30 | Pending capacity |
| Echo Forge | $0.0013294 | $0.0093784 | $0.0107078 | $0.10 | Completed operational rejection |
| **Total** | **$0.004103168** | **$0.0229928** | **$0.027095968** | **$0.90** | Storybook only remains |

Unreconciled amounts retain initial no-usage 429 reservations and Echo's new
timeout reservation; they are not claimed as actual charges. No budgets reset.
Temporary owner credentials were removed after each stop. Original evidence is
unchanged; new source snapshots distinguish executed code from offline repairs.
Owner attempts/registries/story records contain new raw/source hashes and commands.
No commits, defaults, provider fallback, private fixtures or new scopes.
Coordinator verified heartbeat source/raw manifest hashes and credential cleanup.
Doc Web passed 20 offline tests; Echo's narrow endpoint-name repair passed 56,
including wrong model/provider/endpoint rejection. Storybook syntax/privacy/
methodology checks passed; all owner diff checks passed. The automation remains
ACTIVE at six-hour cadence with its prompt updated to **Storybook only**, the
unchanged hard deadline, and the cumulative amounts above.

## Heartbeat2 — 2026-09-13 05:57 UTC

Only Storybook retried. One fresh native request at 05:57:57.712 UTC returned
HTTP429 `engine_overloaded` / shared pool in 472 ms. No output/usage, rapid
retry, harness, persona or judge calls. Doc Web and Echo were not called.
Storybook stays pending; capability remains unmeasured and adoption deferred.

Storybook reported spend remains $0; cumulative unreconciled maximum is now
**$0.004/$0.30**. Campaign reported spend remains **$0.004103168**;
unreconciled exposure **$0.0239928**, combined bound **$0.028095968/$0.90**.
No invoice reconciliation or cap reset. Updated Attempt148/manifest, registry
and Story166 retain immutable heartbeat2 raw and executed-source evidence.
Owner syntax/privacy/methodology/diff checks passed; coordinator independently
verified manifest hashes/sizes and temporary credential absence. No defaults,
commits, provider changes or private inputs. Automation remains active for
Storybook only on the existing six-hour cadence and hard deadline.

## Heartbeat3 — 2026-09-13 11:57 UTC; campaign complete

Only Storybook was called. Its tiny native probe recovered: terminal exact public
model alias and DeepInfra, `API_OK`, 6,047 ms, 10 input/3 output/0 reasoning tokens,
$0.0000038. The dated checkpoint remains catalog-attributed, not response-echoed.

The owner then continued into the approved production-shaped warmth request.
Production prompt parity verified byte-for-byte (10,197 bytes). The maintained
synthetic warmth input returned terminal valid text in **29,210 ms**, with
2,152 input/17 output/0 reasoning tokens and **$0.0004406**. The response was
warm, contained an emoji/follow-up and no reasoning leakage, but was not scored
by the maintained judge. The coordinator inspected its complete retained output,
exact identity, finish reason, latency and reported usage/cost.

**Storybook completed: operationally reject the frozen route/configuration.**
Latency was 5.842 times the five-second hard gate. Native text transport now
qualifies; harness parity, semantic judge scores, remaining persona cases and
fresh incumbent remain unmeasured. No semantic inferiority claim. Combined with
the earlier capacity errors, this does not justify an interactive default change.
No more Storybook retries are authorized by this completed schedule.

| Owner | Reported generation spend | Unreconciled upper bound | Combined maximum / original cap |
| --- | ---: | ---: | ---: |
| Doc Web | $0.002773768 | $0.0106144 | $0.013388168 / $0.50 |
| Storybook | $0.0004444 | $0.0040000 | $0.0044444 / $0.30 |
| Echo Forge | $0.0013294 | $0.0093784 | $0.0107078 / $0.10 |
| **Campaign** | **$0.004547568** | **$0.0239928** | **$0.028540368 / $0.90** |

No billing reconciliation claimed. Earlier no-usage and timeout reservations
remain included; budgets were never reset. All owners completed progressive
stops, not broad benchmarks or adoption. Their exact worktrees/bases and artifact
links above remain authoritative; uncommitted work is preserved.

Storybook's Attempt148, registry, Story166 and manifest include exact executed
source/prompt/fixture hashes, reservations, raw envelopes and commands. Owner
syntax/privacy/methodology/diff checks passed; coordinator verified raw/source
hashes, sizes and temporary credential absence. No defaults, commits, pushes,
private payloads, fallback providers or account settings changed.

Automation `retry-deepseek-v4-1-evaluations` was set **PAUSED** after the last
owner completed, before the hard deadline. No further scheduled calls will run.
Reopening any frozen arm requires materially changed relevant model/route/owner
contract evidence and a new selection; completed rejects are not retry targets.


## Check-in — 2026-09-13

Cam explicitly authorized scoped check-in and push after campaign completion.
The evaluation is complete; repository landing is partial because Echo Forge's
required full test suite remains red. No new provider calls were made.

| Owner | Landing | Validation |
| --- | --- | --- |
| Doc Web | [main at bb3c6ff](https://github.com/copperdogma/doc-web/commit/bb3c6ffaaa9163a831635ffee5429be9debfcd01); [published Attempt036](https://github.com/copperdogma/doc-web/blob/bb3c6ffaaa9163a831635ffee5429be9debfcd01/docs/evals/attempts/036-deepseek-v41-flash-evaluate-model.md) | 968 tests passed; lint, methodology, manifest and diff checks passed. Attempt036 closed; Story207's prior Done status retained. |
| Storybook | [main at 1699050](https://github.com/copperdogma/storybook/commit/16990502a99a0804edb950f93253ef81c28c45fe); [published Attempt148](https://github.com/copperdogma/storybook/blob/16990502a99a0804edb950f93253ef81c28c45fe/docs/evals/attempts/148-luna-persona-deepseek-v41-flash-access.md) | Shared 38, frontend 201 and backend 1499 tests passed initially; missing-runtime failures resolved by installing the existing pinned Dossier runtime, then all five affected files passed (25 + 18 tests). Fresh typecheck, lint, methodology, focused runner and provenance/privacy checks passed. Story166 closed. |
| Echo Forge | Not committed or pushed; scoped changes and evidence retained in the campaign worktree above | Typecheck, lint and 56 focused tests passed. Full suite: 524 passed, 5 App failures. Serial App rerun: 127 passed, 4 failed. All four named playback tests passed individually, indicating suite-sensitive failures; the required full-suite gate remains failed. |

Storybook validation used a uniquely named disposable database with the existing
migrations; it was removed afterward. No live database schema was changed.
Echo's owner check-in skill requires stopping before landing on failed validation;
no broader App fixes or relaxed test thresholds were introduced for this campaign.
Its evaluation rejection remains final even though code/evidence landing is blocked.

Owner landings used isolated fast-forward checkouts and verified remote main SHAs.
Primary checkouts and unrelated changes were preserved. Conductor's allowlist is
this scout, its index, the evaluated-model ledger and campaign changelog entry;
unrelated daily model-watch work is excluded. Conductor methodology, lint and
diff checks passed. Worktrees and ignored raw evaluation artifacts are retained.
