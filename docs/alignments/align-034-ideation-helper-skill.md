# Alignment 034 - Ideation Helper Skill

**Date**: 2026-05-19
**Classification**: Portable improvement
**Source**: [Scout 036](../scout/scout-036-open-collider-ideation-quality.md)
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Decision

Add `/ideation` as a standalone helper skill for divergent option generation
before sticky methodology, product, story, or ADR decisions.

The portable idea from Open Collider is the controlled distant-domain pass:
write a local brief, generate structurally distant domains with mechanisms and
bridge questions, produce candidate options, then curate hard. The local skill
adapts that pattern without requiring the Open Collider tool, provider setup,
LLM-judge scoring, or per-run project folders.

`/ideation` is not a decision owner. Caller skills keep authority:

- `init-project` or equivalent intake owns `docs/ideal.md` / `docs/spec.md`
  truth.
- `/create-adr` owns ADR decision text and final choice.
- `/create-story` owns whether a story is warranted and where the boundary
  lands.
- `/build-story` owns the plan, approval gate, implementation judgment, and
  validation handoff.

## Portable Guidance

Use `/ideation` when option quality is the blocker:

- Ideal/spec drafting needs richer possibilities before compromise.
- ADR considered options are thin or same-neighborhood variants.
- Story boundaries are too vague, tiny, or same-shaped to score honestly.
- A build plan has a real solution-space question before implementation.
- Product, workflow, UX, architecture, eval, or methodology brainstorming is
  stuck in familiar patterns.

Skip it for routine triage, ordinary setup, straightforward bug fixes,
validation, closeout, or cases where the blocker is evidence rather than option
quality.

The output should be a compact caller-ready packet:

- baseline options and limits
- distant domains, mechanisms, and bridge questions
- candidate options with risks and proof needs
- kept/rejected disposition
- one or two strongest options plus an open question for the caller

## Artifact Rule

Do not create a durable folder for every ideation run.

Default durable output belongs in the caller artifact:

- Ideal/spec: integrate product truth and important rejected directions.
- ADR: strengthen considered options, consequences, and rejected options.
- Story: record the chosen boundary, alternatives rejected, and proof plan.
- Alignment/scout: summarize the methodology decision when cross-project value
  matters.

Keep an optional report template for high-impact runs where the ideation search
itself is evidence worth preserving. This prevents loss of useful rejected
options without turning ideation into a parallel backlog.

## Subagent Rule

When the user/runtime explicitly authorizes delegation, the caller may run the
divergent option pass in one bounded subagent. The main thread must pass the
brief, local constraints, and caller-owned final decision surface, then receive
only an option packet back. The worker must not edit files, create stories or
ADRs, invoke `/loop-verify`, spawn more agents, or choose the final answer.

If delegation is unavailable or not explicitly authorized, run the same protocol
sequentially.

## Rollout Decision

Conductor should pilot the helper locally first, then roll it to target repos
through setup-methodology or a focused alignment/story when there is a natural
cross-repo update. The first target-repo rollout should copy the shared
`/ideation` skill and add only small caller-skill references where the repo
already has matching `create-adr`, `create-story`, `build-story`,
`setup-methodology`, or `init-project` surfaces.

Do not force `/ideation` into repos that lack active story/ADR/Ideal planning
surfaces, and do not make it a required step in normal workflows.

## Rollout Result

The first shared rollout installed `/ideation` in Conductor and the seven
tracked target repos: Dossier, Storybook, doc-web, CineForge, Boardgame
Ingester, RoboRally, and Echo Forge. Each target repo received the shared
`ideation` skill package, a synced `.gemini/commands/ideation.toml` wrapper,
`setup-methodology` install guidance, and small caller-skill hooks where the
repo already had matching `init-project`, `retrofit-ideal`, `create-adr`,
`create-story`, or `build-story` surfaces.

Validation used repo-native skill sync checks, methodology checks, whitespace
checks, and bounded `/loop-verify` review. The review found and fixed two
contract gaps before landing: the setup checklist had one path that could skip
installing `/ideation`, and the copyable subagent prompt lacked explicit
no-`/loop-verify` and no-spawn guardrails.

## Evidence

- Scout 036 classified Open Collider as `Adapt`: useful for `ideal.md`
  drafting, story brainstorming, and ADR option expansion, but not as a default
  decision authority.
- Open Collider's public docs frame the workflow as brief, domains, collision,
  and curation, with optional feedback-driven domain evolution.
- The research repo reports stronger originality and semantic distance than
  direct prompting, "be original" instructions, or longer same-domain prompts,
  while also making clear that generated ideas are raw LLM outputs and not
  vetted facts.
- Conductor's existing ADR-002 lane split says investigative work can prepare
  creation work, but normative memory still belongs in ideals, specs, ADRs,
  and stories.

## Stop Conditions

- Do not install Open Collider tooling as part of this skill.
- Do not score novelty as if it proves quality.
- Do not let `/ideation` choose the final path.
- Do not preserve every brainstorm as a durable artifact.
- Do not run subagents unless the current request explicitly authorizes
  delegation or parallel agent work.
