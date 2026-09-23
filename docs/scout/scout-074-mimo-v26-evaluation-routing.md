# Scout 074 — MiMo V2.6 Flash and Pro evaluation routing

Date: 2026-09-22
Status: Completed bounded attempt — transport stops; no adoption

Cam requested both named models and lower-cost delegation because Codex quota
is low. Two Luna agents inspected all seven registered owners read-only; the
coordinator reconciled their checkout findings against today's isolated owner
evidence. No credentials, authenticated requests, inference, or target changes.
No exact candidate match exists in `docs/model-watch/evaluated-models.md`.

## Current public evidence

| Requested OpenRouter model | Catalog canonical slug | USD/M input / output / cache read |
| --- | --- | --- |
| `xiaomi/mimo-v2.6-flash` | `xiaomi/mimo-v2.6-flash-20260921` | 0.14 / 0.28 / 0.0028 |
| `xiaomi/mimo-v2.6-pro` | `xiaomi/mimo-v2.6-pro-20260921` | 0.435 / 0.87 / 0.0036 |

Announced and API-listed; **access: unverified** for owner credentials.
Public catalog: 1,048,576 context, text/image/audio/video input, text output,
optional reasoning, tools, response_format and structured_outputs. These are
metadata claims, not proof of enforced owner contracts. Catalog top-provider
output limit is 131,072; endpoint-specific limits differ and do not override
the smaller owner request budget. No UltraSpeed or open-weight substitution.

Proposed API: `POST https://openrouter.ai/api/v1/chat/completions`.
Both exact models currently list Xiaomi/fp8 and DeepInfra/fp8. DeepInfra appears
in the public ZDR endpoint catalog and advertises named/required/auto/none tool
choice; Xiaomi advertises auto/required but not named/none. Pin DeepInfra/fp8
for this comparison's reproducibility and retention boundary; no provider or
model fallback. This is a proposed route, not successful access evidence.
Refresh its status at owner qualification, preserve a stop without automatic
retry if unavailable. Flash's public status varied during this read-only pass.

Xiaomi documents thinking enabled by default and an enabled/disabled switch;
OpenRouter lists reasoning/include_reasoning and marks reasoning nonmandatory.
Qualify the router's actual reasoning-off contract for bounded interactive
screens, and freeze it before subjects run. Do not infer that hiding reasoning
disables it. Preserve total output/reasoning reservations and complete envelopes.

OpenRouter itself retains prompt content only with opt-in; upstream policies
are separate. DeepInfra's exact endpoint ZDR listing supports the proposed route,
but account settings and owner access remain unchecked. Use only the selected
public/synthetic fixtures; ZDR does not authorize private or licensed material.
No account settings changes. Require ZDR where an owner's policy requires it;
do not add unrelated privacy filters by default.

Sources checked publicly on 2026-09-22:
- [Flash listing](https://openrouter.ai/xiaomi/mimo-v2.6-flash)
- [Pro listing](https://openrouter.ai/xiaomi/mimo-v2.6-pro)
- [Model catalog](https://openrouter.ai/api/v1/models)
- [Flash endpoints](https://openrouter.ai/api/v1/models/xiaomi/mimo-v2.6-flash/endpoints)
- [Pro endpoints](https://openrouter.ai/api/v1/models/xiaomi/mimo-v2.6-pro/endpoints)
- [ZDR endpoint catalog](https://openrouter.ai/api/v1/endpoints/zdr)
- [Xiaomi release](https://mimo.mi.com/docs/en-US/news/latest/v2-6)
- [Xiaomi thinking controls](https://mimo.mi.com/docs/zh-CN/quick-start/usage-guide/text-generation/deep-thinking)
- [OpenRouter retention](https://openrouter.ai/docs/guides/privacy/data-collection)
- [Endpoint ZDR policy](https://openrouter.ai/docs/guides/features/zdr)

## Stable proposed execution handles

Every item includes BOTH Flash and Pro, then one shared fresh incumbent arm if
at least one challenger clears admission. Caps include probes, failed requests,
incumbents and judges; no cross-owner redistribution. Serial progressive runs,
no unchanged retries, exact model/terminal/usage/owner-contract qualification
and zero-cost rendered-matrix preflight precede scoring. A transport failure is
not a semantic miss. Stage 2 must use fresh current-base isolated worktrees,
preserving existing uncommitted owner evidence and any explicit harness transfer.

| Handle | Owner / first lane / comparison | Progressive gates and eligible fixtures | All-in cap |
| --- | --- | --- | --- |
| 1 | Doc Web — `image-crop-extraction`, Gemini 3 Flash control | Owner-established public benchmark pages; exact image/integer-coordinate contract, Image011 then full13. Require >=.95 overall and 13/13 for advancement; measure IoU/count/text exclusion and task cost/latency. Cheap accurate crop alternative is the decision. | USD0.50 |
| 2 | CineForge — `video-understanding` v3, Gemini 3.5 Flash-Lite maintained reference control | Six repo-owned synthetic controls, five ordered JPEGs each; native strict image contract then six-case screen. Overall >=.80, <=15s, <=USD.02 per subject under maintained metrics. Judge cost must fit preflight. No native video/audio claim. | USD1.50 |
| 3 | Storybook — `story056-photo-understanding`, Gemini 2.5 Flash-Lite control | Explicit synthetic FS-001 photo and FS-006 scan; actual JSON/local validation contract, first photo then both. All maintained assertions, <=5s and <=USD.001 per turn. Report photo grounding and OCR independently; two cases cannot establish broad superiority. | USD0.25 |
| 4 | Echo Forge — `control-intent-v1`, Gemini 3.8 Flash-low control | Frozen48 synthetic cases, clear and ambiguous admission cases then complete screen. Preserve current runtime prompt and 2048-token control budget. Stop clear false activation, contract failure or15s timeout; compare exactness, recall, abstention, latency and cost, not aspirational targets alone. Deterministic code retains action authority. | USD0.75 |
| 5 | Dossier — Story170 `standalone-semantic-value`, Astra-medium control | Synthetic correction-withdrawal two chronological snapshots, then matched ten snapshots only after strict compilation and source-meaning admission. Stop material omission/invention/identity or contract failure; preserve owner deadlines, no automatic timeout retry. Lower-cost provenance-preserving SemanticGraph judgment is the decision. | USD2.00 |

**Campaign maximum: USD5.00.** Both candidates are new checkpoint evaluations,
not re-evaluations of prior MiMo models. Controls are fresh comparison anchors;
historic control scores alone cannot prove a relative improvement.

## Owner evidence and scope decisions

- Doc Web: primary `docs/evals/registry.yaml`, Ideal/spec and current
  [Attempt039](/Users/cam/.codex/worktrees/grok47-docweb-20260922/doc-web/docs/evals/attempts/039-grok47-direct-xai-crop-evaluation.md).
  Detector success would not prove crop-only/page-context deletion safety.
  Defer that distinct safety suite until detector admission and a separate
  bounded selection; no video task exists.
- CineForge: registry, eval README, v3 task, and
  [Attempt038](/Users/cam/.codex/worktrees/grok47-eval-20260922/cine-forge/docs/evals/attempts/038-grok47-video-and-script-bible.md).
  Gemini frame results are reference holds, not an adopted passing video model.
  Defer ScriptBible because today's source review left a lexical evidence-form
  ambiguity requiring a prospective scoring decision; avoid spending scarce
  quota on another ambiguous aggregate. Private screenplay QA and second corpus
  remain ineligible. Native audio/video has no selected maintained contract.
- Storybook: primary `docs/evals/registry.yaml` Story056 and
  [Attempt166](/Users/cam/.codex/worktrees/grok47-eval-20260922/storybook/docs/evals/attempts/166-story056-grok47-photo-understanding.md).
  Story060 reuses these images but measures fusion policy; defer that downstream
  lane and text retrieval/linking/clustering to keep this first pass bounded.
  No private photos/transcripts or raw audio/video evaluation is proposed.
- Echo Forge: current
  [control-intent attempt](/Users/cam/.codex/worktrees/grok47-eval-20260922/echo-forge/docs/evals/attempts/control-intent-v1/20260922-grok-4-7.md).
  Defer full soundscape extraction: it is a separate larger output contract,
  some curated narrative fixture eligibility remains unclear, and this screen
  targets the current interactive control decision. No raw-audio generation or
  perception claim, no playback. Existing runtime choice is distinct from the
  older GPT-5.4 Mini soundscape-extractor incumbent.
- Dossier: current
  [Attempt015](/Users/cam/.codex/worktrees/dossier-grok47-eval-20260922/docs/evals/attempts/015-grok47-direct-semantic-transport-stop.md).
  This verifies Story170 exists in the current owner lineage even though the
  primary checkout still exposes older extraction evidence. Use its maintained
  direct SemanticGraph surface. Exclude obsolete ordinary extraction and private
  narratives; no maintained matching image/video/audio lane found. Today's xAI
  timeout repair is provider-specific, not proof that OpenRouter is fixed.

## Not recommended now

- **Board Game Ingester — Defer.** Registry has distinct crop, source-role,
  orientation and inventory vision tasks with real headroom. Current sample
  fixtures include private/licensed RoboRally assets and upload eligibility is
  not established. A ZDR catalog row alone does not authorize these fixtures.
  Prepare an eligible corpus/owner policy before selecting any of those lanes;
  rulebook-derived OCR/import data shares the unresolved boundary.
- **Robo Rally — Do not evaluate.** Current owner instructions prioritize the
  deterministic headless game core; no maintained model-inference benchmark
  was found. The canonical rulebook is private. Model-assisted development is
  not a product evaluation lane.

All seven registered repos have exactly one disposition: first five Evaluate
now, Board Game Ingester Defer, Robo Rally Do not evaluate. No runtime defaults,
commits, pushes, deployment or adoption are proposed by this approval.

Reply `yes` to run all numbered evaluations, or name a subset. This selection
gate is required by `.agents/skills/evaluate-model/SKILL.md` Stage1/Stage2.

## Approved execution — 2026-09-22

Cam replied `yes`, selecting all five handles and both exact candidates under
the USD5 combined maximum. Five lower-cost Terra owner agents were dispatched
before any coordinator inference. Each owns only its fresh current-origin-base
worktree beneath `/Users/cam/.codex/worktrees/mimo26-eval-20260922/`, on its
repo's `codex/mimo26-eval-20260922` branch. The coordinator reviews evidence and
retains aggregate scope/spend responsibility.

Central helper presence-only status confirms OpenRouter configured; vault
permission check passed. Owners prefer existing authorized credentials; otherwise
the approved custody helper supplies only OpenRouter to an ignored owner env,
with variable-name-only cleanup and verification. No secret values or unrelated
credentials are transferred to Conductor records. All owner caps and exclusions
above remain unchanged; no implicit retries, defaults, landing or deployment.

Verified fresh owner bases (all paths under the campaign worktree directory):

| Owner directory | Base SHA |
| --- | --- |
| doc-web | `f9dcf158bff0eea6f7695c592d777db83e1cc800` |
| cine-forge | `5d40a20ed3ead9a97938469a47eb379ab4eecb43` |
| storybook | `8ee92101a558150370ab632aa9033acaab65e5c5` |
| echo-forge | `37699f231a917b5c3de1440b36366d3a79d79467` |
| dossier | `69f48f67143af086b1e3929dbf9d6e9d5abbc718` |

## Owner results — 2026-09-22

All selected owners attempted both requested candidates. Sixteen inference
requests total: Doc Web7, CineForge2, Storybook2, Echo3, Dossier2. No incumbent
or judge calls; no candidate completed an owner benchmark. No semantic model
ranking or adoption claim follows. All runtime defaults remain unchanged.

| Owner / authoritative attempt | Result | Known attributed USD | Conservative accounted exposure USD / cap |
| --- | --- | ---: | ---: |
| [Doc Web040](/Users/cam/.codex/worktrees/mimo26-eval-20260922/doc-web/docs/evals/attempts/040-mimo26-openrouter-deepinfra-access-stop.md) | Flash one strict synthetic response,42.526s,305 reasoning tokens; reasoning-off qualification invalid. Six subsequent capacity429s, including four old-configuration harness attempts. Pro no terminal answer. No crop score. | 0.0001036 | 0.14129416 /0.50 |
| [CineForge039](/Users/cam/.codex/worktrees/mimo26-eval-20260922/cine-forge/docs/evals/attempts/039-video-understanding-mimo-v26-deepinfra-five-image-stop.md) | Both five-JPEG native probes rejected HTTP400: `Too many images in request: 5 > 4`. No four-frame substitution or scoring. Historical raw error bodies were lost; exception text remains, explicitly weaker evidence. | 0 | 0.60373620 /1.50 |
| [Storybook167](/Users/cam/.codex/worktrees/mimo26-eval-20260922/storybook/docs/evals/attempts/167-story056-mimo-v26-pinned-deepinfra-stop.md) | Both FS001 probes hit shared-pool429. No FS006 or quality score. Original budget preflight invalid; post-hoc full-context bound exceeds its owner cap, not an actual charge claim. | 0 | 0.60368660 /0.25 |
| [Echo control-intent](/Users/cam/.codex/worktrees/mimo26-eval-20260922/echo-forge/docs/evals/attempts/control-intent-v1/20260922-openrouter-mimo-v26.md) | Flash one valid strict reasoning-off clear-positive response,805ms; Pro first and Flash next clear-negative both429. One conditional observation, not complete qualification or full48. | 0.00004312 | 0.005973825 /0.75 |
| [Dossier016](/Users/cam/.codex/worktrees/mimo26-eval-20260922/dossier/docs/evals/attempts/016-mimo-v26-openrouter-deepinfra-transport-stop.md) | One exactly route-locked POST per candidate, both429. Dependent second snapshots, source-meaning review and ten-snapshot comparison unmeasured. | 0 | 0.08083636 /2.00 |

Known attributed provider cost totals **USD0.00014672**. Actual total billing is
unknown because fourteen error responses lacked usage/receipts. Combined
conservative accounted exposure is **USD1.435527145**, not billed spend.
Storybook's USD0.60368660 bound exceeds its own USD0.25 authorization; the
overall USD5 maximum does not permit cross-owner redistribution or excuse this
preflight failure. Both failed requests had already been sent when coordinator
review identified it. No further calls were made there. Its bound uses full
model context, deliberately loose rather than asserting unknown image-token
charges. CineForge's analogous finite bound supersedes the earlier blanket
USD1.50 reservation; missing receipts never establish zero billing.

### Scope deviations and evidence limits

- Doc Web, CineForge and Echo initially constrained generic DeepInfra, without
  explicitly enforcing the FP8 endpoint/quantization. Current catalog evidence
  identified FP8, but that is not request-level or served-route proof. Their
  historical evidence is labelled accordingly; later fixes do not govern those
  calls. Storybook used the exact endpoint tag; Dossier used exact endpoint-only
  routing plus price ceilings and dated catalog checkpoint IDs.
- Doc Web's first request used `effort:low, exclude:true`, which did not disable
  reasoning. Calls2,3,6,7 used that old harness configuration; calls4,5 used
  explicit disabled reasoning and also failed429. The harness continued to emit
  requests during this sequence despite the no-unchanged-retry plan. These are
  orchestration defects, not valid retries or semantic misses. An offline
  terminal capacity guard and mocked second-call prevention test now pass.
- Storybook's original preflight confused the per-turn acceptance threshold with
  a worst-case reservation. Original preflight and corrected accounting remain
  separate. No clean within-cap execution claim is made for that owner.
- CineForge's original adapter raised before saving the two raw HTTP error
  bodies. Exception text is not a substitute for raw evidence. The loss is
  recorded and future error persistence is repaired/tested offline, with no
  paid recollection or fabricated reconstruction.
- Complete paid-run reproducibility is limited where original source snapshots
  or exact native commands were not retained. Owner manifests distinguish
  preserved bytes, hashes, later source, and reconstruction. This campaign
  cannot support an adoption-grade comparison even beyond the provider stops.

### Layered synthesis

Flash is callable on DeepInfra from the two valid limited responses; Pro
callability remains unverified because no terminal Pro response was obtained.
Owner transport qualification did not complete. Shared capacity constrained
reliability; this does not establish general model unreliability. CineForge's
observed image-cardinality rejection is route/task incompatibility, with its
raw-custody limitation retained. Full-lane capability, comparative economics,
incumbent superiority and deployment eligibility remain unmeasured. **Defer
both models in all five selected owners.** Do not change defaults.

### Validation, custody and closeout

Owners completed focused offline validation: Doc Web12 tests plus explicit
route/body preflight; CineForge27 video tests, Ruff and registry consistency;
Storybook runner ESLint, methodology and artifact parsing; Echo3 focused tests,
corpus/preflight/manifest checks; Dossier184 semantic benchmark tests, Ruff and
methodology checks. Whitespace checks passed. These validate tooling/records,
not model capability. Coordinator reviewed requests, stop classes, manifests,
cost arithmetic and source-custody limitations; this is not a full independent
implementation audit.

All temporary OpenRouter variables were removed and absence checked:
`DOC_WEB_OPENROUTER_API_KEY`, `OPENROUTER_API_KEY` in CineForge and Storybook,
`ECHO_FORGE_OPENROUTER_KEY`, and `DOSSIER_OPENROUTER_API_KEY`. No owner-managed
credential was overwritten or removed. Worktrees/changes remain uncommitted;
no push, merge, runtime rollout or deployment.

Next action: retain defaults. Reopen only on explicit fresh selection or
decision-bearing changed route evidence, after correcting reservation, exact
route, retry and custody preflight. For CineForge, the route must accept the
maintained five-frame packet; a different provider requires its own proposal.
