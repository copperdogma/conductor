# Decisions

Conductor uses ADRs for hard-to-reverse choices about:

- what Conductor owns versus what tracked projects own
- how alignment should classify drift
- whether automation should prepare or directly apply cross-project changes
- how much structure the supervisor project is allowed to add

ADR files live directly under `docs/decisions/` as `adr-NNN-<name>.md`.
In-flight research notes can live under `docs/decisions/research/`.

Use `/create-adr` to scaffold a new decision plus lightweight research notes.
