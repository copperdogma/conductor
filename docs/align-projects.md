# Align Projects Log

Use this index to track internal cross-project alignment work.

## Classification guide

- `Intentional adaptation`
- `Portable improvement`
- `Methodology conflict`
- `Unclear drift`

## Entries

- `2026-04-09` — [Alignment 001 — Cross-Project Methodology Baseline](./alignments/align-001-methodology-baseline.md)
  Focused on shared methodology surfaces, skill inventories, and tracked-project root correctness.
- `2026-04-10` — [Alignment 002 — Inbox Check-In Landing Guardrail](./alignments/align-002-inbox-checkin-landing.md)
  Focused on close-out workflow parity so inbox capture lands with validated work by default.
- `2026-04-10` — [Alignment 003 — Repo-Entry Routing Guidance](./alignments/align-003-repo-entry-routing-guidance.md)
  Focused on AGENTS and README quick-route guidance for `prioritize`, `build/fix`, and `measure/benchmark/optimize` requests.
- `2026-04-10` — [Alignment 004 — Shared Skill Sync Hardening](./alignments/align-004-shared-skill-sync-hardening.md)
  Focused on the remaining shared `.agents/skills` surface and the portable hardening gap in `scripts/sync-agent-skills.sh`.
- `2026-04-10` — [Alignment 005 — Triage Actionability Sync](./alignments/align-005-triage-actionability-sync.md)
  Focused on porting Dossier's compiled triage-actionability model into Storybook, doc-web, and CineForge.
- `2026-04-10` — [Alignment 006 — UI Scout Setup Surface](./alignments/align-006-ui-scout-setup-surface.md)
  Focused on whether Storybook and CineForge's internal `ui-scout` lane should be documented as an optional `setup-methodology` package module.
- `2026-04-10` — [Alignment 007 — Triage Phase Pressure Defaults](./alignments/align-007-triage-phase-pressure-defaults.md)
  Focused on porting doc-web's phase-driven triage follow-up into Dossier, Storybook, and CineForge without flattening their local triage lanes.
- `2026-04-10` — [Alignment 008 — UI Guidance Art Direction Sync](./alignments/align-008-ui-guidance-art-direction-sync.md)
  Focused on selectively carrying Scout 007's front-end prompting and
  composition guidance into Storybook and CineForge without forcing a
  portfolio-wide UI methodology sync.
- `2026-04-11` — [Alignment 009 — Setup Navigation Build-Map Semantics](./alignments/align-009-setup-navigation-build-map-semantics.md)
  Focused on the post-migration meaning of `docs/build-map.md` across the
  tracked repos and whether the setup/navigation surface teaches that role
  clearly enough for operators.
- `2026-04-11` — [Alignment 010 — Yes-Ready Handoff and Impact Reporting](./alignments/align-010-yes-ready-handoff-and-impact-reporting.md)
  Focused on making task handoffs explain practical impact in plain language
  and end with a next step the user can approve with a simple `yes`, while
  preserving repo-local report shapes.
- `2026-04-11` — [Alignment 011 — Loop Verify Skill Rollout](./alignments/align-011-loop-verify-skill-rollout.md)
  Focused on rolling the new shared `loop-verify` coordination skill into all
  tracked projects.
- `2026-04-17` — [Alignment 012 — Triage Story Fragmentation Guardrail](./alignments/align-012-triage-story-fragmentation-guardrail.md)
  Focused on whether doc-web's newer anti-fragmentation triage rule should sync
  into Dossier, Storybook, and CineForge.
- `2026-04-17` — [Alignment 013 — Triage Vs-Ideal Current-Tech Calibration](./alignments/align-013-triage-vs-ideal-current-tech.md)
  Focused on whether Dossier's newer "north-star versus current-tech" triage
  framing should sync into doc-web, Storybook, and CineForge.
- `2026-04-20` — [Alignment 014 — Provider Dependency Health Surface](./alignments/align-014-provider-dependency-health-surface.md)
  Focused on whether CineForge's new split between app liveness and provider
  dependency readiness should carry into Storybook or stay local to the repos
  that already own runtime/package preflight instead.
- `2026-04-24` — [Alignment 015 — Storybook Skill Surface Across Tracked Apps](./alignments/align-015-storybook-skill-surface-all-projects.md)
  Focused on adding Board Game Ingester and Echo Forge to the tracked-project
  registry, then comparing all six tracked apps against Storybook's recent
  greenfield bootstrap, completion-sanity triage, and eval-ladder changes.
- `2026-04-24` — [Alignment 016 — Local Dev Port Contract](./alignments/align-016-local-dev-port-contract.md)
  Focused on assigning stable local server/UI ports to active UI apps and
  giving Codex Run actions relative, worktree-safe launcher commands.
- `2026-04-25` — [Alignment 017 — Triage Orchestration Leaf-Skill Inventory](./alignments/align-017-triage-orchestration-leaf-skill-inventory.md)
  Focused on inventorying current triage leaf skills across tracked repos,
  preserving battle-tested local guidance, and planning the Storybook-first
  orchestration pilot plus adapted rollout.
- `2026-04-28` — [Alignment 018 — Triage Subagent Contract](./alignments/align-018-triage-subagent-contract.md)
  Focused on strengthening unscoped `/triage` so it explicitly authorizes
  contracted subagent lane fan-out when the runtime exposes delegation, while
  preserving the main thread as the Ideal/spec arbiter.
- `2026-04-28` — [Alignment 019 — Core Story Loop Subagent Contracts](./alignments/align-019-core-story-loop-subagent-contracts.md)
  Focused on applying the Story 005 subagent lessons to `/create-story`,
  `/build-story`, `/validate`, and shared `/setup-methodology` across tracked
  repos, with loop verification and repo-local adaptation.
- `2026-04-29` — [Alignment 020 — Visual Inspect Loop Skill Rollout](./alignments/align-020-visual-inspect-loop-skill-rollout.md)
  Focused on selectively rolling doc-web's `/visual-inspect-loop` skill into
  tracked repos that own visual, rendered, image, screenshot, crop, UI, or
  image-golden quality surfaces.
- `2026-04-29` — [Alignment 021 — Triage Story Sizing Calibration](./alignments/align-021-triage-story-sizing-calibration.md)
  Focused on carrying Robo Rally's anti-micro-story triage lesson into tracked
  triage skills as an "about an hour of AI work" sizing heuristic, while
  preserving exceptions for genuinely tiny indivisible stories.
- `2026-04-29` — [Alignment 022 — Review vs Validate](./alignments/align-022-review-vs-validate.md)
  Focused on comparing Codex's findings-first review stance with tracked
  `/validate` skills and recommending a findings-first review pass inside
  `/validate`, not replacing `/validate`.
- `2026-04-29` — [Alignment 023 — Legacy Skill Retirement](./alignments/align-023-legacy-skill-retirement.md)
  Focused on inventorying custom repo skills before removing the obsolete
  `/advice-for-past-self` context-reset helper and identifying other stale
  custom skills now superseded by context compression and current methodology
  surfaces.
- `2026-05-05` — [Alignment 024 — Reviewed Learning Rollout](./alignments/align-024-reviewed-learning-rollout.md)
  Focused on rolling Story 008's reviewed learning-candidate workflow into the
  tracked repos with isolated worktrees, local adaptation, and loop
  verification.
- `2026-05-11` — [Alignment 025 — Loop Verify Upstream and Model-Sizing Guardrails](./alignments/align-025-loop-verify-upstream-model-guardrails.md)
  Focused on routing the expensive Storybook `/loop-verify` failure mode into
  an upstream-boundary rule and risk-sized worker model guidance, then
  recording the Story 009 target-project rollout evidence.
- `2026-05-11` — [Alignment 026 — PromptFoo and Deletion-Eval Setup Guidance](./alignments/align-026-promptfoo-deletion-eval-setup-guidance.md)
  Focused on shrinking the aspirational-eval and PromptFoo inbox pressure into
  a small setup-methodology clarification instead of a redundant cross-repo
  audit.
- `2026-05-11` — [Alignment 027 — Browser Tool Workflow Selection](./alignments/align-027-browser-tool-workflow-selection.md)
  Focused on routing the Chrome/browser-tool inbox pressure into a practical
  task-shape matrix for Browser, Chrome, Computer Use, and repo-local
  Playwright/runbook validation.
- `2026-05-12` — [Alignment 028 — Fresh Docs Dependency and Prompt Contract Cleanup](./alignments/align-028-fresh-docs-dependency-and-prompt-contract-cleanup.md)
  Focused on making current upstream docs an active dependency for
  drift-prone provider/component work while preserving repo-local
  Ideal/spec/eval truth as the adoption gate.
- `2026-05-12` — [Alignment 029 — Loop Verify Runaway Controls](./alignments/align-029-loop-verify-runaway-controls.md)
  Focused on hardening `/loop-verify` after Echo Forge exposed recursive worker,
  uncapped-doc-loop, and docs/ADR scope-expansion failure modes.
- `2026-05-15` — [Alignment 030 — Validate Codex Review Closeout Signal](./alignments/align-030-validate-codex-review-closeout-signal.md)
  Focused on adapting Codex CLI review as an extra `/validate` signal for
  non-trivial code diffs while keeping `/loop-verify` task-shaped and useful
  beyond story closure.
- `2026-05-16` — [Alignment 031 — Algorithmic Complexity Detector Guidance for Codebase Improvement](./alignments/align-031-algorithmic-complexity-detector-codebase-improvement.md)
  Focused on adapting Scout 033's complexity-hotspot idea into the existing
  `/codebase-improvement-scout` lane as optional detector guidance, without
  installing a new global Codex skill or treating scanner output as proof.
- `2026-05-15` — [Alignment 032 — Portfolio Local Runtime Allocation](./alignments/align-032-portfolio-local-runtime-allocation.md)
  Focused on turning Echo Forge's local service launcher pilot into a
  Conductor-owned port allocation contract plus repo-local launcher guidance for
  multi-agent, multi-worktree development.
- `2026-05-16` — [Alignment 033 — Loop Verify Discovery and Candidate-Close Phases](./alignments/align-033-loop-verify-discovery-candidate-close.md)
  Focused on making strict `/loop-verify` phase-based so cross-cutting defect
  classes are discovered and fixed systemically before expensive candidate-close
  validation, proof generation, or closeout ceremony runs.
- `2026-05-19` — [Alignment 034 — Ideation Helper Skill](./alignments/align-034-ideation-helper-skill.md)
  Focused on adapting Scout 036's Open Collider lesson into a standalone
  optional `/ideation` helper that improves option generation for Ideal/spec,
  story, build-plan, and ADR work while leaving final decisions with the caller.
- `2026-05-19` — [Alignment 035 — Provider-Specific Skill Wrapper Retirement](./alignments/align-035-provider-specific-skill-wrapper-retirement.md)
  Focused on making `.agents/skills/<name>/SKILL.md` the canonical skill
  package across tracked repos now that Google Antigravity and Gemini CLI
  support it directly, with provider-specific command aliases kept optional.
- `2026-05-20` — [Alignment 036 — Codex Worktree Environment Bootstrap](./alignments/align-036-codex-worktree-environment-bootstrap.md)
  Focused on explaining why fresh Codex worktrees still hit missing dependency
  binaries, then recommending explicit repo-owned setup hooks in
  `.codex/environments/environment.toml` instead of per-agent install guesses.
