# Golden fixture contract for {PROJECT_NAME}

This document describes expected outputs for a project-owned, source-backed
fixture. The owning project must replace this starter with its real output
schema, required fields, provenance rules, and validator once representative
outputs exist. Do not invent an output schema or golden pass from an empty or
non-runnable project.

Each fixture should retain or identify the original input, record its source
and integrity/provenance information, and contain the expected output for a
clearly stated evaluation scope. Preserve the source unchanged. Expected
claims must be grounded in the input; keep unresolved interpretations
explicit. A structural validator checks form, while independent semantic
review checks whether the output matches the source.

New or materially changed fixtures remain pending until an independent review
and available structural validation are recorded. Keep review history in the
project’s tracker. A verifier should read the source before the expected
output and should not count its own authored fixture as independent review.

## Project-specific format

Document here after a real product output establishes it:

- Fixture file layout and identifier convention
- Expected output schema and provenance requirements
- Validator command and its limits
- Semantic review criteria and tracker/status convention
- Source retention rules for the project's input types
