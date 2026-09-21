# Scout 072 — JEV classification opportunities

Date: 2026-09-19
Status: Expanded comparison complete; Grok wins quality, Gemini recommended for interactive balance; historical absolute rejection interpretations superseded

## Selected execution — 2026-09-20

Cam provisioned `EVAL_TYPESAFE_API_KEY` and approved item 1. Storybook alone is
selected, with the previously disclosed US$1 total provider ceiling. The isolated
worktree is `/Users/cam/.codex/worktrees/jev-storybook-20260920`, branch
`codex/jev-story150-eval-20260920`, fetched base
`69940efd87b46c1a0e3031757af98a434c01f18a`. Other proposals remain unselected.

The TypeSafe skill is installed at `/Users/cam/.codex/skills/typesafe-ai/SKILL.md`.
Conductor's credential helper now recognizes `typesafe` / `EVAL_TYPESAFE_API_KEY`.
Vault checks passed; only `TYPESAFE_API_KEY` was temporarily injected into the
owner's ignored `.env.local`. The existing owner wrapper provides incumbent
Anthropic access. No values were printed. Headless wrapper commands require
`STORYBOOK_SKIP_LOCAL_DEV_PORTS=true`; `1` does not enable that switch.

The benchmark used eight independently authored fictional cases, with three
repetitions planned, and the maintained Story150 assessor. The native incumbent
arm retained its production prompt and parser, with a disclosed 2,048-token
output ceiling. A benchmark parser mismatch was repaired using the existing
production parser and the saved response; no paid response was repeated.

**Outcome: promising decision primitive, not a demonstrated interpreter replacement.**
Of 22 completed pairs, JEV produced 19 correct accepted decision projections and
three explicit low-confidence fallbacks (86.4% coverage of completed pairs;
82.6% across all 23 attempted matrix calls including the quarantine). Haiku passed
22/22. These are eight unique cases, not 22 independent examples; no broad
safety or quality claim follows. JEV projections omit the required generated
rationale and are not full interpreter-schema passes.

Paired request latency: JEV mean 171 ms / nearest-rank p95 298 ms; Haiku mean
2,430 ms / p95 3,146 ms. Paired JEV cost US$0.00368844 versus incumbent
US$0.082509. Keeping the incumbent for rationales and fallback gives an offline
paired-replay estimate of US$0.07912144, only **4.1% savings**, below the proposed
50% complete-workflow gate. This replay is not a measured live cascade.

The 23rd matrix JEV response returned HTTP 200, exact model identity and valid
usage, but one speculative Choice distribution summed to 0.99. The frozen
validator required a sum within 0.002 of one, so it quarantined the response and
stopped without retry. Rounded probabilities may explain the discrepancy:
this is an adapter/API compatibility stop, not evidence of a semantic error.
Two planned pairs remain incomplete. No scored unsafe actions were observed.

Total 48 calls (26 JEV including three probes, 22 incumbent): **US$0.08689611**
from returned usage and published prices, including the quarantined response,
against the US$1 cap. This is an estimate, not a provider invoice. All calls
stopped. The temporary `TYPESAFE_API_KEY` was removed and absence verified;
the central vault and owner incumbent credentials remain intact.

The owner worktree retains the runner, synthetic fixtures, raw responses,
source hashes, spend ledger and failure evidence under
`docs/evals/artifacts/story150-jev-20260920/`; see the
[owner report](/Users/cam/.codex/worktrees/jev-storybook-20260920/docs/evals/artifacts/story150-jev-20260920/report.md)
and [Attempt 158](/Users/cam/.codex/worktrees/jev-storybook-20260920/docs/evals/attempts/158-story150-jev-native-comparison.md).
No production behavior, database,
commits or pushes changed. Seven Conductor credential-helper tests pass.

Next: verify the probability-rounding contract and add an offline regression
before any further provider run. Do not repeat this small set to claim stronger
quality. A fresh held-out screen needs harder negatives and ambiguity cases.
For practical adoption, Echo Forge's cue classification remains the stronger
new-eval candidate because it does not inherently require generated rationales.

Cam requested current JEV research and inspection of ten suggested project uses.
Cam subsequently excluded Bishop (another machine), unified updater/maintenance,
and Labor/Zero from this pass. Those systems have no recommendation here.
The initial research stage made no provider calls or target-repo edits. The
selected execution above is separately authorized. No commits or pushes have
been made; unrelated existing changes remain preserved.

## Selected Echo Forge eval construction — 2026-09-20

Cam approved building the cue-classification eval and baseline fixtures after
the Storybook result. This is **offline construction only**, not approval for
provider calls or production playback. The owner worktree is
`/Users/cam/.codex/worktrees/jev-echo-forge-20260920`, branch
`codex/jev-cue-eval-20260920`, remote-main base
`f8bcfbbf69e87f65d04d063b9edf27d0ef5c9f80`. Its dirty primary checkout remains
untouched. Owner Story070 anchors the work under ADR-004/007 and explicit-input
spec constraints. No new model attempt belongs in the evaluated-model ledger
until there is a separately selected provider campaign.

The child eval separates multi-label cue judgments from the actual deterministic
matcher/PTT component baseline and the broader production extraction schema.
A fixed synthetic catalog is a controlled component test, not full App.tsx
scene-assembly/executor/UI behavior. Current extractor outputs do not directly
encode current one-shot versus merely potential action or stop/replace intent;
unsupported projections must abstain. No class label authorizes playback.

The completed fixture set has 38 original synthetic cases (22 development, 16
held-out), independent authored labels and rationales. The split is visible to
the authors/reviewer and does not establish statistical generalization. It covers
multi-label ambience/music/foley, control intent, cue presence, unsupported cues,
and explicit uncertainty; combat state and safe action selection remain out of
scope. Offline review corrected ambiguous labels before any model output.

The deterministic component simulation produced no high-confidence autoplay
across 38 cases; always mode would autoplay on 9 of 13 no-cue cases. This is not
a production bug finding or evidence of useful recall in high-confidence mode.
No audio was played. JEV and current-model quality remain unmeasured; provider
spend is US$0. A separate experimental `gpt-5.4-mini` classifier request receives
the identical state/question definitions and projects typed judgments into the
same scorer. It is explicitly a new benchmark prompt, not the production
extractor. The unchanged extractor request is separately retained as a broader
diagnostic. Nine focused tests cover request parity, equal-input reference,
uncertainty, strict provenance, scorer sanity and full-bundle CLI replay;
targeted lint and methodology checks pass (the owner retains its pre-existing
"No Ideal requirements parsed" warning). Request preparation, replay/scoring and baseline artifacts remain
in the isolated owner worktree, with no credential access or production changes.

Owner [protocol](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/cue-classification.md),
[offline observations](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/attempts/cue-classification-offline/20260920-offline.md),
and [Story070](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/stories/story-070-cue-classification-offline-eval.md)
retain the precise scope and next-run prerequisites.

## Selected Echo Forge live development screen — 2026-09-20

Cam approved the development-only JEV versus GPT-5.4 Mini classifier screen,
with a US$1 combined cap including all probes and calls. The existing isolated
Echo Forge worktree above owns execution. The 22 development cases are selected;
16 held-out cases and the broader production extractor are excluded. The GPT
arm uses the explicitly experimental same-input reference prompt, not a claim
of production-extractor equivalence. Prompts, fixtures, gold labels and the
exploratory Noul .2/.8 thresholds remain frozen during this run.

Stop on the first contract failure or false activation on a no-cue fixture;
otherwise measure per-label recall/F1, abstention, latency against the proposed
150 ms target, and total inference cost. No automatic retries, prompt tuning,
playback, default changes, commits or pushes. Stage native contract/parity checks
before the multi-case matrix and reserve conservative cost before each request.
Current official sources verify [JEV `jev-1.13.0`](https://docs.typesafe.ai/models)
at US$0.042/M input (free output) and
[GPT-5.4 Mini](https://developers.openai.com/api/docs/models/gpt-5.4-mini)
at US$0.75/M input, US$0.075/M cached input and US$4.50/M output,
with default reasoning none. Returned identity must be pinned JEV or the
reference alias/documented GPT snapshot `gpt-5.4-mini-2026-03-17`.

Conductor checked the central vault and temporarily injected only TypeSafe into
the owner's ignored `.env.local`; the reference uses its existing owner-managed
OpenAI credential. No secrets were printed or supplied in agent messages.
The run used the first positive (`cue-01`) and a no-cue control (`cue-13`) for
native qualification and exact prepared-payload parity, then continued once
through the development order. Qualification outputs count in the same sample;
they are not extra independent observations. The reviewed preflight bound all
44 possible requests at US$0.586245, including maximum output reservations.

**Result: stopped after eight matched cases / 16 valid requests**, with no
transport errors or retries. Both native contracts qualified. GPT returned
`control=yes` and `presence=yes` for `cue-07`, "Do not play music", despite an
empty active-layer context. The frozen gold treats this as no new cue/action,
so the declared false-activation gate stopped both arms. GPT did **not** predict
`music=yes`; this is a control-policy boundary disagreement, not evidence of
music playback or a production safety bug. No post-exposure relabel or rescore.

JEV answered 39 of 48 label judgments correctly and abstained on nine (81.25%
label coverage); all answered labels were correct. Exact case matches were
2/8 for JEV versus 7/8 for the GPT reference. JEV positive recall was 75% for
ambience, 100% for music and 60% for cue presence; it had no observed false
activations on three no-cue cases. GPT positive recall was 100% on reached
positive classes, with one policy mismatch on those three no-cue cases.
Positive foley/control/unsupported-cue behavior remains unmeasured. Macro F1
was 0.8690 versus 0.9697, but those values exclude classes with no positive
support and cannot override the safety/coverage limits.

JEV p50/p95 latency was **170/426 ms**, versus **967/2,350 ms** for GPT;
nearest-rank p95 over eight valid requests per arm includes qualification.
Both miss the proposed 150 ms target. Estimated usage-priced spend was
**US$0.005804382 / US$1** (JEV US$0.000284382; GPT US$0.00552), with no unsettled
requests. These are provider-usage estimates, not invoices. Fourteen development
cases and all sixteen held-out cases were not called.

**Decision: do not adopt this configuration.** JEV is fast relative to the
reference but its abstention/recall and absolute latency miss the exploratory
requirements. The reference also violates this benchmark's no-new-action rule.
Review the control-versus-new-cue policy and abstention needs offline before
another paid attempt; preserve this historical run and freeze a new contract
if that policy changes. Do not lower thresholds or relabel this case simply to
improve the observed score.

All provider calls stopped; Conductor removed the temporary `TYPESAFE_API_KEY`
and verified absence. Existing owner OpenAI credentials and the central vault
remain intact. Runtime, playback, commits, pushes and defaults are unchanged.
The owner retains safe request/response files, ledger and source hashes under
`.tmp/eval-artifacts/cue-live-20260920-1053/`, with a durable owner report and
manifest. See the [owner live report](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/attempts/cue-classification-offline/20260920-live-dev.md)
and [tracked manifest](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/attempts/cue-classification-offline/20260920-live-dev.manifest.json).
Fifteen focused tests and targeted lint passed before execution; offline replay
verifies the retained ledger, native responses, source snapshots and scores.

## Approved offline cue-policy revision — 2026-09-20

Cam approved a versioned offline revision separating playback-control intent
from newly requested sound. No provider calls or credentials are authorized in
this step. The original v1 code/fixtures and live evidence remain frozen; its
raw replay verified before revision with freeze SHA-256
`8340820d6f4e6b6f81537047c473db169dea6f3a2a0b5a3a26afcde6406b69ff`,
eight matched cases and historical cost US$0.005804382.

V2 treats an operative prohibition/stop/mute/keep/replace/volume directive as
control intent regardless of whether audio currently plays. New-sound presence
excludes control-only requests. Replacement can express both. Deterministic
playback code owns actual effects, missing targets and no-ops; no classifier
judgment executes anything. Quoted, hypothetical and table-discussion mentions
are not operative commands. Sound false-activation measures audible judgments
only; control errors remain separately scored. This is a new contract, not a
post-hoc repair of the old model scores.

The reviewed v2 corpus contains24 author-visible development cases,19 distinct
utterances and5 same-text active/empty-state pairs (prohibit, stop, keep,
replace, volume). Reused v1 wording is identified in fixture provenance. This
control-heavy policy regression set has only one positive music case; it is
not a broad quality/adoption suite or an independent held-out sample. Its
versioned scorer rejects v1/stale prediction bundles and measures control
errors separately from false sound activation. Model quality remains unmeasured;
this offline revision spends US$0.

Owner [v2 protocol](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/cue-classification-v2.md)
and [offline revision report](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/attempts/cue-classification-offline/20260920-v2-offline-policy.md)
record the new contract. Coordinator independently reviewed the fixtures,
scorer and version isolation, then verified that the full historical v1 raw
replay output was byte-identical before and after revision. Conductor lint and
scoped whitespace checks pass. A future v2 provider comparison requires its own
approved capture contract and budget; no old response is translated into v2.

## Selected v2 development comparison — 2026-09-20

Cam approved a fresh comparison of all24 v2 development cases under a combined
US$1 ceiling. The existing isolated Echo Forge worktree owns this new attempt.
JEV `jev-1.13.0` and the experimental same-input GPT-5.4 Mini reference use the
frozen v2 policy, fixtures and .2/.8 Noul thresholds. This tests clarified
control/new-sound semantics; it cannot establish production adoption or broad
held-out quality. V1 evidence and the offline v2 revision remain separate.

Current [TypeSafe API](https://docs.typesafe.ai/api),
[Noul](https://docs.typesafe.ai/primitives/noul),
[model/pricing](https://docs.typesafe.ai/models), and
[GPT reference](https://developers.openai.com/api/docs/models/gpt-5.4-mini)
documentation were rechecked on2026-09-20 and match the prior native routes and
prices. Synthetic inputs only; no account retention-setting changes. The run
uses fresh calls, single concurrency, no judges or retries,30-second request
timeouts, conservative spend reservations and persisted raw responses. Stop on
contract failure or false sound activation under v2; control errors remain
scored separately. No production actions, commits or pushes are authorized.

The independently reviewed preflight reserves at most US$0.64987575 for48
possible requests. Qualification uses v2-01 (prohibition with empty layers) and
v2-11 (new music); each counts once in the24-case sample. Remaining cases follow
fixture order. Returned GPT identity must be `gpt-5.4-mini-2026-03-17`; no model
fallback. Frozen fixture SHA-256 is
`70f526c50178e53a477bc9b7cc5ca655b3e98eb12bcf30222b55e76342cc86c9`.
Conductor temporarily injected only TypeSafe into ignored owner `.env.local`;
the GPT reference reuses its approved owner-managed key.

**Result: stopped at v2-05 after six matched cases /12 valid calls.** The GPT
reference returned music=yes, control=yes and sound_presence=no for “Keep the
music playing” with empty active layers. This contradicts the frozen exclusion
of maintenance-only music mentions and is internally inconsistent across its
sound labels. JEV returned music=no, control=yes, sound_presence=no. The declared
sound-activation gate stopped both arms after the pair; no audio was executed.
Both native contracts qualified, with no retries or transport errors.

JEV was6/6 exact (36/36 judgments), GPT5/6 (35/36), with no abstentions. False
sound activation was0/5 versus1/5 no-new-sound cases. These six cases contain
only four distinct utterances: five control-only contexts and one positive
music request. Positive ambience, foley, unsupported and ambiguity performance
remain unmeasured;18 cases were not called. This is narrow descriptive evidence,
not a general quality win or proof of improvement over the different v1 contract.

JEV p50/p95 was161/475ms; GPT965/2277ms. Both miss the proposed150ms p95 target.
Estimated spend was **US$0.004907424 / US$1** (JEV0.000242424, GPT0.004665), with
all12 calls reconciled and no unsettled charge. Adoption remains deferred for
JEV; this GPT classifier configuration fails its semantic gate. No production
extractor regression or runtime change is implied.

Coordinator independently replayed the complete v2 raw evidence successfully:
freeze SHA-256 `3ea6930367ed791dba81c1dcef962970737344d253d9ad033ac0e13dfb17e68e`.
Historical v1 replay still byte-matches its pre-v2 output. Temporary
`TYPESAFE_API_KEY` was removed and absence verified; owner-managed and central
credentials remain in place. No further calls are authorized by leftover budget.

Owner [v2 live report](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/attempts/cue-classification-offline/20260920-v2-live-dev.md)
and [verified manifest](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/attempts/cue-classification-offline/20260920-v2-live-dev.manifest.json)
retain the complete outcome. Thirteen focused owner tests, targeted lint and
methodology checks pass (existing Ideal parsing warning unchanged); Conductor
lint and scoped whitespace checks pass. The smallest useful further experiment
would be a separately approved diagnostic completion of the18 unrun pairs,
keeping v2 prompts/gold unchanged and logging semantic failures without stopping
the diagnostic sample. The present failure and no-adoption verdict must remain.

## Selected v2 diagnostic completion — 2026-09-20

Cam approved the18 previously unrun v2 pairs under a new combined US$1 cap.
This is a diagnostic continuation: semantic errors are recorded without early
termination, while invalid transport/identity/schema, request timeout and budget
limits still stop the run. Prompts, fixtures, gold, Noul thresholds and provider
configuration remain unchanged. The original six pairs are not called again;
their valid GPT failure and original stop remain part of the record. Existing
same-day native qualification is reused for this identical response contract.

The new attempt covers v2-06 through v2-10 and v2-12 through v2-24, with fresh
subject calls, no judges, no retries and no runtime changes. Any24-case result
must be identified as stitched across the initial screen and this diagnostic
completion;19 distinct utterances and author-visible development provenance
still limit its meaning. No production adoption is authorized.

Coordinator verified all36 prepared request bodies exactly match the original
v2 freeze, with unchanged fixture hash and18 unique remaining IDs. The maximum
conservative reservation is US$0.48750225. Prior qualified source hashes and
manifest identity are checked before execution; the new summary explicitly
distinguishes prior six cases from pending selected cases. Only temporary
TypeSafe access was injected; the existing approved owner OpenAI key is reused.

**Result: all18 remaining pairs completed,36 valid calls, no retries.** New
spend was US$0.014816976 (JEV0.000731976; GPT0.014085), with no unsettled usage.
Both arms were9/18 exact on this continuation; JEV had12 abstentions on decisive
labels. Sound false activation was0/10 no-new-sound cases for JEV and1/10 for
GPT. New-run p50/p95 was149/326ms versus976/1764ms. The preserved first-six
failure remains unchanged; no responses were repeated or rescored under new gold.

Stitched results across both v2 attempts cover24 cases /19 distinct utterances:

| Measure | JEV | Experimental GPT reference |
| --- | ---: | ---: |
| Exact cases |15/24|14/24|
| Correct decisive judgments |126/141|131/141|
| Abstentions on decisive judgments |12|0|
| Positive-support macro F1 |0.6389|0.7434|
| Sound false activation / no-new-sound cases |0/15|2/15|
| Sound-presence recall |4/8|8/8|
| Ambience recall |2/4|4/4|
| Foley recall (abstained positives count as misses) |0/2|2/2|
| Control TP / FP / FN |12/0/0|12/3/0|
| Pooled p50 / p95 response latency |150/326ms|976/1905ms|
| Estimated v2 usage cost |US$0.0009744|US$0.01875|

Combined v2 cost is **US$0.0197244**, across48 valid calls. Pooled timings are
descriptive across two runs, not an independent variance/tail-latency study.
JEV's two control-negative abstentions are not correct negatives; it correctly
abstained on the one ambiguous-control fixture. It failed to abstain on both
ambiguous-sound labels. GPT had no decisive abstentions but missed two of three
ambiguity judgments. Unsupported-sound recall was1/3 for both. GPT also emitted
three false foley labels and two music=yes/sound_presence=no contradictions.

**Decision: do not adopt either configuration as the full cue classifier.**
JEV's15/24 exact result does not outweigh lower F1 and missed audible cues.
Its narrower control-intent signal is worth further investigation, but current
fixtures are synthetic, author-visible, small and correlated. A next experiment
should first build representative independent control-intent fixtures and
deterministic/reference baselines offline, preserving quoted/hypothetical
negative cases and fallback errors. Do not tune thresholds on these observed
cases and call the result a fresh win. Both arms still miss the150ms p95 goal.

Coordinator independently verified diagnostic raw replay and recomputed the
stitched24 scores directly from the two disjoint sets of original responses.
Temporary `TYPESAFE_API_KEY` was removed after completion; no runtime/default,
commit, push or account changes were made.

Owner [diagnostic report](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/attempts/cue-classification-offline/20260920-v2-diagnostic.md),
[raw-evidence manifest](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/attempts/cue-classification-offline/20260920-v2-diagnostic.manifest.json)
and [stitched results](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/attempts/cue-classification-offline/20260920-v2-stitched.json)
retain the full per-case disagreements and provenance. Eight focused
diagnostic/stitch tests, targeted lint and methodology checks pass; the existing
Ideal parsing warning is unchanged. Both prior replay outputs remain
byte-identical. Conductor lint and scoped whitespace checks pass.

## Approved offline control-intent eval — 2026-09-20

Cam approved a new focused control-intent eval with fresh independently reviewed
cases and deterministic baselines, without provider spend. The prior v2 result
motivates investigating the narrower intent seam; it does not establish model
quality on fresh inputs or authorize runtime adoption. Existing v1/v2 source,
fixtures, raw outputs and scores remain frozen.

A separate fixture author, without access to prior model outputs or new baseline
implementations, drafts48 original synthetic cases split24 development /24
challenge. Coordinator reviews the labels against the explicit operative-control
policy before scoring. The owning worker freezes two new reference baselines
(always-no and fixed lexical management-trigger rules) before seeing the new
cases. They are not presented as existing production classifiers. Cases remain
author/reviewer-visible synthetic examples, not real traffic or blind statistical
holdout evidence. Family-disjoint splits and explicit ambiguity are required.

All48 labels were independently reviewed before baseline scoring. Review
corrected confusing denials/prohibitions, distinguished uncertain management
actions from uncertain management intent, and replaced gold-revealing context
with observable dialogue. The final corpus has20 yes,22 no and6 ambiguous cases,
evenly split across development/challenge, with no exact normalized utterance
overlap against either previous cue corpus. Scenario families are disjoint across
splits; broad linguistic structures intentionally recur, so structural
out-of-distribution generalization is not claimed.

The lexical baseline was frozen before fixture exposure with source SHA-256
`b826aba5483284542dbed702d2809167972d0a3485e8efae59daa3df1be35477`.
It matches five simple management-token/keep/volume/turn/prohibition rule groups
and deliberately ignores dialogue, quotation, condition and speaker scope.
Echo Forge's existing `classifySearchIntent` branch in
`src/soundscape/sceneAssembly.ts` depends on eligible matcher candidates and
returns a broader action category; downstream muting requires a source ID.
It is not scored as an equivalent text-only control classifier.

The integrated fixture hash is
`6a508ed0697bf1f5270cf2804ceae0211928cd2a29bafc40adc39deaca7c8df2`.

Offline results, independently reproduced by the coordinator:

| Baseline | Exact cases | True positives | False positives | Control recall |
| --- | ---: | ---: | ---: | ---: |
| Always no |22/48|0/20|0/22|0%|
| Frozen lexical rules |20/48|1/20|3/22|5%|

Lexical precision is25% and F1 is0.0833. Development was9/24 exact and challenge
11/24; neither baseline abstains, so all six ambiguous cases fail. Two of five
quoted negative cases and one of two discussion negatives trigger lexical false
positives. This purpose-built corpus contains many indirect/paraphrased commands;
the lexical reference is a weak floor, not evidence that deterministic solutions
cannot work or that AI is required. No baseline rules were adjusted after scoring.
Model quality on this new eval remains **unmeasured**. Provider spend is US$0.

Owner [protocol](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/control-intent-v1.md),
[offline report](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/attempts/control-intent-v1/20260920-offline.md)
and [baseline observations](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/attempts/control-intent-v1/20260920-offline-baselines.json)
provide runnable check/baseline/score commands and strict versioned prediction
bundles. Eight focused tests, targeted lint, methodology and whitespace checks
pass; prior v1/v2 evidence remains unchanged. No product suite or provider calls
were needed. Coordinator independently reviewed fixtures and scorer semantics
and reproduced the baseline metrics. Conductor lint and scoped whitespace pass.

## Selected control-intent live comparison — 2026-09-20

Cam approved comparing JEV and GPT on all48 frozen control-intent-v1 cases under
a combined US$1 cap, without fixture, scorer or baseline tuning. The existing
isolated Echo Forge worktree owns the run. A separate single-label native
adapter is required; previous six-label qualification is not assumed sufficient.
The intended subjects remain `jev-1.13.0` and the experimental GPT-5.4 Mini
reference, with returned GPT snapshot `gpt-5.4-mini-2026-03-17` required.

Same-day [TypeSafe contract](https://docs.typesafe.ai/api),
[Noul guidance](https://docs.typesafe.ai/primitives/noul),
[TypeSafe price/model](https://docs.typesafe.ai/models) and
[GPT reference documentation](https://developers.openai.com/api/docs/models/gpt-5.4-mini)
were refreshed and remain consistent with the earlier native routes and prices.
Synthetic inputs only; no account-setting changes. Existing authorized owner
OpenAI access is reused, and only temporary TypeSafe access is injected via the
Conductor helper into ignored owner `.env.local`.

Freeze one control judgment per model with JEV .2/.8 exploratory thresholds,
strict GPT yes/no/abstain output, no judges or retries, single concurrency and
30-second request timeout. Qualify representative positive/negative cases once
within the48, then continue recording semantic errors. Invalid transport,
identity/schema, timeout or budget stops remain mandatory. Screening targets
declared before calls are zero false positives on22 clear negatives, at least90%
recall on20 clear positives, correct abstention on6 ambiguous cases and p95 at
most150ms. These are exploratory targets; even passing cannot establish
production readiness on this author-visible synthetic corpus.

Coordinator reviewed the new runner and five mocked native/replay tests, then
independently verified the resolved48-case/96-request matrix. Every arm gets
the same state, question instructions and criteria, without gold labels or
rationales. Question scope explicitly targets current `state.text`; prior turns
are context only. Qualification uses control-001 and control-016 once each.
The GPT reference uses strict `{control: yes|no|abstain}`, `store:false`, default
none reasoning and1000 maximum output tokens. Conservative full-run reservation
is US$0.56437275, including both models and qualification. The fixture hash stays
`6a508ed0697bf1f5270cf2804ceae0211928cd2a29bafc40adc39deaca7c8df2`.

**Result: all48 pairs /96 valid native calls completed, with no retries or
transport errors.** Both single-label contracts qualified. Estimated usage spend
was **US$0.016273332 / US$1**, fully reconciled (JEV0.001107582;
GPT0.01516575). No fixture, prompt, threshold or scorer changes followed calls.

| Control-intent measure | JEV | Experimental GPT reference |
| --- | ---: | ---: |
| Exact cases, including correct ambiguous abstention |31/48|36/48|
| TP / TN / FP / FN |15/12/1/0|19/17/5/1|
| Abstentions on clear positive / negative cases |5/9|0/0|
| Precision / recall / F1 |93.75% /75% /0.8333|79.17% /95% /0.8636|
| Correct abstention on ambiguous cases |4/6|0/6|
| Decisive coverage |66.67%|100%|
| Development / challenge exact cases |15/24 /16/24|17/24 /19/24|
| Response p50 / p95 |159/296ms|694/1684ms|

Both falsely classified control-015, a corrected choice between two new sounds
with no existing playback, as management. GPT also falsely classified an
unfulfilled future command, a historical reported request, quoted roleplay and
another corrected start-only request. JEV abstained on14 clear cases rather than
answering them correctly; its zero negative answers on clear commands must not
be mistaken for100% recall. Both exceed the proposed150ms p95 goal. JEV misses
all four screening targets; GPT passes recall but fails false-positive,
ambiguity and latency targets. These are small synthetic-corpus observations,
not production rates or proof of general superiority over deterministic code.

**Decision: do not adopt either configuration for playback control.** Both
improve over the deliberately weak lexical reference, which is insufficient to
justify adoption. No further automatic paid Echo Forge run is recommended:
representative usage cases and a stronger separately designed context-aware
deterministic baseline are the next evidence prerequisites. Preserve all model
errors and do not tune on the now-observed challenge cases to claim fresh success.

An offline, post-hoc projection of the originally suggested abstain-to-GPT
cascade selects GPT on18/48 cases:37/48 exact,19/20 command recall,4/22 false
positives and0/6 correct ambiguous abstentions. It loses JEV's correct ambiguity
handling and does not solve false control triggers. This uses captured outputs
only, not measured cascade execution/latency, a new paid run or an adoption test.

Coordinator independently verified native raw replay (freeze SHA-256
`6230d1b46a6d4dfe0e8b7c2cd549e5dbc65f15fe5b71a7c7c7be9132d1efa9af`)
and reviewed every disagreement. Temporary `TYPESAFE_API_KEY` was removed after
the final call; owner-managed and central keys are preserved. Runtime defaults,
playback, commits, pushes and account settings are unchanged.

Owner [control-intent live report](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/attempts/control-intent-v1/20260920-live.md)
and [verified manifest](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/attempts/control-intent-v1/20260920-live.manifest.json)
retain complete split/tag/case results and raw provenance. Five new native-runner
tests plus eight scorer tests pass, along with targeted lint, methodology and
whitespace checks. All three historical live manifests remain byte-identical
under offline replay; frozen offline control provenance hashes also remain
unchanged. Conductor lint and scoped whitespace checks pass.
## Expanded relative comparison — 2026-09-20

Cam explicitly requested re-evaluating previously promising models on the new
48-case control-intent set. This supersedes the earlier blanket rejection
interpretation: exploratory latency and perfection targets are not validated
product requirements. A model can win through a useful improvement over the
current comparator, and different models may suit different decisions. The
new GPT classifier is an experimental comparator, not the production pipeline;
the lexical and always-no baselines are only simple reference floors.

Selected prior candidates: `gpt-6-astra`, `gemini-3.8-flash`, `grok-4.6`, and
`gpt-5.6-terra`, alongside fresh `jev-1.13.0` and GPT-5.4 Mini anchors. Selection
uses positive semantic evidence in the evaluated-model ledger: Astra's Dossier
and Doc Web results, Gemini's Echo Tavern and Doc Web results, Grok's prior Echo
lead, and Terra's Doc Web detector results. Earlier long-output timing failures
are not exclusion criteria for this compact task. This is a bounded shortlist,
not an assertion that omitted models cannot win.

Execution remains in the existing isolated Echo owner worktree, with unchanged
fixtures, policy, prompts and scorer. Total new provider-spend ceiling: US$5.
Rank quality, false activations, missed controls, ambiguity handling, latency
and cost separately. Model combinations derived from saved outputs must be
labeled offline exploratory projections, not measured live cascades or fresh
holdout validation. No production, commit or push authorization is implied.

### Completed six-model comparison

All six models completed all48 cases:288 unique model-case calls, US$0.437034082
estimated total against the US$5 cap. No model was rejected for an aspirational
latency or perfection threshold. Frozen question, policy, labels and scorer were
unchanged. Results below are for this control-intent task, not the broad soundscape
extractor or every project.

| Model/configuration | Exact /48 | Controls caught /20 | False activations /22 | Ambiguous abstained /6 | Median / p95 ms | Cost /48 USD |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Grok 4.6 low | 46 | 20 | 0 | 4 | 3895 / 7393 | 0.133624 |
| Gemini 3.8 Flash low | 44 | 20 | 1 | 3 | 1295 / 2597 | 0.037939 |
| GPT-5.6 Terra none | 42 | 20 | 2 | 2 | 943 / 2278 | 0.040418 |
| GPT-6 Astra low | 42 | 20 | 3 | 3 | 1717 / 3607 | 0.208780 |
| GPT-5.4 Mini default none | 36 | 19 | 5 | 0 | 718 / 1707 | 0.015166 |
| JEV 1.13.0 fixed .2/.8 thresholds | 30 | 15 | 1 | 4 | 219 / 323 | 0.001108 |

**Recommendation:** Grok is the quality winner: every clear positive and negative
was correct, with two ambiguous cases decided instead of abstained. Gemini is the
recommended interactive balance: all20 controls caught, one false activation,
about one-third Grok's median latency and28% of its cost. Keep Grok as an optional
accuracy-focused mode. Terra is a faster alternative with two fewer exact cases;
Astra does not earn its additional cost on this task. Mini and JEV are cheaper,
but neither is the preferred stand-alone classifier given these relative errors.
Gemini scores22/24 in both development and challenge; these are synthetic,
author-visible cases, not a real-traffic error-rate estimate.

Predeclared combinations were projected offline from retained outputs:

- JEV abstention → Gemini:42/48,20 controls caught, two false activations,
  US$0.018005/48, projected median284ms. Nineteen fallback calls. Cheaper and
  usually faster, but decisive JEV mistakes make it less accurate than Gemini.
- Gemini + Terra agreement, otherwise abstain:45/48,20 controls caught, one
  false activation,5/6 ambiguous abstentions and one clear-negative abstention.
  US$0.078357/48, projected parallel median1360ms. A useful optional cautious
  mode, not the simplest default.
- Gemini + Grok agreement, otherwise abstain:46/48,20 controls caught, zero
  false activations,5/6 ambiguous abstentions and one clear-negative abstention.
  US$0.171563/48. Same exact score as Grok alone with a different abstention
  tradeoff; no compelling reason to pay for both by default.

These are rule-level projections, not measured live routing or parallel latency;
selection among these combinations on this corpus is exploratory. None removes
all mistakes. Execution and target resolution remain deterministic owner code.

Grok's first successful response exposed an adapter accounting assumption:
its completion tokens exclude separately reported reasoning tokens. A separate,
source-backed repair recovered that saved answer and ran the other47 cases,
without repeating a request or mutating the first frozen run. Token cost matches
xAI's returned billed-cost ticks. The original conservative ledger retains that
first-call reservation, so its liability isUS$0.459440082; the reconciled measured
estimate isUS$0.437034082. All calls are finished; the temporary TypeSafe variable
was removed and absence independently verified. Other owner credentials and
production behavior are unchanged. No commits or pushes.

Root independently replayed both raw runs and recomputed combined results.
See the [owner report](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/attempts/control-intent-v1/20260920-broad.md)
and [combined results](/Users/cam/.codex/worktrees/jev-echo-forge-20260920/docs/evals/attempts/control-intent-v1/20260920-broad-comparison.json).

## Approved Echo Forge runtime integration — 2026-09-20

Cam approved implementing the recommended Gemini control-intent path with Grok
as the accuracy-focused option. This authorizes the runtime patch, rather than
another paid comparison. Implementation belongs to
[Echo Forge Story071](/Users/cam/.codex/worktrees/echo-control-intent-runtime-20260920/docs/stories/story-071-control-intent-runtime.md)
on isolated branch `codex/control-intent-runtime-20260920`, based on current
owner HEAD `cc3c77798ba3da217f46459b39a9338f8651a288`. The primary checkout's
unrelated changes and the older frozen eval worktree are preserved.

The actual seam is explicit push-to-talk submission, including its typed-text
fallback. The app currently uses local matching, so this is a new binary routing
step, not a replacement of a production generative classifier. Gemini is the
default selection; Grok is selectable. Keys stay in the existing server process.
Model output supplies intent only: current-source target/action resolution and
confirmation stay deterministic. Uncertain/unavailable results require manual
review; unsupported control actions point to the existing source controls.
Ordinary typed search remains local. No provider calls, commit, push or deployment
are part of implementation verification. Runtime context contains the submitted
text and active-source labels, which is narrower than some contextual eval cases;
the benchmark scores are not asserted as live-session accuracy.

The runtime patch now supplies the native Gemini/Grok adapter, both HTTP service
routes, persisted model selection, and guarded PTT submission. Independent
browser checks with intercepted synthetic responses verified control-result
filtering, abstention and provider-failure manual review with Always selected,
cancellation, and selection persistence across reload. The final selector and
review copy were visually checked. A transient Vite hot-reload dependency-array
warning occurred while the source was being edited; the page was reloaded after
the change. Browser interception and the temporary dev server were removed.
Owner implementation verification is complete: 134 App tests, 348 non-App tests
and five Node server checks passed, alongside typecheck, lint and production
build. The initial full command exposed a Node-test/Vitest discovery collision;
renaming the Node checks and wiring their runner into `npm test` fixed it. Final
evidence combines unchanged passing App shards with the corrected non-App and
Node runs; the initial command itself did not exit successfully. The build emits
the existing large-chunk advisory. Setup is documented in the owner worktree's
`docs/control-intent-runtime.md`. Story071 remains In Progress, build-complete
and ready for formal owner validation. No commit, push or deployment occurred.

## Echo runtime landed — 2026-09-21

Cam approved final review and landing. Echo Forge Story071 is Done and remote
`main` plus the execution branch both verify at
`518046ebe96a8b1615815f77cb2d45e58e8dc964`. The final review found and fixed an
autoplay-preference race: the handler now cancels pending classification
synchronously. Its independent regression and the 30-test PTT/hold-to-talk group
pass. Typecheck, lint, build, packaging preflight and methodology checks pass;
unchanged broader evidence is reused as recorded in Story071. Integration with
remote `f8bcfbb` changed only changelog/generated-document conflicts, with no
runtime integration changes. Primary checkout and frozen eval artifacts remain
untouched. Worktree retained; no deployment occurred.

## Relative Storybook reassessment — 2026-09-21

Cam approved final review and landing of the Echo runtime patch, then requested
an audit and rerun of other JEV evaluations affected by arbitrary absolute gates.
Storybook is the only other owner with completed JEV calls. Dossier, Doc Web,
Scrypted, Conductor and Robo Rally were deferred before provider comparison;
Bishop, updater/maintenance and Labor/Zero remain excluded.

Storybook's 50% savings and 500 ms targets were experiment aspirations, not
relative incumbent requirements. Haiku passed every completed pair, so its
quality evidence remains valid. JEV's uniform confidence floor and validation
of an unused speculative field caused avoidable fallback/termination. The
original responses and verdict remain historical; a separate branch-aware replay
and fresh paired synthetic comparison are authorized up to US$1 total. Report
accepted coverage, decision errors, full-interpreter contract, cost and latency
separately. No automatic runtime adoption or landing of the new eval is implied.
The official Choice documentation permits ignoring unused speculative answers;
it still states probability distributions sum to one. This is not authorization
to normalize malformed consumed answers silently:
https://docs.typesafe.ai/primitives/choice (checked 2026-09-21).

## Completed relative Storybook rerun — 2026-09-21

Fresh isolated owner worktree: `/Users/cam/.codex/worktrees/jev-relative-20260921`,
branch `codex/jev-relative-20260921`, base
`69940efd87b46c1a0e3031757af98a434c01f18a`. Twelve independently reviewed synthetic
cases were run twice: four fictionalized control-case mirrors and eight fresh
challenge cases, not 24 independent scenarios. Model requests and source hashes
were frozen before calls. Three native probes plus 72 matrix calls completed;
all 75 settled at **US$0.119062142 / US$1**. No cache, retries or runtime changes.
The temporary `TYPESAFE_API_KEY` was removed and absence verified by the coordinator.

| Measured arm | Quality on 24 attempts | Cost for matrix | Median / p95 ms |
| --- | --- | --- | --- |
| JEV narrow routing | 24/24 mode + old target; 20/24 accepted projections | $0.003484908 | 177.5 / 312.7 |
| Haiku narrow routing | 24/24 mode + old target | $0.033080 | 817.5 / 2460.6 |
| Haiku full interpreter | 22/24 full-task passes | $0.082011 | 2309.6 / 3164.7 |
| Measured serial JEV → full Haiku | 22/24 full-task passes | $0.065085908 | 2420.8 / 3305.6 |

The routing metric does not claim complete replacement-argument or generated
rationale parity. JEV accepted 20/24 projections; four fallbacks were two repeats
each of low-confidence reverse-relationship replacement and explicit date-value
extraction. Full Haiku returned a safe no-op instead of asking clarification on
both absent-target repetitions. The serial cascade inherited that miss. No
scored unsafe auto-apply occurred. Error adjudication preserves the pre-reviewed
gold and raw responses.

**Revised recommendation: pursue JEV as a bounded Storybook routing front end.**
It matched narrow Haiku routing on this small screen at 89.5% lower cost and
4.6× faster median latency. Keeping Haiku for corrections and rationales saved
20.6% of full-workflow cost, while median latency rose 4.8%. These are useful
relative tradeoffs; neither a 50% saving nor perfection is required to win.
The measured workflow is a no-op shortcut with the full incumbent for other
branches, not a rationale-only generator or a new mutation authority. The small
synthetic sample and repeat dependence limit generalization. The subsequent approved implementation is recorded below. The owner evaluation
was committed as `4cbe5ca` during approved close-out, preserving raw evidence.

Owner [report](https://github.com/copperdogma/storybook/blob/4cbe5ca/docs/evals/artifacts/story150-jev-relative-20260921/report.md)
and [Attempt159](https://github.com/copperdogma/storybook/blob/4cbe5ca/docs/evals/attempts/159-story150-jev-relative-comparison.md)
retain reproduction sources and raw evidence. Nine focused tests, scoped lint,
source/artifact integrity, methodology and whitespace checks pass. The coordinator
independently verified all 75 ledger entries settled/qualified and every frozen
source hash unchanged. No product/parent suite or runtime adoption is claimed.
The zero-cost posthoc branch-aware replay of old responses is separately stored
at `docs/evals/artifacts/story150-jev-audit-20260921/` in the old frozen eval
worktree: 23/23 projected decisions, 22 paired incumbent results, one unpaired.
That diagnostic is not combined with the fresh results as extra samples.

## Approved Storybook routing implementation — 2026-09-21

Cam approved the bounded integration after the relative comparison. The owner
implemented Story167 in isolated worktree
`/Users/cam/.codex/worktrees/jev-routing-integration-20260921`, branch
`codex/jev-routing-integration-20260921`, refreshed remote base
`69940efd87b46c1a0e3031757af98a434c01f18a`. Both prior evaluation worktrees and
the primary checkout remain preserved. Initial approval covered implementation;
Cam subsequently approved final review and landing. No deployment or new paid
evaluation is included.

The reviewed plan wraps only the freeform relationship correction caller. Other
Knowledge correction factories keep the general Haiku interpreter. A production
module uses the evaluated mode judgment, omitting independent unused questions:
confident no-op can shortcut; explicit confirmation returns a canonical
non-mutating confirmation with a factual routing explanation; corrections,
unknowns and provider failures go to Haiku. General names, aliases and facts
remain outside this router. New runtime module/prompt tests must preserve the
mode contract, existing confirmation/executor/raw-save behavior and separately
track JEV and Haiku usage, including returned usage before fallback failure.
Unknown transport cost must not be represented as known-zero billing.

Activation uses explicit server-side configuration and an owner-managed key;
the existing evaluation-only key is not copied into runtime. The owner provider
manifest and setup docs must describe the payload, provider posture and controls.
Implementation verification used synthetic mocked responses, with no private
provider dispatch. The build is complete in
[Story167](https://github.com/copperdogma/storybook/blob/67e8e44/docs/stories/story-167-jev-relationship-routing.md),
which has completed formal validation and is marked Done. Independent code review is
clean. The coordinator compared the production mode question against the frozen
paid request and found an exact match; state is minimized to referenced fields,
so this is contract/source parity evidence, not a fresh accuracy measurement.

Validation: 171 distinct affected backend tests and 12 env/privacy tests passed,
along with workspace typecheck/lint, backend and direct frontend builds,
methodology and whitespace checks. Three real-consumer cases used a task-owned
synthetic PostgreSQL database and mocked providers to verify terminal no-op,
low-confidence clarification/queue creation without graph mutation, and separate
JEV/Haiku cost rows. Backend startup plus health/database connectivity passed.
The root Turbo build lost the local port-skip variable; the direct frontend
build passed with it explicitly supplied. Existing large-chunk and global
provider-review-date warnings remain; the new TypeSafe coverage is current.

The temporary server and exact task-owned test database were removed. No runtime
key or activation flag was set, and no `.env` was created. Setup is documented in
[tech-stack.md](https://github.com/copperdogma/storybook/blob/67e8e44/docs/tech-stack.md#optional-jev-relationship-routing-story-167).
No new provider spend, commit, push or deployment occurred in this build. The
build was subsequently approved for final review and landing; runtime activation
remains separate server configuration.

## Storybook landing — 2026-09-21

Approved final review and landing completed. Story167 is Done. Runtime commit
`a3fe7cd` and relative evaluation commit `4cbe5ca` retain their ancestry in
`67e8e44ba7f6643daf568642477f34b143dbe740`, verified on Storybook remote `main`
and the execution branch. The evaluation branch was also pushed. Review found
no remaining blockers; all six frozen source hashes and the artifact inventory
match. Nine eval tests and 27 router/scorer tests passed after integration;
unchanged implementation evidence above was reused. Combined methodology,
provider coverage and whitespace checks passed.

No runtime activation, deployment or additional provider spend. Primary
checkouts and older frozen evaluation worktrees remain untouched; task
worktrees are retained. Activation is the next separate operator decision.

## Finding

Pursue Storybook's bounded correction interpreter first. Echo Forge is the most
interesting new classifier eval. Dossier and Doc Web need new, explicitly scoped
evals; neither should receive a blanket replacement-model comparison. Scrypted
may benefit from interpreting ambiguous logs, but its existing probe precedence
belongs in code. Conductor and Robo Rally are lower-priority experiments.

The practical payoff is fewer expensive semantic decisions and less manual
review, if the complete classifier-plus-fallback workflow preserves quality.
The model's token price alone does not establish that payoff.

## Verified model evidence

- TypeSafe's [model page](https://docs.typesafe.ai/models) lists `jev-1.13.0`,
  with moving `jev-latest`/`jev-preview` aliases. Pin the version. Text-only input;
  US$0.042 per million input tokens; output tokens free. Total request limit 64k,
  with state plus longest question limited to 32k. Documented limits are dynamic.
- Native [API](https://docs.typesafe.ai/api): `POST https://api.typesafe.ai/v1/systemone`.
  Choice returns an option/distribution; Score returns a rubric score; Noul a
  yes-probability. These are typed decisions, not generated text or tool calls.
  Choice allows up to 255 options. No reasoning-effort control is documented.
- [Primitives](https://docs.typesafe.ai/primitives) evaluate questions independently
  against shared state. Useful for several atomic decisions, but dependent
  answers must be composed and validated by code.
- [Confidence](https://docs.typesafe.ai/confidence) is derived from the answer
  distribution; it is not a measured probability of correctness on our tasks.
  Calibrate thresholds locally, separately for each primitive and decision.
- [Known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13): numeric/date
  reasoning, indirection, irrelevant long context, adversarial state, and
  cross-question consistency. These directly affect tactical play, identity
  reasoning, release-note interpretation, and evidence triage.
- [Parallel's own experiment](https://parallel.ai/blog/testing-jev) found useful
  zero-shot reranking but its specialized models won topic/freshness classification.
  This is external task evidence, not a result on Cam's projects.
- [Privacy policy](https://typesafe.ai/legal/privacy-policy) commits against training
  on inputs but does not provide a fixed general retention period.
  [Enterprise ZDR](https://docs.typesafe.ai/legal) is separately offered. Start
  with explicitly synthetic/public inputs; private histories, recordings, and
  operational logs need owner-approved handling.

Announced/API-documented: yes. Account callability was unverified at research
time. On 2026-09-20, three native probes returned HTTP 200, the exact
`jev-1.13.0` identity, and valid Choice/usage envelopes. The credential helper
now supports TypeSafe. These transport checks alone do not establish quality.

Illustrative JEV-only cost: 1,000 requests of 2,000 input tokens cost US$0.084
at the published rate. This excludes extraction, transcription, retries,
incumbent comparisons, review, and fallback calls.

## Architecture and measurement

Use reliable code to handle exact rules and assemble evidence/candidates. Ask
JEV an atomic semantic question. A defined unknown choice, low-confidence result,
missing candidate, invalid response, timeout, or inconsistent combination should
take an explicit fallback path. Keep `no cue`, `no match`, and `unknown` distinct:
one is a negative decision, another a candidate-set outcome, another abstention.

UNKNOWN is an application contract, not a guarantee that JEV recognizes every
mistake. A confident false rejection bypasses fallback. For retrieval/filtering,
measure candidate recall before judging retained candidates; a missing answer
cannot be recovered by choosing better among the wrong shortlist.

Compare current deterministic behavior, the current AI where one exists, and
JEV plus its real fallback on the same frozen inputs. Preserve the original
full-task gates even when a projected label scorer measures the new subtask.
Use independently reviewed labels, a development split for thresholds, and a
held-out split grouped by source/document/session. Include negation, quotations,
contradiction, no-answer, prompt injection, truncated input, and rare classes.

Report per-class precision/recall, false actions, coverage versus error rate,
fallback frequency, p50/p95 latency, reliability, and complete workflow cost.
Do not count abstention as correctness or report accuracy only on easy answered
cases. A hundred clean examples cannot establish a sub-one-percent failure rate.
Use repeated calls for variance, not as independent new cases.

## Numbered comparison proposal — Evaluate now

### 1. Storybook — relationship-correction intent

Owner: `/Users/cam/Documents/Projects/Storybook/storybook`.
Maintained lane: `story150-relationship-correction-intent`.
Incumbent: `claude-haiku-4-5-20251001` in the current interpreter.

- [Interpreter](/Users/cam/Documents/Projects/Storybook/storybook/packages/backend/src/ai/knowledge-correction-interpreter.ts)
  accepts correction text plus bounded relationship candidates. JEV can select
  a supplied target and `remove/replace/confirm/noop`; code constructs the typed
  operation from supplied identities and permitted replacement fields.
- [Registry](/Users/cam/Documents/Projects/Storybook/storybook/docs/evals/registry.yaml:2188)
  has exact target/backing-set/action/ambiguity gates. The runner has eight cases,
  repeated three times: the recorded 24/24 result is eight unique cases, not 24.
- First build a benchmark-only native JEV adapter, leaving production unchanged.
  Do not manufacture free-text evidence/rationale or silently weaken the full
  interpreter contract. Any field needing open generation remains incumbent-owned
  and its cost is included. This is an adapter/cascade experiment, not a model-ID swap.
- Resolve fixture provenance before dispatch. Use owner-confirmed synthetic/public
  cases; otherwise author/review synthetic equivalents first. Never send live
  family records. Keep the same inputs for incumbent and challenger.
- Progressive gate: native contract/abstention smoke, then the frozen case matrix
  for both subjects, then held-out paraphrase/distractor expansion only if clean.
  Stop on invented IDs, unsafe actions, ambiguity misapplication, transport failure,
  or cap exhaustion. No database mutation or actual correction execution.
- Preserve existing 100% target/action/safety gates; target p95 end-to-end decision
  under 500 ms and at least 50% lower full-task cost than the fresh incumbent.
  These last two are proposed experiment targets, not existing measured results.
  Retain the owner's 5-second/$0.01 per-case ceilings as outer limits.
- Total provider ceiling: **US$1**, including access probes, both subjects,
  repetitions, fallback, and any judging. Use deterministic scoring where possible.
  Stop if the zero-cost resolved preflight cannot fit that ceiling.

Campaign maximum for the numbered selection: **US$1**. No money spent.
Approval of item 1 authorizes only this isolated owner experiment, not the
deferred baseline-development proposals below or production adoption.

Storybook's text-only artifact-link proposal stage is a second promising lane:
[prompt](/Users/cam/Documents/Projects/Storybook/storybook/packages/backend/src/ai/prompts/artifact-link-proposals.ts:74).
It consumes upstream photo descriptions/OCR, not raw images, and selects existing
candidate IDs. Its two-case eval is too small for an adoption claim and its
generated explanations need separate treatment. Face/place/object visual judges
are not direct JEV candidates. General research/evidence routing lacks a maintained
closed-label eval and is deferred.

## Other projects — not recommended for a provider comparison yet

| Project | Disposition | Concrete next experiment and baseline |
| --- | --- | --- |
| Echo Forge | **Defer live comparison; highest-priority new eval** | Transcript window → cue classes plus active/no-cue/unknown. Project the GPT-5.4 Mini extractor onto those fields; separately measure the live deterministic matcher/action policy. |
| Dossier | **Defer; optional offline review-triage eval** | Source + emitted assertion → supported/contradicted/insufficient evidence. Compare against independent source review; measure defects caught per item reviewed. Do not filter or mutate graphs. |
| Doc Web | **Defer; new text issue-triage eval** | Extracted HTML/text dossier → known issue class and review/rerun/no-action. Compare current planner and deterministic detectors on at least two document structures. |
| Scrypted (`wyze-homekit`) | **Defer; collect ambiguous incident fixtures first** | Classify residual log evidence after exact probes. Compare current shell router and human diagnosis, preserving command/permission ownership. |
| Conductor | **Defer** | No maintained high-volume runtime semantic router or labeled benchmark found. Capture real misroutes first; scripts currently handle metadata/credentials/checks, while semantic triage is skill-driven. |
| Robo Rally | **Defer** | Fixed-seed legal candidate-program selection versus current bot and stronger deterministic rollout scorer. Candidate generation and a tactical-quality eval must be built first; existing tests measure execution more than playing strength. |
| CineForge | **Defer** | Inspected as a registered owner. Text scene classification could eventually fit, but current maintained lanes generate metadata/rationales or require vision/video. Normalization routing already has explicit parser/quality rules. No direct JEV comparison proposed. |
| Board Game Ingester | **Do not evaluate current lanes** | Source-role routing needs pixels. Existing metadata-only baseline deliberately abstains; text-only JEV cannot replace the image evidence. OCR/caption preprocessing would be a different pipeline with its own cost and quality proof. |

### Evidence and eval gaps

**Echo Forge:** [extractor](/Users/cam/Documents/Projects/echo-forge/scripts/campaigns/extract.mjs:15)
uses GPT-5.4 Mini; [loader](/Users/cam/Documents/Projects/echo-forge/scripts/campaigns/eval.mjs:104)
includes 16 narration fixtures among 34 extraction goldens. These seed a new
classification eval but lack enough no-cue/table-chatter cases. The
[PTT policy](/Users/cam/Documents/Projects/echo-forge/src/soundscape/pttCapture.ts:127)
and [matcher](/Users/cam/Documents/Projects/echo-forge/src/soundscape/soundMatcher.ts:1)
are a different, deterministic operational baseline.
The [spec](/Users/cam/Documents/Projects/echo-forge/docs/spec.md:93) explicitly
calls the high-confidence setting provisional. Use multi-label cue decisions;
a window can contain ambience and a discrete action together. Start with newly
authored synthetic narration/negative cases and owner-cleared seed text, not
licensed room text or personal recordings by default. Proposed child gates:
no observed autoplay-causing hard-negative errors, cue recall at least 90%,
macro-F1 no worse than the fresh projected extractor, and p95 classification
below 150 ms. Measure transcription-to-action timing separately. First test
offline/shadow behavior; these pilot gates do not authorize live autoplay.

**Dossier:** inspected both the stale/dirty primary checkout and the newer
`/Users/cam/.codex/worktrees/dossier-semantic-benchmark-20260919` at `5cbe6c30`.
The [engine](/Users/cam/.codex/worktrees/dossier-semantic-benchmark-20260919/src/dossier/engine.py:276)
separates ordinary extraction from direct semantic identity extraction.
[ADR-025](/Users/cam/.codex/worktrees/dossier-semantic-benchmark-20260919/docs/decisions/adr-025-caller-owned-provider-execution/adr.md:8)
qualifies one direct semantic generation call. The ordinary adjudication/judge
stages still exist, but optimizing them is not evidence for that successor.
[Story 170](/Users/cam/.codex/worktrees/dossier-semantic-benchmark-20260919/docs/stories/story-170-standalone-semantic-value-benchmark.md:12)
provides source-reviewed semantic benchmark material. Derive and independently
review assertion-level labels before any classifier test; semantic obligations
are not automatically binary gold labels. Existing candidate-verifier history
also showed recall regressions: [Story 136](/Users/cam/Documents/Projects/dossier/docs/stories/story-136-candidate-verifier-benchmark-loop.md:190).
Do not add another extraction stage just because its output vocabulary is closed.

**Doc Web:** the apparent ready routing benchmark is
[contact-sheet vision](/Users/cam/Documents/Projects/doc-web/modules/intake/contact_sheet_overview_v1/main.py:64),
so it is not a direct match. Better text evidence exists in the
[consistency dossier/planner](/Users/cam/Documents/Projects/doc-web/modules/validate/plan_onward_document_consistency_v1/main.py:537).
It also generates conventions, evidence, and repair rationale, which JEV cannot
replace wholesale. Current
[eval](/Users/cam/Documents/Projects/doc-web/docs/evals/registry.yaml:3512)
is manual and Onward-only, with recorded retry prerequisites after the original
gap closed. Build synthetic repeated-structure documents with reviewed defect
mutations and clean controls. Keep generated correction text and deterministic
neighbor/context selection outside the classifier. Gate on severe-issue recall,
unnecessary rerun rate, and correct context sufficiency, not status accuracy alone.

**Scrypted:** owner is `/Users/cam/Documents/Projects/wyze-homekit`.
[next-action.sh](/Users/cam/Documents/Projects/wyze-homekit/scripts/next-action.sh:112)
already orders service/plugin/LAN/HomeKit/auth/stream checks. Reproducing that
if/else tree with a network model would add cost and failure modes. An eval is
worthwhile only on ambiguous or conflicting log evidence that requires semantic
interpretation. Build synthetic/redacted incident packets covering stale probes,
one-camera versus both-camera failure, simultaneous faults and insufficient
evidence. Separate the known root cause from the next safe diagnostic step;
current script output is a baseline, not ground truth. No live probes or repairs
were run during this research.

**Robo Rally:** [bot policy](/Users/cam/Documents/Projects/roborally/src/core/bot-policies.js:3)
uses deterministic checkpoint routing;
[engine](/Users/cam/Documents/Projects/roborally/src/core/scenario-engine.js:185)
enforces legal choices. Simulating/retaining complete candidate programs and
testing playing strength across seeds would be new work. Numerical/spatial
calculations belong in code. No evidence yet that JEV improves over a stronger
deterministic scorer enough to justify the added model boundary.

Additional registered-owner evidence:
[CineForge routing](/Users/cam/Documents/Projects/cine-forge/src/cine_forge/modules/ingest/script_normalize_v1/routing.py:27),
[CineForge config eval](/Users/cam/Documents/Projects/cine-forge/docs/evals/registry.yaml:654),
[Ingester source-role eval](/Users/cam/Documents/Projects/boardgame-ingester/docs/evals/registry.yaml:1251).

## Recommended sequence

Run the bounded Storybook comparison if selected. Prepare Echo Forge's new
classifier baseline next. Consider Dossier offline review triage and Doc Web
issue triage only as new measured capabilities with clear downstream value.
Hold Scrypted until there are unresolved incident examples. Keep Conductor and
Robo Rally off the first campaign. All deferred work needs its own concrete
owner plan before implementation/provider spending.

Validation: source/code claims and local links inspected; Conductor lint and
whitespace checks recorded in the task handoff. No product suite was needed for
this research-only artifact. No adoption or current model superiority claimed.

## Hosted activation — 2026-09-21

Cam explicitly selected hosted Storybook and supplied a new owner runtime key;
the central synthetic-evaluation credential was not reused. Deployment candidate
`c0a3929` records that operator decision. The production image is
`sha256:b73ce5045cad6b7ecda6f0fd96f1b3a09140373760b0ea928f9454e7d6eb14a2`.
Enforced media-storage and PDF-toolchain startup passed in an isolated process
with production bindings before cutover. No schema/package/Dossier pin changes
relative to the prior image; no migration or private corpus replay was run.

The app and active worker have the new runtime key and enabled flag. Existing
identity/private/worker settings and the $30 identity cap were preserved.
Public health/database and provider readiness passed; root, login and JavaScript
bundle returned HTTP 200. The coordinator visually inspected the in-app browser
landing page with zero console errors. The stored production authenticated smoke
token returned 401, so authenticated smoke remains unverified; no sign-in/out or
user-record inspection was attempted.

One synthetic call through the actual deployed router on the active worker used
`jev-1.13.0`, 849 input / 52 output tokens, 284 ms and $0.000035658 published-price
cost. It completed without Haiku fallback, database writes or private replay.
This verifies activation/transport, not new production accuracy or savings.

The stopped standby's runtime key and enabled flag were also verified through
a temporary idle Node process with worker processing disabled. It was then
stopped and its original worker command, enabled processing policy and standby
association restored with skip-start; final state remains stopped. No extra
inference was performed for this check. Deployment release is v27.

Final checks verified all three machines on the candidate digest and both worker
configurations equal to their predeploy snapshots apart from image. Both health
endpoints returned 200. Fly's aggregate secret status remains Partial with the
standby stopped; actual app/active-worker key presence and enabled flag, plus the
standby's controlled boot, were verified. Do not claim aggregate FullyDeployed.

Owner deployment record landed at `63d75877040e19ecdf94a2d8743710dea1fa26b3`
on Storybook remote main. See [deployment log](https://github.com/copperdogma/storybook/blob/63d75877040e19ecdf94a2d8743710dea1fa26b3/docs/deploy-log.md#story-167-hosted-jev-activation--2026-09-21).

## Approved remaining portfolio campaign — 2026-09-21

Cam explicitly set a goal to complete all remaining positive proposals and
review the grand total afterward. Selected: Doc Web five-class text issue
triage, Dossier source/assertion review assistance, Storybook textual artifact
candidate selection, and Scrypted ambiguous-diagnostics classification. Missing
fixtures and harnesses are authorized preparation, not indefinite deferrals.

Combined provider ceiling US$2, allocated Doc Web $0.60, Dossier $0.60,
Storybook $0.40 and Scrypted $0.40, including qualification/comparators/retries.
Use synthetic/public independent gold and same-input relative baselines; freeze
before calls. Semantic mistakes are observations, not automatic stopping gates.
No product/default changes, commits/pushes, deployment, or adoption decision is
part of this campaign. Private production payloads and the new Storybook runtime
key remain out of scope; Conductor's synthetic-eval key is used temporarily.
Conductor, Robo Rally, CineForge and Board Game Ingester remain deferred, as do
Cam's explicit exclusions Bishop, updater/maintenance and Labor/Zero.

Owner worktrees are independent of primary checkouts and prior frozen evidence.
Coordinator owns fixture/contract review, aggregate budget and final synthesis;
owner workers build and judge repo-local lanes. Each owner must return source
identity, raw synthetic responses, cost ledger, relative results, evidence
limits, focused validation and temporary-key cleanup.

## Remaining portfolio campaign results — 2026-09-21

The four approved experiments completed in isolated owner worktrees. All used
synthetic fixtures with independent gold review, fresh provider calls, and
relative comparisons. No runtime/default changes, deployments, commits, or pushes
were made in this campaign. These results support choosing useful imperfect
components, rather than requiring a perfect score or arbitrary savings floor.

| Owner lane | Relative evidence | Recommendation |
| --- | --- | --- |
| Doc Web issue triage | 20 cases ×2: JEV 24/40, GPT-4.1 narrow projection 29/40, predeclared real serial cascade 33/40. Cascade $0.0196916 vs GPT $0.043408 (54.64% less); median 495 vs730ms, p95 1691 vs1136ms. Both cascade and GPT had three false-clean defects. | Highest-priority bounded shadow integration of JEV plus fallback; retain deterministic layout checks. Full planner and repair outcomes remain unmeasured. |
| Dossier assertion review | 15 short source/assertion pairs: JEV and pinned GPT-5.5 both15/15, including9 held-out; each caught10 planted defects without false alarms. JEV $0.000153006 vsGPT $0.01111; three matched batches took592 vs8919ms in aggregate. | Pursue optional advisory review, preserving source evidence and human/main-model authority. This adds a check; it does not replace semantic graph extraction. |
| Storybook artifact-link candidate selection | 12 scenarios/30 candidate labels: JEV25/30, Gemini2.5FlashLite23/30, new score-only reference17/30. No rejected candidate strongly accepted by either model; unnecessary review proposals2 vs4. | Positive candidate-selection result, but retain Gemini full judge for now. A selection/completion integration must still supply rationale, evidence, and follow-up questions. Candidate-only savings are not complete-workflow savings. |
| Scrypted diagnosis | 16 synthetic incident packets: JEV diagnosis16/16; acceptable next diagnostic15/16. Existing unchanged script replayed16/16 but has a different remediation contract, so no invented head-to-head accuracy. | Useful lower-priority read-only diagnostic assistant; keep repair actions deterministic. No automated remediation or production rollout justified by this small screen. |

Doc Web represents ten paired mutation patterns across only two source documents,
not forty independent documents. Dossier is deliberately defect-enriched and does
not measure normal defect prevalence. Storybook's thirty labels are clustered in
twelve scenarios; the full Gemini contract is richer than JEV's selection output.
Scrypted's script baseline is descriptive, not a weaker gold standard. Confidence
calibration, real-traffic economics, and production accuracy remain unmeasured.

### Campaign accounting and evidence integrity

| Owner | Actual provider calls | Published-price usage cost | Approved cap |
| --- | ---: | ---: | ---: |
| Doc Web |97|$0.063099600|$0.60|
| Dossier |7|$0.017273006|$0.60|
| Storybook links |52|$0.008508768|$0.40|
| Scrypted |16|$0.000840420|$0.40|
| **Total** |**172**|**$0.089721794**|**$2.00**|

These are this four-lane campaign's usage-priced inference costs, including all
qualification, preliminary, rejected, and corrected calls; not historical
portfolio spend, agent labor, or provider invoice reconciliation. Workflow arm
costs share underlying calls and are not added again.

Dossier's initial alias call served `gpt-5.5-2026-04-23` and failed the initial
exact-identity gate. Its $0.00601 remains counted; the comparator was pinned to
that observed checkpoint and rerun with unchanged semantic fixtures/prompts.
Storybook's preliminary26-call run is preserved and excluded from the quality
verdict because raw-before-parse custody, reservation/output-cap alignment, and
contract protections needed repair. The corrected26-call run has its own frozen
identity; both runs' costs are included. Scrypted initially quarantined four
responses whose rounded probability maps summed to0.99. Original envelopes and
strict-parser results were retained, then reparsed offline with explicit rounding
tolerance; no new calls, probability normalization, or gold changes were used.

All four centrally injected TypeSafe eval-key entries were removed after calls.
Owner runtime credentials were not copied or changed. Focused owner validation,
source hashes, request/response artifacts, independent reviews, and usage ledgers
remain in the owner worktrees for review. No private source replay occurred.

### Owner evidence

- [Doc Web report](/Users/cam/.codex/worktrees/jev-docweb-20260921/docs/evals/artifacts/jev-consistency-20260921/report.md), branch `codex/jev-docweb-20260921`, base `0a4d20ff894892f4d96a9a4541d9299d358c2cd5`.
- [Dossier Attempt014](/Users/cam/.codex/worktrees/jev-dossier-review-20260921/docs/evals/attempts/014-jev-assertion-review.md), branch `codex/jev-dossier-review-20260921`, base `3d66f3c52b5f27a58bd49d807e23a94b678e8baa`.
- [Storybook link-selection report](/Users/cam/.codex/worktrees/jev-storybook-links-20260921/docs/evals/artifacts/story061-jev-relative-20260921-v2/report.md), branch `codex/jev-storybook-links-20260921`, base `63d75877040e19ecdf94a2d8743710dea1fa26b3`.
- [Scrypted report](/Users/cam/.codex/worktrees/jev-scrypted-20260921/evals/jev-scrypted/REPORT.md), branch `codex/jev-scrypted-20260921`, base `e0c438f90a3fa9185da27d64fcd100e60106c758`.

The previous portfolio decisions remain distinct: Storybook relationship routing
was already deployed; Echo Forge's Gemini/Grok control-intent implementation was
already landed. No new evidence here reverses Echo's relative model preference.
The four newly screened lanes were worth reconsidering. Conductor, Robo Rally,
CineForge and Board Game Ingester remain deferred for the previously recorded
lack of a concrete semantic router, tactical framework, matching lane, or text-only
fit; Bishop, updater/maintenance and Labor/Zero remain explicitly excluded.

Final validation: Doc Web five focused tests plus Ruff/methodology; Dossier seven
focused tests plus Ruff/registry parsing; Storybook four harness tests plus backend
typecheck, full lint and methodology; Scrypted eleven tests. Owner whitespace
checks passed. Conductor lint and whitespace checks passed; all four owner report
links resolve. Coordinator independently verified all four injected key entries
absent without printing secret values. Results, tooling and records remain
uncommitted in the isolated worktrees, ready for Cam's combined review.

## Approved implementation follow-through — 2026-09-21

Cam approved following the recommendations. The next implementation slice is
Doc Web opt-in shadow triage beside the existing planner and Dossier optional
source/assertion advisory review. Existing authoritative output, deterministic
checks, extraction, and fact acceptance stay in control. Owner worktrees and
evaluation evidence are retained; new owner stories own runtime changes and
integration validation. TypeSafe HTTP/Choice and citation-check documentation
were refreshed from official sources on this date. Validation targets real owner
interfaces, failure isolation, source binding, opt-in behavior, and inspectable
synthetic artifacts. No private replay, paid model rerun, runtime credential
provisioning, commit, push, or deployment is needed for this implementation.

### Doc Web implementation validation

Story234 adds one post-planner hook and an isolated, default-off JEV shadow
module. The full planner and deterministic layout checks stay authoritative.
Explicit uncertainty routes to review; low-confidence or failed calls use the
existing planner decision. This reuses an already-computed result, not the
separate serial GPT call from the evaluation, and adds cost rather than claiming
production savings. Runtime inputs are compact extracted HTML plus conventions;
prior source-prose evaluation accuracy is not asserted for this different input.

Owner configuration requires both `DOC_WEB_JEV_SHADOW=enabled` and a distinct
`DOC_WEB_TYPESAFE_RUNTIME_API_KEY`. No key was provisioned or feature enabled.
Limits are three attempted chapters,16KiB state,64KiB response, two-second caller
deadline, and $0.008064 conservative per-invocation exposure; no redirects/retries.
A timed-out daemon request can finish remotely, so unknown exposure remains
reserved and no late decision is applied. Sidecars omit source excerpts/error
bodies, bind input/plan/authoritative hashes, and replace old reports atomically.

26 affected tests, Ruff, methodology, whitespace, and independent review passed.
The real driver ran disabled/enabled/failure modes using synthetic input,
network-blocked mocks and no inherited provider keys. Primary report, dossier,
pattern inventory, plan and conformance artifacts match apart from run metadata.
Root inspected explicit-uncertain routing and the failed-call reservation.
All222 prior Story233 evaluation artifacts retain their frozen hashes.

- [Setup and limits](/Users/cam/.codex/worktrees/jev-docweb-20260921/docs/runbooks/jev-consistency-shadow.md)
- [Integration artifacts](/Users/cam/.codex/worktrees/jev-docweb-20260921/docs/evals/artifacts/story234-jev-shadow/README.md)
- [Owner story](/Users/cam/.codex/worktrees/jev-docweb-20260921/docs/stories/story-234-jev-consistency-shadow-routing.md)

This is implemented/validated code in an isolated worktree, not a commit, push,
deployment, private replay, or new live-provider qualification. Additional provider
spend for implementation validation is zero; sidecar usage examples are mock data.


### Dossier implementation validation

Story171 adds the explicitly invoked `review_semantic_assertions` API. Ordinary
extraction never calls it, and advisory judgments cannot change accepted graph
facts. The caller owns HTTP dispatch, product authorization, response custody,
WAL and timeout enforcement; the library discovers no credentials and performs
no hidden network calls. This reviews cited excerpts, not full-source or external
truth. Runtime adoption requires a consumer-owned HTTP/auth callback.

Requests preserve opaque entity IDs alongside labels, exact evidence passages,
source roles, offsets and assertion qualifiers. Fixed model/rate reservations,
request/response size caps, batch/assertion/token limits, deadlines and cost bounds
are checked before dispatch. Stable request hashes and batch ordinals distinguish
identical request bodies. Failed or malformed batches make the entire report
unavailable while retaining known usage and unknown-outcome reservations.
Consumed response fields are validated strictly, duplicate JSON keys reject, and
unused additive provider metadata is allowed. Malformed callback models cannot
emit value-bearing validation warnings.

The owner passed 11 final advisory tests, seven frozen-eval tests and an earlier
58-test affected semantic boundary run; unchanged boundary results were reused
after the final strictness-only additions. Independent review passed 18 focused
checks and returned CLEAR. Ruff, size limits and whitespace checks passed.
The semantic contract fingerprint is unchanged:
`028b1cecba17bd6bb6ccb65ca7da36891a200fb0b0ef1346bc8319020a19b149`.
Retained synthetic complete and partial-failure reports show identical sealed
result hashes before and after review. Root inspected both reports, including the
second-batch unknown outcome with no leaked partial judgments.

- [Public API and caller responsibilities](/Users/cam/.codex/worktrees/jev-dossier-review-20260921/README.md)
- [Validation and retained reports](/Users/cam/.codex/worktrees/jev-dossier-review-20260921/docs/stories/artifacts/story-171/validation.md)
- [Owner story](/Users/cam/.codex/worktrees/jev-dossier-review-20260921/docs/stories/story-171-optional-advisory-assertion-review.md)

### Implementation goal complete

Both owner stories are Done, independently reviewed, and ready for combined
review in their isolated worktrees. Doc Web remains disabled; Dossier requires
explicit caller integration. No new live-provider qualification or private replay
was performed. Implementation validation incurred zero provider spend, leaving
the preceding four-lane evaluation total at $0.089721794. Synthetic report usage
is not billed API usage. No commits, pushes, deployment or credential provisioning
occurred. Storybook's full artifact judge and Scrypted repairs remain unchanged.
The next recommended step is scoped landing of the validated work, followed by
separately configured runtime observation before any authoritative adoption.


## Approved landing and observation preparation — 2026-09-21

Cam approved the recommended next step. The finish-and-push workflow covers
Doc Web and Dossier integrations, their evaluation evidence, the linked Storybook
and Scrypted evaluation-only changes, and Conductor records. Each owner owns its
Git integration; all five repositories are preflighted before any push. Existing
validated inputs are reused; only affected integration surfaces require reruns.
Primary checkouts and unrelated dirty work remain untouched. Reviewed primary
Conductor inbox captures are already represented in the newer task copy.

Runtime observation remains advisory. Doc Web is the first runnable observation
path: use the owner's distinct runtime key and explicit enable setting, limit the
initial run to one invocation (at most three JEV attempts), inspect coverage,
latency, unknown reservations and disagreements with the unchanged planner, and
retain the sidecar with its input hashes. Do not treat agreement as a gold label
or claim savings from shadow mode. Dossier is a library API; representative
observation requires an identified consumer to supply authenticated dispatch and
source custody. No generic library-owned network path should be added merely to
turn it on. Runtime key absence does not block landing validated disabled code.


Observation setup check: the Doc Web primary runtime key was absent and shadow
was not enabled. A blank `DOC_WEB_TYPESAFE_RUNTIME_API_KEY` entry and
`DOC_WEB_JEV_SHADOW=disabled` were prepared only in the isolated worktree's ignored
`.env`; all existing values and the primary checkout were preserved. Cam was
asked to fill the key locally. No central eval key was repurposed. The first
native observation can use the retained r4 synthetic dossier and mock-authored
plan through `write_shadow`, capped at one call/$0.002688 reserve; this qualifies
runtime transport and policy only, not production quality or savings. No live
observation has been run while that credential is missing.


### Verified owner landings

| Repository | Commit on remote main | Scope |
| --- | --- | --- |
| Doc Web | `81d4cfa95da71f10ef28e5f82195d8e496610a5d` | Story233 evaluation and Story234 disabled shadow integration |
| Dossier | `9fc49b175ef6b1a79ec5a291f8b7b771ab728687` | Attempt014 evaluation and Story171 explicit advisory API |
| Storybook | `b619d00745e5cda87893f2db26a7d337ae8c62fd` | Attempt160 artifact-link evaluation only |
| Scrypted | `b2198f3d4c1a6e6663fee9e4571002959fd422a9` | Synthetic diagnostic evaluation only |

Every owner refreshed its remote, pushed its execution branch, fast-forwarded
main without force, and verified the exact destination hash with `git ls-remote`.
No integration conflicts arose. Each task worktree is clean and retained; ignored
credential files and protected local raw evidence remain outside commits. Primary
checkouts were not reset, stashed or synchronized. Applicable prior validation
was reused after hash checks; Dossier additionally passed18 combined tests and
Doc Web refreshed methodology validation. All scoped secret/whitespace checks
passed. No provider calls were made during landing. The earlier unlanded statuses
above describe their historical checkpoints and are superseded by this record.

The validated integrations and all four campaign evidence sets are now landed.
Doc Web live observation is pending its dedicated runtime key; Dossier consumer
observation is pending an identified host integration. Neither integration has
been enabled for private production data. Storybook's full artifact judge and
Scrypted repair behavior remain unchanged.
