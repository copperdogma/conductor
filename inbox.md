# Inbox

Use this file as the capture surface for cross-project work. Notes can be raw.
Triage is responsible for turning them into stories, scout missions, ADRs, or
explicit rejections.

## General

- Idea: add state machine specs (if it makes sense) to story planning. Apparnetly this very much helps vibe coded app quality. Let's research and discuss.

- new model to eval: https://openai.com/index/gpt-5-5-instant/

- 20260506: Scout this: https://claude.com/blog/new-in-claude-managed-agents
  - Looks similar to a lot of stuff we do but we may be able to use some of its hardness/code/ideas in our projects.

- 20260507: OpenAI released the Chrome plugin today. That now gives Codex something like four different tools for browser use we have installed (playwright MCP, Codex Computer Use via Any App and Chrome, and... anoher one I think?) We need to do evals for our own repo workflows to determine which is best for what use cases so we can give each repo advice on when to use what and why.
  - Oh! Apparnetly you can use it with subagent so it would be perfect to use to test the UI in roborally when we get around to making it multiplayer

- HTML docs/views where it makes sense: This is kind of cool: https://x.com/trq212/status/2052809885763747935
  - I'm imaginging moving our core management docs over to something like this. If it's just text, like the ideal.md, it could be an html file with a nicer presentation. Instead of referecing docs via paths or notation in markdown we could just hyperlink to them. And some things that are data-heavy like the stories.md file or the like could be done in a better format for AI to worth with (like json) with an HTML view available for humans to look at, which would be much easier to understand. The stories could also be linked a lot better with hyperlinks plus there are a ton of broken-link tools and the like we could use for linting to make sure nothing goes astray.
  - I'd be worried about the cruft it would create. It's not usually just html, it's css, svg, image files, js, etc, etc. Maybe it doesn't matter because it's written and maintaned by AI and the benefits may outweigh the costs.
  - A lot of this could be stitched together in a project dashboard, linking to the ideal and spec, showing the active and upcoming stories, perhaps showing the pipeline runs or latest evals if applicable, etc.

- Aspriational Eval: [I added this to echoforge's inbox, but this is something that I want in basically every single one of my AI applications. We've currently added them as one-offs to all or most of them right now. So I want you to do two things with this. Do a scout across all of our repos to see which ones are missing aspirational evals in which areas. This is going to take a long time because you have to really deeply understand the code and what API calls are being made now to figure out which might be eliminated with a better AI model. And I want to add something like this into the setup methodology. Like, we need this somewhere in every repo so that as we create new work, something in there triggers the AI to say, hey, one day we might not need this work. Let's create an aspirational eval around it. ]
  - ECHO-FORGE NOTE: One of the core tenets of all of my applications is that AI will eventually get better and we need evals in place to understand when they've achieved a new level where we can delete some complexity out of the application. For instance, right now, the DM pushes the push-to-talk button, rambles off a description. We use a cheap model to convert that into a JSON sound inventory out of that description. Then we use another model, or we use that as the basis of a search to search our system to find sounds that best match that. In the future, likely what we do is make one AI call with the audio speech that the DM spoke aloud. And our entire sound library feed all that into an AI model and it would come back with just the perfect soundscape for us. We likely can't do that yet. It's just too big, too much context, too expensive. So we have this intermediate step to build a search prompt, but we do need the eval for that much more difficult AI operation that just takes in speech and our entire audio library catalog. So we do need to build evals for that and other operations like that now and start running them. We only need a baseline, run them for everything currently. And then every time a new state-of-the-art model comes out, we rerun these aspirational evals to see if we can simplify the application now.

- PromptFoo: I was working with AI in the EchoForge project, and I told it to set up evals, and it began writing its own eval setup from scratch. We've kind of landed on PromptFoo as our eval framework. How can we make that a little more obvious in new repos we create using setup methodology? How do you suggest we set this up and how do you suggest we take care of this class of things, where we want to give our new repos an opinionated leg up on infrastructure if they choose to use it? And would a premade runbook help?
