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

The right move is a bounded spike, not adoption. Run one report-only pilot in
an isolated target-project worktree, preferably against RoboRally first because
it is a compact JavaScript repo with deterministic scenario behavior and tests.
Do not run `clawpatch fix` during the pilot. The useful question is whether
Clawpatch finds concrete, verified bugs that Cam's existing `/validate`,
`/loop-verify`, and optional `codex review` closeout signals would not have
surfaced cheaply.

## Recommendation

- Create or triage a small Conductor-owned spike for one report-only Clawpatch
  pilot.
- Use an isolated RoboRally worktree as the first target.
- Pin the tool version, record the exact package/source used, and keep generated
  state outside the repo when possible with `--state-dir`.
- Run only the read/report path: `init`, `map`, a small `review --limit`, and
  `report`.
- Manually verify any findings against source and repo-native tests before
  treating them as real work.
- Decide after the pilot whether Clawpatch deserves:
  - no further action
  - a runbook-only "optional scanner" note
  - a second pilot on a larger TypeScript repo such as Echo Forge or Storybook

Do not add Clawpatch to normal validation, CI, or target-project stories yet.
Do not route repo-local inbox items from unverified findings.

## Project Relevance

- **conductor**: `Spike`. Conductor should own the pilot decision and the
  adoption rule. This is a cross-project evaluation problem, not a product
  feature.
- **dossier**: `Defer`. Dossier is Python. Latest Clawpatch main has Python
  mapping work after the v0.1.0 package release, but the published package is
  not yet the right first test target.
- **storybook**: `Defer`. Storybook is a strong eventual stress test because it
  is a large TypeScript monorepo, but it is too expensive and broad for the
  first proof.
- **doc-web**: `Defer`. Same Python caveat as Dossier. Revisit after Python
  mapping is in a published release and after a smaller JavaScript pilot proves
  signal quality.
- **cine-forge**: `Defer`. Mixed Python/JavaScript surface with real product
  pressure. Useful later only if the pilot shows high-confidence findings
  without creating noisy backlog.
- **boardgame-ingester**: `Reject for now`. No supported top-level package
  surface was identified in the quick fit pass.
- **roborally**: `Spike`. Best first pilot: small JavaScript repo, deterministic
  scenarios, meaningful tests, and lower operational cost.
- **echo-forge**: `Defer`. Plausible later target because it is an active
  TypeScript/Vite app with tooling scripts, but it should not absorb scanner
  noise before the tool proves itself elsewhere.

## Spike Shape

Suggested first-run envelope:

```bash
npm view clawpatch@0.1.0 version dist.integrity dist.tarball --json
npx clawpatch@0.1.0 --root /path/to/isolated/roborally --state-dir /tmp/clawpatch-roborally init
npx clawpatch@0.1.0 --root /path/to/isolated/roborally --state-dir /tmp/clawpatch-roborally map
npx clawpatch@0.1.0 --root /path/to/isolated/roborally --state-dir /tmp/clawpatch-roborally review --limit 3
npx clawpatch@0.1.0 --root /path/to/isolated/roborally --state-dir /tmp/clawpatch-roborally report
```

The pilot should capture:

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
choose a conservative pilot. Confidence is not high until one real report-only
run proves finding quality and noise level on Cam's repos.

## Open Questions

- Does Clawpatch produce enough verified, non-obvious findings to justify the
  extra review surface?
- Can `--state-dir` reliably keep generated state outside target repos for
  no-pollution scouting?
- Is the current npm package enough, or should a later pilot wait for the next
  release that includes Python mapping?
- Should any future adoption be a manual runbook step only, or an optional
  `/validate` escalation for stale/risky code areas?
