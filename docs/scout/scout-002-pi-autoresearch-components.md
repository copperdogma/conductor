# Scout 002 — Evaluate PI AutoResearch for Reusable Research Components

**Source**: `https://github.com/davebcn87/pi-autoresearch`
**Status**: Defer
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

The source is real and current, but it is not primarily a reusable research
automation substrate for the tracked repos. `pi-autoresearch` is a Pi-specific
autonomous optimization loop: an extension layer provides `init_experiment`,
`run_experiment`, and `log_experiment`; the companion skills create
`autoresearch.md` plus an append-only `autoresearch.jsonl`; an optional
`autoresearch.checks.sh` gates correctness; and the finalize path splits kept
results into independent merge-base branches.

That means the interesting parts are narrower than the repo name suggests. The
portable ideas are:

1. keep experiment memory in explicit session files that survive context loss
2. separate the benchmark loop substrate from domain-specific optimization
   instructions
3. record a confidence score against benchmark noise instead of trusting single
   wins
4. turn noisy exploratory branches into reviewable branches with deterministic
   grouping rules

The main mismatch is substrate and workflow shape. The package depends on Pi's
extension system, terminal widget/dashboard surface, slash-command model, and
tool-managed auto-commit/revert loop. The tracked repos already own richer
story/eval/golden methodology than this package assumes, and none currently has
enough repeated benchmark-optimization pressure to justify importing another
agent runtime whole.

## Project Relevance

- **dossier**: `Defer`. Highest relevance, but as a design-reference bundle for
  bounded benchmark optimization rather than as a research-automation layer.
  Dossier already has substantial local benchmarking and golden/eval surfaces;
  the potentially reusable pieces are the session-memory pair
  (`autoresearch.md` + `autoresearch.jsonl`), separate checks gating,
  confidence-against-noise scoring, and the branch-finalization logic.
- **storybook**: `Defer`. Storybook's live pressure is promptfoo/persona/runtime
  evaluation, not endless code-optimization loops. The source offers some
  conceptual value around iteration memory, but not enough to justify a local
  handoff now.
- **doc-web**: `Defer`. `doc-web` does have OCR and benchmark seams, but the
  current pressure is model and pipeline evaluation, not a Pi-style autonomous
  code loop with auto-commit/revert behavior.
- **cine-forge**: `Defer`. CineForge already has extensive benchmark and eval
  infrastructure, but much of it is expensive, model-driven, and sidequested.
  The source does not reduce that real cost surface, and its "loop forever"
  posture is a poor fit for multimodal benchmark runs.

## Recommendation

- Keep this at `Defer`.
- Do **not** treat `pi-autoresearch` as a shared research substrate and do
  **not** create a Conductor story from this scout alone.
- Do **not** port the Pi extension/UI/dashboard layer, the slash-command
  surface, or the unconditional "never stop" autonomous loop into the tracked
  repos.
- Hand off one narrow future note to Dossier only. If Dossier later opens a
  bounded runtime/perf/cost optimization story with a stable benchmark script,
  revisit these specific ideas:
  1. explicit session memory files for optimization loops
  2. separate correctness backpressure via an optional checks script
  3. MAD-style confidence scoring so noisy wins do not get over-trusted
  4. merge-base branch finalization for splitting kept experiments into
     reviewable changesets
- Keep Storybook, doc-web, and CineForge local for now. The source does not
  remove enough repeated work there to justify extra methodology.

## Confidence

- Medium-high. The repo structure, README, and finalize path were read directly
  from the primary source and a fresh local clone, and the fit judgment was
  compared against current benchmark/eval surfaces in the tracked repos. I did
  not install Pi or run the extension live.

## Evidence

- `https://github.com/davebcn87/pi-autoresearch`
- `/var/folders/8f/3nlcf3sj1s5bbk1g_3dt3djm0000gn/T/tmp.rf9YgjrmMN/pi-autoresearch/README.md`
- `/var/folders/8f/3nlcf3sj1s5bbk1g_3dt3djm0000gn/T/tmp.rf9YgjrmMN/pi-autoresearch/extensions/pi-autoresearch/index.ts`
- `/var/folders/8f/3nlcf3sj1s5bbk1g_3dt3djm0000gn/T/tmp.rf9YgjrmMN/pi-autoresearch/skills/autoresearch-create/SKILL.md`
- `/var/folders/8f/3nlcf3sj1s5bbk1g_3dt3djm0000gn/T/tmp.rf9YgjrmMN/pi-autoresearch/skills/autoresearch-finalize/SKILL.md`
- `/var/folders/8f/3nlcf3sj1s5bbk1g_3dt3djm0000gn/T/tmp.rf9YgjrmMN/pi-autoresearch/skills/autoresearch-finalize/finalize.sh`
- Dossier local evidence:
  - `/Users/cam/Documents/Projects/dossier/src/dossier/benchmarking.py`
  - `/Users/cam/Documents/Projects/dossier/docs/inbox.md`
- Storybook local evidence:
  - `/Users/cam/Documents/Projects/Storybook/storybook/AGENTS.md`
- doc-web local evidence:
  - `/Users/cam/Documents/Projects/doc-web/docs/stories/story-208-glm-ocr-benchmark-for-handwritten-and-table-heavy-seams.md`
- CineForge local evidence:
  - `/Users/cam/Documents/Projects/cine-forge/AGENTS.md`

## Open Questions

- If Dossier later wants a repo-local optimization lane, is the honest move a
  small skill around existing benchmark scripts rather than a new extension or
  plugin substrate?
- Is there enough repeated benchmark-tuning pressure in any tracked repo to
  justify even the smaller adaptation, or is this best kept as a design
  reference only?
