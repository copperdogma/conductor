# Scout 055 - Evaluate NVIDIA SkillEvaluator and ClawHub Skill Lift

**Source**: `https://x.com/pat_erichsen/status/2090142910499205145`,
`https://github.com/NVIDIA/SkillEvaluator`, and
`https://docs.nvidia.com/skills/skillevaluator/`

**Status**: Adopt
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Patrick Erichsen announced that the OpenClaw team is working with NVIDIA to
bring SkillEvaluator to ClawHub so skills can be discovered using quantitative
evidence rather than popularity or intuition alone. The post's concrete idea is
"skill lift": compare the same task with and without the skill and report how
much the skill changes agent performance.

The announcement is directionally useful but not yet an adoption surface. The
post does not provide an availability date, integration contract, ranking
policy, or evidence that ClawHub verification is live. A reply asking whether
skills can already be verified had no retrieved answer during this scout.

The underlying NVIDIA SkillEvaluator project is available now. It is an
Apache-2.0 Python CLI with three independent tiers:

1. deterministic validation for schema, quality, PII, licensing, Unicode,
   scripts, and security evidence;
2. LLM/embedding-backed context and semantic-overlap checks; and
3. sandboxed live agent evaluation through Harbor, including Codex support,
   with-skill and without-skill arms, repeated attempts, dimension scores,
   pass@k, and skill lift.

This is meaningfully different from the existing SkillOpt scout. SkillOpt is a
validation-gated optimization loop for proposing and selecting bounded skill
edits. SkillEvaluator is primarily an evaluation and reporting harness for
checking whether a skill is well formed, distinct, safe enough to inspect, and
actually improves agent behavior. They are complementary: SkillEvaluator could
provide evidence for a candidate; it should not become an automatic promotion
authority.

The strongest local opportunity is a bounded Conductor-owned trial for the
agent that scouts and compares skills across the portfolio. Cam clarified that
this is the intended domain: when he supplies a new skill, or if Conductor later
runs a recurring skill-discovery search, Conductor may use SkillEvaluator to
qualify the candidate before making project-specific recommendations. The tool
is not proposed as infrastructure for the product repositories themselves.

The tracked repos still provide the relevance context and stronger
task-specific truth surfaces for product behavior. SkillEvaluator may reduce
the one-off work needed to test skill routing, negative activation, baseline
lift, repeated-run reliability, and portable report output, but it should
inform Conductor's recommendation rather than decide downstream adoption.

## Project Relevance

- **conductor**: `Only spike owner`. Conductor owns the distributed skill
  comparison problem and already has report-only skill-surface auditing,
  reviewed learning, and validation-gated skill-improvement guidance. Test
  whether SkillEvaluator adds useful behavioral evidence without turning it
  into a canonical harness or portfolio-wide dependency.
- **dossier**: `Reference context only`. Dossier has mature scored
  extraction evals and already completed a SkillOpt-style no-promotion trial.
  Those surfaces can help Conductor judge candidate relevance, but this story
  creates no Dossier adoption pressure.
- **doc-web**: `Reference context only`. Its narrow exact-check surfaces make
  it useful for judging whether a discovered skill has plausible value, but
  this story creates no doc-web installation or evaluation work. The current
  model decision continues to use the frozen hand-authored goldens.
- **boardgame-ingester**: `Reference context only`. Rulebook/component
  procedures help define what a relevant candidate might look like, without
  creating an owning-repo follow-up.
- **storybook**: `Reference context only`. Privacy, provenance, and human
  judgment constrain what Conductor may infer from a generic skill-lift score.
- **cine-forge**: `Reference context only`. Creative quality, visual taste,
  and production usefulness remain repo-local decision surfaces.
- **echo-forge**: `Reference context only`. Audio quality and live-table
  usefulness remain repo-local decision surfaces.
- **roborally**: `Not relevant to the current spike`. There is no active skill
  pressure in the game-framework proof lane.

The former product-by-product `Defer` framing is intentionally removed. The
projects are comparison context for Conductor, not queued owners of future
SkillEvaluator work.

## Recommendation

`Adopt` SkillEvaluator as an optional, non-authoritative Conductor skill-intake
diagnostic. Use it selectively when deterministic provenance/safety checks or a
hand-authored with-skill/without-skill comparison can materially improve a
cross-project recommendation.

Do not install SkillEvaluator across tracked repos, add it to every CI pipeline,
or depend on the announced ClawHub integration yet. Do not let generated eval
cases, default LLM judges, or a single low-attempt lift score supersede
hand-authored goldens and repo-native acceptance tests.

Story 030 records the bounded evaluation and its two stop gates:

1. **Keyless report-only qualification**: pin a reviewed SkillEvaluator
   revision and run only deterministic checks against two representative local
   skills. Compare findings with the existing skill-surface audit, record false
   positives and local-path/PII handling, and stop if the report adds no useful
   signal.
2. **One behavioral lift canary**: the useful keyless findings earned this
   gate. The spike hand-authored explicit, implicit, contextual, and negative
   cases for `scout`, ran two attempts per case in both arms, and retained all
   16 trajectories. Both arms passed 4/4 cases at pass@2. Overall lift was a
   neutral `+0.0248`; behavior adherence improved `+0.1027` and
   execution/discoverability improved `+0.0859`, while correctness fell
   `-0.05` and efficiency was flat.

This belongs in Conductor rather than a target repo inbox: the question is
whether the supervisor agent can qualify skills more rigorously before making
recommendations. No product repo should carry speculative integration pressure.
A possible weekly discovery schedule remains separate future work and should
only be considered after repeated manual skill intake proves that the lane
removes more work than it adds.

Do not normalize the tool into every intake or interpret its aggregate quality
grade as a recommendation. The default evaluator produced material false
positives and judge disagreement: it repeatedly treated the required read of
the candidate skill as an incorrect skill read, and different attempts judged
the same reject/adapt reasoning inconsistently. Hand-authored cases, a baseline
arm, raw trajectory review, and exact/custom checks where practical are part of
the adoption contract.

Keep installation isolated and pinned for now. The tested runtime required a
temporary compatibility patch because Harbor 0.13.2 uses Docker Compose
`up --wait` while SkillEvaluator deliberately emits `HEALTHCHECK NONE`, a
combination rejected by Docker Compose 28.5.1. A permanent Conductor wrapper is
not justified until upstream fixes that boundary or repeated manual intake
proves enough value to own it locally.

## Rejected Adaptations

- Do not use ClawHub ranking or verification claims until the integration is
  live and its evidence contract can be inspected.
- Do not treat Tier 1 quality scores as proof that a skill helps an agent.
- Do not treat Tier 2 semantic similarity as proof that two distributed local
  skills should be merged; justified divergence remains expected.
- Do not accept automatically generated eval cases without human review and
  negative activation coverage.
- Do not use `--skip-baseline` when the decision depends on skill lift.
- Do not make experimental Tier 3 results blocking until repeated local trials
  agree with an owning repo's accepted verifier.
- Do not expose provider or agent credentials through committed eval config.

## Evidence

- The X post says the goal is quantitative proof for ClawHub skill discovery
  and names skill lift as the example metric. The retrieved post and replies do
  not establish that the ClawHub integration is currently available.
- [NVIDIA's repository](https://github.com/NVIDIA/SkillEvaluator) describes
  independent deterministic, semantic-deduplication, and live-agent tiers;
  Codex, Claude Code, and OpenCode are supported live-agent targets. The
  project is marked experimental and community-supported with no SLA.
- [NVIDIA's report contract](https://docs.nvidia.com/skills/skillevaluator/reports)
  defines lift as the with-skill score minus the without-skill baseline. It
  treats lift below `+0.05` as neutral rather than a pass, reports pass@k
  separately, and preserves execution status so failed runs do not masquerade
  as scores.
- [NVIDIA's dataset contract](https://docs.nvidia.com/skills/skillevaluator/eval-datasets)
  supports explicit, implicit, contextual, and negative cases, plus observable
  assertions, expected skill routing, scripts, fixtures, custom environments,
  and custom graders. Generated datasets can fall back to templates, which is
  convenient for bootstrapping but not sufficient for a local adoption gate.
- [NVIDIA's CI guidance](https://docs.nvidia.com/skills/skillevaluator/ci-integration)
  recommends progressive adoption: start report-only, then gate deterministic
  checks, add model-backed checks later, and keep live Tier 3 advisory until a
  team deliberately makes it blocking. It also keeps operator credentials out
  of committed eval configuration.
- The current Conductor skill-surface audit is intentionally structural and
  report-only. SkillEvaluator's possible added value is behavioral baseline
  evidence, not automatic cleanup or cross-project canonicalization.
- At pinned upstream commit
  `aa195cacf1f115c86fd11d3c2821ea267c843ef2`, deterministic qualification of
  temporary copies of `scout` and `skill-surface-audit` passed PII, license
  validation, Unicode, quality threshold, and lint. The external profile failed
  only on missing publisher-oriented `metadata.author`. The reports added
  distinct provenance/safety/resource checks, but their quality grades were
  dominated by generic section and metadata advice.
- A four-case synthetic Tier 3 dataset passed strict validation. After working
  around Docker Desktop's stalled registry pull and the Harbor/Compose
  no-healthcheck compatibility bug, run
  `20260820_040023_98790_58edbfed38f2` completed all 16 planned trials with no
  runtime or security errors. With-skill overall was `0.8953`, baseline was
  `0.8705`, and lift was `+0.0248`, below the tool's `+0.05` positive-lift
  threshold. Both arms passed all four cases at pass@2.
- Dimension lift was mixed: behavior `+0.1027`, skill execution `+0.0859`, goal
  accuracy `+0.01`, security and efficiency flat, and correctness `-0.05`.
  Total preflight-plus-matrix cost was $0.3922806 for 769,798 input tokens,
  including 616,448 cached, and 51,341 output tokens.
- Manual trajectory inspection found the default efficiency rule mislabeled
  required reads of `candidate-skill/SKILL.md` as wrong-skill routing. LLM
  judges also disagreed about whether rejecting the unsafe skill as written
  while retaining its discovery idea satisfied an expected Adapt/Spike
  outcome. These are report-quality limitations, not reasons to discard the
  A/B harness.
- [OpenAI's official model page](https://developers.openai.com/api/docs/models/gpt-5.4-mini)
  supplied the live gate's `gpt-5.4-mini` pricing: $0.75 per million input
  tokens and $4.50 per million output tokens.
- Scout 052 already records the stronger local promotion boundary: bounded
  skill changes need scored tasks, held-out proof, rejected-edit evidence, and
  human inspection. SkillEvaluator does not weaken that boundary.

## Confidence

High that SkillEvaluator is a credible, materially distinct optional evaluation
tool and that its default scores must remain advisory. High that the completed
canary supplied useful evidence unavailable from the current structural audit:
the skill changed workflow adherence but not pass@2 on this suite. Medium that
its recurring benefit will exceed fixture, grader, and compatibility overhead;
future real candidate intakes must establish that.

## Open Questions

- Will upstream resolve the Harbor/Compose no-healthcheck incompatibility and
  provide a prebuilt or documented reusable evaluator image?
- How stable are lift scores across agent model versions and repeated attempts
  on the same local cases?
- Which candidate decisions justify a custom deterministic grader rather than
  default LLM grading plus manual trajectory inspection?
- What evidence, signatures, and ranking policy will ClawHub expose when the
  announced integration becomes available?
