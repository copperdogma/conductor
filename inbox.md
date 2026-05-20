# Inbox

Use this file as the capture surface for cross-project work. Notes can be raw.
Triage is responsible for turning them into stories, scout missions, ADRs, or
explicit rejections.

## General

- Idea: add state machine specs (if it makes sense) to story planning. Apparnetly this very much helps vibe coded app quality. Let's research and discuss.

- 20260506: Scout this: https://claude.com/blog/new-in-claude-managed-agents
  - Looks similar to a lot of stuff we do but we may be able to use some of its hardness/code/ideas in our projects.

- HTML docs/views where it makes sense: This is kind of cool: https://x.com/trq212/status/2052809885763747935
  - I'm imaginging moving our core management docs over to something like this. If it's just text, like the ideal.md, it could be an html file with a nicer presentation. Instead of referecing docs via paths or notation in markdown we could just hyperlink to them. And some things that are data-heavy like the stories.md file or the like could be done in a better format for AI to worth with (like json) with an HTML view available for humans to look at, which would be much easier to understand. The stories could also be linked a lot better with hyperlinks plus there are a ton of broken-link tools and the like we could use for linting to make sure nothing goes astray.
  - I'd be worried about the cruft it would create. It's not usually just html, it's css, svg, image files, js, etc, etc. Maybe it doesn't matter because it's written and maintaned by AI and the benefits may outweigh the costs.
  - A lot of this could be stitched together in a project dashboard, linking to the ideal and spec, showing the active and upcoming stories, perhaps showing the pipeline runs or latest evals if applicable, etc.

- Triage ADR: We might need a triage skill specific to ADRs. So I've been noticing a pattern in it. We start talking about something, we create an ADR, then the steps forward aren't always clear. It's sort of a rambling conversation, which is great. Sometimes that's what you need to start it, but at one point the user becomes uncertain as to the state of the ADR and what's left and what's next and that sort of thing. So triaging an ADR would basically be going through identifying all the decisions that remain to be made, and I'd like to split it into two categories within those. One is more opinion-based decisions that mostly fall on the user for preferences for how something should work, especially when they have downstream consequences. And the second category is more technical decisions. So if the decision is something like, you know, what file format should be used for this, YAML or JSON, we're gonna assume the user doesn't really care about that sort of thing in an AI-written application. So any more technical, less opinion-based decisions like that, the AI should put a lot of time into thinking about each and making its recommendation. The third part of triage is how far along are we in the ADR, what's left to do. And the fourth part is, if the ADR seems to be complete from a decision standpoint, the triage should suggest that the next step should be to align it because there are no real decisions left to be made in it. Everything's more or less been decided. So this skill could be invoked specifically by the user if they want, but this should be the default loop, a skill that the AI should itself call on a regular basis when working through an ADR with the user to help guide the process.
