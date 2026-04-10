# Scout 009 — Evaluate RepoProver for Textbook Intake and Verification

**Source**: `https://github.com/facebookresearch/repoprover`
**Status**: Spike
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

Queued from the inbox as a textbook-intake lead with prior ad hoc exploration.
The likely value is whether RepoProver exposes techniques for document intake,
verification, or structured extraction that could help Doc Web or related
workflows.

## Project Relevance

- **dossier**: Relevant if it offers reusable methodology for structured
  document analysis or verification.
- **storybook**: Lower direct relevance unless the techniques generalize to
  content ingestion or narrative verification.
- **doc-web**: Highest relevance because the note explicitly frames this as a
  textbook-intake opportunity.
- **cine-forge**: Low direct relevance unless the verification patterns are
  broadly portable.

## Recommendation

- Run a `/scout` pass focused on what concrete intake or verification ideas are
  actually transferable, then decide whether the next step is `Adapt`, `Spike`,
  or `Reject`.

## Evidence

- `https://github.com/facebookresearch/repoprover`
- `https://chatgpt.com/c/69d29053-5468-83e8-a30e-2382f1a18ae2`
- Inbox note: `Already scouted a bit with ChatGPT and many things to take/try`

## Open Questions

- Which parts are useful beyond the original research setting?
- Does the best follow-up belong in Doc Web, Dossier, or a shared eval lane?
