# Scout 022 — Evaluate Axios Compromise Note for Cross-Project Dependency Risk

**Source**: `https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan`
**Status**: Reject
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

Queued from the inbox as a dependency-risk note. A 2026-04-10 repo search found
no `axios` hits across Dossier, Storybook, Doc Web, or CineForge, so there is
no live cross-project action surface right now.

## Project Relevance

- **dossier**: No current relevance because `axios` does not appear in the
  checked project tree.
- **storybook**: No current relevance on the same basis.
- **doc-web**: No current relevance on the same basis.
- **cine-forge**: No current relevance on the same basis.

## Recommendation

- Reject for the current tracked projects. Reopen only if `axios` enters a
  manifest, lockfile, or incident-review scope later.

## Evidence

- `https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan`
- 2026-04-10 `rg` search across tracked project trees returned no `axios`
  dependency hits.

## Open Questions

- None for now.
