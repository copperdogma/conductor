---
title: "Fresh Docs Dependency and Prompt Contract Cleanup"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I4"
  - "I5"
spec_refs:
  - "spec:1.1"
  - "spec:2.2"
  - "spec:3.2"
  - "spec:4.2"
  - "spec:5.1"
  - "spec:5.2"
  - "spec:5.3"
decision_refs:
  - "ADR-001"
  - "ADR-002"
depends_on: []
category_refs:
  - "alignment"
  - "scouting"
  - "story-prep"
  - "memory"
tracked_projects:
  - "conductor"
  - "dossier"
  - "storybook"
  - "doc-web"
  - "cine-forge"
  - "boardgame-ingester"
  - "roborally"
  - "echo-forge"
---

# Story 011 — Fresh Docs Dependency and Prompt Contract Cleanup

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: None

## Goal

Turn Scout 030 and the follow-up discussion into a portable supervisor rule:
fresh upstream documentation is an active dependency for OpenAI work and for
all major component/API provider work, not a one-off OpenAI lookup habit.

The story should adapt the OpenAI guidance strategically rather than copying it
wholesale. The existing project structure is the durable advantage:
`ideal.md` defines what good means, `spec.md` defines active constraints,
compromise/eval surfaces define intentional gaps and deletion gates, and
repo-local skills/AGENTS files route execution. The OpenAI guidance is better
where it pushes newer-model prompts toward outcome-first contracts and away
from inherited process-heavy prompt stacks. The adoption path is therefore:
keep the Ideal/spec/eval spine, make current upstream docs a required evidence
source for drift-prone dependencies, and trim redundant process ballast from
shared skills only where the local guardrail is not tied to a known failure.

The practical result should be a small, reusable policy plus one proof edit on
the shared methodology/skill surface. It should help future agents answer:
"which current upstream docs must be checked before touching this provider,
component, model, SDK, or plugin, and which local eval proves the change is
safe?"

## Acceptance Criteria

- [x] Conductor records a fresh-doc dependency rule that applies beyond
      OpenAI: API providers, SDKs, browser/tooling plugins, UI/component
      libraries, auth/payment/storage providers, and model/provider surfaces
      should use current upstream docs when behavior or interfaces may have
      drifted.
- [x] The rule is scoped by risk and drift, not applied as ritual browsing:
      stable repo-local behavior can still use local docs/tests first, while
      version-sensitive or provider-sensitive work must verify upstream docs
      before implementation or recommendations.
- [x] The story distinguishes durable local truth from external truth:
      Ideal/spec/compromise/eval surfaces remain the acceptance contract;
      upstream docs provide current interface/model/platform facts.
- [x] The story produces or updates one Conductor alignment record explaining
      where OpenAI's guidance is better than the current shared methodology and
      where the current methodology should remain stronger.
- [x] At least one shared skill or methodology surface is patched with the
      smallest reusable wording for fresh-doc dependencies and
      outcome-first prompt contracts.
- [x] The patch explicitly avoids blanket prompt rewrites, blanket provider
      default changes, and broad repo-by-repo churn without a concrete
      model/component/provider change.
- [x] If target-project propagation is recommended, it is framed as
      repo-local adoption work or isolated-worktree rollout, not direct edits in
      active primary checkouts.
- [x] Conductor methodology outputs are regenerated and checked.

## Out of Scope

- Rewriting every repo skill or AGENTS file just to mention docs freshness.
- Changing production model defaults, provider routing, SDK versions, or
  prompt templates without repo-native eval/spot-check evidence.
- Installing new MCP servers, provider SDKs, or plugins across tracked repos.
- Treating OpenAI documentation as canonical for non-OpenAI providers.
- Replacing repo-local Ideal/spec/eval truth with upstream vendor guidance.
- Creating a heavyweight central provider registry unless the implementation
  proves the repeated work is worth that structure.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Re-read Scout 030 and adjacent model/provider/eval alignment memory
- [x] Identify the smallest shared surface that should carry the fresh-doc
      dependency rule
- [x] Classify current process-heavy skill text into real guardrails versus
      model-era ballast
- [x] Implement the needed doc, skill, script, or log changes
- [x] Create or update alignment memory with the strategic adoption decision
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: `make test` not required; no scripts
        or repo checks changed
- [x] Search docs and update any related surfaces
- [x] Verify Conductor tenets:
  - [x] I1 — Meaning over text
  - [x] I2 — Distributed ownership
  - [x] I3 — Recommendation-first supervision
  - [x] I4 — Honest divergence
  - [x] I5 — Minimal overhead

## Workflow Gates

- [x] Build complete
- [x] Validation complete or explicitly skipped by user
- [x] Story marked done via `/mark-story-done`

## Files to Modify

- `docs/stories/story-011-fresh-docs-dependency-and-prompt-contract-cleanup.md`
  — story source of truth.
- `docs/alignments/` and `docs/align-projects.md` — expected alignment record
  and index entry for the strategic adoption decision.
- One or more shared methodology/skill surfaces, likely
  `.agents/skills/setup-methodology/SKILL.md`, `.agents/skills/triage/SKILL.md`,
  or another narrow owner chosen during `/build-story`.
- `docs/scout/scout-030-openai-docs-prompting-bundle.md` — update only if the
  adoption decision materially sharpens the scout.
- Generated methodology surfaces after compile:
  `docs/stories.md` and `docs/methodology/graph.json`.

## Notes

- Source discussion:
  - Scout 030: OpenAI docs/prompting bundle should be adapted narrowly.
  - Follow-up conclusion: fresh docs as an active dependency should apply to all
    major components and API providers, not just OpenAI.
  - Strategic interpretation: OpenAI guidance is strongest where it tells us to
    define outcomes, constraints, evidence, and final answer shape instead of
    carrying inherited process stacks forward forever.
- Existing structure to preserve:
  - Ideal/spec define product truth and constraints.
  - Compromise/eval surfaces define accepted gaps and proof/deletion gates.
  - Skills and AGENTS route execution and known guardrails.
  - Conductor recommends and records alignment before broad sync.
- Candidate provider/component classes:
  - OpenAI, Anthropic, Google/Gemini, xAI, ElevenLabs, Deepgram, Stripe,
    Supabase/Postgres, Vercel/hosting, browser automation tools, React/Next,
    Vite, shadcn/ui, Tailwind, Playwright, and repo-specific SDKs.
- Important distinction:
  - Upstream docs answer "what is true about this moving external surface now?"
  - Repo-local evals answer "is this change good and safe for this product?"

## Plan

Proposed `/build-story` shape:

1. Patch `/scout` and `/triage` with source-routing rules for provider,
   component, model, SDK, plugin, and framework notes.
2. Patch `/build-story` so implementation planning identifies current upstream
   evidence before touching drift-prone external surfaces.
3. Patch `/validate` so findings-first review checks for current upstream
   evidence or an explicit local-only rationale when diffs touch those
   surfaces.
4. Patch `/setup-methodology` with the two strategic rules:
   - fresh upstream docs are an active dependency for drift-prone external
     surfaces
   - outcome-first prompt contracts should replace generic process ballast
     while preserving failure-proven local guardrails
5. Create Alignment 028 and index it from `docs/align-projects.md`.
6. Update Scout 030 to point to the broader adoption decision.
7. Run `make methodology-compile`, `make methodology-check`, `make lint`,
   `make skills-check`, and `git diff --check`.
8. Run `/loop-verify` across the changed story/alignment/skill surfaces until a
   full clean material round or a clear blocker.

## Work Log

20260512-0000 — `/create-story` from Scout 030 follow-up: created this story
after Cam agreed with the OpenAI prompt-contract cleanup recommendation and
expanded "fresh docs as active dependency" to all major components and API
providers. This is now a Conductor alignment/story-prep problem, not just an
OpenAI scout note. Next step: `/build-story 011`.

20260512-0018 — `/build-story 011` implementation: patched shared routing and
story-loop skill surfaces (`/scout`, `/triage`, `/build-story`, `/validate`,
and `/setup-methodology`), added Alignment 028, indexed it from
`docs/align-projects.md`, and linked Scout 030 to the broader decision. The
rule is intentionally scoped: upstream docs prove current external facts, while
repo-local Ideal/spec/compromise/evals remain the acceptance contract. Target
repo propagation is not claimed complete; Alignment 028 records that shared
skill rollout would need explicit isolated worktrees if pursued. Next step:
compile/check, then loop-verify the changed surfaces.

20260512-0027 — Round 2 shard verification: confirmed the Story 011 generated
surfaces are current after `make methodology-compile`; `make methodology-check`,
`make lint`, `make skills-check`, and scoped `git diff --check` passed. The
test target was not required because no scripts or repo checks changed in this
shard.

20260512-0042 — `/loop-verify` converged after four full rounds. Material fixes
landed in early rounds for triage's version-sensitive docs trigger, the
full `Ideal/spec/compromise/evals` acceptance contract, setup-methodology's
target-repo propagation boundary, and the local-only rationale escape hatch.
Round 4 returned `RESULT: no-issue` across setup-methodology, story/alignment,
and source-routing/story-loop shards. Final checks passed:
`PYTHONDONTWRITEBYTECODE=1 make methodology-compile`,
`PYTHONDONTWRITEBYTECODE=1 make methodology-check`,
`PYTHONDONTWRITEBYTECODE=1 make lint`, `make skills-check`, and
`git diff --check`.

20260512-0045 — `/mark-story-done 011`: marked Story 011 done after current-pass
validation, added the changelog entry, and regenerated methodology outputs.
