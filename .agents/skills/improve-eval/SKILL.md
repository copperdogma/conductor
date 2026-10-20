---
name: improve-eval
description: Investigate an existing evaluation, classify its failure, and plan or perform a bounded evidence-backed improvement.
user-invocable: true
---

# /improve-eval [eval id]

Use this for an existing evaluation. If it does not exist, use
`/create-eval` first. Read the [evidence contract](../setup-methodology/assets/evidence/README.md)
and the local eval registry, runner contract, relevant attempt records, and the exact inputs,
prompts, scorers, outputs, and goldens used.

## Choose the next action

Report `No action needed` when current applicable evidence meets its targets
and no material quality, latency, cost, or safety issue remains. Otherwise
rank the next candidates by retry-ready attempts with a genuinely new trigger,
evidence made inapplicable by a relevant change, largest decision-bearing
gap, then an unmeasured compromise gate. A different commit SHA alone does
not make evidence stale. Check provider claims against current primary sources
when the proposed action depends on them.

Inspect the full evaluated path before attributing a failure. For golden-backed
work, classify meaningful mismatches as `model-wrong`, `golden-wrong`, or
`ambiguous`; for non-golden work, use `prompt-wrong`, `test-wrong`, or
`ambiguous`, adapting the labels only when the local contract has a better
explicit taxonomy. Preserve unresolved uncertainty.

## Bound the experiment

Before a paid or externally billed run, present the candidate, evidence-backed
hypothesis, baseline, primary metric and aggregation, quality gates, smallest
meaningful change, maximum calls/time/spend, stop rule, and validation plan.
Wait for explicit authorization if the user has not already authorized that
scope and budget. Do not infer a spend allowance from an eval request alone.
Run only within the authorized bound. Start with the cheapest analysis that
can change the decision; stop if it rules out the proposed experiment.

Keep development inputs distinct from independent validation inputs. Disclose
overlap or exposure; do not call tuned-on inputs independent confirmation.
Predeclare when one confirmation batch is useful and include it in the
authorized budget. Do not repeat a favorable run to seek a better result. If
the evidence remains borderline after that batch, report it as uncertain.

When authorized, make the smallest change tied to the measured cause, rerun
the relevant eval, and record results, code/data identity, metric, cost,
latency when relevant, and limitations in the attempt record and registry.
Separate diagnostic or non-replayable results from decision-grade evidence.
Do not adopt or change runtime defaults from a score that fails the project's
quality, identity, safety, or operational gates.

If implementation or broad file changes are needed, stop at a concrete plan
and route the work to the owning story. Preserve existing inputs and evidence;
never replace a golden merely to make a result pass.
