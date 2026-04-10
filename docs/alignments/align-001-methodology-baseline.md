# Alignment 001 — Cross-Project Methodology Baseline

**Date**: 2026-04-09
**Focus**: First-pass comparison of shared methodology surfaces and skill inventories
**Source Project**: Baseline across `dossier`, `storybook`, `doc-web`, and `cine-forge`
**Target Projects**: `dossier`, `storybook`, `doc-web`, `cine-forge`

## Surfaces Compared

- Conductor tracked-project roots in `projects.yaml` and `inbox.md`
- `AGENTS.md`
- `docs/ideal.md`
- `docs/spec.md`
- `.agents/skills/setup-methodology/SKILL.md`
- `.agents/skills/triage/SKILL.md`
- Shared `.agents/skills/` inventory

## Key Differences

- Conductor pointed Storybook at `/Users/cam/Documents/Projects/Storybook`, but the active repo root is `/Users/cam/Documents/Projects/Storybook/storybook`. Conductor was updated during this pass so future alignment runs inspect the real project.
- All four tracked projects share a large common supervisor-style skill surface: 32 skill files exist in every repo. None of those shared files are text-identical, which confirms that the real shared artifact is workflow shape rather than exact file text.
- Dossier remains build-map-first and does not have `docs/methodology/state.yaml` or `docs/methodology/graph.json`. Storybook, doc-web, and CineForge all plan from state/graph surfaces and keep `build-map.md` as a supporting or generated view.
- Storybook and CineForge carry webapp, deploy, and project-bootstrap skills that do not belong in Dossier or doc-web. doc-web carries intake- and eval-heavy skills that look mission-specific. Dossier carries library/eval bootstrap extras that are not obviously portable everywhere.
- The intake project uses `doc-web` as the repo slug while its product-facing docs and AGENTS surface the name `Doc-forge`. That split looks tolerable, but Conductor should treat repo slug and product name as separate concepts if naming ambiguity becomes costly.

## Classification

- **Intentional adaptation**: Product ideals/specs diverge strongly by mission, and the product-specific skill extras should stay local. Exact textual sync is not the right target.
- **Portable improvement**: Conductor should track nested repo roots accurately; the Storybook root fix was applied during this pass. The state/graph-centered methodology package used by Storybook, doc-web, and CineForge is also a credible portability candidate if you want one planning model across the portfolio.
- **Methodology conflict**: Dossier's build-map-first operating rule conflicts with the newer state/graph-first operating rule used by the other three projects. This is a real methodology choice, not a cosmetic drift issue.
- **Unclear drift**: The `doc-web` and `Doc-forge` naming split is harmless today, but may confuse future Conductor routing or reporting if it is not made explicit.

## Recommendation

- **dossier**: Ask for a decision. Either migrate toward the state/graph package or explicitly bless build-map-first as an intentional divergence.
- **storybook**: Keep local. Treat it as one reference implementation for the newer state/graph package and keep webapp/deploy skills local.
- **doc-web**: Keep local. Preserve the intake-specific skill surface; revisit naming only if the slug/product split starts confusing routing or reports.
- **cine-forge**: Keep local. Treat it as another reference implementation for the newer state/graph package and keep film/webapp-specific skills local.

## Human Decision Needed

- Resolved on 2026-04-09: pursue the migration path toward the
  state/graph-first package. The remaining design question is how much of
  Dossier's current build-map-first package survives as a generated or
  supporting surface after migration.
- Do you want Conductor to report the intake project as `doc-web`, `Doc-forge`, or both (`doc-web` repo / `Doc-forge` product)?

## Follow-Up

- Conductor Story 001 now tracks the supervisor-side migration preparation:
  `docs/stories/story-001-dossier-state-graph-methodology-migration.md`
- Dossier Story 095 now queues the target-project execution work:
  `/Users/cam/Documents/Projects/dossier/docs/stories/story-095-dossier-state-graph-methodology-migration.md`
