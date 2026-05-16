# Scout 034 - Evaluate Clawpatch for Automated Repo Review

**Source**: `https://x.com/steipete/status/2055657966515155293?s=46&t=uFZE-MuhgWdh1YErEZzLtQ`,
`https://clawpatch.ai/`, `https://github.com/openclaw/clawpatch`, and
`https://www.npmjs.com/package/clawpatch`

**Status**: Spike
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Clawpatch is an early CLI for repo-wide AI code review. It maps a repository
into semantic feature records, asks a provider to review bounded context,
persists findings under a project-local state directory, and can run an
explicit fix loop for one finding at a time.

This is adjacent to, but broader than, Scout 032's `codex-review` workflow.
`codex-review` is a closeout signal for the current diff. Clawpatch is a
latent-bug discovery tool for code that may not be changing right now. That
makes it interesting, but also riskier operationally: it can produce a backlog
of speculative findings, create `.clawpatch/` state, and eventually apply code
changes if the `fix` path is used.

The right move is optional detector guidance inside
`/codebase-improvement-scout`, not always-on adoption. Roll the report-only rule
into repos that already have that lane and let first natural use be the pilot.
Do not run `clawpatch fix` during scout-mode use. The useful question is
whether Clawpatch finds concrete, verified bugs that Cam's existing
`/validate`, `/loop-verify`, and optional `codex review` closeout signals would
not have surfaced cheaply.

## Recommendation

- Treat Clawpatch as an optional periodic `/codebase-improvement-scout`
  detector for stale, high-churn, thinly-tested, pre-release, or pre-cleanup
  code areas.
- Roll optional guidance into the existing target-repo
  `codebase-improvement-scout` skills now; the first natural use in each repo
  is the pilot.
- Pin the tool version, record the exact package/source used, and keep generated
  state outside the repo when possible with `--state-dir`.
- Run only the read/report path: `init`, `map`, a small `review --limit`, and
  `report`.
- Manually verify any findings against source and repo-native tests before
  treating them as real work.
- If a repo's natural use exposes noisy findings, poor framework coverage, or a
  better local rule, fix that repo first and distribute the improved wording via
  Conductor alignment when it generalizes.

Do not add Clawpatch to normal validation, CI, or target-project stories yet.
Do not route repo-local inbox items from unverified findings.

## Project Relevance

- **conductor**: `Spike`. Conductor should own the pilot decision and the
  adoption rule inside `/codebase-improvement-scout`. This is a cross-project
  detector-guidance problem, not a product feature.
- **dossier**: `Spike`. Roll optional guidance into the lane, but record
  unsupported tool coverage if the pinned package lacks Python mapping.
- **storybook**: `Spike`. Strong natural-use candidate because it is a large
  TypeScript monorepo; keep findings manually verified and story-bounded.
- **doc-web**: `Spike`. Same Python caveat as Dossier; artifact/driver truth
  remains the proof surface.
- **cine-forge**: `Spike`. Mixed Python/JavaScript surface with real product
  pressure; provider/runtime/artifact-flow truth outranks generic scanner
  claims.
- **boardgame-ingester**: `Spike`. Roll optional guidance into the lane, but
  record unsupported tool coverage if there is no compatible package surface.
- **roborally**: `Spike`. Compact JavaScript repo with deterministic scenario
  behavior and tests, so it remains a good first natural-use target.
- **echo-forge**: `Spike`. Active TypeScript/Vite app with tooling scripts;
  browser/live-scene and audio behavior remain the proof surface.

## Spike Shape

Suggested first-run envelope:

```bash
npm view clawpatch@0.1.0 version dist.integrity dist.tarball --json
npx clawpatch@0.1.0 --root /path/to/isolated/roborally --state-dir /tmp/clawpatch-roborally init
npx clawpatch@0.1.0 --root /path/to/isolated/roborally --state-dir /tmp/clawpatch-roborally map
npx clawpatch@0.1.0 --root /path/to/isolated/roborally --state-dir /tmp/clawpatch-roborally review --limit 3
npx clawpatch@0.1.0 --root /path/to/isolated/roborally --state-dir /tmp/clawpatch-roborally report
```

Natural-use runs should capture:

- the exact Clawpatch version/source and install path
- feature count and sample feature quality
- finding count by severity/confidence
- accepted findings, rejected findings, and reasons
- repo-native verification commands used for any accepted finding
- whether the result justifies another run on Echo Forge or Storybook

## Evidence

- The X/Twitter connector failed on the source tweet with a URL metadata parser
  error, so retrieval used Twitter oEmbed and direct link resolution.
- Twitter oEmbed showed Peter Steinberger's May 16, 2026 post recommending the
  linked tool for finding latent repo bugs.
- The linked `t.co` URL resolved to `https://clawpatch.ai/`.
- The Clawpatch website and GitHub README describe semantic feature mapping,
  Codex-backed review, persisted findings, report generation, explicit
  one-finding fixes, and manual control over resulting worktree changes.
- GitHub shows `openclaw/clawpatch` as a public MIT TypeScript repo with a
  v0.1.0 release published May 15, 2026.
- The v0.1.0 release notes say the published package includes the initial CLI,
  Codex provider integration, strict provider schemas, tests, docs, Swift/Rust
  support, and npm packaging proof.
- A May 16, 2026 main-branch commit added Python feature mapping after the
  v0.1.0 release, so Python fit should not be assumed for the current npm
  package.
- Local fit sampling found package surfaces in Storybook, CineForge, RoboRally,
  and Echo Forge; Python surfaces in Dossier and Doc Web; and no supported
  top-level package surface for Board Game Ingester.

## Confidence

Medium-high. The public docs and repo are clear enough to classify the tool and
choose an optional report-only detector role. Confidence in finding quality
will come from normal repo use rather than a separate pre-rollout pilot.

## Open Questions

- Does Clawpatch produce enough verified, non-obvious findings to justify the
  extra review surface?
- Can `--state-dir` reliably keep generated state outside target repos for
  no-pollution scouting?
- Is the current npm package enough, or should a later pilot wait for the next
  release that includes Python mapping?
- Should repeated useful runs justify a small reviewed local helper around
  `/codebase-improvement-scout`?
