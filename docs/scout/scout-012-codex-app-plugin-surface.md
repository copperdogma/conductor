# Scout 012 — Evaluate Codex App Plugin Surface Across Desktop and Mobile

**Source**: `https://x.com/dimillian/status/2041948910512652313?s=46&t=uFZE-MuhgWdh1YErEZzLtQ`
**Status**: Defer
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

Reviewed the 2026-04-08 X post plus current OpenAI help and release notes. The
important clarification is that Codex plugins are not a mobile app-extension or
product-integration surface. They are installable Codex workflow bundles that
package skills, optional app integrations, and MCP server configurations for
Codex users.

That makes this primarily a workflow-distribution feature for people already
using Codex across app, CLI, IDE, web, and connected workspace surfaces. It is
not a direct plugin channel for Storybook, doc-web, or CineForge end users.

The useful remaining angle is narrower: if Storybook eventually starts real
native macOS or iOS app work, plugins may become a good way to package the
Codex workflow for that repo once the local native-builder skills and toolchain
patterns are already proven. In other words, this is not a product feature, but
it could become a workflow accelerator for native app development later.

The original X thread is useful mainly as market signal: people are interested,
some saw feature-flag gating on Mac business accounts, and several replies
asked about CLI or iOS support. But the real product meaning comes from the
official documentation, not the thread.

## Project Relevance

- **dossier**: `Defer`. Possible future value if Dossier wants to package a
  stable internal Codex workflow bundle, but it does not help Dossier's product
  surface directly.
- **storybook**: `Defer`. This does not create a Storybook plugin platform or
  mobile integration path, but it could help later if Storybook starts a native
  macOS or iOS repo and wants to package a stable Codex-native-builder workflow
  for reuse across app, CLI, and IDE surfaces.
- **doc-web**: `Defer`. No direct product benefit. Possible internal-tool value
  only if Doc Web needs reusable Codex workflow packaging later.
- **cine-forge**: `Defer`. Same reasoning as Storybook: possible internal
  builder workflow value, but not a product-facing integration.

## Recommendation

- Keep this at `Defer`.
- Do not treat Codex plugins as a current product opportunity for the tracked
  projects.
- Hand this off to Storybook's `docs/inbox.md` as a future native-app workflow
  note rather than keeping it only in Conductor.
- Revisit when Storybook begins concrete native macOS or iOS work. The right
  sequence would be:
  1. prove the local Xcode/native workflow with repo-local skills first
  2. package that workflow as a plugin only if it becomes stable and reused
- No Conductor story is warranted now because the immediate value is future
  Storybook workflow packaging, not supervisor-side execution.

## Evidence

- `https://x.com/dimillian/status/2041948910512652313?s=46&t=uFZE-MuhgWdh1YErEZzLtQ`
- `https://help.openai.com/en/articles/11369540`
- `https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes`
- Inbox note: `Storybook in particular would benefit from this`
- Official help says plugins package reusable Codex workflows and can combine
  skills, app integrations, and MCP server configurations.
- Official help also says Codex app availability is macOS and Windows, while
  workspace controls apply across surfaces including ChatGPT mobile.
- Handoff recorded in Storybook inbox:
  `/Users/cam/.codex/worktrees/conductor-storybook-scout-012/docs/inbox.md`
- X replies surfaced unresolved questions about account gating, CLI coverage,
  and iOS demand rather than clear evidence of a mature mobile plugin path.

## Confidence

- High on the product-shape conclusion. The official docs are explicit that
  plugins are a Codex workflow distribution unit, not a general product plugin
  surface.

## Open Questions

- If one tracked project eventually wants a shared internal Codex workflow kit,
  would plugins be meaningfully better than repo-local skills plus setup docs?
- Are the current workspace controls and account-gating behavior stable enough
  for broader internal adoption, or is the surface still too fresh?
