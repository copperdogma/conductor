# Scout 037 - Evaluate Google Antigravity Skills and CLI for Skill Wrapper Retirement

**Source**:
`https://x.com/altryne/status/2056794446021468419?s=20`,
`https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/`,
`https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/`,
`https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/`,
`https://antigravity.google/docs/skills`,
`https://antigravity.google/docs/cli-features`,
and `https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/using-agent-skills.md`

**Status**: Adapt
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Reviewed Google's May 19, 2026 Antigravity/Gemini developer-tool rollout.
The linked X post is item 20 in an I/O roundup thread and points at the
broader AI Studio rollout, not the skill interface itself. The relevant
first-party docs are Google's Managed Agents announcement, the Gemini CLI to
Antigravity CLI migration post, and Antigravity/Gemini CLI skill docs.

The important change for Cam's distributed skill surface is that Google now
supports the same basic `SKILL.md` package shape in the standard
`.agents/skills` workspace location:

- Antigravity documents skills as folders containing `SKILL.md`, with
  workspace skills under `<workspace-root>/.agents/skills/<skill-folder>/`.
- Antigravity global skills live under `~/.gemini/antigravity/skills/`.
- Antigravity says it now defaults to `.agents/skills`, while keeping backward
  support for the older `.agent/skills`.
- Gemini CLI discovers user skills from `~/.gemini/skills/` or
  `~/.agents/skills/`, and workspace skills from `.gemini/skills/` or
  `.agents/skills/`.
- Gemini CLI's `SKILL.md` format requires YAML frontmatter with `name` and
  `description`, matching the repo-local skill format already used here.
- Google's Gemini CLI to Antigravity CLI transition post says Antigravity CLI
  preserves Agent Skills, Hooks, Subagents, and Extensions, although not every
  Gemini CLI feature has immediate one-to-one parity.

This means the old Google-specific wrapper generation should no longer be
needed as a skill-discovery mechanism. In this repo, `scripts/sync-agent-skills.sh`
already keeps `.agents/skills` as the canonical skill directory and generates
`.gemini/commands/*.toml` wrappers only for Gemini. That wrapper layer can
probably be retired or downgraded to optional slash-command aliases after a
small smoke test.

## Project Relevance

- **conductor**: `Adapt`. Conductor owns the cross-project skill-sync
  contract. The likely next move is an alignment/story to stop treating
  `.gemini/commands` wrappers as required skill-sync output.
- **dossier**: `Adapt later`. Dossier should keep repo-local skills in
  `.agents/skills`; wrapper retirement should follow Conductor's alignment
  decision and Dossier's own skill check update.
- **storybook**: `Adapt later`. Storybook has prior wrapper-regeneration memory
  and should benefit from removing a stale generated surface, but only after
  confirming its current Gemini/Antigravity workflow does not rely on slash
  command wrappers.
- **doc-web**: `Adapt later`. Same canonical skill benefit; no unique Google
  runtime pressure beyond existing Gemini API scouting.
- **cine-forge**: `Adapt later`. Same skill-surface simplification applies, but
  do not mix it into active provider/model eval work.
- **boardgame-ingester**: `Adapt later`. Same generated-wrapper cleanup applies
  if its current checks still count Gemini wrappers.
- **roborally**: `Adapt later`. Keep the headless-first boundary; this is only
  tool-surface cleanup, not product work.
- **echo-forge**: `Adapt later`. Same cleanup applies, but should be done in an
  isolated worktree because Echo Forge often has active asset/UI work in
  progress.

## Recommendation

Adopt `.agents/skills/<skill>/SKILL.md` as the sole canonical repo skill
surface for Google-aware tools too.

Keep lightweight compatibility links where they cost almost nothing, such as
`.claude/skills -> .agents/skills`, `.cursor/skills -> .agents/skills`, and
possibly `skills -> .agents/skills`, until each tool's current behavior is
verified. Stop generating Google-specific `.gemini/commands/*.toml` files as
required skill wrappers unless a repo explicitly wants them as slash-command
aliases.

The caveat is UX, not skill compatibility. `SKILL.md` discovery lets an agent
activate a skill by description or by name. It does not automatically prove
that typing `/triage` in every Google surface will behave exactly like the old
custom command wrapper. If a repo depends on slash-command spelling, preserve
that as an explicit command-alias concern rather than calling it skill sync.

Concrete next move:

1. In Conductor, create a small alignment/story for "retire generated Gemini
   skill wrappers".
2. Update `scripts/sync-agent-skills.sh` so `--check` validates canonical
   `.agents/skills` plus any cheap symlinks, not `.gemini/commands` parity.
3. Run one live smoke in Antigravity CLI or current Gemini CLI:
   after trusting the workspace, `/skills list` should show repo skills from
   `.agents/skills`.
4. If slash command UX is still needed, keep a separate optional command-alias
   generator with a different check name.
5. Roll the script/check update across tracked repos through isolated
   worktrees.

## Evidence

- Google's Managed Agents announcement says the Gemini API can run the
  Antigravity agent in an isolated Linux environment and custom agents can be
  defined with markdown files such as `AGENTS.md` and `SKILL.md`.
- Google's I/O developer highlights say Antigravity 2.0, Antigravity CLI, and
  Antigravity SDK now share an Antigravity agent harness, and Managed Agents
  let developers extend agents with custom instructions and skills using
  markdown files.
- Google's Gemini CLI to Antigravity CLI transition post says Antigravity CLI
  preserves Agent Skills, Hooks, Subagents, and Extensions, while warning that
  not every feature has immediate one-to-one parity.
- Antigravity's skills docs describe a skill as a folder containing `SKILL.md`,
  list workspace skills at `.agents/skills/<skill-folder>/`, list global skills
  at `~/.gemini/antigravity/skills/<skill-folder>/`, and say Antigravity now
  defaults to `.agents/skills`.
- Gemini CLI's official docs list `.agents/skills` as an alias for both user
  and workspace skills and document `/skills` plus `gemini skills` management.
- Gemini CLI's creation docs show the same `SKILL.md` frontmatter pattern used
  locally: `name` and `description`, followed by markdown instructions and
  optional `scripts/`, `references/`, and `assets/`.
- Current Conductor script evidence: `scripts/sync-agent-skills.sh` uses
  `.agents/skills` as canonical, creates `.claude/skills`, `.cursor/skills`,
  and `skills` symlinks, and separately writes `.gemini/commands/*.toml`
  wrappers.
- Local Gemini CLI smoke on this worktree did not load project skills because
  the folder is not trusted; that matches Gemini CLI's documented trust gate
  for workspace skills and leaves the Antigravity/Gemini live proof as a small
  follow-up rather than a blocker to the scout conclusion.

## Confidence

High that `.agents/skills` is now the right Google-compatible workspace skill
location. Medium-high that the `.gemini/commands` wrapper layer can be removed
portfolio-wide, because the remaining uncertainty is slash-command ergonomics
and per-repo check expectations, not `SKILL.md` support.

## Open Questions

- Does Antigravity CLI's current `/skills` panel list workspace skills from
  every active Project folder, or only the current terminal working directory?
- After running `/trust` or an equivalent trust setup, does the local Gemini CLI
  list this repo's `.agents/skills` exactly as documented?
- Do any tracked repos still depend on `.gemini/commands/*.toml` for typed
  slash commands rather than skill activation?
- Should `scripts/sync-agent-skills.sh` keep creating `.gemini/skills` as a
  symlink for older Gemini CLI builds, or is `.agents/skills` enough after the
  Antigravity migration?
