# AGENTS.md — Conductor

Read this file at the start of every session.

> **Mission:** Conductor is the supervisor project for Cam's active AI-first
> projects. It reduces cross-project busywork by routing notes, comparing
> infrastructure drift, scouting external ideas, and preparing project-specific
> adoption work.

## Core idea

Conductor is **not** the canonical copy of the harness. The harness remains
distributed across the tracked projects.

Conductor exists to:

- compare those distributed surfaces when asked
- explain where they differ and why
- recommend what should sync, what should stay local, and what needs a human decision
- turn raw links and notes into ready work

## Operating rule

Start planning from:

- `docs/ideal.md`
- `docs/spec.md`
- `docs/methodology/state.yaml`
- `docs/methodology/graph.json`
- `projects.yaml`
- `inbox.md`
- `docs/align-projects.md`
- `docs/scout.md`

Implementation starts from the active story, but the graph/state context still
defines whether the work is alignment, scouting, routing, or memory upkeep.

## Central tenets

1. **Canonicalize meaning, not text** — exact file identity is not the goal.
2. **Divergence is expected when justified** — local adaptation is healthy when explicit.
3. **Recommendations before sync** — propose changes before forcing multi-project edits.
4. **One capture surface** — raw notes belong in `inbox.md`, not scattered scratchpads.
5. **Human judgment at conflicts** — methodology conflicts should be surfaced clearly, not hidden.
6. **Smallest useful overhead** — Conductor exists to remove work, not create a bureaucracy.

## Core surfaces

- `projects.yaml` — tracked project registry and comparison surfaces
- `inbox.md` — raw capture surface
- `docs/align-projects.md` + `docs/alignments/` — internal cross-project alignment memory
- `docs/scout.md` + `docs/scout/` — external source scouting memory
- `docs/stories/` — supervisor stories
- `docs/decisions/` — hard-to-reverse workflow or architecture choices

## Content connectors

For Conductor-only scouting and routing work, prefer the available content MCPs
over generic browsing when the source matches them:

- `Twitter Scraper` — use for X/Twitter URLs, tweet IDs, tweet replies, and
  account lookups
- `YouTube Transcripts` — use for YouTube URLs when you need transcript or
  video metadata
- `Project Agent` — use for Obsidian project documents or notes when the
  source likely lives in Cam's project vault

Use the source-specific connector first, then fall back only if it fails or the
request clearly needs something else.

## Workflow

Default loop:

1. capture in `inbox.md`
2. `/triage`
3. `/create-story` when warranted
4. `/build-story`
5. `/validate`
6. `/mark-story-done`

Specialized loops:

- `/init-project` for interview-first greenfield kickoff before setup
- `/align-projects` for cross-project infrastructure drift
- Cross-repo skill, methodology, and shared-infrastructure rollout requests
  also use `/align-projects`, beginning with its managed-project check: discover
  new repos, show the existing list, and resolve requested additions/removals
  before choosing rollout targets.
- `/loop-review` for strategic checks of long-running work against user intent,
  applying or handing off a proposed course correction only when authorized
- `/scout` for external sources and adoption analysis
- `/evaluate-model` for current model/API verification, portfolio-fit
  recommendations, reproducibility requests, evidence audits, and approved
  repo-local execution. Conductor first returns numbered evaluation choices;
  after the user selects all or a subset, it enters isolated owning-repo
  worktrees where each repo runs and judges its own maintained benchmark,
  temporarily supplying only the selected provider's designated eval key when
  the owner lacks one
- `/ideation` for optional divergent option generation before Ideal/spec,
  story, or ADR decisions when option quality is the blocker
- `/setup-methodology` for refreshing this project's own methodology package

## Working norms

- When a nontrivial obstacle makes the next step uncertain, inspect enough
  local evidence to name the general problem class, then check established
  approaches before inventing a workaround. Reuse applicable prior research;
  otherwise consult a few primary sources, retaining the constraints that
  affect applicability. Stop once you can choose an approach and a small local
  test. Prefer the simplest permitted technique that fits; explain material
  departures. If attempts keep failing, revisit the diagnosis and assumptions
  before adding retries or special cases. Record reusable sources, the
  decision, local evidence, and uncertainty in existing project notes. Obvious
  fixes need no research ceremony. Preserve project reuse boundaries and
  acceptance criteria.
- In long-running work, use `/loop-review` to periodically challenge the
  approach against the intended outcome and established alternatives, even
  when local metrics improve. Preserve a requested cadence; otherwise use
  roughly 30 minutes of active work or three substantive rounds, whichever
  comes first, as a tunable default within the authorized run. `/loop-verify`
  keeps its round checks and earlier stop rules. Reuse applicable source
  comparisons, carry cadence across interruptions, and charge research to the
  existing budget. This does not create a schedule or extend work past a stop.

- For strategic loop reviews, use the strongest available eligible model at its
  maximum supported thinking level, resolved from current runtime capabilities.
  Follow `/loop-review` for selection evidence and one bounded read-only
  reviewer when the main agent is not already suitably configured. Existing
  scope, access, privacy, budgets and clean-stop rules prevail.
- Use the cheapest capable workers when delegation saves more than context,
  coordination and verification overhead. Give bounded packets and direct
  artifact access. Do independent work or use message-aware completion waits;
  avoid unchanged status sweeps, duplicate work and watcher agents when native
  events suffice. Child mailboxes and separate user-owned chats have distinct
  authorization and continuation contracts.

### Decision models

Decision models are an architecture option for bounded semantic judgments over
supplied context, including TypeSafe's Jev and OpenAI's announced Decisions API.
Consider them for routing, candidate selection, evidence checks and ranking when
heuristics or a full generative call are a poor fit. When changing semantic
decision logic, compare deterministic code, a decision model and a language model
and explain the choice. Keep exact rules, arithmetic, identities, permissions and
execution in code; use language models for generated text and open-ended outputs.
Read [the local guide](docs/decision-models.md) and current provider docs before
designing an integration. Respect owner evaluation verdicts, privacy and enablement
gates. Measure complete behavior, fallback, quality, latency and cost before
adoption; typed answers or concentrated probabilities do not prove correctness.
Conductor routes evaluations to owning repos; awareness does not authorize a paid
campaign or a runtime change.

### Handoffs

- When reporting technical work, include 1-2 plain-language lines on what
  improved for Cam or the target projects, what practical risk or annoyance
  got smaller, or what they should notice next.
- End most completed-task handoffs with one recommended next step phrased so
  Cam can approve it with a simple `yes`. Prefer the explicit form: Reply
  `yes` to proceed with: ... when there is one clear next move. If there is no
  honest next step, say so explicitly.

## Guardrails

- Do not assume the newest project change should propagate everywhere.
- Do not collapse intentional project-specific differences into fake "drift."
- Do not create a heavyweight canonical core unless the user explicitly wants one.
- Do not describe sync work as complete until the target projects have their own
  stories, patches, or applied changes.
- When Conductor needs to modify a tracked project repo directly, do that work
  in a dedicated git worktree/branch for that repo, not in the project's
  primary checkout, unless the user explicitly asks to work in place.
- Treat an active target-project checkout as shared workspace: supervisor
  upgrades should be quiet, isolated, and easy to land or discard without
  polluting the project's live work environment.
- An approved cross-project evaluation remains repo-local work: read and obey
  each owning repo's instructions, fixtures, privacy, gates, artifacts, and
  verdict contract rather than running a synthetic substitute in Conductor.
  Conductor may inject one configured eval-only provider key through its safe
  helper; never expose the value, copy the whole vault, overwrite an owner key,
  or infer permission to change provider account settings.
- No implicit commits or pushes.

For close-out, including `/validate` and `/mark-story-done` handoffs, use the
validation selection and evidence-reuse policy in
`.agents/skills/finish-and-push/SKILL.md`. Local commands supply the applicable
checks; generic full-suite/current-pass wording does not require rerunning
unchanged inputs. Preserve explicit task acceptance and mandatory CI gates.
