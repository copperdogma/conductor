# Scout 064 — Muse Spark 1.3 Evaluation Routing

**Source:** Meta first-party release, model, structured-output, pricing, and
privacy documentation; OpenRouter public catalog; checked 2026-09-02.
**Status:** Do not adopt / Defer
**Stage:** Stage 2 owner campaign complete; retry follow-through is authoritative.
**Candidate:** Meta `muse-spark-1.3`; OpenRouter `meta/muse-spark-1.3`
(canonical endpoint `meta/muse-spark-1.3-20260902`)
**Projects reviewed:** conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Identity, contract, access, and privacy

Meta released and API-listed Muse Spark 1.3 with a 1,048,576-token context
window, text, image, video, PDF, and audio inputs, text output, structured
outputs, function calling, and configurable reasoning. Meta's OpenAI-compatible
API exposes Responses and Chat Completions interfaces; the model documentation
also lists Messages compatibility. The exact OpenRouter Standard route is
`meta/muse-spark-1.3`, served through the sole listed Meta endpoint
`meta/muse-spark-1.3-20260902` at the time of qualification.

Public Standard pricing was US$1.25/M input tokens, US$0.15/M cached input
tokens, and US$4.25/M output tokens. Meta states that Standard prompts and
completions are not used for training. This campaign did not use the cheaper,
training-eligible Contributor tier. Neither the provider material nor the
selected OpenRouter path was treated as a verified zero-data-retention
contract, so all selected owner lanes were limited to public or synthetic
fixtures.

Official/public sources:

- <https://research.meta.ai/blog/introducing-muse-spark-1-3>
- <https://dev.meta.ai/docs/models>
- <https://dev.meta.ai/docs/structured-output>
- <https://dev.meta.ai/docs/pricing-rate-limits>
- <https://openrouter.ai/api/v1/models>

## Selected owner evaluations

Cam approved three bounded, provider-native owner evaluations:

1. **Storybook — Luna Persona synthetic challenger, US$0.20 ceiling.** Test
   whether the exact route can enter the maintained persona ladder using only
   synthetic inputs.
2. **CineForge — script-bible Open Frequency, US$0.20 ceiling.** Test strict
   ScriptBible transport and only then the maintained public/synthetic owner
   lane.
3. **Echo Forge — scene-to-soundscape golden, US$0.10 ceiling.** Test the
   public Tavern access/transport gate before any broader fixture run.

**Campaign maximum: US$0.50.**

## Not recommended in this campaign

- **Dossier — Defer.** Its decision-bearing matrix is non-public, and the
  selected route did not establish a sufficient zero-retention contract for
  that data boundary.
- **doc-web — Defer.** No current held-out selection slice made another model
  run decision-bearing.
- **Board Game Ingester — Do not evaluate.** Its current gates are
  deterministic workflow and package checks rather than a maintained model
  comparison.
- **Robo Rally — Do not evaluate.** Its maintained gates are deterministic and
  its canonical rulebook is private.
- **Conductor — Route only.** Owner repositories retain their fixtures,
  evidence, scores, and adoption decisions.

## Stage 2 follow-through

### Storybook

- **Execution surface:** isolated worktree
  `/Users/cam/.codex/worktrees/evaluate-muse-spark-13/storybook`, branch
  `codex/evaluate-muse-spark-13-storybook`, base
  `51ec96f933f6bf7970373ac92a6bf161ab8d0fb6`.
- **Observed stop:** the first synthetic exact-route probe returned a
  pre-inference HTTP 403 requiring the OpenRouter account owner to complete
  18+ age confirmation. No valid model response, incumbent call, judge call,
  or scoring run occurred.
- **Spend and verdict:** US$0.00 of US$0.20. Access is blocked; transport,
  reliability, capability, latency, and per-case economics are unmeasured.
  Adoption is deferred.
- **Owner evidence:** `docs/evals/attempts/115-luna-persona-muse-spark-13-challenger.md`
  and
  `docs/evals/artifacts/luna-persona-muse-spark-13-challenger-2026-09-02.json`.
- **Retry condition:** after the account owner independently completes the
  OpenRouter age confirmation, resume at the same exact-route access gate.

### CineForge

- **Execution surface:** isolated worktree
  `/Users/cam/.codex/worktrees/muse-spark-13-cineforge/cine-forge`, branch
  `codex/muse-spark-13-script-bible`, base
  `89b336ddc95788563d966d8193ae6380f6199a30`.
- **Observed stop:** local disk exhaustion prevented preparation of the durable
  raw-evidence destination. Execution stopped before any provider invocation
  because lossless response persistence could not be guaranteed.
- **Spend and verdict:** US$0.00 of US$0.20. Access is unverified; transport,
  reliability, capability, latency, and economics are unmeasured. Adoption is
  deferred and the provisional Gemini 3.5 Flash-Lite incumbent is unchanged.
- **Owner evidence:** `docs/evals/attempts/035-script-bible-muse-spark-13.md`,
  `docs/evals/story-218-muse-spark-13-evidence.json`, and
  `docs/stories/story-218-muse-spark-13-script-bible-evaluation.md`.
- **Retry condition:** after enough disk is available for durable raw evidence,
  resume only the same tiny strict access/transport probe.

### Echo Forge

- **Execution surface:** isolated worktree
  `/Users/cam/.codex/worktrees/muse-spark-13-echo-forge`, branch
  `codex/muse-spark-13-eval`, base
  `d4c2c316bce11d8962e558d0199385c5863fc15f`.
- **Observed stop:** the first public Tavern request returned a pre-inference
  HTTP 403 requiring OpenRouter 18+ age confirmation. The client observed
  372 ms to the rejection, but no inference, usage, served-model identity, or
  terminal model response occurred.
- **Spend and verdict:** US$0.00 of US$0.10. Access is blocked; transport,
  reliability, capability, latency, and economics are unmeasured. Adoption is
  deferred and the incumbent was not rerun.
- **Owner evidence:**
  `docs/evals/attempts/scene-to-soundscape-golden/20260902-openrouter-meta-muse-spark-1-3.md`,
  its adjacent decision record, and the captured Tavern transport manifest.
- **Retry condition:** after the account owner independently completes the
  OpenRouter age confirmation, resume at the exact Tavern access gate.

## Portfolio synthesis

The campaign spent **US$0.00 of US$0.50**. Storybook and Echo Forge reached the
configured OpenRouter route but were rejected before inference by an account
age-confirmation policy. CineForge stopped even earlier on local disk capacity.
These are access and infrastructure outcomes, not model-quality failures:
strict transport, reliability, semantic capability, latency, and measured
economics remain unknown in all three owner lanes.

No private data was transmitted, and no model default, production runtime,
deployment, commit, or push changed. Each owner retained its uncommitted worktree
and durable stop evidence. Temporary evaluation credentials and task-local
credential material were removed after execution.

## Stage 2 retry follow-through — 2026-09-02

Cam independently completed OpenRouter's 18+ account confirmation and asked
Conductor to retry the stopped gates. The same three isolated owner worktrees,
public/synthetic data boundaries, configurations, and original per-repo spend
ceilings remained in force. No previously unselected repo or wider lane was
added.

OpenRouter's live responses returned the exact requested alias
`meta/muse-spark-1.3` and provider `Meta`, but did not echo the dated endpoint
checkpoint. The authenticated catalog mapped that alias to exactly one Meta
endpoint, `meta/muse-spark-1.3-20260902`. Owners therefore record the checkpoint
as a dated sole-endpoint catalog inference, not as response-returned identity.

### Storybook resumed result

Access cleared. Two 32-token probes were quarantined while the owner resolved
the alias-versus-canonical identity contract, and a third tiny probe exhausted
its deliberately small output budget on hidden reasoning; none was scored. A
source-backed adapter repair accepted the exact alias only with Meta pinned,
fallback disabled, required parameters enabled, and the live sole-endpoint
catalog mapping preserved.

The one authorized fresh warmth harness-parity case then passed its unchanged
rubric and independent GPT-5 judge at `1/1`. Subject latency was 1,754 ms and
subject cost was US$0.00251875; estimated judge cost was US$0.00339875.
Conservative cumulative spend, including upper-bound debits for the three
quarantined probes, is **at most US$0.00681750 of US$0.20**. The remaining 11
turns and fresh incumbent were not run. Access and one-case transport are
qualified, but broader reliability, comparative capability, and full-lane
economics remain unmeasured; adoption remains **defer / not advanced**.

Authoritative owner evidence is Storybook Attempt 116 and
`docs/evals/artifacts/luna-persona-muse-spark-13-access-retry-2026-09-02.json`.
A broader fresh parity comparison requires a separately selected owner run; do
not repeat the tiny identity probes.

### CineForge resumed result

Despite critically constrained shared disk, CineForge preallocated and fsynced
the exact ignored evidence destinations before credential injection. The tiny
strict probe and full synthetic Open Frequency subject both qualified the exact
Meta-pinned provider-strict `ScriptBible` contract without retries. The full
subject completed in 13,376 ms for US$0.00895525; cumulative confirmed spend
was **US$0.01418325 of US$0.20**.

The frozen deterministic scorer produced raw `0.9511` but hard-gated the result
to `0.6999`: four of nine source-faithful theme paraphrases were neither
explicit scene references nor sufficiently literal brief quotes for the
lexical evidence-grounding rule. This is an ambiguous evidence-form/scorer-
contract mismatch; neither a model error nor a golden error was established.
The owner stopped before rubric judge, incumbent, retry, or private data.
Capability remains **inconclusive** and adoption remains **defer**, with the
provisional Gemini 3.5 Flash-Lite incumbent unchanged.

Authoritative owner evidence is the updated CineForge Attempt 035 and
`docs/evals/story-218-muse-spark-13-resume-evidence.json`. Do not repeat the
unchanged subject call; reopen only for a source-backed decision about the
maintained evidence-form contract or an explicitly approved frozen-output
diagnostic.

### Echo Forge resumed result

Access and Tavern transport qualified: strict JSON Schema, terminal completion,
normalization, provenance, usage, cost, and owner-harness parity all passed.
The request used 2,571 prompt and 1,798 completion tokens, including 427
reasoning tokens, and completed in 11,737 ms for **US$0.01085525 of US$0.10**.

Tavern then scored `0/1`. Muse paired `intensity.label=low` with
`defaultLevel=2`, a model-wrong internal inconsistency against the maintained
mapping. It also omitted a separate no-auto-tension negative constraint while
preserving the required muted zero-volume speculative layer; because the frozen
prompt does not explicitly request that separate sentence, the owner correctly
classified this as prompt-wrong / contract-exposure-sensitive rather than a
second model-quality miss. Muse was 15.2% slower and 35.1% costlier than the
retained incumbent averages without a quality advantage. The progressive stop
fired before Dungeon and a fresh incumbent. The exact frozen configuration is
**do not adopt**.

Authoritative owner evidence is the updated Echo Forge 20260902 attempt and its
adjacent decision contract. Do not repeat this unchanged arm; reopen only for a
material checkpoint/provider change or a source-backed prompt, schema, scorer,
or golden change.

### Retry campaign synthesis

Conservative aggregate campaign spend is **at most US$0.03185600 of
US$0.50**. Storybook provided a positive one-case smoke result but not enough
evidence for adoption. CineForge qualified transport and operational gates but
ended inconclusively at an ambiguous deterministic evidence-form gate. Echo
Forge produced the only decision-grade negative result: do not adopt the exact
frozen Tavern configuration. No portfolio-wide Muse Spark capability or
adoption claim is supported.

All three credentials were removed and verified absent after execution. No
private data, runtime default, deployment, commit, push, or merge was involved;
owner changes and evidence remain uncommitted in their isolated worktrees.
