# Scout 052 - Evaluate SkillOpt for Validation-Gated Skill Optimization

**Source**: `https://microsoft.github.io/SkillOpt/`,
`https://arxiv.org/abs/2605.23904`, and
`https://github.com/microsoft/SkillOpt`

**Status**: Adapt
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

SkillOpt is a Microsoft Research system for training natural-language agent
skills as external state for a frozen model. The loop keeps the target model,
backend, and harness fixed, then uses a separate optimizer model to turn scored
rollouts into bounded add/delete/replace edits on one skill document. Candidate
skills are accepted only when they improve a held-out selection split, and the
deployed output is a compact `best_skill.md` rather than optimizer memory or
model-weight changes.

The useful local idea is the discipline, not the package. SkillOpt gives a
strong vocabulary for cases where Cam's repos already have something close to a
train/selection/test loop: collect scored trajectories, reflect over successes
and failures separately, make small patch-style skill edits, preserve rejected
edits as negative feedback, and promote only the validation-gated skill.

That maps well to Conductor's reviewed-learning, skill-surface, and
loop-verify direction, but it should not become automatic self-editing. The
tracked projects already separate learning candidates from live behavior
changes. SkillOpt strengthens that rule: skill changes should be bounded,
evidence-backed, inspectable, and gated by held-out proof before promotion.

The upstream implementation is also research-shaped. It is a Python 3.10+
package with benchmark configs, a training CLI, an eval CLI, and an optional
Gradio WebUI, but the README notes that benchmark datasets are not included.
The GitHub package is marked alpha, has no published release, and assumes
prepared split directories plus provider credentials. That is enough for a
bounded spike when a repo has real scored failures. It is not enough to justify
installing SkillOpt portfolio-wide.

## Project Relevance

- **conductor**: `Adapt`. Conductor should own the adoption gate: use SkillOpt
  as a reference for evidence-backed skill improvement, especially the
  train/selection/test split, bounded textual learning rate, rejected-edit
  buffer, and best-skill export. Do not add automatic skill mutation to ordinary
  scout, learning-candidate, or closeout workflows.
- **dossier**: `First spike completed`. Dossier was the best target fit because
  its extraction surface already had repeatable scored evals and recent
  relationship-recall failures. Story 156 completed as `reject/no-promotion`,
  preserving the SkillOpt-style gate without landing a prompt change.
- **doc-web**: `Spike later`. Good conceptual fit for deterministic pipeline
  tasks with exact checks, schema checks, OCR/crop metrics, or golden HTML
  artifacts. Poor fit for subjective preview-quality judgment unless the
  verifier is made explicit.
- **boardgame-ingester**: `Spike later`. Rulebook/component extraction could be
  a good eventual target once schema goldens and scoring are mature enough.
- **storybook**: `Defer`. Some Journey Scout or Dossier-backed family-data
  flows may eventually produce scored trajectories, but current product truth
  still depends heavily on human/taste judgment and privacy-sensitive data.
- **cine-forge**: `Defer`. Creative and render-quality work is too subjective
  for this loop unless a narrow eval-backed prompt or adapter surface emerges.
- **echo-forge**: `Defer`. Audio/UI quality and live tabletop workflow judgment
  are not a natural first target. Use only for narrow catalog/schema/tool
  procedures with clear checks.
- **roborally**: `Defer`. Current value is low unless a future game-agent or
  rules-interpreter eval harness appears.

## Recommendation

Keep this scout as `Adapt`.

Do not install SkillOpt across tracked repos, copy its optimizer loop into
ordinary skill maintenance, or let agents mutate repo-local skills from local
reflection alone.

Adopt these principles as future gating guidance:

1. A SkillOpt-style run needs a real scored task set with train, selection, and
   locked test data.
2. The target surface should be one compact skill or prompt-like procedure, not
   a heterogeneous library or whole methodology stack.
3. Candidate edits should be small patches with an explicit edit budget.
4. Success and failure traces should be reflected separately so good behavior is
   preserved while recurring failures are corrected.
5. Rejected edits should be retained as negative evidence for the run, not
   hidden or retried blindly.
6. Promotion should require held-out improvement and human-readable inspection
   of the final skill.

Follow-up routing is now recorded in
[Alignment 043](../alignments/align-043-skillopt-first-spike-routing.md).
Dossier is the first concrete owner because it already has a mature extraction
benchmark runner, golden fixtures, extraction prompt modes, recent scored
failure artifacts, and a clean target checkout. The first target story is
Dossier Story 156:
`/Users/cam/Documents/Projects/dossier/docs/stories/story-156-skillopt-style-extraction-prompt-spike.md`.
That story has now completed with no runtime prompt promotion: the best
candidate improved relationship F1 but lowered projection F1 and the combined
quick-smoke score, so the broader guard was not run and the temporary prompt
mode was removed.

doc-web and Board Game Ingester remain later candidates. They should only get
their own story after a specific scored prompt or skill failure class is
selected.

## Rejected Adaptations

- Do not run SkillOpt as a background learner over `.agents/skills`.
- Do not use a train-score improvement as enough proof; the held-out gate is
  the core safety mechanism.
- Do not use the package for subjective UI, prose, audio, or creative taste
  work unless the verifier is explicitly designed and accepted.
- Do not treat one-off closeout lessons as training examples. The current
  reviewed-learning workflow is still the right path for sparse user
  corrections and workflow lessons.
- Do not optimize a whole distributed skill surface as one artifact. SkillOpt's
  design is one compact portable skill, while Conductor's local framework
  intentionally keeps skills distributed and repo-owned.

## Evidence

- The project page describes SkillOpt as text-space optimization for frozen
  agents, where rollout evidence, optimizer-side reflection, bounded skill
  edits, validation gates, rejected-edit feedback, slow update, and meta skill
  produce a reusable exported skill.
- The arXiv paper was submitted on 2026-05-22 and revised on 2026-05-25. It
  reports that SkillOpt was best or tied-best across 52 evaluated model,
  benchmark, and harness cells, with benchmark coverage across QA,
  spreadsheets, documents, math, and embodied decision making.
- The paper reports average GPT-5.5 gains of +23.5 points in direct chat,
  +24.8 inside the Codex agentic loop, and +19.1 inside Claude Code compared
  with no-skill execution.
- The method keeps train, selection, and test splits separate. The selection
  split gates candidate skill updates, and the test split is reserved for final
  reporting.
- The default optimization protocol uses four epochs, rollout batch size 40,
  reflection minibatch size 8, textual learning rate 4 with cosine decay,
  held-out validation gating, slow update, and optimizer-side meta skill.
- The paper's limitations are directly relevant locally: the loop needs scored
  trajectories and reliable feedback, costs extra rollout and optimizer-model
  calls during training, optimizes one portable skill rather than a large skill
  library, and still needs held-out evaluation before transfer.
- The GitHub README shows a Python 3.10+ package with `scripts/train.py`,
  `scripts/eval_only.py`, supported configs for SearchQA, ALFWorld, DocVQA,
  LiveMathematicianBench, SpreadsheetBench, and OfficeQA, and a structured
  output directory ending in `best_skill.md`.
- The repository is MIT licensed, marked alpha in `pyproject.toml`, has no
  published release on GitHub as of this scout, and does not include benchmark
  datasets.

## Confidence

High that SkillOpt is a strong design reference for eval-backed skill
improvement and that direct portfolio-wide adoption would be premature. Medium
on the first practical target because the right repo depends on which current
skill or prompt has scored failures, cheap trajectories, and a meaningful
held-out gate.

## Open Questions

- Which current Dossier, doc-web, or Board Game Ingester skill/prompt has
  enough scored failures to make a small optimization spike worthwhile?
- Should Conductor add a future `/improve-skill` gate that explicitly asks
  whether the target has train/selection/test proof before broad skill edits?
- What is the smallest local output format for a SkillOpt-style run: a
  `best_skill.md`, an accepted learning candidate, or a repo-local eval report
  with a patch proposal?
- When the verifier is model-judged rather than exact, what threshold and audit
  trail would make promotion trustworthy enough?
