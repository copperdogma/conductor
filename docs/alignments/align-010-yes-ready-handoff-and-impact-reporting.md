# Alignment 010 — Yes-Ready Handoff and Impact Reporting

**Date**: 2026-04-11
**Focus**: Align task-completion guidance so agents explain practical impact in
plain language and end with a next step the user can approve with a simple
`yes`
**Source Project**: Baseline across `conductor`, `dossier`, `storybook`, `doc-web`, and `cine-forge`
**Target Projects**: `conductor`, `dossier`, `storybook`, `doc-web`, `cine-forge`

## Surfaces Compared

- `AGENTS.md`
- `.agents/skills/build-story/SKILL.md`
- `.agents/skills/validate/SKILL.md`

## Decision Context

- Conductor [ADR-001](../decisions/adr-001-conductor-as-supervisor-not-canonical-core.md)
  applies: the goal is to align workflow meaning across repos, not to force
  identical report templates everywhere.
- The existing repos already shared the same high-level story loop
  (`/build-story` -> `/validate` -> `/mark-story-done`), but their completion
  handoffs differed in two ways the operator explicitly felt:
  - some repos told the agent to summarize technical changes without enough
    plain-language context about what improved for the user/operator
  - some repos recommended a next step, but not consistently in a
    yes-ready form that made a bare `yes` sufficient approval
- No narrower decision record was found for cross-repo reporting style,
  user-facing impact framing, or yes-ready next-step wording.

## Key Differences

- Impact reporting was already partially present, but uneven:
  - Dossier, doc-web, and CineForge already had impact-first or
    evidence-first wording in `AGENTS.md`
  - Storybook emphasized `Where to verify`, but not the same plain-language
    "what improved for the user" requirement
  - Conductor had no equivalent general reporting rule in `AGENTS.md`
- Yes-ready handoffs also existed unevenly:
  - CineForge already required simple-`yes` approval phrasing broadly
  - Storybook and the repo skills often implied a next step, but did not teach
    a consistent yes-ready wording pattern
  - Dossier and doc-web did not yet state the cross-repo expectation clearly in
    AGENTS or in both story-lifecycle skills
- Skill-level gaps were the real behavioral source:
  - `/build-story` usually recommended `/validate`, but not always with
    explicit plain-language impact framing or yes-ready wording
  - `/validate` usually produced a disposition, but not always a short
    user-facing impact summary or a next step the operator could accept with a
    bare `yes`
- Repo-specific output shape still differs legitimately:
  - Storybook and CineForge keep `Where to verify`
  - doc-web keeps its broader validation-summary format
  - Dossier keeps its Dossier-native validation template and work-log focus
  - Conductor keeps a lighter supervisor report shape than the product repos

## Classification

- **Portable improvement**: all repos should teach two shared handoff rules:
  - explain practical impact in plain language when the work is technical
  - end with a yes-ready next step when there is one honest next move
- **Intentional adaptation**: preserve repo-local report structure, validation
  detail level, and optional `Where to verify` guidance. The portable target is
  handoff behavior, not identical markdown sections.
- **Methodology conflict**: none. This is a consistency and operator-clarity
  improvement, not a competing methodology model.
- **Unclear drift**: prior partial coverage in Dossier, doc-web, and CineForge
  showed the intent was already emerging, but the missing cross-repo contract
  left behavior dependent on which repo/skill the operator invoked.

## Recommendation

- **conductor**: Sync partially. Add general AGENTS-level reporting norms plus
  explicit plain-language impact and yes-ready next-step requirements in
  `/build-story` and `/validate`.
- **dossier**: Sync partially. Keep Dossier's impact-first reporting, but add
  explicit yes-ready handoff guidance in AGENTS plus `/build-story` and
  `/validate`.
- **storybook**: Sync partially. Keep `Where to verify` and the existing
  validation template, but add explicit impact-first and yes-ready handoff
  expectations in AGENTS plus `/build-story` and `/validate`.
- **doc-web**: Sync partially. Keep the custom impact block and numbered-plan
  validation format, but require a yes-ready next-step ending in AGENTS plus
  `/build-story` and `/validate`.
- **cine-forge**: Sync partially. Keep CineForge's existing `Where to verify`
  and yes-ready rhythm, but sharpen the plain-language impact requirement and
  carry it explicitly into `/build-story` and `/validate`.

## Human Decision Needed

- None for the classification pass itself.
- The executed scope was narrow: update AGENTS plus `/build-story` and
  `/validate` only, without reworking repo-local validation schemas or
  introducing new workflow stages.

## Result

- Applied the instruction updates in dedicated target-repo worktrees on branch
  `codex/handoff-reporting-sync`:
  - Dossier: `/Users/cam/.codex/worktrees/handoff-reporting-sync/dossier`
  - Storybook: `/Users/cam/.codex/worktrees/handoff-reporting-sync/storybook`
  - doc-web: `/Users/cam/.codex/worktrees/handoff-reporting-sync/doc-web`
  - CineForge: `/Users/cam/.codex/worktrees/handoff-reporting-sync/cine-forge`
- Updated Conductor locally in the current worktree:
  - `AGENTS.md`
  - `.agents/skills/build-story/SKILL.md`
  - `.agents/skills/validate/SKILL.md`
- Updated each tracked repo's corresponding surfaces:
  - `AGENTS.md`
  - `.agents/skills/build-story/SKILL.md`
  - `.agents/skills/validate/SKILL.md`
- Verified the target worktrees with repo-local checks:
  - Conductor: `make skills-check`, `make methodology-check`
  - Dossier: `./scripts/sync-agent-skills.sh --check`,
    `make methodology-check PYTHON=/Users/cam/Documents/Projects/dossier/.venv/bin/python`
  - Storybook: `./scripts/sync-agent-skills.sh --check`,
    `pnpm methodology:check`
  - doc-web: `./scripts/sync-agent-skills.sh --check`,
    `make methodology-check`
  - CineForge: `./scripts/sync-agent-skills.sh --check`,
    `pnpm methodology:check`
- 2026-04-16 verification follow-up: checked the dedicated worktree tip commits
  against the corresponding target `main` branches and confirmed the landing is
  already complete:
  - Dossier: `dbe98ac` is an ancestor of `main`
  - Storybook: `c53c659` is an ancestor of `main`
  - doc-web: `8519bf3` is an ancestor of `main`
  - CineForge: `5d5a5ed` is an ancestor of `main`
- 2026-04-16 cleanup follow-up: removed the dedicated local
  `codex/handoff-reporting-sync` worktrees after verification. The local
  worktree cleanup for this line is complete.

## Follow-Up

- No new Conductor story was created.
- The rollout is already landed across the target repos.
- 2026-04-16 branch cleanup follow-up: deleted the merged local
  `codex/handoff-reporting-sync` branches after confirming no remaining
  worktree still had them checked out.
- Supervisor memory for this line is current; no further local worktree or
  merged-branch cleanup is pending.
