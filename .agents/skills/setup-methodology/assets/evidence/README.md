# Evidence workspace starter assets

These are small starting contracts for a product project's evaluation and
golden workspace. Copy and adapt them only when the project has a real,
observable product outcome. The owning project must define its output schema,
validator, evidence fields, runner, and thresholds from actual product
outputs; these files do not prescribe those details.

These templates are for product projects. Supervisor projects keep their own
evidence surfaces and should not copy a product eval/golden workspace unless
their authored Ideal defines an outcome that needs one. A product project may
defer its root eval until the first executable root outcome exists; do not
invent a root sample or mark an unrun result passed.

The starter files are:

- `registry.yaml`: JSON-compatible YAML with no fabricated eval result.
- `evals-README.md`: minimal guidance for creating a project-owned evidence
  surface.
- `attempt-template.md`: a pre-run plan and post-run evidence record. Leave
  result fields empty until a real run is authorized and completed.
- `golden-README.md`: source retention and semantic-grounding requirements,
  leaving output shape to the owning project.

Preserve original inputs and provenance. Keep development and independent
validation material distinct. Separate structural validation from semantic
judgment, and report deferred or uncertain evidence plainly.
