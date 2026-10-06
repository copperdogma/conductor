# Alignment 055 — Agent staffing and event-driven waits

Date: 2026-10-06 (America/Edmonton)
Status: **Implemented and validated; all eleven owner landings verified on remote main**
Classification: portable improvement, with intentional owner adaptations
Predecessor: [Scout 085](../scout/scout-085-model-delegation-and-strategic-review.md)

## Decision and user preference

Cam wants **strongest model and maximum thinking** for strategic loop review,
resolved at execution time rather than pinned to a model name. Adopt that
wording in the proposal. This is a review-quality preference; the research
does not establish it as the cheapest configuration. Routine execution and
evidence gathering still use the cheapest capable model when delegation's
benefit exceeds context, coordination and verification costs.

Recommended common wording:

> For strategic loop reviews, use the strongest available eligible model at its
> maximum supported thinking level. Resolve the concrete model and highest
> supported effort from current runtime capabilities when the run starts, and
> record the selection. Respect existing access, privacy, tool and budget
> constraints. Do not silently substitute a weaker configuration or describe
> an unperformed review as complete.
>
> If the main agent is not already using that configuration, dispatch one
> bounded, read-only strategic reviewer. Give it direct access to decisive
> artifacts as well as the compact progress packet. Keep ordinary coordination,
> checks and worker execution proportional to their difficulty. Preserve the
> main agent's ownership of scope, integration and follow-through.
>
> While delegated work runs, do useful independent work or wait on completion
> events. Use the runtime's message-aware wait when the next step needs a
> result. Do not repeatedly poll unchanged state, redo assigned work, or start
> a watcher model when the runtime already exposes the needed event.

“Maximum” means the selected model's highest supported setting on the actual
tool surface, not necessarily a parameter literally named `max`. Select the
strongest eligible model from current capability guidance and the user's
preference, not price or release date alone; catalogue positioning is not a
measured ranking on this task. Record the requested configuration separately
from independently verified served identity. Recheck selection after an
availability error, runtime change or meaningful interruption; otherwise reuse
it within the run. A fallback must stay within existing authorization and be
disclosed. No new account, tier or budget increase is implied.

Keep the existing strategic-review cadence. Routine round bookkeeping is not a
strategic review. An already suitably configured main agent can review directly
unless a fresh independent challenge is useful or requested. Review before
costly ambiguous decisions; a timer is not a reason to postpone evident drift.

## Messaging and wake-up verification at proposal time

| Surface | Current live tool contract | Consequence |
| --- | --- | --- |
| Child-agent tree | `collaboration.send_message` queues messages; `wait_agent` waits on the mailbox; child final reports return to the parent. `followup_task` can resume a non-root agent. | An active parent can block rather than repeatedly inspect child status. Ordinary messages do not themselves start a new turn. |
| Separate user-owned Codex chats | `send_message_to_thread` accepts follow-up prompts to existing chats with human authorization for that destination. `wait_threads` waits for completion/attention, with cursors suppressing repeated results. | Cross-chat messaging is available, but distinct from the child mailbox. Another agent's request alone does not authorize a reply. |

The official [Multi-agent action reference](https://developers.openai.com/api/docs/guides/responses-multi-agent#how-multi-agent-works)
also distinguishes message delivery without a new turn, mailbox waiting, and
follow-up dispatch. Desktop-chat contracts above came from this session's live
tool metadata; they were not inferred from the hosted API.

### Local test

1. Assigned an existing child a bounded task with a delayed explicit parent ping.
2. Parent called `collaboration.wait_agent` with a 60,000 ms timeout.
3. It returned `timed_out: false` and delivered the explicit message:
   `Wake-up probe: child message delivered while parent waits.`
4. The child continued its audit and subsequently returned its final report.

There were no intervening status polls. This proves a child message waking an
active mailbox wait before the child finishes. It does not measure billed
savings, demonstrate interruption of generic shell/clock sleep, or establish
automatic reactivation of a finished parent. No unrelated user-owned chat was
messaged as a test.

Use a message-aware wait for this purpose. Waiting need not generate model
tokens continuously, but calls/resumptions, repeated context and messages can
still cost tokens. Waits can also end for timeout, other messages or user input;
they are not indefinite child-only sleep. `wait_threads` does not wake on
commentary. Respect the host's wait/responsiveness limits; renew a bounded wait
without a fresh status sweep when nothing changed. A timeout does not establish
completion or necessarily stop the child.

Use final delivery for normal completion. Earlier pings should convey an
actionable blocker, decision, failure or requested milestone. If a host needs a
terminal ping, deduplicate it with the final report. Do not replace polling
with frequent child heartbeats. Do not finish the parent turn while promising
an ephemeral child will wake it later without a supported continuation mechanism.

## Audit coverage at proposal time

The following records the original read-only audit, before the approval and
implementation section below. Its no-fetch/no-edit statements apply to that
audit only.

Scanned all **21 Conductor SKILL.md entrypoints**, inspecting relevant
coordination sections and references, plus personal `delegate-wait`. Targeted
read-only scans covered relevant skill names in all **11 managed owner roots**.
This was not a full review of every owner skill or a new remote installation
audit. Checkout content and cached Git refs can be stale. No fresh fetch,
membership change, owner edit, commit or push occurred.

The inspected execution skills contain no hardcoded staffing model IDs. Model
names in benchmark examples or historical observations should remain as dated
evidence; a text match is not automatically a staffing defect.

## Recommended Conductor changes

Keep a short common policy in `AGENTS.md`, with actual review dispatch in
`loop-review`. Add only the missing local decision at each skill boundary.
Do not create another mandatory coordinator skill or centrally hosted harness.

| Skill and inspected location | Finding and minimal change |
| --- | --- |
| [loop-review](../../.agents/skills/loop-review/SKILL.md), destination/investigation | No model/dispatch protocol. Add strongest/maximum runtime resolution, compact delta plus artifacts, one read-only reviewer, no recursion, event wait and failure/late-result handling. Keep existing authority boundaries. |
| [loop-verify](../../.agents/skills/loop-verify/SKILL.md), defaults (114), strategy (211), results (346) | Inherited coordinator also handles deep strategy; collection merely says wait. Route deep reviews through strongest/maximum policy, keep brief round checks local and workers risk-sized, add event collection. Preserve clean-stop and single-pass shards. |
| [build-story](../../.agents/skills/build-story/SKILL.md), delegation (83), cadence (107) | Good plan gate and disjoint ownership. Add a short staffing/wait reference and strategic-review dispatch, without moving implementation before the gate or delegating small stories. |
| [validate](../../.agents/skills/validate/SKILL.md), parallel packets (84) | Separate inexpensive checks from genuinely strategic outcome/architecture review; use event waits. Keep main-agent disposition. No compulsory maximum-effort reviewer for every validation. |
| [finish-and-push](../../.agents/skills/finish-and-push/SKILL.md), coordination (34) | Already balances savings against overhead. Keep that rule, add event waits and strategic escalation only when warranted. Preserve one Git/integration owner and proportional validation. |
| [evaluate-model](../../.agents/skills/evaluate-model/SKILL.md), owner dispatch (326), monitoring (336) | Preserve mandatory repo-local owners and no duplicate provider work. Add role-sized staffing and event collection. Strategic maximum effort must not change benchmark subjects, frozen prompts or judge configurations. |
| [triage](../../.agents/skills/triage/SKILL.md), full sweep (129) | Contracted lane fan-out lacks a small/empty-lane economics rule. Batch tiny related lanes when useful, preserving required coverage and explicit requested fan-out. Explain direct execution when delegation has no benefit. |
| [ideation](../../.agents/skills/ideation/SKILL.md), subagent mode (66), and [create-adr](../../.agents/skills/create-adr/SKILL.md), option sidecar (19) | Wording can demand fresh explicit delegation permission despite existing governing authorization. Recognize current session/project/runtime authorization; retain user opt-outs, one bounded option packet and caller decision authority. Ideation is not automatically strategic review. |
| [setup-methodology](../../.agents/skills/setup-methodology/SKILL.md), core loop (216), installer (430–490) | Teach approved common policy and focused leaf changes so setup does not reproduce older contracts. Update its [runbook](../runbooks/setup-methodology.md); retain sparse/no-code exceptions. |

That is **10 Conductor skill entrypoints** with narrow proposed edits, plus
`AGENTS.md` and the setup runbook. Reconcile the setup checklist only if its
completion assertions change; a local edit is not a portfolio rollout.

No bespoke leaf edit is needed in the other **11**: `align-projects`, `scout`,
`create-story`, `init-project`, `security-audit`, `mark-story-done`,
`triage-stories`, `triage-adr`, `learning-review`, `learning-candidate`, and
`skill-surface-audit`. They can use common policy when warranted. Keep their
existing read-only, setup, lifecycle and human-judgment boundaries; do not turn
a simple scaffold or security scan into a mandatory model committee.

Spend enforcement is separate from notifications. Provider/job limits,
conservative dispatch reservations and after-the-fact reporting are different
controls. Reserve for concurrent workers before launch; sleeping parents must
not weaken aggregate caps. This spawn interface has no monetary cap field.
Do not describe a concurrency limit, prompt budget or wait timeout as a hard
dollar limit.

## Personal delegate-wait change

[delegate-wait](/Users/cam/.codex/skills/delegate-wait/SKILL.md) already separates
active-parent waiting from durable scheduling and says simple timers normally
need no agent. Add this entry decision:

> Prefer native completion/event waits when the target exposes them. Delegate
> observation only when no usable event source exists and real read-only
> monitoring is needed, or when explicitly testing the handoff. Use an available
> low-cost capable model and compact brief. Keep the parent in its message-aware
> wait and preserve deadlines and terminal outcomes.

Move the dated model example at line 18 into historical evidence rather than
operational selection prose. Keep legitimate external polling at an explicit
cadence when the external application offers no event. Do not remove failure,
deadline or durable-lifecycle checks based on an untested idle-wakeup claim.

## Owner applicability and retained differences

| Owners inspected | Recommendation |
| --- | --- |
| Dossier, Storybook, Doc Web, CineForge, Board Game Ingester, Robo Rally, Echo Forge, Ultima IV Web, VLC Thumbs | Candidates for selective later alignment, after actual target-state verification and the managed-project check. Preserve owner validation, plan gates, disjoint writes and final disposition. |
| Financial Hub, Financial Monthly Analysis | Retain manual strategic checkpoints and privacy/source/production boundaries. Hub's local loop-verify worker guidance does not authorize automatic strategic-review rollout. |

Local variants to preserve: Dossier triage sizes workers by lane risk;
Storybook build-story gates delegated edits on plan approval; Doc Web validation
keeps final scoring/closure with the main thread; CineForge golden-verify
distinguishes semantic judgment; Financial Hub loop-verify keeps shared semantic
work find-only.

Dossier's local loop-review was absent while its cached `origin/main` blob
existed, with the primary 148 commits behind that ref. Doc Web's local skill
existed and its primary was two commits behind the cached ref. These establish
local state only. Alignment 054 (dated primary-checkout audit, not imported into this scoped patch) is a
separate dated remote coverage check, not today's live remote evidence.

## Proposed next action and validation at audit time

Apply the ten scoped Conductor skill edits, short root policy, setup runbook
adjustment and personal delegate-wait clarification. Preserve unrelated dirty
work and existing authorization. Do not change model settings or benchmark
subjects, commit/push, or edit owner repos as part of this local package.

Validate with skill/format/link checks and bounded scenarios: cheap executor at
a strategic checkpoint; already-strong main agent; clean verifier at its stop;
unavailable strongest configuration; frozen evaluation subject; timeout or
progress-only message; late result; external monitoring without notifications.
The live ping already proves the active mailbox path and need not be rerun for
prose-only changes. Resolve the highest configuration dynamically.

Practical improvement: reserve maximum-capability thinking for intentional
strategic review, make worker selection explicit, and avoid repetitive checking
without weakening ownership or stopping rules. Savings remain unmeasured.

Audit validation: `make lint`, scoped `git diff --check`, local-link and
whitespace checks passed; the 21-entrypoint count was verified. An independent
strategic critique requested the strongest general reasoning configuration
exposed by this runtime at its highest supported effort and returned the
budget-enforcement, notification and wake-semantics cautions retained above.
Requested configuration is not independent proof of served identity or cost.

## Approved Conductor implementation — 2026-10-06

Cam approved this package, relevant-owner rollout and scoped commits/pushes.
The Conductor candidate is isolated on `codex/align-055-conductor` from freshly
fetched `origin/main` at `511655e8efdaba459427fb90b4f2815b7335bb34`.
Nine skill baselines and the setup runbook match the primary checkout byte for
byte. Primary `loop-review` has a separate unlanded refactor; primary `AGENTS.md`
lacks already-landed decision-model/handoff sections. Retained fresh-origin
content and predecessor guardrails instead of importing either unrelated diff.
Only Scout 085, this alignment and their exact index/inbox captures came from
the dirty primary. No primary files were reset, stashed or edited.

The parent coordinator refreshed rollout membership: 72 unique Git roots under
`/Users/cam/Documents/Projects` were inventoried to maximum depth 7. The existing
ten managed owners plus VLC Thumbs remain selected. Six previously excluded
candidates stay excluded: Ravenloft Cthulhu, RPG Map Projector, Canmore Town
Council, Alain Lessard Book, Onward to the Unknown Website and Codex Forge.
Two app Git roots outside Projects were checked: Hardware Specs and the images
root for Matt's 2025 Waterdeep campaign; neither has `.agents/skills`.
Exact paths and the parent-reported evidence boundary are in the scoped record.
This membership check does not make every discovered repository a rollout target.

Implemented the ten named skill edits, common policy and setup runbook.
Staffing and dispatch remain model-agnostic, with strongest/maximum thinking
reserved for strategic review. Provider subjects and judge configurations stay
owner-defined, and actual aggregate spend gates precede concurrent paid work.
Owner and personal-skill work are outside this Conductor candidate.

Validation target: preserve existing authority and stopping contracts while
making worker economics, strategic review dispatch and completion waits explicit.
`make skills-check` (21 entrypoints), `make lint`, `make methodology-check` and
`git diff --check` passed on the candidate. Local-link and whitespace checks
cover new links/content only; historical Alignment 054 is a plain dated reference
because that separate primary-only audit is outside this patch. No product suite
or provider calls apply to this prose-only change, and the existing mailbox test
is reused without claiming economic savings or idle-parent reactivation.

Skill-creator's validator first lacked PyYAML in both host and bundled Python.
A temporary `uv run --with pyyaml` environment ran it: raw files reject the
pre-existing `user-invocable` frontmatter field. All ten temporary copies with
only that unsupported field omitted pass. Original repo metadata is preserved;
this is a validator compatibility limit, not ten fully passing raw checks.
Baseline identities and tested policy hashes are in
[the scoped evidence record](evidence/align-055-conductor.json).
Independent read-only review passed all five realistic forward scenarios with
no defects. Requested configuration was `gpt-6-astra` at `ultra`; served identity
is not independently verified. The reviewer included the current dispatch-schema
inheritance/override guidance. Parent froze policy after the pass.

The separately assigned personal-skill worker updated non-Git `delegate-wait`.
Its [compressed portable patch](evidence/align-055-personal-delegate-wait.patch.gz) and
[receipt](evidence/align-055-personal-delegate-wait-receipt.txt) retain before,
after and raw patch hashes. Deterministic gzip preserves the exact patch
without treating diff context markers as prose whitespace. Its raw skill-creator validator passes in the temporary
PyYAML environment. Conductor imports evidence only; the personal directory
cannot be committed or pushed as a repository. Existing mailbox evidence is
reused without adding a timer or live-provider test.

Global preflight passed before owner pushes. All eleven selected owners have
landed policy and final receipt commits, with each final remote-main SHA verified.
The [readable owner ledger](evidence/align-055-owner-landing-ledger.md) and
[full machine-readable receipt](evidence/align-055-owner-landing-ledger.json)
retain full bases, commit SHAs, checked-file identities, owner commands,
adaptations and limits. The supervisor closeout follows these owner landings.

Finance retains manual strategic checkpoints, privacy and production boundaries.
Frozen strategic-dispatch blocks match source; Ultima/VLC provenance records were
checked against source/current/original/history hashes. Ultima's untouched
triage-evals/improve-eval receipt hashes were already stale at base and remain
explicitly recorded. Echo's methodology check has a non-failing warning that no
Ideal requirements were parsed. No paid evaluations, product model settings or
production activation changed. Task branches/worktrees remain retained; primary
checkouts remain untouched.

Practical improvement: relevant owners now have the scoped staffing/wait rules
and their own validation receipts, preserving local gates. The strongest review
configuration is resolved dynamically; economic savings remain unmeasured.
