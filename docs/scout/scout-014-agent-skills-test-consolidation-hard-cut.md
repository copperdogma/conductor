# Scout 014 — Evaluate Agent-Skills Additions for Test Consolidation and Hard Cuts

**Source**: `regenrek/agent-skills`
**Status**: Reject
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

The two source skills are coherent and tightly scoped.
`consolidate-test-suites` is a small rule set for test placement: identify the
invariant, choose one owning layer, prefer an existing canonical suite, avoid
duplicate bug guards across multiple layers, and only create standalone
regression tests by exception. `hard-cut` is a cleanup policy for pre-release
refactors: keep one canonical implementation, remove compatibility branches,
fallbacks, adapters, and dual-shape tests unless a real external compatibility
boundary exists.

After comparing those ideas against the tracked repos, neither skill justifies
adoption as a shared external addition.

The `hard-cut` value is already absorbed locally in stronger forms. All four
tracked repos already carry explicit greenfield/no-backwards-compatibility
policy in `AGENTS.md`, and Dossier, Storybook, doc-web, and CineForge all now
ship a repo-local `codebase-improvement-scout` lane that explicitly scans for
compatibility shims, duplicate ownership, dead wrappers, placeholder
pass-throughs, and other drift signatures. That is not just the same idea; it
is a stricter and more project-aware version of the external `hard-cut` skill.

`consolidate-test-suites` is the only partially novel part, but it still does
not rise to the level of a shared skill import. The tracked repos already rely
on stronger repo-native validation contracts than a generic unit/integration/e2e
placement rule:
- Storybook explicitly biases toward integration tests, behavior-based checks,
  and runtime/browser verification.
- doc-web defines done in terms of `driver.py` execution, produced artifacts,
  and manual artifact inspection.
- Dossier and CineForge lean on eval-first, golden-driven, artifact-level proof.

Those contracts matter more than a generic "pick one owning layer" heuristic.
If cross-project test-placement confusion becomes a recurring pain later, the
honest move is to steal one or two lines of guidance into local AGENTS or
runbooks, not to import another parallel skill tree.

## Project Relevance

- **dossier**: Low incremental value. Dossier already has the stronger local
  no-compatibility rule plus a repo-hygiene lane that names hard-cut and
  duplicate-ownership proof targets directly.
- **storybook**: Low incremental value. Storybook already has no-backwards-
  compatibility policy, "architecture drift is real debt" guidance, and a
  stricter validation/runtime proof culture than the external skill provides.
- **doc-web**: Low incremental value. doc-web already carries the hard-cut
  direction locally, and its real validation bar is pipeline/artifact truth,
  not generic test-layer placement.
- **cine-forge**: Low incremental value. CineForge already carries the same
  greenfield and duplicate-ownership drift guidance locally.

## Recommendation

- Reject this as a shared external skill adoption line.
- Do **not** create a Conductor story and do **not** hand this off to any
  target-project inbox.
- Keep one small reusable lesson only:
  - when touching tests, prefer one owning suite for each invariant and run the
    narrowest relevant target first
- If that lesson ever becomes real cross-project pressure, fold it into the
  methodology package or repo-local AGENTS wording directly instead of syncing
  an external skill.

## Confidence

- Medium-high. The source skills are simple enough to evaluate directly, and the
  reject decision is grounded in current local methodology surfaces across all
  tracked repos.

## Evidence

- `https://raw.githubusercontent.com/regenrek/agent-skills/main/skills/consolidate-test-suites/SKILL.md`
- `https://raw.githubusercontent.com/regenrek/agent-skills/main/skills/hard-cut/SKILL.md`
- `https://raw.githubusercontent.com/regenrek/agent-skills/main/README.md`
- Local overlap evidence:
  - `/Users/cam/Documents/Projects/dossier/AGENTS.md`
  - `/Users/cam/Documents/Projects/Storybook/storybook/AGENTS.md`
  - `/Users/cam/Documents/Projects/doc-web/AGENTS.md`
  - `/Users/cam/Documents/Projects/cine-forge/AGENTS.md`
  - `/Users/cam/Documents/Projects/dossier/.agents/skills/codebase-improvement-scout/SKILL.md`
  - `/Users/cam/Documents/Projects/Storybook/storybook/.agents/skills/codebase-improvement-scout/SKILL.md`
  - `/Users/cam/Documents/Projects/doc-web/.agents/skills/codebase-improvement-scout/SKILL.md`
  - `/Users/cam/Documents/Projects/cine-forge/.agents/skills/codebase-improvement-scout/SKILL.md`
  - `/Users/cam/Documents/Projects/conductor/docs/alignments/align-004-shared-skill-sync-hardening.md`

## Open Questions

- Is there a real repeated cross-project failure mode around test-placement
  sprawl, or is the current pressure still mostly repo-local validation depth?
- If Conductor later adds shared test-placement guidance, should it live in one
  of the close-out skills or in the methodology package rather than as a new
  standalone skill?
