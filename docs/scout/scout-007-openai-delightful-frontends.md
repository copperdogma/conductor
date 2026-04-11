# Scout 007 — Evaluate OpenAI Frontend Guidance for UI Skill Upgrades

**Source**: `https://developers.openai.com/blog/designing-delightful-frontends-with-gpt-5-4`
**Status**: Adapt
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

The source is real, current, and materially useful. The OpenAI blog is not just
general taste advice; it ships an explicit front-end prompt pattern and an
embedded `frontend-skill` centered on composition-first layout, strong visual
hierarchy, mood-board/reference usage, meaningful motion, design-system
constraints, and lower default reasoning for UI work.

Compared with the tracked repos, the most important overlap is already present
in Storybook and CineForge: both repos already emphasize design tokens,
design-in-browser theme routes, and screenshot-verified iteration. That means
this source is not a missing front-end substrate and does not justify a broad
portfolio sync by itself.

The genuinely new value is narrower and worth adapting selectively for UI-heavy
repos: explicit composition-first rules ("poster, not document"), cardless
defaults, stronger hero/content narrative constraints, low/medium reasoning as
the front-end default, reference-image or mood-board guidance, and the
pre-build framing of `visual thesis`, `content plan`, and `interaction thesis`.
Those are meaningful improvements to front-end prompting discipline for
Storybook and CineForge, but they do not belong in Dossier or doc-web today.

## Project Relevance

- **dossier**: Keep local. Lower direct relevance. Dossier does not currently
  need a richer front-end methodology lane beyond occasional internal tooling.
- **storybook**: `Adapt`. Highest relevance. Storybook already has strong
  design-token and screenshot-loop guidance, but this source adds sharper
  art-direction and content-structure rules that fit its consumer-facing UI.
- **doc-web**: Keep local. Some ideas could transfer later, but doc-web does
  not currently have a dedicated UI methodology lane or enough active front-end
  pressure to justify adopting this now.
- **cine-forge**: `Adapt`. Strong relevance. CineForge already uses
  design-in-browser and token-driven UI work; the new composition/narrative
  guidance would improve prompting for visually led surfaces without changing
  the underlying stack.

## Recommendation

- Treat this as `Adapt`, not `Adopt`.
- Do **not** copy the OpenAI frontend skill wholesale into the tracked repos.
- The honest next artifact is a narrow Conductor alignment pass for the
  UI-heavy repos only: compare Storybook and CineForge UI-development guidance
  against the OpenAI front-end skill and port only the missing principles.
- Keep Dossier and doc-web local for now. No front-end sync is justified there.
- If execution is desired, the selective carry-through should focus on:
  1. defaulting to low/medium reasoning for front-end generation
  2. requiring visual references or mood boards when the task is visually led
  3. adding `visual thesis`, `content plan`, and `interaction thesis` before
     implementation on major UI builds
  4. making composition-first / cardless / strong-hero rules explicit for
     landing pages and promotional surfaces
  5. grounding UI generation in real copy or product context instead of
     placeholders
- No Conductor story was created from this scout alone. The alignment pass is
  the more honest first follow-up than a direct target-repo execution story.

## Confidence

- High on the source-shape and medium-high on the fit judgment. The OpenAI
  source is primary and explicit, and the repo comparison is grounded in
  Storybook/CineForge AGENTS guidance, but I did not run a before/after UI
  generation experiment inside the tracked repos.

## Evidence

- `https://developers.openai.com/blog/designing-delightful-frontends-with-gpt-5-4`
- Official source highlights:
  - practical quickstart: low reasoning, design constraints, visual references,
    and narrative/content strategy
  - embedded `frontend-skill`: composition-first, cardless defaults, visual
    thesis/content plan/interaction thesis, full-bleed hero rules, meaningful
    motion, and mobile-safe layout guidance
- Inbox note: `enhance our ui skill?`
- Inbox note: `Codex Cloud as a front-end design partner`
- Local workflow context:
  - `/Users/cam/Documents/Projects/Storybook/storybook/AGENTS.md`
  - `/Users/cam/Documents/Projects/cine-forge/AGENTS.md`
  - `/Users/cam/.codex/worktrees/7be2/conductor/docs/alignments/align-006-ui-scout-setup-surface.md`

## Open Questions

- Is the right landing a shared UI-guidance sync between Storybook and
  CineForge AGENTS, or a narrower repo-local update in each UI-heavy project?
- Which parts of the OpenAI skill are actually net-new after accounting for the
  repos' existing design-token, theme-route, and screenshot-verification
  workflow?
- If this becomes an alignment pass, should the scope include only guidance, or
  also a reusable template/checklist for mood boards and real-content framing?
