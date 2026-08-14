# Scout 054 - Route Gemini 3.7 Flash and DeepSeek V4 Pro GA Evals

**Source**: Official Google Gemini and DeepSeek API changelogs, model guides,
pricing documentation, and authenticated API probes, checked 2026-08-13.
**Status**: Spike
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
canmore-town-council, boardgame-ingester, roborally, echo-forge

## Summary

Two decision-relevant model releases landed on 2026-08-13:

- Google released Gemini 3.7 Flash to GA as `gemini-3.7-flash`. It is a stable,
  natively multimodal text/image/video/audio/PDF model with a 1,048,576-token
  input limit, 65,536-token output limit, structured outputs, function calling,
  built-in tools, and `low`/`medium`/`high` thinking. Introductory pricing through
  2026-12-31 is $0.75/M input and $3.75/M output, then doubles. Google positions
  it as a stronger coding, agentic, spatial/multimodal, and design-adherence
  successor to Gemini 3.6 Flash.
- DeepSeek promoted V4 Pro to GA and updated the existing `deepseek-v4-pro`
  alias to DeepSeek-V4-Pro-0813. This is a production/post-training update
  behind the existing slug, not a new API name. The text-only model has a 1M
  context window, up to 384K output, JSON output, tools, Responses,
  Chat Completions, and Anthropic-compatible APIs, plus low/high/max thinking
  controls (with lower compatibility levels mapping upward). DeepSeek's direct
  list price is $0.435/M uncached input, $0.003625/M cached input, and $0.87/M
  output before the announced peak/off-peak pricing change on 2026-08-16.

Both are available to the current workspace, with stronger evidence than a
catalog listing:

- The repo-scoped Dossier Google credential returned a schema-valid
  `{"status":"API_OK","accessible":true}` from `gemini-3.7-flash`, with exact
  returned model identity and terminal `STOP`. An initial `minimal` thinking
  probe correctly returned Google's documented unsupported-level error; the
  valid probe used `low`.
- No repo-local direct DeepSeek credential was found, but the existing Dossier
  OpenRouter account returned schema-valid
  `{"accessible":true,"status":"API_OK"}` from
  `deepseek/deepseek-v4-pro`, served by Baidu with terminal `stop`, while
  requiring supported parameters and denying data collection. OpenRouter is
  therefore the practical first eval path unless a direct DeepSeek account is
  deliberately added. Use public/synthetic fixtures until a chosen route's
  retention posture is pinned and recorded.

These are eval triggers, not default-change evidence.

## Recommended Eval Routing

### Gemini 3.7 Flash

1. **doc-web — Spike first.** This is the cleanest predecessor-to-successor
   question in the portfolio. Gemini 3.6 Flash was already close: `13/13` on
   the detector, `39/40` crop-only, `21/22` page context, and about `0.984` on
   both corrected real-handwriting fixtures, but it missed every maintained
   promotion bar. Run the exact progressive ladder: 13-case detector, then
   40-case crop-only and 22-case page-context only if justified, plus the two
   corrected real-handwriting fixtures. Stop on the first maintained hard-gate
   failure. The new half-price introductory rate makes a real quality win more
   operationally plausible than the 3.6 result.
2. **cine-forge — Spike second.** Test the exact source-backed failures from
   Gemini 3.6 rather than rerunning every model slot blindly. Start with the
   known-good QA case and six-anchor ordered-frame/video lane; only expand to
   `script_bible_v1` if the owning agent needs a direct runtime-value comparison
   against Gemini 3.5 Flash-Lite. Require current quality, latency, and cost
   gates. Google's coding/design claims do not prove screenplay or video truth.
3. **dossier — Spike third, judge-stage only first.** Gemini 3.5 Flash was not
   viable as the extraction/adjudication default, but it left one unresolved
   judge-stage promotion question after beating `gpt-4.1-mini` on entity and
   relationship F1 while losing projection F1 and value. Use the maintained
   judge comparison to test whether 3.7's higher quality plus introductory
   price closes that exact gap. Do not repeat broad extraction matrices unless
   the judge screen passes or a current failing extraction golden names a new
   decision.
4. **boardgame-ingester — Defer.** Its rulebook/image corpus is relevant, but
   no current story has selected a failing model-owned lane. Use 3.7 as the next
   subject only when package readiness opens a concrete multimodal eval.
5. **storybook — Reject for this wave.** A Flash model can sound superficially
   appropriate for Luna, but no maintained failing persona golden currently
   justifies another chat-default campaign. Storybook should consume upstream
   doc-web/Dossier wins instead of duplicating their model evaluation.
6. **echo-forge, canmore-town-council, roborally — Defer or reject.** None has a
   more decision-bearing Gemini 3.7 lane than the three first-wave repos.

### DeepSeek V4 Pro GA

1. **cine-forge — Spike first.** This is the strongest exact-family follow-up.
   DeepSeek V4 Flash qualified strict schema but never completed the full
   `script_bible_v1` screenplay within the reliability/30-second gate, leaving
   quality unmeasured. V4 Pro's GA update and today's fast strict-schema probe
   justify one bounded `script_bible_v1` run through OpenRouter, but not a broad
   suite. Pin served identity, provider, routing, retention, effort, usage, and
   cost; stop immediately if the $0.01/call or 30-second gate fails.
2. **dossier — Spike second.** Run the smallest public/synthetic structured
   extraction and adjudication screen that exercises long-context entity and
   relationship fidelity. Dossier has the best provider-aware harness and the
   existing OpenRouter credential, but the first question is whether V4 Pro is
   reliable and cost-effective on Dossier's runtime contract, not whether its
   vendor agent benchmarks are impressive.
3. **echo-forge — Spike third, aspirational mapper only.** V4 Flash's cheap
   no-reasoning scene-to-soundscape run produced valid schemas but passed `0/2`
   goldens by missing explicit control requirements. The attempt itself named
   a future smarter-generator/reasoning lane as the honest retry condition.
   V4 Pro GA satisfies that trigger: rerun only those two public/synthetic
   goldens at an eligible thinking level, without proposing it as an audio
   model or production default.
4. **canmore-town-council and boardgame-ingester — Defer behind first-wave
   results.** Both have plausible public long-context material, but neither
   should add another candidate before selecting a maintained provenance or
   rulebook-ingest decision lane.
5. **doc-web — Reject.** V4 Pro is text-only, so it cannot address doc-web's
   current visual crop and handwriting blockers.
6. **storybook and roborally — Reject.** V4 Pro is not a credible private
   family-chat default or a decision-bearing game-runtime candidate, and its
   current practical route has not been approved for private inputs.

Conductor owns this scout and routing decision only. Target-repo agents should
execute and interpret any approved evaluations in isolated worktrees; no
target-repo inbox notes or stories were created in this pass.

## Evidence

- Google Gemini API release notes (2026-08-13):
  https://ai.google.dev/gemini-api/docs/changelog
- Google Gemini 3.7 Flash model page and migration/pricing guide:
  https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash
  https://ai.google.dev/gemini-api/docs/latest-model
- DeepSeek API changelog and quick start:
  https://api-docs.deepseek.com/updates/
  https://api-docs.deepseek.com/quick_start/pricing
- OpenRouter DeepSeek V4 Pro route:
  https://openrouter.ai/deepseek/deepseek-v4-pro
- Authenticated evidence on 2026-08-13: exact Gemini direct strict-schema
  response, exact DeepSeek/OpenRouter strict-schema response with supported
  parameters and data collection denied. No benchmark or private fixture was
  sent.
- doc-web predecessor evidence:
  `/Users/cam/Documents/Projects/doc-web/docs/evals/attempts/018-gemini36-flash-and-gemini35-flash-lite-bounded-challenger.md`
- CineForge DeepSeek V4 Flash predecessor evidence:
  `/Users/cam/Documents/Projects/cine-forge/docs/evals/attempts/022-script-bible-deepseek-v4-flash.md`
- Dossier Gemini predecessor decision:
  `/Users/cam/Documents/Projects/dossier/docs/inbox.md`
- Echo Forge DeepSeek V4 Flash predecessor evidence:
  `/Users/cam/Documents/Projects/echo-forge/docs/evals/attempts/scene-to-soundscape-golden/20260803-openrouter-deepseek-deepseek-v4-flash.md`

## Confidence and Open Questions

Confidence is high on launch identity, API callability, structured-output
transport, and the first-wave repo routing. Quality remains deliberately
unknown until the owning repos run their maintained gates.

Open questions:

- Can Gemini 3.7 clear doc-web's one-case crop/page misses and the `0.99`
  handwriting bar without losing latency/value?
- Does Gemini 3.7 repair CineForge's source-backed QA/video failures rather
  than merely scoring well on coding and agent benchmarks?
- Can DeepSeek V4 Pro complete CineForge's full-script contract under 30
  seconds and $0.01 through a pinned privacy-compatible route?
- Does the Pro update add enough instruction fidelity to rescue Echo Forge's
  two missed control requirements?
- Should a direct DeepSeek account be added only after OpenRouter eval evidence
  shows a reason to prefer canonical provider transport?

## Downstream Eval-Validity Outcome — 2026-08-13

Story 028 audited the three executed first-wave lanes before accepting their
model rankings. The audit found material contract defects in every repo and
repaired them in isolated worktrees; Dossier remained untouched.

- **doc-web / Gemini 3.7 Flash**: keep the `page-126-000` fail label and the
  production-safety veto. Gemini remains `39/40`, but all `40` crop-only and
  `22` page-context cases are selection-exposed, challenger tuning was
  asymmetric, and the recorded incumbent `40/40` is stale. There is no honest
  intrinsic winner. Selection is `blocked_pending_held_out_truth`; the next
  contract freezes 12 natural crops, balanced 6/6, across at least eight unused
  source pages before calls. The detector remains credible at `13/13`; both
  handwriting fixtures remain below `0.99`.
- **CineForge / Gemini 3.7 Flash versus GPT-4.1 Mini**: withdraw the old
  incumbent `1.0` and the interim challenger comparison. The final independently
  derived six-family QA contract was established after the paid calls. Frozen
  final-scorer scores are `0.832475` for GPT-4.1 Mini and `0.834975` for Gemini
  3.7; both fail, and fresh final-contract capability parity is unmeasured.
  Gemini was faster in the pre-final calls but cost `3.48x` more. Retain the
  default by inertia, not proven superiority.
- **CineForge / DeepSeek V4 Pro**: retain the operational no-adopt result.
  Full-script quality is unmeasured; the qualified tiny route already failed
  value headroom and the cheaper route exceeded 60 seconds without completing.
- **Echo Forge / DeepSeek V4 Pro**: exact-duration scoring was an unstated
  golden preference and duration belongs to the Executor, not scene-quality
  scoring. The normalized outputs diagnose `2/2` on measured non-duration
  semantics, but raw assistant content was never retained and one normalized
  output cannot reproduce strict schema. Evidence is therefore
  `legacy-incomplete-provenance`: strict output, quality qualification, and
  decision-grade capability are unmeasured. The independent operational reject
  remains valid at `66.889s` and `$0.016126` per fixture plus degraded initial
  routing. Future public/synthetic v3 attempts retain raw content and replay
  strict schema plus deterministic normalization.

No default changed, no private data was used, and none of these repairs
justifies a broader model sweep. The reusable cross-project contract is recorded
in [Alignment 044](../alignments/align-044-eval-validity-and-incumbent-parity.md).
