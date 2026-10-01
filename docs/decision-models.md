# Decision models

Decision models put semantic understanding inside code as a bounded judgment.
Supply the relevant state and define the answer space; code consumes the answer
and owns the surrounding workflow. Consider this option when exact rules are
insufficient and a full text-generating call does more than the task needs.

## Choose the kind of work

| Need | Starting approach |
| --- | --- |
| Exact lookup, arithmetic, simulation, identity integrity, permissions or execution | Deterministic code |
| Interpret meaning among defined outcomes, rate evidence or rank candidates | Consider a decision model against the actual baseline |
| Write replies, summaries, rationales or discover open-ended output | Language model |

An LLM returning schema-constrained JSON is also a candidate baseline; a dedicated
decision service can have a different training objective and uncertainty contract.
The interface alone does not establish which will work better.

## TypeSafe primitives

- **Choice:** select among defined alternatives and inspect their distribution.
  Example: classify a captured note as `alignment`, `scout`, `story-prep`, or
  `insufficient-evidence`. This is illustrative, not an implemented router.
- **Noul:** estimate the probability that a condition holds. It has no separate
  confidence field. A probability near 0.5 means uncertainty about yes versus no,
  not medium intensity. Independent conditions can use separate Noul questions.
- **Score:** rate an ordered rubric. Its value is the probability-weighted mean
  of the level positions; it is not an arbitrary measurement or permission to act.

Build the candidate set and copy selected values in code. Missing candidates
cannot be selected. Include a no-match outcome when nothing may fit. Do not
substitute inferred identities or invented evidence for actual candidates.
Ask independent questions together over the same state; code resolves consistency
and any dependent steps rather than assuming answers can see one another.

## Uncertainty and workflow evaluation

Choice/Score confidence summarizes distribution concentration; it does not prove
an individual answer correct. Set thresholds from representative owner data and
consequences. Route unknown, uncertain, invalid, inconsistent or timed-out results
to the existing fallback or review path. Check freshness before applying a result
to changed state. Retain a usable path when the service is unavailable.

Compare with the real rules or LLM baseline using reviewed representative cases,
including absent evidence, negation and ambiguous inputs. Measure errors and
useful complete outcomes, abstention and review burden, end-to-end latency and
total cost including preparation, retries and fallback. A better intermediate
label or lower token price is insufficient for adoption. Preserve dated verdicts;
a new provider does not erase a previous no-go or qualify every task.

## Current provider evidence

Verified source date: **2026-10-01**. Refresh before integration.

- [TypeSafe System One](https://docs.typesafe.ai/concepts/system-one),
  [primitives](https://docs.typesafe.ai/primitives) and
  [confidence](https://docs.typesafe.ai/confidence): Jev accepts text only and
  returns typed decisions/probabilities. Images, audio and video are not inputs.
- [OpenAI DevDay recap, September 29](https://openai.com/index/devday-2026-recap/):
  Decisions API focuses Luna on predefined questions with finite answers using
  text or images. It is announced in limited preview, with broad release planned
  soon. Account access, SDK/endpoint contract and prices were not verified here.
  Do not infer that Jev's primitives or fields transfer to OpenAI.

Review each provider's current retention/training/privacy terms before supplying
private material. Start with approved public or synthetic evidence. Keep keys
server-side; a configured key does not authorize data use or enablement.

## Conductor ownership

Use `/evaluate-model` for current provider verification and numbered owner
evaluation recommendations. Execution remains in the selected owning repository
with its maintained cases, gates and verdict authority. Research and awareness
do not authorize paid calls, private data, deployment or changed defaults.
[Scout 081](scout/scout-081-jev-additional-decision-seams.md) preserves the Echo
Forge no-go for normal/default Jev use despite improved raw intent labels.

## Instruction compatibility

`AGENTS.md` is the repository instruction source. Use Claude Code v2.1.281 or
later with the built-in `agents-md` plugin enabled and the default
`claude-md-or-agents-md` instruction mode. If absent after upgrade, the supported
`claude plugin enable agents-md@builtin` command can enable it. Check a fresh
session's `/context` for loaded AGENTS files. Project/ancestor `CLAUDE.md`,
`.claude/CLAUDE.md` or `CLAUDE.local.md` can suppress fallback. Verify other hosts
before relying on them. An unsupported host may temporarily use `@AGENTS.md` in
a minimal bridge; keep policy in AGENTS. Preserve `.claude/skills` discovery links.
