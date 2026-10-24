# {PROJECT_NAME} — Setup Checklist

Working copy for one setup or refresh. Use `complete`, `pending`,
`deferred: reason`, or `not applicable`; do not turn optional lanes into
mandatory phases. Retain it while work is active and summarize open decisions
at handoff.

## Intake and north star

- [ ] Project-specific Ideal and Spec exist and reflect reviewed intake.
- [ ] Ideal describes user outcomes without implementation or delivery plan.
- [ ] Privacy, fidelity, accessibility, offline ability, and other intrinsic
      user needs remain explicit where applicable.
- [ ] Current architecture, active constraints, and unresolved choices are
      linked to their proper Spec, decision, runbook, story, or eval surfaces.

## Reuse and reference discovery

- [ ] Conductor reference library reviewed for relevant capabilities, or access
      gap/no match recorded. Resolve it from the Conductor source checkout.
- [ ] Useful tools/examples discussed with the user; current sources and
      alternatives checked before adoption recommendations. Record reuse,
      adaptation, or build rationale and remaining evidence in setup notes.

## Package fit

- [ ] Setup mode selected from `.agents/skills/setup-methodology/references/modes.md`.
- [ ] Existing repo guidance and evidence inspected before changing surfaces.
- [ ] Only relevant methodology and optional lanes installed; sparse or
      supervisor projects mark product-only lanes not applicable/deferred.
- [ ] Public skills and setup instructions describe one canonical entrypoint.
- [ ] Recurring work, if present, selects/adapts `scheduled-work`: deterministic
      mechanics precede AI; monitor versus periodic synthesis is explicit;
      privacy, thresholds, state, delivery, budgets and natural-tick proof are
      local. Otherwise mark this lane not applicable; copying enables no timer.

## Evidence baseline (product projects only)

- [ ] Starter assets in `.agents/skills/setup-methodology/assets/evidence/`
      were adapted to the project's actual contracts, or intentionally not
      copied for a non-product/supervisor project.
- [ ] Golden workspace and project-owned output contract exist, or are
      deferred until real outputs can define them.
- [ ] Root Ideal eval/golden seed exists, or registry records an honest reason
      for deferral and a trigger for the first executable root outcome.
- [ ] Eval registry, evidence README, attempt template, runner, and relevant
      source-backed fixtures are connected; no unmeasured result is called a
      pass.
- [ ] Child evals link to a measured parent failure; compromise evals identify
      the constraint and deletion/simplification condition.
- [ ] Any paid evaluation has an explicit bounded authorization before calls.

## Planning and handoff

- [ ] Planning state/graph and active story surfaces are present only where
      they fit the project's actual workflow.
- [ ] Setup and skill references resolve; local commands match local files.
- [ ] Deferred items have a reason and a next trigger; completed claims cite
      current evidence.
