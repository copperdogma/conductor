# Scout 067 — GPT-6 Astra Evaluation Routing

**Source:** OpenAI first-party model, model-guidance, and data-controls
documentation; checked 2026-09-04.
**Status:** Evaluated; no portfolio runtime adoption
**Stage:** Stage 2 owner campaign and Doc Web safety follow-on complete.
**Candidate:** OpenAI `gpt-6-astra`
**Projects reviewed:** conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Identity, contract, economics, and privacy

OpenAI documents `gpt-6-astra` as its most capable model and says rollout
begins with enterprise Trusted Access, with broader API access following in
the coming days. The documented contract includes text input/output, image
input, Responses and Chat Completions, strict structured outputs, and
`reasoning.effort` values `low`, `medium`, `high`, `xhigh`, and `max`.
Short-context list pricing is US$10/M input tokens, US$1/M cached input,
US$12.50/M cache writes, and US$50/M output.

API data is not used to train OpenAI models unless the customer opts in.
Standard abuse-monitoring logs may retain customer content for up to 30 days;
ZDR/MAM requires separate approval. This campaign therefore authorized only
checked-in public Doc Web fixtures and synthetic Storybook fixtures. The
existing process-level OpenAI key was reused through each owner wrapper and
was not copied, printed, or persisted.

Official sources:

- <https://developers.openai.com/api/docs/models/gpt-6-astra>
- <https://developers.openai.com/api/docs/guides/latest-model>
- <https://developers.openai.com/api/docs/guides/your-data>

## Selected owner evaluations

Cam approved two direct-provider evaluations:

1. **Doc Web — maintained crop detector ladder, US$1.00 ceiling.** Require
   exact access and native/strict/harness qualification before one public
   maintained case and the frozen 13-case detector. The existing page-context
   gate could run only after the detector cleared every entry gate.
2. **Storybook — Luna Persona challenger, US$0.20 ceiling.** Repair the known
   eval-prompt snapshot drift, qualify exact access, then run one isolated
   synthetic warmth/era case. The remaining 11 turns and a fresh incumbent
   were conditional on candidate quality, latency, cost, and reliability.

**Campaign maximum: US$1.20.**

## Stage 2 owner results

### Doc Web

- **Execution surface:** isolated worktree
  `/Users/cam/.codex/worktrees/gpt6-astra-20260904/doc-web`, branch
  `codex/gpt6-astra-eval-20260904`, base
  `18c8c1509ba015ea80a4f6b6a4294075944681a6`.
- **Access result:** owner-wrapped authenticated
  `GET /v1/models/gpt-6-astra` returned HTTP 404 `model_not_found`.
- **Stop and spend:** no Responses inference request or fixture transmission
  occurred. Spend was exactly **US$0.00 of US$1.00**.
- **Layered verdict:** access blocked; transport, reliability, capability,
  latency, and per-call economics not measured; adoption deferred. The
  maintained Gemini detector and GPT-5.5 page-context evidence are unchanged.
- **Owner evidence:** `docs/evals/attempts/032-gpt6-astra-evaluate-model.md`,
  registry Attempt 032, Story 232, changelog, and generated methodology graph.
  The ignored raw diagnostic is protected by mode and recorded with SHA-256
  `7bea5c03cb640d285e9921662c06aa9ce8bc2eb6f7e7e0535b1402d84cb96d3e`.

### Storybook

- **Execution surface:** isolated worktree
  `/Users/cam/.codex/worktrees/gpt6-astra-20260904/storybook`, branch
  `codex/gpt6-astra-eval-20260904`, base
  `96529f7ddec99cc03c49e05247de57d9b34d6bc2`.
- **Access result:** the authenticated catalog returned 138 models without
  `gpt-6-astra`; one minimal synthetic Responses probe then returned HTTP 404
  `model_not_found` before producing a response or usage envelope.
- **Stop and spend:** no PromptFoo case, judge, representative fixture,
  remaining Luna turn, or incumbent call ran. Spend was exactly **US$0.00 of
  US$0.20**.
- **Harness repair:** the tracked Luna eval snapshot was restored to current
  production `buildPrompt({ userName: "Test User" })` content parity. Production
  prompt logic, rubrics, goldens, chat runtime, and defaults did not change.
- **Layered verdict:** access blocked; native and live harness transport,
  reliability, capability, latency, and per-turn economics not measured;
  adoption deferred.
- **Owner evidence:**
  `docs/evals/attempts/117-luna-persona-gpt6-astra-challenger.md`,
  `docs/evals/artifacts/luna-persona-gpt6-astra-challenger-2026-09-04.json`,
  Story 165, registry, and generated methodology surfaces. The ignored raw
  response has SHA-256
  `4ba95103c42ea5bb3fddc69fb83e2bd219549eb413aa29d4c0073c83fcce2e84`.

## Portfolio synthesis

The campaign spent exactly **US$0.00 of US$1.20**. Both independent owner
routes prove that the currently configured OpenAI project/key does not expose
the exact model. This is an access result, not a transport, reliability,
capability, latency, cost-per-turn, or semantic-quality result. No private data
was transmitted. No production default, deployment, commit, push, or merge
changed; owner evidence remains uncommitted in isolated worktrees.

## Retry condition

Resume at the exact failed access gate only when authenticated model retrieval
or catalog listing returns exact ID `gpt-6-astra`, or OpenAI explicitly confirms
this project has access. Do not repeat either unchanged probe, substitute a
different alias/route, or run fixtures before that condition changes.

## 2026-09-05 re-evaluation follow-through

The recorded retry trigger changed on 2026-09-05: the existing OpenAI project
returned HTTP 200 and exact ID `gpt-6-astra`. Cam then approved a fresh bounded
owner campaign covering Doc Web (US$1.50), CineForge (US$0.60), and Storybook
(US$0.30). Dossier's Mariner and Big Fish fixtures are explicitly eligible for
future model evaluations, but Dossier remained deferred because its checkout
and evaluation surfaces are under heavy active work.

### Doc Web — bounded detector-quality leader, safety adoption rejected

- Reused isolated worktree
  `/Users/cam/.codex/worktrees/gpt6-astra-20260904/doc-web`, branch
  `codex/gpt6-astra-eval-20260904`, base
  `18c8c1509ba015ea80a4f6b6a4294075944681a6`.
- Exact access, native strict text/image transport, and PromptFoo parity
  qualified. All 33 inference calls completed without provider, schema, parser,
  or retry failure.
- One public calibration image measured all five reasoning efforts. `high`,
  `xhigh`, and `max` were dominated on quality, latency, and cost. Full
  survivor runs scored `low = 0.979562` and `medium = 0.980392`, both `13/13`.
- `medium` is the new bounded detector-quality leader versus maintained Gemini
  `0.9703`, but its US$0.434804 full-run cost is about 7.4 times Gemini's
  recorded US$0.059. The remaining campaign allowance could not fund the
  22-case page-context gate, whose input floor alone projected to US$0.696740.
- Spend: **US$0.960878 of US$1.50**. The separately approved safety follow-on
  below resolves the deferred adoption question. Owner evidence: Attempt 033.

### CineForge — strong conditional semantics, value rejection

- Isolated worktree
  `/Users/cam/.codex/worktrees/gpt6-astra-20260905/cine-forge`, branch
  `codex/gpt6-astra-script-bible`, base
  `89b336ddc95788563d966d8193ae6380f6199a30`.
- Exact direct Responses access and strict ScriptBible transport qualified on
  synthetic Open Frequency at `low` reasoning.
- The maintained aggregate was `0.82495`: deterministic `0.6999` after a
  theme-evidence hard gate, with independent semantic rubric `0.95`. Source
  inspection found accurate paraphrases tripping a near-verbatim heuristic, so
  capability is scorer-contract ambiguous rather than a clean semantic loss.
- Economics independently reject the value slot: 33,086 ms and approximately
  US$0.10699 per subject call versus 30,000 ms and US$0.01 hard gates. Medium,
  high, and the incumbent were not run after the progressive stop.
- Spend: **US$0.290085 of US$0.60**. Do not adopt for `script_bible_v1`; owner
  evidence: Attempt 035 and Story 218.

### Storybook — representative quality/latency pass, economics rejection

- Fresh isolated worktree
  `/Users/cam/.codex/worktrees/gpt6-astra-20260905/storybook`, branch
  `codex/gpt6-astra-eval-20260905`, base
  `7b4e4d74ef8f80d643a9d75587b70005d12a9107`.
- Exact access, native Responses transport, production-shaped harness parity,
  prompt snapshot parity, and isolated case topology qualified.
- Astra `low` passed the synthetic representative warmth rubric and the latency
  gate at 2,686 ms, but cost US$0.023070 per subject turn, 2.307 times the
  US$0.01 ceiling. Medium had no semantic justification and no economics
  margin; the remaining 11 turns and fresh Claude incumbent were not run.
- Spend: **US$0.027640 of US$0.30**. Do not adopt for Luna's interactive
  default; owner evidence: Attempt 140 and Story 165.

### Updated portfolio verdict

Total campaign spend was **US$1.278603 of US$2.40**. Astra is a credible
quality leader for Doc Web's bounded visual detector, but not its value leader;
it is economically ineligible for the tested CineForge and Storybook runtime
slots at current pricing. Higher effort was useful only as a calibration fact:
on Doc Web it was dominated, while the two latency/cost-sensitive lanes stopped
at `low`. No private Storybook payload, CineForge Mariner fixture, runtime
default, deployment, commit, push, or merge changed.

Do not repeat the unchanged Storybook or CineForge arms without a material
price, mode, prompt-size, or owner-contract change.

## 2026-09-05 Doc Web page-context safety follow-on

Cam separately approved up to US$1.50 to resolve whether Astra's detector lead
was safe enough for Doc Web adoption. Attempt 034 froze the detector-winning
`medium` configuration and began with `page-122-001`, the authoritative
neighboring-portrait differentiator, before permitting the other 21 cases.

- Exact `gpt-6-astra` completed the first-party strict two-image contract with
  `store=false`, `6353` prompt tokens, `58` completion tokens, `8068 ms`
  latency, and US$0.066430 cost.
- This single request had no provider error or retry, but it does not establish
  general reliability. Cam separately observed availability trouble in another
  long-running Astra task; that external signal remains unverified here and
  does not affect this completed response's semantic classification.
- Astra returned `pass` and described “the two oval portraits.” The maintained
  golden requires `fail`: the intended Moise/Edward crop contains the entire
  adjacent Sophie L'Heureux portrait. Manual source/crop inspection confirmed
  a model-wrong false negative.
- The hard `1.0` safety prerequisite therefore stopped the campaign before the
  remaining 21 cases, any retry, or a fresh GPT-5.5 comparator. Cost was not
  the stop: US$1.433570 of the follow-on ceiling remained unspent.
- Doc Web adoption is now **rejected**, not merely deferred. Astra medium may
  remain the bounded detector-score leader, but it cannot replace either the
  maintained Gemini crop runtime or the recorded GPT-5.5 Responses `22/22`
  page-context validator.

The follow-on brings measured Astra spend to **US$1.345033** across the three
original owner lanes plus Doc Web's separate safety gate. No runtime default,
prompt, scorer, golden, deployment, commit, push, or merge changed. Reopen Doc
Web only for a materially revised Astra checkpoint or demonstrated
page-context capability change; higher reasoning alone is not warranted by the
already dominated `high`/`xhigh`/`max` detector calibration.
