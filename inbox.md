# Inbox

Use this file as the capture surface for cross-project work. Notes can be raw.
Triage is responsible for turning them into stories, scout missions, ADRs, or
explicit rejections.

## General

- OpenAI Symphony: https://openai.com/index/open-source-codex-orchestration-symphony/
  - THIS looks interesting... It might be a good meta-layer on top of what we've already built. The system and I could log work in Linear (or stick with stories), logging things that need to be built, bugs, issues found while building, etc. Symphony could manage the existing triage/create story/build story/validate loop. What do you think?

- Look at what other skills we should put subagents in. These are my thoughts, but I want you to think through what the highest value usages of subagents and verify-loop would be for the following skills, and whehter we shuold upgrade them or not:
  - Create Story may be a good one. An agent can do code exporations for what the story may impact. Checking best practices on the web for this problem/pattern could be subagents. Verify loop could keep checking alignment vs ideal/spec and keep checking the new plan vs existing code for completeness/edge cases.
  - Build Story could obviously be a good one. Some side-quest code could be done via subagents. So could code explorations for more planning/impact. As could writing tests and verifying already written code as the main loop moves on.
  - Validate could also use subagents, running different tests in parallel, double checking results vs plan in parallel, checking final solution vs ideal/spec, looking holistically at code to see if it's been architected well, etc.
