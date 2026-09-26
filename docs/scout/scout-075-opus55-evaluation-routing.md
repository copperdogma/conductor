# Scout 075 — Claude Opus 5.5 evaluation routing

Date: 2026-09-26
Status: Completed bounded campaign — no adoption; interrupted billing reservation retained

## Identity and route

Anthropic `claude-opus-5-5` is announced and API-listed, released September 22.
Proposed route: direct `POST https://api.anthropic.com/v1/messages`.
**Owner access: unverified.** No credentials or authenticated catalogs were used.
The evaluated-model ledger has Opus 5 and Fable 5.1 attempts, but no exact
Opus 5.5 attempt. This is a new checkpoint, not an unchanged retry.

Official specifications: text/image input, text output, 1M context, 128K maximum
output. Standard prices are USD4/20 per million input/output tokens; cache reads
USD0.20, five-minute writes USD5, one-hour writes USD8. No fast mode or batch
route is proposed. Adaptive thinking is always on; low/medium/high/xhigh/max
efforts are supported, medium is default. Forced any/named tool choice and
disabled/manual-budget thinking are rejected. Native JSON-schema output and
auto strict tools are documented; exact owner contracts remain unqualified.
Use explicit medium effort for Dossier/Doc Web/CineForge and low for
Storybook/Echo Forge. No effort sweep or silent parameter substitution.

Standard commercial API inputs/outputs may be retained up to 30 days, subject
to policy exceptions, and are not used for training by default. Messages is
eligible for ZDR arrangements; structured-output schemas can be cached up to
24 hours. Account ZDR is unverified. Current Covered Models documentation lists
Fable/Mythos, not Opus 5.5; do not import Fable's retention exception or claim
account-specific ZDR. Only owner-established public/synthetic fixtures below
are proposed, with stricter owner privacy policy controlling. No account changes.

Public sources checked today:
- [Model and pricing](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- [Breaking changes](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5)
- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort)
- [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- [Retention and ZDR](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)
- [Standard retention](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)
- [Training policy](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training)

## Stable execution handles

Two lower-cost agents inspected all seven registered owners read-only. The
coordinator reviewed their findings, current registry/adapter evidence and
Scouts 073/074. Caps include qualification, failed requests, thinking tokens,
fresh controls and any paid judges. No cap redistribution or automatic retries.
Reserve the complete worst-case call before dispatch; unknown billing retains
its reservation and stops progression. A cap is a maximum, not a promised cost
or promise to finish every downstream case.

1. **Dossier — Evaluate now; USD4.00.** First lane: Story170
   `standalone-semantic-value`, correction/withdrawal snapshots, against fresh
   `gpt-6-astra` medium. This tests whether the new checkpoint preserves source
   meaning as well as the strongest maintained reference with better task value.
   Native schema/compiler admission, then the two chronological correction
   snapshots; advance to the maintained ten-snapshot screen only after complete
   source-first acceptance. Stop on missing meaning, unsupported assertion,
   identity/contract failure, owner deadline or budget. Use reference histories
   for same-input comparisons, isolate oracles, retain all original schemas and
   local validation. Synthetic/public corpus only. No long-narrative or scale
   expansion. This is exposed-corpus evidence, not a general superiority claim.
2. **Doc Web — Evaluate now; USD2.00.** First lane `image-crop-extraction`:
   native image/integer-coordinate contract, Image011, then full13 and fresh
   Gemini 3 Flash control if admitted; require 13/13 and overall >=0.95.
   Independently qualify `crop-page-level-deletion-gate`: start with the
   `page-122-001` neighboring-portrait differentiator, then full22 against fresh
   GPT-5.5 Responses if admitted and budget permits; require 22/22 and stop on
   false-safe labels. Compare IoU, grouping, text exclusion, latency and total
   task cost. Owner-established public benchmark images only. Detector failure
   does not itself cancel the independent safety screen. Safety corpus is
   selection-exposed; passing cannot remove C5 or authorize promotion without
   separately frozen held-out truth.
3. **CineForge — Evaluate now; USD2.00.** First lane `video-understanding` v3,
   six repo-owned synthetic cases with five ordered JPEGs each, fresh Gemini
   3.5 Flash-Lite reference. Better sequence grounding could change the held
   video-model decision. Qualify exact five-image/schema contract; first case,
   then six only after admission. Maintained targets: overall >=0.80, <=15s and
   <=USD0.02 per subject call. Freeze judge and its pricing before dispatch;
   stop on contract or clear operational/value failure. This measures ordered
   frames, not native video/audio. Reference is not an adopted passing model.
4. **Storybook — Evaluate now; USD0.50.** First lane
   `story056-photo-understanding`, synthetic FS-001 photo then FS-006 scan,
   against fresh Gemini 2.5 Flash-Lite. Qualify actual JSON/local validation;
   require maintained assertions, <=5s and <=USD0.001 per turn before advancing.
   Keep grounding and OCR outcomes separate. The incumbent's two easy passing
   examples leave broader quality unknown; this is a small compatibility/value
   screen, not evidence of general equal ability. No private photos/transcripts.
5. **Echo Forge — Evaluate now; USD3.00.** First lane `control-intent-v1`,
   frozen48 synthetic cases versus fresh Gemini 3.8 Flash low. Hypothesis:
   improve the accuracy-oriented option, especially ambiguous intent; the recent
   Gemini control scored45/48 and abstained correctly on4/6 ambiguous cases.
   Actual contract is strict JSON, not forced tools. Preserve runtime policy,
   2048 total output budget and15s timeout; native admission, clear positive,
   negative and ambiguous cases, then full48 if valid. Stop on clear false
   activation, schema failure, timeout or budget. Compare exactness, control
   recall, false activation, abstention, p50/p95 and cost using deterministic
   scoring. Judge cost is zero. Historical Grok results are context, not a fresh
   superiority comparison. Code retains action/target/permission authority.

**Campaign maximum: USD11.50.** All five are new checkpoint evaluations.
Any native-to-owner adapter projection must retain prompt/schema meaning and
be explicitly recorded; adapter-required evidence is not drop-in parity.
Zero-cost resolved-matrix preflight precedes multi-case runs. Stop before a
call whose full reservation exceeds the remaining owner cap, even if estimated
typical usage is small. No model substitution or implicit retry.

## Owner evidence and omitted lanes

- Dossier: [Story170](</Users/cam/.codex/worktrees/dossier-semantic-benchmark-20260919/docs/stories/story-170-standalone-semantic-value-benchmark.md>),
  [benchmark protocol](</Users/cam/.codex/worktrees/dossier-semantic-benchmark-20260919/evals/semantic_benchmark/README.md>)
  and Anthropic adapter in that directory. Existing worktree contains maintained
  eval code not necessarily in the primary checkout. Stage2 must reconcile it
  into an isolated current-base owner workspace, preserving prior evidence.
  Exclude obsolete ordinary-extraction comparison, private narratives and
  larger scale tests outside this small semantic decision.
- Doc Web: [registry](</Users/cam/Documents/Projects/doc-web/docs/evals/registry.yaml>).
  Crop-only validation is omitted because selected page-context validation
  directly addresses the neighboring-content failure. Neither proves HTML/OCR
  pipeline quality; no matching maintained video/audio task exists.
- CineForge: [registry](</Users/cam/Documents/Projects/cine-forge/docs/evals/registry.yaml>)
  and [Scout073 offline adjudication](scout-073-grok47-evaluation-campaign.md#cineforge-offline-adjudication-complete).
  Defer ScriptBible until a prospectively frozen evidence/journey scoring
  contract resolves the ambiguity; private screenplay QA/second corpus remain
  ineligible. No audio-generation claim from image/text input support.
- Storybook: [registry](</Users/cam/Documents/Projects/Storybook/storybook/docs/evals/registry.yaml>)
  and Scout073 Attempt166 evidence. Defer Story060 downstream fusion policy
  and separate text-persona/linking/clustering lanes: this bounded visual screen
  qualifies the upstream photo contract first. No audio-generation lane fit.
- Echo Forge: [current implementation](</Users/cam/.codex/worktrees/echo-control-intent-runtime-20260920/server/control-intent.mjs>)
  and [fresh comparison](scout-073-grok47-evaluation-campaign.md).
  Defer full text-to-soundscape extraction: separate larger output contract and
  unresolved eligibility of some narrative fixtures; control intent is the
  active narrower decision. Text soundscape extraction is not audio generation.

## Not recommended now

- **Board Game Ingester — Defer.** Maintained crop, orientation, source-role,
  inventory and rulebook/OCR tasks match vision capabilities, but their sample
  scans/assets include private or licensed RoboRally material; upload eligibility
  is unestablished. Prepare an eligible corpus/owner policy first. Evidence:
  [registry](</Users/cam/Documents/Projects/boardgame-ingester/docs/evals/registry.yaml>),
  owner AGENTS and benchmark sample provenance. ZDR alone is not authorization.
- **Robo Rally — Do not evaluate.** Owner instructions prioritize deterministic
  game/rules behavior; no maintained model-owned inference benchmark was found.
  The canonical private rulebook is not an eligible substitute eval corpus.
  Evidence: [owner instructions](</Users/cam/Documents/Projects/roborally/AGENTS.md>).

All seven registered repos have one disposition. No target changes, credentials,
inference, defaults, commits or pushes occurred. No evaluated-ledger entry is
warranted until selected execution reaches an authenticated probe or owner stop.

Reply `yes` to run all numbered evaluations, or name a subset.
The evaluate-model skill requires selection before execution; its Stage1 rule
says: "Do not run a paid benchmark or mutate a target repo yet."

## Approved execution — 2026-09-26

Cam replied `Yes`, selecting handles1–5 exactly, with USD11.50 maximum:
Dossier4, DocWeb2, CineForge2, Storybook0.50, EchoForge3. The original proposal
above remains the pre-execution contract. Five separate Sol owner agents were
dispatched before any coordinator provider call. The coordinator makes no
duplicate inference requests and reviews owner evidence before synthesis.

Each owner creates its isolated current-origin-base workspace beneath
`/Users/cam/.codex/worktrees/opus55-eval-20260926/`, branch
`codex/opus55-eval-20260926`, preserving primary checkout work. Maintained
eval-only surfaces from prior worktrees are reconciled only where needed.
No runtime defaults, deployment, commits, pushes or merges are authorized.

Credential-custody protocol read completely. Presence-only central `status`
and `check` passed; the helper has no direct Anthropic mapping. Owners use
their own existing approved process environment or owner wrapper when present.
No whole environment file or credential is copied into Conductor, and no
OpenRouter substitution is authorized by this direct-route proposal. Any owner
without direct access records a zero-spend access stop. Cleanup applies only
to temporary injected keys, never owner-managed credentials.

Verified isolated base identities (all on the branch named above):

| Owner directory | Current origin base SHA | Owner cap USD |
| --- | --- | ---: |
| dossier | `f05b75821b8a4d0b7bb56593df88ef0d4e012222` | 4.00 |
| doc-web | `b75324c69a0fcf5578d5909f28c95a44dc0d3f5e` | 2.00 |
| cine-forge | `cb388508df4bac0e54f3b61ca24c432112e2dcc5` | 2.00 |
| storybook | `0bb4b3895acb71941da50efae365bebf59985e2b` | 0.50 |
| echo-forge | `d4211147ec775bf55ca893f0ebdceec915026d41` | 3.00 |

## Owner results — 2026-09-26

All paid execution is stopped. Exact direct `claude-opus-5-5` inference was
observed in every owner. No runtime replacement is justified by this campaign.
Availability, valid native output and task suitability remain separate claims.

| Owner | Evidence and result | Usage-priced USD | Unresolved reservation USD | Cap USD |
| --- | --- | ---: | ---: | ---: |
| Dossier | [Owner report and artifacts](</Users/cam/.codex/worktrees/opus55-eval-20260926/dossier/docs/evals/artifacts/opus55-semantic-20260926/README.md>). Opus and fresh Astra compile and preserve reviewed correction meanings in two snapshots; no completed independent full semantic review. Opus namesakes second graph references an undeclared local entity and fails compilation; broader superiority unmeasured. Orchestration deviation below. | 0.605892 | 0.755648 | 4.00 |
| Doc Web | [Attempt041](</Users/cam/.codex/worktrees/opus55-eval-20260926/doc-web/docs/evals/attempts/041-opus55-crop-and-page-context.md>). Native contracts/parity passed. Full13 detector:12 contract-valid cases, mean0.9177 on those valid rows; Image037 has integer coordinate1359 outside0–1000. Independent page122001 safety response falsely passes neighboring-portrait leakage. Both lanes stop; fresh controls/full22 unmeasured. | 0.352940 | 0 | 2.00 |
| CineForge | [Attempt040](</Users/cam/.codex/worktrees/opus55-eval-20260926/cine-forge/docs/evals/attempts/040-opus55-video-understanding-cost-stop.md>). Exact native five-frame/schema response completed11.688s, but USD0.034948 exceeds0.02. Stop before parity/judge/full6/control; semantic quality unmeasured. Post-save local metadata bug repaired offline; no repeated call. | 0.034948 | 0 | 2.00 |
| Storybook | [Attempt168](</Users/cam/.codex/worktrees/opus55-eval-20260926/storybook/docs/evals/attempts/168-story056-opus55-photo-understanding.md>). Native FS001 complete and local assertions pass diagnostically;8.205s/USD0.022780 exceed5s/0.001 gates. FS006, harness parity and fresh Gemini unmeasured. | 0.022780 | 0 | 0.50 |
| Echo Forge | [Manifest](</Users/cam/.codex/worktrees/opus55-eval-20260926/echo-forge/docs/evals/attempts/control-intent-v1/20260926-anthropic-claude-opus-5-5.manifest.json>).32candidate/31control terminal-valid calls. Candidate falsely marks adding room tone alongside vinyl as management of existing playback on control032; predeclared stop. Matched31: Opus29 exact versus fresh Gemini30. Full48 unmeasured; retain current choice. | 0.14026175 | 0 | 3.00 |

**Usage-priced total USD1.15682175; unresolved reservation USD0.755648;
conservative combined exposure USD1.91246975 of USD11.50.** These are token-usage
estimates and a worst-case reservation, not an invoice. Every owner remains
within its cap. No central key was injected, so no temporary-key cleanup was
needed; owner-managed credentials remain unchanged.

### Dossier stop-rule deviation and offline repair

The reference-history runner did not stop after `namesakes` second snapshot
failed canonical compilation. It completed three additional candidate requests
and dispatched one more before the coordinator detected the deviation and the
owner interrupted execution. This violated the selected progressive stop rule.
Those extra responses are retained as out-of-sequence diagnostics, not used to
claim a completed valid comparison. No further provider calls were made.

Independent read-only review verified the raw candidate declared `narrator2`
but used undeclared `narrator` as assertion endpoints. The unchanged owner
compiler correctly rejected this; it is a candidate graph-contract failure,
not a compiler defect or a scored source-meaning loss. The separate orchestration
defect was that reference-history mode only halted for billing/budget conditions.

Known Dossier costs: native0.041416, Opus correction0.095808, fresh Astra
correction0.172120, extension five completed0.296548 = USD0.605892. The sixth
extension request (`source-attribution` second) has a dispatch event and retained
request but no response/usage; its full USD0.755648 reservation remains unresolved.
Independent review verified these sums and the reservation directly.

Owner added an explicit prospective `stop_on_failure` option plus a focused
test proving reference-history failure prevents subsequent independent calls
while retaining failed-call cost. Future reproduction must enable it. Original
run configs and call-time code identities remain frozen; repaired code did not
produce earlier results. No automatic rerun is authorized.

### Evidence boundaries and validation

Root reviewed source/graph evidence for Dossier correction and namesakes,
Echo's false-activation fixture and raw response, Storybook's terminal receipt,
and owner transport/cost records. The Dossier review was independently repeated.
Doc Web's conditional detector average excludes its contract-invalid row; it
is not a13-case success average. No general model-quality or promotion claim
follows from these exposed, progressively stopped corpora.

Owner reports preserve exact commands, source hashes and raw custody pointers.
Focused validation is recorded there. Storybook's repository typecheck reports
eight existing errors in the untouched MiMo evaluator; scoped ESLint/privacy/
YAML/whitespace checks pass. No unrelated typecheck repair or product-wide test
run is justified by this eval-only change. Changes remain isolated/uncommitted.

Conductor validation: `make lint`, `git diff --check`, local Scout075 link
existence and decimal cost reconciliation passed. Dossier's32 focused runner
tests pass, including the new stop-regression test. No product-wide suites or
paid repeat were run by the coordinator.

Doc Web passed26 focused provider/fixture tests and methodology checks. Echo
verified its130-file raw manifest/ledger and passed8 focused harness/runtime
tests. CineForge passed47 focused provider/report tests; its broader owner unit
suite passed2182 with3 pre-existing failures (stale Grok-status expectation,
old registry hash and a provider size limit already exceeded at base). Together
with Storybook's existing typecheck failures, these are validation limitations,
not provider-quality evidence; they remain documented rather than repaired
outside scope. No claim of a clean full-suite landing is made.

Recommended next action: scoped review and check-in of the evaluation records
and validated tooling repairs, preserving the documented pre-existing check
failures and all negative/unknown evidence. This would require separate landing
authorization; no further paid evaluation is currently recommended.

## Approved closeout — 2026-09-26

Cam accepted scoped closeout with validation blockers resolved before pushing.
This authorizes the five owner evidence/tooling commits and the Conductor
record, not further inference, runtime model changes or deployment. All six
repositories are preflighted before the first push. Owners hold their prepared
commits until the coordinator releases landing; Conductor lands last.

Conductor uses a fresh `codex/opus55-closeout-20260926` worktree from
`47189f26be9d7784543207119a1a8f4992f28d3c`. Only this report, its scout index
entry, evaluated-model row and Opus inbox capture were transferred. Current
remote records of earlier campaigns remain intact; stale primary-checkout
versions and unrelated model-watch/credential edits were not copied. Reviewed
inbox capture added no other new unresolved note to the current remote record.

Preflight validation here: lint, methodology freshness, skill surface check,
report local links, cost arithmetic and whitespace checks passed. Owner fixes
are offline only; original call-time artifacts and unresolved billing exposure
remain preserved. Worktrees and protected/ignored raw artifacts are retained.
