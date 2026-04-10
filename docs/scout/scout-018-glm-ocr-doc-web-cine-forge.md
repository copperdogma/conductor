# Scout 018 — Evaluate GLM-OCR 0.9B for OCR and Intake Workflows

**Source**: `https://x.com/kimmonismus/status/2018706291489923372?s=12&t=uFZE-MuhgWdh1YErEZzLtQ`
**Status**: Defer
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

The source tweet from 2026-02-03 pointed at a real release, but the current
decision should follow the later primary sources rather than the announcement
framing. The official GLM-OCR technical report (`arXiv:2603.10910`, submitted
2026-03-11 and revised 2026-03-16) and the official Hugging Face model card
confirm that this is a real 0.9B specialized OCR model with MIT licensing,
8-language support, and deployment paths for Transformers, vLLM, SGLang, and
Ollama. The official OmniDocBench repository then updated its public evaluation
on 2026-03-31: GLM-OCR scored `95.22` overall on `v1.6_full`, which is strong
but no longer the top result because `MinerU2.5-Pro` is listed ahead at
`95.75`.

That makes GLM-OCR a credible OCR candidate rather than tweet noise, but the
evidence is still benchmark- and vendor-source-heavy. I did not find primary
source proof that it solves the live `doc-web` handwritten OCR blocker or that
it changes CineForge's current PDF-ingest shape enough to justify immediate
execution.

## Project Relevance

- **dossier**: Low direct relevance. This is mostly a target-repo OCR/runtime
  question rather than a portable Conductor methodology change.
- **storybook**: No current relevance beyond generic awareness. There is no
  live Storybook OCR pressure attached to this source.
- **doc-web**: Real future relevance. `doc-web` has a live blocked OCR line in
  Story 191 that explicitly waits for a materially stronger OCR substrate, and
  GLM-OCR's MIT license plus current benchmark standing make it a plausible
  future candidate worth handing off locally.
- **cine-forge**: Low direct relevance. CineForge's current PDF intake work is
  centered on readable screenplay extraction and normalization, where
  `ocrmypdf`-style recovery is already the active seam; rich table/layout OCR is
  not the current bottleneck.

## Recommendation

- Defer at the Conductor level and hand the note off to `doc-web`'s inbox.
- Do not create a new Conductor story or target-repo story yet. The honest next
  move is a repo-local triage decision in `doc-web`, not a cross-project work
  line.
- If `doc-web` reopens stronger-OCR evaluation later, benchmark GLM-OCR on two
  explicit seams only:
  - the blocked LOC handwritten pair from Story 191
  - one existing table-heavy scanned-page benchmark against the current
    incumbent/golden surfaces
- Do not assume the 2026-02-03 "SOTA" framing is still current, and do not
  treat the current benchmark placement as handwriting proof.

## Confidence

- Medium. The source is real and the current benchmark standing is supported by
  primary sources, but the fit to the live repo-specific failure surfaces is
  still unproven.

## Evidence

- `https://x.com/kimmonismus/status/2018706291489923372?s=12&t=uFZE-MuhgWdh1YErEZzLtQ`
- `https://huggingface.co/zai-org/GLM-OCR`
- `https://huggingface.co/docs/transformers/en/model_doc/glm_ocr`
- `https://arxiv.org/abs/2603.10910`
- `https://github.com/opendatalab/OmniDocBench`
- Inbox note: `GLM-OCR 0.9B`
- `Twitter Scraper` retrieved the source post and replies, but account lookup
  failed due a connector cookie error; the scouting decision therefore relies on
  the tweet payload plus the primary sources above.

## Open Questions

- Does GLM-OCR actually improve the blocked LOC handwritten fixtures in
  `doc-web`, or is its current strength mostly on benchmark document parsing?
- If `doc-web` evaluates it later, should the first proof be full-page OCR,
  page-window rescue, or a narrower table/layout comparison?
