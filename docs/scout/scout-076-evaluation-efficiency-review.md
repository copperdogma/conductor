# GPT-6 Sol/Luna campaign efficiency review

Date: 2026-09-26
Status: Measured orchestration review; delivery closeout tracked in Scout076.

## What the campaign accomplished

The campaign compared five owner repositories and several separate model roles.
It found useful Luna wins in Storybook persona and CineForge inspected frame
analysis, rejected unsafe or poor-value substitutions in Doc Web and Echo, and
identified an observable compiler-rejection fallback boundary for Dossier.
The work also repaired harnesses, source truth and judges, implemented a
streaming persona provider, and then proceeded into deployment and pilot work.
Those are separate deliverables from merely running a model comparison.

## Measured overhead and limits

Snapshot: root session log through **2026-09-27 03:31:15 UTC** (September26
local time), beginning September26 14:24:31 UTC. The approximately 13h07m span
includes user pauses and idle time. Eighteen completed root turns record
**2h57m10s** total duration; the current closeout/deployment/pilot turn began
03:25:25 UTC and is additional. Turn duration includes tools and waits, so it
is not pure model-compute time and does not sum parallel worker effort.

| Root log measurement | Value |
| --- | ---: |
| Input token processing | 98,177,510 |
| Cached input tokens (included in input) | 96,096,768 (97.9%) |
| Uncached input tokens | 2,080,742 |
| Output tokens | 168,089 |
| Reported total (input + output) | 98,345,599 |
| Reported reasoning tokens | 30,997; not added again to total |
| Exec calls / agent spawns / follow-ups | 382 / 12 / 20 |
| Agent waits / inter-agent messages | 121 / 158 |
| Context compactions | 4 |
| Paired exec output payload volume | Approximately5.38 million characters |
| Exec outputs over10,000 characters | 81 |

A later closeout checkpoint at **03:54:07 UTC** has 791 response records and
**103,547,763 total tokens**: 103,358,962 input, 101,211,904 cached input,
2,147,058 uncached input and 188,801 output. It is the same cumulative stream,
not additional to the earlier table. The current turn had run about 29 minutes
at this checkpoint, on top of the 2h57m of completed turns.

Both checkpoints were verified by summing
`token_usage_record.payload.usage` and matching
`token_usage_record.payload.thread_token_usage`; older `token_count` display
counters are a different surface and are not mixed in. The 728 per-response
records reconcile to the earlier cumulative thread counter. These counters measure repeated context processing,
not 98 million unique tokens. They cannot be converted to account quota percentage
or dollars from the available information. Child-session usage could not be
attributed from the spawn records, which expose task names without session IDs;
no extra child estimate is added. The separate goal meter is not summed into
these counters. Account usage was 12% of the weekly window at the start of this
closeout; it is account-wide and has no campaign-start baseline, so it does not
establish the campaign's quota share.

The raw transcript remains local at
`/Users/cam/.codex/sessions/2026/09/26/rollout-2026-09-26T08-24-30-01a0de1a-742f-7511-aece-936e73bcde8c.jsonl`.
Only aggregate metrics are included here. Repeated path references include
writes as well as reads; output characters are not model-input tokens. Wait
calls do not themselves establish inference cost. The evidence supports a
large orchestration footprint, not a precise savings forecast.

**Assessment:** much of the substantive work was valuable, but coordination was
heavier than necessary. I repeatedly revisited large records and owner state,
and the campaign cycled through approvals and follow-through instead of keeping
one compact decision record with clear phase boundaries. The approximately
USD3.78 of evaluation API spend was small; optimizing subject calls alone would
miss the larger coordination problem.

## What should change next time

1. **Freeze one decision sheet per owner before dispatch.** Name the actual
   runtime call, current model, required contract, quality floor, aspirational
   target, representative fixtures, candidate settings, comparator and budget.
   CineForge had no production frame-analysis call to replace; discovering that
   only during follow-through inflated the adoption discussion.
2. **Run one offline readiness check before paid calls.** Inspect the rendered
   production prompt, source-backed expectations, coordinate/schema parser,
   judge citations and request reservation. The Storybook prompt snapshot,
   CineForge truth/rubric and Dossier judge-format repairs were concrete sources
   of avoidable rework. Do not create a large generic preflight framework.
3. **Use one owner worker and a compact receipt.** The coordinator needs the
   decision, evidence paths, changed file identities, cost ledger, validation
   and blocker. Repeatedly rereading the owner's files or spawning another
   worker to reconstruct the same history increases context processing without
   adding independent evidence. Use lower-cost workers for receipts and scoped
   closeout; reserve stronger reasoning for ambiguous source truth, routing
   boundaries, privacy and adoption decisions.
4. **Separate evaluation, adoption and deployment milestones.** Finish the
   decision report once the evidence supports a call, then execute authorized
   implementation as a distinct track. Track both in the same campaign without
   describing all later engineering time as evaluation time. Classify release
   and test commands by actual provider side effects: a required live smoke
   still needs a budget reservation and durable usage receipt before dispatch.
5. **Reuse immutable evidence and checks.** Rejudge saved subject answers after
   a proven rubric repair; rerun only inputs affected by code changes. The
   CineForge repair reused all 12 subject outputs, requiring only six new judge
   calls. Documentation and commit changes should not restart product suites.
6. **Make relative and mixed-model decisions immediately.** A candidate can win
   an identifiable task without passing an aspirational universal threshold.
   Preserve hard safety contracts; measure the actual combined fallback path,
   including failed-call cost and latency. Avoid another approval cycle merely
   to recover an agent-created soft stop inside the approved scope and ceiling.

**Priority:** first make offline validation unable to reach providers and route
live checks through existing budget guards. Then remove duplicated coordinator
reads and precautionary broad reruns, using one compact owner receipt and
validation tied to changed inputs. Record per-phase token-counter deltas and elapsed time at the start and
end of the next campaign so improvement can be measured; keep API spend separate.
No percentage reduction is promised from this single observation.

These are recommendations, not a newly installed cross-project framework.
The already requested evaluate-model changes cover strong recommendations,
recovery and mixed-model outcomes; no additional broad skill rewrite is implied.

## Tradeoffs worth retaining

Keep independent source review where it can overturn a bad oracle, exact model
identity, charge reconciliation, privacy boundaries and actual runtime
qualification. Those checks found real issues here. Reduce duplicated context
and ceremonial transitions, rather than replacing consequential review with
unverified cheap-model judgments.

## Closeout examples

Doc Web's owner started a broad `make test` during closeout despite an existing
95-test focused result. It was interrupted after 367 passes while unrelated
pip-install CLI tests consumed about five minutes. The owner confirmed this was
a precautionary choice, not a mandatory release gate. This is not a full-suite pass;
the scoped95 tests, changed-file lint and methodology checks remain the relevant
evidence. A broad lint check also found a pre-existing violation in an untouched
MiMo test, which was preserved rather than expanding this campaign.

Storybook's required deployment suite illustrates a different case: it caught
six legacy tests mocking the old Anthropic streaming contract. That broader
release check was decision-bearing and must remain. The fixtures were updated to
exercise the new Responses completion/billing behavior; the required suite then
passed: backend 1,208, frontend 218, shared 44 and native 8, with 12 backend skips.
The test-only follow-up landed as `ef0c86ac3c9d85218f1665536982c98257b13468`. The first test attempt also lacked an explicit disposable test
DB; preparing required environment variables before launch would avoid that
setup failure.

Dossier also launched an unfiltered `pytest -q` after a green unit suite and an
explicit request for only focused offline checks. That command entered live
Anthropic integration fixtures and was interrupted. The entered passages were
synthetic; dispatch and charges require separate reconciliation. This is an
orchestration deviation, not a GPT6 model failure, and not a zero-cost check.
It strengthens the recommendation to use explicit offline test targets with
provider access disabled during routine validation, rather than relying only
on prose instructions. The owner established a deliberately loose **USD11.039940** reservation from
maximum context/output and retry bounds; exact dispatch/usage remains unknown.
This exceeds the remaining approved allowance and is not a billed amount.
Scout076 preserves the accounting exception; no unrelated live rerun is justified.

Storybook's mandatory Dossier release smoke passed but its artifact omitted
provider cost. The follow-up therefore required separate accounting inspection.
The corrective recommendation is small: distinguish offline and live targets
in the owner runbook, run offline targets without provider access, and make live
smoke targets emit the same usage/reservation receipt as other paid calls.
A command named "test" or "smoke" must not be assumed free.

The Storybook accounting follow-up confirmed that the direct smoke command
bypassed an existingUSD1 guarded launcher. Exact cost and compliance with the
remainingUSD1.060552615 allowance are uncertified; no increase was approved.
The prior matched fixture'sUSD0.010297 is reference only. The maintained runbook
was corrected in remote-main commit `9340cdcacc62ad8bd8f216c416ea3ba990685a4c`
to use the existing bounded path. Browser checks found no signed-in Claude
billing session, so the accounting gaps remain explicit. No new framework or
additional inference was introduced to perform this correction.
