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

- `/align-projects` for cross-project infrastructure drift
- `/scout` for external sources and adoption analysis
- `/setup-methodology` for refreshing this project's own methodology package

## Working norms

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
- No implicit commits or pushes.
