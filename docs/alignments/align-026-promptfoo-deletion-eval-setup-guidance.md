# Alignment 026 — PromptFoo and Deletion-Eval Setup Guidance

**Date**: 2026-05-11
**Focus**: Shrink the aspirational-eval and PromptFoo inbox pressure into the
smallest useful supervisor change after checking the existing methodology
surface.

## Source

Primary Conductor Story 010, reduced after an evidence pass and Cam's scope
correction:

- The tracked repos already have a strong sense of Ideal/spec compromises.
- Compromises are already guarded by evals and methodology state/graph
  actionability.
- The useful question is not "do a broad aspirational-eval audit?", but "what
  tiny setup guidance is still missing?"

## Existing Enforcement

Current product-repo methodology already covers most of the original story
pressure:

- Alignment 015 already rolled the eval-ladder guidance across the tracked
  product repos. The portable rule is root Ideal eval or explicit deferral,
  parent failure, measured failure mode, and child eval/story only when the
  next ladder node is clear.
- `/setup-methodology` already treats eval/golden setup as baseline product
  infrastructure and requires root Ideal eval/golden coverage or explicit
  deferral.
- `/create-story` surfaces in product repos already ask AI-capability stories to
  identify the eval ladder, check the single-call simplification baseline, and
  note eval coverage when AI-powered capabilities change.
- `/triage-evals` already reads registry/state/graph evidence, distinguishes
  quality evals from compromise gates, and uses `climb`, `hold`, and
  `converge` semantics before recommending reruns or deletion work.
- Eval registries and methodology compilers already preserve explicit lineage
  between evals, stories, spec refs, categories, and compromise refs.

That means "aspirational eval" should not become a new portfolio-wide lane.
The existing terms are better: compromise eval, deletion gate, root/parent/child
eval ladder, simplification baseline, and explicit deferral trigger.

## Classification

Portable clarification with exact shared-skill propagation, not a broad audit.

The original story shape was too heavy. A per-repo gap matrix would mostly
repeat Alignment 015 and the target repos' existing eval-ladder surfaces. The
honest improvement is a small setup-methodology wording clarification that
helps future setup runs choose the right eval substrate and avoid inventing
one-off eval harnesses.

## Decision

Keep the current eval-ladder model. Do not add a new "aspirational eval" lane or
new required audit surface.

When setup or story work identifies a new AI compromise, it should either:

- attach or create the owning compromise/deletion eval, or
- explicitly defer that eval with the trigger that would make it worth creating
  later.

PromptFoo should be the default only when its proof shape fits:

- prompt/model comparison
- rubric or judge scoring
- repeated output-quality checks over a stable case set

Custom runners, scripts, browser checks, artifact inspection, golden verifiers,
or runtime benchmarks should stay preferred when they prove the actual behavior
more honestly:

- structural behavior
- deterministic pipeline truth
- browser or UI behavior
- visual, audio, video, or document artifacts
- latency, cost, provider, or runtime instrumentation that PromptFoo cannot
  represent cleanly

## Shared Setup Change

The shared `.agents/skills/setup-methodology/SKILL.md` surface now records the
two clarified rules:

- new AI compromises need an owning compromise/deletion eval or explicit
  deferral trigger
- PromptFoo is the default for prompt/model/rubric proof, while custom runners
  remain the default for structural/runtime/browser/artifact truth

This is an exact shared-skill update, not a target-project product change.

## Recommendation

Do not create target-repo follow-up stories now. The needed target action is
only the shared setup-methodology wording update.

If a future shared setup-methodology refresh is already happening for another
reason, treat this wording as part of the shared package and keep it
byte-identical unless a local repo explicitly decides to fork the setup
contract.

## Rollout Execution

After Cam pointed out that the shared setup-methodology file should not stop at
Conductor, the wording was propagated to isolated target-repo worktrees.

Shared rollout settings:

- Worktree root:
  `/Users/cam/.codex/worktrees/story010-promptfoo-deletion-eval/`
- Branch: `codex/story-010-promptfoo-deletion-eval-setup`
- Core edit: `.agents/skills/setup-methodology/SKILL.md`

Per-repo evidence:

| Project | Base | Commit | Files changed | Checks |
| --- | --- | --- | --- | --- |
| Dossier | `a473105` | `820af37` | `.agents/skills/setup-methodology/SKILL.md` | `PYTHON=/Users/cam/Documents/Projects/dossier/.venv/bin/python make methodology-check skills-check`; `git diff --check`. |
| Storybook | `fc25eed` | `83f653c` | `.agents/skills/setup-methodology/SKILL.md`; generated `docs/methodology/graph.json`; generated `docs/stories.md` | `bash scripts/sync-agent-skills.sh --check`; `pnpm methodology:compile`; `npm run methodology:check --silent`; `git diff --check`. Generated changes only update UI-scout freshness from current to due. |
| doc-web | `71e1eca` | `4f62f8a` | `.agents/skills/setup-methodology/SKILL.md` | `make methodology-check skills-check`; `git diff --check`. |
| CineForge | `2ffda18` | `dbd688e` | `.agents/skills/setup-methodology/SKILL.md`; generated `docs/build-map.md`; generated `docs/methodology/graph.json`; generated `docs/stories.md` | `make skills-check`; `pnpm methodology:compile`; `npm run methodology:check --silent`; `git diff --check`. Generated changes only refresh the date-sensitive UI-scout freshness/build-map state. |
| Board Game Ingester | `b51e3cf` | `862718d` | `.agents/skills/setup-methodology/SKILL.md` | `make methodology-check skills-check`; `git diff --check`. |
| RoboRally | `4137536` | `3856eae` | `.agents/skills/setup-methodology/SKILL.md` | `npm run methodology:check --silent`; `npm run skills:check --silent`; `git diff --check`. |
| Echo Forge | `9dcc8ba` | `4c9abaa` | `.agents/skills/setup-methodology/SKILL.md` | `npm run methodology:check --silent`; `npm run skills:check --silent`; `git diff --check`. |

## Stop Conditions

- Do not run a broad paid eval/model sweep for this line.
- Do not audit every tracked repo for missing aspirational evals unless fresh
  evidence suggests actual drift.
- Do not force PromptFoo into lanes where deterministic scripts, browser proof,
  artifact inspection, or runtime benchmarks are better evidence.
- Do not claim target product behavior changed; this update changes only shared
  setup guidance.

## Practical Impact

This keeps the methodology small. Agents get clearer setup guidance for the one
place the old wording was vague, while Cam avoids a redundant portfolio audit
over behavior the repos already enforce.
