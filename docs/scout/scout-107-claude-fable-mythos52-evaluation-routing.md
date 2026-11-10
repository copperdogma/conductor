# Scout 107 — Claude Fable 5.2 and Mythos 5.2

**Superseded proposal:** [Capability revision 2](scout-107-claude52-capability-revision.md) replaces all numbered choices and the USD53 ceiling after Cam corrected the capability framing. Access research below remains applicable. No old item was selected.

2026-11-09, America/Edmonton. **Stage 1 recommendation only.** No authenticated
catalog/probe, inference, target-repo write, worktree, commit or push. Two
lower-cost read-only owner reviewers assisted; coordinator checked current
owner attempts and bounded the recommendations below. No evaluation-ledger row
is added for an unexecuted proposal. Existing unrelated checkout changes remain.

## Availability and access

- [Fable overview](https://platform.claude.com/docs/en/models/fable-5-2/overview)
  and [release changes](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2):
  released today, all Claude API customers; exact `claude-fable-5-2`.
- [Mythos overview](https://platform.claude.com/docs/en/models/mythos-5-2/overview):
  exact `claude-mythos-5-2`, verified organizations only. Documented same
  capabilities/specifications/pricing as Fable. This is not authenticated
  entitlement or served-weight equivalence proof; do not silently substitute
  the IDs or pay for duplicate capability comparisons.
- Both: text/image input, text output, 1M context, 128K maximum output, adaptive
  thinking always on. Standard USD8/M input, USD40/M output. Native Messages API
  structured JSON and tools supported, but forced `any`/named tools unsupported;
  omit sampling controls. CMEK organizations have a structured-output restriction.
- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort):
  `output_config.effort` low/medium/high(default)/xhigh/max. Thinking consumes
  the total output allowance and bill. High is the initial fidelity setting;
  low is used only for the specified interactive tasks. No effort sweep or
  conditional semantic rescue is proposed. Medium/xhigh/max remain unmeasured;
  these small initial screens first settle source fidelity/contract/value,
  rather than long-running agentic capability. Truncation/adapter repairs are
  operational recovery, recorded separately, not semantic retuning.
- [Retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention):
  covered models require 30-day retention; ZDR only with express Anthropic
  authorization, including on partner clouds. No account settings changes.
  [Commercial training policy](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training)
  excludes training by default, with opt-in/feedback exceptions. Router account
  policy remains unverified; only the public/authored synthetic inputs below
  are proposed. No private genealogy/photos/finance, restricted game scans or
  screenplays.

Public unauthenticated OpenRouter catalog and endpoint GETs list
`anthropic/claude-fable-5.2`, canonical `anthropic/claude-fable-5.2-20261109`.
Saved [catalog evidence](evidence/scout107-claude52-public-catalog.json) includes
Anthropic standard, Google, Bedrock, Azure, and a doubled-price fast endpoint.
The exact Mythos5.2 ID was absent from that public catalog. Presence-only central
helper reports OpenRouter configured; it does not report/manage a direct
Anthropic provider, so direct credential absence is **not** established.
No owner credential inspected. **Access: unverified for both models.**

Proposed candidate path: OpenRouter's provider-native Messages surface where
the owner supports it, Anthropic **standard** endpoint, exact Fable5.2 only;
otherwise qualify the owner's existing adapter against native responses.
Pin this route for retention, pricing and reproducibility. No fast premium,
different-model fallback or implicit Mythos substitution. Candidate price
ceiling USD8/40 per MTok; exact native/schema/identity/usage qualification belongs
to selected Stage 2, never inferred from catalog metadata.

The ledger matches only Fable/Mythos5.1, not this new checkpoint. [Scout062](scout-062-claude-fable-mythos-51-evaluation.md)
records prior Doc Web contract/quality/value failure and explicitly permits an
exact new checkpoint. This proposal does not reinterpret that failure as5.2 data.

## Stable execution handles — Evaluate now

Each number selects all its listed independent tasks, with separate stop gates.
All use frozen eligible owner fixtures and fresh matched maintained controls.
Native contract probes should double as first scored cases when requests match.
Stop each arm at a valid decisive source/contract failure or hard value gate;
finish other selected independent tasks. These are exposed development screens,
not adoption qualification. No full-suite expansion or runtime routing change.
Freeze complete resolved matrix and reservation ledger before multicase calls.

1. **Doc Web — USD12 inclusive.** First `image-crop-extraction`, Image011 and
   Image001 only, vs exact maintained Gemini3 Flash Preview. High16384 total
   output for spatial fidelity. Require both source-valid, no schema errors,
   complete lettering/date/seal/signature preservation, score>=.95; a two-case
   pass does not establish the full13 gate. Independently one current
   neighboring-content `crop-page-level-deletion-gate` discriminator vs GPT5.5,
   high16384, zero false-safe; one authored synthetic bakery
   `literal-table-fidelity` case vs GPT6 Astra medium8192, high32768, exact clear
   glyph/cell ownership/spans and correct ambiguity holds; one maintained public
   LOC Barney `image-entry` handwriting page vs exact Gemini3.7 Flash,
   high32768, >=.99 with no invented/normalized words. Freeze current
   source-adjudicated truth; preserve historical scores/promotion holds rather
   than reviving contradictory captions/grouping policy. No paid judge.
   Source-fidelity failures in recent models make reduced manual cleanup the
   hypothesis, not cheaper tokens. Approximate maximum candidate reservations
   at input26K detector/table/OCR and46K safety: 2x.86336 +1.02336 +2x1.51872
   =USD5.78752. Reserve up to2 for fresh controls and4.21248 qualification/
   operational recovery. No remaining11 detector/21 safety/full table/OCR suite
   in this selection; those are later qualification if these discriminators pass.

2. **Dossier — USD18 inclusive.** `standalone-semantic-value`, Story184v4
   authored synthetic long-history-two-families/follow-1, full321KB frozen
   continuation vs fresh GPT6.1 Sol medium16384. High65536 allows thinking and
   a complete graph; test difficult documentary attribution/correction rather
   than a cheap short extraction. Require compilation, all five meanings,
   supported attribution/provenance/uncertainty and every emitted row reviewed;
   zero material errors. Two blind native Opus4.6 complete-source reviews,
   one saved-answer judge-repair reservation. Seek useful quality improvement,
   or >=30% subject cost/latency reduction at full meaning parity; cheaper
   tokens are not predicted. Conservative candidate330K-input/65536-output
   bound USD5.26144 per dispatch; two bound10.52288, Sol<=.56384,
   three judge bounds<=4.7076 leave2.20568 qualification/recovery.
   Native free counts should materially tighten byte-derived reservations.
   One exposed case cannot prove family-scale/private or independent quality.

3. **Board Game Ingester — USD7 inclusive.** `asset-orientation` four public
   CC0 native inputs pub001/012/013/014 vs Sol low2048; candidate low8192 for
   interactive quarter-turn recognition. Zero wrong automatic turns, correct
   ambiguity/equivalence holds, exact native inverse/hash/dimension/pixel
   receipts. Independently `physical-outline-retention` **source001 and006
   only**, candidate high32768 vs Sol low8192; zero material/rim loss and
   definite-background leakage, exact component/hole/contact/provenance checks.
   Recent challengers lose rims; improved safe coverage would reduce manual
   review. At <=26K input/call, four orientation plus two contour candidate
   reservations totalUSD5.18016; controls<=.50 and1.31984 operational headroom.
   Count actual inputs before admission; no private Brass/RoboRally scans.
   Remaining four contour sources and package/physical graduation omitted
   from this bounded screen; no contour fitting or regenerated source pixels.

4. **CineForge — USD5 inclusive.** `video-understanding` v4, **first authored
   synthetic five-JPEG dialogue case only**, vs fresh Sol6.1 low4096 and Luna6
   low1400 research references. High32768 for temporal/source-grounding ceiling;
   strict13-key schema, structural>=.70, rubric/combined>=.80, <=15s and
   <=USD.02 subject. Independent blind native Opus4.6 source-first reviews.
   Latest controls both miss full quality, so there is practical headroom even
   at higher price. Candidate <=106K-input/32768-output reserves2.15872;
   controls<=.10, three20K-input/8192-output judges<=.9144 leave1.82688 for
   qualification/recovery. Reuse the exact first native answer as scored
   response; another maximal candidate dispatch requires released usage-based
   headroom. No other five cases, native audio/video, private screenplay or
   shipped analyzer/autonomous-QA claim. One case can reject/prioritize only.

5. **Storybook — USD7 inclusive.** First `luna-persona` no-advice discriminator,
   then full12 synthetic turns in seven real reset groups1/1/1/1/3/3/2 only
   if first gates pass, vs Luna6 none512; fixed blind GPT5 original rubric.
   Candidate low8192 for responsive source-grounded voice, always-on thinking
   retained. Require all source/continuity/Inference Firewall/no-therapy
   assertions, <=5s and<=USD.01/turn. Quality benefit is uncertain: Luna12/12
   already passes the small panel. Independently photo FS001 thenFS006 vs
   Gemini2.5 Flash-Lite, low8192, actual prompt-only JSON/Zod contract,
   all assertions, <=5s and<=USD.001/photo. Field-placement raw failures are
   not automatically semantic gaps. Free exact-model input-cost admission
   first; no borrowing image-token counts from another model. If no conclusive
   offline exclusion exists, one native response measures actual cost.
   At <=8K input/persona,12 candidate reservations4.70016; two photo at<=26K
   input USD1.07136 total; controls/judge<=.80 leave.42848 recovery. (Photo total
   is USD1.07136, not a per-call estimate.) Tighten real rendered reservations
   before dispatch; stop economic failure before expansion. This is lower
   priority than the source-fidelity lanes, not an incumbent price contest.

6. **Echo Forge — USD4 inclusive.** First `control-intent-v1` admission slice
   001/016/006 only vs Gemini3.8 Flash low2048, candidate low8192. Strict native
   one-label schema, actual production system/state; no worse direct-control
   recall, negative false activation or ambiguity abstention, hard15s. Seek
   useful grounded quality or30% cost/latency improvement at parity. Remaining
   39 eligible cases omitted until useful admission evidence exists; six
   unsent-context exclusions stay excluded. Independently actual Story069
   scene-to-soundscape Tavern thenDungeon vs GPT5.4 Mini4000, low8192,
   full2/2 required semantics, <=USD.01 each, soft5s. Source-explicit required
   layer misses in recent models justify quality testing. No paid judge.
   Three intent at<=6K input +two scenes<=26K input reserveUSD2.1984;
   controls<=.10 leave1.7016 qualification/recovery. The repaired34-golden
   extractor lane is deferred pending fixture-by-fixture campaign provenance;
   old judge-defective rankings are not valid candidate evidence.

**Campaign maximum: USD53** (12+18+7+5+7+4). These are provisional operator
ceilings that become hard on selection, not expected invoices. No transfers
between owners. All include subjects, fresh controls, judges where specified,
qualification and bounded recovery; unknown charges retain full reservation.
Per-call value gates are separate from campaign reservation ceilings. If an
unrepairable hard boundary prevents a selected comparison, preserve the useful
work and concrete missing decision; do not claim a model-quality failure.

No within-task effort comparison is selected. Do not escalate effort to rescue
a valid failed arm. Later quality/economics calibration needs its own bounded
selection after evidence; lower/higher untested settings are not rejected.
Whole-workflow stage shares are unknown; report task cost/time and manual-work
implications without manufacturing application-wide savings.

## Not recommended now

Every remaining registered owner has one disposition:

- **Robo Rally — Do not evaluate:** deterministic rules/bots/replay contracts,
  no maintained hosted-model decision; private canonical rulebook ineligible.
- **Ultima IV Web — Do not evaluate:** original-game reconstruction, differential
  tests and browser controls are not a maintained hosted-model benchmark.
- **Financial Hub — Defer:** registered path absent; no eligible maintained
  synthetic lane established. Do not substitute Financial Data/Reporting or
  transmit consequential private records by implication.
- **Financial Monthly Analysis — Defer:** registered path absent, same ownership
  and private-source boundary; registry repair is separate work.
- **VLC Thumbs — Do not evaluate:** registered nested path absent; known native
  thumbnails/cache/bookmarks contracts do not evaluate this model.

Other tasks in positively recommended repos remain unmeasured:
Dossier broad C5 extraction has separate contracts and costly context; prioritize
the maintained long-history screen instead of a general tournament. CineForge
script-bible hardUSD.01/30s/.90 contract and corpus eligibility do not establish
a worthwhile Fable lane yet; ordered frames test a distinct quality gap.
Storybook diarization/embeddings require different API modalities; retired
Story160–162 raw-model selector lanes stay retired, Story094 needs supplied-memory
substrate, and private media/history need separate eligibility. BGI asset role/
matching/layout require their own eligible representative inputs; orientation and
scanner contours cannot qualify restricted full-game intake. Doc Web whole-book
HTML/reference resolution and caller grouping/automatic publication remain
separate contracts; reference resolution is deterministic, source grouping holds
are not waived by a detector screen. Echo audio generation is an output-modality
mismatch. Mythos5.2 is deferred across all owners pending verified entitlement
and a decision-bearing need for its different access/policy configuration;
no duplicate benchmark or verification-program application is proposed.

## Owner evidence used

- Doc Web `docs/evals/registry.yaml`, Attempt031 Fable5.1; current source-fidelity
  ownership and recent [Scout105](scout-105-hy4-ripple-evaluation-campaign.md).
- Dossier [Attempt040](/Users/cam/.codex/worktrees/hy4-ripple-20261105/dossier/docs/evals/attempts/040-ripple-long-history-20261105.md),
  full continuation and complete-source judge reservation precedent.
- BGI [public asset screen](/Users/cam/.codex/worktrees/hy4-ripple-20261105/boardgame-ingester/docs/evals/attempts/20261105-scout105-hy4.md).
- CineForge [Attempt056](/Users/cam/.codex/worktrees/hy4-ripple-20261105/cine-forge/docs/evals/attempts/056-hy4-ordered-frame-screen.md).
- Storybook [Attempt197](/Users/cam/.codex/worktrees/hy4-ripple-20261105/storybook/docs/evals/attempts/197-scout105-hy4-ripple-persona-photo.md).
- Echo [current intent/scene attempt](/Users/cam/.codex/worktrees/hy4-ripple-20261105/echo-forge/docs/evals/attempts/control-intent-v1/20261105-scout105.md),
  `docs/evals/attempts/20261024-harness-integrity.md` for repaired extractor.

These retained owner records supplement primary registries; they do not by
themselves establish landing/current runtime defaults. Stage2 must reconcile
current remote owner base and owner instructions before any calls. Fresh
isolated worktrees belong under `/Users/cam/.codex/worktrees/<task>/<project>`;
no new worktree was created in this recommendation pass.

Reply `yes` to run all numbered evaluations, or select a subset by number.
