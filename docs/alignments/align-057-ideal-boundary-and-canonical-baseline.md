# Alignment 057 — Ideal boundaries and the reusable methodology baseline

Date: 2026-10-17. Status: local guidance updated; target Ideal review complete;
no target rewrites or rollout performed.

## Owner intent and local changes

Cam clarified that the Ideal is a short north star of desired outcomes with
zero implementation. Technical capability should not constrain the aspiration;
"magic" is a shorthand for that freedom, not a style of prose.

Cam also clarified Conductor's responsibilities: improve projects and assess
how they and their skills work, evaluate models on their behalf, and maintain
the canonical reusable skills/methodology for new and existing projects.
Canonical means the best reviewed reusable baseline, not an absolute newest
copy of everything. Generic, evidence-backed, non-overfit local improvements
should be considered for promotion back into Conductor. Projects retain their
product truth and justified adaptations.

The local Ideal, Spec, AGENTS, README, methodology explanation, kickoff/setup
skills and runbooks, setup checklist, and alignment skill now reflect these
boundaries. [ADR-004](../decisions/adr-004-canonical-skills-and-methodology.md)
partially supersedes ADR-001 without erasing its history. No external technical
research was needed to resolve the explicit owner decision.

## Review scope and method

Reviewed all 11 projects in `projects.yaml`, plus seven additional distinct
local repositories with `docs/ideal.md`. Duplicate evaluation/development
worktrees were excluded using their Git common directory. Additional reviewed
repos are not enrolled in the registry. App inventory was inspected; this is
not a complete search of every folder, remote host, or cloud project.

Read-only reviewers read root AGENTS where present, then Ideals. The coordinator
checked cited passages and revised findings that confused desired execution
experience, user interaction, or product identity with implementation. No
product tests, provider calls, private financial records, or target writes.

Counts use `len(text.split())`, including headings, and indicate editing burden
rather than a correctness threshold. File hashes, paths, checkout heads, and
scope are in [source evidence](evidence/align-057-ideal-audit.json). Heads alone
do not describe dirty working copies; the hashes identify reviewed content.

Classification is **methodology conflict** for implementation/process leakage,
with **portable improvement** in Conductor's new authoring guidance. Product
needs and useful local distinctions are **intentional adaptation** to preserve.

## Findings

Five Ideals have substantial mixing, ten have localized leakage or stage/proof
material, and three are substantially clean. Length and repetition are separate
findings: a long outcome statement is not automatically implementation.

| Project | Words | Finding | Recommended treatment |
| --- | ---: | --- | --- |
| Dossier | 1,329 | Substantial mixing | Move schema/architecture and eval contracts; condense repeated outcomes. |
| Storybook | 2,082 | Light leakage; substantial repetition | Preserve the distinctive narrative; relocate the minimum floor and compress repeated needs. |
| Doc Web (file calls itself Doc-forge) | 992 | Substantial mixing | Separate conversion pipeline and acceptance targets from fidelity/traceability outcomes. |
| CineForge | 3,491 | Substantial mixing | Separate persistence design and detailed quality fixtures; strongly condense. |
| Board Game Ingester | 827 | Light leakage; repetition | Condense the Builder handoff vision; move reliability/workflow scaffolding guidance. |
| Robo Rally | 1,277 | Light leakage; repetition | Preserve game/reuse outcomes; move named eval/golden seeds and duplicate floors. |
| Echo Forge | 641 | Light leakage | Move the prescribed physical synthesis mechanism; retain sound creation and reuse. |
| Ultima IV Web | 802 | Light leakage | Preserve autonomous-player outcome; move its learning procedure and qualifying-run protocol. |
| Financial Hub | 657 | Light leakage | Move named application/source strategy and initial-release scope. |
| Financial Monthly Analysis | 2,130 | Substantial mixing | Separate implementation/security controls, pilot sequence, and current operating details. |
| VLC Thumbs | 481 | Clean; repetition | Optional compression of repeated outcomes and removal of methodology meta-text. |
| Alain Lessard Book* | 547 | Light leakage | Move script/output-path/manifest mechanics; preserve archive and audio identity. |
| Canmore Town Council* | 337 | Light leakage | Move transcription/index pipeline; preserve official-source coverage and honest speaker uncertainty. |
| Onward to the Unknown website* | 591 | Light leakage | Move normalized-content-model and repo-resumption mechanics. |
| Ravenloft Cthulhu* | 252 | Clean | Keep the distinctive campaign north star. |
| RoboRally Web* | 481 | Light stage leakage | Relocate one-course minimum floor; retain complete 2015-edition ambition. |
| RPG Map Projector* | 406 | Clean | Keep physical-table, secrecy, calibration, and DM-control outcomes. |
| Wyze HomeKit* | 415 | Substantial mixing | Move architecture candidates, discovery questions, build order, and verification procedures. |

\* Additional local repo; no registry membership change implied.

## Exact examples and preservation boundaries

- **Dossier:** `docs/ideal.md:69–77` prescribes closed vocabularies and
  architecture extensibility; `:86–88` names document/chunk/character-offset
  representation; `:144–147` mandates golden scale and acceptance policy.
  Route detailed representation to Spec/ADR and proof contracts to evals.
  Preserve source-backed knowledge, honest ambiguity, temporal meaning,
  completeness, consistent consumer results, privacy, and cross-domain use.
  A knowledge-graph library can name its output; technical product identity is
  not automatically an architecture violation.
- **Storybook:** `:80–87` defines a minimum viable floor. Move that contract to
  Spec/evals. The conversational execution ideal at `:31–38` is a valid desired
  development experience. Seamless voice at `:74` is a UX aspiration, not by
  itself implementation leakage. Preserve Luna's warmth, narrator-stated
  memory rather than adjudicated reality, continuity, elderly accessibility,
  artifacts, consent, and the prohibition on psychological interpretation.
- **Doc Web:** `:56–68` decomposes conversion into named internal stages and a
  normalized intermediate representation; `:76–77` sets sample/time/cost proof
  thresholds. Move mechanisms to Spec/architecture and thresholds to evals.
  Preserve no-configuration use, fidelity, source traceability, useful downstream
  output, and explicit uncertainty. Its Dossier relationship can be product
  identity; converter graduation procedure belongs in operating guidance.
- **CineForge:** `:181` requires complete snapshots and forbids reconstruction
  from diffs, an unambiguous storage choice. `:159–161` prescribes readiness
  colors; `:82`, `:129`, and other quality-bar examples are detailed fixture
  material. Move mechanisms to Spec/ADR and fixtures to evals. Preserve
  psychologically safe revision/history, cinematic creative collaboration,
  authorship and control, real-world assets, production usefulness, professional
  interoperability, and the ability to participate at different depths. Export
  compatibility and production artifacts may be real product needs; do not
  discard them merely because they name technical formats.
- **Board Game Ingester:** `:21` teaches what to do while a step is unreliable;
  `:41` discusses eval/process scaffolding deletion. These are methodology
  concerns. The Builder-ready handoff, source-quality images, usable rules,
  completeness, provenance, explicit gaps, and sparse human judgment are product
  needs. HTML/manifest compatibility with the receiving product may be an
  external contract, not arbitrary implementation; preserve that intent and
  route its detailed interface definition to Spec.
- **Robo Rally:** `:138–156` names a root eval and golden seeds; move that proof
  catalog to evals while keeping the underlying outcomes. `:54–71` describes
  the desired development experience and is not automatically leakage. Preserve
  classic rules, solo pressure, trusted and explainable race outcomes, private
  use, save/replay, multiple play surfaces, and reusable game-building learning.
- **Echo Forge:** `:59` prescribes calculating sound from layered physical
  components, rather than library playback, while `:63–65` says the best result
  wins regardless of source. Separate sound-creation capability from its
  mechanism; leave synthesis choices to Spec/ADR. Preserve GM control, table
  flow, reusable favorites, cinematic sound, accessibility, rights safety, and
  availability during unreliable connectivity. Audition/save interactions are
  user experiences, not inherently implementation.
- **Ultima IV Web:** `:60–64` prescribes speedrunner-style authoring with saves,
  reloads, and accumulated player skills; `:66–69` defines the qualifying-run
  protocol. Move procedures to runbook/evals without dropping independent,
  honest, repeatable earned-completion evidence. The autonomous player at
  `:49–55` is a desired deliverable; keep it alongside original browser fidelity,
  distinct comfortable mobile play, and transparent AI capability learning.
- **Financial Hub:** `:82–84` mandates Sure as implementation; `:96–98` discusses
  current acquisition/handoff strategy; `:103–107` scopes the first release.
  Route those to Spec/stories. Preserve private read-only analysis, provenance,
  dated context, history without hindsight, calm attention, and owner decisions.
  Source-preparation versus analysis ownership remains a useful product boundary.
- **Financial Monthly Analysis:** `:90–95` specifies pilot/catch-up sequence;
  `:101–113` mandates a release-pinned application and precise URL/CSRF/handoff
  mechanisms; `:198–203` prescribes hosting/access architecture and staged
  reporting. Route to Spec/security ADR/runbook/story as appropriate. Preserve
  household usefulness without surveillance or shame, uncertainty, source
  coverage, receipt corroboration, family value and effort, control over
  execution, and verified realized outcomes. No security control is to be
  removed from its governing operational artifact merely to shorten the Ideal.
- **VLC Thumbs:** `:27–30` is outcome-only execution aspiration and may stay.
  Requirements `:40–46` repeat desired outcomes; technical identity as a VLC
  feature is appropriate. `:60–61` is a methodology routing reminder, not a
  leaked implementation. Optional compression, no urgent rewrite.
- **Alain Lessard Book:** `:34–41` specifies output paths, repo scripts, and
  manifests; `:49–50` prescribes image-processing method. Route to Spec/runbook.
  Preserve source lineage, faithful family archive, warm tone, accessible site,
  and narrative audio without inappropriate table narration.
- **Canmore Town Council:** `:31–36` specifies extraction/transcription/
  normalization and static index construction. Move mechanics to Spec/runbook.
  Source matching and honest speaker labels remain user-valued capabilities;
  preserve official-source coverage and the distinction from official minutes.
- **Onward website:** `:35–37` and `:51–52` prescribe a normalized reusable
  content model; `:40–42` specifies repo artifacts for resumption. Route to
  Spec/runbook, preserving warm family reading/audio, elderly accessibility,
  source links, completeness, and easy continuity after time away.
- **Ravenloft Cthulhu:** retain the compact thematic and player-experience
  intent. Campaign structure is creative product content, not software
  implementation leakage.
- **RoboRally Web:** `:61–65` reduces the complete game to a minimum one-course
  floor. Move staged acceptance to Spec/story; preserve complete 2015 rules,
  digital usability, multiplayer/solo play, all-screen use, and readable chaos.
  This is a distinct repository from registry project `roborally`.
- **RPG Map Projector:** calibration, physical table conditions, reversible
  edits, manual fallback, and player-safe reveal are product experiences. Keep
  them; do not mistake physical requirements for implementation decisions.
- **Wyze HomeKit:** `:24–34` names a bridge architecture and candidates;
  `:36–42` lists current discovery questions; `:47–50` prescribes command
  recording, actual-device proof, and first-camera build order. Route to
  Spec/ADR, inbox/story, and runbook/evals. Preserve two distinct cameras,
  reliable Apple Home viewing/recovery, private local availability with visible
  dependencies, additional stream consumers, and recoverability.

Line numbers refer to the hashed source files in the evidence record. The
financial findings intentionally omit private records and operational values.

## Recommended next action

Prepare isolated rewrite proposals for CineForge, Financial Monthly Analysis,
Dossier, Doc Web, and Wyze HomeKit, starting with CineForge and Financial Monthly
Analysis for the largest reduction in mixed vision/spec material. Keep source
provenance, map moved requirement IDs and links, retain detailed needs in the
owning Spec/ADR/evals, and show the proposed outcome-only Ideal for review.
Do not delete contract detail or weaken proof/privacy/security gates.

That follow-up is not performed or authorized by this review. Additional local
repos remain outside managed rollout membership; resolve membership through the
alignment inventory check before any broader rollout. Existing target checkout
changes are shared workspace and must remain untouched.

## Validation and limits

- Local docs-only checks: methodology compile/check, skills-check, lint, and
  whitespace check passed for the final local guidance/report/index/evidence.
  All 18 reviewed source hashes remain unchanged and report/ADR links resolve.
- Source evidence covers 18 distinct target Ideals; no target edits.
- One independent synthetic drafting exercise from the preceding guidance
  update kept proposed stack details out while preserving user outcomes. That
  is a bounded behavior check, not proof across real future kickoffs.
- The standalone skill-creator validator was unavailable because PyYAML was
  absent; repo-native skill-surface checks pass.
- No commit, push, enrollment, scheduled monitor, or cross-project application.
