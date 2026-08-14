---
title: "Eval Validity Audit and Repair"
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
depends_on: []
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

# Story 028 — Eval Validity Audit and Repair

**Priority**: High
**Status**: Done
**Decision Refs**: None yet
**Depends On**: None

## Goal

Restore confidence in model-selection evidence across CineForge QA, doc-web
crop validation, and Echo Forge scene-to-soundscape evaluation. Independently
separate factual golden correctness, scorer/prompt alignment, adoption policy,
and incumbent/challenger parity; repair proven defects in each owning repo;
then preserve a durable cross-project account of which model conclusions still
hold.

This work matters because repeated challenger rejection is only useful if the
incumbent was measured under the same current contract and the hard gate tests
an explicit product requirement rather than a hidden golden preference.

## Acceptance Criteria

- [x] CineForge QA no longer compares current challengers against contaminated
      historical incumbent evidence; the prompt, golden, and scorer agree on
      what a passing explanation must contain, with regression tests and a
      current-contract incumbent/challenger comparison or an explicit blocked
      record.
- [x] Echo Forge transition-duration scoring tests an explicit product
      requirement rather than an unstated exact-golden preference; frozen
      outputs are honestly regraded and semantic quality remains separate from
      latency/cost adoption gates.
- [x] doc-web retains source-correct visual exclusions while preventing a
      repeatedly prompt-tuned case from acting as the sole hidden selection
      oracle; incumbent and challenger evidence is comparable under a declared
      current contract, with visual review retained.
- [x] Each target repo has an isolated worktree, repo-local durable evidence,
      focused regression coverage, and proportionate validation. No primary
      checkout, runtime default, commit, or remote is changed implicitly.
- [x] Conductor records the cross-project failure modes and corrected adoption
      conclusions without becoming the canonical owner of repo-local harnesses.

## Out of Scope

- Any work in Dossier; its dedicated task and checkout remain untouched.
- Broad paid model sweeps, private-data calls, or speculative provider changes.
- Automatic runtime-default changes. A model promotion requires fresh,
  independently valid evidence and a separately explicit adoption decision.
- Commits, pushes, merges, or edits in target projects' primary checkouts.
- Making every repo use identical scorer text, fixture structure, or thresholds.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and scout context
- [x] Audit and repair the three repo-local evaluation contracts in isolated
      worktrees with disjoint subagent ownership
- [x] Regrade retained outputs and rerun actual incumbents where available and
      proportionate; record any credential/runtime blocker rather than
      substituting historical scores
- [x] Add a cross-project alignment record and update Scout 054's downstream
      disposition
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: not applicable; no Conductor skill changed
  - [x] If scripts or repo checks changed: not applicable; Conductor changes are documentation/generated graph only
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

- `docs/stories/story-028-eval-validity-audit-and-repair.md` — approved plan,
  work log, and cross-project acceptance evidence.
- `docs/alignments/align-044-eval-validity-and-incumbent-parity.md` — durable
  comparison of repaired local contracts and remaining intentional divergence.
- `docs/align-projects.md` — index the alignment result.
- `docs/scout/scout-054-gemini-37-flash-deepseek-v4-pro-api-eval-routing.md` —
  append corrected downstream evaluation disposition.
- Dedicated target-repo worktrees — repo-owned stories/attempts, scorer or
  prompt/golden repairs, frozen-output regrades, and regression tests.

## Notes

- Cam explicitly approved the three-repo audit and requested one subagent per
  repo. This approval satisfies the build-story plan gate for the bounded plan
  below; pause only if a repair requires product preference or a production
  default decision.
- Initial evidence already confirms an Echo Forge duration tolerance not stated
  by the prompt and a CineForge registry comparison between current challengers
  and historical evidence that the same registry marks contaminated.
- Manual inspection supports doc-web's `page-126-000` fail label. The audit is
  therefore about selection contamination and gate design, not presuming the
  image golden is wrong.
- Dossier is explicitly excluded.

## Plan

1. Resolve current base commits and create one isolated worktree/branch for
   CineForge, doc-web, and Echo Forge without disturbing primary checkout dirt.
2. Delegate one repo to each subagent with explicit ownership of that
   worktree's evaluation contract, regression tests, regrade evidence, and
   repo-local documentation.
3. Require each lane to classify separately: source/golden truth,
   prompt/scorer agreement, selection-set contamination, current incumbent
   parity, semantic capability, and operational adoption.
4. Repair only independently demonstrated contract defects. Preserve valid
   safety cases as regression tests, quarantine or split prompt-tuned selection
   cases where warranted, and rerun/regrade the smallest decision-bearing
   matrix.
5. Integrate the three reports into one Conductor alignment, update Scout 054,
   and run methodology compile/check, lint, target-repo focused tests, and
   honest broader checks proportional to changed code.

**Autonomy**: Go after approval. Cam approved this exact bounded audit in the
2026-08-13 task and explicitly requested subagents for each repo. Pause before
any default change, use of private data, material paid expansion, commit, push,
or product-preference decision not entailed by existing Ideal/spec contracts.

## Work Log

- 20260813-1625 — Story created from Cam's approved follow-up to the Gemini 3.7
  Flash / DeepSeek V4 Pro results. Scope fixed to CineForge, doc-web, Echo
  Forge, and Conductor; Dossier and implicit default/remote changes excluded.
- 20260813-1630 — Initial audit evidence recorded: Echo Forge's maintained
  scorer requires transition durations within 0.5 seconds although its prompt
  only requests short crossfades; CineForge labels old QA rows contaminated but
  still names an old-contract GPT-4.1 Mini row the production winner; visual
  review supports doc-web's recurring `page-126-000` fail label while its use
  in prompt tuning raises selection-contamination risk.
- 20260813-1640 — Compiled Story 028 into `docs/stories.md` and the methodology
  graph, then delegated disjoint CineForge, doc-web, and Echo Forge repair lanes
  to one subagent each. Each contract requires isolated worktrees, source-first
  adjudication, current-contract comparator parity, frozen-output regrading,
  separate semantic and operational verdicts, and no implicit default, commit,
  push, private-data, or Dossier work.
- 20260813-1645 — Added Alignment 044's portable six-layer validity contract
  and calibration/selection/safety-regression role split. Repo outcomes remain
  explicitly pending until their local repairs and tests complete.
- 20260813-1710 — Echo Forge repair completed in its isolated worktree. Replaced
  hidden exact-golden duration tolerance with tested `0.5`–`5` second semantic
  crossfade bounds and symmetrically regraded every frozen attempt. DeepSeek V4
  Pro changed `0/2` to `2/2` quality; all other scores remained stable. It
  remains an operational reject at `66.889` seconds average plus degraded
  initial routing, so `gpt-5.4-mini` stays executable default. Full repo-local
  validation passed; repair spend `$0`; no primary/default/commit/remote change.
- 20260813-1715 — Reused Echo's freed agent slot for CineForge's required
  independent source-first QA verification. The verifier received no parent
  history or disputed golden/model output and is following the repo-local
  golden-verification protocol before the owning agent finalizes its repair.
- 20260813-1740 — doc-web validity repair completed in its isolated worktree.
  Preserved `page-126-000` as a source-backed production-safety veto, but
  reclassified all exposed crop cases as calibration/regression evidence and
  blocked intrinsic winner claims pending held-out truth. No honest held-out
  could be formed from the three available unscored, pass-style crops; a
  balanced 12-crop, eight-unused-page confirmation contract is now frozen for
  the next run. Focused and repo-wide lint/methodology/regrade checks passed;
  follow-up spend `$0`; primary/default/golden/commit/remote state unchanged.
- 20260813-1745 — CineForge's first blind verifier independently confirmed the
  exact-event summary anchors had no production basis and found a separate
  source spelling defect (`RUDDY & GREENE`). It corrected only protocol-owned
  fixture/golden facts, confirmed all eight negative defects, and did not read
  the scorer, task, results, registry, story, or prior attempt. The owning lane
  started its required second verification before current-contract reruns.
- 20260813-1810 — First strict candidate-close review of doc-web found two
  accepted material defects: the new frozen-result regrader failed open on
  duplicate keys, partition overlap, blocked selection status, and failed
  held-out rows; Attempt 026 also recorded the pre-repair detector prompt hash
  while the integer arm actually used a changed coordinate prompt. Classified
  as one systemic provenance/regrader class and returned for focused repair and
  adversarial confirmation. The safety golden and `39/40` raw result remain
  supported; no provider rerun is required.
- 20260813-1825 — First strict candidate-close review of Echo Forge found two
  accepted material defects. Removing exact-golden duration equality was
  warranted, but the replacement `0.5`–`5` second endpoints were an unsupported
  post-hoc product preference; final timing is delegated to the Executor and
  numeric duration should not decide scene-understanding quality absent a
  source-backed product range. The runner also recorded reasoning/max-token
  flags for providers that ignored them and could retain stale top-level config
  under `--force`. Returned as systemic contract/provenance repair; frozen
  outputs remain sufficient and no provider rerun is required.
- 20260813-1850 — doc-web repaired the systemic regrader/provenance class with
  fail-closed duplicate, overlap, coverage, status, and held-out-quality rules
  plus corrected normalized/integer prompt and provider hashes. A fresh
  candidate-close worker then reinspected all 18 files, reproduced the
  adversarial cases, verified raw hashes and `39/40` evidence, and returned
  `RESULT: no-issue`. The doc-web lane is clean and complete.
- 20260813-1855 — CineForge completed identical current-production-contract
  two-case reruns: GPT-4.1 Mini `0.9044`, `3.148s`, `$0.000955/call`; Gemini 3.7
  `0.9139`, `2.340s`, `$0.003324/call`. Both verdicts are correct, but neither
  reaches the exact `1.0` quality target; Gemini's two-case `+0.0095` edge does
  not justify its `3.48x` cost or a default change. A fresh candidate-blind
  reviewer is deriving the negative-case feedback threshold from production
  obligations before accepting or rejecting the post-run `6` to `4` change.
- 20260813-1915 — CineForge's candidate-blind threshold review blocked both the
  proposed four-count and old six-count gates. One combined metadata issue
  received triple credit and, with a confidence warning, passed while omitting
  identity, fabricated plot, and conflict; a generic failure summary also
  passed. Reviewer derived six non-overlapping repair families and required
  critical identity/plot/beats coverage plus source-specific feedback. Returned
  for family-based systemic repair; no candidate-driven threshold tuning.
- 20260813-1920 — Echo Forge's second candidate-close confirmed the duration
  and effective-config repairs, then found another fail-open evidence defect:
  wrong served model/error status and unbound output bytes could be accepted or
  reused. Because two consecutive passes hit the same provenance class, the
  loop switched from instance repair to a bounded systemic audit of the full
  request/response/metadata/output/reuse chain before candidate-close resumes.
- 20260813-1950 — Fresh full-scope CineForge review blocked three remaining
  classes: adjective-only positive and sparse two-token family findings could
  still score `1.0`; two pre-final-contract Gemini rows remained marked
  decision-grade and generated a stale current winner; Story 213's claimed
  hash-complete manifest omitted Attempt 026/current provider/results and held
  stale contract hashes. Returned for actionable source-specific family
  matching, uniform historical contamination, graph regeneration, and complete
  manifest repair. Frozen final-contract regrades still fail both models and no
  default conclusion changes.
- 20260813-2010 — After those three fixes, the next fresh CineForge pass found
  the same semantic-matcher class still fail-open to polarity: six issues that
  explicitly denied every candidate defect scored `1.0`, as did a positive
  summary that ended with a material tone contradiction. Because repeated
  matcher defects survived phrase-level hardening, the loop switched to a
  bounded systemic polarity audit across all six families and both positive
  and negative summaries. If deterministic text matching cannot establish the
  relation honestly, the lane must fail closed and report capability unmeasured
  rather than weaken the gate.
- 20260813-2035 — Echo Forge's post-systemic final probe found that retained
  normalized output plus a migrated validation marker cannot recompute strict
  pre-normalization schema truth. Paired output/hash tampering was accepted and
  the real normalized dungeon output lacks a schema-required property removed
  during normalization; raw response bytes were never retained. Returned to
  add raw-content/hash plus deterministic-normalization provenance for future
  captures and to downgrade the historical V4 semantic `2/2` to diagnostic,
  non-decision-grade evidence. Its independent latency/routing operational
  rejection remains valid.
- 20260813-2055 — CineForge's polarity candidate-close confirmed explicit
  negation/contrast defenses but found modal ambiguity still received hard
  credit: a fully hedged six-family response using `may`/`might`/`perhaps`/
  `appears to`/`seems to` scored `1.0`. Returned for one bounded systemic
  modality matrix across every family and negative-summary anchor. This stays
  inside the declared fail-closed canonical-language contract; it does not
  expand into general entailment.
- 20260813-2110 — Echo Forge closed clean after refusing to synthesize missing
  V4 raw evidence. The historical bundle is now `legacy-incomplete-provenance`:
  normalized non-duration semantics are diagnostic `2/2`, while strict output
  and decision-grade capability are unmeasured; the independent `66.889s`/
  routing operational rejection remains. Future public/synthetic v3 captures
  bind exact raw assistant content through strict schema and deterministic
  normalization. Focused `47/47`, full `520/520`, and a fresh final review all
  passed; follow-up spend `$0`.
- 20260813-2140 — CineForge closed clean after systemic family, polarity,
  modality, and clause-role repair. Candidate-defect and source-correction
  proofs are disjoint and clause-local; sparse, negated, hedged, contrastive,
  source-correct-only, and token-bridge attacks fail closed across all six
  families. All `29` historical QA rows are non-decision-grade and QA
  `latestScore` is null. Frozen GPT/Gemini results remain `0.832475`/`0.834975`,
  both fail; fresh final-contract parity is unmeasured. Focused `168`, full
  unit, golden, registry/truth-ledger/manifest/methodology/lint/diff checks and
  a fresh final reviewer all passed.
- 20260813-2145 — Integrated final outcomes into Alignment 044 and Scout 054.
  The corrected portfolio conclusion is no promotion: doc-web needs untouched
  held-out truth, CineForge has no decision-grade current QA winner, and Echo's
  V4 semantic `2/2` is diagnostic-only while its operational rejection remains
  valid. All target changes remain isolated and uncommitted; Dossier and
  production defaults remain untouched.
- 20260813-2150 — `/validate` found no remaining material defect. Reviewed the
  complete Conductor status, diff, untracked set, generated index/graph, and
  each isolated target worktree. Fresh direct reruns passed the CineForge
  scorer/golden/manifest/runtime-provider slice, doc-web's `16/16` crop
  substrate tests, and Echo Forge's `47/47` transition/provenance tests.
  Conductor methodology compile/check, lint, and diff checks passed. The final
  independent full-scope reviewers returned `RESULT: no-issue` for all three
  lanes. Residual limits are deliberately recorded as unmeasured evidence, not
  hidden implementation gaps. `codex review` was skipped for Conductor's
  docs-only diff; the target code received repeated independent hostile review
  through `/loop-verify`.
- 20260813-2155 — `/learning-review` returned `RESULT: candidate-warranted`
  (`repeated-friction` and `high-risk-miss`, high confidence). Candidate target:
  the distributed `evaluate-model` / `improve-eval` guidance and repo-local eval
  runbooks. Proposed lesson: decision-grade runs should predeclare evidence-set
  roles, invalidate incompatible historical scores after contract changes,
  retain recomputable raw-to-normalized structured-output evidence, and probe
  semantic scorers for negation, modality, duplicate credit, and cross-clause
  borrowing before paid comparisons. Promotion is intentionally deferred to
  `/learning-candidate`, comparison against existing detailed guidance, and a
  recommendation-first alignment decision; no live skill changed here.
- 20260813-2200 — `/mark-story-done` closed Story 028 after all acceptance
  criteria, tasks, Build, and Validation gates passed. No changelog entry was
  needed because this episode produced supervisor evidence and isolated
  unlanded target patches rather than a shipped Conductor runtime or skill
  change.
