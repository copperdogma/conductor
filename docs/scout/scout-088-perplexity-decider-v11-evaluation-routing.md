# Scout 088 — Perplexity Decider v1.1 versus Jev/OpenAI Decisions

Date: 2026-10-06 (America/Edmonton)
Status: Completed — four approved owner comparisons; no promotion

Cam's new entry: “Perplexity open weights Decider v1.1. Check that vs
Jev/OpenAI decider via evaluate-model.” This preserves a narrow decision-model
comparison. No authenticated discovery, credential inspection, provider probe,
paid inference, target mutation, commit, push or runtime change in Stage 1.
Conductor's dirty shared checkout is preserved. An economical read-only worker
inspected seven other registered owners; root inspected the four maintained
comparison owners and their latest isolated attempts.

## Verified public identity and contract

- Candidate: provider-qualified `perplexity-ai/pplx-decider-v1.1-27b`, native
  hosted ID `pplx-decider-v1.1-27b`, distinct from `pplx-decider-v1-27b` and
  Mapika's unrelated Decider family. Announced/open release and API-listed:
  **yes**. Owner/account callability: **access unverified**.
- [Official model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b):
  Apache 2.0 Qwen3.8-27B-derived decision checkpoint. Publisher reports Decision
  Index61.56 versus Jev57.9 (v1:56.4); this is a publisher benchmark, not local
  task superiority, and its Jev comparator is not proven identical to our
  pinned `jev-1.13.0`. Knowledge remains below the published Jev score.
- Public unauthenticated [Hub metadata](https://huggingface.co/api/models/perplexity-ai/pplx-decider-v1.1-27b)
  returned private=false/gated=false, revision
  `3b45dead91dfa6d95aad6b95764a606fab2bf7a6`, modified2026-10-05T17:00:35Z,
  with11 backbone Safetensors shards. No weights downloaded. The model card's
  private-repository usage wording conflicts with this current metadata;
  metadata establishes public listing, not a successful full-weight download.
  Local native serving needs about49GiB weights plus workspace, its separate
  readout, saved noncausal full-attention behavior and calibration applied once.
  A generic causal generation export is not checkpoint parity. No local GPU
  deployment, weight download or self-hosting experiment is proposed here.
- [Official native API](https://docs.perplexity.ai/api-reference/decisions-post):
  `POST https://api.perplexity.ai/v1/decisions`, explicit exact model,
  state plus named questions; Noul, Choice, ordered Score; typed probabilities,
  no generated explanations, tools, custom schema or reasoning-effort knob.
  Text/JSON and inline PNG/JPEG/WebP images;1–128questions, up to255Choice
  options, input under262144tokens/body32MiB. Response model is an echo, not
  cryptographic proof of hosted weight revision; record this identity limit.
- [Quickstart](https://docs.perplexity.ai/docs/decisions/quickstart) and
  [pricing](https://docs.perplexity.ai/docs/getting-started/pricing):
  **USD0.02/M input**, free output/no request fee. Do not reuse older v1
  USD0.04/M claims. Per-image limit2048tiles of32×32; oversized input may time
  out rather than reject promptly. Treat tile admission as zero-cost preflight.
- [Perplexity privacy](https://docs.perplexity.ai/docs/resources/privacy-security)
  explicitly scopes no-training/ZDR to Chat Completions; this does **not** prove
  Decisions endpoint coverage. Hosted Decisions retention/training/ZDR remains
  unverified. Only explicitly synthetic inputs are proposed. Selection accepts
  this disclosed uncertainty for those synthetic fixtures; private/unclear
  payloads remain excluded, and stricter owner policy prevails.
- [Jev current models](https://docs.typesafe.ai/models): pinned `jev-1.13.0`,
  `POST https://api.typesafe.ai/v1/systemone`, text-only Noul/Choice/Score,
  USD0.042/M input/free output. No customer-request training; enterprise ZDR
  available, account activation unverified. No image arm or OCR workaround.
- [OpenAI Decisions](https://developers.openai.com/api/docs/guides/decisions):
  native `gpt-6-luna` public beta, predicate/Choice/Score, text/inline images,
  USD0.10/M input/free output, eligible ZDR. No generated rationale. Its native
  payload differs from Perplexity/TypeSafe: preserve semantics, adapt only the
  provider envelope. Public docs fetched live through official OpenAI Docs.

Perplexity's nominal input rate is80% below OpenAI Decisions and52.4% below
Jev. Tokenizers, image accounting, latency and downstream fallback determine
actual task economics. Typed answers/confidence do not establish correctness
or interchangeable confidence calibration. No overall workflow saving is known.

## Ledger and recent owner evidence

Read docs/model-watch/evaluated-models.md before routing: no exact Perplexity
candidate attempt found. Jev and OpenAI Luna have prior attempts. Their fresh
arms below are **explicitly requested comparator re-evaluations**, not newly
nominated models, checkpoint improvements or retries to rescue prior losses.
Preserve original evidence and fresh run identities; no unchanged independent
Responses tournament or broad same-model rerun is proposed.

[Scout086](scout-086-openai-decisions-api-evaluation-routing.md#completed-owner-decisions--2026-10-06)
records current exact-owner results, independently read here:

| Owner evidence | Most recent bounded outcome |
| --- | --- |
| [Storybook Attempt178](/Users/cam/.codex/worktrees/decisions-storybook-20261006/docs/evals/attempts/178-story150-decisions-native-relative.md) | OpenAI/optimized Haiku routing24/24 each; complete cascade/full20/24 each;12.19% task savings but8.90% worsep95. Story191 integration is isolated/default-off/unlanded. Earlier Jev Attempt159 routing24/24; not a fresh three-way comparison. |
| [Echo control](/Users/cam/.codex/worktrees/decisions-echo-20261006/docs/evals/attempts/control-intent-v1/20261006-openai-decisions.md) | OpenAI37/48 vs Gemini45/48, false controls7vs2; retain Gemini. Historical Jev30/48 remains a dated reference. |
| [Doc Web Attempt063](/Users/cam/.codex/worktrees/decisions-docweb-20261006/docs/evals/attempts/063-decisions-api.md) | Text OpenAI22/40 vs GPT4.1 28/40; false-clean4vs2. Historical Jev24/40. Real OpenAI cascade30/40 with3false-clean. Retain incumbent. |
| [Board orientation](/Users/cam/.codex/worktrees/decisions-boardgame-20261006/docs/evals/attempts/20261006-decisions-orientation.md) | OpenAI1/3 vs Sol3/3, two source-confirmed rotation errors;11cases unmeasured after stop. Retain Sol. |

## Stable execution handles — Evaluate now

All caps include candidate/comparator qualification, subjects, real fallbacks
where specified, and bounded operational recovery. No paid judges: independent
source-based review plus maintained deterministic scorers. Caps are provisional
operator proposals, becoming hard on selection. Zero-cost resolved-matrix,
prompt/hash/topology/reservation preflight precedes paid batches. Recover soft
adapter faults within cap; no semantic retries, threshold fitting or golden
changes. Run independent owner subagents in isolated current-base worktrees.

1. **Storybook — USD3.** First Story150/167 relationship-correction routing:
   Attempt159's12fictional synthetic cases×2. Fresh Perplexity v1.1 versus
   Jev1.13 and OpenAI Decisions Luna, optimized Haiku routing and full Haiku
   interpreter. This can choose a finite early-exit component; full rationale,
   correction generation, permissions/confirmation/mutation stay with code and
   incumbent. No Story191 activation or overwrite of its existing worktree.
   Start exact contract/consumed-question qualification, then identity/action/
   ambiguity/confirmation cases; stop on invented ID, wrong target or unsafe
   action. Preserve frozen policy (.8 where already required, safe confirmation
   exception); do not claim .8 transfers calibration across providers.
   Measure false acceptance, fallback coverage, matched routing and complete
   cascade quality, actual cost/latency. Only safe noops avoid full Haiku.
   Target no worse complete quality/cost and >=30% lower routingp95 against a
   fresh comparator; if both fast models tie, require measurable full-task
   value rather than promoting nominal token-price savings. Existing request
   envelopes reserve the original75-call comparison matrix underUSD1. Budget
   another equivalent full-fallback envelope for each additional decision arm;
   extra typed calls are small, leaving operational headroom underUSD3 after
   exact matrix admission. Shared full outputs can supply baseline scoring,
   but real per-arm sequential fallbacks are required for actual cascade timing;
   reconstructed timing must be explicitly labeled. Only synthetic fixtures;
   disclosed Perplexity retention uncertainty, no private family records.

2. **Echo Forge — USD1.** First `control-intent-v1`,48frozen synthetic cases:
   20controls/22noncontrols/6ambiguous. Fresh Perplexity versus Jev and OpenAI
   Decisions, plus Gemini3.8Flash low incumbent. Native qualification then
   negation/quotation/conditional/no-action screen; invalid contract stops the
   affected arm, valid semantic misses remain in the full diagnostic cohort.
   Preserve owner relative-value rule: no worse false activations/control recall
   than fresh incumbent and >=30% lowerp95 is a promotion screen, not a claim
   that faster wrong labels win. Report ambiguity and paired correctness.
   The48diagnostic and later42runtime-shaped inputs are separate; no playback,
   soundscape generation or runtime generalization. Gemini48 at8192input/
   2048output reservesUSD0.663552 at0.75/3.75 perM; three typed48-case arms
   reserveUSD0.063700992 at0.02/0.042/0.10, sumUSD0.727252992, leaving
   USD0.272747008 for probes/recovery. Source-stage share of whole soundscape
   cost unknown; plausible payoff is less control latency at equal quality.
   Synthetic only; Perplexity retention/training uncertain and disclosed.

3. **Doc Web — USD2.** First Story233 `jev-consistency`,20unique synthetic
   cases on2sources×2, five labels. Fresh Perplexity/Jev/OpenAI Decisions versus
   pinned GPT4.1 projection and maintained deterministic references. Preserve
   exact conventions, hashes, scorer and each frozen cascade policy:
   uncertain→review, otherwise confidence<.8→actual GPT4.1 fallback; no fitting
   thresholds to exposed cases. Qualify native contract, then full40judgments
   even with semantic misses under owner plan. Compare false-clean, per-class
   recall, review coverage and whole cascade cost/latency; require fewer
   dangerous misses or no worse misses with useful economics. No invented
   perfection/50% threshold; no convention-generation/repair/rationale parity.
   GPT4.1 baseline40 plus at most120fallbacks at4096input/160output reserves
   USD1.51552 at2/8 perM. Typed120calls reserveUSD0.02654208; sumUSD1.54206208,
   leavingUSD0.45793792 for qualification/recovery. Existing synthetic fixture
   source classes verified; no private genealogy upload. Whole-pipeline stage
   share unknown, so no total pipeline-saving claim.

4. **Board Game Ingester — USD1.** First `asset-orientation` on
   `synthetic-orientation-v1`:14authored images,12determinate plus symmetry and
   ambiguity hold. Fresh Perplexity versus OpenAI Decisions and Sol/low;
   provider-free blind baseline. Jev excluded because text-only. Qualify image
   Choice rotation0/90/180/270/unknown, then differentiators012/006/010 plus
   hold gates, full14only if eligible. Stop affected candidate on a
   source-confirmed rotation/safety miss; finish independent surviving arms.
   Require12/12rotations and both hold gates, exact inverse/pixel/hash/
   provenance/no-downsample proof; target>=30% lessp95 or full-stage cost at
   equal quality. Fourteen related synthetic designs cannot establish broad
   real-source quality. No generated visual reason is supplied by either
   decision model; benchmark provenance is not an invented rationale.
   Sol14 at4096input/2048output and conservative cache-write price reserves
   USD0.43008; both decision arms reserveUSD0.00688128; sumUSD0.43696128,
   leavingUSD0.56303872 for probes/recovery. All14original PNGs verified by
   native headers: dimensions97–192pixels, maximum30tiles, unchanged inputs fit
   Perplexity's2048-tile limit. No private game scans, deskew or source roles.

**Campaign maximum: USD7.** No local GPU rental, model deployment or download.
Current paid spendUSD0. Fresh comparator arms answer Cam's requested new
candidate comparison; unchanged previous evidence remains separate. Previously
exposed corpora are bounded screens, not fresh held-out validation. Any later
promotion requires the complete owner contract and independent coverage.

## Not recommended now

| Registered owner | Disposition and reason |
| --- | --- |
| Dossier | **Defer.** Same/different identity stage-judge and acquaintance-pair judgment are plausible finite seams, but extraction F1 is not their semantic benchmark. No separately maintained eligible candidate-level oracle found; private/licensed oral history and script inputs need owner classification. Do not send a full graph or treat extraction replacement as a decision-model lane. |
| CineForge | **Defer.** Entity-verdict subcalls lack independent gold and still require incumbent canonicalization/rationale; maintained extraction and ordered-frame tasks generate names/descriptions/claims. No eligible finite-decision benchmark/payoff established. |
| Robo Rally | **Do not evaluate.** Deterministic rule legality/simulation; no maintained tactical decision-model benchmark, private original manual. |
| Ultima IV Web | **Do not evaluate.** Source recovery/runtime fidelity/admission, no maintained external decision-model runtime task. |
| VLC Thumbs | **Do not evaluate.** Deterministic decode/cache/scheduler/bookmarks; owner says model eval dormant because no AI requirement. |
| Financial Hub | **Defer.** Private household context, no maintained synthetic finite-decision benchmark or Decisions-qualified privacy policy. |
| Financial Monthly Analysis | **Defer.** Transaction suggestions are a conceivable seam, but no maintained synthetic benchmark; source/owner-confirmed private evidence cannot be sent to an unqualified new provider. |

Additional matching-task omissions inside recommended owners:

- **Doc Web crop-page-level-deletion-gate: defer for input-contract mismatch.**
  Local read-only dimension check of Attempt063 image-eligibility manifest found
  all22source pages at1505×2000or1545×2000. They exceed2048tiles even with
  nearest rounding;42of44source/crop image occurrences exceed a conservative
  ceil-tile limit. Resizing changes maintained pixels/context and requires a
  separately frozen matched adaptation; do not silently downsample or pay to
  rediscover the documented timeout. Bounding boxes/OCR need generated values;
  layout classification lacks an enabled measured decision lane.
- Board Game source-role routing/count/grouping and deskew need other contracts
  and private fixtures. Orientation approval does not cover them.
- Storybook photo/OCR/persona need generated outputs; identity merges lack an
  independently reviewed false-merge lane. Optional retrieval reranking has
  no new representative payoff evidence after anchor rescue.
- Echo scene-intent full proposal remains NO-GO after prior candidate/context
  limitations: local repaired baseline4/7useful vs Jev2/7 with14/16review. Do not
  repeat a label-only comparison and imply full-proposal improvement.
- Conductor itself: **Defer**, no maintained labeled high-volume runtime lane.

## Validation and next action

Claims checked against live official pages, current central ledger, owner
attempts and maintained plans. Public Hub metadata and local image-header/
manifest admission checks are read-only and zero-provider-spend. Documentation
only: inspect links, routing coverage, arithmetic and scoped whitespace; no
product suite or paid benchmark needed. Evaluated-model ledger remains unchanged
until a selected owner reaches authenticated qualification/stop.

Reply `yes` to run all four numbered evaluations, or name a subset.
The evaluate-model skill explicitly requires Stage1 selection before paid owner
execution; this is the only pending authorization, not a runtime rollout request.

## Approved execution — 2026-10-06

Cam replied `yes`, selecting all four positive items, inclusive hard caps:
Storybook USD3, Echo Forge USD1, Doc Web USD2, Board Game Ingester USD1;
combined maximum USD7. Four isolated owner workers were dispatched before any
root provider call. Existing owner credentials take precedence. Presence-only
central helper status/check passed: TypeSafe is configured, Perplexity is not
a supported/configured central provider. No secret values inspected or copied.
Owners check their own ordinary credential configuration; no unrelated owner
credential discovery or provider substitution. Candidate access missing in an
owner prevents paid incumbent-only work, while zero-cost preparation continues.
Full portable custody and owning-repo protocols read by coordinator; workers
must read owner-specific instructions and preserve privacy, contracts, frozen
inputs, safe raw evidence, reservations and independently surviving lanes.
No defaults, deployment, landing, commit or push authorized.

### Credential search authorized by Cam

When missing access was reported, Cam explicitly authorized searching
`/Users/cam/Documents/Projects` and using an existing key for evals if found.
Coordinator searched280 env/credential candidate files and311066 text/config/
source files, excluding Git internals, dependency/build/cache/output directories
and large/binary inputs. No populated Perplexity/PPLX key assignment or
Perplexity-format credential literal found. Only two third-party dependency
provider-variable references were found; neither contained a credential.
No values printed, fingerprinted, copied, imported or modified. This bounded
filesystem search does not prove absence from keychains, browsers, encrypted
stores, excluded dependency caches or locations outside the requested folder.
The provider/account remains access-unverified; a missing local credential is
not provider rejection. Existing central TypeSafe is available for later narrow
injection; no injection is useful until the common candidate key exists.

### Verified isolated bases

| Owner | Worktree / branch suffix | Fresh origin/main base | Hard cap |
| --- | --- | --- | --- |
| Storybook | `pplx-storybook-20261006` | `d9cb51527e4e5b16a3e406617da8e72caf1f1ba2` | USD3 |
| Echo Forge | `pplx-echo-20261006` | `69631247146c0a9770a02e2ddd71c4d88628a901` | USD1 |
| Doc Web | `pplx-docweb-20261006` | `19b30b1d0db4a7f3b2e31614ba9846dfdb93355c` | USD2 |
| Board Game Ingester | `pplx-boardgame-20261006` | `ff1a9fe799744ac82ff8aca4b73301826c358600` | USD1 |

Paths are under `/Users/cam/.codex/worktrees/`, branches use `codex/` plus the
listed suffix. Coordinator verified HEAD and branch directly. Storybook's
fresh base already includes landed/default-enabled Story191; the earlier Stage1 “unlanded”
snapshot is superseded by current owner base evidence. This campaign does not
activate or modify its runtime route; the frozen comparison policy remains
explicitly separate from current integration state.

## Owner preparation and access stop — 2026-10-06

**No new task winner measured.** Keep current owner defaults pending candidate
access. All four selected owners completed useful zero-cost preparation and
documented the missing local candidate credential. No authenticated probes,
provider calls, subject/fallback/judge/retry charges or unknown exposure occurred.
Actual spend **USD0/7**, all caps remain reserved authorizations, not charges.
This campaign is incomplete; it did not evaluate Decider's semantic quality.

| Owner/task | Fresh comparison result | Preparation and validation | Owner authority |
| --- | --- | --- | --- |
| Storybook relationship routing | Not measured; current route retained |12unique×2, three typed arms plus optimized/full Haiku and actual per-arm fallbacks; inclusive reservationUSD2.01966676/USD3.19focused tests, scoped lint, methodology/privacy coverage and whitespace pass. | [Attempt179](/Users/cam/.codex/worktrees/pplx-storybook-20261006/docs/evals/attempts/179-story150-perplexity-native-comparison.md), [report/resume](/Users/cam/.codex/worktrees/pplx-storybook-20261006/docs/evals/artifacts/story150-perplexity-20261006/report.md), [manifest](/Users/cam/.codex/worktrees/pplx-storybook-20261006/docs/evals/artifacts/story150-perplexity-20261006/preparation-manifest.json) |
| Echo control intent | Not measured; Gemini retained |48unique synthetic diagnostic inputs×4arms,196planned calls including qualification; initial reserveUSD0.649050446+USD0.15recovery/USD1.12mocked tests including full simulated replay, scoped lint/freeze/methodology/whitespace pass. | [Owner attempt](/Users/cam/.codex/worktrees/pplx-echo-20261006/docs/evals/attempts/control-intent-v1/20261006-perplexity-decider-v11.md), [manifest](/Users/cam/.codex/worktrees/pplx-echo-20261006/docs/evals/attempts/control-intent-v1/20261006-perplexity-decider-v11.manifest.json) |
| Doc Web consistency | Not measured; current defaults retained |20unique×2, four native arms plus actual fallbacks; reservationUSD1.26000106/USD2.10focused tests, Ruff, methodology/whitespace and missing-key-before-network check pass. | [Attempt064](/Users/cam/.codex/worktrees/pplx-docweb-20261006/docs/evals/attempts/064-perplexity-decider-v11.md), [manifest](/Users/cam/.codex/worktrees/pplx-docweb-20261006/docs/evals/evidence/064-pplx/manifest.json) |
| Board Game orientation | Not measured; Sol retained |14synthetic images×3arms,42rendered native bodies; unchanged PNG bytes, max30tiles; reserveUSD0.43696128/USD1.46focused tests, compilation/lint/methodology/whitespace pass. Blind baseline3/12determinate,1/1symmetry,0/1ambiguity,14/14pixel proofs is provider-free setup evidence, not candidate quality. | [Owner attempt](/Users/cam/.codex/worktrees/pplx-boardgame-20261006/docs/evals/attempts/20261006-perplexity-orientation.md), [manifest](/Users/cam/.codex/worktrees/pplx-boardgame-20261006/benchmarks/results/synthetic-orientation-v1/20261006-perplexity/manifest.json) |

Layered verdict common to four owners: public exact model/API listing verified;
account **access unverified / local credential prerequisite missing**; live
transport/reliability/capability/economics **not measured**; adoption **defer**.
No cost/latency/pass-rate table can honestly rank these models without inference.
Earlier owner wins/losses stay historical, not fresh three-way evidence.

Coordinator directly verified branches/bases and all owner manifest hashes/sizes:
Storybook19entries, Echo12source entries, Doc Web24files, Board Game62entries.
Storybook manifest SHA256a097798fc4b492b8f5efbbc9844d72cfa1644fdaf5ace7dbacfb25bd9907d4e6;
Doc Web ff891ad8a9e083d7be4690cb0fafd183e4e4e76d72fcb7a393334c736538a54e.
Echo live replay correctly has no native freeze/response evidence yet; its
complete mocked replay is explicitly local harness validation, not live proof.
Root review corrected Echo's Perplexity Noul adapter to preserve documented
criteria fields directly, before any calls. Maintained .2/.8 Noul mapping is
separate from OpenAI Choice; neither identical wire contract nor shared
confidence calibration is claimed. No product/scorer/golden changes.

Storybook's current minimized mode-only runtime is distinct from this approved
frozen full-state/multiquestion comparison. Its current Story191 status is
landed/default-enabled, superseding Stage1 dated evidence. A screen win would
not itself qualify minimized-runtime replacement or private-data use. Owner
privacy review expiration is preserved; only fictional synthetic cases allowed.

No owner primary writes, default changes, service activation, deployment,
commits or pushes. No temporary key injected; cleanup not applicable in every
owner. Durable preparation remains uncommitted in the listed worktrees.
Central evaluated-model ledger now records the documented zero-spend owner
access stops so future discovery does not nominate an unchanged duplicate.

**Only missing next input:** provide a Perplexity eval key through protected
local configuration, then tell the coordinator only its env-file path and
variable name. Never paste its value into chat. Existing central TypeSafe can
then be temporarily injected through the custody helper; preserve original
owner keys and remove temporary variables after execution. A new central
Perplexity import still requires explicit provisioning authorization; direct
authorized protected owner use does not require centralization. Existing
selection remains sufficient for these exact lanes/caps; no repeat scope
approval is needed. Refresh current provider prices/contract and recheck
preflight source hashes before resuming, without rerunning unchanged preparation.

## Credential provision and approved continuation — 2026-10-06

Cam supplied a dedicated evaluation key in Conductor's ignored mode0600 `.env`
as EVAL_PERPLEXITY_API_KEY, then said ready. Coordinator checked presence only,
added Perplexity's designated name to the custody helper, passed all7existing
helper tests, and imported only the selected variable into the protected central
vault. Vault check passed; no values/fingerprints/headers printed. Source `.env`
is preserved. This explicit provisioning supersedes the earlier missing-key stop.

Temporary ignored owner variables injected through the helper, with no overwrite:
Storybook `.env.local`:PERPLEXITY_API_KEY/TYPESAFE_API_KEY; Echo `.env.eval`:
PERPLEXITY_API_KEY/TYPESAFE_API_KEY; Doc Web `.env`:DOC_WEB_PERPLEXITY_API_KEY/
DOC_WEB_TYPESAFE_API_KEY; Board Game `.env`:PERPLEXITY_API_KEY. Original owner
OpenAI/Anthropic/Google credentials remain owner-local. Root will remove only
these temporary variables after completion or stop and verify absence by name.
All four owner workers resumed before any coordinator provider call; no duplicate
root model calls. Original hard caps3/1/2/1, totalUSD7, remain unchanged.
Prepared source/matrix hashes and current official contracts/prices are rechecked
before native qualification. No private/default/deployment/landing authorization.

## Completed paid comparisons — 2026-10-06

**Prioritize an independent Doc Web consistency promotion check for Decider;
retain current Storybook/Echo/orientation models.** Perplexity is a qualified
low-cost text decision primitive, not a universal winner over Jev or OpenAI.
All candidate/native comparator contracts qualified in the four owner contexts.
Exact native requested/reported IDs retained; Perplexity model echo establishes
API contract identity, not an immutable hosted weight hash. Only approved
synthetic data used; no paid judges, defaults, deployment or landing.

| Owner/task | Fresh matched quality | Task cost and p95 | Recommended action |
| --- | --- | --- | --- |
| Storybook routing,12unique×2 | All three typed routes and optimized Haiku24/24. Full cascades Perplexity22/24,Jev22/24,OpenAI20/24; fresh full Haiku21/24. Cascade errors belong to generated fallback confirmation/schema behavior, not invalid native decisions. | PPLX cascadeUSD0.07019548/4974ms; Jev0.070445908/4606ms; OAI0.0817282/4703ms; fullHaiku0.091106/4372ms. Routingp95 PPLX733/Jev709/OAI326/Haiku2469ms. | No compelling Perplexity replacement:0.36%cascade saving vsJev with slower tail is negligible and exposed12case screen is small. Retain current route; measured full-state/multiquestion lane does not qualify replacing current minimized mode-only runtime. |
| Echo control intent,48unique | PPLX35/48,Jev31/48,OAI37/48,Gemini45/48. PPLX/OAI/Gemini20/20controls recalled; Jev15/20. False controls2/1/7/2; correct ambiguous abstention1/4/2/5 of6. PPLX abstains on6clear negatives. | Subject USD/P95ms: PPLX0.00030456/706; Jev0.001107582/382; OAI0.0022873/300; Gemini0.03693375/6123. Two Gemini503s recovered, charges conservatively unresolved separately. | Retain Gemini overall:10paired correctness losses and0wins for PPLX despite passing predeclared false-control/recall/latency screen. PPLX is the cheapest full-recall typed candidate here; ambiguity/review coverage prevents blanket adoption. No unmeasured fallback policy promoted. |
| Doc Web consistency,20unique×2 | Raw PPLX28/40,Jev24/40,OAI22/40,GPT4.1 30/40. Cascades PPLX30/40,Jev32/40,OAI30/40; confirmed defects calledclean4/4/2 versusGPT4.1 4. | PPLX+GPTcascadeUSD0.00252668/569ms; Jev+GPT0.0196836/975ms; OAI+GPT0.0303968/1276ms; GPT4.1alone0.043376/834ms. PPLX2actual fallbacks,Jev17,OAI26. | PPLX measured economics winner against GPT narrow projection:94.18%cheaper/31.85%faster at same aggregate75%accuracy and4confirmed-defectfalsecleans. Prioritize independent shadow/full-path promotion check, not automatic planner replacement: uncertainty failures differ and no generated rationale/conventions/repair parity. Jev has best cascadeaccuracy/uncertaintyrecall; OAI fewest confirmed-defectfalsecleans but slower tail. |
| Board Game orientation,2matched then stop | PPLX1/2,OAI1/2,Sol2/2; both decision arms fail source-confirmed DOCK case012. Remaining12candidate images/hold gates not measured. Surviving Sol finishes12/12determinate+symmetry1/1+ambiguity1/1. | Matched2: PPLXUSD0.00001524/433ms,OAI0.0000672/932ms,Sol0.00318/5451ms. FullSol14cost0.02437/p956723ms, not a matched14candidate comparison. | Reject both decision primitives for this unchanged rotation lane; retain Sol. Faster/cheaper choices fail quality. Sol DOCK→DOWN rationale typo preserved separately: rotation passed, explanation accuracy not promoted. |

Costs above exclude qualification overhead and unknown failed Gemini attempts.
All cascade calls were real serial fallbacks, not a post-hoc free simulation.
Latency is measured request/cascade latency in these owner runs, not production
throughput or whole-product time. Same inputs/prompts/criteria/goldens/scorers
frozen before inference; provider envelope/native primitives differ as recorded.
Two repeats in Storybook/Doc Web are not independent source expansion, and all
corpora were previously exposed. No threshold fitting, semantic retry or subset
selection. No paid evidence warrants extrapolating a universal winner.

### Spend, stops and cleanup

| Owner | Provider attempts | Settled usage-priced USD | Unresolved maximum USD | Inclusive hard cap |
| --- | --- | --- | --- | --- |
| Storybook |163|0.281633542|0|3|
| Echo Forge |198,including2Gemini503s|0.040943300|0.024501750|1|
| Doc Web |209|0.097180996|0|2|
| Board Game Ingester |18|0.024452440|0|1|
| **Campaign** |**588attempts,586valid responses**|**0.444210278**|**0.024501750**|**7**|

**Conservative maximum exposure USD0.468712028/7.** Usage-derived estimates,
not invoice proof. Gemini503requests remain unknown at their full reservations;
successful retries do not erase the original failures or charges. No paid judge.
Native qualification is included in owner all-in totals; no root duplicate calls.

Root removed all7temporary injected owner variables using the custody helper and
independently verified absence by name in all4ignored env files. Original owner
credentials remain untouched; Conductor's user-provisioned source `.env` and
protected central eval key are retained for future expressly approved evals.
No key values, fingerprints or authorization headers retained in campaign artifacts.

Root independently corroborated Board Game DOCK source/output mismatch visually;
Doc Web family03continuous-table and04fused-header defects against conventions;
maintenance09source-missing dates/notes and10unbound note attribution both support
uncertaingold. PPLX clean on09 is unsafe uncertainty handling even though it does
not increase the narrower confirmed-defectfalseclean metric. GPT falsely asserts
a defect on10; aggregate parity is not identical case-level safety. Root source
review of Echo006wish,024truncatedpredicate,042unansweredlivecondition confirms
genuine ambiguity, rather than scorer/payload defects. Golds unchanged.

Owner closeout, offline replay and proportional validations completed; no further
provider calls authorized merely because cap headroom remains. Owner final manifests,
validation receipts and layered verdicts are authoritative; no default change
or promotion implemented. Best next portfolio action is a bounded independent
Doc Web shadow/full-path promotion plan preserving source review and uncertainty
holds. Runtime adaptation, private-data eligibility and deployment remain separate.


### Final evidence verification

All four owners completed their maintained replay and proportional checks. Root
verified final inventories: Storybook219source/artifact entries; Echo422current,
prior-source and protected raw entries; Doc Web34durable artifacts plus offline
209call/418receipt reconciliation; Board Game205entries including provenance.
Conductor lint and scoped whitespace checks pass. Owner tests: Storybook19,
Echo12, Doc Web10, Board Game46; source/input identity supports reuse of the
recorded checks. No further paid calls needed.

Final owner evidence:

- [Storybook report](/Users/cam/.codex/worktrees/pplx-storybook-20261006/docs/evals/artifacts/story150-perplexity-20261006/report.md), [final manifest](/Users/cam/.codex/worktrees/pplx-storybook-20261006/docs/evals/artifacts/story150-perplexity-20261006/final-evidence-manifest.json).
- [Echo attempt](/Users/cam/.codex/worktrees/pplx-echo-20261006/docs/evals/attempts/control-intent-v1/20261006-perplexity-decider-v11.md), [manifest](/Users/cam/.codex/worktrees/pplx-echo-20261006/docs/evals/attempts/control-intent-v1/20261006-perplexity-decider-v11.manifest.json).
- [Doc Web attempt](/Users/cam/.codex/worktrees/pplx-docweb-20261006/docs/evals/attempts/064-perplexity-decider-v11.md), [manifest](/Users/cam/.codex/worktrees/pplx-docweb-20261006/docs/evals/evidence/064-pplx/manifest.json).
- [Board Game attempt](/Users/cam/.codex/worktrees/pplx-boardgame-20261006/docs/evals/attempts/20261006-perplexity-orientation.md), [manifest](/Users/cam/.codex/worktrees/pplx-boardgame-20261006/benchmarks/results/synthetic-orientation-v1/20261006-perplexity/manifest.json).


## Approved planning follow-through

Cam approved preparation of the [Doc Web independent shadow-validation plan](scout-088-docweb-shadow-validation-plan.md). Plan complete; no new provider calls or target writes. Proposed synthetic runtime re-evaluation has a hard inclusive USD4 ceiling and awaits execution selection. The existing shadow depends on full-planner conventions, so projection savings are not whole-pipeline savings.


## Independent Doc Web runtime follow-through

Cam selected the bounded USD4 synthetic shadow plan. [Runtime result](scout-088-docweb-shadow-validation-plan.md#runtime-screen-outcome): stop promotion of the frozen guarded path. Decider correctly flagged a changed birth year but confidence.42031 failed the frozen.8gate, so fallback retained a planner false-clean. Rawcandidate2/2valid correct; guardedworkflow2/3,1inherited unsafeclean/0introduced, no useful accepted correction. A generated-policy conflict skipped the other candidate chapter. Source/request and receipt hashes independently confirmed; no semantic tune/retry/threshold change. Remaining15unique cases and all second repeats unmeasured.

Five complete calls, USD0.02588316/4, unknown0, temporary key removed. Combined original campaign plus this follow-through: knownUSD0.470093438, unknown maximumUSD0.02450175, conservativeUSD0.494595188 across separately approved ceilingsUSD7+4. Prior uncertainty liability belongs to original Echo Gemini errors, not this run. No defaults/landing. Next justified work is offline disagreement-to-review policy analysis, not automatic fresh spending.


## Campaign close-out decision — 2026-10-06

Stop the campaign and retain current model choices. The completed comparisons
do not demonstrate a reason to adopt Perplexity Decider in any evaluated lane.
Doc Web's follow-up identified a fallback-policy problem and verified an
advisory warning in the experimental sidecar using saved responses and mocked
driver runs; it does not establish fresh model quality or whole-pipeline savings.
The experimental sidecar remains disabled. No further paid evaluation is planned.

Cam authorized scoped check-in and push of the four owner records and Conductor
summary, including the disabled Doc Web experimental integration. Historical
no-commit/no-landing statements above describe their original milestones.
Final remote landing identities are recorded below after owner verification.


## Verified owner landings — 2026-10-07

All four owner execution branches and remote `main` branches were pushed and
verified. Active primary checkouts and unrelated work were preserved. Task
worktrees are retained. No paid calls, activation or model-default changes were
made during close-out.

- Storybook: [`c46a4d14`](https://github.com/copperdogma/storybook/commit/c46a4d14f2a29ce8a82d65700836d6fb22abf82e). Validation: 19 provider-free tests, lint, methodology, privacy coverage, 219-entry manifest and receipt replay.
- Echo Forge: [`16856a03`](https://github.com/copperdogma/echo-forge/commit/16856a0310eeb185b1dcba847b75faa4cbb4dba7). Validation: 12 mocked tests, scoped lint, methodology, freeze/manifest and offline replay.
- Board Game Ingester: [`151c13fc`](https://github.com/copperdogma/boardgame-ingester/commit/151c13fc01deb1fefc193264f4435fc8946e27f4). Validation: 8 focused tests; unchanged 46-test evidence reused; lint, methodology and 204-entry manifest.
- Doc Web: [`cff6771a`](https://github.com/copperdogma/doc-web/commit/cff6771a01ba202b8eb39e13a604a932708e2278). Validation: 83 focused tests, scoped Ruff, methodology; historical manifests and offline replays.

Doc Web preserves all four original attempt commits as ancestors of the combined
landing. Its [historical custody and replay instructions](https://github.com/copperdogma/doc-web/blob/cff6771a01ba202b8eb39e13a604a932708e2278/docs/evals/perplexity-20261006-landing.md)
distinguish the frozen paid-run source from later offline integration. Historical
source manifests remain unchanged. The warning sidecar is still disabled.

Conductor close-out checks: seven credential-helper tests, provider mapping,
scoped credential-pattern scan, repo lint and diff hygiene passed. Only the
Perplexity records, inbox resolution, credential mapping and `.env` ignore rule
were included; unrelated primary changes were preserved. Final recommendation:
keep the existing models; no further evaluation or adoption action is pending.
