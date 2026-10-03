---
name: evaluate-model
description: Verify a current AI model, map its decision-bearing fit across tracked projects, recommend a numbered evaluation shortlist, and after explicit all-or-subset approval run fair provider-native evaluations inside isolated owning-repo worktrees with centrally custodied eval access when needed. Use for new-model, replacement, comparison, rerun, reproducibility, or evidence-audit requests where API access, structured output, reasoning, reliability, cost, latency, privacy, or quality affect adoption. Use scout only for release research with no evaluation decision.
user-invocable: true
---

# /evaluate-model [natural-language evaluation brief]

Use one skill for the whole campaign:

1. verify that the candidate exists on a current API surface
2. determine which tracked repositories have a maintained decision it could change
3. recommend the evaluations worth running and explain the deferrals
4. after the user selects all or a subset, enter each owning repo and run its
   evaluation under its own context
5. synthesize the repo-local verdicts without centralizing their harnesses

The public name remains `evaluate-model`. “Remote model” is an access path, not
the purpose of the workflow.

Success means a decision Cam can act on: name the winners, explain the tradeoffs,
and recommend where to use each model. Completing calls or listing blockers is
not sufficient. A repository may use several models for different tasks; a
candidate need not replace every model-owned call to be a worthwhile adoption.

## Invocation Contract

Treat everything after `/evaluate-model` as a natural-language brief, not
positional arguments. A model name alone is sufficient. Extract and retain:

- candidate names and possible slugs, providers, routers, or access paths
- any named repo, runtime stage, eval lane, fixture, incumbent, or capability
- reasoning, output, schema, tool, sampling, modality, and route requirements
- cost, latency, concurrency, privacy, safety, repeat, and deadline constraints
- whether the user wants portfolio recommendations, selected execution, a
  force-fresh rerun, reproducibility work, or a read-only evidence audit
- exclusions and later corrections; the latest clear instruction wins

Resolve routine slugs, providers, incumbents, eval IDs, and repo paths from
current official and repository evidence. Do not ask for facts that are safely
discoverable. Preserve narrow requests rather than widening them into a model
tournament.

## Choose the Current Stage

State the stage briefly before acting.

### Stage 1 — Portfolio recommendation

This is the default for a model-only invocation such as:

```text
evaluate-model grok 4.6
```

Verify availability, inspect portfolio fit, and return the numbered proposal.
Do not run a paid benchmark or mutate a target repo yet.

### Stage 2 — Selected owning-repo campaign

Enter this stage when the user responds to the numbered proposal with `yes`,
`go ahead`, `do it`, `only do 1, 5, and 6`, equivalent named repos, or another
unambiguous selection. Execute the selected evaluations; do not merely write
handoffs for another agent.

An explicit request to “run now in Dossier” or an equivalent named target may
also enter Stage 2 directly when the repo, lane, scope, and spend boundary are
already clear. Otherwise produce a one-item Stage 1 proposal first.

### Read-only audit

`Audit`, `inspect`, `review`, or `verify existing evidence` does not authorize
provider calls, harness execution, artifact creation, or repo mutation. Report
the evidence and its limits only.

### Force-fresh intent

A clear request to rerun from scratch, reproduce, measure variance, or exercise
the workflow fresh bypasses duplicate avoidance only. Preserve prior evidence,
use a new artifact/run identity, and make uncached subject calls even when the
model and configuration are unchanged. It still preserves all scope, privacy,
spend, fairness, retry, truth, commit, and rollout controls. A fresh adoption
comparison reruns incumbent and challenger on the same frozen inputs; a
candidate-only transport or variance check cannot support a current superiority
claim.

## Stage 1 — Verify and Recommend

### 1. Verify the model

Use current first-party provider documentation, release notes, pricing, model
catalogs, and API references. For temporally unstable facts, browse or query
the current official source rather than relying on model-family memory or
announcement copy.

Distinguish these claims:

- **announced** — the provider describes the model publicly
- **API-listed** — an official API document or authenticated model-catalog
  lookup exposes the exact slug
- **callable** — a dated successful native inference response proves access for
  the credentials and region that will own the run

Stage 1 must not use a target repo's credential, including for model discovery.
Use public official API evidence and dated existing owner-returned access
evidence only. Authenticated catalog, text, schema, image, tool, or harness
probes always belong to Stage 2. An explicitly requested standalone access
probe may enter Stage 2 under a named owner context and disclosed bounded spend;
it does not create a Stage 1 credential exception. If callability is not already
proven, say `access: unverified` rather than turning missing proof into a
model-access failure.

Record the exact slug, endpoint/API family, relevant modalities and structured
output/tool support, reasoning controls, pricing, and retention/ZDR posture.
Availability is not adoption.

Treat privacy controls as payload-dependent rather than universal eval gates:

- for clearly public or synthetic fixtures, ZDR and provider data-collection
  denial are optional unless the owner or repo requires them. Disclose when the
  selected route may retain or train on inputs, and proceed only within the
  approved evaluation scope
- for non-public but non-sensitive project material, follow the owner's stated
  provider policy and disclose retention/training uncertainty before calls
- for private, personal, confidential, licensed-restricted, or unclear inputs,
  fail closed until the route and owner policy make them eligible

Do not combine every available privacy filter by default. A filter is an
absolute gate only when the payload classification or owner policy requires it.

### 1.5 Check the evaluated-model ledger

Read `docs/model-watch/evaluated-models.md` before portfolio routing. Match the
candidate's provider-qualified ID, public aliases, and dated checkpoints. An
authenticated contract probe, provider call, or documented owner-side
access/transport stop counts as a prior evaluation attempt for deduplication,
even when semantic quality remained unmeasured.

Do not recommend an exact matched model as a new evaluation. A prior model may
enter the numbered list again only when the user explicitly requests a fresh
rerun or current evidence satisfies the narrow retry trigger recorded in the
ledger and owner evidence. Label that item **re-evaluation**, cite the prior
attempt and changed trigger, and rerun only the decision-bearing failed gate or
current parity surface. Documentation, catalog, pricing, or route metadata
alone does not satisfy a callability, strict-contract, privacy, reliability,
latency, cost, or capability trigger.

Repairing a judge, adapter or harness within an already approved active campaign
is continuation, not a new model nomination. Preserve failed evidence and reuse
saved subject outputs where possible; do not turn routine recovery into repeated
approval requests. Respect explicit user retry limits and hard spend ceilings.

Keep distinct checkpoints distinct. Do not collapse a similarly named open
checkpoint, managed service, dated snapshot, or provider alias unless exact
served-identity evidence proves they are the same evaluated model.

### 2. Inspect the portfolio

Start with `projects.yaml`, then inspect every registered project and any
explicitly named active repo. Read enough current owner context to identify:

- its runtime and maintained model-owned surfaces
- the local `AGENTS.md`, Ideal/spec, eval registry, recent attempts/stories,
  inbox or scout evidence, and repo-local model-evaluation skill when present
- incumbent and recent same-family or same-provider evidence
- frozen prompts, fixtures, scorers/goldens, hard quality gates, latency/cost
  gates, privacy restrictions, and current work that makes an eval timely or
  disruptive
- each fixture's actual data class: clearly public/synthetic, non-public but
  non-sensitive project material, or private/sensitive data. Checked into Git
  does not by itself mean public, and realistic names do not by themselves
  prove personal data when the owner identifies the fixture as public or
  synthetic
- the smallest lane whose result could change a real decision

For efficiency proposals, estimate the stage's contribution to total workflow
time, cost, or human effort and the plausible overall gain, using representative
owner evidence when available. Stage share × fractional reduction approximates
additive savings; parallel work requires critical-path analysis. Label unknowns
and compare benefit with experiment/maintenance effort and competing work.
Quality defects or critical dependencies can justify a lane independently.

Require a maintained decision-bearing surface, eligible fixtures, a plausible
measurable benefit, and a bounded progressive run. The bar for evaluation is
lower than the bar for adoption: do not demand demonstrated superiority before
testing, or treat "the incumbent already works well" as a sufficient deferral.

Apply this balanced selection policy:

- **Default to a small comparison on matching modalities.** For a new
  vision-capable checkpoint, normally recommend a bounded screen on each
  maintained, eligible vision task (for example cropping, photo/OCR grounding,
  and ordered-frame understanding). These measure different abilities; choosing
  one does not cover the others. Verify the actual supported inputs and task
  fit; an omni label alone does not justify audio generation or unrelated text
  evaluations. Apply the same principle to other matching capabilities.
- **Look beyond pass rate.** Consider continuous accuracy, difficult cases,
  reliability, latency, total task cost and useful capability gains. A 100%
  pass rate can coexist with imperfect localization or a tiny, easy fixture
  set. Prefer a fresh same-input incumbent/challenger comparison when making
  relative claims. If the benchmark cannot distinguish quality, say so; measure
  what it can and propose representative held-out coverage when warranted.
  Freeze new criteria before either model runs and respect scope approval;
  never change goldens or scorers to manufacture a winner.
- **Skip comparisons with no plausible practical payoff.** Defer or exclude
  task mismatches, ineligible fixtures, redundant prior attempts, or candidates
  whose expected economics cannot justify adoption. For example, a dramatically
  costlier/slower model against a cheap incumbent with representative, reliable
  full-quality results may be unjustified when no relevant difficult cases or
  other valuable capability remain. Cite the task-level cost estimate or known
  gate, fixture coverage and missing benefit. Token price or a small 100% smoke
  test alone is insufficient; do not claim an untested model cannot be better.
- **Qualify uncertainty consistently.** Unverified access or schema support can
  justify a small first-stage qualification inside a selected owner campaign;
  it is not automatically a reason to omit an otherwise useful comparison.
  Qualify the owner's actual contract; do not invent a strict-schema requirement
  for a lane that uses another output contract. Distinguish missing proof from
  documented incompatibility. Preserve hard
  owner contracts, privacy, prior-attempt retry triggers and spend limits;
  any permitted relaxed diagnostic remains capability-only evidence.
- **Evaluate adoption by task.** Identify separable calls or stages where a
  cheaper/faster model could win while a stronger model handles other work.
  Test each proposed boundary; failure on one task does not erase a win on an
  independent task. Do not require a repository-wide replacement decision.

For every matching task omitted, give a concrete task-specific reason. Prioritize
larger expected gains when resources are constrained, but do not silently turn
that priority into a rule that only failing incumbents deserve challengers.

Give every inspected repo exactly one disposition:

- **Evaluate now** — the result can change a current maintained decision
- **Defer** — plausible later value, but a prerequisite, privacy posture,
  competing work, or maintained lane is missing
- **Do not evaluate** — the model does not address a relevant maintained
  surface or prior evidence makes the run unjustified without a new trigger

### 3. Return an executable recommendation

Put only **Evaluate now** items in the numbered list. Those numbers are stable
execution handles for the next user message. For each numbered item include:

- owning repo and exact first eval lane
- incumbent and decision the evidence can support
- why this model could change that decision now
- progressive stop gate and the most important quality/latency/cost threshold
- fixture eligibility and privacy/ZDR restriction
- proposed per-repo provider-spend ceiling, normally lower than the US$5
  fallback when the maintained lane can be bounded more tightly

Size that ceiling for the decision-bearing comparison, independent judging and
bounded operational recovery. Check reservation feasibility before proposing it;
do not offer a budget that cannot admit the intended cases, then discover this
after approval. Distinguish hard user limits from provisional operator estimates
and soft screening thresholds. Avoid blanket zero-retry plans for recoverable
harness/judge faults unless the user explicitly requires them.

Then include an unnumbered `Not recommended now` section that names every
remaining inspected repo and gives its **Defer** or **Do not evaluate** reason. Do not
silently omit a tracked project.

State the sum of all proposed per-repo ceilings as the **campaign maximum**.
The ordinary acceptance line is:

```text
Reply `yes` to run all numbered evaluations, or `only do 1, 5, and 6` to run a subset.
```

If no repo deserves an evaluation, say so and do not offer a meaningless
approval prompt. A recommendation pass may create or update Conductor's normal
scout/routing artifact when durable portfolio memory is warranted, but it must
not change a target repo.

## Stage 2 — Execute the Selection

### 1. Resolve approval exactly

- `yes`, `go ahead`, or equivalent means every positively recommended numbered
  item from the immediately preceding proposal
- `only do ...` means exactly those numbered positive items
- named repos are equivalent when they map unambiguously to the proposal
- exclusions such as `except Storybook` remove that item

If the numbered mapping is no longer available in conversation context, print
the proposal again rather than guessing. A request to add an unnumbered
**Defer** or **Do not evaluate** repo is a scope change: explain what
prerequisite or boundary changed, issue a new numbered Stage 1 proposal for that
repo, and wait for its own `yes` or equivalent before spending.

Before starting, restate the selected repos and their combined disclosed spend
ceiling in one concise line. Do not ask for a second approval when the selection
already maps unambiguously to positively recommended numbered items.

The selection authorizes:

- isolated current-base worktrees for the selected owners
- temporary injection of the one required configured evaluation-only provider
  credential from Conductor's local vault into each selected isolated owner's
  ignored environment, under the owner's expected variable name
- the repo-local story/plan, adapter or evidence scaffolding, provider probes,
  bounded progressive benchmark, artifact inspection, tests, and durable eval
  records needed for the proposed lane
- spend up to each disclosed per-repo ceiling and no more than the disclosed
  selected-campaign total
- use of the proposal's clearly public or synthetic fixtures under the
  disclosed provider retention/training posture. This does not authorize
  private or unclear fixtures

It does **not** authorize:

- use of private fixtures on an unapproved provider/retention path
- copying product/runtime credentials into Conductor, copying the whole eval
  vault into an owner, changing provider-account privacy/billing settings, or
  retaining a temporary owner copy after the campaign
- spend above a disclosed ceiling or an unbounded-price call
- product prompt/golden/scorer changes that require a new preference decision
- runtime-default changes, rollout, deployment, destructive operations, commit,
  push, merge, or landing

Source-backed deterministic repair of an eval defect may proceed when the
owning repo's existing contract clearly requires it. Otherwise pause and ask
for the missing judgment without blocking unrelated selected repos.

### 2. Switch into the owning repo

When Stage 2 selects more than one repository and subagents are available,
assign each repository to its own isolated owning-repo subagent. Give each
worker only that repo's approved lane, disclosed cap, privacy boundary, current
base/worktree, and the portable owner protocol. The worker reads and follows
the repo-local instructions and returns its durable artifacts, spend ledger,
and layered owner verdict. Do not make one worker mutate or judge another
repo. Dispatch all selected owner workers before the root makes any owner
provider call; coordination should not duplicate work already assigned to an
owner.

The root agent remains campaign coordinator and final judge: it resolves
cross-repo scope, monitors aggregate spend, reviews every returned artifact and
verdict against the predeclared contract, corrects unsupported conclusions,
and produces the final synthesis. Delegation does not authorize extra repos,
broader lanes, private payloads, higher spend, commits, pushes, or rollout. If
only one repo is selected, or subagents are unavailable, the root may execute
the same owner protocol directly and must say so.

Before dispatching an owner that needs evaluation-only access, read
[the credential-custody protocol](references/credential-custody.md) completely.
Check provider presence by name only. Prefer an owner's already-configured
credential when it exists; otherwise inject one central provider key through
the helper into an ignored environment without exposing or overwriting a value.
Pass the owner worker only the provider, target variable name, ignored env path,
and cleanup requirement—not the secret. Central credential presence is access
infrastructure, not proof of callability, privacy eligibility, or transport.

For each selected item:

1. Resolve the path from `projects.yaml` and inspect its primary checkout and
   remote/base state read-only.
2. Create or reuse a dedicated `codex/` branch and isolated worktree from the
   current remote base. Reuse only when its base and existing changes belong to
   this exact campaign. Never pollute or overwrite the primary checkout.
3. Enter that worktree and read its root instructions plus relevant Ideal,
   spec, methodology state/graph, active story, eval registry, privacy and
   artifact rules.
4. Read [the owning-repo execution protocol](references/owning-repo-execution.md)
   completely. If the repo also has a local `evaluate-model` skill, read that
   `SKILL.md` completely and use its owner-specific adaptation. Otherwise adapt
   the portable protocol to the local harness.
5. When local and portable guidance differ, the owning repo controls its
   prompts, fixtures, scorers, thresholds, artifact locations, and stricter
   privacy/spend rules. Preserve the portable transport-validity, fairness,
   provenance, and layered-verdict invariants.

The work happens on behalf of the owning repo, not “from Conductor.” Provider
calls use either the owner's existing authorized credential or the one
temporary Conductor-custodied eval key injected for the selected provider.
Never copy secrets or private payloads into Conductor artifacts or commentary.
Remove a temporary injected key after the owner finishes or stops, and record
cleanup by variable name only.

### 3. Run as the owner would

Use the selected repo's normal workflow and artifact vocabulary. Create or
reuse only the durable surfaces it ordinarily requires—such as a story, scout,
attempt document, registry row, raw-artifact manifest, or regression test. Do
not manufacture every artifact type merely for portfolio symmetry.

Treat the user's selection as plan approval for the exact bounded lane already
recommended. It satisfies a repo-local approval gate only when the gate asks for
the same disclosed plan and owner-context inspection has not materially changed
the lane, gates, artifacts, privacy boundary, or spend. If local instructions
require a distinct plan review, or exploration changes any of those terms,
present the repo-local plan and pause. Otherwise continue without ceremonial
reapproval. Always pause for a material new product choice, private-data
authorization, higher spend, or broader rollout.
Routine operational recovery under the rules below is not a new selection
merely because an agent's provisional timeout, token allowance or retry default
changes. A hard user ceiling or explicit user exclusion remains binding.

Read the owner protocol reference before live execution. Qualify access and the
actual production contract before semantic scoring, use frozen maintained
inputs, and run progressively to a decision. Stop an affected lane for a clear
candidate failure against a valid required contract or source-backed quality
gate. Retain failures as access/transport/reliability evidence rather than hiding
them; do not confuse an evaluation-system failure with a candidate failure.

**Pursue recoverable problems through to conclusion.** A judge-format error,
undersized output allowance, conservative reservation estimate, timeout setting,
or other soft operational limit is a repair task, not a finished evaluation.
Diagnose it, make the smallest evidence-backed repair, validate it, and continue
within the approved task and hard budget. Rejudge saved answers instead of
rerunning subjects. Record changed settings and use matched comparison arms
where subject behavior could change. An agent-invented soft stop or zero-retry
default must not force another user approval loop for routine repair. Never
weaken quality gates or keep tuning a clearly failing candidate into a winner.
The owner protocol defines recovery and genuine hard-boundary handling.

Keep subject identity strict without overconstraining router infrastructure:

- exact requested and served model identity is mandatory; never substitute a
  different model as a fallback
- pin a provider endpoint only when the owner decision, reproducibility claim,
  pricing, quantization, privacy policy, or multiple available endpoints makes
  that route decision-bearing. Otherwise allow same-model provider routing and
  record the resolved provider
- provider fallback among endpoints serving the exact model is not itself a
  model substitution. Disable it only when route identity is decision-bearing;
  always disable model-list fallbacks to another model

For structured lanes, test the production contract first. Use strict schema
and parameter enforcement when a drop-in adoption claim depends on them. If
that route fails before a valid answer, a clearly labeled diagnostic may relax
one transport constraint on clearly public/synthetic data to measure raw model
capability. Such evidence cannot prove production parity or direct adoption;
record it as adapter-required, transport-limited, or exploratory. Do not let a
production-contract failure prevent all capability measurement when the
approved payload is safe and a bounded diagnostic can isolate the cause.
Persist the complete diagnostic response in owner-approved ignored/protected
storage before strict parsing or cleanup can discard it, then record a safe
hash and pointer. This allows offline wrapper removal and schema/scorer checks
without paying for or biasing a second model response.

Before the first paid multi-case run, perform a zero-cost resolved-harness
preflight. Inspect the rendered case matrix, conversation grouping, exact
prompt/runtime parity, selected subject and judge providers, estimated judge
cost, cache keys, concurrency, and the command that will be preserved for
reproduction. Fix or fail closed on unintended case chaining, stale prompt
snapshots, implicit judge selection, or another topology mismatch before
spending. A one-case contract probe does not replace this resolved-matrix
check.

In the owner's existing attempt record, predeclare the hypothesis, preserved
quality requirements, baseline/metric/aggregation, meaningful improvement
threshold, budget/stop conditions, and adoption/rejection/uncertainty rules.
Choose the cheapest evidence that can settle the question; an offline bound or
cached replay may justify rejection before implementation or paid calls.
Identify development versus independent-validation inputs. If validation results
guide tuning, disclose that reuse and reserve fresh material for confirmation.
Judge borderline aggregates against paired variation and sample limits rather
than treating a numerical pass as a convincing win. Allow at most one
predeclared confirmation batch for the unchanged hypothesis within authorized
scope/budget, or retain an uncertain verdict. Never rerun or select subsets until
a favorable result appears; a changed hypothesis requires a disclosed new attempt.
Use the owning repo's proportional-validation policy (or
[Conductor's policy](../finish-and-push/SKILL.md#validation-proportional-to-the-change))
to reuse applicable unchanged checks and rerun affected ones; this does not waive
the independent evidence required by the declared experiment.

Do not preserve a normal-looking aggregate command that is known to execute an
invalid topology. Repair it, make it fail closed with an actionable message, or
label and isolate it as a diagnostic command while retaining a safe owner
reproduction path.

An early stop in one lane does not cancel independent selected lanes, even
inside the same repo. Preserve honest `not measured` surfaces and finish the
other approved comparisons that can still change a decision. If a hard boundary
prevents completion, exhaust useful authorized work, prepare the concrete
recovery, and ask only for the missing decision; do not close with a shrug or a
list of stops.

### 4. Synthesize without stealing ownership

Lead the user-facing report with **what won and what to do**, not the last error
or a blanket "no adoption." Give a concise task-level comparison table covering
every evaluated repo: task, measured winner/tie/no winner, quality evidence,
task cost and latency versus the comparator, and recommended action with its
reason. State sample size, whether the comparison was fresh/matched, and the
material uncertainty without burying the recommendation. Separate subject cost
from judge/retry overhead and distinguish quality scores from pass rates.

Make a strong, evidence-proportional call: **adopt for this task**, **prioritize
this bounded promotion check**, **retain the incumbent**, or **reject for this
task**. Explain why that action has the best practical payoff. Distinguish a
measured task winner from deployment readiness; neither erase a demonstrated
win because another gate failed nor promote a small smoke-test winner beyond
its evidence. Rank the most useful next actions across the portfolio rather
than automatically pursuing the repo with the latest failure. If evidence is
inconclusive, identify the exact missing decision-bearing evidence and obtain
it within scope instead of merely recommending another round.

Explicitly consider mixed-model adoption: "use Luna for crop detection; retain
the stronger model for independent page-safety decisions" is a valid conclusion
when both roles and their interface are qualified. State which calls move,
which stay, the deterministic routing/escalation condition, combined quality,
latency and cost, and any untested routing risk. A subset must be identifiable
at runtime, not a post-hoc selection of cases the candidate happened to pass.
Do not invent a working fallback or routing policy from a model's self-reported
confidence. Recommend the split when supported; implementing it still requires
the user's rollout authorization.

Keep the full evidence in each owner's record, linked from the summary:

- worktree/branch and exact base identity
- durable evidence files and exact commands
- actual provider spend versus cap
- access, transport, reliability, capability, economics, and owner adoption
  verdicts
- stopped or unmeasured surfaces
- validation results and any remaining user decision

After a Stage 2 campaign, update Conductor's campaign scout/alignment with the
user's actual selection, links, base identities, costs, stopped surfaces, and
repo-returned verdicts. This closeout is required when execution differs from
the preserved recommendation; append a dated follow-through rather than
rewriting the original recommendation as though it predicted the later choice.
Do not copy private artifacts or duplicate the owning repo's full benchmark
record. Leave worktrees and changes uncommitted unless the user separately asks
for closeout or landing.

Also add or update the candidate in
`docs/model-watch/evaluated-models.md` before final synthesis. Do this after
every selected owner campaign that reaches an authenticated probe, provider
call, or documented access/transport stop, including zero-spend stops. Record
the canonical provider-qualified ID, aliases/checkpoints, latest attempt date,
direct owner evidence, layered outcome, and narrow retry trigger. Preserve
unmeasured verdict layers as unmeasured. This central row is a dedupe pointer;
the owning repository remains authoritative and retains the full evidence.

## Non-Negotiable Rule

Do not call a model bad when the request, provider path, harness adapter, output
contract, parser, cleanup, scorer, or judge failed before a valid answer was
produced. Keep access, transport, reliability, capability, economics, and
adoption as separate verdict layers.

## Guardrails

- Do not score pre-response infrastructure failures as semantic misses.
- Do not hide repeated instability behind a successful retry.
- Do not weaken schema, tools, modality, or input requirements to claim
  production parity. A bounded, explicitly diagnostic relaxation is allowed on
  approved public/synthetic data when it isolates raw capability and is not
  presented as adoption evidence.
- Do not alter goldens or scorers to rescue a model without source-backed
  verification and owner-contract authority.
- Do not send private fixtures through a provider path that has not cleared the
  owning repo's policy.
- Do not print, message, fingerprint, commit, or copy the whole central eval
  vault; transfer only the selected provider key through the helper.
- Do not treat possession of a central key as authorization to change an
  account privacy/billing setting or weaken an owner's payload policy.
- Do not evaluate an unselected or unnumbered repo by implication.
- Do not commit, push, merge, change defaults, deploy, or broaden rollout
  without separate explicit authorization.
