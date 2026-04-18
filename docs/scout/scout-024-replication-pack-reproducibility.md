# Scout 024 — Evaluate Solve Everything's "Replication Pack" Concept

**Source**: `https://solveeverything.org/`
**Status**: Defer
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

Reviewed Solve Everything on 2026-04-17 to answer two questions: is a
"Replication Pack" a real thing, and should the tracked projects adopt it?

The answer splits cleanly in two:

- Solve Everything's exact term is mostly its own coined framing. The site
  defines a "Replication Pack" as a downloadable, cryptographically signed file
  containing code, proofs, and logs that lets third parties verify a claim.
- The underlying idea is real, but under a different, broader name:
  replication packages or reproducibility packages are already standard in
  research and policy workflows. Those typically include code, data, a README,
  environment/dependency information, and rerun instructions. They do not
  generally imply formal proofs or the stronger "bug-free and mathematically
  safe" claim Solve Everything is making.

So this is not fake, but the site is stretching a real reproducibility concept
into a much heavier proof-and-signature vision.

## Project Relevance

- **dossier**: `Defer`. Plausible future value if Dossier starts publishing
  stronger public eval, research, or benchmark bundles, but the full
  proof-heavy framing is heavier than the current need.
- **storybook**: `Defer`. Low immediate fit. Most likely future use would be a
  lighter reproducibility bundle for research or evaluation artifacts, not a
  formal "Replication Pack" lane.
- **doc-web**: `Defer`. Possible later fit for external OCR/intake benchmarking
  or public artifact bundles, but not enough current pressure for a shared
  methodology commitment.
- **cine-forge**: `Defer`. Similar to Storybook: plausible only if public eval
  or benchmark publication becomes important later.

## Recommendation

- Keep this at `Defer`.
- Do not adopt Solve Everything's branded "Replication Pack" framing or create
  a new shared methodology lane around cryptographic proofs right now.
- If a tracked repo later needs externally reviewable evidence bundles, adapt
  the lighter real-world replication-package pattern instead:
  - code and input artifacts
  - README / rerun instructions
  - environment and dependency capture
  - outputs or verification scripts
- Reopen this only if a repo starts publishing formal research, benchmark
  claims, or public eval artifacts where reproducibility becomes an operator or
  trust bottleneck.

## Evidence

- Solve Everything uses "Replication Pack" as a glossary term and ties it to a
  speculative proof-heavy future with signed code/proofs/logs.
- Independent reproducibility guidance from research institutions and journals
  uses "replication package" or "reproducibility package" for code/data/README
  bundles that let others rerun the work.
- Sources reviewed:
  - `https://solveeverything.org/`
  - `https://openeconomics.zbw.eu/en/knowledgebase/how-research-is-made-reproducible/`
  - `https://apsanet.org/PUBLICATIONS/Journals/American-Political-Science-Review/Guidelines-for-Reproducibility/`

## Confidence

- High on the naming/fit judgment. The distinction between the real research
  term and Solve Everything's heavier coined version is explicit in the sources.

## Open Questions

- If one tracked repo later needs public reproducibility bundles, should that
  stay repo-local or become a shared lightweight evidence-pack pattern?
