# Scout 033 - Evaluate Codex Complexity Optimizer for Codebase-Improvement Scans

**Source**: `https://x.com/kappaemme1926/status/2055343704467206506?s=46&t=uFZE-MuhgWdh1YErEZzLtQ`,
`https://github.com/Kappaemme-git/codex-complexity-optimizer`, and
`https://www.npmjs.com/package/codex-complexity-optimizer`

**Status**: Adapt
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Kappaemme's `codex-complexity-optimizer` is a small Codex skill package for
report-first complexity and performance hotspot scouting. The tweet positions
it as a Codex skill that checks loops, repeated lookups, render-heavy code,
N+1-shaped patterns, before/after complexity estimates, risk level, tests
needed, and one-command install.

The package is real and inspectable. Version `0.1.0` was published to npm on
2026-05-15, has no package dependencies, and contains:

- a Codex `complexity-optimizer/SKILL.md`
- a heuristic Python scanner at `complexity-optimizer/scripts/analyze_complexity.py`
- a short optimization playbook
- a report template
- an installer that copies the skill into
  `${CODEX_HOME:-~/.codex}/skills/complexity-optimizer`

The useful idea is not a new always-on optimizer. The useful idea is an
algorithmic-complexity lead generator inside the existing report-first
`/codebase-improvement-scout` workflow. The local tracked repos already have
stronger adoption discipline than this package assumes: Conductor has a
codebase-improvement lane, report artifacts, triage classification, optional
safe auto-fix limits, story creation rules, and repo-native validation gates.

The right move is selective adaptation:

- Keep report-only as the default.
- Treat scanner output as leads, not proof.
- Rank algorithmic complexity only alongside churn, file size, user impact,
  maintenance drag, and drift pressure.
- Require local code inspection before any finding becomes a story or patch.
- Require tests, benchmarks, or manual measurements before claiming a
  performance improvement.
- Avoid global `npm install` / `npx` adoption until the package or helper is
  reviewed for the local environment.

## Fit Against Current Codebase-Improvement Lane

Already covered locally:

- report-first codebase scans
- current git state and dirty-worktree awareness
- repo-native checks and optional detectors
- top-findings triage instead of laundry lists
- classification as auto-fix, story, suppress, or ignore
- optional auto-fix only for narrow behavior-preserving changes
- story creation only for the highest-value non-mechanical improvement
- state files to avoid rediscovering the same suppressed findings
- explicit duplicate-ownership and architecture-drift checks

Useful gaps exposed by the source:

- no standard optional algorithmic-complexity scanner is named in the shared
  codebase-improvement lane
- repeated lookup, nested scan, sort-in-loop, render-derived-work, and
  N+1-shaped checks could become a useful deterministic detector category
- complexity reports could more consistently ask for before/after complexity,
  risk level, and tests or measurements needed
- UI-heavy repos could benefit from explicitly checking render-path derived
  collection work, while still requiring browser or profiler evidence before
  performance claims

## Project Relevance

- **conductor**: `Adapt`. Record the source and, if Cam wants to act, prepare a
  Conductor story to add an optional algorithmic-complexity detector/checklist
  to `/codebase-improvement-scout`. Do not install the npm package globally as
  the shared solution.
- **dossier**: `Defer`. Dossier already has the richest codebase-improvement
  history and should inherit any Conductor-approved detector wording rather
  than receive a one-off note.
- **storybook**: `Defer`. Storybook's TypeScript/backend/UI surfaces could use
  this class of detector, especially render-derived work and repeated scans,
  but only through the existing repo-hygiene scan lane.
- **doc-web**: `Defer`. Pipeline code may have real algorithmic hotspots, but
  doc-web's proof surface is generated artifacts and driver output; scanner
  findings should not outrank artifact truth.
- **cine-forge**: `Defer`. CineForge's current throughput pressure is more
  likely provider/runtime/artifact-flow bound than simple loop complexity, but
  the detector could help future codebase-improvement scans.
- **boardgame-ingester**: `Defer`. Rulebook parsing and component extraction
  could eventually benefit from repeated-scan detection, but there is no
  immediate adoption pressure.
- **roborally**: `Defer`. The headless engine may eventually need simulation
  performance checks, but current stories should stay behavior-first and
  scenario-backed.
- **echo-forge**: `Defer`. Echo Forge is the closest active UI-performance
  candidate because of scene controls, registry tooling, and audio-meter
  concerns, but browser/profiler evidence matters more than a generic scanner.
  Route through Echo Forge's existing codebase-improvement or architecture
  triage lanes if the performance pressure becomes the next story.

## Recommendation

Adapt the idea into Conductor's shared codebase-improvement guidance, not as a
standalone global Codex skill.

Recommended follow-up story scope:

- Add an optional "algorithmic complexity detector" subsection to
  `/codebase-improvement-scout`.
- Name the detector categories: nested scans, membership/search in loops,
  sort-in-loop, render-derived collection work, N+1-shaped IO/query loops, and
  repeated expensive derivations.
- Add the report fields from this source where useful: current pattern,
  estimated current complexity, recommended change, estimated complexity after,
  risk level, and tests or measurements needed.
- Keep scanner output explicitly non-authoritative.
- If a helper is wanted, vendor or recreate a small reviewed local script
  rather than requiring `npx codex-complexity-optimizer` in live workflows.
- Roll the wording to target repos only after Conductor has the shared rule
  right.

Do not create target-repo inbox notes yet. This is a cross-project methodology
improvement candidate, not a concrete product bug or feature for one repo.

## Rejected Adaptations

- Do not install this package globally in Cam's Codex environment as the
  default response to the tweet.
- Do not run `npx codex-complexity-optimizer` in a repo without first accepting
  that npm lifecycle scripts will execute remote package code.
- Do not treat heuristic scanner output as a bug list.
- Do not create a new parallel "complexity optimizer" lane next to
  `/codebase-improvement-scout`.
- Do not auto-refactor performance findings without measured input size,
  behavior tests, and an ownership boundary.
- Do not use this to justify speculative optimization where the current story
  pressure is product quality, provider quality, artifact correctness, or UI
  taste.

## Evidence

- The X post describes a Codex skill for complexity hotspot analysis and names
  report-only mode plus one-command npm install as core features.
- The Twitter connector failed on the original source with a
  `withheld_in_countries` parser error, so this scout used public tweet
  metadata mirrors and Twitter oEmbed as fallback source retrieval.
- npm package metadata shows `codex-complexity-optimizer@0.1.0`, MIT license,
  Node `>=16`, no dependencies, one version, and a 2026-05-15 publish time.
- The npm tarball contains nine files: README, license, installer, package
  metadata, the skill, the Python scanner, two reference docs, and a small
  OpenAI agent metadata file.
- The installer removes and replaces
  `${CODEX_HOME:-~/.codex}/skills/complexity-optimizer` with the bundled skill.
- The bundled scanner is heuristic and mixed-language. It checks Python AST
  patterns plus textual patterns for JavaScript, TypeScript, JSX/TSX, Java,
  Go, Ruby, PHP, C#, C/C++, and Swift.
- The bundled skill itself correctly says scanner output should be treated as
  leads, requires tests/measurements before edits, and defaults analysis
  requests to no file modifications.
- Conductor alignment memory already defines `/codebase-improvement-scout` as
  report-first, deterministic, ranked by churn/size/complexity/risk, and
  distinct from architecture triage.

## Confidence

Medium-high. The package is small enough to inspect directly, and the overlap
with existing local codebase-improvement methodology is clear. Confidence is
not higher because the package is brand new, has only one release, and has not
yet proven value against Cam's repos.

## Open Questions

- Should Conductor vendor a small local scanner, or is instruction-level
  detector guidance enough?
- If vendored, should the scanner live in the shared methodology package or
  only inside repos that already have `/codebase-improvement-scout`?
- Which repo should pilot it first? Echo Forge has visible UI-performance
  pressure, while Dossier has the most mature codebase-improvement history.
