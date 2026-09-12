# Scout 069 — Ling 3.0 Flash VL Evaluation Routing

Date: 2026-09-12
Status: Defer — no owner evaluation selected

## Verified candidate and route

The requested checkpoint is `inclusionAI/Ling-3.0-flash-VL`, distinct from
text-only Ling Flash, Fin, and Sante. No matching prior attempt was found in
the evaluated-model ledger or the seven owners' inspected documentation.

The [creator model card](https://huggingface.co/inclusionAI/Ling-3.0-flash-VL)
documents MIT weights, 124B total/5.5B active parameters, image/video/text input
and text output, up to 256K context, and self-hosted thinking/tool parsers.
Thinking defaults on; the local template supports `enable_thinking=false`.
That local control does not establish hosted control enforcement.

The selected route is OpenRouter Chat Completions at
`https://openrouter.ai/api/v1/chat/completions`, request model
`inclusionai/ling-3.0-flash-vl`, pinned to DeepInfra FP16 because route contract
and price matter. The public [endpoint catalog](https://openrouter.ai/api/v1/models/inclusionai/ling-3.0-flash-vl/endpoints)
maps it to `inclusionai/ling-3.0-flash-vl-20260910`: 131,072 context, 32,768
maximum completion, US$0.06/M input, $0.18/M output, $0.012/M cached input.
It advertises reasoning, structured outputs, response_format, and forced/named
tool choice. This is catalog checkpoint attribution, not response-proven revision.

[DeepInfra's direct API](https://deepinfra.com/inclusionAI/Ling-3.0-flash-VL/api)
also lists the model. Its [schema documentation](https://docs.deepinfra.com/chat/structured-outputs)
describes strict JSON Schema enforcement. Exact owner schema enforcement and
hosted reasoning settings still require qualification. Freeze one provider-valid
arm before scoring; prefer a documented instant/off mode for interactive lanes
only if the exact route supports it, and do not silently change modes after a miss.

The [free Novita route](https://openrouter.ai/inclusionai/ling-3.0-flash-vl:free)
has 262K context but does not advertise response_format; it is not a substitute
for this strict-contract proposal. No account creation or self-hosted deployment
is proposed.

Announced: yes. API-listed: yes. **Access: unverified.** No credentials were
read, authenticated probes made, or target repositories changed. Reliability,
capability and actual economics remain unmeasured; no adoption verdict exists.

## Payload boundary

[DeepInfra policy](https://docs.deepinfra.com/account/data-privacy) describes
ordinary inference in memory and no training, but reserves limited content
logging for debugging/security. Do not describe this as unconditional ZDR.
OpenRouter/account-specific retention settings remain unverified. This proposal
uses only owner-established public or synthetic fixtures and explicitly accepts
that residual logging uncertainty; ZDR is optional unless current owner policy
requires it. Private family photos/documents, scans and licensed material are
excluded. No provider-account settings may be changed.

## Proposed lanes, deferred

All caps include probes, bounded diagnostics, retries, subjects, controls and
judges. Stop before any call whose conservative maximum exceeds the balance.
Use isolated current-base owner worktrees; preserve prompts, goldens and scorers.
First qualify exact identity, terminal response, native modality/output contract
and harness parity. A single safe diagnostic relaxation after a strict failure
may isolate capability, but cannot count as production parity or unlock a full
adoption comparison. Zero-cost resolved-matrix preflight precedes multi-case work.

1. **Doc Web — Evaluate now; US$0.50 ceiling.** First lane:
   `image-crop-extraction`, frozen `conservative-count` prompt. Start with the
   Image011 seal/signature grouping differentiator after synthetic strict-image
   qualification, then the maintained 13-case detector only if it passes.
   Require 13/13, overall >=0.95 and zero transport/schema errors. Runtime
   incumbent is `gemini-3-flash-preview`; maintained reference is 13/13 at
   0.9703. Run a fresh same-input incumbent only after candidate qualification
   and budget preflight to assess quality/latency/cost value. Native layout
   understanding at this price is a credible lower-cost crop challenger.
   Fixtures are owner-identified public benchmark images. This selection is
   detector-only: page-context GPT-5.5 safety, production crop exclusion, and
   selection-exposed validator corpora remain separate, unmeasured boundaries;
   no detector result alone authorizes replacement or removal of safety logic.
2. **Storybook — Evaluate now; US$0.10 ceiling.** First lane:
   `story056-photo-understanding` (`pnpm test:eval:story056:photo`), FS-001
   photo and FS-006 scanned document. Both have explicit synthetic provenance
   and actual PNG inputs. The shipped incumbent is `gemini-2.5-flash-lite`;
   prior clean runs scored 1.0 at about 2.3–2.9 seconds, $0.000150/run.
   Require every OCR/grounding/follow-up assertion, pass rate 1.0, latency
   <=5 seconds and cost <=$0.001 under owner metric semantics. Qualify one
   image through an isolated provider adapter; stop at first hard miss, then
   finish both fixtures and a fresh incumbent only if candidate passes.
   The hypothesis is cheaper grounded photo/OCR with preserved interaction
   speed. The current binding is Google-native JSON MIME plus local Zod;
   preserve its actual prompt/image/schema semantics. Passing establishes an
   adapter-required challenger, not a drop-in runtime replacement or privacy
   clearance for real family uploads. Broader evidence-fusion remains unmeasured.
3. **CineForge — Evaluate now; US$0.75 ceiling.** First lane:
   repaired `video-understanding`, five ordered JPEGs per case. Start with
   `dialogue_confession_push_in`; continue to six active cases only after
   strict frame-packet parity and a passing anchor. Keep all deterministic and
   rubric hard gates, overall >=0.80, <=15 seconds and <=$0.02 subject cost/case.
   Include the maintained Opus 4.6 judge in preflight and spend accounting.
   Current decision-grade Gemini 3.6 Flash / 3.5 Flash-Lite rows are 0.4397 /
   0.4071 and support HOLD, leaving substantial useful headroom for a native
   visual reasoner. They do not support fine ranking: known conservative
   matcher defects need classification if decision-bearing for Ling. Stop on
   ambiguity rather than changing the scorer to rescue it. Use a fresh Gemini
   3.5 Flash-Lite control if advancing to a current comparison. All six assets
   are explicitly project-owned synthetic controls; no audio, screenplay,
   transcript, semantic title or MP4 goes to subject or judge. This tests frame
   QA, not native-video or audio understanding, and cannot activate QA by itself.

**Campaign maximum if reopened: US$1.35.** Cam deferred the full proposal on
2026-09-12. No repository evaluation, provider call, credential access, worktree
creation, or spend was selected or performed. Reopen only with a new explicit
selection; recheck the exact endpoint, owner contracts, fixture eligibility and
prices before treating these lanes or ceilings as current.

## Not recommended now

| Owner | Disposition | Reason |
| --- | --- | --- |
| Dossier | Defer | Maintained extraction is text-based; C5 value work is on hold amid identity/runtime work. No stronger current visual decision was established. |
| Echo Forge | Defer | Maintained scene-to-soundscape eval is text-only; prospective image intake has no maintained image fixture lane. A generic text tournament is lower priority than the three visual decisions. |
| Board Game Ingester | Defer | Asset orientation is promising, but current Robo Rally scan fixtures lack provider-upload eligibility; Story015 excludes paid/private uploads and a VLM subject adapter is absent. |
| Robo Rally | Do not evaluate | Deterministic game/scenario goldens, no maintained model-owned runtime slot; private rulebook is outside this scope. |

## Owner evidence inspected

- Doc Web: `docs/evals/registry.yaml`, `docs/runbooks/crop-eval-workflow.md`,
  `benchmarks/tasks/image-crop-extraction.yaml`, Attempt025, local evaluate-model.
- Storybook: `docs/evals/registry.yaml` Story056; executable photo eval and
  `packages/backend/src/ai/photo-understanding.ts`; photo prompt/model binding;
  both fixture `notes.md` files and PNGs under `tests/fixtures/golden/`.
- CineForge: `docs/evals/registry.yaml` video-understanding; task, report,
  `benchmarks/video_understanding/README.md`, active asset metadata, local skill.
- Dossier: AGENTS, Ideal/spec/state, registry, local skill and active work context.
- Echo Forge: AGENTS, Ideal/spec, registry and local evaluate-model skill.
- Board Game Ingester: AGENTS/spec/state, Story015 and asset-orientation registry.
- Robo Rally: AGENTS private-input boundary, Ideal/spec and deterministic registry.

Owner paths are resolved by `projects.yaml`. Primary-checkout state may lag
remote execution bases; recheck current owner contracts before spending and
surface material scope changes. The watch discovery remains untouched; this
proposal adds full portfolio routing. Ledger remains unchanged until execution.
