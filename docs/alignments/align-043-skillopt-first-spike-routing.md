# Alignment 043 - SkillOpt First Spike Routing

**Date**: 2026-05-27
**Classification**: Portable eval discipline with repo-local spike
**Source**: [Scout 052](../scout/scout-052-skillopt-validation-gated-skill-optimization.md)
**Target Story**:
`/Users/cam/Documents/Projects/dossier/docs/stories/story-156-skillopt-style-extraction-prompt-spike.md`
**Projects Reviewed**: conductor, dossier, doc-web, boardgame-ingester

## Focus

Turn Scout 052's SkillOpt lesson into the first concrete target-repo work item
without importing SkillOpt or authorizing automatic skill mutation.

The routing question is not "which repo could eventually use SkillOpt?" The
right first target needs:

- scored evals that already exist
- enough fixture diversity to define a selection gate and a broader guard
- a compact prompt/skill-like target surface
- low risk if the spike rejects every candidate
- a clean checkout where a story handoff will not collide with active product
  work

## Target Comparison

| Project | Current evidence | Routing decision |
| --- | --- | --- |
| Dossier | Mature `scripts/benchmark_models.py` runner, golden fixtures, `quick-smoke`, `t1-cross-domain`, extraction prompt modes, eval registry attempts, rescore support, and recent long-prose semantic failures from Stories 154-155. | First spike owner. Create a Dossier story for a SkillOpt-style extraction prompt improvement spike. |
| doc-web | Strong promptfoo/image/OCR/crop eval culture and maintained quality gates, but current open pressure is intake honesty and blocked handwritten OCR; a prompt/skill optimization target is less clear. | Keep as later candidate after a specific prompt or guided-runtime failure class is selected. |
| Board Game Ingester | Strong eval-led greenfield package with top-level and child scorers, but current primary checkout is on an active story branch and the natural next work is package-readiness/production proof, not prompt optimization. | Keep as later candidate after active branch state is settled and a model/prompt-owned failure class is isolated. |
| Conductor | Owns the gating discipline and routing memory. | Record the decision; do not build a generic optimizer service. |

## Decision

Create Dossier Story 156 as the first concrete SkillOpt-style spike.

The story is intentionally a bounded spike, not a runtime promotion:

- It uses existing Dossier benchmark and golden infrastructure.
- It treats SkillOpt as a method reference: split, reflect, patch, reject, gate.
- It does not add the upstream SkillOpt dependency.
- It does not let an agent mutate `.agents/skills` or `extract_prompt.py`
  outside the story's explicit gate.
- It requires a held-out selection improvement before any broader test run or
  live prompt promotion.

## Outcome

Dossier Story 156 completed as a `reject/no-promotion` spike.

The spike validated the routing discipline rather than a prompt change:

- Baseline quick-smoke rescore: entity F1 `0.8874`, relationship F1 `0.6149`,
  projection F1 `0.6164`, combined score `0.9324`.
- Candidate 001 regressed relationship and combined score and had split-hygiene
  risk.
- Candidate 002 improved relationship F1 to `0.6364`, but projection F1 fell to
  `0.5471` and combined score fell to `0.9276`.
- Both temporary benchmark-only prompt modes were removed; no runtime default
  changed.

This is the desired failure mode for the first adoption pass: the SkillOpt-style
gate prevented a plausible prompt nudge from landing without preserved held-out
quality.

## Dossier Spike Shape

The Dossier story should start from the extraction prompt surface because it is
compact enough to patch and already benchmarked:

- target surface: `src/dossier/stages/extract_prompt.py`
- runner: `scripts/benchmark_models.py --stage extract`
- likely selection gate: `quick-smoke`
- likely broader guard: `t1-cross-domain`
- optional semantic side check: Story 154/155 Cthulhu long-prose scorer
- artifact shape: baseline report, rejected-candidate ledger, candidate patch
  proposal, final `best_skill.md`-style summary or explicit no-promotion
  report

The story should choose and lock the exact train/selection/test split before
any prompt edit. If Dossier cannot form a sufficiently disjoint split from
current fixtures without overpaying for model calls, the story should record
that limitation and use the smallest honest Dossier-native gates rather than
pretending to reproduce SkillOpt's research protocol exactly.

## Non-Targets

- No portfolio-wide installation.
- No always-on learner.
- No skill mutation from closeout reflection alone.
- No Storybook, CineForge, Echo Forge, or creative/UI/audio target until a
  scored subproblem exists.
- No Dossier runtime-default change unless the spike clears its held-out gates
  and Dossier's normal validation path.

## Practical Impact

This turns SkillOpt from an interesting scout into a concrete, reviewable
Dossier spike. The useful decision is preserved even if the spike rejects every
candidate: future prompt or skill optimization work must prove itself against
locked eval gates instead of relying on train-score improvement or plausible
reflection.
