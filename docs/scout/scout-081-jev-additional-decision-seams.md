# Scout 081 — Additional Jev decision seams

Date: 2026-09-30
Status: Complete; deterministic repair landed, NO-GO normal/default Jev use

Cam requested another repository pass for complex heuristics or full LLM calls
whose useful output is a decision. Inspected all seven registered owners,
Conductor scripts, and the previously considered Wyze HomeKit next-action router.
The initial audit changed no owner code/credentials/defaults/deployment and ran
no paid calls. The subsequently approved owner benchmark and live comparison
are recorded below; the later optional runtime prototype stays off by default.
Initial authored changes were this record and Conductor intake/index entries.
The owner primary checkouts are current inspection evidence, not necessarily
deployed code or the newest isolated implementation branch.

## Recommendation

Start with Echo Forge's six-way scene intent classification. It is an active,
bounded semantic decision presently approximated with token lists and word counts.
Build an offline comparison first; runtime savings are unmeasured. Dossier's
acquaintance participant selection is another narrow semantic seam, with greater
identity consequences. CineForge offers the clearest full-LLM verdict subtask,
but the existing call also performs work Jev cannot simply replace.

Scout 072 already covered relationship-correction intent, retrieval reranking,
Echo cue/control intent, broad Dossier assertion review, Doc Web consistency
triage, and tentative format/game routing. Those are not new findings here.
Storybook artifact-link judging was also already noted; it is not counted again.

## New shortlist

### 1. Echo Forge — scene intent classification

- Evidence: [sceneAssembly.ts:220](/Users/cam/Documents/Projects/echo-forge/src/soundscape/sceneAssembly.ts:220).
  The function selects six intents using action/creature/weather/recall/destructive
  tokens, matcher capabilities, scene state and narration-length thresholds.
  `App.tsx` calls the proposal assembler at lines 3028 and 4656; this is an app
  path, rather than only an unused benchmark helper.
- Jev shape: one Choice over the six existing intents plus unknown, supplied with
  query, current scene, and candidate metadata. Code preserves candidate IDs,
  command construction, permissions, destructive-action handling and confirmation.
  This is finer-grained scene proposal routing, adjacent to but distinct from the
  prior binary PTT control-intent evaluation.
- Baseline: [sceneAssembly.test.ts:43](/Users/cam/Documents/Projects/echo-forge/src/soundscape/sceneAssembly.test.ts:43).
  Add independently labeled paraphrases, negation, quoted requests, mixed intents,
  absent candidates and stale scene state. Measure intent errors and resulting
  proposal behavior, plus complete latency/cost/abstention against the local router.
- Limit: local rules currently have no inference cost. Jev adds a network boundary;
  lower maintenance and better interpretation must justify that cost. Start offline
  or in shadow; inferred intent does not authorize playback.

### 2. Dossier — who does an explicit acquaintance cue refer to?

- Evidence: [repair_explicit_acquaintance_edges.py:320](/Users/cam/Documents/Projects/dossier/src/dossier/stages/repair_explicit_acquaintance_edges.py:320).
  Role/name patterns collect people near a cue such as “They met once”; lines
  370–376 select the first two grounded people and assume later attendees are incidental.
  Other fallbacks use prior names and speaker-relative roles. The standard runtime
  invokes mention repair after adjudication in
  [engine_runtime_support.py:357](/Users/cam/Documents/Projects/dossier/src/dossier/engine_runtime_support.py:357).
- Jev shape: Choice over code-enumerated, grounded person pairs plus insufficient
  evidence, using the relevant turn and mentions. Keep explicit cue detection,
  entity identity, edge direction, provenance and graph updates in owner code.
- Baseline: [test_repair_explicit_acquaintance_edges.py](/Users/cam/Documents/Projects/dossier/tests/unit/test_repair_explicit_acquaintance_edges.py).
  Test novel multi-person turns, incidental attendees, repeated first names,
  changed introduction order, negation and insufficient context. Measure wrong-pair
  rate and missed explicit acquaintances; initially record suggestions only.
- Limit: existing repairs already address known cases. This targets generalization,
  not an established current defect, and does not optimize a newer standalone
  semantic compiler merely because the ordinary pipeline contains it.

### 3. CineForge — candidate entity verdicts

- Evidence: [entity_adjudication.py:44](/Users/cam/Documents/Projects/cine-forge/src/cine_forge/ai/entity_adjudication.py:44)
  calls a full LLM on a code-extracted candidate list and script excerpt.
  [candidate_resolution.py:224](/Users/cam/Documents/Projects/cine-forge/src/cine_forge/modules/world_building/character_bible_v1/candidate_resolution.py:224)
  consumes verdicts before character-bible generation, rejecting non-valid candidates.
- Jev shape: Choice for valid / invalid / retype / insufficient evidence, with
  closed target-type options if retyping applies. Supply candidate-specific script
  evidence and the relevant neighboring identities.
- Baseline: character-bible unit tests cover invalid-candidate rejection and alias
  merging, but their mocked adjudicator outputs are not independent semantic gold.
  Build source-reviewed cases containing real minor characters, formatting tokens,
  sound cues, alias pairs and numbered roles.
- Limit: the incumbent also generates canonical names, merges aliases and explains
  decisions. Jev verdicts alone are not its full contract. Benchmark complete
  workflow savings after retaining canonicalization/rationale/fallback; otherwise
  this could add a call without removing one. False rejection loses real characters.

### 4. Doc Web — ambiguous text block labels

- Evidence: [elements_content_type_v1/main.py:310](/Users/cam/Documents/Projects/doc-web/modules/adapter/elements_content_type_v1/main.py:310)
  contains text/heading/list/table/form heuristics and later page-position nudges.
  An optional full LLM assigns DocLayNet labels at
  [main.py:696](/Users/cam/Documents/Projects/doc-web/modules/adapter/elements_content_type_v1/main.py:696)
  and processes ambiguous elements at line 1155.
- Jev shape: Choice among allowed content labels for ambiguous text elements,
  using neighboring text and available layout metadata. Keep exact input kinds,
  geometry, sequence mapping and known layout roles deterministic. Preserve or
  separately handle subtype metadata; it is part of the current output contract.
- Baseline: [test_elements_content_type_v1.py](/Users/cam/Documents/Projects/doc-web/tests/test_elements_content_type_v1.py),
  extended with source-reviewed headings, captions, lists, form fields and noisy OCR
  from multiple document structures. Measure downstream HTML structure, not labels alone.
- Limit: `module.yaml:8` defaults `use_llm` to false, and this pass found no recipe
  explicitly enabling that branch. This is an available heuristic/optional-LLM seam,
  not demonstrated ongoing inference spend. Text cannot recover missing pixel evidence.

### 5. Storybook — ambiguous person-match suggestions

- Evidence: [person-resolution.ts:426](/Users/cam/Documents/Projects/Storybook/storybook/packages/backend/src/ai/person-resolution.ts:426)
  handles uncertain-name matches; line 482 collects exact canonical identity matches.
  Unique matches merge; a unique exact display-name rule can also resolve a match;
  otherwise the ordinary branch creates a person at line 512.
- Jev shape: Choice among eligible existing person IDs / new person / unknown,
  based on proposal and source context, presented as a review suggestion.
- Baseline: [person-resolution.test.ts](/Users/cam/Documents/Projects/Storybook/storybook/packages/backend/src/__tests__/person-resolution.test.ts)
  covers alias merges, uncertain names, household aliases and false-merge cases.
- Limit: false merges are more consequential than duplicate records. Preserve self,
  uncertainty, role and ambiguity guards. Defer until observed duplicate/review volume
  establishes value; a model verdict must not itself authorize a merge.

## Secondary and excluded seams

- Dossier [filter.py:441](/Users/cam/Documents/Projects/dossier/src/dossier/stages/filter.py:441)
  checks pronouns, compound/group labels, redundant buckets, name fragments and
  non-entities. Possible semantic review triage, but the current function lacks
  source quotes and deterministic redundancies should remain code. Obtain evidence
  context first; do not replace it with model-authorized pruning.
- CineForge story-format classification remains an earlier tentative idea, with
  substantial parser/structural evidence. It is not a new priority.
- Doc Web OCR candidate selection and escalation also contain text-quality
  heuristics (`pick_best_engine_v1` and `ocr_escalate_gpt4v_v1`), but this pass
  found no active recipe callers. A semantic readability judgment could miss
  names, tables or valid non-prose text; establish an active quality gap first.
- Board Game Ingester: inspected source-role lane derives geometry from pixels;
  semantic package assembly consumes Doc Web output. No compelling additional
  bounded text decision identified in the inspected paths.
- Robo Rally: checkpoint/facing/card selection depends on deterministic spatial
  simulation and legality. No compelling additional semantic-text decision found.
- Conductor: inspected scripts are metadata, credential and methodology checks;
  no high-volume runtime semantic decision seam established.
- Wyze HomeKit: `scripts/next-action.sh:112` orders exact service/readiness probes.
  That routing belongs in code; ambiguous-log triage remains the prior unqualified idea.

## Current provider framing and next step

Official [models](https://docs.typesafe.ai/models) still list text-only
`jev-1.13.0`. The [System One guide](https://docs.typesafe.ai/concepts/system-one)
and [entity alignment cookbook](https://docs.typesafe.ai/cookbooks/entity_alignment)
support typed judgments over explicit state, with arithmetic and execution in code.
These patterns support architectural fit, not measured quality in these repositories.

Recommended next approval: build the offline Echo Forge scene-intent benchmark in
an isolated owner worktree, preserving its current router as baseline. No paid
calls or runtime adoption are implied. Then select a bounded provider comparison
using independently reviewed cases and relative quality/cost/latency measurements.

## Approved offline follow-through — 2026-09-30

Cam approved the specific offline Echo Forge benchmark. Owner branch
`codex/jev-scene-intent-offline-20260930` is isolated at
`/Users/cam/.codex/worktrees/jev-scene-intent-offline-20260930`, based on current
remote main `7ab91978b4048118aab0051832d1f462ff7dca13`. Dirty primary classifier
changes were not imported; the committed baseline and exact source bytes are frozen.

[Story 076](https://github.com/copperdogma/echo-forge/blob/main/docs/stories/story-076-scene-intent-offline-benchmark.md)
is complete for offline construction. The owner retains42 original synthetic cases
(dev28/eval14, group-disjoint but author/reviewer-visible), independent pre-baseline
semantic review, frozen hashes, native Choice request preparation without a network
client, and diagnostic replay with strict case/identity coverage.

The unchanged rules match14/32 cases in their existing six-label vocabulary,
14/42 including the experimental unknown extension. All28 mismatches were reviewed:
18 rule/policy errors against the semantic contract and10 unknown-extension gaps.
11/16 search-or-unknown negatives construct nonempty proposals; no executor/UI/audio
ran, so this is not observed playback or a production-defect count. These deliberately
selected synthetic cases are not a live-session accuracy estimate. Jev is unmeasured.

Owner [report](https://github.com/copperdogma/echo-forge/blob/main/docs/evals/attempts/scene-intent-v1/20260930-offline.md)
and [validation](https://github.com/copperdogma/echo-forge/blob/main/docs/evals/attempts/scene-intent-v1/validation.json)
retain commands and claims. Focused18 tests, affected lint, methodology and whitespace
checks pass; existing methodology-generation warning retained. No credentials,
provider calls, model-evaluation ledger attempt, runtime changes, commits or pushes.
SpendUSD0. Recommended next selection: Jev on frozen synthetic cases versus the actual
rule baseline, with a US$1 total provider ceiling including qualification/recovery,
native response/raw-evidence requirements and no runtime adoption implied.

## Approved live follow-through — 2026-09-30

Cam approved the Jev scene-intent lane with a US$1 cap and requested completion
through a go/no-go decision. The isolated owner Story076 extension is complete.

**GO for a bounded suggestion-only interpretation trial.** Raw Jev recognized
32/32 clear intents vs current rules14/32; all-label38/42. The dev-selected cutoff
.95 accepts25/42 inputs,25/25 correct, with17 for review. Evaluation and its fixed
repeat each achieved9/12 clear intents vs rules6/12, with zero accepted wrong
negative routes or baseline-correct regressions. Unfiltered Jev made four
action-like routing errors on unknown development inputs; preserve that evidence.

57/57 pinned native calls valid, no retries/unresolved spend; total USD.002316762
including qualification/parity/confirmation. Initial unique-case median121ms,
p95201ms; no App/table or full-fallback latency measured. Independent review
reconstructed raw hashes, requests, metrics, cutoff and spend; no material finding.
Temporary provider-only .env removed.23 focused tests, lint, methodology and
provider-free raw replay pass; unchanged compiler warning retained. No runtime
adoption, defaults, execution, commit or push.

Owner [live decision report](https://github.com/copperdogma/echo-forge/blob/main/docs/evals/attempts/scene-intent-v1/20260930-jev-live.md)
and [verified summary](https://github.com/copperdogma/echo-forge/blob/main/docs/evals/artifacts/scene-intent-v1/20260930-live/summary.json)
retain exact evidence. Source/rubric/requests stayed frozen; one secret-error cause
repair after qualification retained old snapshots and changed no request/policy.

This is a small author-visible synthetic challenge benchmark, not a live accuracy
estimate; repeats add reproducibility, not new cases. Better labels do not yet
prove better proposals. Next recommended approval: opt-in suggestion-only route
with explicit review/correction, deterministic action/candidate guards and fresh
representative end-to-end proposal evidence before any default change. Other
audit candidates remain recommendations, not approved paid campaigns.

## Approved opt-in full-proposal trial — 2026-09-30

Cam approved the next integration/fresh-input step. Echo Forge Story077 is in the
separate `codex/jev-scene-intent-trial-20260930` worktree at the same base7ab9197;
Story076's frozen study is preserved. Typed Search now has explicitly submitted,
default-off semantic suggestions, server-only keys, strict bounded native contracts,
stale-response cancellation and code-owned targets/policy. Executor application is
blocked for all Jev-origin proposals; manual Search stays available. No deployment,
commit, push or default adoption is implied.

**NO-GO for normal/default use; diagnostic prototype only.** On16 reviewed fresh
synthetic cases, raw intent15/16, original complete outcomes10/16 vs local7/16,
but positive proposals1/7 vs local3/7 and14/16 manual reviews. A bounded post-output
Scene-ID construction repair replays to11/16 complete,2/7 positives using the same
receipts; retain original10/16 and do not call the replay fresh evidence. No accepted
negative proposals or executor actions. Minimum retention gate passes; practical
positive coverage does not justify normal use. Fix deterministic eligibility/assembly
and measure a new reviewed set before considering adoption; no observed-cutoff tuning.

16 valid pinned native calls, no retries, freshUSD.000966504, cumulativeUSD.003283266
withinUSD1. Adapter median117ms/p95290ms; no full table/human-review latency claim.
Author-visible synthetic corpus is not production prevalence or blind holdout proof.
Provider-only temporary .env removed; local browser proof used no key.

[Owner decision](https://github.com/copperdogma/echo-forge/blob/main/docs/evals/attempts/scene-intent-trial/20260930-jev-proposal-trial.md),
[validation](https://github.com/copperdogma/echo-forge/blob/main/docs/evals/attempts/scene-intent-trial/validation.json)
and original/current summaries preserve evidence and remaining gaps. Other repo
candidates remain unapproved recommendations.

## Approved deterministic repair — 2026-09-30

Story078 repairs capability-specific anchors, favourite Source/Scene dispatch,
Scene-scoped target identities, additive environment behavior and missing-target
abstention in a new isolated `scene-proposal-repair-20260930` worktree.
19 provider-free development contracts pass (6/19 on preserved pre-code);54 affected
tests pass/reuse, type/build/affected lint and final local browser proof pass.
Independent/Codex findings were fixed and re-reviewed; source snapshots and all31
original trial artifact files stay byte-identical. No landing/deployment/defaults.

Retained native-output regression replay now improves local complete outcomes7→9/16
and useful positives3→4/7; Jev remains11/16,2/7,14/16review. This is code regression
evidence, not fresh model quality. **NO-GO normal/default Jev use remains; keep local
Search.** Zero additional provider calls/cost; prior cumulativeUSD.003283266.

[Repair decision](https://github.com/copperdogma/echo-forge/blob/main/docs/evals/attempts/scene-proposal-repair/20260930-deterministic-contracts.md)
and [validation](https://github.com/copperdogma/echo-forge/blob/main/docs/evals/attempts/scene-proposal-repair/validation.json).

## Landing record

Original task used provisional Scout080; current remote already assigns080 to the
thinking-level campaign, so this independent record is Scout081. Echo Forge076–078
land together with original frozen evidence and the provider-free historical harness.
Echo Forge remote main verified at
[`69dc6a8`](https://github.com/copperdogma/echo-forge/commit/69dc6a8c8c551e5d1dcbc4ccf3413cb99f792de7).
Stories076–078, the default-off prototype, local repair and original native evidence
are landed. [Landing validation](https://github.com/copperdogma/echo-forge/blob/69dc6a8c8c551e5d1dcbc4ccf3413cb99f792de7/docs/evals/attempts/scene-proposal-repair/landing-validation.json)
records40 mixed historical/current tests,8 server tests, frozen replay, archived
hash preservation and reused final54 affected tests. Full lint retains six
pre-existing errors in unrelated control-intent scripts; maintained new files pass.
Raw review transcripts retain their original whitespace. No deployment, default
enablement or additional provider spend. Dirty primary checkouts remain untouched.
