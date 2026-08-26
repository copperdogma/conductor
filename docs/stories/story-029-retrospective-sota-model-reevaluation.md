---
title: "Retrospective SOTA Model Re-evaluation"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I4"
  - "I5"
spec_refs:
  - "spec:2.1"
  - "spec:2.2"
  - "spec:3.2"
  - "spec:4.1"
  - "spec:4.2"
  - "spec:5.1"
decision_refs: []
depends_on:
  - 28
category_refs:
  - "alignment"
  - "scouting"
  - "story-prep"
  - "memory"
tracked_projects:
  - "conductor"
  - "cine-forge"
  - "doc-web"
  - "echo-forge"
---

# Story 029 — Retrospective SOTA Model Re-evaluation

**Priority**: High
**Status**: Done
**Decision Refs**: None yet
**Depends On**: Story 028

## Goal

Use the repaired evaluation contracts from Story 028 to revisit historical
model attempts in CineForge, doc-web, and Echo Forge, identify candidates that
could plausibly become the current per-surface SOTA, and rerun only those
decision-relevant comparisons with fresh paid calls. Historical results guide
the shortlist but do not substitute for current-contract incumbent parity.

This matters because the validity repair withdrew or downgraded several old
winner claims. The next honest step is to determine whether a newer model now
clears the owning repo's actual quality and operational gates—not to preserve a
default by inertia or launch another indiscriminate model tournament.

## Acceptance Criteria

- [x] A durable cross-project matrix classifies every relevant historical
      attempt as current-contract replayable, shortlist-only, or obsolete, and
      names the smallest justified fresh comparison for each decision surface.
- [x] doc-web removes the proposed 12-case held-out promotion prerequisite and
      records Cam's hand-authored crop goldens as the authoritative normative
      benchmark; new books may expand that suite later but do not block this
      campaign.
- [x] CineForge, doc-web, and Echo Forge each execute fresh incumbent-parity
      comparisons for every historically supported candidate that could
      plausibly become the new SOTA, using isolated worktrees, frozen current
      contracts, provider-valid configurations, progressive stops, and a
      maximum US$5 aggregate provider spend per repo unless Cam approves more.
- [x] Each owning repo records access, transport, reliability, capability,
      latency, cost, privacy eligibility, evidence limits, and an explicit
      per-surface adopt/do-not-adopt/defer recommendation with reproducible
      artifacts and registry history.
- [x] No private fixture is sent over an unapproved route, no scorer/golden is
      tuned to rescue a candidate, and no runtime default changes without a
      separately explicit adoption instruction.
- [x] Conductor preserves the final rerun matrix and corrected portfolio SOTA
      conclusions without becoming the canonical owner of repo-local harnesses.

## Out of Scope

- Dossier work; its dedicated long-running task remains untouched.
- Re-evaluating models that historical evidence already makes operationally or
  contractually incapable of changing a maintained decision.
- Treating exposed hand-authored goldens as invalid merely because they are
  known; they are the product's normative acceptance surface.
- Broad prompt tuning, new private corpora, or speculative model-family sweeps.
- Automatic runtime-default changes, commits, or pushes beyond separately
  authorized closeout.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Audit historical registries, attempts, raw artifacts, and current runtime
      defaults; write the three rerun matrices before paid calls
- [x] Repair doc-web's held-out prerequisite and validate the authoritative
      golden contract
- [x] Execute the bounded owning-repo paid comparisons and retain provenance
- [x] Record per-surface SOTA and adoption recommendations in each repo
- [x] Implement the needed supervisor alignment and work-log changes
- [x] Update related scout or alignment memory if applicable
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check` (not applicable)
  - [x] If scripts or repo checks changed: `make test` (target-repo proportional suites run; no Conductor script changed)
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

- `docs/stories/story-029-retrospective-sota-model-reevaluation.md` — plan,
  approval boundary, work log, and acceptance evidence.
- `docs/alignments/align-045-retrospective-model-rerun-matrix.md` — historical
  classification, candidate shortlists, paid-run decisions, and final SOTA
  synthesis.
- `docs/align-projects.md` — index the retrospective matrix.
- Dedicated target-repo worktrees — doc-web contract correction plus repo-owned
  attempts, result artifacts, registries, tests, and recommendations.

## Notes

- Cam explicitly approved the retrospective story, historical shortlist, and
  paid execution on 2026-08-14. This satisfies the `/build-story` plan gate for
  the bounded plan below.
- Paid work uses each owning repo's credentials and policies, defaults to an
  aggregate US$5 ceiling per repo, and starts only after the matrix and stop
  rules are frozen.
- Existing goldens remain authoritative. A held-out set would answer broader
  unseen-generalization questions but is not a promotion prerequisite here.
- Dossier remains explicitly excluded.

## Plan

1. Create one clean current-main worktree per target repo and record branch,
   base SHA, primary-checkout dirt, credentials/privacy constraints, current
   default, maintained gates, and available raw evidence.
2. Read every relevant registry row and attempt report, inspect differentiating
   failures and retained artifacts, and classify evidence as replayable,
   shortlist-only, or obsolete. Predeclare candidates, incumbent parity,
   configuration arms, spend estimates, retry caps, and progressive stops.
3. In doc-web, remove the 12-case held-out prerequisite and restore the existing
   hand-authored crop suite as the decision-bearing normative benchmark. Keep
   provenance disclosures and future-suite expansion guidance without blocking
   current comparisons.
4. Enter each owning repo and use its local `evaluate-model` workflow to qualify
   transport and run the smallest fresh incumbent/challenger matrix. Inspect
   artifacts between stages, stop candidates that cannot win, and never infer
   semantic failure from invalid transport or incomplete evidence.
5. Update repo-local attempts, registries, stories, manifests, and tests; write
   Alignment 045 with final per-surface SOTA conclusions and explicit limits.
6. Run target-repo focused/full validation proportionate to changed code, then
   Conductor methodology compile/check, lint, diff review, `/validate`, and
   learning review if the user correction or campaign exposes a reusable gap.

**Autonomy**: Go after approval. Cam approved this exact plan and paid calls.
Pause before exceeding US$5 in any repo, sending private data over a route not
already approved by that repo, changing a runtime default, or widening beyond a
historically justified candidate/surface.

## Work Log

- 20260814-0040 — Story created from Cam's explicit instruction to remove the
  doc-web held-out prerequisite, use historical attempts to choose reruns, and
  make paid calls for any candidate that could plausibly become the new SOTA.
  Story 028 is the validity-contract dependency; Dossier and implicit default
  changes remain excluded.
- 20260814-0045 — Read Conductor Ideal, Spec, state, graph, and the current
  provider-native `evaluate-model` contract. Execution will be sequential in
  isolated owning-repo worktrees because no new delegation was requested;
  Conductor itself will only own the matrix and handoff record.
- 20260814-0145 — Completed the three owning-repo campaigns. Fresh incumbent
  parity established per-surface measured leaders independently from hard
  production eligibility. GPT-5.6 Terra is the only new leader and eligible
  winner, on doc-web detector (`13/13`, `0.9689`). CineForge incumbents remain
  measured leaders but all miss repaired quality targets; Echo Forge is an
  official `0/2` three-way tie and its executable default no longer has a sole
  SOTA claim. The doc-web held-out prerequisite is removed. Conservative total
  spend was `$1.32303`; no private data or runtime default changed.
