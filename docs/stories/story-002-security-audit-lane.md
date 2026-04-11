---
title: "Build Portable Security Audit Lane"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I4"
  - "I5"
spec_refs:
  - "spec:2.2"
  - "spec:3.2"
  - "spec:4.2"
  - "spec:5.3"
decision_refs:
  - "ADR-001"
  - "ADR-002"
depends_on: []
category_refs:
  - "scouting"
  - "story-prep"
  - "memory"
tracked_projects:
  - "dossier"
  - "storybook"
  - "doc-web"
  - "cine-forge"
---

# Story 002 — Build Portable Security Audit Lane

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: None

## Goal

Turn the new `/security-audit` idea into a real Conductor-owned investigative
lane and portable skill. Conductor should research practical security-audit
patterns, identify lightweight deterministic tools or wrappers worth bundling,
expand the current skill beyond a checklist, and prove that the resulting lane
can review tracked repos usefully without inventing fake portfolio-wide
security pressure.

## Acceptance Criteria

- [x] Conductor records the chosen security-audit methodology clearly enough
      that the lane is reusable: audit modes, trust-boundary framing, severity
      guidance, follow-up routing, and explicit non-goals.
- [x] The `/security-audit` skill grows beyond its first-pass scaffold to
      include the most useful portable support assets available for the tracked
      repo mix, such as deterministic wrapper scripts, search helpers, or
      documented lint/audit command routing for Python and JavaScript projects.
- [x] The story evaluates candidate security tools and practices honestly,
      including which ones to adopt, adapt, defer, or reject for a lightweight
      AI-led local workflow.
- [x] The upgraded lane is exercised on at least two tracked repos or
      representative repo surfaces, with the results recorded well enough to
      judge signal quality versus noise.
- [x] The story leaves a clear recommendation about future integration: keep as
      optional/manual, add to `/validate` or `/check-in`, route through setup,
      or keep Conductor-local for now.

## Out of Scope

- Pretending every tracked repo now has active security pressure
- Adding mandatory state-graph categories, setup modules, or recurring triage
  work before the lane proves it reduces repeated work
- Building a hosted security-automation platform like the Cursor case study
- Claiming the tracked repos are "secure" after a few bounded audits

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Re-read Scout 003 and any directly relevant repo-local audit or
      architecture-review lanes for reference patterns
- [x] Research practical best practices for lightweight security review in
      AI-driven codebases, prioritizing primary or tool-owner sources
- [x] Inventory portable local tools worth considering for the tracked stacks
      (for example: secret scanning, dependency auditing, static analysis,
      Semgrep/Bandit/pip-audit/npm audit or better equivalents) and decide what
      should be wrapped, documented, or rejected
- [x] Expand `.agents/skills/security-audit/` with the needed workflow,
      references, and any deterministic helper scripts that actually earn their
      keep
- [x] Pilot the lane on at least two tracked repos or repo surfaces and record
      signal, noise, gaps, and follow-up recommendations
- [x] Update related scout or alignment memory if applicable
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: `make test`
- [x] Search docs and update any related surfaces
- [x] Verify Conductor tenets:
  - [x] I1 — Meaning over text
  - [x] I2 — Distributed ownership
  - [x] I3 — Recommendation-first supervision
  - [x] I4 — Honest divergence
  - [x] I5 — Minimal overhead

## Workflow Gates

- [x] Build complete
- [x] Validation complete or explicitly skipped by user
- [x] Story marked done via `/mark-story-done`

## Files to Modify

- `docs/stories/story-002-security-audit-lane.md` — track the supervisor work
  line and record evidence
- `.agents/skills/security-audit/SKILL.md` — grow the skill into a real
  reusable lane
- `.agents/skills/security-audit/references/checklist.md` — refine audit
  lenses, tool routing, and severity guidance
- `.agents/skills/security-audit/references/tooling.md` — record the tool
  support matrix and current adopt/adapt/defer decisions
- `.agents/skills/security-audit/scripts/hotspot-grep.sh` — deterministic
  hotspot search helper
- `.agents/skills/security-audit/scripts/run-local-audit.sh` — local scan
  orchestrator with explicit skip behavior
- `.gemini/commands/*.toml` — regenerated Gemini wrappers after skill-count
  drift caused `skills-check` failure
- `docs/decisions/adr-002-normative-memory-and-investigative-lanes.md` —
  update only if story findings materially sharpen the lane model
- `docs/scout/scout-003-cursor-security-agents.md` — link the Cursor scout to
  the actual follow-up if that context remains relevant
- `docs/methodology/graph.json` — generated story index
- `docs/stories.md` — generated story backlog view

## Notes

- The user explicitly wants this treated as a substantial Conductor work line,
  not a loose idea.
- ADR-002 already establishes the key boundary: security review is an optional
  investigative lane until it proves recurring value.
- Scout 003 is useful as a starting reference for staged review flow and
  evidence-backed findings, but the hosted Cursor substrate is not the target.
- The likely success condition is a portable, local-first skill that can
  operate across Python- and JavaScript-heavy repos without requiring shared
  infrastructure.
- The main design pressure is signal quality. A noisy security lane is worse
  than no lane because it adds review theater rather than reducing operator
  work.
- Current tracked-stack mix:
  - Python-first repos: `dossier`, `doc-web`, `cine-forge`
  - pnpm/Node-heavy repo: `storybook`
- Relevant local reference lanes already exist for structure, not content:
  - Storybook / CineForge `/.agents/skills/triage-architecture/SKILL.md`
  - doc-web `/.agents/skills/triage-architecture/SKILL.md`
- Early candidate tools to evaluate during implementation:
  - code scanning: Semgrep
  - Python dependency review: `pip-audit`
  - Python code review: Bandit
  - JavaScript dependency review: `pnpm audit` / `npm audit`
  - secret scanning: `gitleaks` or `trufflehog`
  - vulnerability database sweep: `osv-scanner`
- Local environment reality matters for wrapper design:
  - available now: `semgrep`, `npm`, `pnpm`, `python3`, `uv`, `rg`
  - missing now: `gitleaks`, `trufflehog`, `pip-audit`, `bandit`,
    `osv-scanner`
- Current intent is Conductor-only implementation plus read-only pilot audits.
  No target-project file edits are planned in this story unless the research
  later proves a specific repo needs its own follow-up artifact.
- Current integration recommendation after implementation and pilots:
  - keep `/security-audit` optional/manual for now
  - keep Gitleaks as an explicit secret-sweep path, not part of the default
    helper bundle
  - do not add this lane to setup-methodology, state-graph pressure, `/validate`,
    or `/check-in` by default until repeated real findings justify the extra
    workflow weight

## Plan

### Concrete File Changes

- `docs/stories/story-002-security-audit-lane.md`
  - record exploration evidence, approved plan, implementation notes, and
    build-state progression
- `.agents/skills/security-audit/SKILL.md`
  - expand the workflow from first-pass scaffold into a fuller lane with
    explicit mode selection, tool-routing rules, pilot guidance, and follow-up
    routing
- `.agents/skills/security-audit/references/checklist.md`
  - refine audit lenses, search starters, severity language, and boundaries
- `.agents/skills/security-audit/references/tooling.md`
  - add a tool-evaluation reference covering what to use, what to avoid, when
    to prefer built-in package-manager commands, and what to do when a tool is
    missing locally
- `.agents/skills/security-audit/scripts/run-local-audit.sh`
  - add one deterministic helper that detects repo shape and available tools,
    then runs the smallest honest local scan bundle or exits with explicit skip
    reasons
- `.agents/skills/security-audit/scripts/hotspot-grep.sh`
  - add a deterministic search helper for high-signal hotspot discovery when
    full scanners are absent or too noisy
- `docs/scout/scout-003-cursor-security-agents.md`
  - link the design-reference scout to this executed follow-up if that still
    reads as the honest memory shape
- `docs/decisions/adr-002-normative-memory-and-investigative-lanes.md`
  - update only if the tool and pilot findings materially sharpen the lane
    boundary or promotion rules
- `docs/methodology/graph.json`
  - regenerate after story changes
- `docs/stories.md`
  - regenerate after story changes

### Expected Outputs

- a materially stronger `/security-audit` skill with:
  - bounded audit modes
  - stack-aware tool routing
  - deterministic helper scripts
  - clearer severity and routing guidance
- a written tool decision surface covering candidate scanners and local-first
  tradeoffs for the tracked repo mix
- at least two read-only pilot audits, likely:
  - `dossier` for Python/package/security-boundary pressure
  - `storybook` for pnpm/Node/dependency and automation pressure
- a concrete recommendation on whether future integration belongs in:
  - optional/manual usage only
  - `/validate`
  - `/check-in`
  - setup-methodology
  - or nowhere yet

### Manual Inspection

- Confirm the skill remains recommendation-first and does not imply a mandatory
  recurring security program.
- Confirm the chosen tools are realistic for solo local workflows and not just
  enterprise defaults.
- Confirm helper scripts fail clearly when tools are absent instead of hiding
  that gap.
- Confirm the pilot audits cover both conventional code/dependency issues and
  AI/tool-permission surfaces where relevant.
- Confirm no target-project files are modified unless a later explicit handoff
  is genuinely warranted.

### Checks

- `make methodology-compile`
- `make methodology-check`
- `make lint`
- `make skills-check`
- `make test` if any Conductor scripts or repo-check surfaces change
- any narrow script syntax checks needed for new helper scripts

## Work Log

20260410-2258 — story creation: created as a new Conductor work line after the
security-lane discussion clarified that the honest next step is a substantial
portable-skill build, not immediate methodology-wide integration. Next step is
`/build-story` to research best practices, choose tool support, and upgrade the
lane with evidence.

20260410-2320 — `/build-story` exploration: confirmed this work belongs in
Conductor under ADR-001 and ADR-002 because the current deliverable is a
portable investigative lane, not a target-repo patch. Re-read Conductor ideal,
spec, state, graph, ADR-001, ADR-002, Scout 003, the current
`/security-audit` scaffold, and repo-local `triage-architecture` skills in
Storybook, doc-web, and CineForge for lane-shape reference. Inspected tracked
repo stack surfaces: Dossier, doc-web, and CineForge are Python-first;
Storybook is pnpm/Node-heavy. Found existing local tool availability:
`semgrep`, `npm`, `pnpm`, `python3`, `uv`, and `rg` are present; `gitleaks`,
`trufflehog`, `pip-audit`, `bandit`, and `osv-scanner` are currently absent.
Files expected to change: this story file, the `security-audit` skill,
new tooling reference(s), likely helper scripts under
`.agents/skills/security-audit/scripts/`, and generated story surfaces.
Tracked projects affected: all four as read-only pilot targets and future skill
consumers; no direct repo edits planned in this story. Risks: noisy or
enterprise-heavy tool choices, wrappers that assume unavailable scanners, and
accidentally converting an optional lane into fake mandatory methodology.
Expected evidence: a stronger skill, explicit tool decisions, two recorded
pilot audits, and a recommendation on later workflow integration. Next step is
human approval on the plan before implementation.

20260410-2348 — implementation: expanded the `security-audit` skill with
bundled helper guidance, explicit local-tool routing rules, and guardrails
against silent downloads. Added `references/tooling.md` to record the current
tool decisions:
- Adopt: `rg` hotspot search, Semgrep, `pnpm audit` / `npm audit`
- Adapt: `pip-audit`, Gitleaks
- Defer: Bandit, OSV-Scanner, TruffleHog
Added deterministic helper scripts:
`.agents/skills/security-audit/scripts/hotspot-grep.sh` and
`.agents/skills/security-audit/scripts/run-local-audit.sh`.
Updated `docs/scout/scout-003-cursor-security-agents.md` so the Cursor scout
points to this narrower local-first carry-through instead of remaining a pure
ambient note.

20260410-2358 — pilot audits: ran the helper on Dossier and Storybook in
read-only mode against representative surfaces.
- Dossier pilot:
  `/Users/cam/.codex/worktrees/7be2/conductor/.agents/skills/security-audit/scripts/run-local-audit.sh /Users/cam/Documents/Projects/dossier --mode repo --target src/dossier --allow-uvx`
  Results: hotspot grep now surfaces mostly real env-var and path/process
  leads with far less noise; Semgrep reported 2 findings (`document_ids.py`
  SHA1 usage and one likely noisy logger-disclosure heuristic in
  `stages/resolve_merge.py`); `uvx pip-audit` reported no known dependency
  vulnerabilities.
- Storybook pilot:
  `/Users/cam/.codex/worktrees/7be2/conductor/.agents/skills/security-audit/scripts/run-local-audit.sh /Users/cam/Documents/Projects/Storybook/storybook --mode repo --target packages/backend/src`
  Results: hotspot grep highlights real secret/env, auth/session, process, and
  network surfaces; Semgrep reported 7 findings, with at least some looking
  like audit leads in eval/test fixtures rather than immediate product bugs;
  `pnpm audit` reported 15 advisories (10 moderate, 5 high), including Hono,
  `@hono/node-server`, `fast-xml-parser`, and `drizzle-orm`.
Interpretation: the lane is producing real signal, but grep and Semgrep still
need human review to separate true issues from expected test or fixture usage.

20260411-0007 — validation and close-out: ran `make methodology-compile`,
`make methodology-check`, `make lint`, `make skills-check`, and `make test`.
The first `skills-check` and `make test` run failed honestly because the
generated Gemini wrappers were stale after adding `create-adr` and
`security-audit` to `.agents/skills/`. Ran `make skills-sync`, which
regenerated `.gemini/commands/*.toml`, then reran `make skills-check` and
`make test` successfully. Build gate is now complete; next step is `/validate`.

20260411-0018 — Gitleaks experiment: extended the lane with an explicit
Gitleaks path in `run-local-audit.sh` using either a local binary or a
Docker-backed fallback behind `--include-gitleaks --allow-docker`. Results:
- Storybook root-level secret sweep added real net-new signal by surfacing
  working-tree `.env` and `.secrets` files alongside known doc/story noise.
- Dossier root-level secret sweep was mostly noise from eval artifacts and
  fixture JSON rather than live credentials.
Decision: keep Gitleaks support, but only as an explicit opt-in secret-scan
path. It is useful enough to keep in the skill, but not honest as a default
step in every repo audit.

20260411-0001 — `/validate`: re-ran `make methodology-compile`,
`make methodology-check`, `make lint`, `make skills-check`, and `make test`
with the current diff and all passed. Confirmed Story 002 acceptance criteria,
tasks, helper scripts, tooling reference, pilot evidence, and generated story
surfaces are present. Validation result: story requirements are met. Remaining
working-tree caveat: the branch also still contains earlier unrelated
Conductor changes around ADR scaffolding (`create-adr`, ADR-002, and
`docs/decisions/README.md`), so close-out should either keep those grouped
intentionally or split them before final push.

20260411-0010 — `/mark-story-done`: closed Story 002 after validation. Fresh
evidence on close-out: the story gates were complete, the implementation
surfaces remained present, and the current remaining work for this story was
only bookkeeping. `make methodology-compile` was rerun to refresh generated
story surfaces. Note: unrelated ADR and ADR-scaffolding changes remain in the
working tree and were intentionally left untouched by this story close-out.
