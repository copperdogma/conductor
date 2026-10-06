# Scout 085 — Model delegation and strategic review economics

Date: 2026-10-06 (America/Edmonton)
Verdict: **Adapt** the review contract; **Spike** competing execution patterns before claiming savings.
Original research scope: research and proposal only. No skill/configuration changes, target-repo edits, provider benchmark campaign, commit, or push during that audit.

Approval follow-through: Cam subsequently approved the Alignment 055 policy
and relevant-owner rollout with scoped commits/pushes. The Conductor patch is
implemented and validated in isolation; all eleven owner landings are verified
and their receipts are tracked in Alignment 055. This does not authorize the economic pilot below.

## Decision

There is no current controlled evidence establishing either a cheaper executor
with occasional strong review or a strong coordinator with cheaper workers as
the universal winner for long-running repository work. Recent evidence supports
selective delegation, explicit dispatch conditions, compact evidence transfer,
and measuring the cost of an accepted outcome across the entire agent tree.

For Conductor, trial a capable lower-cost executor with the strongest available
eligible model at maximum supported thinking for strategic review. Resolve the
concrete configuration at runtime rather than embedding a model name in skills.
This incorporates Cam's follow-up preference in
[Alignment 055](../alignments/align-055-agent-staffing-and-event-waits.md).
It is a workload-fit hypothesis, not a measured model ranking. Use a strong initial
planning review when uncertainty or the cost of an incorrect direction is high;
do not let a cheaper executor wander until the first timed review. Keep a strong model
as the main agent when problem framing, decomposition, and integration dominate.
Delegate sizeable independent work units where that makes sense. Retain solo
lower-cost and strongest-model runs as comparison baselines.

Use maximum thinking for designated strategic reviews, not every routine check
or worker action. This supersedes the initial named-model/high-effort pilot
proposal; it is a quality policy, not a demonstrated cost optimum. Do not require
delegation on every small task. Model choice and reasoning effort remain separate
runtime settings. The strongest available model may finish with
fewer actions, making even a solo run economical. Conversely, repeated
supervisor reasoning can consume savings from cheaper workers.

## Recent evidence and its limits

Sources were retrieved on October 6. A new publication/revision date does not
make its evaluated model population current.

| Source and date | Decision-bearing evidence | What it does not establish |
| --- | --- | --- |
| [How Do AI Agents Spend Your Money?, v3](https://arxiv.org/html/2604.22750v3), revised **2026-10-02**, originally April 24 | 500 SWE-bench Verified tasks, eight models, four runs each: 16,000 coding trajectories. Repeated input context drives expense; costly runs repeat views/edits and do not reliably improve success. | Single-agent OpenHands study using older models, with history carried forward unchanged. It neither measures Astra nor compares our two staffing patterns. Modern compaction can change magnitudes. |
| [Capable language models can outgrow the benefits of collaboration](https://www.nature.com/articles/s42256-026-01268-y), **2026-07-24** | Peer-reviewed comparison: 260 configurations, six benchmarks, five architectures, three model families, matched compute ceilings. Strong single-agent baselines often remove the benefit of coordination. In the cost-tracked subset, hybrid and centralized systems achieved similar success with markedly different overhead. | Coding subsets contain only 20 tasks each. A small heterogeneous-team extension is exploratory. Its empirical capability threshold is domain-conditioned, not a rule for Astra or every task. |
| [DecisionBench](https://arxiv.org/html/2605.19099v1), **2026-05-18** | 23,375 instances across eleven models and three suites. Worker availability alone produced little delegation. On-demand worker profiles improved top-choice routing from 14.2% to 29.5%, without a significant end-quality improvement. | Preprint, limited solo controls and single-seed cells; not a coding-repository staffing trial. Supports explicit contracts rather than faith in spontaneous routing. |
| [Uno-Orchestra](https://arxiv.org/html/2605.05007v1), **2026-05-06** | Positive counterexample: a trained 7B controller selectively decomposes work and routes to a heterogeneous pool. Reports 77.0% macro pass@1 across 13 benchmarks and much lower query cost than its AgentOrchestra comparison. | Requires SFT/RL and includes strong workers. Does not show an ordinary prompted cheap coordinator can reproduce the result. |
| [Anthropic multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), **2025-06-13**, historical context | Opus lead plus Sonnet workers improved an internal research score by 90.2% over solo Opus. Authors emphasize breadth-first independent research and explicit effort allocation. | Vendor report, older models, no matched-spend proof. Its often-quoted 15× token figure is relative to chat, not a solo agent; not a general coding cost result. |

We also inspected the September [AgentRouter preprint](https://arxiv.org/pdf/2609.22951).
Its headline savings use an older GPT-4o/Llama pool and an evaluation fallback
with ground-truth quality labels. Do not use it as proof of deployable savings
for current Codex. Newness alone is not evidence quality.

The Nature page failed on one direct web read; its publisher search content and
[author-hosted research summary](https://www.media.mit.edu/publications/capable-language-models-can-outgrow-the-benefits-of-collaboration/)
provided a primary-source fallback. No paper above compares Astra/Sol/Luna under
Cam's current skill and runtime contracts.

## What changed recently in OpenAI's tools

- The [API changelog](https://developers.openai.com/api/docs/changelog) records
  **September 3** async tools, steering, and reasoning-effort updates;
  **September 29** brought GPT-6.1 Sol and Astra Ultrafast. These are distinct
  from a measured improvement in delegation economics.
- Current [Astra guidance](https://developers.openai.com/api/docs/guides/latest-model#subagent-delegation)
  explicitly warns that Astra may delegate less often than desired. Give it
  concrete dispatch conditions. Its stronger instruction following does not
  convert a prompt into an enforceable scheduler.
- [Async tool calling](https://developers.openai.com/api/docs/guides/async-tool-calling)
  supports useful independent work while tools run, then a synchronous wait
  when their results are needed. The application owns pending jobs and result
  delivery. Async is not permission to generate filler while waiting.
- [Reasoning configuration updates](https://developers.openai.com/api/docs/guides/reasoning#change-reasoning-mid-conversation)
  provide a third option: vary effort within the same model while retaining
  the cache prefix. This is documented for standard single-agent API requests,
  not hosted multi-agent mode. It changes effort, not the model, and has
  compaction restrictions. We have not verified a corresponding desktop
  control for automatic checkpoint switching.
- [Codex subagent configuration](https://learn.chatgpt.com/docs/agent-configuration/subagents)
  supports explicit models/effort and custom roles. Unspecified subagents
  inherit the parent's settings. A worker called “cheap” is not thereby cheap.
- Do not confuse this with [hosted Responses Multi-agent](https://developers.openai.com/api/docs/guides/responses-multi-agent):
  its current documented children share the request model. That page lists
  Sol 6.1 and the 5.6 family for the beta. Local Codex capabilities must be
  checked separately; neither interface proves arbitrary mixed-model support
  in the other.
- The **September 11** [Astra skills article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
  recommends narrower skill triggers, selective document loading, and removing
  obsolete procedural overhead. A small dispatch contract should not become
  another elaborate mandatory ceremony.

## Economics and waiting

Current [Codex Standard credit rates](https://learn.chatgpt.com/docs/pricing#token-rates),
credits per million tokens:

| Model | Input | Cached input | Output |
| --- | ---: | ---: | ---: |
| GPT-6 Astra | 250 | 25 | 1,250 |
| GPT-6.1 Sol | 50 | 2.5 | 250 |
| GPT-6 Luna | 2.5 | 0.25 | 12.5 |

Astra's input/output rates are 5× Sol 6.1 and 100× Luna; cached input is 10×
Sol 6.1. These are not ratios of completed-task cost or included subscription
quota consumption. Codex credits have no separate cache-write charge;
[API pricing](https://developers.openai.com/api/docs/pricing) does. Compare
actual usage on the surface used, including reasoning, retries, cache traffic,
tool charges and failed work. Do not add reasoning tokens twice when already
included in billed output.

The break-even condition is simple: strong-model work and rework avoided must
exceed worker execution plus dispatch, context transfer, supervision, review,
and integration. There is no universal minimum task size or useful agent count.

**Waiting is an orchestration concern.** A suspended tool wait does not require
the language model to keep generating thoughts. Repeated wakeups, status calls,
history reads, summaries and replanning do require model work. Use completion
events or blocking waits, and return compact deltas only when something changes.
Do not dispatch a second language model solely to poll when a native event wait
already exists. This follows from runtime behavior and cost structure; the
papers did not experimentally isolate polling frequency.

If mandatory dispatch and hard spending limits matter, enforce them outside the
prompt: a controller checks review deadlines, allowed models, concurrency and
remaining budget before starting work. Keep that as a later option if a small
skill-level pilot demonstrates missed reviews or excessive overhead. Avoid
building a new supervisor framework before that evidence exists.

## Which pattern fits which work

| Work shape | Initial policy to trial | Main failure to watch |
| --- | --- | --- |
| Clear, serial task; executor has demonstrated competence | Solo capable cheaper agent, with strategic review only for a long run or a meaningful trigger | Cheap agent fails to recognize uncertainty or misses the review |
| Long bounded implementation with occasional strategic uncertainty | Sol 6.1 executor plus Astra reviewer; initial strong framing if needed | Reviewer receives a sanitized summary or advice arrives after expensive rework |
| Ambiguous destination, costly architectural decisions, difficult decomposition | Astra leads; delegate sizeable independent evidence or implementation units | Lead redoes workers' work, micromanages, or turns every tool action into a handoff |
| Broad independent research or many disjoint checks | Strong coordinator plus a small bounded worker set | Duplicate research, unverified summaries, integration overhead |
| Small fix or tightly coupled native/debugging sequence | One capable agent | Delegation costs more than doing the step directly |

These are engineering inferences to test. Evidence does not justify insisting
that every main thread use the cheapest model, or that the highest-priced model
never do implementation itself.

## Proposed loop-review change, not applied

The [current skill](../../.agents/skills/loop-review/SKILL.md) already covers
outcome alignment, failures, bottlenecks, source-backed alternatives, bounded
experiments, recommendation disposition and authority. Preserve those checks
and its 30 active minutes/three substantive rounds default. Waiting does not
advance that active-work clock; deadlines and hard stops still govern.

Add a concise dispatch section, with runtime specifics in a supporting reference:

> For an ongoing loop, select the strongest available eligible model and its
> maximum supported thinking level from current runtime capabilities at the
> start. If execution is not already using that configuration, dispatch one
> bounded strategic review at the existing checkpoint, or
> earlier when repeated failure, uncertainty, or the cost of a wrong direction
> warrants it. Review consequential initial plans before substantial work.
>
> Supply the intended outcome, constraints, current worktree/snapshot, remaining
> budget, previous recommendation and disposition, changes since the last
> checkpoint, failures, measured costs where available, and links to decisive
> artifacts. The reviewer should inspect selected primary evidence and look for
> omitted or disconfirming evidence, rather than trust the executor's summary.
> Reuse applicable research; search only enough to resolve the current decision.
>
> Return a compact continue/change/defer/stop recommendation, supporting
> evidence, the smallest next experiment or deliverable, and its stop condition.
> Reopen a settled decision only for concrete new evidence or a demonstrated
> outcome mismatch, accounting for the cost of changing direction.
> The reviewer remains read-only and does not recursively commission another
> strategic review. The main agent records the recommendation's disposition
> and verifies follow-through. Routine corrections within existing authorization
> can proceed; new scope or authority still requires the existing approval path.
>
> Use completion events or a blocking wait when results are required. Continue
> only independent work while a review is pending, and avoid advancing a decision
> that the review could invalidate. Do not repeatedly poll unchanged state or
> duplicate the delegated work. Review consumes the existing budget.

Delegate work units only when their interfaces are stable and their outputs
have a meaningful, affordable acceptance check. If a review fails or arrives
after the underlying state changes, record that condition and check its advice
against the current snapshot before adoption; do not silently treat it as a
completed gate or restart the entire investigation.

The dispatch reference should distinguish a review of the current authorized
loop from a user-requested audit of another chat. A parent-child return is not
permission to message an unrelated user-owned chat. If the requested reviewer
is unavailable, disclose the fallback; do not silently call an inherited model
the configured reviewer. A standalone audit or already-strong main agent need
not spawn another equally costly agent merely to satisfy a ritual.

## Local applicability check

This scout requested independent read-only subtasks with explicit Sol 6.1 and
Luna configurations and `fork_turns: none`. Their reports returned through the
parent mailbox without status polling. A bounded Astra `high` critique returned
separately and reinforced initial-plan review, primary-evidence access, stable
worker boundaries, and avoiding review-induced churn. This checks the usable
dispatch/report path, not savings,
served-model billing identity, or automatic cadence compliance.

The follow-up [Alignment 055](../alignments/align-055-agent-staffing-and-event-waits.md)
records an explicit child message waking an active parent mailbox wait, before
the child completed its task. It keeps this separate from generic timer sleep,
idle-parent reactivation and cross-chat messaging availability.

The current collaboration schema accepts model/effort overrides only for no
history or partial-history forks; full-history forks inherit the parent.
`wait_agent` waits on mailbox activity and final child reports are delivered to
the parent. The spawn schema supplies no token or monetary ceiling. Therefore,
budgets written into prompts are soft limits here. Avoid claiming a hard cap or
verified per-model savings from these calls. No provider benchmark campaign
or settings change was performed.

## Bounded next experiment

After approving the contract, prepare a small matched pilot in one owning repo,
with its authorization, isolation and acceptance rules. Compare four arms:
solo Sol 6.1; solo Astra; Sol plus checkpoint Astra reviews; Astra lead with
explicit cheaper worker contracts. Hold work scope, initial state, tools,
quality criteria and total ceilings fixed. Include both a mostly serial task
and a genuinely decomposable task, randomize order, and repeat enough to expose
run variance. Do not give one arm solutions learned in another arm.

Measure accepted outcomes and serious defects first, then total billed usage
across all agents, elapsed time, interventions, actual dispatch, review latency,
duplicated work, unchanged status wakeups, and integration/rework. Preserve
failed and stopped runs. Judge artifacts independently of the staffing label.
If the environment cannot attribute model usage, say the economic result is
unmeasured. Do not estimate dollars from wall time or model names alone.

Predeclare a concrete budget, quality gates, meaningful savings threshold and
stop rule before execution. A tiny pilot selects the next experiment; it does
not establish a universal staffing policy. Keep the current policy if results
are ambiguous. No paid pilot is authorized by this research request.

## Project routing

| Owner | Disposition and useful application |
| --- | --- |
| Conductor | **Adapt/Spike**: own the proposed review contract and compare staffing; route any later rollout through align-projects membership check. |
| Dossier | **Defer rollout**: potential fit for long semantic/evaluation iterations; preserve owner evidence and acceptance contracts. |
| Storybook | **Defer rollout**: potential fit for long product/integration work and independent evidence checks. |
| Doc Web | **Defer rollout**: potentially useful strategic review; page safety and source adjudication remain decisive. |
| CineForge | **Defer rollout**: pipeline investigations can split where artifact contracts are independent. |
| Board Game Ingester | **Defer rollout**: strong fit for bounded optimization checkpoints; preserve frozen/independent validation and no-progress stops. |
| Robo Rally | **Defer rollout**: independent exploration may split; coupled game behavior needs one integration owner. |
| Echo Forge | **Defer rollout**: useful for sizeable independent work; small semantic decisions should not acquire heavyweight review overhead. |
| Ultima IV Web | **Defer rollout**: strategy review may challenge recovery/control approaches while preserving original-game reference and reuse restrictions. |
| VLC Thumbs | **Defer rollout**: retain one native debugging/integration owner; delegate research or independent artifact inspection. |
| Financial Hub | **Defer automatic rollout**: retain guarded, manual review and distinct authorization for production changes. |
| Financial Monthly Analysis | **Defer automatic rollout**: preserve source truth, privacy and proposal-first handling; no autonomous classification changes. |

This is a cross-project methodology proposal, so it stays in Conductor rather
than adding speculative inbox pressure to every owner. No new inventory or
rollout was performed. Practical benefit: make expensive strategic attention
deliberate and observable while reducing redundant context, polling, and work
that the supervisor later repeats.

Confidence: high that automatic delegation and maximum reasoning are poor
universal rules; moderate in the proposed conditional policy; low in any claimed
savings or model-pair superiority before a current local comparison.

Validation: `make lint` and scoped `git diff --check` passed. The new scout's
local links, index/inbox references and whitespace were checked. Existing
unrelated checkout changes were preserved. Product suites were unnecessary for
this research-only change; no economic benchmark result is claimed.
