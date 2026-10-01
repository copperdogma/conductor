# Alignment 051 — Agent instructions and decision-model awareness

Date: 2026-10-01 (America/Edmonton)
Classification: Portable improvement with intentional owner adaptations
State: Seven owner patches landed and remotely verified; Conductor close-out in this commit

## Scope and evidence

Cam requested verification and a recommendation before deleting Claude files or
adding decision-model instructions. Inspected the seven `projects.yaml` owners
and Conductor's primary checkouts. The current Conductor checkout is dirty and
31 commits behind its cached origin/main; existing work is preserved. These are
local inspection findings, not claims about every deployed host or remote HEAD.
The latest numbered records on origin/main were Alignment 050 and Scout 081.
Upstream research is in [Scout 082](../scout/scout-082-agent-instructions-and-decision-model-awareness.md).

## Initial primary-checkout inventory (before approval)

| Repository | Root CLAUDE.md | Existing decision-model guidance | Recommendation |
| --- | --- | --- | --- |
| Dossier | `@AGENTS.md` plus generic bridge explanation | No dedicated introduction found in root | Remove bridge after host upgrade; add intro and local guide |
| Storybook | Absent; AGENTS explicitly prohibits it | Dedicated Language Models vs Decision Models section; opt-in Jev router and owner gates | Keep absent; refine existing section and link local guide |
| Doc Web | Prose directing Claude to read AGENTS | No dedicated introduction found in root | Remove after upgrade; add intro and local guide |
| CineForge | `@AGENTS.md` plus generic bridge explanation | No dedicated introduction found in root | Remove after upgrade; preserve nested guidance; add intro and guide |
| Board Game Ingester | Prose directing Claude to read AGENTS | No dedicated introduction found in root | Remove after upgrade; add intro and guide with modality limits |
| Robo Rally | Absent | No dedicated introduction found in root | Keep absent; compact awareness; deterministic simulation remains code |
| Echo Forge | Absent | No dedicated introduction found in root | Keep absent; intro and guide preserve default-off/no-go trial status |
| Conductor | Absent | Evaluation orchestration exists, but no category introduction | Keep absent; intro and guide route to owner evaluations |

The four Claude files contain bridges, not independent full instruction copies.
Removing them primarily simplifies discovery rather than eliminating a current
large duplication burden. Doc Web and Board Game Ingester's prose bridges rely
on Claude choosing to read AGENTS; an `@AGENTS.md` import is the stronger temporary
compatibility option if an old host must remain supported.

Tracked instruction paths include nested AGENTS under CineForge's
`src/cine_forge/modules` and `tests`. No tracked nested Claude instruction files
were found in the registered scope. All eight lack a repo-local
`.agents/skills/typesafe-ai/SKILL.md`. The local personal skill is available only
on this environment. AGENTS sizes range from approximately 2.6 KB to 78 KB, so
root additions should stay compact.

The delegated read-only inventory also checked Canmore Town Council,
Ravenloft/Cthulhu and RPG Map Projector from Alignment 050, plus
financial-monthly-analysis and Financial Hub. All five have root AGENTS and no
root CLAUDE; none has a local TypeSafe skill or dedicated root decision-model
introduction. At that primary-checkout snapshot, only the four registered bridges above
were present among these 13 roots. These extra projects can join a named expansion; finance
guidance must preserve source preparation versus downstream reporting ownership.

The wider scan found nested Claude files in Dossier runtime source copies,
Storybook's ignored Claude worktrees and Financial Hub's ignored Sure snapshots.
Sure's upstream files contain substantial instructions. Exclude generated,
archived and embedded upstream content from blanket deletion. Several native
skill-sync scripts create/check `.claude/skills` links to `.agents/skills`; those
are skill discovery links, not CLAUDE instruction generators, and should remain.

## Proposed AGENTS addition

Adapt the paragraph to the owner, preserving Storybook's existing integration
instructions. Proposed text for repos without an introduction:

> Decision models are an available architecture option, including TypeSafe's Jev
> and OpenAI's announced Decisions API. They answer bounded semantic questions
> over supplied context with predefined outcomes; Jev also supports yes/no
> probabilities and rubric scores. Consider them for routing, candidate selection,
> evidence checks and ranking when brittle heuristics or a full generative call
> are a poor fit. When changing semantic decision logic, compare deterministic
> code, a decision model and a language model, and explain the choice. Keep exact
> rules, arithmetic, identities, permissions and execution in code; use language
> models for generated text or open-ended outputs. Read `docs/decision-models.md`
> and current provider docs before designing an integration. Respect existing
> owner evaluation verdicts, privacy and enablement gates. Measure complete
> behavior, fallback, quality, latency and cost before adoption; typed answers or
> concentrated probabilities do not prove correctness. Jev is currently text-only;
> OpenAI announces text/image input, but access and contracts need verification.

The proposed local guide should explain Choice/Noul/Score with a small example,
candidate coverage and no-match handling, stale evidence, fallback and service
failure, confidence calibration, provider privacy, current dated source links,
owner implementation references and evaluation verdicts. Keep providers and
prices out of permanent policy except as dated evidence. A new reusable skill can
follow if actual integration work justifies it; a portable guide is sufficient now.

## Coordinated rollout recommendation

Do both changes in one documentation campaign, with removal gated by host proof:

1. Upgrade the local Claude Code and check other active CLI/IDE/cloud hosts; use
   v2.1.281 or later. Verify the built-in plugin and default instruction mode,
   ancestor/private Claude files, exclusions and fresh-session loaded-file notice.
   Check CineForge's nested AGENTS loading in particular. No upgrade was performed
   during this recommendation pass.
2. Use dedicated branches/worktrees for approved owner edits. Preserve unique
   Claude instructions if new ones have appeared, remove eligible bridges,
   correct live references and ensure setup/sync tooling does not recreate them.
   Keep compatibility imports only for explicitly unsupported hosts.
3. Add the compact awareness paragraph and repo-local guide. Refine Storybook's
   existing section rather than adding a second introduction. Preserve Echo
   Forge's no-go/default-off and finance or identity authority boundaries.
4. Validate instruction discovery, local links, relevant native documentation
   checks and setup/skill-sync behavior. No runtime model changes, paid evals or
   product suites are needed for a pure instruction change. Commits and pushes
   require a later explicit close-out request.

Recommend the registered eight-repository scope first. Additional repos from
prior campaigns are not automatically registered or authorized for this rollout;
their inventory can inform a named extension without making it implicit scope.

This reduces instruction-file clutter and makes new architecture options visible
to every agent without reversing owner evaluation results.

## Recommendation validation

`make methodology-check lint` passed. Existing planning sources are unchanged,
so graph regeneration was unnecessary. `git diff --check` passed; the two new
records also passed explicit local-link and trailing-whitespace checks. No
owner instructions, runtime configuration, host installations, credentials or
model defaults were changed. Existing dirty supervisor files were appended only
with this task's intake/index entries; no commits or pushes were performed.


## Approved execution — 2026-10-01

Cam approved the compatibility checks and combined documentation patches for the
seven registered owners plus Conductor. Work started from freshly fetched
`origin/main` in eight dedicated worktrees on `codex/agent-instructions-20261001`.
No commits, pushes, merges or product enablement were authorized or performed.

Fresh remote bases contained a fifth generic bridge in Storybook. Its primary
checkout already had a staged deletion and uncommitted decision-model guidance;
those changes were preserved rather than copied. The initial five isolated bridge
deletions were Dossier, Storybook, Doc Web, CineForge and Board Game Ingester.
During validation, Storybook independently landed its bridge removal and a
decision-model section on remote main (`f1a786d3`). Its isolated patch was
refreshed against that commit, refining the landed section and adding the guide.
Four bridge deletions therefore remain in the pending patches; Storybook is
already absent on main.
None contained unique policy. All eight patches add compact root awareness and
an owner-specific `docs/decision-models.md`. They preserve code-owned authority,
privacy and local evaluation gates; Echo Forge remains default-off with its
complete-proposal NO-GO. No provider integration or model default changes.

### Host proof

Updated the local native CLI from 2.1.202 to 2.1.287. The upgrade alone did not
load AGENTS; enabling `agents-md@builtin` through the supported plugin command
resolved that. Fresh `/context` sessions showed each of the eight root AGENTS
files. CineForge startup from `tests/` loaded both root and scoped tests guidance.
Direct launch of Claude Desktop's bundled 2.1.286 executable also loaded AGENTS.
These were local instruction-context commands with tools/MCP disabled and no
model request. Existing Desktop sessions and cloud hosts were not verified;
nested attachment on a later Read was not exercised. Preserve skill-discovery
links under `.claude/skills`.

### Prepared owner patches and validation

Worktree root: `/Users/cam/.codex/worktrees/agent-instructions-20261001/`.
Each owner directory below contains its reviewable patch. Exact base hashes,
changed-file hashes, checks and preserved-checkout results are in the
[evidence manifest](evidence/agent-instructions-20261001/rollout-manifest.json).

| Owner directory | Root bridge removed | Applicable validation |
| --- | --- | --- |
| `dossier` | Yes | Methodology and skill discovery checks; links and whitespace |
| `storybook` | Already landed independently | Methodology and skill discovery checks; links and whitespace |
| `doc-web` | Yes | Methodology and skill discovery checks; links and whitespace |
| `cine-forge` | Yes | Methodology and skill discovery checks; links and whitespace |
| `boardgame-ingester` | Yes | Methodology and skill discovery checks; links and whitespace |
| `roborally` | Already absent | Methodology and skill discovery checks; links and whitespace |
| `echo-forge` | Already absent | Methodology and skill discovery checks; links and whitespace |
| `conductor` | Already absent | Methodology, lint and skill checks; links and whitespace |

Independent review checked provider semantics, owner boundaries, local links,
bridge contents and change scope. Its setup-wording finding was corrected to
verify fresh context before enabling a disabled plugin. Existing CineForge
architecture/UI-scout aging warnings and Echo's missing parsed Ideal requirements
warning do not concern these documentation changes. Dossier passed using the
already installed Miniconda Python because system Python lacked PyYAML; legacy
migration metadata warnings remain. Product suites and paid
evaluations were unnecessary for this patch scope. Native checks were reused
after small prose corrections; final links and whitespace were checked again.

This rollout made no primary-checkout edits. Seven primary HEAD/status snapshots
were unchanged. Storybook advanced independently through Story 180 and its
instruction update; its primary checkout is now clean, and that landed work was
preserved in the refreshed patch. This preparation makes one instruction
source usable by Claude and gives agents portable awareness of decision models.

## Close-out and remote landing

Cam explicitly approved commit, push and landing. All eight repos passed
preflight before the first push; refreshed remote bases had no new integration
conflicts. Each owner patch was committed, pushed to its execution branch and
fast-forwarded to remote main, then verified by `git ls-remote`.

| Owner | Verified remote-main commit |
| --- | --- |
| `dossier` | `3db0b1f400bb60baccd73614d198a46352362053` |
| `storybook` | `5992e8724af55e4e813084fede1c6b781858064a` |
| `doc-web` | `b90c0da0f95eff852eeaea16419051a0b0a2e10d` |
| `cine-forge` | `b66b42ad989c1187ff539ec1b4ddc398d3900da2` |
| `boardgame-ingester` | `7a3c470fe4d2d008289ebf530c0439e57a6388dd` |
| `roborally` | `4123c2bbe22dc680748fc7823303a140d8ecf1ed` |
| `echo-forge` | `726864e531c2327d73462fcfd2be81c444fea504` |

Conductor's own guidance and this completion record are included in the
supervisor commit. [Landing receipts](evidence/agent-instructions-20261001/landing-receipts.json)
record the exact owner destinations, validation reuse and final primary snapshots.
The prepared-file manifest remains the historical validation input, rather than
being overwritten with close-out bookkeeping hashes. Required dated changelog
entries were added; RoboRally has no tracked changelog and none was created.

The close-out included no runtime changes, provider calls, paid evaluations or
deployments. Primary work was preserved; isolated task worktrees and branches
remain available because cleanup was not requested. No further rollout work is
required after the supervisor commit is verified on remote main.
