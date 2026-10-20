---
name: golden-create
description: Create a source-grounded expected-output fixture for a product project with a real output contract.
user-invocable: true
---

# /golden-create [fixture id or input path]

Create one expected-output fixture for a real, representative product input.
This skill applies only when the project owns stable outputs that can be
compared. Conductor is a supervisor project; do not create product goldens for
it or populate its supervisor evidence surfaces with product fixtures.

Read the [evidence contract](../setup-methodology/assets/evidence/README.md)
and the target project's golden-format README, schema, and validator. Keep the
format contract and validation rules owned by the target project. If no stable
output exists yet, defer the golden; author the output schema and validator
only when real output examples exist.

Read the full source and establish the expected facts independently before
reviewing model-produced output. Every expected claim must be supported by
the source, with precise provenance where the product promises it. Preserve
ambiguity instead of guessing. Do not treat an AI-generated expectation as
ground truth without source review.

Retain the original input unchanged. Copy it into the project fixture area or
record a stable, permissioned source reference and integrity metadata when a
copy is inappropriate. Do not delete, move, or rewrite the only source copy.

Create only the files required by the repo's real contract. Run its structural
validator when available; a validator pass does not establish semantic
correctness. Record coverage and provenance using local conventions, mark the
new fixture `pending`, and request an independent verification pass. Report
the created paths and any unresolved questions without claiming the golden is
verified.
