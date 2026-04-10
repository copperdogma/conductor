# Scout 010 — Evaluate Axi for Better Browser Agent Tooling

**Source**: `https://axi.md/`
**Status**: Defer
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

Axi is a real, current browser-tooling project with a coherent claim: agent
interfaces should be judged less by "CLI vs MCP" ideology and more by whether
they minimize token waste, discovery friction, and multi-step coordination. The
official site and repo present ten design principles for agent-ergonomic CLIs
and a reference `chrome-devtools-axi` wrapper around `chrome-devtools-mcp`.

The useful insight is mostly methodological. Their strongest mechanisms are:
- combined operations like `open` and `click --query` that avoid
  navigate/snapshot round trips
- filtered, content-first output instead of dumping full snapshots or huge
  schemas
- contextual next-step hints and concise help
- specialized extraction commands such as `tables --url`

But the current benchmark boundaries matter. Axi's browser results were
measured on public, read-only sites using headless isolated
`chrome-devtools-mcp`, with one model family and no authenticated app flows.
That is not the same problem your tracked repos currently face. Storybook and
CineForge browser work is mostly local-dev or app-authenticated UI verification
through Claude-in-Chrome or Playwright; Doc Web's maintained web-page lane is a
checked static-HTML input seam, not live URL fetch or browser automation.

So this is worth keeping as a design-reference bundle, not as an adoption line.

## Project Relevance

- **dossier**: Low direct relevance. Dossier does not currently have a browser
  tooling bottleneck, though the interface-design principles are compatible with
  its general prompt/token discipline.
- **storybook**: Medium methodological relevance. Storybook already carries a
  browser-automation runbook for Claude-in-Chrome MCP. Axi does not solve the
  extension-specific connection/detach problems in that runbook, but its
  principles could inform any future repo-local browser helper scripts or CLI
  wrappers.
- **doc-web**: Low direct relevance. The maintained web-page lane is explicitly
  static checked HTML, and the repo explicitly avoids drifting into live-fetch
  or browser-driven behavior from that seam.
- **cine-forge**: Medium methodological relevance. CineForge has the strongest
  current browser-automation operational surface, including Playwright MCP
  troubleshooting and browser smoke scripts. Axi is interesting as a possible
  design model for future wrappers, but not as an immediate tool switch.

## Recommendation

- Defer direct adoption.
- Do **not** add Axi or `chrome-devtools-axi` as a tracked-project dependency
  right now, and do **not** open a target-project inbox note from this scout.
- Keep two reusable conclusions:
  - for agent-facing CLIs, the ten Axi principles are a good design checklist
    when building repo-local wrappers or helper tools
  - for browser automation specifically, combined action+observation commands
    and filtered result views are the real value, not the transport label
- Revisit only if one of these becomes true:
  - Storybook or CineForge decides to standardize on `chrome-devtools-mcp`
    instead of the current Claude-in-Chrome / Playwright split
  - a tracked repo starts building its own agent-facing browser helper CLI and
    needs a proven interaction pattern

## Confidence

- Medium-high. The source itself is clear and current, and the main uncertainty
  is not what Axi is but whether your future browser substrate choices will move
  closer to the benchmarked environment.

## Evidence

- Primary external sources:
  - `https://axi.md/`
  - `https://github.com/kunchenguid/axi`
- Local overlap / mismatch evidence:
  - `/Users/cam/Documents/Projects/Storybook/storybook/docs/runbooks/browser-automation.md`
  - `/Users/cam/Documents/Projects/cine-forge/docs/runbooks/browser-automation-and-mcp.md`
  - `/Users/cam/Documents/Projects/doc-web/README.md`
- Historical context:
  - inbox note: `Chrome remote debugging / live Chrome sessions`

## Open Questions

- If a tracked repo later builds its own browser-helper CLI, which Axi ideas
  matter most in practice: combined commands, filtered output, or ambient
  context?
- Are the current browser pain points actually protocol/interface problems, or
  mostly environment-specific issues like extension health, local server
  binding, and profile/session management?
