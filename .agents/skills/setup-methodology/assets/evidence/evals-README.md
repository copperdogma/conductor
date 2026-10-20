# Evaluation workspace for {PROJECT_NAME}

The evaluation registry is the index of decision-bearing evals. Keep each
entry connected to its implementation, inputs, scoring method, target, and
relevant Spec/story/decision. Use the project’s actual runner and evidence
layout; choose PromptFoo only when prompt/model comparison or rubric scoring
fits the proof. Deterministic contracts, runtime, UI, and media behavior may
need a project-owned script, validator, browser check, or artifact review.

Begin with a root evaluation of the Ideal outcome end to end. If there is no
executable product path yet, record a deferred status, why it is blocked, and
the trigger for the first runnable root outcome. Do not create a child eval
without a parent result and measured failure mode, unless the child’s first
purpose is to measure that parent. Link compromise evals to the constraint
they test and the condition for removal or simplification.

Before a paid run, state the hypothesis, baseline, metric and aggregation,
quality gates, maximum calls/time/spend, stop rule, and validation plan; obtain
authorization for that scope. Keep development and independent validation
inputs separate. A metric or validator pass alone does not prove the product
outcome.

Store raw results where the project normally retains evidence. Record exact
inputs, runner/config/scorer versions, revision, subject identity when
relevant, measured result, limitations, and whether evidence is decision
grade. Use the attempt template for each authorized run; leave unrun results
blank.
