# Alignment 028 — Fresh Docs Dependency and Prompt Contract Cleanup

**Date**: 2026-05-12
**Focus**: Adapt OpenAI's docs and prompt guidance into a broader
cross-project rule for drift-prone providers, components, SDKs, model slugs,
and AI-first coding skills.

## Source

Primary inputs:

- Scout 030 on the OpenAI Docs MCP, Codex prompting guide, GPT-5.5 prompt
  guidance, `openai-docs` skill, and upgrade guide.
- Cam's follow-up: fresh docs as an active dependency should apply to all
  components and API providers, not only OpenAI.
- Existing Conductor methodology: Ideal/spec/compromise/eval surfaces define
  local product truth, while scout/alignment memory prevents repeated external
  research.

## Classification

Portable improvement with shared-skill wording, not a new central provider
registry.

The repeated failure mode is treating stale memory, old SDK assumptions, or
docs naming as enough evidence for provider/component decisions. That is
different from product value. Current upstream docs can prove what an external
surface supports today, but they cannot prove the change belongs in a tracked
project. Local Ideal/spec/eval surfaces still own that judgment.

## Decision

Treat current upstream docs as an active dependency when work touches
drift-prone external surfaces:

- API providers and hosted services
- SDKs and client libraries
- model/provider slugs and capability claims
- browser automation, Codex, MCP, or tooling plugins
- UI/component libraries and frontend frameworks
- auth, payment, storage, database, deploy, audio, media, and transcription
  providers

Use the narrowest current official source first: source-specific connector,
first-party docs, release notes, changelog, official repository, or provider
API discovery. Do not classify a model/provider/component as live, dead,
compatible, or worth routing from memory alone when the official source is easy
to check and likely to drift.

This rule is scoped by risk and drift. Stable repo-local behavior can still use
local tests, local docs, and current code first when no external interface fact
is at issue.

## Prompt Contract Cleanup

OpenAI's model-era guidance is useful where it pushes prompts and skills toward
outcome-first contracts:

- define what good looks like
- name constraints
- name available evidence
- name the final answer or artifact shape
- leave room for the model to choose an efficient path

That is better than carrying every process-heavy instruction forward forever.
However, the tracked repos already have valuable local guardrails that should
stay:

- exact checkout/path fidelity
- dirty-worktree and isolated-worktree rules
- destructive git limits
- UI/browser/live-artifact proof requirements
- eval and golden completeness gates
- provider/model freshness gates
- data-loss, privacy, and externally visible action boundaries

The strategic adoption rule is therefore: trim generic process ballast, but do
not delete failure-proven guardrails.

## Shared Skill Changes

Conductor now carries the rule in the shared workflow surfaces:

- `/scout` uses official/provider docs and source-specific connectors before
  generic commentary for provider/component/model sources.
- `/triage inbox` routes provider/component/model notes with current upstream
  docs instead of stale memory alone.
- `/build-story` identifies upstream evidence before implementation when a
  story touches drift-prone external surfaces.
- `/validate` checks that such evidence exists or that the story explains why
  local docs/tests are sufficient.
- `/setup-methodology` installs the fresh-doc dependency rule and the
  outcome-first prompt contract rule as part of the shared package.

## Recommendation

Keep this as an alignment/story-prep improvement now. Do not create a central
provider registry, do not install new MCP servers across every repo, and do not
rewrite every repo prompt or provider default.

Target-project rollout is warranted only for the shared skill surfaces that are
already intended to stay portable. Any product-specific provider change still
needs its own repo-local story, eval, or inbox note.

## Stop Conditions

- Do not browse official docs ritualistically when the task is purely local and
  no external interface or provider fact matters.
- Do not treat upstream docs as product acceptance. They prove current external
  facts; local Ideal/spec/evals prove local fit.
- Do not promote provider/model defaults without measured quality, latency,
  cost, compatibility, and product evidence.
- Do not mutate target repos from Conductor unless the work has an explicit
  isolated worktree and scoped rollout plan.

## Practical Impact

This reduces stale-provider mistakes and model-release churn without creating a
new bureaucracy. Agents get a clear trigger for when to refresh external truth,
and Cam keeps the existing product-specific proof system as the final decision
surface.
