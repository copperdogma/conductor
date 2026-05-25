# Scout 040 - Evaluate Peter Steinberger GitHub Autotriage for Autonomous Work Boundaries

**Source**: `https://x.com/steipete/status/2058240758801420530?s=20`
and `https://github.com/steipete/agent-scripts/blob/main/skills/github-project-triage/SKILL.md`

**Status**: Adapt
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Peter Steinberger's May 23, 2026 X post describes a Codex autotriage skill that
reads each repo's `VISION.md`, then allows autonomous work only when an
issue/PR:

- fits the project vision
- can be inferred from code with high confidence
- has a clear fix
- can be live-tested

The public artifact behind the post is `github-project-triage` in
`steipete/agent-scripts`. It is a maintainer-facing GitHub triage skill, not a
general replacement for story-driven development. The useful local lesson is
the explicit promotion boundary: vision fit is necessary but not enough; the
candidate must also have code evidence, bounded implementation scope, and a
real verification path before it can move autonomously.

This strongly validates the local Ideal/spec/triage/work loop. The framework
already has the better local version of `VISION.md`: `docs/ideal.md`,
`docs/spec.md`, methodology state, graph context, stories, and validate/closeout
contracts. The gap is that our loop can state the autonomous eligibility
boundary more explicitly when recommending or executing work.

## Source Details

The X post says the skill uses guidelines plus repo `VISION.md` to decide which
issues/PRs can be worked on autonomously. Retrieved replies mostly reinforced
the same point: the interesting part is the filter, especially project fit,
high-confidence code inference, and live-testability.

The GitHub skill adds concrete operating rules:

- `triage` inside a repo scopes to the current GitHub project by default.
- Broad triage uses a fast queue-discovery tool first, then expands only the
  relevant detail pass.
- If `VISION.md` exists, it is read before judging autonomous fit.
- Local work starts only from a clean `main` checkout after `git pull --ff-only`;
  otherwise the agent stops and asks.
- Current-project triage lists open issues and PRs, then inspects enough detail
  to explain the surfaced items.
- Latest maintainer comments are routing instructions and must be read before
  acting.
- Autonomous mode processes eligible items sequentially until no safe item
  remains, a blocker requires the maintainer, or items are landed/closed/deferred
  with proof.
- Go candidates are bounded bugfixes, performance improvements, small UI/UX
  tweaks, docs fixes, tests/internal cleanup, and low-risk dependency/CI work
  with a clear verification path.
- Ask-first candidates include new features, product/vision choices, broad
  behavior changes, risky dependencies, security-sensitive changes without
  strong proof, live-provider work without credentials, and anything that cannot
  be end-to-end tested.
- Each item gets type, fit, risk, proof, blocker, trust, and exact next action.
- Before land/closeout, it runs Codex Auto Review unless trivial/docs-only,
  verifies locally and live when possible, ensures CI is green, then returns to
  clean `main` before selecting another item.

## Fit Against Conductor

Already covered locally:

- Ideal/spec/state/graph are the source of project fit for Conductor and the
  tracked repos.
- `/triage` already starts from Ideal, spec/state, existing work, and smallest
  honest artifact shape.
- `/build-story` has a plan gate before implementation and checks whether work
  belongs in Conductor or a target repo.
- `/validate` is the closure authority and already has Codex review guidance
  from Scout 032.
- Target-project edits are isolated in dedicated worktrees when Conductor must
  touch another repo.

Useful gap:

- Triage recommendations do not always name whether the recommended action is
  safe for autonomous execution after approval, needs human judgment first, or
  is blocked because it lacks a verification path.
- The story loop does not yet have one compact "autonomous-fit" checklist that
  combines Ideal/spec fit, code evidence, bounded fix, testability, checkout
  safety, and authority to continue.

## Project Relevance

- **conductor**: `Adapt`. Add the autonomous-work boundary to shared
  methodology wording first, especially `/triage` and possibly `/build-story`.
- **dossier**: `Defer`. Should inherit any shared wording later; no direct
  Dossier product story is warranted.
- **storybook**: `Defer`. Same. The idea is useful for issue/story selection,
  but only after Conductor shapes the portable boundary.
- **doc-web**: `Defer`. Good fit for bug/intake/parser tasks with strong proof,
  but no direct repo-local note yet.
- **cine-forge**: `Defer`. Useful for eval-backed bugfixes and provider work
  only when live credentials and proof are available.
- **boardgame-ingester**: `Defer`. Potentially useful for deterministic
  ingestion bugs, but not enough pressure for direct work.
- **roborally**: `Defer`. Potentially useful for scenario-engine bugfixes, but
  current story flow is already light.
- **echo-forge**: `Defer`. Useful for clear UI/runtime/audio bugs, but asset and
  taste work often needs human judgment and live review.

## Recommendation

Adapt the autonomous promotion boundary, not the whole GitHub queue workflow.
This provides enough value to add to the shared methodology because it sharpens
an already-important decision point: when a recommendation is safe to execute
after the operator says `yes`, when it needs another product/workflow judgment,
and when it is blocked by missing proof or unsafe workspace state. The overhead
is low if it stays as one visible boundary line and a short build-story
checklist.

Recommended Conductor follow-up:

- Create a focused Conductor story for the methodology wording.
  - Follow-up created:
    [Story 021](../stories/story-021-autonomy-boundary-methodology-update.md).
- Add an `Autonomy Boundary` line to `/triage` output for the one recommended
  action:
  - `Go after yes` when Ideal/spec fit is clear, evidence is local/current, the
    fix or artifact shape is bounded, and verification is available.
  - `Needs human judgment` when product direction, taste, cross-project policy,
    or broad behavior is the real decision.
  - `Blocked` when the work lacks credentials, repro, target checkout safety,
    or an honest validation path.
- Add a small checklist to `/build-story` Phase 1 or Phase 2 so plans explicitly
  state whether the story can proceed autonomously after approval, or whether it
  must pause again for a human decision.
- Keep direct GitHub issue/PR queue automation out of the shared default. It is
  useful only for repos where GitHub issues/PRs are the live work queue and the
  user explicitly asks for autonomous queue processing.
- Do not weaken the existing Conductor plan gate. The new boundary should make
  approval and continuation safer, not let stories skip human judgment.

No target-repo inbox notes are needed yet. This is a shared methodology
refinement; target projects should inherit it only after Conductor proves the
wording is useful.

## Rejected Adaptations

- Do not import RepoBar or Peter's queue tooling. Conductor's problem is not a
  public GitHub queue discovery problem.
- Do not require every repo to add `VISION.md`; our equivalent is the existing
  Ideal/spec/state package.
- Do not let "fits the vision" become enough to start work. The high-value idea
  is the full gate: fit, high-confidence evidence, bounded fix, and live or
  repo-native verification.
- Do not make "keep going" mean "process the whole backlog" unless the operator
  explicitly authorizes that batch mode.
- Do not add author-trust scoring to normal story work. Use it only for
  external GitHub PRs/issues where contributor identity changes review depth.

## Evidence

- The Twitter Scraper connector retrieved Peter's post and top-level replies.
- The `t.co` attachment resolves to the post's first image; it did not expose
  additional machine-readable details.
- GitHub code search found
  `steipete/agent-scripts/skills/github-project-triage/SKILL.md`.
- The current `agent-scripts` commit history shows recent updates to the triage
  skill, including `docs: document autonomous github triage` on 2026-05-22 and
  `docs: honor maintainer comments during triage` on 2026-05-23.
- Broader Twitter search and nested reply retrieval timed out after the initial
  connector pass, so this scout relies on the original post, retrieved replies,
  and the public GitHub skill.

## Confidence

High that the source validates the Ideal/spec/triage/work direction and that
the useful adoption is an explicit autonomous-work boundary. High enough to
create a small Conductor story now, because the current loop already behaves
this way implicitly and making the boundary visible should reduce both
over-asking and over-autonomy without creating a new artifact class.
