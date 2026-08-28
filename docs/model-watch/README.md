# Daily frontier model watch

This is Conductor's durable, discovery-only record for the daily frontier/SOTA
watch. Conductor verifies public release and access evidence, maps plausible
repo-local evaluation fits, and recommends next actions. Owning repositories
retain benchmark fixtures, provider calls, scorecards, and adoption decisions.

## Qualification

A lead must be newly released, announced, previewed, or materially newly
accessible and plausibly challenge a maintained decision-bearing lane. Routine
small-model churn, fine-tunes, wrappers, vendor benchmarks, and catalog-only
claims do not qualify. A launch-day posture is **available now; evaluate, don't
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
