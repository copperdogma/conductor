# Scout 104 — Liquid LFM3 access and evaluation routing

2026-10-29, America/Edmonton. **Closed — deferred by Cam; no evaluation.**

## Final user decision

Cam declined this family: no local model execution, dependency setup or downloads.
Disk space is constrained and this is not currently a model he wants to adopt.
Reconsider only if the models rise meaningfully in relevant rankings and a
usable hosted route is available; this is a future discovery trigger, not
authorization to evaluate or create a new monitor. Hosted access was advertised,
but exact owner-callable routes were not established here.

Downloaded weights carry no provider inference charge. The original proposal's
dollar ceilings covered remote incumbents/judges, not Liquid downloads or local
inference. Cam found that presentation misleading: do not list prices in future
local-model proposals. Do not silently turn a hosted-access inquiry into a local
deployment campaign. Preserve this preference in future recommendation routing.

The original Stage1 proposal below is historical and **withdrawn**, including
all numbered execution handles and budgets. No selection or spending permission
remains pending. No model execution/downloads, provider spending, target changes
or evaluation-ledger attempt occurred.

## Original recommendation — withdrawn
Cam supplied [Liquid's October27 announcement](https://x.com/liquidai/status/2115128329003303107).
Provider spend USD0. No credentials, authenticated discovery, inference, model
downloads, target writes, worktrees, defaults, commits or pushes. Three economical
read-only portfolio workers assisted. Coordinator corrected stale primary-checkout
conclusions against current owner evidence linked by Scout103, including Echo's
maintained intent task and BGI's public orientation/contour lanes. Existing dirt
is preserved. All eleven registered owners have dispositions below.

## Access and identity

**Yes: published weights and documented local inference APIs are accessible.
Our successful inference access remains unverified.** This post names a family,
not one interchangeable model. [Official collection](https://huggingface.co/collections/LiquidAI/lfm3),
[library](https://docs.liquid.ai/lfm/models/complete-library), and
[release](https://www.liquid.ai/blog/lfm3) establish the six specialized checkpoints.

| Exact open ID | Inputs / output | Context / computation |
| --- | --- | --- |
| `LiquidAI/LFM3-1.7B` | Text / generated text, tools |256K; thinking on by default, template `enable_thinking=False` available |
| `LiquidAI/LFM3-VL-2B` | Text, images, video / generated text |128K; default reasoning, no verified named effort levels |
| `LiquidAI/LFM3-Audio-2B` | Text, audio / text and speech |32K; not nominated below |
| `LiquidAI/LFM3-Omni-2B` | Text, images, video, audio / text and speech |32K; non-reasoning, thinking=true unsupported |
| `LiquidAI/d1-2B` | Text, images, video / typed decisions |128K; one forward pass, no generated reasoning |
| `LiquidAI/d1-Omni-2B` | Text, images, audio / typed decisions |128K; no generated reasoning |

[Text docs](https://docs.liquid.ai/lfm/models/lfm3-1.7b),
[VL docs](https://docs.liquid.ai/lfm/models/lfm3-vl-2b),
[decision docs](https://docs.liquid.ai/lfm/models/d1-2b),
[omni card](https://huggingface.co/LiquidAI/LFM3-Omni-2B),
[audio docs](https://docs.liquid.ai/lfm/models/lfm3-audio-2b),
[omni decision docs](https://docs.liquid.ai/lfm/models/d1-omni-2b), and
[template](https://docs.liquid.ai/lfm/key-concepts/chat-template) define these
controls. Reasoning consumes generated-token headroom. No invented low/high sweep.
VL tools/constrained JSON have documented server recipes, but the
[current card](https://huggingface.co/LiquidAI/LFM3-VL-2B) still describes vLLM
support as in progress and SGLang support as in review. Recipes do not establish
released runtime availability. Transformers is the proposed qualification path.

Open d1 has Noul/Choice/Score, multiple choices, source-span text/number/date,
boxes/counts and numeric intervals. Full typed answers need Transformers;
llama.cpp supports the core decision types. Arbitrary JSON schemas, generated
rationale and tools are not equivalent to typed decisions.

Hosted access is advertised by Liquid's release/model pages. Public
[pricing](https://www.liquid.ai/pricing) specifically lists LFM3-1.7B at
USD.08/.20 per million input/output tokens, cached input.02. The public page
retrieved here does not give the other new generative models' rates or exact
hosted request IDs. Do not derive an execution budget from third-party console
screenshots. [Hosted d1 docs](https://docs.liquid.ai/lfm/models/d1) list `d1.1`
and `d1-ultra` at `https://api.liquid.ai/decisions/v1/systemone`; they do not prove
either is the open d1-2B checkpoint. No substitution is authorized. Hosted
retention/ZDR/account callability are unverified; the custom-deployment privacy
promise on the pricing page is not evidence for ordinary hosted API policy.

The evaluated ledger contains older d1/d1-ultra attempts, no exact LFM3/open
d1-2B attempt. October28 candidate discovery is not an evaluation. No evaluated
ledger entry is added before execution. Distinct hosted d1.1 is outside this
specific open-family proposal.

## Proposed route and shared execution contract

**Local exact open checkpoints**, pinned public revisions and reviewed custom
model code, in isolated owner environments. Transformers BF16 on Metal where
supported; a documented CPU FP32 qualification path is allowed, recorded as a
different execution configuration with its actual timing. Freeze the chosen
device/dtype before semantic comparisons. No quantization sweep or GPU rental.
Candidate provider charge USD0; local electricity, download/storage and setup
time are not free economic inputs. Report warm inference, cold load, memory,
throughput and setup separately; no hosted-latency or zero-total-cost claim.

Read-only host check found48GiB memory, MLX available in default Python, no
torch/Transformers there and no llama-server on PATH. This is a plausible local
capacity fit, not successful setup or long-context admission. Selection permits
isolated dependency setup and downloads of the three nominated checkpoints;
no system-wide upgrade. Qualify exact public revision/runtime/input contract
before paid controls. If dependencies, source pixels, context or output contract
cannot qualify, preserve access/transport evidence; do not call it a quality miss.
No cloud fallback or new provider account is implied.

Each owner gets its own isolated current-base worktree under the approved root
and its own worker; **serialize local model use across workers** on this shared
machine. Follow all owner protocols, no private inputs despite local processing.
Comparators/judges receive only owner-cleared public/authored-synthetic fixtures
through existing approved routes. Their ordinary retention may apply; account
ZDR/opt-in is unverified. No private genealogy, photos, family audio, finance,
licensed game scans or screenplays. Exact original pixels and complete source
requests; no truncation/resizing to force admission.

Zero-cost resolved case/prompt/history/schema/source/judge/token/reservation
preflight precedes multi-case spending. Preserve original output before parsing.
Actual strict production contract first; local prompt-JSON diagnostics are
capability-only when strict enforcement cannot qualify. Source-backed adapter
and judge repairs may continue within caps, reusing saved outputs. No tuning a
valid semantic failure, altered goldens, favorable repeat selection or automatic
thinking escalation. Independent tasks stop independently. Whole-workflow stage
shares remain unknown; compare task benefit and added maintenance explicitly.

## Original handles — withdrawn, not executable

1. **Doc Web — US$6 inclusive.** `LFM3-VL-2B`, default thinking with16384
   generated-token headroom; difficult literal table/OCR may use32768, frozen
   before calls. First `image-crop-extraction`: Image011/Image001 then remaining
   public13 versus fresh exact Gemini3 Flash Preview. Require13/13 contract
   passes, mean>=.95 and source-preserving lettering/date/seal/signature extent;
   source review accompanies tolerant geometry scores. Independent
   `literal-table-fidelity`: bakery discriminator, then three authored
   confirmation-v2 sources versus Astra medium8192; all36 clear cells, ownership,
   genuine I/l holds, zero harmful change or gratuitous clear hold. Independent
   actual `image-entry` Barney LOC handwriting versus a pinned, qualified Gemini
   reader; >=.99 and no invented/normalized words. Current requested3.7 redirected
   to3.8: qualify the current comparator and label it, never claim3.7 parity.
   First decisive source failure stops its task. Hypothesis: local geometry or
   literal fidelity at useful speed; recent reference arms leave both gaps.
   These are development screens, not automatic crop-consumer qualification.

2. **Dossier — US$6 inclusive.** `LFM3-1.7B`, thinking enabled/default,
   32768 output tokens including reasoning. First native schema/compiler
   namesakes qualification, then `standalone-semantic-value`, full authored
   Story184v4 `long-history-two-families/follow-1`321KB continuation versus
   fresh Sol6.1 medium16384. Public256K context can plausibly admit this
   approximately73–75K-token request, but candidate token count/KV memory must
   qualify locally first. Preserve all five meanings, complete supported
   attribution/corrections/provenance/uncertainty, compile and zero material
   errors. Two blind complete-obligation/complete-emitted-row Opus4.6 reviews,
   one operational review repair. Seek30% task latency reduction or useful local
   quality parity with disclosed operational costs. Provider cautions against
   complex reasoning: this makes the quality gate important, not a measured
   failure. n1 exposed continuation, no candidate-history/scale/adoption claim.

3. **Board Game Ingester — US$3 inclusive.** `LFM3-VL-2B`, default thinking,
   16384 output; dense contours32768. First `asset-orientation`: four public
   CC0 inputs pub001/012/013/014 versus Sol6.1 low2048. Zero wrong auto angles,
   correct equivalence/ambiguity holds, exact inverse/hash/pixel/provenance
   receipts. Independently `physical-outline-retention`: six authored scanner
   scenes versus Sol low8192; source001 discriminator and006 clean control
   first. Zero full-plane material/rim loss or definite-background leakage,
   component/hole/contact integrity; also report continuous lost/leaked pixels.
   Stop contour expansion on first confirmed material failure. Current Sol and
   Terra both lose material, so better boundaries or safe orientation coverage
   can matter independently of tiny API savings. No contour fitting or real
   package/physical acceptance claim.

4. **CineForge — US$4 inclusive.** `LFM3-VL-2B`, default thinking32768,
   `video-understanding`v4: three fixed synthetic dialogue/prop-continuity/motion
   cases, five original ordered JPEGs each, against fresh Sol6.1 low4096 and
   Luna6 low1400 references. Strict13-key schema, deterministic>=.70,
   rubric/overall>=.80, mean<=15s and<=.02USD subject; nine blind Opus4.6 reviews
   maximum. Preserve Attempt047 source clarifications symmetrically. First
   discriminator then stop valid decisive failure. Current controls miss quality
   gates: temporal grounding is useful even without cost savings. This is an
   ordered-image development screen, not six-case independent qualification,
   native MP4/audio or autonomous QA.

5. **Storybook — US$2 inclusive.** First `LFM3-1.7B` on `luna-persona`,
   thinking explicitly disabled for interactive latency,2048 output. No-advice
   discriminator then12 authored synthetic turns/seven reset/history groups
   1/1/1/1/3/3/2 against Luna6 none512 and fixed blind GPT5 rubric. Require all
   system/source/continuity/Inference Firewall/no-therapy assertions,<=5s and
   <=.01USD per turn; seek30% latency or meaningful grounded-quality gain.
   Independently `LFM3-VL-2B` default thinking4096 on Story056 FS001 then FS006,
   actual prompt-only JSON/Zod/assertions versus Gemini2.5 Flash-Lite.
   Every assertion,<=5s,<=.001USD remote subject cost; local operating cost
   reported separately. Source-review lexical/field-placement conflicts without
   rewriting scores. Private provider eligibility/defaults unchanged.

6. **Echo Forge — US$2 inclusive.** First `d1-2B` native forward computation
   on `control-intent-v1`: qualify001/016/006 then42 current-input authored
   synthetic cases versus fresh Gemini3.8 Flash low2048. Preserve six excluded
   unsent-context cases008/009/019/024/027/045. Deterministic finite label
   projection, no fabricated rationale or tuned probability threshold. No worse
   exact accuracy/recall/false activation/ambiguity, hard15s; seek30% p95 gain or
   useful quality improvement. Stop when no-worse becomes impossible.
   Independently `LFM3-1.7B`, thinking disabled8192, on
   `scene-to-soundscape-golden` Tavern then Dungeon versus GPT5.4 Mini4000.
   Require2/2 full role/music/negative/default requirements and<=.01USD subject;
   report soft5s. Recent mapper controls fail meaning, so this is a quality
   question too. No licensed34-room expansion, private speech or audio playback.

**Campaign maximum US$23**, six nontransferable ceilings. Candidate inference
local; dollars cover fresh controls, independent judging and bounded recovery.
No selected semantic calibration arms: default thinking protects hard grounding,
disabled text thinking protects interactive tasks, d1 has no effort control.
Other configurations/quantizations remain unmeasured, not failed. Truncation
repairs need adequate supported headroom, not arbitrary thinking sweeps.

### Reservation feasibility

Scout103's maintained owner matrices reserve conservative remote controls and
judges: DocWeb<=5.40, Dossier Sol<=.70 plus three reviews<=4.70760, BGI<=1.86288,
Cine controls<=.60 plus nine reviews<=2.74320, Story controls<=.15 plus three
reviews<=.62076, Echo<=.782016. Removing its paid challenger reservations gives
room inside the above caps for local candidate runs and finite remote recovery.
These are planning bounds, not claimed bills. Stage2 must verify current exact
prices/token accounting and full reservations before dispatch; no unbounded
provider-price call. Local qualification precedes paid matrix calls. No hosted
Liquid prices are used to size this campaign.

## Not recommended now

| Remaining registered owner | Disposition and reason |
| --- | --- |
| Robo Rally | **Defer:** deterministic bot/replay seeds exist, no maintained interchangeable model benchmark. Define the legal-program decision boundary first. |
| Ultima IV Web | **Defer:** live model/Decisions comparison is explicitly deferred; zero scored trials and input isolation/leakage/pause/primitive-action/budget prerequisites remain. Scripted playthrough is a different qualification. |
| Financial Hub | **Defer:** private financial product; no maintained owned eligible model benchmark found, spec absent. Define a synthetic source-grounded task first. |
| Financial Monthly Analysis | **Defer:** review-only AI proposals exist, but no maintained semantic-quality fixture/harness; parser/security tests do not establish advisory quality. Private household records excluded. |
| VLC Thumbs | **Do not evaluate:** registered nested path absent; no accessible owner contract or fixture lane. Resolve location before reconsideration. |

Matching-task omissions: DocWeb actual crop admission/grouping and page-safety
promotion remain blocked by Attempts081/083 consumer/source-policy gaps; a new
checkpoint alone cannot resolve those. Crop-only40 is lower priority: incumbent
already40/40 at roughly.05USD, while no representative held-out benefit or
local maintenance payoff has been identified. d1 text consistency20 and
source-span extraction are possible later adapters; present source/literal
quality work is more consequential than marginal categorical cost savings.
Alverson OCR needs source/golden adjudication. Dossier typed identity58-case
screen already has Luna13/13 ask labels and no false questions at.00086USD;
rerunning that small easy set cannot settle the new large-family false-question
problem. The larger chapter task needs a frozen compatible d1 producer contract
before a separate proposal. Assertion review15/15 at.000153USD likewise has
little standalone payoff. No identified maintained raw-photo Dossier lane.

Storybook correction-mode capture/retrieval produced zero router dispatches in
Attempt191; a faster new finite classifier does not fix that consumer. Its batch
audio story requires diarization/word/speaker/timing contracts absent from the
verified LFM3 speech interface; Omni Q&A/TTS is not speaker-attributed transcription.
No new voice-generation contract benchmark selected. BGI real licensed scans,
restoration routing and source-role/inventory tasks lack a frozen eligible
public representative panel; image generation/restoration is not VL text output.
CineForge ScriptBible/entity extraction lacks a newly frozen eligible small-model
value question beyond this stronger modality match; defer its separately sized
full-text contract, not a claim that small models cannot improve it. Native
video/audio is absent from the maintained ordered-frame task. Omni versions are
not added as duplicate vision contenders without a cross-modal task decision.
Echo VL/audio lanes lack maintained eligible tasks; d1 cannot generate complete
soundscape JSON. Hosted d1.1 is a distinct future proposal, not an alias here.

## Evidence and next action

Current owner evidence and worktree pointers: [Scout103](scout-103-gpt61-terra-evaluation-routing.md),
especially Dossier038, DocWeb085, BGI20261026, CineForge055, Storybook196 and
Echo20261026. Earlier primary-checkout registry rows are historical where these
records establish newer owner contracts. Dossier possible-identity registry,
Storybook192/191/Story201, BGI restoration report20261025 and current financial/
game methodology were also inspected read-only.

Cam declined the proposal. Do not execute these handles from a later generic
`yes`; any future evaluation requires a fresh hosted-route recommendation and
selection. No temporary worktrees were created during Stage1.

## Closeout scope and validation

Documentation-only landing: this scout, its index/candidate pointers, reviewed
inbox decision and changelog. No product or skill changes, no paid checks.
Validation uses `make methodology-check`, `make lint`, scoped whitespace and
local-link checks. The task-owned integration worktree is
`/Users/cam/.codex/worktrees/liquid-lfm3-deferral-20261029/conductor`, branch
`codex/liquid-lfm3-deferral-20261029`, owner: this Liquid access-review chat.
Retain it after landing under finish-and-push's default retention policy; no
cleanup requested. It holds this task's recoverable scoped landing candidate,
not models or benchmark artifacts. Primary checkout changes remain untouched
except this chat's document additions.

Validation result: methodology graph current; lint OK; scoped local links,
withdrawn decision and whitespace checks passed on the isolated candidate.
