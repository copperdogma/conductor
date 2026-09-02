# Scout 062 - Claude Fable and Mythos 5.1 Evaluation

**Source**: Anthropic release/model documentation plus authenticated Doc Web
Models and Messages API calls on 2026-09-01.
**Status**: Do not adopt / Defer
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Release and route truth

Anthropic released Claude Fable 5.1 and invitation-only Mythos 5.1 as two
access tiers for the same underlying model. The general first-party API model
is exact `claude-fable-5-1`; Mythos does not represent a second checkpoint that
needs a duplicate owner evaluation. Anthropic documents image input, adaptive
thinking, native structured output, 1M context, 128K maximum output, and
standard pricing of `$10/M` input and `$50/M` output. Normal API retention is
30 days unless stronger account terms apply.

Official sources:

- <https://www.anthropic.com/claude-fable-and-mythos-5-1>
- <https://platform.claude.com/docs/en/models/fable-5-1/overview>
- <https://www.anthropic.com/claude/fable>

## Selected owner campaign

Cam selected only Doc Web's maintained crop detector, with a US$3.50 ceiling
and public checked-in fixtures. Dossier, Storybook, CineForge, and the other
tracked repos were not authorized for inference. Doc Web executed in isolated
worktree branch `codex/fable51-docweb-eval-20260901` from `origin/main`
`0864678de68246e3fe62fddd90c62585d16e17b3`.

Layered result:

- access: authenticated discovery listed exact `claude-fable-5-1`;
- transport: strict text, generated synthetic vision, and one-case PromptFoo
  parity qualified with exact served identity and terminal `end_turn`;
- reliability: failed the maintained zero-error gate when `Image059` emitted
  an out-of-range normalized bbox and was quarantined locally;
- capability: `12/13` scorer passes, aggregate `0.870015` including the error,
  and only `0.942517` across the 12 schema-valid rows, below the `0.95` target;
- economics: detector spend `$0.731890`, average latency `6661 ms`, and total
  campaign spend `$0.799160`; detector cost was about fourteen times the fresh
  comparable Gemini control;
- privacy: generated data and approved public repo fixtures only; Doc Web's
  owner credential stayed in its existing env boundary;
- adoption: do not adopt; no runtime default changed.

The progressive stop gate prevented the 22-case page-context run. Doc Web's
tracked owner evidence is
`docs/evals/attempts/031-claude-fable51-evaluate-model.md` in the isolated
worktree; the ignored raw detector result SHA-256 is
`601c95e420e384e5c19a02ceab3c085f10b2d4af32b0ebabc1d261d607480600`.

## Portfolio recommendation

- **Doc Web**: close this checkpoint as a rejected crop challenger. Reopen only
  for a materially updated checkpoint or a provider contract that both
  enforces normalized numeric ranges and plausibly improves value.
- **Dossier**: defer. Fable 5 previously missed its extraction value gate, and
  this higher-priced checkpoint has no current owner-specific reopen signal.
- **CineForge**: defer. Opus 5 already missed the maintained script-bible value
  gate; Fable 5.1's doubled price and Doc Web reliability miss do not justify
  another campaign without a new maintained headroom signal.
- **Storybook and private-document repos**: defer behind explicit payload
  authorization and a current decision-bearing gap.
- **Conductor**: retain exact alias and owner outcome in the evaluated-model
  ledger; do not route Mythos as a separate model.

## Retry condition

Re-evaluate only for an exact new checkpoint or a material Anthropic
structured-output/value change that directly addresses the owner stop: strict
normalized-coordinate enforcement plus a credible quality/cost improvement.
Routine Mythos access expansion, benchmark claims, or documentation churn is
not a retry trigger.
