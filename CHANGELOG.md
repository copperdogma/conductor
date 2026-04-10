# Changelog

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
