# Scout 036 - Evaluate Open Collider for Ideation Quality

**Source**: `https://x.com/cdriclion/status/2056419767603298607?s=46&t=uFZE-MuhgWdh1YErEZzLtQ`,
`https://www.oparine.ai/`, `https://cdriclion.substack.com/p/why-direct-prompting-pushes-llms`,
`https://github.com/CL-ML/open-collider`, and
`https://github.com/CL-ML/open-collider-research`

**Status**: Adapt
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Open Collider is a semantic-collision workflow for LLM ideation. Instead of
asking the model for better ideas directly, it builds a brief, generates a bank
of structurally distant domains, collides the brief with each domain in separate
contexts, then curates the useful outputs from a larger noisy pool.

The useful local lesson is practical: when a task needs divergent solution
quality, adding more same-domain context can make the model more precise but
also more trapped in the already-obvious solution space. A bounded
distant-domain collision pass can expand the option set before the normal
Ideal/spec/ADR/story filters choose what is actually worth doing.

This should not become a default replacement for triage, validation, or ADR
judgment. Novelty is not correctness. The method belongs before decision
closure, as an option-discovery pass whose outputs are then judged against local
repo evidence, constraints, user intent, tests, and implementation risk.

## Project Relevance

- **conductor**: `Adapt`. Conductor should own the shared rule: collision-based
  ideation is optional guidance for high-ambiguity brainstorming, greenfield
  Ideal/spec drafting, story solution design, and ADR option expansion. It
  should route through a Conductor alignment or story before target-repo rollout.
- **dossier**: `Defer`. Useful for new harness, extraction, GEDCOM, or document
  workflow design choices, but not as a substitute for artifact/eval proof.
  Inherit later shared wording rather than creating Dossier-only pressure now.
- **storybook**: `Adapt`. Strong fit for `init-project`, `docs/ideal.md`, and
  product/story workflow design because those surfaces explicitly need broad
  idea intake before compromise.
- **doc-web**: `Defer`. Could help when designing architecture alternatives or
  review surfaces, but doc-web's proof remains generated artifact behavior and
  driver output.
- **cine-forge**: `Adapt`. Strong fit for creative workflow, previz, scene
  generation, and visual-fidelity ADRs where direct prompting can collapse to
  generic product ideas.
- **boardgame-ingester**: `Defer`. Could help with reusable framework and
  component-model design, but rulebook interpretation must stay source-grounded.
- **roborally**: `Adapt`. Useful for framework and AI-opponent design
  brainstorming while keeping game-rule behavior source-backed and
  scenario-verified.
- **echo-forge**: `Adapt`. Strong fit for soundscape, source-control,
  live-table UX, and ADR option exploration, especially where many plausible UI
  ideas would otherwise cluster around generic panel/control patterns.

## Recommendation

Adapt the method as a lightweight `/ideation` helper inside shared methodology
guidance, not as an always-on dependency or new mandatory lane.

Recommended first implementation scope:

- Add optional guidance to the appropriate Conductor-owned methodology surface
  for high-impact ideation moments: `init-project` / Ideal drafting,
  story-solution brainstorming, and ADR option generation.
- Keep the helper separate from caller skills so `create-adr`, `create-story`,
  `build-story`, and future `init-project` surfaces can call it without
  duplicating the protocol.
- Use a small manual protocol before automating:
  1. Generate a direct baseline option set.
  2. Generate 5-7 structurally distant domains, each with a mechanism and bridge
     question.
  3. For each domain, generate options that explicitly bridge the domain
     mechanism back to the local problem.
  4. Curate the top few ideas and record why the rest were rejected.
  5. Run normal repo filters: Ideal/spec fit, evidence, constraints, risk,
     tests, reversibility, and user taste.
- Keep `/triage` recommendation-first. Use collision passes only when triage
  has identified that option quality, not priority selection, is the blocker.
- For ADRs, use the collision pass to improve "considered options" and
  consequences. Do not let a novel option win without local proof.
- Pilot manually on the next real `docs/ideal.md` generation or substantive ADR
  before deciding whether the full Open Collider tool is worth installing.

Do not add target-repo inbox notes yet. This is a cross-project methodology
improvement candidate; Conductor should shape the shared rule first. Alignment
034 records the resulting `/ideation` helper contract.

## Evidence

- The source X post by Cédric Lion linked to Oparine/Open Collider and presented
  it as an open-source engine for improving LLM creativity.
- Oparine describes Open Collider as a four-phase session: brief, distant
  domains, collisions across pairs, and curation.
- The launch study claims 12 real-world projects, about 23,000 generated ideas,
  4,320 blind LLM-judge pairs, and higher originality for collision outputs.
- The research repo ships artifacts, cached embeddings, judge results, and a
  local integrity check rather than only a blog claim.
- The engine repo is MIT licensed, Python >=3.10, and can run in Claude Code
  skill mode or Anthropic API mode.
- The author's own limitations matter: the generation side used a single model,
  prompt format may be important, and quality/originality judgment relied on
  LLM judges rather than human raters.
- The study also reports that overall-quality wins are weaker than originality
  wins, which matches the local guardrail: use this for option discovery, then
  judge with repo-native evidence.

## Confidence

Medium-high for adapting the technique as instruction-level methodology.
Medium for adopting the full Open Collider tool. The mechanism fits Cam's
brainstorming, Ideal drafting, and ADR-option problems, but the full pipeline
adds time, provider coupling, and curation overhead that should only be accepted
after a manual pilot improves a real local decision.

## Open Questions

- Which real upcoming Ideal/spec or ADR pass should pilot the collision protocol?
- How large should the local domain bank be before the overhead stops paying for
  itself?
- Should the eventual shared wording live in `init-project`, `create-adr`,
  `build-story`, or a small common ideation note consumed by those skills?
- Would the full Open Collider repo add enough value over a local lightweight
  prompt pattern to justify installation and API-mode setup?
