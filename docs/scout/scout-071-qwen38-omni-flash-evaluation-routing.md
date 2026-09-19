# Scout 071 — Qwen3.8-Omni-Flash Evaluation Routing

Date: 2026-09-19
Status: Deferred by Cam — no configured Alibaba access; US$0 spent

## Deferral decision — 2026-09-19

Cam explicitly deferred the campaign because direct Alibaba access is absent
and authorized pushing the scoped campaign records. No automatic retry or
monitor is scheduled. Reopen only at Cam's request after eligible access is
available; refresh the exact route, owner contracts and budget before calls.
All three lanes remain capability-unmeasured.

## Selected campaign follow-through — 2026-09-19

Cam selected all three revised items after approving the skill-only policy
update. That update landed on Conductor origin/main as
`822f00b1ae889c30c5a72a6132c588f31e088121`; only
`.agents/skills/evaluate-model/SKILL.md` was committed and pushed. The campaign
selection initially left evidence uncommitted; the subsequent deferral and push
request authorized landing these records.

Each owner fetched its remote and entered a dedicated worktree on branch
`codex/qwen38-omni-flash-20260919`. Primary checkout changes were preserved.

| Owner | Worktree | Exact remote base | Spend / cap |
| --- | --- | --- | --- |
| CineForge | `/Users/cam/.codex/worktrees/qwen38-omni-flash-cineforge-20260919` | `b5140648653c16194ba025a80d0b9542ddaeb775` | US$0 / $0.75 |
| Doc Web | `/Users/cam/.codex/worktrees/qwen38-omni-flash-doc-web-20260919` | `9f09aca6ff055d1f9842c0f4ab2e800627f4bdba` | US$0 / $0.50 |
| Storybook | `/Users/cam/.codex/worktrees/qwen38-omni-flash-storybook-20260919` | `42f25e4d88080373b0aad14e9f376388ceb89e6f` | US$0 / $0.10 |

All three owners found no configured direct DashScope/Alibaba credential through
presence-only checks. Conductor ran `python3 scripts/eval_credentials.py status
--json` and `python3 scripts/eval_credentials.py check`: supported configured
providers are Moonshot, OpenRouter and xAI, and vault permissions passed. The
helper does not currently expose an Alibaba provider mapping. This is no usable
centrally custodied Alibaba access, not a claim about arbitrary uninspected vault
variables. No credential was injected, copied, exposed or removed; cleanup is
not applicable.

A fresh unauthenticated GET of `https://openrouter.ai/api/v1/models` returned no
Qwen Omni entry. Existing OpenRouter access therefore does not supply the exact
approved model. No substitute model or reseller route was used.

Combined spend: **US$0 / US$1.35**. Access is blocked by local provisioning;
account callability remains unverified. Transport, reliability, capability,
latency and task economics are all **not measured**. Adoption is **defer**, not
model rejection. No native/contract/harness probe, subject/judge/control call,
fixture transmission or runtime-default change occurred.

The campaign is now deferred. A future explicit reopening requires authorized
direct Alibaba access and its region/workspace endpoint; refresh the proposed
lanes and caps then. Do not repeat absent-credential checks as model-quality
evaluations or start automatic retries.

Owner evidence, including exact safe credential-check commands and layered
verdicts:

- [CineForge Attempt037](/Users/cam/.codex/worktrees/qwen38-omni-flash-cineforge-20260919/docs/evals/attempts/037-video-understanding-qwen38-omni-flash-access-stop.md).
- [Doc Web Attempt038](/Users/cam/.codex/worktrees/qwen38-omni-flash-doc-web-20260919/docs/evals/attempts/038-qwen38-omni-flash-access-stop.md).
- [Storybook Attempt157](/Users/cam/.codex/worktrees/qwen38-omni-flash-storybook-20260919/docs/evals/attempts/157-story056-qwen38-omni-flash-access.md).

Doc Web and Storybook methodology build/check and whitespace checks passed;
registry records were parsed by their owner generators. No product tests or
paid reruns were needed for these documentation-only access stops. Owner
attempts/registries and generated records were prepared in isolated worktrees.
The later deferral close-out lands only this campaign's records, preserving
unrelated Dossier and watch edits.

CineForge registry, truth-ledger, generated-methodology freshness and whitespace
checks passed. Its broader `make check-evals` reported pre-existing contract
manifest drift for `AGENTS.md` and `scripts/methodology-graph.js`; those files
match the fetched base and were not repaired in this access-only campaign.
Conductor `make lint`, `make methodology-check`, `make skills-check` and
`git diff --check` passed. No code/harness behavior changed.

## Deferral close-out landings — 2026-09-19

Scoped owner records were validated, committed and verified on remote `main`:

| Owner | Commit | Durable evidence |
| --- | --- | --- |
| CineForge | `bdcea8d5b9fafe9f358274ee57ccf3987a07f49f` | [Attempt037](https://github.com/copperdogma/cine-forge/blob/bdcea8d5b9fafe9f358274ee57ccf3987a07f49f/docs/evals/attempts/037-video-understanding-qwen38-omni-flash-access-stop.md) |
| Doc Web | `0a4d20ff894892f4d96a9a4541d9299d358c2cd5` | [Attempt038](https://github.com/copperdogma/doc-web/blob/0a4d20ff894892f4d96a9a4541d9299d358c2cd5/docs/evals/attempts/038-qwen38-omni-flash-access-stop.md) |
| Storybook | `69940efd87b46c1a0e3031757af98a434c01f18a` | [Attempt157](https://github.com/copperdogma/storybook/blob/69940efd87b46c1a0e3031757af98a434c01f18a/docs/evals/attempts/157-story056-qwen38-omni-flash-access.md) |

Owner execution branches were also pushed. Primary owner checkouts remained
untouched; isolated worktrees were retained. Applicable record/generated-document
checks passed, with CineForge's unrelated pre-existing manifest drift disclosed
above. Conductor's scoped close-out contains only this scout, its index entry
and this model's ledger row. No provider calls or credential changes occurred.

## Revised recommendation after review — 2026-09-19

This section supersedes the original one-owner proposal and its Doc Web and
Storybook deferrals below. At proposal time, no execution had been selected. A passing incumbent
is not a reason to exclude a relevant challenger: an eval can measure quality,
latency, cost and reliability improvements. Require a plausible measurable
benefit, not demonstrated superiority before testing. Passing all cases does
not imply perfect quality, and a saturated test is a measurement limitation.

Stable execution handles for the revised proposal:

1. **CineForge — Evaluate now; US$0.75.** Preserve the exact lane, progressive
   gates, synthetic payload boundary and diagnostic limit in original item 1.
2. **Doc Web — Evaluate now; US$0.50.** First lane `image-crop-extraction`,
   frozen `conservative-count` prompt and maintained integer-coordinate schema.
   Challenger hypothesis: improved box overlap, count/grouping and text exclusion,
   or equivalent quality with lower latency/cost, against `gemini-3-flash-preview`.
   Its 13/13 pass rate still leaves continuous score headroom: maintained 0.9703,
   with a later fresh incumbent at 0.9629. Qualify native image/schema contract
   and harness parity, then Image011 grouping, then full13 only if the anchor
   passes. Require 13/13, overall >=0.95 and zero transport/schema errors;
   advancing candidates receive a fresh same-input incumbent comparison for
   measured quality/latency/cost. Use only owner-established public benchmark
   images, verifying that classification before transmission; no private scans.
   Strict failure permits one labeled JSON-object diagnostic on an eligible
   image, not production parity or a full adoption run. This selection is
   detector-only; page-context safety and crop-deletion gates remain separate,
   unmeasured requirements before any production adoption. The cap covers all
   calls and controls; stop before exceeding it.
3. **Storybook — Evaluate now; US$0.10.** First lane
   `story056-photo-understanding`, FS-001 photo and FS-006 scanned document;
   both notes explicitly identify synthetic stand-ins. Compare against shipped
   `gemini-2.5-flash-lite` using identical prompts/images and a fresh control.
   Qualify the actual JSON/local-validation contract, then one fixture, then
   both if passing. Require all grounding/OCR/follow-up assertions, pass rate
   1.0, <=5s and <=$0.001 under owner metric semantics. Freeze reasoning `none`
   for this interactive arm. Measure actual response cost and latency rather
   than inferring value solely from token prices. The incumbent's prior 1.0
   score covers only two intentionally simple images; a tie cannot prove equal
   general visual ability. This small screen can establish compatibility and
   bounded operational value, not broader quality superiority. If quality is
   tied and broader comparison matters, propose harder representative held-out
   public/synthetic fixtures, freeze their criteria before fresh runs of both
   models, and request a separate scope decision. Do not alter this benchmark
   during the campaign. Results remain adapter-required, with no private family
   upload clearance or default change. Cap includes qualification and controls.

**Revised campaign maximum: US$1.35.** Same direct Alibaba route and disclosed
retention apply. ZDR is optional only for owner-eligible public/synthetic inputs.
Missing access stops the selected owner; no account provisioning or model
substitution is implied. No paid call or target-repo edit has occurred.

Remaining dispositions: **Dossier — Defer** (in-flight catch-up);
**Echo Forge — Defer** (no distinct maintained audio/video-input decision);
**Board Game Ingester — Defer** (fixture/upload eligibility and lane preparation);
**Robo Rally — Do not evaluate** (no current model-owned API slot).

Rechecked evidence: Doc Web registry's crop target and incumbent rows;
Storybook registry's Story056 target, fixture notes and photo-understanding
implementation. The original exclusions below are retained as superseded
recommendation history, not the current execution scope.

## Verified identity and access

Alibaba's [exact model page](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-omni-flash)
lists `qwen3.8-omni-flash`: text, image, audio and video input, text output,
1M context and 131,072 maximum output tokens. It supports Chat Completions
and Responses in Beijing, Singapore, Hong Kong, Tokyo, Frankfurt and Virginia.
This is a distinct service from the previously evaluated Qwen3.8 Flash and Max;
no exact prior attempt appears in the current evaluated-model ledger. No
immutable dated snapshot was established.

Announced: yes. API-listed: yes. **Access: unverified.** No authenticated
catalog, credential inspection or inference was performed. Public OpenRouter
catalog inspection returned no Qwen Omni entry. Use direct Alibaba Model Studio,
not an inferred router slug or a reseller substitution.

The [Omni guide](https://www.alibabacloud.com/help/en/model-studio/qwen-omni)
documents regional workspace endpoints, for example
`https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1/chat/completions`.
Thinking defaults to `xhigh`; `none` disables it, `minimal` maps to `low`, and
`high`/`max` map to `xhigh`. Do not combine reasoning effort and thinking budget.
The proposed visual reasoning arm freezes `low` before qualification.

[Pricing](https://www.alibabacloud.com/help/en/model-studio/model-pricing):
Singapore is US$0.15/M input, $0.016/M cache-hit input and $0.47/M output.
The other five listed regions show $0.113/$0.014/$0.382 respectively. The
proposal budgets Singapore pricing and no cache savings; actual owner region,
identity and billing must be established before calls.

[Structured-output documentation](https://www.alibabacloud.com/help/en/model-studio/qwen-structured-output)
explicitly lists Omni for JSON Object, but not in its JSON Schema supported-model
list. Function calling is advertised; forced-tool and strict schema enforcement
are unverified. Do not inherit ordinary Flash's schema support for Omni.

[Alibaba's privacy notice](https://www.alibabacloud.com/help/en/model-studio/privacy-notice)
says customer data is not used for training, but model/application call data is
stored. No retention duration or unconditional ZDR was established. Only the
owner's project-owned synthetic frame controls are proposed; no private media,
screenplays, family uploads, licensed scans or account-policy changes.

## Original numbered proposal — superseded

1. **CineForge — Evaluate now; US$0.75 ceiling.** First lane:
   `video-understanding`, frozen `video-understanding-frame-packet-v3`.
   Qualify exact served identity, terminal response, usage, five ordered JPEGs,
   required output contract and native/harness parity. Begin semantics with
   `dialogue_confession_push_in`; only a qualifying passing anchor unlocks the
   six active cases. Require all maintained deterministic/rubric hard gates,
   overall >=0.80, <=15 seconds and <=$0.02 subject cost per case.

   The comparison references are Gemini 3.6 Flash (0.4397) and Gemini 3.5
   Flash-Lite (0.4071). Attempt019's repaired v3 evidence supports HOLD, not fine
   ranking; its current registry rows supersede the local skill's general
   quarantine warning for this exact repaired surface. The useful decision is
   whether Omni can clear the visual QA gap and merit further integration.
   If it advances, run a fresh Gemini 3.5 Flash-Lite control on the same frozen
   cases within the ceiling. No runtime-default change or QA activation follows
   automatically.

   Strict output is a qualification risk, not an assumed feature. If native
   strict transport is unsupported, stop the parity/adoption branch. Permit at
   most one clearly labeled JSON-object diagnostic on the synthetic anchor,
   retaining the complete response before parsing, to decide whether an adapter
   investigation is worthwhile. This cannot unlock the six-case adoption run
   or establish production parity. Stop on access, identity, transport, hard
   quality, latency or cost failure. Classify decision-bearing scorer ambiguity
   rather than changing goldens to rescue the candidate.

   Fixtures are six project-owned synthetic controls, five ordered JPEGs each;
   neither subject nor judge receives audio, MP4, transcript or semantic titles.
   ZDR is optional for these inputs unless current owner policy is stricter.
   This evaluates frame understanding, not native audio/video capability.

   The cap includes probes, diagnostic, subject, fresh control, retries and the
   maintained Opus 4.6 judge. Before multi-case calls, inspect the resolved case
   matrix, exact prompts, judge, no-cache configuration, concurrency and
   conservative remaining cost. Reduce/stop the run if it cannot fit; never
   exceed the cap. Use existing eligible owner/eval-only access in an isolated
   current-base worktree; missing access is an honest stop, not authorization
   to create an account or use a different model.

**Campaign maximum: US$0.75.** Actual spend: US$0. No provider call, target-repo
mutation, worktree creation, commit, push or default change occurred.

## Original deferrals — superseded where noted above

| Owner | Disposition | Reason |
| --- | --- | --- |
| Dossier | Defer | The sequential owner catch-up campaign is already in flight. No stronger Omni-specific maintained decision was established; do not duplicate or broaden that campaign. |
| Storybook | Defer | Story056 photo-understanding already scores 1.0 with Gemini 2.5 Flash-Lite at 2.3–2.9s and $0.000150, within 5s/$0.001 gates. No demonstrated quality/value advantage justifies a second saturated visual lane now. Real family payloads are excluded. |
| Doc Web | Defer | Relevant public crop fixtures exist, but the strict integer bounding-box contract is unqualified and the incumbent is already 13/13 at 0.9703. Prioritize CineForge's larger quality gap; page-context safety remains a separate decision. |
| Echo Forge | Defer | Maintained work maps text to structured soundscapes, not audio/video input. Omni produces no audio, and strict output remains unqualified; no stronger current advantage over its maintained production winner was identified. |
| Board Game Ingester | Defer | Orientation is promising, but no eligible isolated Omni comparison is ready and canonical rulebook/scan upload eligibility is unresolved. Require public/synthetic fixtures or owner-approved provider eligibility first. |
| Robo Rally | Do not evaluate | Maintained engine/scenario tests are deterministic; no current model-owned API slot. The planned rules-model eval and private source PDF do not create an eligible live lane. |

## Evidence inspected

Owner paths are resolved by `projects.yaml`. Current primary-checkout records
were inspected read-only; execution must recheck remote base and owner contracts.

- CineForge: `docs/evals/registry.yaml` video-understanding;
  `docs/evals/attempts/019-video-understanding-post-commit-calibration.md`;
  `benchmarks/video_understanding/README.md`;
  `benchmarks/tasks/video-understanding.yaml`;
  `benchmarks/providers/video_understanding_provider.py`; local evaluate-model.
- Storybook: `docs/evals/registry.yaml` story056-photo-understanding and owner
  photo-eval context.
- Dossier: current owner instructions/eval context and Conductor's
  [in-flight campaign](../alignments/align-047-dossier-model-catchup.md).
- Doc Web, Echo Forge, Board Game Ingester and Robo Rally: owner instructions,
  spec/eval context and each `docs/evals/registry.yaml`.
- [September 19 discovery](../model-watch/daily/2026-09-19.md) and
  [evaluated-model ledger](../model-watch/evaluated-models.md).

The earlier discovery left privacy unclear. The exact current Alibaba notice
now supports no-training plus storage, still not ZDR. This routing does not
change the discovery report or mark the candidate evaluated. Ledger entry waits
for a selected owner attempt.
