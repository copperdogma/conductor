# Scout 082 — Claude instruction fallback and decision-model awareness

Date: 2026-10-01 (America/Edmonton)
Verdict: Adapt; prepare one coordinated documentation alignment

## Verified upstream behavior

Anthropic's current [memory documentation](https://code.claude.com/docs/en/memory#agentsmd)
confirms that Claude Code supports `AGENTS.md` by default starting at v2.1.277.
Use v2.1.281 or later as the rollout baseline: earlier supporting versions had
exceptions including Bedrock and telemetry-disabled sessions. A first session
after upgrading an older installation can still omit the feature; check a fresh
subsequent session. This is Claude Code behavior, not a property of Claude model
weights or proof that every other Claude host loads repository instructions.

The default `claude-md-or-agents-md` mode uses AGENTS only when no project
`CLAUDE.md`, `.claude/CLAUDE.md`, or `CLAUDE.local.md` is found in the working
directory or its ancestors. User `~/.claude/CLAUDE.md`, managed instructions and
`.claude/rules` do not suppress fallback. Disabling the built-in `agents-md`
plugin or selecting `claude-md` prevents it. The setting is user/managed scoped;
project/local settings cannot set that plugin option.

Root AGENTS loads at startup; nested AGENTS loads on text Read. The official
docs also flag differences for InstructionsLoaded hooks, `--add-dir` and external
imports. The [built-in plugin source](https://github.com/anthropics/claude-code/blob/main/mods/agents-md/README.md)
documents further nested loading and compaction limitations. Do not remove a
compatibility file from a host that depends on those behaviors without checking it.

`claude --version` on this machine returned **2.1.202**. No update or inference
was performed. Relevant user settings contain no explicit instruction mode or
disabled agents-md entry; this does not prove all hosts/settings support fallback.
The ancestor directories Projects, Documents and the home directory had none of
the checked project Claude instruction files at inspection time.

## Decision models

The live TypeSafe [System One guide](https://docs.typesafe.ai/concepts/system-one)
defines typed judgments and probabilities over supplied state. Jev currently
accepts text only. [Primitives](https://docs.typesafe.ai/primitives) include Choice
(defined options), Noul (yes probability) and Score (ordered criteria).
[Confidence](https://docs.typesafe.ai/confidence) describes concentration of the
answer distribution; it does not establish correctness on an individual case.
Local calibration and complete-workflow testing remain necessary.

OpenAI's [September 29 DevDay recap](https://openai.com/index/devday-2026-recap/)
announces the **Decisions API**, powered by Luna, for predefined questions with
finite answers using text or images. It is in limited preview, with broad release
planned in the coming days. That is an announcement, not verified account access,
a validated SDK contract, a price comparison or a repo-local adoption result.
The docs MCP search and fetched model catalog did not establish a Decisions
contract; the attempted guide URL was unavailable. Do not invent endpoint or
response details. The web reader failed on TypeSafe Markdown URLs; normal HTML
pages and direct read-only Markdown retrieval succeeded.

## Recommendation

Teach the category in AGENTS because agents cannot reliably discover a new tool
from training knowledge. Require an explicit approach comparison when changing
semantic decision logic, without requiring a paid benchmark for every story.
Keep integration details in a repository-owned `docs/decision-models.md`, linked
from AGENTS, so the guidance travels to other machines and cloud environments.
The personal TypeSafe skill is a useful current reference but cannot be the sole
discovery path. Avoid copying provider SDK instructions into root files.

Storybook already has a substantial decision-model section, an opt-in Jev router,
privacy gates and usage accounting. Preserve those adaptations. Echo Forge's
complete-proposal trial retained a no-go for normal/default Jev use despite
better raw intent labels; preserve that verdict. Other owners should learn to
consider the category without treating awareness as adoption or enablement.

See [Alignment 051](../alignments/align-051-agent-instructions-and-decision-models.md)
for the inventory, proposed root text and coordinated rollout recommendation.


## Approved follow-through

After Cam approved Alignment 051, the local CLI was updated to 2.1.287 and its
built-in AGENTS plugin enabled. Fresh local sessions proved root loading across
eight isolated owner worktrees and scoped CineForge startup loading. Five
fresh-origin bridges were removed in the prepared patches, including Storybook's
bridge that was already staged for deletion in its primary checkout. The patches
include portable decision-model guides with owner-specific gates. Storybook
subsequently landed its bridge deletion and introduction independently; its patch
was refreshed against that new main, leaving four pending bridge deletions. They are
validated and remain uncommitted; see Alignment 051's execution record and
evidence for exact scope and host limitations.


Cam subsequently approved close-out. The seven owner patches are committed and
verified on remote main, with Conductor completion in the supervisor commit.
Alignment 051 records exact receipts and validation reuse; no provider integration
or model-default change was made.
