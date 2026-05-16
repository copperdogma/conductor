# Changelog

## [2026-05-16-01] - Add complexity detector scout guidance

### Added
- Added Scout 033, Alignment 031, and Story 014 for adapting
  `codex-complexity-optimizer` as optional algorithmic-complexity detector
  guidance inside `/codebase-improvement-scout`, without installing the npm
  package globally or treating scanner output as proof.
- Added Scout 034 for a bounded report-only Clawpatch spike, with a RoboRally
  pilot note in `inbox.md`.

### Changed
- Updated `/setup-methodology` so codebase-improvement lane setup keeps
  algorithmic complexity scanning report-first, local-proof-based, and optional.
- Rolled the detector guidance into Dossier, Storybook, doc-web, CineForge,
  Board Game Ingester, RoboRally, and Echo Forge from isolated worktrees, then
  landed each target repo on `main`.

## [2026-05-15-01] - Add Codex review validation signal

### Added
- Added Scout 031 documenting the declined OpenClaw `fs-safe` opportunity for
  the current tracked repos.
- Added Scout 032, Alignment 030, and Story 013 for adopting Codex CLI review
  as an optional `/validate` signal for non-trivial code diffs.

### Changed
- Updated `/validate` so `codex review` can provide an advisory extra review
  signal while `/validate` remains the closure authority.
- Updated `/loop-verify` with a task-agnostic accepted/rejected/follow-up
  finding ledger and clean-stop guidance, without narrowing it to story closure.
- Rolled the validate and loop-verify guidance into Dossier, Storybook,
  doc-web, CineForge, Board Game Ingester, Robo Rally, and Echo Forge from
  isolated worktrees, then landed each target repo on `main`.

## [2026-05-13-01] - Tighten check-in inbox handling

### Changed
- Updated `/check-in` so completed inbox items are removed or marked handled
  before closeout, and modified inbox files are always included in the landing
  set unless Cam explicitly excludes them.
- Added explicit isolated-worktree guidance to inspect and fold in inbox-only
  edits from the primary checkout before validation.

## [2026-05-12-03] - Harden loop-verify runaway controls

### Added
- Added Alignment 029 and Story 012 for the Echo Forge runaway-loop report and
  the portable `/loop-verify` fix.

### Changed
- Updated `/loop-verify` with budgeted, docs/ADR alignment, and
  strict-until-clean modes so workers do not recursively invoke the skill,
  spawn subagents, or widen shard scope.
- Rolled the loop-control guidance into Dossier, Storybook, doc-web, CineForge,
  Board Game Ingester, Robo Rally, and Echo Forge from isolated worktrees.

## [2026-05-12-02] - Add fresh-doc dependency guidance

### Added
- Added Scout 030, Alignment 028, and Story 011 for making current upstream
  docs an active dependency when work touches drift-prone providers,
  components, SDKs, model/provider slugs, tooling plugins, framework APIs, or
  auth/payment/storage surfaces.

### Changed
- Updated `/scout`, `/triage`, `/build-story`, `/validate`, and
  `/setup-methodology` so fresh upstream docs establish current external facts
  while repo-local Ideal/spec/compromise/evals remain the acceptance contract.
- Added outcome-first prompt-contract guidance to `/setup-methodology`, while
  preserving failure-proven local guardrails and avoiding blanket prompt
  rewrites or unscoped target-repo churn.

## [2026-05-12-01] - Clarify setup eval substrate guidance

### Added
- Added Alignment 026 and Story 010 for the PromptFoo/deletion-eval setup
  clarification.

### Changed
- Clarified the shared `/setup-methodology` guidance so new AI compromises get
  an owning compromise/deletion eval or explicit deferral trigger.
- Clarified that PromptFoo is the default for prompt/model/rubric proof, while
  custom runners remain preferred for structural, runtime, browser, and
  artifact truth.
- Rolled the exact setup-methodology wording into Dossier, Storybook, doc-web,
  CineForge, Board Game Ingester, Robo Rally, and Echo Forge from isolated
  worktrees.

## [2026-05-11-01] - Roll out loop-verify upstream guardrails

### Added
- Added Alignment 025 and Story 009 for upstream-owned blocker handling and
  risk-sized worker model guidance in broad verification loops.

### Changed
- Updated Conductor's `/loop-verify` seed guidance and rolled the same
  behavior into Dossier, Storybook, doc-web, CineForge, Board Game Ingester,
  Robo Rally, and Echo Forge from isolated worktrees.
- Removed blanket strongest-model defaults from target `golden-verify` skills
  while preserving high-capability defaults for semantic golden review.

## [2026-05-05-01] - Add reviewed learning workflow

### Added
- Added Story 008, Scout 029, and Alignment 024 for the reviewed
  learning-candidate workflow inspired by holaOS without adopting its heavier
  runtime.
- Added `/learning-review` and `/learning-candidate` plus lightweight
  `docs/learning-candidates/` templates and examples.

### Changed
- Hooked reviewed-learning checks into selected Conductor closeout skills and
  rolled the workflow into Dossier, Storybook, doc-web, CineForge, Board Game
  Ingester, Robo Rally, and Echo Forge from isolated worktrees.
- Landed the target repo rollout commits onto each target `main` branch after
  repo-local validation and a clean fourth `/loop-verify` round.

## [2026-04-29-01] - Roll out visual inspect loop skill

### Added
- Added Alignment 020 and Story 007 for the selective
  `/visual-inspect-loop` rollout from doc-web into the visual-surface tracked
  repos.
- Prepared isolated target-repo worktree landings for Storybook, CineForge,
  Board Game Ingester, Robo Rally, and Echo Forge.

### Changed
- Updated Storybook and Echo Forge `/ui-scout` guidance so UI Scout invokes
  `/visual-inspect-loop` when a finding or inline fix depends on
  visual/rendered correctness.
- Recorded Dossier as deferred for this skill until it owns a concrete visual
  or rendered-artifact lane.

## [2026-04-28-01] - Upgrade core story loop contracts

### Added
- Added Scout 025 for the OpenAI Symphony orchestration reference and
  Alignment 019 for the cross-repo core story-loop subagent contract rollout.
- Added Story 006 to record the review, loop-verification evidence, validation,
  target repo commits, and close-out path.

### Changed
- Upgraded Conductor's `/create-story`, `/build-story`, and `/validate`
  guidance with optional bounded sidecar/parallel validation contracts while
  keeping the main thread responsible for final judgment.
- Replaced the shared `/setup-methodology` skill with the identity-preserving
  version that refreshes the accepted core-loop guidance across tracked repos.
- Routed the completed Symphony and story-loop notes out of `inbox.md`.

## [2026-04-24-01] - Record local dev port contract

### Added
- Added Robo Rally to the tracked project registry.
- Added Alignment 016 and Story 004 to record stable local server/UI port
  assignments and Codex Run action commands for the active UI apps.

### Changed
- Closed Story 004 after validating the Conductor registry/alignment surfaces
  and landing the target launcher commits for CineForge and Echo Forge.

## [2026-04-11-01] - Roll out loop-verify skill

### Added
- Added the shared `/loop-verify` coordination skill to Conductor and recorded
  Alignment 011 for the portfolio-wide rollout decision and execution details.

### Changed
- Updated `docs/align-projects.md` and Alignment 009 to record the validated
  Dossier, Storybook, doc-web, and CineForge `main`-branch landings for the
  shared skill rollout.

## [2026-04-10-08] - Land triage actionability sync

### Added
- Alignment 005 documenting the triage-actionability sync from Dossier into
  Storybook, doc-web, and CineForge, including the follow-up audit findings and
  the added regression coverage used before landing.

### Changed
- Marked the consumed inbox note complete and updated supervisor memory to
  record the validated Storybook, doc-web, and CineForge `main`-branch landings
  for the triage-actionability sync.

## [2026-04-10-07] - Route inbox backlog into scout memory

### Added
- Scout 014 through Scout 022 to convert the remaining routed inbox backlog
  into explicit scout memory, including tighter bundled investigations for
  agent skills, OpenClaw operator surfaces, long-running agent platform notes,
  media automation, OCR, realtime platform notes, and two explicit `Defer` /
  `Reject` dispositions.

### Changed
- Cleared `inbox.md` down to the one still-blocked `202602 Project Notes.md`
  recovery item instead of keeping routed notes as raw capture.
- Expanded the relevant existing scout entries with related inbox evidence so
  the memory line for security review prompts, prompt evolution, front-end
  guidance, browser tooling, and memory approaches stays coherent.

## [2026-04-10-06] - Align shared skill sync hardening

### Added
- Alignment 004 documenting which parts of the remaining shared
  `.agents/skills` surface should stay local and which `sync-agent-skills`
  hardening should port across tracked projects.

### Changed
- Replaced the consumed inbox alignment candidate with the concrete
  post-alignment follow-up to port Storybook's stricter wrapper-drift checks to
  Dossier, doc-web, and CineForge.
- Landed that follow-up onto Dossier, doc-web, and CineForge `main` branches
  from dedicated `codex/skill-sync-hardening` worktrees without forcing bulk
  text sync across the shared skill files.

## [2026-04-10-05] - Align repo-entry routing guidance

### Added
- Alignment 003 documenting how repo-entry routing guidance should port across
  Conductor, Dossier, Storybook, doc-web, and CineForge.

### Changed
- Routed the earlier CineForge quick-route note out of `inbox.md` into the new
  alignment record while preserving newer inbox capture added during the same
  supervisor window.
- Landed the linked Dossier, Storybook, and doc-web AGENTS quick-route
  follow-ups onto their respective `main` branches as part of the same
  supervisor line.

## [2026-04-10-03] - Scout Codex App Server

### Changed
- Completed Scout 008 using the new X connector plus official OpenAI App
  Server docs, then closed it as `Reject` after confirming the current
  projects do not need an embedded Codex workspace surface
- Updated scout memory and scouting state to reflect the first detailed source
  evaluation in the current scout backlog

## [2026-04-10-04] - Scout Codex plugins

### Changed
- Completed Scout 012 using the X connector plus official OpenAI help and
  release notes, and marked it `Defer` after confirming plugins are a Codex
  workflow-distribution mechanism rather than a tracked-project plugin or
  mobile product surface
- Added scout-handoff guidance so repo-specific future ideas now move to the
  owning repo's `docs/inbox.md` by default instead of lingering only in
  Conductor
- Refined Scout 012 so Storybook keeps the relevant future native-workflow
  angle without treating plugins as a present product feature
- Recorded the Scout 012 handoff into Storybook's `docs/inbox.md`

## [2026-04-10-02] - Triage inbox into scout memory

### Added
- Scout 001 through Scout 013 so each captured source now has its own scout
  mission instead of one combined backlog artifact

### Changed
- Trimmed `inbox.md` so only the remaining alignment candidate and the blocked
  `202602 Project Notes.md` dependency stay live there
- Updated the scout index and methodology state to reflect that Conductor now
  has individual queued scout missions instead of an empty scout lane
- Clarified `/triage inbox` so future scout routing defaults to one source per
  scout mission unless a small grouped investigation is clearly the more honest
  shape
- Documented Conductor's preferred content connectors so future scouting and
  routing work uses `Twitter Scraper`, `YouTube Transcripts`, and `Project
  Agent` before generic browsing when applicable

## [2026-04-10-01] - Close Story 001 and land inbox capture guardrails

### Added
- Alignment 002 documenting the inbox-capture close-out guardrail and its
  landing path across Dossier, Storybook, doc-web, and CineForge

### Changed
- Marked Story 001 done after validating the Dossier methodology-migration
  preparation line and regenerating the Conductor planning surfaces
- Expanded supervisor close-out guidance so linked target-project worktrees are
  in scope by default, target-project edits stay isolated from primary
  checkouts, and inbox capture rides along with validated landings unless the
  user explicitly excludes it
- Refreshed methodology state so the alignment lane now records real comparison
  history instead of claiming no prior passes exist

## [2026-04-09-02] - Add supervisor alignment and closeout workflows

### Added
- First recorded alignment baseline and a follow-up Conductor story for the
  Dossier state/graph methodology migration
- New `check-in` and `finish-and-push` supervisor close-out skills

### Changed
- Expanded tracked project comparison surfaces to include methodology, setup,
  and scout artifacts by default
- Reworked `triage` to prioritize supervisor pressure and absorbed inbox
  routing into that single skill

## [2026-04-09-01] - Bootstrap Conductor

### Added
- Initial Conductor project scaffold, methodology docs, project registry, and
  supervisor log surfaces
- First-pass supervisor skill surface for triage, scouting, alignment, and
  story flow
