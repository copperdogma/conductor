# Alignment 056 — Continuing reviewer and independent milestone reviews

Date: 2026-10-08 (America/Edmonton)
Status: **All 12 owner landings verified; Conductor skill and supervisor record published together**
Classification: portable improvement, preserving owner cadence and review boundaries
Predecessor: [Alignment 055](align-055-agent-staffing-and-event-waits.md)

## Intended improvement

Reduce repeated orientation during periodic strategic reviews while retaining
an independent challenge of the executor's assumptions. Cam approved drafting
this policy, then explicitly requested rollout to every repo already having the
skill, with commits and pushes. Running-thread messages remain outside scope.

## Proposed skill wording

### Reviewer continuity and independence

For repeated strategic checkpoints on one active story or goal, default to one
continuing reviewer with its own conversation, separate from the executor.
Reuse that reviewer through the runtime's supported follow-up mechanism.
Completion of one review does not alone require a new reviewer. If the reviewer
cannot be resumed, start a replacement with a compact review-state summary and
record the continuity gap. Do not imply that its original full history survived.

Preserve the user's requested model, thinking level, cadence, scope, and budget.
Where no model is specified, retain the owning skill's eligible-model selection
policy. Reviewer reuse does not authorize a weaker configuration. Record the
requested configuration separately from independently verified served identity.

At the first checkpoint, give the reviewer the user's intended outcome,
constraints, acceptance criteria, current artifact locations, relevant evidence
and unresolved decisions. For later checkpoints, append a concise update:

- Changes and measured results since the last review, including useful failures.
- Previous recommendations, their disposition, and evidence of follow-through.
- Current blocker or decision, relevant alternatives, and evidence links.
- Remaining authorized budget/time and the existing next checkpoint.

Distinguish observed facts, executor interpretations, and open hypotheses. Give
the reviewer access to primary artifacts so it can test the update rather than
accepting the executor's account. Do not flood its history with routine polling,
raw logs, or the executor's full reasoning narrative. The reviewer may request
or inspect additional decisive context when the compact packet is insufficient.

Request a fresh independent reviewer at a meaningful milestone, such as a
completion or adoption claim, a consequential change in approach, or conflicting
evidence that suggests the continuing reviewer is stuck. User-required fresh
reviews and independent-validation gates take precedence. Use judgment about
consequence; a routine implementation checkpoint is not automatically a new
milestone and does not require a second review.

Give the fresh reviewer the intended outcome, constraints, artifacts and
measured results. Ask it to form its initial assessment before reading the
executor's or continuing reviewer's verdict; then reconcile disagreements with
evidence. Do not withhold material failed results, constraints or contrary
evidence in pursuit of a clean framing. A fresh conversation improves separation
of framing but does not prove statistical independence or unbiased judgment.

Avoid full-history executor forks as the default review handoff. Use one when
the decision requires extensive chronological context that targeted evidence
cannot adequately supply, and explain the tradeoff. Raising effort in the main
thread can aid self-checking but does not satisfy an explicitly independent
review requirement. A fork also does not automatically satisfy that requirement.

Keep the reviewer bounded and read-only unless implementation is separately
authorized. The main agent owns integration, disposition and follow-through.
Continue useful independent work while review runs; wait for native completion
or actionable messages when the next step depends on the result. Preserve the
existing cross-thread messaging authorization rules and avoid duplicate pings.

Retain reviewer identity, latest disposition and last/next checkpoint in the
existing work log. Do not add a separate reporting system. When its history
becomes noisy or stale, prepare a compact state summary and replace or compact
the reviewer using supported mechanisms. Recheck decisive claims against
artifacts; neither compaction nor resumption guarantees verbatim full history.

### Cost and cadence

Treat reviewer reuse as a hypothesis about reducing repeated investigation and
reasoning. Saved conversation history still contributes input context; an idle
reviewer does not guarantee a warm computation cache. Model changes, context
rewriting, expiry and routing can affect cache reuse. Do not add keep-alive calls
or shorten a user-requested review interval merely to preserve a cache.

Where existing telemetry permits, compare input, cached input, output/reasoning
usage and repeated evidence-gathering work across comparable checkpoints. Report
unavailable attribution and quality differences; do not infer a quota-saving
percentage from spawn counts or API discounts alone. This policy does not
authorize paid experiments, additional reviews, account changes or extra budget.

## Evidence and uncertainty

The preceding read-only inspection found repeated fresh hourly Astra Ultra
reviewers in Ultima IV Stories 007, 008 and 009, alongside substantial existing
reviewer reuse in Story 005. This establishes that both dispatch patterns occur;
it does not establish which is cheaper or better on matched decisions.

Official documentation consulted on 2026-10-08:

- [Codex thread lifecycle](https://learn.chatgpt.com/docs/app-server#threads):
  stored threads can be resumed; storage and loaded runtime state are distinct.
- [Conversation state](https://developers.openai.com/api/docs/guides/conversation-state):
  prior context remains input; response chaining does not make history free.
- [Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching):
  matching rendered prefixes matter; GPT-5.6 and later have a default minimum
  cache lifetime of 30 minutes after write/reuse, possibly longer. An hourly
  review cannot assume a hit. This API contract is not proof of a particular
  Codex session's cache settings or observed hits.
- [Changing reasoning effort](https://developers.openai.com/api/docs/guides/reasoning#change-reasoning-mid-conversation):
  supported GPT-6 API configuration updates change effort within a model;
  they do not establish autonomous model switching on every Codex tool surface.
- [Codex subagents](https://developers.openai.com/codex/agent-configuration/subagents):
  separate conversations can reduce context pollution, but delegation adds work.
- [Codex pricing](https://learn.chatgpt.com/docs/pricing):
  cached input has separate credit rates; those rates alone do not determine
  included subscription usage. API and Codex credit billing differ.

Recommendation: adopt this as a workflow default after approval, then assess
the next naturally occurring checkpoints from existing telemetry. No new paid
benchmark or extra review is needed to begin observing applicability. Remaining
uncertainty: actual savings, comparative review quality, reviewer availability
across runtime restarts, and how well concise updates preserve decisive context.

## Draft validation and next action

Documentation-only review: checked policy against the current loop-review
cadence, research/reuse, read-only, follow-through and authorization boundaries.
Walked through routine checkpoints, milestone disagreement, unavailable reviewer,
compacted history, missing telemetry and exhausted budget. These are policy
consistency checks, not executed runtime or cost experiments.

## Approved rollout and discovery

Cam selected every repository already having loop-review. This explicit scope
satisfies target selection without enrolling or removing registry members.
The managed list is Dossier, Storybook, Doc Web, CineForge, Board Game Ingester,
Robo Rally, Echo Forge, Ultima IV Web, Financial Hub, Financial Monthly Analysis,
and VLC Thumbs. Conductor plus the existing copies in Ravenloft Cthulhu,
RPG Map Projector and Canmore Town Council are included in this approved rollout.
Both finance repos have no skill and retain manual checkpoints.

Discovery compared the current app project list and 81 unique Git common
directories under Projects (through three directory levels) plus the external
app roots Hardware Specs and Matt's campaign images. Nested VLC and Storybook
repos are included; historical worktree copies were deduplicated. Existing local
or remote-tracking skill presence selected candidates; every selected origin was
then fetched. All 13 selected remote main branches contain the skill. This is a
bounded local/app inventory, not an exhaustive search of every disk or host.
Hardware Specs and Lightbox Sky show recent activity but have no skill; other
unselected local repos also lack a discovered copy. Registry membership unchanged.

Dedicated worktrees live under
`/Users/cam/.codex/worktrees/align056-reviewer-continuity/<repo-key>` on each
repo's `codex/align056-reviewer-continuity` branch from current `origin/main`.
Primary checkouts remain untouched, including unrelated dirty files and commits.
The published skill is an owner-local adaptation retaining existing model,
cadence, research, waiting, approval and clean-stop rules. The old direct-main
review allowance is reconciled: recurring reviews use a separate reviewer;
one-off self-checks remain allowed unless independent review is required.

### Checkout constraint and local demonstration

Problem class: large tracked media makes full isolated checkouts exceed available
local disk. Git's [worktree manual](https://git-scm.com/docs/git-worktree) explicitly
supports `--no-checkout` for sparse-checkout preparation; the
[sparse-checkout manual](https://git-scm.com/docs/git-sparse-checkout) documents
worktree-specific sparse settings. Adopted sparse dedicated checkouts for large
repos, retaining the skill, instructions and required validation files. Failed
new checkouts were recovered without deleting user data. Local skill/doc checks
and commit scope establish applicability here; sparse checkout does not qualify
product behavior. Existing primary checkouts were not sparsified.

### Validation and landing evidence

[Rollout receipt](evidence/align-056-reviewer-continuity.json) records per-repo
base, isolated path/branch, scoped commit, skill hash, applicable owner checks,
remote landing verification and any limits. Documentation-only scope uses skill
wiring, methodology/provenance checks where applicable, diff review and whitespace
checks. No paid model calls or gameplay/native media tests are needed for this
instruction change. No claim of measured quota savings is made.

Landing all selected owners precedes the final supervisor record. No running
thread is messaged, restarted or claimed to have loaded the new skill. Existing
active agents/checkouts may retain older instructions until their owner loads
the landed version; preserving active work takes precedence over forcing refresh.

Owner landing verification: all twelve non-Conductor remote main and execution
branch tips equal their scoped commits in the receipt. Ravenloft's legacy
instructions reference an absent checker/runbook; manual frontmatter, exact
policy/preserved-content review and whitespace validation passed instead. This
limit is recorded rather than represented as an automated checker pass. Conductor
passes skills-check, methodology-check and lint; its enclosing publication commit
is verified on remote main by the coordinator after push. No follow-up work is
required for this scoped rollout. Active-thread loading and quota savings remain
unmeasured.
