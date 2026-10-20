---
name: create-eval
description: Create a traceable evaluation scaffold for a product capability, runtime choice, or removable compromise.
user-invocable: true
---

# /create-eval [eval id or short description]

Create an evaluation scaffold after the project has an authored Ideal and a
repo-owned evidence surface. This skill creates the plan and files; it does not
run paid evaluations.

Read the [evidence contract](../setup-methodology/assets/evidence/README.md).
For a new product evidence workspace, use the sibling
[`registry.yaml`](../setup-methodology/assets/evidence/registry.yaml),
[`evals-README.md`](../setup-methodology/assets/evidence/evals-README.md), and
[`attempt-template.md`](../setup-methodology/assets/evidence/attempt-template.md)
as starter assets, adapting them to the project's actual output and runner.
They are templates, not live evaluation state. Conductor's supervisor registry
and evidence surfaces remain separate from product evidence; do not replace or
populate them with a product eval workspace.

## Workflow

1. Read the Ideal, relevant Spec constraints, applicable decisions, and the
   existing registry and runner documentation. Reuse the repo's existing
   layout and registry schema.
2. Classify the question: product quality/capability, runtime tradeoff, or
   compromise deletion. State the observable decision the eval will support.
3. Place it in the eval ladder. A root eval tests the ideal outcome end to end.
   A child eval requires a parent result and a measured failure mode, unless
   the first task is explicitly to measure that parent. A compromise eval
   names the constraint and the condition for simplifying or deleting it.
4. Choose a runner that can honestly observe the behavior: a stable-case model
   comparison or rubric may fit PromptFoo; deterministic contracts, UI, media,
   and pipeline behavior may need a custom runner, validator, or inspection.
5. Add a complete registry entry with command, runner/config path, inputs,
   expected output or scoring method, metric and aggregation, relevant Spec,
   story/category links, parent/failure links when applicable, and evidence
   freshness fields supported by the local schema.
6. Add only the necessary runner, prompt, scorer, and fixture references. If
   there is no runnable product path, keep the root eval deferred with its
   reason and trigger; do not invent a passing sample or claim proof.
7. Check that every referenced path exists and hand off the next execution to
   `/improve-eval`.

Do not create an orphan child eval, duplicate an existing runner surface, or
mark a scaffold as measured evidence.
