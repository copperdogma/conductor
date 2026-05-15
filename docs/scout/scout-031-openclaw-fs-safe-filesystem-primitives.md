# Scout 031 - Evaluate OpenClaw fs-safe for TypeScript Filesystem Hardening

**Source**: `https://x.com/steipete/status/2055179961535705327?s=12&t=uFZE-MuhgWdh1YErEZzLtQ`,
`https://fs-safe.io/`, and `https://github.com/openclaw/fs-safe`

**Status**: Reject
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

OpenClaw's `@openclaw/fs-safe` is a useful TypeScript/Node library for code
that must touch caller-controlled paths inside a trusted root. Its core value is
a capability-style `root()` API that centralizes path escape prevention,
symlink/hardlink policy, write verification, atomic writes, temp workspaces,
archive extraction, and secret-file helpers.

The idea is credible. The adoption case for the tracked repos is not.

The only close fit is Echo Forge's local asset and registry tooling. That code
does handle local paths around sound intake, registry review, studio recipes,
and served audio files, but the user clarified this functionality is
intentionally personal/operator-local rather than a shared hostile-input
surface. In that context, adding a new `0.x` filesystem security dependency,
plus its Node-version and optional Python-helper deployment shape, would create
more operational surface than it removes.

The useful lesson is still worth recording: if any tracked repo later exposes
Node filesystem operations to untrusted user uploads, archives, model-generated
paths, plugin inputs, or multi-user local services, the right shape is a
capability-root boundary rather than scattered `path.resolve` and
`startsWith` checks. That future lesson does not justify adoption now.

## Project Relevance

- **conductor**: `Reject`. Conductor supervises routing and docs, not a
  TypeScript runtime that accepts arbitrary filesystem paths.
- **dossier**: `Reject`. Dossier is not TypeScript-first for this boundary, and
  any filesystem hardening would need to be evaluated in its Python/runtime
  substrate instead.
- **storybook**: `Reject`. Storybook has TypeScript backend code, but no current
  evidence of a high-risk local path ingestion surface that justifies this
  dependency.
- **doc-web**: `Reject`. The relevant pipeline is not a Node/TypeScript
  filesystem service in the current tracked shape.
- **cine-forge**: `Reject`. CineForge's TypeScript surface is primarily UI/API
  client code; filesystem boundaries belong in the backend/runtime layer, not a
  Node UI dependency.
- **boardgame-ingester**: `Reject`. No current TypeScript/Node adoption surface
  was identified for this package.
- **roborally**: `Reject`. RoboRally's JavaScript file writes are deterministic
  local scenario/report outputs, not untrusted path handling.
- **echo-forge**: `Reject`. It is the closest technical fit, but the exposed
  tooling is personal local intake/auditioning infrastructure. Existing focused
  validation is enough unless the surface becomes multi-user, hosted, or fed by
  untrusted archives/paths.

## Recommendation

- Do not adopt `@openclaw/fs-safe` in any tracked repo now.
- Do not create target-repo inbox notes or stories.
- Keep this as a declined Conductor scout so the idea does not keep returning
  as ambient backlog pressure.
- Reopen only if a repo develops one of these concrete triggers:
  - a Node service accepts user-controlled file paths or archive uploads
  - model/tool output is used to choose read/write/delete paths
  - a local-only tool becomes hosted, multi-user, or network-exposed beyond a
    trusted operator machine
  - repeated ad hoc filesystem boundary checks become maintenance risk

## Evidence

- The X post announced OpenClaw's move from ad hoc filesystem hardening to a
  TypeScript `fs-safe` library and claimed large speedups for some file ops.
- `https://fs-safe.io/` describes `fs-safe` as safe filesystem primitives for
  Node.js apps that handle untrusted relative paths.
- The same docs position `root()` as the core capability-style boundary and
  explicitly say this is a library-level guardrail, not an OS sandbox.
- The GitHub README describes protection against `..`, symlink swaps, hardlink
  aliases, and TOCTOU rename races, with Node 20.11+ as the runtime floor and an
  optional POSIX Python helper for stronger fd-relative behavior.
- Local repo sampling on 2026-05-15 found TypeScript/Node surfaces mainly in
  Storybook, Echo Forge, CineForge UI/tooling, and RoboRally. Echo Forge was the
  only plausible pilot, and the user clarified its relevant intake surface is
  intentionally personal local tooling.

## Confidence

High. The source is clear, the decision is conservative, and the user's product
context removes the only near-term adoption case.

## Open Questions

- None for now. Revisit only if one of the concrete reopen triggers appears.
