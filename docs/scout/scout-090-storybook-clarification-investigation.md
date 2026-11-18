# Storybook clarification investigation — evaluator boundary correction

Date: 2026-10-12
Status: Complete — offline source investigation and saved-output replay
Authority: Cam selected “investigate the shared clarification defect offline,
with no provider calls.” No production repair, private data, provider inference,
default change, commit/push or deployment was selected.

## Finding

**The existing application guard already clears the ambiguous c07 target and
asks which relationship to change.** The paid benchmark measured the composed
interpreter before that guard. Earlier descriptions of those results as complete
application behavior were too broad. This investigation corrects that boundary
without changing original model answers, golds, scores or spend.

The valid raw model errors remain: both finite routers select removal for two
overlapping periods, and both Haiku drafts select an unsupported target; the
candidate draft also invents an exact date. The production operation guard
normalizes both drafts to a targetless clarification. No new overlap heuristic
or blanket conversion of all confirmations is justified by that case.

|Measured surface, same24fresh scenarios/one pass|Microsoft|Current native control|
| --- | ---: | ---: |
|Original paid interpreter composition, before consumer guard|23/24|22/24|
|Separate offline consumer-operation projection|17/24|16/24|
|c07 after existing guard|Pass: targetless question|Pass: targetless question|

The post-guard scores are against the unchanged reviewed synthetic expectations.
They are not a new provider run, live database/persistence test, production
accuracy estimate or new latency/economics measurement. Both projections lose
seven otherwise-correct targeted results to extra clarification; control n06
also remains an unnecessary correction question. Thus this is neither a
retrospective passed promotion nor a reason to deploy Microsoft.

## Actual consumer path and authority

- [Freeform consumer](/Users/cam/.codex/worktrees/microsoft-storybook-promotion-20261012/packages/backend/src/knowledge-correction-freeform-relationships.ts:276)
  applies `guardKnowledgeCorrectionRelationshipOperation` after interpretation;
  [question-answer consumer](/Users/cam/.codex/worktrees/microsoft-storybook-promotion-20261012/packages/backend/src/knowledge-correction-operations.ts:886)
  applies the same guard. The paid runner instead called `assessRun` directly
  on the factory's interpreted result.
- [Operation guard](/Users/cam/.codex/worktrees/microsoft-storybook-promotion-20261012/packages/backend/src/knowledge-correction-relationship-context.ts:266)
  constructs targetless `needs_confirmation`, clearing target IDs, old value
  and proposed mutation. In c07 the explicit-change grounding check rejects the
  drafts before the later indistinguishable-candidate gate is reached.
- [Application boundary](/Users/cam/.codex/worktrees/microsoft-storybook-promotion-20261012/packages/backend/src/knowledge-correction-application.ts:517)
  queues a confirmation question for `needs_confirmation`, non-autoapply or
  non-high-confidence drafts. Its operation audit record is not canonical
  graph truth. This investigation observed no database mutation; code tracing
  establishes the branch and pure replay establishes its guarded draft.
- [Question presentation](/Users/cam/.codex/worktrees/microsoft-storybook-promotion-20261012/packages/backend/src/question-presentation.ts:102)
  gives no binary Yes/No shortcut to the “Which specific relationship…”
  question. Source inspection found no direct approve-old-operation action;
  answers go through interpretation again. No live UI/answer workflow was run.

Disambiguation and consent are different: choosing among unknown targets needs
a selection question, while a grounded known-target proposal can legitimately
request consent. Three saved, well-grounded mutations (p02/r05/p01), changed
only in-memory to threshold`confirm`, retain their targets through the actual
guard. A blanket clear-every-confirmation change would break those controls.

## Seven shared extra clarifications

Pure exported-predicate traces identify current conservative lexical grounding
limitations, not one universal first-name defect:

|Case|Observed predicate boundary|
| --- | --- |
|r01|Plural “cousins” does not ground singular cousin labels.|
|r04|Plural “friends” does not ground singular friend labels.|
|r02|Neighbor clause is grounded, but “strike” is outside the removal-verb set.|
|r03|Relationship/action wording occurs in a separate clause without exact full endpoint labels/declared aliases among several candidates. Natural period wording is not an exact stored date label.|
|p03|Correction/date clause lacks endpoint grounding among multiple candidates; later date-grounding checks remain unexercised because this earlier gate stops it.|
|p04|Plural replacement “cousins” does not ground the new type; negative plural “siblings” does not ground corrected-away evidence.|
|p05|Full names occur in the “mentored” clause, while exact “mentor” and “reversed” wording occurs in endpoint-free clauses. The32-candidate selector finds no uniquely endpoint-bound grounded clause.|

These fail the packet's source-reviewed legitimate correction expectations.
First-name aliases, morphology, supported verb forms, clause binding and actual
producer payload conventions need separate analysis before changing the guard.
Do not silently add aliases to gold inputs, loosen uniqueness checks, fit a
threshold to these exposed cases or equate safe deferral with useful correction.
How often this affects real users remains unmeasured.

## Research, evidence and validation

General problem class: partial-pipeline evaluation and conservative linguistic
grounding versus ambiguity/consent. A bounded primary-source pass reviewed
[Google disambiguation/question guidance](https://developers.google.com/assistant/conversation-design/questions)
and [confirmation guidance](https://developers.google.com/assistant/conversation-design/confirmations).
The reusable distinction is to resolve which option a user means before asking
for consent to a known action. These older design references are conceptual
guidance, not evidence for current platform APIs or a new dependency. The local
guard and three negative controls demonstrate applicability here.

One read-only auditor traced source and independently replayed byte-identical
primary code with existing locked dependencies, without writes/network/DB.
The owner then retained a distinct reproducible replay in the isolated campaign
worktree. Guard/context and both consumer call sites are byte-identical to the
paid base338714c12339f3717331e96b9f4c86b3704f4f4f. No runtime/gold/paid-output
edits. Temporary dependency links were removed after verification.

Owner [Attempt182 dated correction](/Users/cam/.codex/worktrees/microsoft-storybook-promotion-20261012/docs/evals/attempts/182-story150-microsoft-independent-promotion.md),
[offline replay](/Users/cam/.codex/worktrees/microsoft-storybook-promotion-20261012/docs/evals/artifacts/story150-microsoft-promotion-20261012/offline-consumer-replay.json),
[verification](/Users/cam/.codex/worktrees/microsoft-storybook-promotion-20261012/docs/evals/artifacts/story150-microsoft-promotion-20261012/offline-consumer-verification.json),
and [separate inventory](/Users/cam/.codex/worktrees/microsoft-storybook-promotion-20261012/docs/evals/artifacts/story150-microsoft-promotion-20261012/offline-consumer-inventory.json)
retain exact pure-replay commands, rows, predicate traces, source snapshots and
negative controls. Four provider-free tests passed: c07 clears both drafts,
n06 correct/noop versus false confirmation persists, all48projections preserve
saved inputs, and legitimate targeted confirmations retain their targets.

Replay SHA2566971eade3a904947231ce8c65d423b927a119106756fe5c5f5b533d2abfbe446;
offline inventory d90a0ccbb4cb5d3111a4ae0ca6bf56149cccc901689170867c0d5c898f036d0e.
Root verified every offline inventory hash/size and that the original paid
inventory54a27da5a322c22df9f47f28fa4a4bf99f051531898fe3d4f05165423771b372
remains byte-identical. Original89inference chargesUSD.188736872 remain unchanged.
**New provider calls0, database operations0, provider spendUSD0.**

## Recommended next action

Repair the evaluator boundary: retain separate interpreter, post-guard operation
and actual persistence/application verdicts, and require the actual guard in
future paid comparison code. Add the saved replay and negative controls as
provider-free boundary regressions. Then investigate/generalize the seven
grounding deferrals under the owner's exact alias/type/authority contract;
do not begin by rewriting production ambiguity handling or replacing models.
No additional model comparison is warranted until that consumer boundary is
represented correctly. Runtime repair/default promotion remains unapproved.

## Approved evaluator repair — 2026-10-12

Cam approved correcting the benchmark boundary and adding offline regressions.
The isolated owner runner now uses an eval-only shared helper to apply the actual
production operation guard before scoring and deciding safety/repeat admission.
Interpreter answers, scores and safety diagnostics remain separate. The helper
also represents the consumer's terminal noop and zero/multiple-operation
clarification branches. Runtime guard, reviewed golds and original paid answers
remain unchanged.

Future runs require a new explicit immutable run identity and approved fixture
and review paths. The historic paid identity cannot execute or be refrozen;
historical verification reads retained snapshots without rewriting its evidence.
Future timing separates interpreter latency from the operation projection and
ends before deterministic scoring. This is still an operation projection, not
a database, canonical mutation, queued question or UI acceptance test.

Focused offline regressions cover all 48 saved outputs, c07, n06, zero/multiple
operations, three valid targeted confirmations, raw invented-target diagnostics,
repeat admission and protection of historical evidence. The root independently
ran the combined boundary/replay/spend suite: **17 tests passed**, including
a fake-transport SDK retry test and a future-artifact tamper-rejection test; no provider dispatch or database operation.
New provider spend **USD0**. The saved-output post-guard result remains
Microsoft17/24 versus control16/24; no new accuracy or performance claim.

Implementation: [shared boundary scorer](/Users/cam/.codex/worktrees/microsoft-storybook-promotion-20261012/scripts/story150-consumer-boundary.mjs),
[runner](/Users/cam/.codex/worktrees/microsoft-storybook-promotion-20261012/scripts/run-story150-microsoft-promotion.mjs),
[regressions](/Users/cam/.codex/worktrees/microsoft-storybook-promotion-20261012/scripts/story150-consumer-boundary.test.mjs).
No commits, pushes, deployment or model-default changes. The next useful work
is a source-backed investigation of the seven shared grounding deferrals before
any further paid comparison.

Root verified the separate [implementation manifest](/Users/cam/.codex/worktrees/microsoft-storybook-promotion-20261012/docs/evals/artifacts/story150-microsoft-promotion-20261012/boundary-repair-implementation.json),
all four code snapshots and every preserved-evidence hash. Manifest SHA256
12dd9380a5e8404c2e3b9e5d820a979aafb0d2c255e5881e74a6254f60b9e3ef.
Owner focused lint, syntax/diff and methodology checks passed; temporary
dependency links removed.
