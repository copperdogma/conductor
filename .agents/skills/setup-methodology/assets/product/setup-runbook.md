# Setup methodology

Use `.agents/skills/setup-methodology/SKILL.md` as the canonical setup entrypoint.
Project-specific Ideal/spec intake comes first through `/init-project` or
reviewed equivalent. Package installation cannot replace that conversation.

Before choosing an implementation, follow the setup skill's reference-library
review in the Conductor source checkout (`docs/reference.md`). Discuss relevant
tools and working examples with the user; check current fit and alternatives
before recommending adoption. Record the result or access gap in setup notes;
reuse a completed kickoff review. The library stays in Conductor.

Select the relevant modules, copy package resources using the bundled package
helper's plan/install commands, and author state from the actual project.
The helper preserves existing files; a conflicting retrofit needs a reviewed
local adaptation. It does not invent an Ideal, Spec, state, product golden,
root eval result, port allocation, server, or dependency install.

Complete `docs/setup-checklist.md`, not just the copy operation. Compile and
check the graph, verify skill links, parse facts directly as JSON, and inspect
that optional lanes are honestly absent/deferred. Evidence setup requires an
actual root proof or explicit reason/trigger for deferral. Runtime/dependency
commands, where needed, use the conditional reference in the setup skill bundle.
Record what was installed, deferred and locally adapted plus applicable checks
and their limitations. Never call package checks product acceptance.

For real recurring collection/monitoring/reporting, select the optional
`scheduled-work` module. Its `tools/scheduled-work/README.md` explains setup,
shadow operation, failure recovery and natural scheduler proof. Adapt mechanics
before model invocation; a periodic synthesis may still call AI each period.
No timer or model adapter is enabled by copying the kit.
