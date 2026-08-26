# Alignment 045 - Retrospective Model Rerun Matrix

**Date**: 2026-08-14
**Classification**: Recommendation-first historical evidence audit with repo-local paid execution
**Story**: [Story 029](../stories/story-029-retrospective-sota-model-reevaluation.md)
**Depends On**: [Alignment 044](align-044-eval-validity-and-incumbent-parity.md)
**Projects Reviewed**: conductor, cine-forge, doc-web, echo-forge

## Decision

Revisit historical model attempts only to choose which current-contract reruns
can change a maintained decision. Old scores do not remain decision-bearing when
the prompt, scorer, output-provenance chain, or runtime contract changed.

Evidence roles:

- **Replayable**: retained raw evidence can be recomputed under the current
  contract without a fresh subject call.
- **Shortlist-only**: historical behavior identifies a plausible candidate or
  differentiating failure, but current-contract parity requires a fresh call.
- **Obsolete**: transport, modality, privacy, latency, cost, or known quality
  evidence makes the candidate incapable of changing the current decision.

## Product Contract Correction

doc-web's hand-authored crop goldens are the normative acceptance benchmark.
Their known status does not invalidate them. Repeated exposure is disclosed as
a generalization limitation, but no new 12-case held-out set is required before
the current model comparison. Future books can expand the regression suite when
Cam has time to correct new SOTA output into additional ideal examples.

## Campaign Rules

- Freeze each repo's historical classification, candidate list, incumbent,
  prompt, fixtures, scorer/golden, configuration budget, retry cap, and stop
  rules before paid calls.
- Default aggregate provider-spend ceiling: US$5 per repo.
- Rerun the incumbent whenever a fresh superiority claim is possible.
- Use provider-valid recommended settings and at most two justified candidate
  variants; do not tune only the challenger.
- Separate access, transport, reliability, semantic capability, economics,
  privacy, and adoption verdicts.
- No runtime-default change is part of this campaign.

## Rerun Matrix

| Repo / surface | Current incumbent | Historical candidates | Evidence classification | Fresh decision-bearing matrix | Status |
| --- | --- | --- | --- | --- | --- |
| CineForge QA | GPT-4.1 Mini | Gemini 3.7 Flash | Old rows were shortlist-only after the QA contract repair | Fresh two-case exact-runtime parity | GPT-4.1 Mini leads `0.817475` to `0.73495`; neither reaches `1.0` |
| CineForge config detection | Gemini 3 Flash | Gemini 3.7 Flash | Historical rows shortlisted the cheaper challenger; current parity required | Fresh two-corpus subject and symmetric replacement-judge arm | Gemini 3 Flash leads `0.67995` to `0.65245`; neither reaches `0.92`, incumbent misses latency |
| CineForge script bible | Gemini 3.5 Flash-Lite | Gemini 3.7 Flash | Historical rows were not current exact-runtime parity | Fresh two-corpus exact-runtime and symmetric replacement-judge arm | Gemini 3.5 leads `0.74495` to `0.70995`; neither reaches `0.90` |
| doc-web detector | Gemini 3 Flash | GPT-5.6 Terra | Retained scores were close but not fresh symmetric parity | Fresh 13-case candidate/incumbent rerun | GPT-5.6 Terra is new measured and production-eligible leader: `13/13`, `0.9689` |
| doc-web crop-only | Gemini 3.1 Flash Lite | Gemini 3.7 Flash | Gemini 3.7's prior source-backed miss required retained/fresh confirmation; raw result was absent | Fresh 40-case candidate/incumbent rerun | Gemini 3.1 retains quality and production lead: `40/40`, `1.0`; 3.7 repeats `39/40` |
| doc-web page context | GPT-5.5 Responses | GPT-5.6 Terra | Current retained artifacts are replayable on unchanged goldens | No paid rerun: `22/22` already beats Terra `21/22` | GPT-5.5 retains lead |
| doc-web handwriting | Gemini 3.6 Flash | Gemini 3.7 Flash | Current corrected-real evidence is replayable and decisive | No paid rerun | Gemini 3.6 retains measured lead; neither reaches `0.99` |
| Echo Forge scene outline | GPT-5.4 Mini | Gemini 3.7 Flash; GPT-5.6 Terra | All prior provider results lacked fresh v3 parity | Fresh two-fixture v3 run for all three | Official three-way `0/2` tie; no sole quality leader and no production-eligible winner |

## Final SOTA Decisions

“SOTA” is now split into two explicit claims:

- **Measured quality leader**: the highest valid comparable current-contract
  score, even below the absolute target.
- **Production-eligible winner**: a measured leader that also clears every hard
  safety, schema, privacy, reliability, latency, and cost gate.

On that basis, GPT-5.6 Terra is the only new leader and only new
production-eligible winner in this campaign, for doc-web's 13-case detector.
CineForge's three freshly rerun incumbents remain their respective measured
leaders but are not production-qualified under the repaired contracts.
doc-web's crop-only, page-context, and handwriting leaders remain unchanged.
Echo Forge has an official three-way tie at `0/2`; the incumbent stays
executable for continuity but no longer owns a unique current SOTA claim.

Total conservative provider spend was approximately `$1.32303`: CineForge
`$0.942709`, doc-web `$0.29152`, and Echo Forge `$0.08880`.

## Intentional Divergence

The repos should not share one global model ranking. CineForge screenplay QA,
doc-web crop/OCR validation, and Echo Forge live soundscape mapping have
different modalities, latency budgets, privacy paths, and failure costs.
