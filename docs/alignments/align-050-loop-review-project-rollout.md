# Alignment 050 — Loop Review Project Rollout

**Date:** 2026-09-30
**Classification:** Portable improvement
**State:** Ten target repos landed and verified on remote main; this supervisor commit records the rollout and installs the Conductor copy. Personal folder deleted.

## Intent and authorization

Cam approved installing the personal `loop-review` skill in repositories that
use `loop-verify`, then removing the personal copy to avoid duplicate discovery.
This authorizes the file rollout and source removal. Project rules still require
explicit authorization for commits and pushes. Cam subsequently replied `yes`
to commit, push, and land these 11 scoped patches.

`loop-verify` checks bounded work for defects. `loop-review` checks whether
long-running work is advancing the user's intended outcome. The skills serve
different decisions and can coexist without making every verification loop
require a strategic review. The review remains read-only until follow-through
is authorized; it preserves project constraints and prepares a concrete handoff.

## Scope and source

Compared the seven tracked projects, Conductor, and local project folders at
one or two levels under `/Users/cam/Documents/Projects` for an existing
`.agents/skills/loop-verify/SKILL.md`. Deduplicated existing worktrees by Git
common directory. The three additional repositories with that skill are
Canmore Town Council, Ravenloft/Cthulhu, and RPG Map Projector. No new tracked
project registrations or unrelated methodology propagation are included.

The complete source folder was `/Users/cam/.codex/skills/loop-review`. Both
original files were captured with these hashes:

- `SKILL.md`: SHA-256 `87493f9e8696cde65fb13dc15d77d221099a8c98a97dfe96f7ae57c246d044c6`
- `agents/openai.yaml`: SHA-256 `149d0338f88b35e66440377bc3349b59572691e3f24880f4718d8dd539bd101a`

The OpenAI UI metadata is preserved byte-for-byte. All project copies add
`user-invocable: true`, required by several native skill checks. Ravenloft also
adds its explicitly mandated alignment blockquote. Removing those documented
additions leaves the instruction text identical to the personal source.
Each AGENTS file adds a concise route that preserves existing authorization.
Compatibility links and discovery checks follow each owning repository's tooling.

## Isolation and bases

All worktrees use branch `codex/loop-review-rollout-20260930`, created after
fetching `origin/main`. Active primary checkouts are preserved.

| Repository | Base | Worktree |
| --- | --- | --- |
| storybook | `e9e588823f870897b476151fc8ab12cc5a178f8e` | `/Users/cam/.codex/worktrees/loop-review-rollout-20260930/storybook` |
| boardgame-ingester | `2d3b0bb1de7c429200e81ca9440de3c92220edbb` | `/Users/cam/.codex/worktrees/loop-review-rollout-20260930/boardgame-ingester` |
| canmore-town-council | `a17e92a9ab65fb6011cf92a8294da3c8868ca49b` | `/Users/cam/.codex/worktrees/loop-review-rollout-20260930/canmore-town-council` |
| cine-forge | `8be0fe2966d24613404763addd1948716227d272` | `/Users/cam/.codex/worktrees/loop-review-rollout-20260930/cine-forge` |
| conductor | `5dc5d930f46c2cd275f9d5a958e89677b5f7a8f3` | `/Users/cam/.codex/worktrees/loop-review-rollout-20260930/conductor` |
| doc-web | `f6352ed8b62b49b53800ad5b0345dc085dd6a479` | `/Users/cam/.codex/worktrees/loop-review-rollout-20260930/doc-web` |
| dossier | `811da7dadc4225d101b785aecf7d6c376beb139e` | `/Users/cam/.codex/worktrees/loop-review-rollout-20260930/dossier` |
| echo-forge | `69dc6a8c8c551e5d1dcbc4ccf3413cb99f792de7` | `/Users/cam/.codex/worktrees/loop-review-rollout-20260930/echo-forge` |
| ravenloft-cthulhu | `4421cdfdcc492907cc119ccd924cd8b937754528` | `/Users/cam/.codex/worktrees/loop-review-rollout-20260930/ravenloft-cthulhu` |
| roborally | `deef51febe2e92d5c2d85b8a85752d377e611f65` | `/Users/cam/.codex/worktrees/loop-review-rollout-20260930/roborally` |
| rpg-map-projector | `7d628dac55d8ccb324c4ecb4a13ac005171a8fe2` | `/Users/cam/.codex/worktrees/loop-review-rollout-20260930/rpg-map-projector` |

## Validation and removal

Validation is limited to skill discovery, compatibility surfaces, metadata,
applicable repository documentation/methodology checks, source identities, and
diff hygiene. No product suites, paid model calls, deployments, or goal/thread
changes are necessary for this instruction-only rollout.

The [rollout manifest](evidence/loop-review-rollout-20260930.json) records
commands, results, bases, worktrees, source and installed file hashes, reviewed
file lists, and source-removal evidence. Coordinator verification parsed both
YAML surfaces, checked the complete file set and exact permitted adaptations,
reviewed every AGENTS routing diff, and checked whitespace in tracked and new
files. All passed. Every primary HEAD and Git status matched the pre-edit
baseline after the isolated file rollout, before landing. Other active tasks
may continue advancing those checkouts; this task does not synchronize them.

| Repository | Applicable validation |
| --- | --- |
| Conductor | `make skills-check methodology-check lint`; diff and metadata checks |
| Dossier | `make skills-check`; methodology check with existing primary venv; diff and metadata checks |
| Storybook | skill sync check; `pnpm run methodology:check`; diff and metadata checks |
| Doc Web | `make skills-check methodology-check`; diff and metadata checks |
| CineForge | `make skills-check`; native methodology build/check; diff and metadata checks |
| Board Game Ingester | `make skills-check methodology-check`; diff and metadata checks |
| Robo Rally | `npm run skills:check`; `npm run methodology:check`; diff and metadata checks |
| Echo Forge | `pnpm run skills:check`; native methodology check; diff and metadata checks |
| Canmore Town Council | native skill and methodology checks; diff and metadata checks |
| Ravenloft/Cthulhu | manual metadata/alignment checks (no native checker); diff checks |
| RPG Map Projector | native skill, methodology, and triage-facts checks; diff and metadata checks |

CineForge required regeneration of three methodology outputs to resolve
pre-existing date/freshness drift; coordinator review confirmed date/counter-only
diffs. Existing Dossier migration warnings, CineForge audit/freshness warnings,
and Echo Forge's no-Ideal-requirements warning remain outside the rollout scope.

The personal source was rehashed immediately before deletion. Its exact two
files were removed only after all 11 targets passed source-preservation and
metadata checks. `/Users/cam/.codex/skills/loop-review` is now absent; there was
no second installation at `/Users/cam/.agents/skills/loop-review`.

## Landing evidence

Cam approved commit, push, and landing. Required changelog entries were added
in Storybook, Board Game Ingester, Dossier, Echo Forge, and Ravenloft. Robo Rally
has no tracked changelog; its policy records that fact. Canmore's required
`make skills-sync test` passed, and RPG Map Projector's skill sync and local
status checks passed with its isolated runtime stopped.

Doc Web advanced with an unrelated upstream crop-provenance commit; the patch
was rebased and skill/methodology checks passed. Board Game Ingester advanced
with higher-resolution manual graphics; the changelog conflict was resolved
by preserving the upstream entry and assigning the rollout the next sequence
(2026-09-30-29). Its skill/methodology checks passed after integration.

All ten target execution branches and remote main branches were pushed without
force, then verified to contain these commits:

| Repository | Landed commit |
| --- | --- |
| storybook | `90766ded41e796f452c98db83fcc0e2d780f8b36` |
| boardgame-ingester | `7a677416b1418a4fd1b651536354c40134d6067c` |
| canmore-town-council | `e6bf3784f47e35a329de86a007e64a02f3b21a73` |
| cine-forge | `3ba38d7a8a222ed51ca8097dfc1f2fdad2234520` |
| doc-web | `b47a6def39344bac988c58b36c72614f0dac1d9e` |
| dossier | `38629be704096b3cc47563b60980d71cd0193826` |
| echo-forge | `d9fdce175631e6344b7cc942e8d2729ef184a59a` |
| ravenloft-cthulhu | `f5138b0bf3c7b5f1bbd224fed9ee43343278d162` |
| roborally | `99322fa379b2e62507851f3affc07b165b865783` |
| rpg-map-projector | `fc90ecbef62f27799dc1c38021596201952869c5` |

Conductor installs its own copy and records this completion in the supervisor
commit. The invoking agent verifies that commit on remote main after pushing;
its own hash is not embedded recursively in this record.

Active primary checkouts are retained with their ongoing work. Clones, cloud
environments, and the Mac Mini receive the project skills when they update
from remote main. Personal-copy removal does not update those checkouts.
Task worktrees and execution branches are retained because cleanup was not
requested. No product suites, paid calls, deployment, or goal/thread changes
were made.
