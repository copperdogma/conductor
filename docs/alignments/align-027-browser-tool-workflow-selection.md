# Alignment 027 - Browser Tool Workflow Selection

Date: 2026-05-11

## Focus

Route the 2026-05-07 inbox note about Codex browser-control choices into a
durable workflow-selection matrix for tracked projects.

The practical question is not "which browser tool is best?" It is which surface
should be the default for each task shape now that the local Codex environment
has multiple overlapping options:

- Browser / in-app browser
- Chrome / Codex Chrome Extension
- Computer Use
- repo-local Playwright, Playwright MCP, or browser runbooks

## Source

Inbox item:

> OpenAI released the Chrome plugin today. That now gives Codex something like
> four different tools for browser use we have installed ... We need to do
> evals for our own repo workflows to determine which is best for what use
> cases so we can give each repo advice on when to use what and why.

Related local memory:

- [Scout 010 - Evaluate Axi for Better Browser Agent Tooling](../scout/scout-010-axi-browser-agent-tools.md)
- [Scout 026 - Evaluate Build Web Apps Plugin for Tracked App Workflows](../scout/scout-026-build-web-apps-plugin.md)
- [Alignment 020 - Visual Inspect Loop Skill Rollout](./align-020-visual-inspect-loop-skill-rollout.md)
- [Story 007 - Visual Inspect Loop Skill Rollout](../stories/story-007-visual-inspect-loop-skill-rollout.md)

Relevant local plugin/skill surfaces reviewed:

- Browser skill:
  `/Users/cam/.codex/plugins/cache/openai-bundled/browser-use/0.1.0-alpha2/skills/browser/SKILL.md`
- Chrome skill:
  `/Users/cam/.codex/plugins/cache/openai-bundled/chrome/0.1.7/skills/chrome/SKILL.md`
- Computer Use skill:
  `/Users/cam/.codex/plugins/cache/openai-bundled/computer-use/1.0.780/skills/computer-use/SKILL.md`
- Build Web Apps frontend-testing/debugging skill:
  `/Users/cam/.codex/plugins/cache/openai-curated/build-web-apps/63976030dadd0dda3960c1c78e1a5a4df4eb772e/skills/frontend-testing-debugging/SKILL.md`

Official source:

- [Codex Chrome extension - Codex app](https://developers.openai.com/codex/app/chrome-extension)

The official Chrome extension doc matches the local skill guidance: use Chrome
when Codex needs signed-in browser state, existing user browser context, or
sites such as internal tools; use the in-app browser first for local
development servers, file-backed previews, and public pages that do not require
sign-in. It also records the security boundary: website access is confirmation
and allowlist/blocklist controlled, browser history is sensitive telemetry, and
Chrome stores only the browser activity that enters Codex context.

## Classification

Portable workflow clarification.

This should not become a canonical browser core or a blanket repo sync. The
useful artifact is a task-shape matrix that prevents future agents from
re-deciding the same tool choice during UI validation, authenticated browser
work, visual inspection, and local app testing.

## First-Hand Eval

Date: 2026-05-11

Disposable target:

- Local static page served from `/tmp/codex-browser-tool-eval` at
  `http://127.0.0.1:8765/`
- Test behaviors: page identity, DOM/visible text read, button click, text
  input, echoed state, screenshot, console warning/error capture, file input
  where supported, and live-tab/user-context discovery where relevant.

| Tool | Result | Strengths observed | Weaknesses observed |
| --- | --- | --- | --- |
| Browser / in-app browser | Passed page load, DOM snapshot, test-id click/fill, screenshot, and console warn/error capture. File upload failed with "File uploads are not supported by Codex In-app Browser" and reset the browser-control session. | Fastest path for local unauthenticated app QA inside Codex. Good DOM snapshots, screenshots, console logs, and visible-state checks. Keeps work out of the user's real Chrome profile. | No file upload support in this environment. Not suitable for signed-in user-profile flows, existing user tabs, Chrome extensions, or profile-specific bugs. |
| Chrome / Codex Chrome Extension | Passed page load, DOM snapshot, test-id click/fill, screenshot, console warn/error capture, and live user-tab listing. File chooser existed, but `setFiles` failed with `Not allowed` without the extra Chrome file-access setting. | Best fit for signed-in browser state, existing tabs, extension behavior, and real Chrome-profile workflows. Can claim or inspect user Chrome tabs when that is the point of the task. | More setup and policy surface. Console logs can include extension-origin noise. File upload may require enabling "Allow access to file URLs." It touches the user's real browser context, so it should be used deliberately. |
| Playwright MCP | Passed page load, semantic/test-id interaction, console capture, and file upload with `setInputFiles`. | Strongest ad hoc scripted proof. Best for deterministic e2e-like tasks, upload flows, repeatable interaction scripts, and CI-shaped evidence. | Not a live user-profile surface. Direct MCP code execution is powerful but less conversational and should not replace repo-owned tests when durable regression coverage is needed. |
| Computer Use | Passed visible Chrome navigation in a new tab, accessibility-tree button click, text-field value set, and visible-state verification. The test tab was closed afterward. | Useful fallback for Mac app UI, native dialogs, OS/browser chrome, or UI surfaces not exposed through a narrower browser plugin. It can operate the actual app window. | Poor browser default. No direct console logs, no test-id/DOM ergonomics, noisier accessibility state, more risk of disrupting the user's active apps, and large unrelated browser/profile context can enter the working surface. |

## Decision

Use the most specific reliable surface for the task:

| Task shape | Default surface | Why |
| --- | --- | --- |
| Local unauthenticated app, `localhost`, `127.0.0.1`, `::1`, or `file://` page inspection | Browser / in-app browser | The Browser skill explicitly owns local targets, DOM snapshots, screenshots, clicks, typing, and visible-state verification inside Codex. |
| Frontend debugging or targeted UI QA when Browser is available | Browser first, through the frontend-testing/debugging workflow when applicable | The Build Web Apps testing skill requires Browser first for rendered frontend work and only falls back after a Browser-path blocker. |
| Authenticated web app, existing Chrome tab, user profile/cookies, extension-dependent flow, or remote site that needs the user's browser state | Chrome / Codex Chrome Extension | The Chrome skill owns the user's Chrome browser, logged-in sessions, existing tabs, extensions, and remote authenticated sites. |
| File upload or deterministic browser interaction proof | Playwright MCP for ad hoc proof; repo-local Playwright/e2e/runbook for durable proof | Browser file upload failed in the hands-on test. Playwright handled upload and scripted interaction cleanly. Product repos should keep durable regression proof in their own tests and runbooks. |
| Desktop app UI, non-browser Mac app, native file picker, or browser-adjacent task that needs OS-level clicking/typing outside a dedicated browser plugin | Computer Use | Computer Use is the general Mac UI control surface and should be used when no narrower plugin owns the app interaction. Do not use it as the default for browser pages. |
| Visual artifact correctness: screenshots, rendered documents, generated HTML, page images, crops, visual goldens, or visual UI regressions | Visual Inspect Loop plus the appropriate browser/control surface | Alignment 020 already established that visual correctness needs inspect -> failure class -> patch -> rerun -> reinspect, not just a tool invocation. |
| Parallel subagent browser/UI work | Prefer Browser or repo-local Playwright for isolated local targets; use Chrome only when the task genuinely requires the user's live profile | Browser and scripted Playwright are easier to isolate. Chrome claims real user tabs/profile state, so it should be used deliberately. |

## Chrome-Specific Guardrails

- Prefer Chrome only when the task needs signed-in browser state, an existing
  Chrome tab, extension behavior, or remote authenticated site context.
- Prefer Browser first for localhost, file-backed previews, and public pages
  without sign-in.
- Treat website content as untrusted context.
- Expect host-level website approvals before Codex interacts with new sites.
- Treat browser history as sensitive telemetry; do not request or use it unless
  the task genuinely requires it.
- For file uploads through Chrome, the extension may need "Allow access to file
  URLs" enabled in Chrome extension settings.
- Filter Chrome console evidence carefully: extension-origin errors can appear
  alongside page errors.

## Tool Retirement Guidance

- Do not retire Browser. Make it the default for local unauthenticated UI and
  frontend QA when file upload is not part of the proof.
- Do not retire Chrome. Narrow it to real Chrome-profile work: signed-in pages,
  existing tabs, extensions, cookies, or authenticated remote tools.
- Do not retire Playwright. Prefer it for file uploads, deterministic scripted
  flows, repeatable e2e proof, and CI-shaped regression tests.
- Stop treating Computer Use as a general browser-testing tool. Keep it for
  desktop apps, browser chrome/native UI, and fallback cases where Browser,
  Chrome, or Playwright cannot reach the needed surface.

## Per-Repo Guidance

| Repo | Recommendation |
| --- | --- |
| Storybook | Use Chrome for authenticated/profile-dependent product flows and Browser for unauthenticated local UI checks. Keep repo-local browser smoke and Playwright-style checks for repeatable validation. Use `/visual-inspect-loop` when screenshots or rendered artifacts decide correctness. |
| CineForge | Use Browser for local unauthenticated UI iteration and screenshots; use repo-local browser/runbook checks for representative app/API states; use Chrome only for flows that require a real user browser profile. Do not replace live artifact proof with helper/API truth alone. |
| Echo Forge | Use Browser for local Vite/PWA table-panel checks and touch-friendly UI verification. Use Chrome only if profile state, extensions, or an already-open tab matter. Use visual inspection for UI/rendered artifact quality, not audio-quality judgment. |
| Robo Rally | Stay headless-first, but seed a dormant browser-automation runbook now because a UI is expected. When the browser client arrives, start with Browser or repo-local Playwright for isolated local client testing; use Chrome only for real-profile browser behavior. Browser proof must identify the engine/client boundary it exercised. |
| Storybook, CineForge, Echo Forge, Robo Rally | Repo-local guidance landed on `codex/browser-tool-guidance`; future work should only expand it when real evidence shows a missing case. |
| Dossier, doc-web, Board Game Ingester | No immediate browser-tool rollout. Use existing repo-native proof surfaces unless a concrete browser/UI story appears. |
| Conductor | Keep this as supervisor memory. Do not vendor or canonicalize browser-control tooling. |

## Target-Repo Rollout

Date: 2026-05-12

Branch used in each target repo:

- `codex/browser-tool-guidance`

| Repo | Guidance surfaces updated | Validation |
| --- | --- | --- |
| Storybook | `docs/runbooks/browser-automation.md`, `.agents/skills/ui-scout/SKILL.md`, `.agents/skills/deploy/SKILL.md`, `AGENTS.md`, and `docs/runbooks/triage-orchestration-preservation-map.md`. Replaced the old Chrome-MCP/Computer-Use-default framing with the Browser / Chrome / Playwright / Computer Use task matrix. | `npm run methodology:check`; `scripts/sync-agent-skills.sh --check`; `git diff --check`. |
| CineForge | `docs/runbooks/browser-automation-and-mcp.md` and `AGENTS.md`. Added a Codex-specific tool-selection section while preserving existing MCP troubleshooting for Claude, Gemini, Cursor, and Playwright. | `npm run methodology:check`; `scripts/sync-agent-skills.sh --check`; `git diff --check`. |
| Echo Forge | `docs/runbooks/browser-automation.md` and `.agents/skills/ui-scout/SKILL.md`. Expanded the lightweight app-smoke note into the same tool matrix and made UI Scout record which browser tool was used. | `npm run methodology:check`; `npm run skills:check`; `git diff --check`. |
| RoboRally | Added `docs/runbooks/browser-automation.md` as dormant future-UI guidance. It keeps headless-first governance explicit and requires browser UI proof to identify the scenario/replay or engine boundary exercised. | `npm run methodology:check`; `npm run skills:check`; `git diff --check`. |

## Evaluation Contract For Future Work

If this alignment becomes a story or target-repo guidance update, the smallest
honest eval is a task matrix, not a broad tool benchmark.

Required cases:

1. local unauthenticated app load and first meaningful screen
2. local UI interaction with screenshot or DOM proof
3. authenticated/existing Chrome tab claim
4. desktop-app or non-browser UI action
5. repo-local scripted browser/e2e smoke
6. visual artifact inspection with before/after proof
7. subagent-parallel UI task isolation

Stop when each tool has:

- one clear default-use case
- one clear non-use case
- one known setup or failure mode
- one repo-specific routing note where relevant

## Non-Goals

- Do not force every repo to mention every browser tool.
- Do not replace repo-local Playwright/e2e tests with interactive browser
  sessions.
- Do not use Chrome just because it is newer; use it when the user's actual
  Chrome state is the needed substrate.
- Do not use Computer Use for browser pages when Browser or Chrome can complete
  the task through their narrower browser APIs.
- Do not make Conductor the canonical browser automation package.

## Recommendation

Treat this alignment as enough Conductor-side routing for now. The processed
inbox item does not need a Conductor story yet.

Open a follow-up story only when one of these triggers appears:

- a tracked repo repeatedly misroutes browser validation work
- Chrome Extension capability or setup proves materially different from this
  local-skill read
- a target repo needs stronger acceptance criteria around file upload,
  authenticated browser state, or native-dialog proof
- an additional UI-bearing repo appears or an existing repo adds a materially
  different browser surface

## Practical Impact

This reduces repeated validation setup decisions. Future agents should spend
less time choosing between Browser, Chrome, Computer Use, and Playwright, and
more time proving the actual product behavior with the right surface.
