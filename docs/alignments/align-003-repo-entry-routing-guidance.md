# Alignment 003 — Repo-Entry Routing Guidance

**Date**: 2026-04-10
**Focus**: Compare repo-entry routing guidance for methodology surfaces and common user-intent phrases
**Source Project**: `cine-forge`
**Target Projects**: `conductor`, `dossier`, `storybook`, `doc-web`

## Surfaces Compared

- `README.md` and `AGENTS.md` in Conductor, Dossier, Storybook, doc-web, and CineForge
- Storybook `docs/decisions/adr-021-execution-ideal-build-constraints/adr.md`
- Corresponding skill presence for `.agents/skills/triage`, `improve-eval`, `align`, and `create-eval`

## Decision Context

- Conductor [ADR-001](../decisions/adr-001-conductor-as-supervisor-not-canonical-core.md)
  applies: this pass should recommend what ports cleanly instead of forcing
  textual identity.
- Storybook ADR-021 already settles the state/graph-first methodology package
  and makes
  `docs/methodology/state.yaml` plus `docs/methodology/graph.json` the planning
  start point.
- No narrower decision record for repo-entry routing guidance was found in
  Dossier, doc-web, or CineForge after searching `docs/decisions/`.

## Key Differences

- CineForge is the only repo whose `README.md` and `AGENTS.md` both give a
  concise phrase-to-surface quick map: `prioritize` to
  `docs/methodology/state.yaml`, `build/fix` to stories, and
  `measure/benchmark/optimize` to `docs/evals/registry.yaml`.
- Storybook already has the same methodology shape in `AGENTS.md` and ADR-021,
  but the repo-entry docs stop at "planning starts from state/graph" instead of
  spelling out the common user-language routes.
- Dossier has the underlying eval/story/triage machinery and strong eval-first
  guidance, but no top-level operational rule that maps user phrasing to the
  authoritative surface.
- doc-web has the methodology surfaces and eval-first tenets in `AGENTS.md`,
  but its `README.md` is intentionally consumer/runtime-facing and its skill
  surface currently lacks `/create-eval`, so CineForge's README quick map and
  exact tool wording do not port verbatim.
- Conductor's supervisor loop is intentionally different: it routes work through
  `inbox.md`, `/triage`, `/align-projects`, and `/scout` rather than through a
  product repo's eval/story loop. A literal `measure ->
  docs/evals/registry.yaml` copy would be wrong here.

## Classification

- **Portable improvement**: AGENTS-level quick routing guidance that translates
  common user requests into the authoritative repo surface is worth porting
  wherever the repo already owns state/story/eval methodology.
- **Intentional adaptation**: README role differs by repo. CineForge's README
  is development-facing enough to hold a methodology quick map; Dossier and
  doc-web READMEs are primarily package/runtime-consumer docs and should not be
  forced into the same shape.
- **Methodology conflict**: Conductor is a supervisor project, not a product
  repo with an eval registry. Its routing vocabulary should stay
  supervisor-specific.
- **Unclear drift**: Storybook and Dossier may simply be missing the concise
  phrase-level quick map in `AGENTS.md`, but the current evidence does not
  prove whether that omission is intentional or just documentation lag.

## Recommendation

- **cine-forge**: Keep local. Treat it as the strongest current reference
  implementation for repo-entry routing guidance.
- **dossier**: Sync partially. Add a short AGENTS-level operational rule
  mapping `prioritize`, `build/fix`, and `measure/benchmark/improve` to
  `docs/methodology/state.yaml`, `docs/stories/`, and
  `docs/evals/registry.yaml`. Keep the README consumer/package focused.
- **storybook**: Sync partially. Add a concise AGENTS quick map that
  complements ADR-021 without duplicating it. README adoption is optional and
  only makes sense if Storybook wants a more developer-oriented entry section.
- **doc-web**: Sync partially in `AGENTS.md` only. Keep the README focused on
  the downstream runtime contract. Phrase eval work as "create or update the
  owning eval / registry entry" rather than assuming a `/create-eval` skill.
- **conductor**: Keep local. If a future pass wants parity, write a
  supervisor-specific variant (`prioritize` -> `/triage`; cross-project drift
  -> `/align-projects`; external source -> `/scout`) instead of copying
  CineForge's product-repo wording.

## Human Decision Needed

- None for the classification pass itself.
- If you want execution next, the clean scope is: port the AGENTS-level
  quick-route block to Dossier, Storybook, and doc-web while leaving README
  placement repo-specific and leaving Conductor on its supervisor-specific
  routing.

## Follow-Up

- No new Conductor story was created. The honest supervisor artifact for this
  line remains the alignment record.
- 2026-04-10 execution follow-up: landed repo-specific AGENTS quick-route
  blocks from dedicated `codex/routing-guidance-sync` task branches onto target
  `main` branches:
  - Dossier: `f010db9`
  - Storybook: `c25fa9f`
  - doc-web: `d0839bd`
- Those landings kept the README placement repo-specific and left Conductor on
  its supervisor-specific routing model, matching the recommendation above.
- 2026-04-16 verification follow-up: checked the dedicated
  `codex/routing-guidance-sync` worktree tip commits against target `main`
  branches and confirmed they are already merged.
- 2026-04-16 cleanup follow-up: removed the dedicated local
  `codex/routing-guidance-sync` worktrees after verification. The local
  worktree cleanup for this line is complete.
- 2026-04-16 branch cleanup follow-up: deleted the merged local
  `codex/routing-guidance-sync` branches after confirming no remaining
  worktree still had them checked out.
- Supervisor memory for this line is current; no further local worktree or
  merged-branch cleanup is pending.
