# Installing from the source library

Choose role and project need, not "all skills." Conductor's root supervisor
skills remain tailored to portfolio work. `package.json` selects shared guidance
and **explicit product variants** for triage, story work, local scouting and ADRs.
The variants live under `assets/product/skills/`; install them as the target's
SKILL.md while retaining shared helper scripts/templates. Local AGENTS, product
requirements, schemas, evidence and justified adaptations remain authoritative.

## Inventory and copy

Run from the canonical source root (substitute actual absolute paths):

```bash
python3 .agents/skills/setup-methodology/scripts/package.py audit
python3 .agents/skills/setup-methodology/scripts/package.py plan --target /absolute/new-project --modules core evidence
python3 .agents/skills/setup-methodology/scripts/package.py install --target /absolute/new-project --modules core evidence
```

`core` is a sparse product workflow with a compiler, facts, story/ADR helpers,
setup checklist, operating guidance, optional-invocation `/loop-verify`, and canonical skill links.
`evidence` adds eval/golden skills and starter tracking with **deferred**,
unmeasured root proof. Optional modules: `architecture`, `codebase`, `ui`,
`strategic-review`, `security`, `scheduled-work`. Dependencies are selected automatically.
Use `core` alone when the project's agreed package has no product evidence lane.
The installer only copies; it never calls a provider or creates a runtime.

`scheduled-work` copies a self-contained example kit to `tools/scheduled-work/`:
collector, state-change/report gate, scheduler templates and setup/recovery
runbook. Select it for actual recurring work; it is not in the default product
profile. Examples use synthetic data and no dispatcher. For a standalone script
project that does not need core methodology, copy/adapt just the kit rather than
installing the product profile. A task queue needs project-owned persistent work
dispositions; the sample's single pending request is not a workflow engine.

Both Ideal and Spec must already exist, be substantive and be reviewed against
intake by the agent. The helper checks existence/nonempty content only; it cannot
judge intent, coherence, or implementation leakage. It deliberately never
writes those truths or state. A different existing destination causes the whole
copy preflight to refuse before writes. Identical files are reused. No force
option exists: adapt existing packages explicitly rather than silently replacing
local guidance. The helper supports new/sparse product bootstrap; full retrofits
retain existing schemas/compilers and are agent-led.

The receipt at `docs/methodology/package.json` records selected modules and source
file hashes; it is provenance, not proof that setup or product behavior is done.
The installed helper's audit checks source availability for selected modules.
Keep Conductor as the source for adding modules absent from a target's local kit.

## Finish the authored setup

1. Preserve seed/Ideal/Spec; read every selected surface for project fit.
2. Personalize AGENTS and checklist, removing irrelevant material without
   silently importing supervisor rules. Record changed files as adaptations.
3. Author JSON-compatible `docs/methodology/state.yaml` from actual `spec:N`
   headings and categories. See `assets/product/methodology.md` for its schema.
   Existing richer state/compiler formats remain local; do not replace them.
4. Create a first story only if the agreed package needs one. Otherwise zero
   stories is valid. Do not invent implementation history.
5. Run `make skills-sync`, `make methodology-compile`, `make package-check`,
   and parse `python3 scripts/triage_facts.py --json` directly. `make facts`
   is convenience output; its Make banner is not JSON.
6. Inspect the compiled outputs and evidence deferrals. If there is a real
   product output, author its schema, golden/validator and root eval. Otherwise
   state the actual blocker and concrete trigger. Optional runtime/dependency
   needs use the conditional reference and require project-specific proof.
7. Record checks and limits in the checklist/setup summary. Copy checks do not
   prove semantic correctness, UI quality, project acceptance, or skill utility.

## Learning back into the baseline

Preserve useful project-local versions. A generic improvement merits promotion
when there is evidence it solves a recurring problem across a plausible class of
projects and its assumptions can be stated without domain names, fixtures, or
local provider/runtime mandates. Some improvements belong to a product, hardware,
creative, or supervisor variant rather than the shared core. Record provenance,
expected benefit, applicability, and a small real-use check. A local difference
is neither automatically drift nor automatically reusable wisdom.
