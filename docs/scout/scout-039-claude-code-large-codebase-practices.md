# Scout 039 - Evaluate Claude Code Large-Codebase Practices for Harness Navigation

**Source**: `https://x.com/claudedevs/status/2056403446056784288?s=12&t=uFZE-MuhgWdh1YErEZzLtQ`
and `https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start`

**Status**: Adapt
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

The X post announces Anthropic's May 14, 2026 Claude Code at scale article
about large codebases, legacy systems, and distributed microservice estates.

The useful local lesson is not Claude-specific adoption. The useful lesson is
that agent performance at real repo scale depends on the harness around the
model: lean root instructions, local path context, command scoping, generated
file exclusion, skills loaded only when needed, structured tool access, code
navigation, read-only exploration before editing, and one owner keeping those
surfaces current.

Cam's current framework already has strong equivalents for many of those
ideas: `AGENTS.md`, `.agents/skills`, compatibility links, source-specific
content connectors, explicit subagent contracts, isolated worktrees,
repo-local validation, and Conductor as the supervisor that compares
distributed harness surfaces. The high-value gap is narrower: make
"navigation quality" and "context debt" first-class review topics across the
tracked repos, without creating a heavyweight canonical core.

## Project Relevance

- **conductor**: `Adapt`. Conductor should own the shared review pattern:
  evaluate whether repo instructions are lean, whether generated/noisy files
  are excluded from agent attention, whether path-specific commands are easy to
  find, and whether stale model-compensation rules should be removed after tool
  or model upgrades.
- **dossier**: `Adapt later`. Strong fit for path-specific extraction,
  GEDCOM, document, and eval commands. Do not add new pressure until a
  Conductor review identifies stale instructions or missing navigation maps.
- **storybook**: `Adapt later`. Strong fit because native Dossier integration,
  memory research, UI, and family-data paths can need different local commands
  and constraints. Treat this as cleanup/review pressure, not a product story.
- **doc-web**: `Adapt later`. Good fit for pipeline path maps, crop/OCR
  evidence commands, and generated artifact exclusion. Its current proof still
  belongs in driver outputs and artifact checks.
- **cine-forge**: `Adapt later`. Strong fit for path-specific commands and
  generated media/runtime exclusions because the repo mixes app code, prompts,
  renders, evals, and deployment surfaces.
- **boardgame-ingester**: `Defer`. Useful once the rulebook/component pipeline
  grows, but current value is lower than deterministic ingestion and evidence
  work.
- **roborally**: `Defer`. The repo is still small enough that the main benefit
  is keeping headless scenario truth obvious; a broad navigation audit would be
  premature.
- **echo-forge**: `Adapt later`. Strong fit because active work spans UI,
  asset catalogs, local services, generated audio/icons, and review surfaces.
  Any rollout should use isolated worktrees because primary checkout work is
  often active.

## Recommendation

Create a Conductor-owned follow-up for "harness navigation and context-debt
review" before touching target repos.

Follow-up created: [Story 020](../stories/story-020-harness-navigation-context-debt-review.md).
Inventory result recorded in [Alignment 038](../alignments/align-038-harness-navigation-context-debt-review.md).
Alignment 038 is the controlling post-inventory recommendation: do not
implement the candidate guidance below as a rollout queue unless a repo-local
failure mode clears the expected-value and overhead gate.

Recommended first scope:

1. Audit Conductor plus the tracked product repos for root instruction bloat,
   stale process rules, and instructions that compensate for old model/tool
   limitations.
2. Treat `docs/build-map.md`, README setup sections, local-service scripts,
   and setup checklists as the local equivalent of codebase maps and
   path-command tables. Improve those only where the repo already has
   confusing multi-surface navigation.
3. Add a lightweight context-debt review trigger to shared methodology: review
   AGENTS/skills/setup guidance every 3-6 months, after major model/tool
   upgrades, or when agent performance plateaus.
4. Add optional guidance for path-scoped validation commands: a repo should
   make the cheapest relevant lint/test/eval command discoverable near the
   path or workflow that needs it.
5. Add optional guidance for generated-file and dependency-artifact exclusion:
   keep build outputs, generated media, dependency folders, and third-party
   bundles out of routine agent context unless the task explicitly works on
   those artifacts.
6. Evaluate LSP/code-intelligence support as a spike only for repos where text
   search is repeatedly selecting the wrong symbol or module. Do not add a
   blanket LSP requirement.

Do not create target-repo inbox notes yet. This is a cross-project methodology
and harness-maintenance idea; Conductor should shape the shared review first,
then create repo-specific work only for concrete gaps found by that review.

## High-Value Ideas To Reuse

- **Context budget as an asset**: keep root instructions short and move
  reusable expertise into skills or path-local documentation.
- **Live evidence over stale indexes**: prefer current files, current tests,
  and repo-native search over cached assumptions.
- **Path-scoped commands**: make the cheapest honest command for a changed
  area discoverable so agents do not default to noisy full-suite runs or weak
  no-op validation.
- **Context-debt review cadence**: periodically delete stale instructions,
  especially rules written to compensate for older model behavior.
- **Read-only scouts before edits**: keep the established local pattern where
  exploration can be delegated or isolated, but the main thread owns final
  edits and validation disposition.
- **Harness ownership**: Conductor is already the agent-manager equivalent;
  use that role to compare distributed surfaces and recommend sync, not to
  centralize every instruction file.

## Evidence

- The X post by `ClaudeDevs` announces a blog post on Claude Code best
  practices for multi-million-line monorepos, decades-old legacy systems, and
  distributed microservices.
- The linked Claude blog says Claude Code navigates from the live local
  codebase using the filesystem, file reads, grep, and references rather than
  relying on a maintained codebase index.
- The blog identifies the harness as a major driver of performance and lists
  `CLAUDE.md` files, hooks, skills, plugins, MCP servers, LSP integrations,
  and subagents as the relevant setup layers.
- The configuration guidance emphasizes lean/layered instruction files,
  starting in relevant subdirectories, path-specific test/lint commands,
  generated-file exclusions, codebase maps for confusing structures, and LSP
  support for symbol-level navigation.
- The blog recommends meaningful configuration reviews every 3-6 months and
  after major model releases because older instructions and hooks can become
  constraining as models and tools improve.
- The blog also describes a dedicated agent-manager or DRI role for owning the
  coding-agent setup, conventions, permissions, plugin/skill governance, and
  adoption roadmap.
- Retrieved replies to the X post reinforced the same practical concerns:
  shared state, stale instruction cleanup, wrong-context retrieval, multi-repo
  dependency understanding, and auditable evidence plumbing.
- Local Conductor evidence shows the framework already has canonical
  `.agents/skills`, `.claude/skills` compatibility links, subagent contract
  alignments, setup-methodology guidance, local runtime allocation, and
  worktree bootstrap guidance.

## Confidence

High that the source validates the current Conductor direction and identifies
a worthwhile context-debt/navigation review. Medium on LSP/tooling adoption,
because the benefit depends on each repo's language, current editor/tool
surface, and whether wrong-symbol retrieval is a real observed failure.

## Open Questions

- Should the context-debt review live as a new Conductor story, or be folded
  into the next `/setup-methodology refresh` story?
- Which repos have actually suffered from wrong-file or wrong-symbol edits
  often enough to justify an LSP/code-intelligence spike?
- Should generated-file exclusion be recorded as repo-local guidance only, or
  should Conductor define a shared comparison checklist for dependency folders,
  build outputs, generated media, and third-party code?
- What is the smallest proof that a repo's path-command table is working:
  a successful targeted validation during one real story, or a static check
  that required command surfaces exist?
