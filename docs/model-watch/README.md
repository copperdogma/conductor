# Daily frontier model watch

This is Conductor's durable, discovery-only record for the daily frontier/SOTA
watch. Conductor verifies public release and access evidence, maps plausible
repo-local evaluation fits, and recommends next actions. Owning repositories
retain benchmark fixtures, provider calls, scorecards, and adoption decisions.

## Watch categories

- **Frontier general-purpose models:** reasoning, coding, tools, vision and document understanding.
- **Decision models and typed judgment APIs:** JEV/TypeSafe, OpenAI Decisions, Microsoft Decision, Perplexity Decider, Alibaba/Qwen decision services and comparable releases. Small size, derived weights or non-generative output do not exclude this category when a maintained owner decision could change.

Both categories use the same identity, prior-attempt dedupe, retry-trigger and discovery-only rules. Decision endpoint/configuration changes remain distinct from new model checkpoints.

## Qualification

A lead must be newly released, announced, previewed, or materially newly
accessible and plausibly challenge a maintained decision-bearing lane. For the general-purpose category, routine small-model churn and fine-tunes do not qualify. For both categories, wrappers, benchmark-only claims and catalog-only quality claims do not qualify. A launch-day posture is **available now; evaluate, don't
adopt yet**.

For each lead, records distinguish announcement, exact documented model ID,
direct API availability, aggregator availability, access/account requirements,
price, region, modalities, limits, structured-output and tool support, served
identity, privacy, reliability, capability, economics, and adoption. `Unknown`
means no supporting evidence was found.

## Layout and automation contract

- `search-playbook.md` — current retrieval plan and failure modes.
- `source-scorecard.md` — source quality and rotation decisions.
- `candidates.md` — deduplicated cross-run candidate ledger.
- `evaluated-models.md` — exact model/alias dedupe index backed by owner evidence.
- `daily/YYYY-MM-DD.md` — append-only run reports.

The watch checks `evaluated-models.md` before recommending any evaluation. A
prior access or transport stop still counts as an attempted evaluation for
deduplication; its unmeasured verdict layers remain unmeasured. A repeat must be
labeled **re-evaluation** and tied to a satisfied recorded retry trigger or an
explicit fresh-run request. Documentation or catalog churn alone is not enough.

The automation uses public metadata and documentation only: no credentials,
account creation, provider settings, paid inference, target-repository changes,
commits, or deployments. It preserves earlier records and runs `git diff --check`
after edits.

## Efficiency pilot

[Deterministic preparation pilot](deterministic-pilot-plan.md) now has a tested
two-catalog collector and exact-diff packet. See the [runbook](collector-runbook.md)
for offline replay, manual collection and recovery, and the
[Stage A evidence](evidence/stage-a-2026-10-23.json) for the one manual public check.
The script-only shadow ran October 24–30 at 07:45 America/Edmonton with a 20%
remaining quota floor and automatic expiry. [Stage B setup evidence](evidence/stage-b-2026-10-23.json)
records the installation. The [October 31 review](shadow-review-2026-10-31.md)
confirmed five complete collections, two fail-closed quota skips, and a disabled
job. Stage C still needs seven usable scheduled dates and remains on hold.
The independent daily scout continues to check announcements and evaluation history.

## Reporting clarification — 2026-11-10

Future reports briefly acknowledge major newly announced or newly discovered
releases already covered by owner evaluations, linking the official announcement
and dated evaluation outcome. This is news coverage, not permission to repeat
an evaluation. Do not repeat unchanged releases daily. Include a compact source
coverage line and material gaps even on no-lead days. Historical reports remain
unchanged. The automation prompt was updated at Cam's explicit request.
