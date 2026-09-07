# Scout 058 - Route DeepSeek V4 Flash Vision Exp Evals

## Scheduled Metadata Follow-Through — 2026-09-07

Unauthenticated zero-cost OpenRouter catalog and exact endpoint metadata returned HTTP 200. The exact route remains catalog-listed as `text+image->text`; active DeepInfra and Fireworks endpoints advertise `structured_outputs` and `tool_choice.required=true`, while DeepSeek and other endpoints remain generic-only. This is a metadata trigger, not owner-native proof that the required strict contract is enforced for the served identity.

The requested campaign worktrees remain absent. Current doc-web and CineForge checkouts contain unrelated dirty changes and are not safe substitutes, so no isolated owner workers or provider calls occurred. Cumulative spend remains US$0.00 of each owner cap. Access is metadata-available; owner transport, reliability, capability, and economics remain unmeasured; adoption remains deferred. The campaign is waiting for safe isolated owner worktrees plus provider-enforced forced tools or strict JSON Schema on the exact OpenRouter route so the doc-web crop-extraction and CineForge ordered-frame evaluations can run.

**Source**: Official DeepSeek API model listing, 2026-08-21 release notes,
vision guide, JSON-output guide, and pricing documentation; all tracked
repositories in `projects.yaml`; checked 2026-08-21.
**Status**: Spike
**Stage**: Portfolio recommendation only; no provider calls or target-repo
mutations.
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

DeepSeek lists the exact experimental API identity
`deepseek-v4-flash-vision-exp` and describes it as the V4 Flash family with
image input. The release is a real portfolio trigger because two owning repos
have maintained public visual decision surfaces with unresolved model-quality
gaps: doc-web's crop detector and CineForge's ordered-frame video-understanding
lane. It is not a reason to repeat every text benchmark or expose private
Storybook artifacts.

Official documentation supports image input and bills image tokens as input.
The model has a 1M context window, up to 384K output, thinking and non-thinking
modes, JSON Output, tool calls, Responses, Chat Completions, and an
Anthropic-compatible API. Peak direct pricing is $0.44/M uncached input and
$1.32/M output; off-peak pricing is $0.22/M and $0.66/M. These are provider
claims and contract listings, not owner-run proof of access, strict-schema
parity, reliability, or capability.

Stage 1 intentionally did not use target credentials. Exact callability is
therefore **unverified**. DeepSeek's documented `json_object` mode is weaker
than provider-enforced strict JSON Schema; each owner must qualify an eligible
strict tool/schema path against its production contract or stop with
`transport: blocked` and `capability: not measured`. Only public or synthetic
fixtures are eligible until retention, training, and ZDR posture is qualified.

## Recommended Eval Routing

Only numbered items are approved candidates for a Stage 2 campaign.

1. **doc-web - `image-crop-extraction` crop detector.**
   - **Incumbent and decision:** the executable rescue model is
     `gemini-3-flash-preview`; maintained evidence is `13/13`, overall
     `0.9703`, about `7,878 ms/case`, and about `$0.059` total. Determine
     whether the new visual model can meet the detector contract and then
     support a fair held-out candidate/incumbent decision.
   - **Why now:** this is a maintained visual runtime decision and DeepSeek's
     newly added image input is the relevant changed fact. The current
     13-case detector is credible, while all existing crop/page-context cases
     are selection-exposed, so a challenger that passes must proceed to the
     already predeclared held-out truth slice rather than claim victory on
     exposed fixtures.
   - **Progressive stop gate:** qualify exact served identity, image transport,
     usage/cost, terminal completion, and provider-enforced strict
     `crop_regions` output first. Stop on any mandatory-contract failure. Then
     run one representative public smoke and the frozen 13-case detector at
     concurrency 1 with no cache. Stop unless it reaches `13/13` and overall
     `>= 0.95`. Only after that, freeze 12 natural production crops balanced
     `6 pass / 6 fail` across at least eight unused source pages, independently
     review and hash them before calls, and run the candidate and current
     incumbent fresh on identical inputs. No superiority claim may use only
     the exposed set.
   - **Fixture/privacy posture:** checked-in public detector fixtures first;
     the held-out slice must contain only owner-approved material and remain
     protected until its truth contract is frozen. No private material is
     authorized for an unqualified DeepSeek route.
   - **Per-repo spend cap:** **US$1.00**, including probes, candidate calls,
     any required fresh incumbent calls, and at most one causally justified
     repair retry.

2. **CineForge - `video-understanding` ordered-frame comprehension.**
   - **Incumbent and decision:** the repaired maintained lane sends five
     ordered JPEG frames plus neutral timing facts, not MP4, audio, title, or
     transcript. Current decision-grade references both fail all six cases:
     Gemini 3.6 Flash scored `0.4397` at about `6,356 ms/call` and
     `$0.017154/call`; Gemini 3.5 Flash-Lite scored `0.4071` at about
     `2,307 ms/call` and `$0.00273/call`. Determine whether DeepSeek can become
     an eligible frame-only QA subject, not whether it has native video
     understanding.
   - **Why now:** this is a source-backed six-case visual lane with a genuine
     quality gap, and the candidate's image capability is new. DeepSeek's claim
     of text parity with V4 Flash does not reopen CineForge's unrelated text
     slots.
   - **Progressive stop gate:** qualify exact served identity, multi-image
     ordering, strict maintained output, usage/cost, and harness parity. Stop
     on a mandatory-contract failure. Run one public differentiating case,
     then the frozen six-case lane only if the response is valid and remains
     economically plausible. Adoption eligibility requires overall `>= 0.80`,
     subject latency `<= 15,000 ms/call`, subject cost `<= $0.02/call`, and
     acceptable end-to-end reliability. Keep the deterministic structural
     score and maintained Opus rubric score separate; a transport failure is
     not a semantic miss.
   - **Fixture/privacy posture:** the six source-backed Open Frequency frame
     fixtures are public and eligible. Send only the maintained ordered JPEGs
     and timing facts; do not add transcript, audio, title, or other leakage.
   - **Per-repo spend cap:** **US$1.50**, including probes, six candidate
     subject calls, maintained judge calls, and at most one causally justified
     repair retry.

**Campaign maximum:** **US$2.50** across both numbered evaluations. A blocked
access or contract probe spends no remaining benchmark budget and does not
cause the campaign to broaden to another repo.

## Not Recommended Now

- **Storybook - Do not evaluate.** It has real maintained visual lanes, but
  `gemini-2.5-flash-lite` already passes the relevant photo-understanding and
  artifact-evidence fixtures at `1.0`, within their latency and sub-mill
  cost gates. Storybook's private-family-data boundary is also stricter than
  the currently qualified DeepSeek posture. Reopen only for a concrete
  incumbent failure/new visual decision and an approved production privacy
  path; do not test this model as Luna's chat default.
- **Dossier - Do not evaluate.** Dossier's maintained model-owned surfaces are
  attributable text extraction and adjudication. Raw PDF/image/OCR ownership
  belongs to doc-web, so a direct vision run here would duplicate ownership
  without changing a Dossier decision.
- **Board Game Ingester - Defer.** Its future rulebook/image corpus is relevant,
  but current work is package/downstream readiness and no failing model-owned
  visual lane is selected. Reconsider when a broader image/package story
  freezes fixtures and a scorer.
- **Echo Forge - Defer.** The maintained `scene-to-soundscape-golden` lane is
  text input, and exact-family V4 Flash evidence already failed its strict
  outputs. The new model's claimed text parity is not a rerun trigger. Reopen
  when photographed-room understanding has a maintained image fixture and
  scorer.
- **RoboRally - Do not evaluate.** Its maintained evals are deterministic game
  and scenario seeds, not a model-owned vision decision.
- **Conductor - Route only; do not evaluate.** Conductor owns portfolio
  selection and handoff. The owning repositories must execute, preserve, and
  judge their native evidence.

## Official Evidence

- Exact API identity and experimental status:
  https://api-docs.deepseek.com/
- 2026-08-21 release notes and vendor capability claims:
  https://api-docs.deepseek.com/updates/
- Image formats/input shapes and image-token behavior:
  https://api-docs.deepseek.com/guides/vision/
- JSON Output contract:
  https://api-docs.deepseek.com/guides/json_mode/
- Current context, feature, and price table:
  https://api-docs.deepseek.com/quick_start/pricing

## Local Evidence

- doc-web maintained runtime and comparison:
  `/Users/cam/Documents/Projects/doc-web/docs/evals/attempts/025-grok46-evaluate-model.md`
- doc-web held-out truth requirement:
  `/Users/cam/Documents/Projects/doc-web/docs/evals/attempts/026-gemini37-flash-evaluate-model.md`
- CineForge repaired six-case lane and current references:
  `/Users/cam/Documents/Projects/cine-forge/docs/evals/registry.yaml`
- CineForge maintained task:
  `/Users/cam/Documents/Projects/cine-forge/benchmarks/tasks/video-understanding.yaml`
- Storybook photo/artifact decisions:
  `/Users/cam/Documents/Projects/Storybook/storybook/docs/evals/registry.yaml`
- Echo Forge exact-family predecessor:
  `/Users/cam/Documents/Projects/echo-forge/docs/evals/attempts/scene-to-soundscape-golden/20260803-openrouter-deepseek-deepseek-v4-flash.md`

## Stage Boundary

No paid call, credential probe, target story, branch, worktree, benchmark,
registry update, default change, commit, or push occurred in Stage 1.

Reply `yes` to run all numbered evaluations, or `only do 1` / `only do 2` to
run a subset.

## Campaign Follow-Through — 2026-08-21

Cam approved both numbered evaluations. Each owning repo executed in an
isolated worktree from its current `origin/main`; neither primary checkout was
mutated. Both lanes stopped before semantic scoring and total campaign spend
was **$0.00 of the approved $2.50 maximum**.

### 1. doc-web — access blocked; capability not measured

- Worktree/branch:
  `/private/tmp/doc-web-deepseek-v4-vision.iPJ5Gv`,
  `codex/deepseek-v4-flash-vision-exp-eval`
- Base: `009afed44da2494273983449b73c9f4c0a5cde37`
  (`origin/main`)
- Spend: `$0.00 of $1.00`; zero provider requests and zero fixture
  transmissions
- Stop: the doc-web-owned ignored environment has no
  `DOC_WEB_DEEPSEEK_API_KEY` or child `DEEPSEEK_API_KEY`, and its normal
  provider wrapper has no DeepSeek mapping. No sibling credential was copied
  and no router/model was substituted.
- Verdict: access **blocked**; transport, reliability, capability, and
  owner-run economics **not measured**; adoption **defer**. The maintained
  Gemini detector remains unchanged.
- Owner evidence:
  `/private/tmp/doc-web-deepseek-v4-vision.iPJ5Gv/docs/evals/attempts/027-deepseek-v4-flash-vision-exp-evaluate-model.md`
- Validation: registry parse, methodology compile/check, 17 methodology graph
  tests, and whitespace checks passed.

Retry only after explicit authorization provisions a doc-web-scoped DeepSeek
credential and adds the normal non-secret wrapper mapping. Resume at native
identity and combined public-image/strict-schema qualification, not the
13-case benchmark.

### 2. CineForge — strict transport blocked; capability not measured

- Worktree/branch: `/tmp/cineforge-deepseek-v4-vision.TBbZrE`,
  `codex/deepseek-v4-flash-vision-exp-video-understanding`
- Base: `94861914623fff237ffb4ab379fa9f995a58da1e`
  (`origin/main`)
- Spend: `$0.00 of $1.50`; two pre-inference rejected requests, no completed
  model inference or judge call
- Access evidence: the repo-owned OpenRouter catalog exposed exact model
  `deepseek/deepseek-v4-flash-vision-exp`, canonical snapshot ending
  `20260821`, image input, and a sole endpoint named DeepSeek. CineForge has no
  direct DeepSeek credential.
- Stop: with provider pinned, fallbacks disabled, required parameters enabled,
  and data collection denied, the sole route rejected both the named forced
  function and the one-variable `tool_choice: required` repair with HTTP 404:
  `No endpoints found that support the provided tool_choice value`. The owner
  correctly did not weaken the maintained strict contract to prompt-only JSON.
- Verdict: access **constrained**; transport **blocked**; reliability,
  structural/rubric capability, latency, and economics **not measured**;
  adoption **defer**.
- Owner evidence:
  `/tmp/cineforge-deepseek-v4-vision.TBbZrE/docs/evals/attempts/028-video-understanding-deepseek-v4-flash-vision.md`
- Safe topology and ledger:
  `/tmp/cineforge-deepseek-v4-vision.TBbZrE/docs/evals/deepseek-v4-flash-vision-exp-topology-2026-08-21.json`
  and
  `/tmp/cineforge-deepseek-v4-vision.TBbZrE/docs/evals/deepseek-v4-flash-vision-exp-transport-2026-08-21.json`
- Validation: full unit suite `2171 passed`, focused registry/methodology tests
  `44 passed`, contract-manifest tests `5 passed`, Ruff, methodology compile,
  and `git diff --check` passed. Unqualified benchmark code was removed before
  closeout.

Retry only when the exact OpenRouter endpoint supports forced strict tool
choice for image requests, or after explicit authorization provisions a
CineForge-scoped direct DeepSeek credential for separate beta strict
qualification.

No default, prompt, scorer, golden, runtime, deployment, commit, push, merge,
or private-data authorization changed in either owner repo. These are distinct
access/transport results, not evidence that the model failed either visual
task.

## Credential-Reuse and Router-Diagnosis Continuation — 2026-08-21

Cam explicitly authorized copying a working sibling test credential and asked
for deeper diagnosis of the OpenRouter failure. Both owner worktrees resumed
without erasing the initial stop evidence.

Safe name/equality-only inspection found OpenRouter credentials in CineForge,
doc-web, Dossier, and Echo Forge, but all four values are identical: they are
one shared OpenRouter account, not independent routes with different privacy
ceilings. No direct `DEEPSEEK_API_KEY` exists in the inspected repo-local or
process environments. The sibling OpenRouter key was copied without printing
into doc-web's ignored mode-`0600` environment; source repos were untouched.

The combined diagnostic matrix establishes two independent OpenRouter routing
blocks:

1. **Forced tool-choice capability filter.** Named forced-function and
   `tool_choice: required` requests return pre-inference HTTP 404. A text-only
   `required` request reproduces the same result, ruling out image encoding or
   five-image ordering as the cause. Strict `response_format: json_schema`
   likewise has no eligible endpoint under required-parameter routing.
2. **Account privacy ceiling.** Omitting forced choice or disabling required
   parameter enforcement advances to a second pre-inference 404: the sole
   endpoint is classified `Paid model training`, while the shared account
   excludes that data policy. Setting request-level `data_collection=allow`
   cannot widen the account-level guardrail.

All seven CineForge transport shapes and seven doc-web qualification requests
stopped before model inference. No provider returned served identity, terminal
content, usage, or cost; no doc-web image was transmitted; cumulative campaign
spend remains **$0.00**. Exact DeepSeek multimodal-plus-tools behavior,
reliability, latency, economics, and visual capability therefore remain **not
measured**. This is not a model-quality result.

Updated owner evidence:

- doc-web Attempt 027:
  `/private/tmp/doc-web-deepseek-v4-vision.iPJ5Gv/docs/evals/attempts/027-deepseek-v4-flash-vision-exp-evaluate-model.md`
- CineForge Attempt 028:
  `/tmp/cineforge-deepseek-v4-vision.TBbZrE/docs/evals/attempts/028-video-understanding-deepseek-v4-flash-vision.md`
- CineForge root-cause ledger:
  `/tmp/cineforge-deepseek-v4-vision.TBbZrE/docs/evals/deepseek-v4-flash-vision-exp-transport-2026-08-21.json`

doc-web now retains a tested fail-closed OpenRouter adapter path for
configurable request ZDR and DeepSeek-compatible strict crop tools, but no
claim that the blocked endpoint qualified. Its focused provider/environment
tests (`13`) and methodology tests (`17`) pass, as do repo lint, Ruff, YAML,
methodology, and whitespace checks. CineForge removed its unqualified
benchmark adapter; its full suite (`2171`), focused suites, Ruff, methodology,
contract-manifest, and whitespace checks pass.

A semantic evaluation now requires a new external-access decision: either
explicitly authorize changing the shared OpenRouter account privacy guardrail
for public/synthetic fixtures, accepting the endpoint's paid-model-training
classification, or provision a direct DeepSeek test credential for separate
beta strict qualification. The current authorization to reuse local keys did
not itself change that shared account setting.

## Authorized Privacy-Window Follow-Through — 2026-08-21

Cam explicitly authorized one temporary public/synthetic-fixture window for
the shared OpenRouter account. Before any resumed provider call, the
coordinator recorded **Allow paid endpoints that train on request data** as
off, enabled only that control, and verified the browser UI reported it on.
After both owners reported their final provider call complete, the coordinator
restored the control to its original off state and verified it off. The
temporary `DOC_WEB_OPENROUTER_API_KEY` copy was then removed from doc-web's
ignored mode-`0600` `.env`; CineForge's owner-managed credential was untouched.

The window did not qualify either production contract and added no billable
spend:

- **doc-web:** two public text-only access isolations pinned the exact model and
  DeepSeek endpoint, disabled fallback, explicitly allowed provider data
  collection, and disabled request ZDR. The first retained required-parameter
  routing; the second changed only that gate to false. Both stopped before
  generation with the same OpenRouter guardrail/data-policy `404`. Across the
  whole owner campaign, nine failed requests produced no served identity,
  content, usage, cost, or image transmission. Spend remained `$0.00 of
  $1.00`; transport, reliability, capability, and economics remain not
  measured; adoption remains defer.
- **CineForge:** the five-public-image named forced-function retry still
  stopped before inference because the endpoint rejected `tool_choice`. The
  final contract-preserving alternative replaced tools with strict
  `response_format=json_schema` while retaining the complete maintained
  schema, prompt, frame order, pinned provider, and public-data eligibility;
  it also stopped before inference because no endpoint could handle the
  requested parameters. Spend remained `$0.00 of $1.50`; parity, semantic
  scoring, judge calls, reliability, capability, latency, and economics remain
  not measured; adoption remains defer.

The account UI's Default Workspace showed both API keys with **No guardrails**,
and its active default guardrail showed **No policies**. That rules out a
visible per-key/workspace policy as the explanation for doc-web's remaining
data-policy rejection. It does not prove that the temporary account control
became effective in OpenRouter's routing backend; the UI reported enabled, but
the minimal request still received the policy rejection. No additional
account control was changed to investigate that discrepancy.

The OpenRouter request-shape conclusion is firmer: independent of the privacy
discrepancy, the sole exact DeepSeek endpoint exposed neither forced strict
tool choice nor strict JSON Schema for the owner contracts. This is a router
endpoint-compatibility result, not a DeepSeek visual-quality result. Retry only
after OpenRouter exposes one of those provider-enforced strict contracts for
the exact route, or after a direct DeepSeek eval credential is provisioned for
separate native qualification.

## Scheduled Metadata Follow-Through — 2026-08-26

The exact public OpenRouter catalog and endpoint metadata again returned HTTP
200 and one text+image route, but only generic `tools`, `tool_choice`, and
`response_format`; provider-enforced forced tools and strict JSON Schema remain
absent. The unchanged gate stopped before workers, credentials, account
controls, fixtures/frames, inference, parity, scoring, or judges. Spend remains
US$0.00 in doc-web and US$0.00 in CineForge. The missing campaign worktrees
were not recreated because their retained branch tips do not contain this
campaign's exact evidence and recreation could mix unrelated owner work.

## Scheduled Metadata Follow-Through — 2026-08-27

The exact public OpenRouter catalog and endpoint metadata again returned HTTP 200 and one text+image route. Its supported parameters remain generic `tools`, `tool_choice`, and `response_format`; provider-enforced forced tools and strict JSON Schema remain absent. The unchanged gate stopped before owner workers, credentials, account controls, fixtures/frames, inference, parity, scoring, or judges. Spend remains US$0.00 of the US$2.50 campaign maximum. Access is metadata-available; transport is blocked; reliability, capability, and owner economics are unmeasured; adoption remains deferred. The requested campaign worktrees remain absent and were not recreated.

## Scheduled Metadata Follow-Through — 2026-08-28

Unauthenticated zero-cost OpenRouter catalog and exact endpoint metadata again returned HTTP 200. The exact route remains catalog-listed as `text+image->text` with one DeepSeek endpoint, but only generic `tools`, `tool_choice`, and `response_format` are advertised; provider-enforced forced tools and strict JSON Schema remain absent. The unchanged absolute gate stopped before owner workers, credentials, account controls, public fixtures/frames, inference, parity, scorers, judges, and comparators. Cumulative spend remains **$0.00 of the $2.50 campaign maximum**: access is metadata-available, transport is blocked, reliability/capability/economics are unmeasured, and adoption remains deferred. The campaign is waiting for the exact OpenRouter route to expose provider-enforced forced tools or strict JSON Schema so the doc-web crop-extraction and CineForge ordered-frame evaluations can run.
