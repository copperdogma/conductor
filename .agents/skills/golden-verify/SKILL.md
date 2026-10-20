---
name: golden-verify
description: Adversarially check a golden fixture against its source, output contract, and available validator.
user-invocable: true
---

# /golden-verify [fixture id]

Verify one fixture or a bounded set using the target project's format
documentation and schema. This skill applies to product projects with real
outputs; Conductor's supervisor evidence does not use product golden fixtures.

Read the shared [evidence contract](../setup-methodology/assets/evidence/README.md)
and follow the target project's local format and tracker.

Read the source first and form an independent view of what it supports before
examining the expected output. Check completeness for the declared scope,
provenance, exactness, ambiguity, and whether each expected value follows the
source and output contract. Run the project validator if one exists. Report
structural validation separately from semantic review.

Classify material differences as model/output wrong, golden wrong, or
unresolved when evidence cannot decide. Correct a golden only when the source
or contract justifies the correction; preserve the original input and prior
expectation in repository history. Record findings and review status in the
project's tracker. Use one writer for shared tracking files. A newly created
golden remains pending until an independent pass; do not verify your own work
as that independent pass.

Use parallel reviewers only when the fixture set warrants it and the user or
task authorizes delegation. For a single fixture, perform a focused adversarial
review directly. Never mark a fixture clean when its validator fails or a
material semantic mismatch remains.
