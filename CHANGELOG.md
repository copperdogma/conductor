# Changelog

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
