# Eval Registry

Conductor's eval surface is lighter than the product repos.

Use `docs/evals/registry.yaml` to track evidence for questions such as:

- Did a scouting workflow produce useful project-specific recommendations?
- Did an alignment pass correctly separate intentional divergence from drift?
- Did a new skill or prompt reduce supervisor busywork?

An eval entry should record:

- the question being tested
- the inputs or cases used
- the outcome
- the decision taken
- what follow-up is still needed

This repo does not need a heavy benchmark workspace until Conductor itself has
enough repeated tasks to justify one.

