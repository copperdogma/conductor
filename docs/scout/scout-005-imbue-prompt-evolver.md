# Scout 005 — Evaluate Imbue Prompt Evolver for Prompt Optimization

**Source**: `https://imbue.com/research/2026-02-27-arc-agi-2-evolution/`
**Status**: Defer
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

The source is real and more concrete than a generic "let the model improve its
own prompt" claim. Imbue's 2026-02-27 article and the linked
`darwinian_evolver` repo describe a generic optimization framework around three
explicit parts:

- an initial organism to improve
- an evaluator that returns both a score and concrete failure cases
- one or more mutators that use those failure cases to generate improved
  variants

The repo also adds weighted failure-case sampling, optional batch mutation,
post-mutation verification, and learning-log reuse. That is a credible design
reference for bounded prompt-optimization loops.

But it is not the honest next shared move for the tracked repos. The core
discipline it assumes already exists locally:
- Dossier already records prompt hashes in run metadata and exposes stable
  prompt-hash helpers for extraction, adjudication, and identity-resolution
  prompts.
- Storybook already enforces prompt-first-before-model-escalation and requires
  promptfoo eval coverage for production prompts.
- doc-web already maintains a promptfoo benchmark workspace with explicit
  prompt/scorer/golden structure and prompt-iteration workflow.
- CineForge already enforces prompt-first-before-model-escalation and keeps its
  own promptfoo eval substrate in the sidequest benchmark workspace.

So the source is best treated as a narrow design-reference bundle for future
automation on top of existing eval loops, not as a new cross-project framework
or shared skill import.

## Project Relevance

- **dossier**: `Defer`. Highest real fit. Dossier already has the strongest
  prompt-version tracking and eval-improvement substrate, so if any repo later
  deserves a bounded mutator/evaluator helper on top of existing evals, it is
  Dossier. But there is no measured bottleneck yet proving that manual
  `/improve-eval` loops need an evolutionary wrapper.
- **storybook**: `Defer`. Storybook already has the key local discipline:
  prompt-first iteration plus promptfoo-backed evals for production prompts.
  The future value would only be in a very specific repeated optimization lane,
  not in importing the framework itself.
- **doc-web**: `Defer`. doc-web already has promptfoo tasks, prompt templates,
  golden data, scorers, and a documented prompt-iteration loop. The current
  pressure is still task-specific eval improvement, not generic prompt
  evolution infrastructure.
- **cine-forge**: `Defer`. Similar to Storybook. The repo already has the
  prompt-first rule and benchmark substrate; there is no current signal that a
  reusable evolver layer would outrank normal eval work.

## Recommendation

- Keep this at `Defer`.
- Do **not** create a Conductor story or a target-repo story from this scout
  alone.
- Do **not** add a shared "prompt evolver" skill, methodology package change,
  or cross-project sync line.
- Route one narrow future note to Dossier only, because Dossier is the clearest
  owner if automated prompt mutation ever becomes worth trying.
- If revisited later, borrow only the smallest portable pieces:
  1. evaluator/mutator separation tied to existing eval IDs
  2. explicit failure-case bundles rather than score-only optimization
  3. optional weighted failure sampling or small batch mutation
  4. post-mutation verification before accepting a candidate prompt
  5. learning-log summaries of what change was attempted and what improved
- Do **not** import the full framework, self-improving-agent framing, or a new
  always-on optimization loop unless one repo shows measured repeated prompt
  iteration pain that the current local eval process cannot absorb cheaply.

## Confidence

- Medium-high. The fit judgment is grounded in the primary Imbue article, the
  public `darwinian_evolver` repo, and current local eval/prompt surfaces
  across the tracked repos. I did not run the framework or reproduce the ARC
  experiments.

## Evidence

- `https://imbue.com/research/2026-02-27-arc-agi-2-evolution/`
- `https://github.com/imbue-ai/darwinian_evolver`
- Inbox note: `one skill. that's all you need to add`
- Local overlap evidence:
  - `/Users/cam/Documents/Projects/dossier/src/dossier/engine.py`
  - `/Users/cam/Documents/Projects/dossier/src/dossier/stages/adjudicate.py`
  - `/Users/cam/Documents/Projects/dossier/src/dossier/stages/resolve_judge.py`
  - `/Users/cam/Documents/Projects/dossier/.agents/skills/improve-eval/SKILL.md`
  - `/Users/cam/Documents/Projects/Storybook/storybook/AGENTS.md`
  - `/Users/cam/Documents/Projects/doc-web/AGENTS.md`
  - `/Users/cam/Documents/Projects/doc-web/.agents/skills/improve-eval/SKILL.md`
  - `/Users/cam/Documents/Projects/cine-forge/AGENTS.md`
  - `/Users/cam/Documents/Projects/cine-forge/.agents/skills/improve-eval/SKILL.md`

## Open Questions

- Which repo, if any, will first show a measured prompt-iteration bottleneck
  that is repetitive enough to justify automated mutation on top of its current
  eval loop?
- If Dossier ever tries this, should it stay as a thin helper around the
  existing eval registry and prompt-hash metadata rather than a standalone
  framework import?
