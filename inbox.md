# Inbox

Use this file as the capture surface for cross-project work. Notes can be raw.
Triage is responsible for turning them into stories, scout missions, ADRs, or
explicit rejections.

## General

- 2026-09-19: Evaluate the models deferred from Dossier while development was
  active, one at a time. Routed to [Alignment 047](docs/alignments/align-047-dossier-model-catchup.md);
  the applicable historical queue and exclusions are reconciled there.
  Follow-through approved: resolve the ordinary benchmark contradictions in the
  same isolated owner worktree, preserving the original model evidence.
  Subsequent direct-runtime audit corrected the ordinary-lane scope; approved
  standalone Dossier semantic benchmark was built and tested as owner Story170 in
  its own worktree, with no consumer coupling. The subsequently authorized
  serial comparison is complete:17 callable models screened, no cheaper
  replacement established, US$3.66071209916 conservative accounted cost.

- Idea: add state machine specs (if it makes sense) to story planning. Apparnetly this very much helps vibe coded app quality. Let's research and discuss.

- 20260506: Scout this: https://claude.com/blog/new-in-claude-managed-agents
  - Looks similar to a lot of stuff we do but we may be able to use some of its hardness/code/ideas in our projects.

- HTML docs/views where it makes sense: This is kind of cool: https://x.com/trq212/status/2052809885763747935
  - I'm imaginging moving our core management docs over to something like this. If it's just text, like the ideal.md, it could be an html file with a nicer presentation. Instead of referecing docs via paths or notation in markdown we could just hyperlink to them. And some things that are data-heavy like the stories.md file or the like could be done in a better format for AI to worth with (like json) with an HTML view available for humans to look at, which would be much easier to understand. The stories could also be linked a lot better with hyperlinks plus there are a ton of broken-link tools and the like we could use for linting to make sure nothing goes astray.
  - I'd be worried about the cruft it would create. It's not usually just html, it's css, svg, image files, js, etc, etc. Maybe it doesn't matter because it's written and maintaned by AI and the benefits may outweigh the costs.
  - A lot of this could be stitched together in a project dashboard, linking to the ideal and spec, showing the active and upcoming stories, perhaps showing the pipeline runs or latest evals if applicable, etc.
