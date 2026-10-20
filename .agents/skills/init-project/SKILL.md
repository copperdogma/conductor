---
name: init-project
description: Interview-first greenfield project kickoff. Use when the user has a new repo, raw idea capture, docs/initial-concept.md, or an existing unshaped project and wants to start, bootstrap, kick off, or choose which methodology/framework pieces to use. Can be run by pointing a blank-repo agent at this Conductor skill file. Produces a discussed setup plan before any project scaffolding.
user-invocable: true
---

# /init-project [repo-path|new-idea|from-seed|from-existing]

Use this skill to turn a raw project seed into an agreed kickoff plan. It is
not an autonomous scaffolder. The first deliverable is a conversation: what the
project appears to be, what setup options are available, what the agent
recommends, why, and what the user wants to change before setup begins.

This skill often runs from a brand-new target repo that has no local
`AGENTS.md`, skills, stories, or methodology files yet. In that case, keep two
roots separate:

- **Conductor source root**: the repo containing this `SKILL.md`.
- **Target project root**: the new repo being kicked off.

For every target mutation, use an absolute destination or an explicit tool
working directory at the verified target root. Reading a source skill by path
never changes the tool's current directory. Do not run relative writes from
Conductor. If a command touches the wrong checkout, stop and report it; do not
restore from Git HEAD over possibly uncommitted work.

Always read the companion runbook when it is available. Resolve it relative to
this file by replacing `.agents/skills/init-project/SKILL.md` with
`docs/runbooks/new-project-kickoff.md` in the Conductor source root. If the
runbook is unavailable, continue with this skill's embedded workflow.

## Boundaries

- Preserve raw intake such as `docs/initial-concept.md`; do not overwrite it.
- Conductor maintains the canonical reusable skills and methodology. Select
  relevant pieces from its source root; use other projects as evidence for
  adaptations, not as competing master packages. Do not copy any repo wholesale.
  Keep target-project requirements and justified local differences.
- Do not create or modify target-repo files until the user approves a named
  setup action. A bare `yes` approves only the plan you just stated, not commit,
  push, or cross-repo rollout.
- If the user asks only for advice, stop after the kickoff brief.
- Do not assume the target repo is a git repo or has package/runtime tooling.
- If the target is an existing tracked project, use Conductor's normal
  worktree/checkout guardrails before editing it.

## Ideal authoring contract

`docs/ideal.md` is a concise north star: **what should be true for the user if
technical capability were no obstacle?** "If magic existed" is a useful mental
shortcut, not a request for fanciful prose. Write concrete desired experiences
and outcomes, independent of today's implementation or AI limitations.

- **Zero implementation.** No architecture, stack, providers, models, APIs,
  schemas, file layouts, algorithms, prompts, orchestration, tooling, or build
  steps. Today's constraints, compromises, MVP cuts, and delivery phases belong
  in `docs/spec.md`; operating rules belong in `AGENTS.md` or runbooks; proof
  procedures belong in evals or stories.
- **Short by default.** Aim for one readable page, usually 200–500 words; small
  projects can be shorter. This is an editing target, not a quota. Preserve
  distinct user requirements, merge repetitions, and retain detailed intake in
  its source rather than expanding the Ideal into an exhaustive catalog.
- **Separate ends from means.** Preserve the need behind a proposed mechanism.
  "Use a vector database" becomes "Relevant past knowledge is available when
  needed." A user-valued property such as privacy, fidelity, accessibility, or
  offline availability can belong in the Ideal; the mechanism that achieves it
  cannot. Don't silently promote a suggested technology into a requirement.
- **Execution ideals are outcomes too.** If product and execution ideals are
  both useful, keep them brief. Execution describes the desired experience of
  developing and operating the project, not a checklist of agent workflows,
  approval gates, tests, or repository conventions. Do not add empty categories
  just to mirror the Spec or state graph.

Before presenting the Ideal, read it sentence by sentence: does this describe a
wanted outcome, or prescribe how to achieve it? Would it still be true if an
entirely different implementation delivered the same experience? Move mechanisms
to the appropriate artifact and preserve their provenance. Then remove duplicate
ideas and check that no distinct user outcome disappeared during compression.

## Interview Workflow

1. **Orient**
   - Verify the exact target repo path and whether it has a git checkout.
   - Read the seed file, usually `docs/initial-concept.md`.
   - Check whether `docs/ideal.md`, `docs/spec.md`, `AGENTS.md`,
     `docs/inbox.md`, or stories already exist.
   - If the seed is missing, ask for the seed path or a short idea capture
     before recommending setup.
2. **Extract**
   - Identify durable product ideals, practical constraints, non-goals, open
     questions, first risks, and likely proof points.
   - Separate raw chronology from durable meaning, and desired outcomes from
     proposed mechanisms using the Ideal authoring contract above.
3. **Classify**
   - Pick a primary project shape, with secondary shapes if needed:
     creative/writing, prototype/hardware, web app/product, AI pipeline,
     tooling/library, supervisor/workflow, personal utility, or sparse/no-code.
   - Explain the classification in one or two concrete reasons.
4. **Choose Surfaces**
   - Recommend the minimal useful setup package:
     `docs/ideal.md`, `docs/spec.md`, `docs/inbox.md`, `AGENTS.md`,
     `docs/stories/`, state/graph, setup checklist, eval/golden lane, local
     runtime/ports, UI scout, source-intake, ADRs, scout logs, README, and
     Codex environment setup.
   - Mark each important optional surface as adopt, adapt, defer, or reject.
   - When intake exposes a nontrivial obstacle that makes the first approach
     uncertain, inspect local evidence, name the general problem class, and
     check applicable prior research before proposing a workaround. If none
     applies, use a bounded pass over relevant primary sources and identify a
     small local applicability check. Obvious fixes need no research ceremony.
5. **Discuss**
   - Present the kickoff brief, alternatives, and the first proof story.
   - Ask only the questions needed to resolve material ambiguity.
   - Incorporate the user's corrections before setup.
6. **Set Up After Approval**
   - After explicit approval, author the concise, implementation-free Ideal
     using the contract above; put constraints and implementation choices in
     the Spec or other owning artifacts. Review the split against raw intake
     before handing it to `/setup-methodology`.
   - After explicit approval, create the agreed files; create a first story
     only when the approved setup package includes it.
   - Run `/setup-methodology greenfield` only after real, reviewed
     `docs/ideal.md` and `docs/spec.md` exist and the chosen package warrants
     it.
   - Include a concise, project-specific form of the research rule in the new
     `AGENTS.md`: reuse applicable prior findings; for unfamiliar material
     obstacles, diagnose locally, consult a few relevant primary sources, and
     verify a chosen approach with a small local check. Record reusable
     sources, the decision, result, and uncertainty in existing project notes.
     Stop research once the next experiment is clear; repeated failures call
     for reframing before more special cases. Keep this in lean kickoffs even
     when full methodology setup is deferred.
     Preserve implementation-reuse boundaries and acceptance criteria.

## Kickoff Brief Shape

```markdown
## Kickoff Brief

### Project Read
- {what this project is trying to become}

### Recommended Shape
- Primary type: {type}
- Why: {evidence from the seed}

### Setup Package
- Adopt: {surfaces}
- Adapt: {surfaces}
- Defer: {surfaces}
- Reject: {surfaces}

### First Proof Story
- {the first story that reduces the largest real risk}

### Questions
- {1-3 material questions, if needed}

### Approval Boundary
- Reply `yes` to proceed with: {specific setup action}
```
