# Scout 009 — Evaluate RepoProver for Textbook Intake and Verification

**Source**: `https://github.com/facebookresearch/repoprover`
**Status**: Reject
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

RepoProver is real, current research code for one very specific problem:
large-scale formalization of mathematics textbooks into Lean. The official repo
and paper show a multi-agent scaffold operating on a shared Lean codebase with
already-prepared LaTeX chapters, an explicit theorem manifest, a file-based
issue tracker, pull-request review agents, and a merge queue that keeps the
main branch buildable.

That is not a document-intake system. It assumes the hard intake work is
already done: the source textbook already exists as curated LaTeX files, the
targets are already enumerated as formalization goals, and success is measured
by Lean build/proof completion. Doc Web and Dossier sit much earlier in the
pipeline. They deal with messy PDFs, OCR, layout recovery, provenance, evidence
grounding, and recommendation/verification surfaces before any downstream
task-specific formal reasoning could happen.

There are a few portable motifs here, but they are too generic and already
absorbed locally to justify follow-up from this scout:
- immutable source material with derived work happening downstream
- explicit manifests / target lists for bounded work decomposition
- build-gated merge discipline instead of silently merging broken output

Those ideas do not create a new intake opportunity for the tracked repos, and
they do not change the current substrate choice.

## Project Relevance

- **dossier**: Low incremental value. Dossier already has stronger local rules
  around provenance, fresh verification, prompt grounding, and end-to-end eval
  discipline. RepoProver's theorem-formalization workflow does not help with
  extracting grounded entity graphs from text.
- **storybook**: No meaningful direct relevance. Storybook needs memory,
  capture, extraction, and UX improvements, not Lean-backed theorem proving.
- **doc-web**: Reject for the originally suspected use case. RepoProver does
  not improve raw textbook ingestion, OCR, layout recovery, or recommendation-
  only intake planning. It starts after a book is already converted into clean,
  structured source files with explicit formalization targets.
- **cine-forge**: No meaningful direct relevance.

## Recommendation

- Reject this as a Doc Web / Dossier intake lead.
- Do **not** create a Conductor story and do **not** hand this off to any
  target-project inbox.
- Keep only one small reusable lesson in mind:
  - if a future downstream formal-reasoning system appears, keep source
    material immutable and drive work from explicit manifests plus hard
    verification gates
- Treat the earlier textbook-intake framing as clarified and closed: RepoProver
  is a downstream formalization system, not an upstream document pipeline idea.

## Confidence

- High. The source repo and paper are explicit about scope, inputs, and success
  criteria, and those do not overlap with the tracked repos' current intake
  problems in a way that would justify even a bounded spike.

## Evidence

- Primary external sources:
  - `https://github.com/facebookresearch/repoprover`
  - `https://arxiv.org/abs/2604.03071`
  - `https://github.com/facebookresearch/algebraic-combinatorics`
- Local overlap / mismatch evidence:
  - `/Users/cam/Documents/Projects/doc-web/AGENTS.md`
  - `/Users/cam/Documents/Projects/doc-web/docs/ideal.md`
  - `/Users/cam/Documents/Projects/doc-web/docs/stories/story-176-confirmed-intake-handoff-to-explicit-recipe-runs.md`
  - `/Users/cam/Documents/Projects/Dossier/AGENTS.md`
- Historical note only:
  - inbox note: `Already scouted a bit with ChatGPT and many things to take/try`

## Open Questions

- If a tracked repo later wants formal reasoning over already-structured source
  material, would that be a new downstream project surface rather than an
  intake extension?
