# Scout 025 — Evaluate OpenAI Symphony for Conductor Orchestration

**Source**: `https://openai.com/index/open-source-codex-orchestration-symphony/`
**Status**: Adapt
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Reviewed OpenAI's Symphony post and the public `openai/symphony` repository on
2026-04-29. Symphony is an issue-tracker-driven orchestration spec and
reference implementation: it watches work items, creates isolated workspaces,
runs coding agents against those items, retries or reconciles runs, and leaves
humans to review higher-level work outcomes instead of supervising individual
agent sessions.

The strongest match to Conductor is conceptual, not mechanical. Symphony names
a real pressure Cam already has: too much manual context switching between
inbox notes, stories, worktrees, validation, and follow-up issues. It also
matches Conductor's current direction around isolated worktrees, repository
owned workflow policy, explicit validation and handoff states, and subagent
orchestration contracts.

The wrong move would be to import Symphony as a hard Linear dependency or start
running an always-on daemon before Conductor has a narrower local control-plane
problem. Conductor already has a lightweight control plane: `inbox.md`, stories,
alignment logs, scout logs, methodology graph/state, and explicit skills. The
portable improvement is to adapt Symphony's work-item lifecycle and observably
managed runs into those existing surfaces before considering an external issue
tracker.

## Project Relevance

- **conductor**: `Adapt`. Strongest fit. Use Symphony as a reference for
  work-item orchestration, isolated execution, retry/recovery language,
  operator-visible run status, and a repo-owned workflow policy. Do not replace
  Conductor's lightweight local stories with Linear yet.
- **dossier**: `Defer`. Dossier may eventually benefit from better queued
  research/extraction work, but its current loop is still repo-local
  methodology, eval, and document-workflow execution. Any orchestration should
  come through Conductor first.
- **storybook**: `Defer`. Storybook has plausible future background-agent and
  follow-up-task needs, but current work should stay on its product stories and
  eval-backed lifecycle. A Symphony-like runner would be premature.
- **doc-web**: `Defer`. Doc Web already has durable pipeline/run concepts in
  its document workflow. Symphony is useful as orchestration reference only if
  agent-managed issue execution becomes the bottleneck.
- **cine-forge**: `Defer`. CineForge already owns long-running action and
  provider-health concerns locally. Symphony may be useful later for parallel
  implementation or CI shepherding, not for current previz/product pressure.
- **boardgame-ingester**: `Defer`. Current value is low; the repo is still
  building ingestion/eval substrate where direct stories and focused validation
  are enough.
- **roborally**: `Reject`. The private proof-of-concept game does not need a
  project-management orchestrator now.
- **echo-forge**: `Defer`. Could benefit later if the app accumulates many
  parallel feature or QA tasks, but current greenfield methodology and
  product-shaping work should stay lightweight.

## Recommendation

- Keep this scout as `Adapt`.
- Do not install Symphony, depend on Linear, or create an always-on daemon yet.
- Do not hand off new ambient inbox items to the product repos.
- Treat Symphony as a Conductor-side design reference for:
  - one work item as the unit of orchestration
  - isolated per-item workspaces
  - explicit active, blocked, review, and terminal states
  - repo-owned workflow policy instead of out-of-band operator memory
  - bounded concurrency, retry, reconciliation, and stall handling
  - proof-of-work packets that make review cheap
- If Conductor accumulates repeated friction around monitoring several active
  stories or target worktrees at once, create a Conductor story to define a
  local "work-item control plane" using existing stories and methodology state
  before considering Linear integration.
- If Linear becomes desirable later, evaluate it as a separate adoption choice:
  the key decision is not Symphony itself, but whether Cam wants an external
  tracker to become the authoritative control plane for local AI work.

## Evidence

- OpenAI's post describes Symphony as an orchestrator that turns a
  project-management board such as Linear into a control plane for Codex agents,
  with active tasks mapped to dedicated agent workspaces.
- The post emphasizes the motivation as reducing context-switching and human
  micromanagement across multiple agent sessions.
- The public repository describes Symphony as isolated autonomous
  implementation runs with CI status, PR review feedback, complexity analysis,
  and walkthrough-video proof of work.
- The repository warns that Symphony is an engineering preview for trusted
  environments.
- The public `SPEC.md` defines Symphony as a long-running service that reads an
  issue tracker, creates isolated workspaces, runs coding-agent sessions,
  documents trust/safety posture, and loads runtime behavior from a
  repository-owned `WORKFLOW.md`.
- The spec explicitly says Symphony is a scheduler/runner and tracker reader;
  ticket writes and business logic live in workflow prompts and agent tooling.
- Source: `https://openai.com/index/open-source-codex-orchestration-symphony/`
- Source: `https://github.com/openai/symphony`
- Source: `https://raw.githubusercontent.com/openai/symphony/main/SPEC.md`

## Confidence

High for the fit judgment. The sources are official OpenAI materials and the
Conductor overlap is direct. Medium for implementation timing because the real
trigger is operational pressure: whether Cam wants persistent work tracking
outside the current local story and inbox flow.

## Open Questions

- Should Conductor eventually track active story/worktree runs in one status
  surface, or is the current explicit skill-by-skill loop still enough?
- Would Cam actually use Linear as a control plane, or would that add more
  overhead than it removes?
- What is the smallest proof packet that would make multi-agent work review
  cheaper across Conductor-managed target worktrees?
