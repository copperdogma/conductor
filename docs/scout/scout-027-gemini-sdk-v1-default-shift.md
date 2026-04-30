# Scout 027 — Evaluate Gemini SDK v1 Default Shift Across Tracked Repos

**Source**: Google Gemini API SDK email to Cam, received 2026-04-30; Google
AI for Developers API-version and libraries docs, last updated 2026-04-28.
**Status**: Adapt
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Google says the next major official Gemini API SDK release, expected in
February 2027, will default to the stable `v1` endpoint instead of `v1beta`.
Existing deployed code keeps working; the risk appears only when upgrading an
official SDK without explicitly choosing an API version. Google's current docs
also say `v1` is the stable channel, `v1beta` is for early features, and SDK
clients can set the version explicitly (`api_version` in Python,
`apiVersion` in JavaScript).

The tracked repos are not uniformly exposed. Most Gemini usage is hard-coded
REST against `generativelanguage.googleapis.com/v1beta` or an OpenAI-compatible
`v1beta/openai` gateway, which is not affected by an SDK default flip but is
still deliberately beta-channel traffic. One repo, `doc-web`, does use the
official Python `google-genai` package shape directly and currently constructs
clients without an explicit API version.

The practical result is no emergency migration today. The right follow-up is a
small, explicit-version hardening pass in `doc-web`, plus a lower-priority
inventory story for repos that intentionally hard-code `v1beta` so preview
model and beta-endpoint reliance is documented rather than accidental.

## Project Relevance

- **doc-web**: `Adapt`. Direct official SDK use was found in
  `modules/common/google_client.py` via `from google import genai` and
  `genai.Client(api_key=...)`; benchmark scripts also use
  `from google.genai import Client` directly. Recipes and eval surfaces use
  both stable-looking `gemini-2.5-pro` and preview models such as
  `gemini-3.1-pro-preview` / `gemini-3-flash-preview`. This is the only
  first-order match to the email.
- **storybook**: `Adapt later`. Storybook depends on Vercel's
  `@ai-sdk/google`, not Google's official `@google/genai`, and it also has
  several direct REST calls to `/v1beta/models/...:generateContent`. The
  installed provider currently defaults its own `baseURL` to Google's
  `v1beta` endpoint. Not directly covered by the official-SDK notice, but it
  is still beta-channel dependent.
- **cine-forge**: `Adapt later`. CineForge uses direct REST to Gemini/Imagen/Veo
  beta endpoints for LLM, image, video, health, and eval paths. It does not
  appear to depend on an official Gemini SDK in the checked manifests. Preview
  video and Gemini 3.x model usage makes this an intentional beta-channel lane,
  not a February-2027 SDK-default risk.
- **dossier**: `Adapt later`. Dossier uses the OpenAI Python SDK against
  Google's OpenAI-compatible `v1beta/openai/` endpoint and a benchmark-only
  direct REST client rooted at `/v1beta`. Earlier `google-genai` exploration
  is documented as removed. Not directly exposed to an official SDK default
  change, but the repo should keep beta endpoint reliance explicit.
- **boardgame-ingester**: `Not affected`. No runtime Gemini SDK/API use was
  found outside generated `.gemini` CLI wrapper/tooling references and docs
  comparing with `doc-web`.
- **roborally**: `Not affected`. No runtime Gemini SDK/API use was found
  outside generated `.gemini` CLI wrapper/tooling references.
- **echo-forge**: `Not affected`. No runtime Gemini SDK/API use was found.
  Matches were scout/decision docs and generated skill wrapper references, not
  maintained runtime code.
- **conductor**: `Defer`. Conductor owns the scout/alignment memory, not a
  Gemini runtime. Its role is to route follow-up work rather than implement a
  shared harness change.

## Recommended Actions

1. Create a `doc-web` story to make official `google-genai` client versioning
   explicit.
   - If the maintained `doc-web` Gemini lanes can run on stable capabilities,
     configure `genai.Client(..., http_options={"api_version": "v1"})` and run
     the maintained Gemini OCR/crop smoke or eval slice.
   - If the preview model lanes still need beta-only behavior, configure
     `api_version: "v1beta"` deliberately and document why those lanes are
     experimental.
   - Apply the same explicit option to direct benchmark helper scripts that
     instantiate `Client(...)`.
2. Create a lower-priority cross-repo alignment note or story for direct REST
   beta endpoints in Storybook, CineForge, and Dossier.
   - Do not rewrite these to `v1` blindly. First classify each call by feature:
     stable `generateContent`/embeddings/model-list, Imagen, Veo, OpenAI
     compatibility, and preview model IDs.
   - Where stable `v1` works, migrate or centralize the API root so the version
     is a named constant.
   - Where `v1beta` is required, keep it explicit and add a short code or
     runbook note that it is intentionally beta-channel.
3. No action for Board Game Ingester, Robo Rally, or Echo Forge unless future
   work adds real Gemini runtime dependencies.

## Evidence

- Google docs distinguish stable `v1` from breakable `v1beta` and show SDK
  API-version configuration for Python and JavaScript.
- Google docs list `google-genai` / `@google/genai` as the official production
  Gemini SDKs; `doc-web` imports the Python one directly.
- `doc-web/modules/common/google_client.py` creates `genai.Client(api_key=...)`
  without `http_options`.
- `doc-web/benchmarks/scripts/eval_image_gate.py` and
  `doc-web/benchmarks/scripts/eval_permissive_gate.py` instantiate
  `google.genai.Client(...)` directly.
- `doc-web/configs/recipes/recipe-images-ocr-html-handwritten-notes-gemini-rescue.yaml`
  and the PDF sibling use `gemini-2.5-pro`; the Onward MVP recipes use
  `gemini-3.1-pro-preview` and `gemini-3-flash-preview`.
- `storybook/packages/backend/package.json` depends on `@ai-sdk/google`; the
  Storybook source also hard-codes several direct `/v1beta` REST calls.
- `cine-forge/src/cine_forge/ai/{llm,image,video}.py` and health/eval helpers
  hard-code `generativelanguage.googleapis.com/v1beta` roots.
- `dossier/src/dossier/llm.py` and `dossier/src/dossier/google_direct.py`
  hard-code Google `v1beta` OpenAI-compatible or direct REST roots.
- Dependency-manifest searches across the seven target repos found no
  `@google/genai`, `@google/generative-ai`, `google-generativeai`, or
  `google-genai` declared dependency outside `doc-web`'s optional/imported
  module path and docs references.

## Confidence

High that `doc-web` is the only first-order official-SDK exposure in the
tracked set, based on source and manifest searches. Medium on whether
`doc-web` should prefer `v1` or `v1beta` immediately: its current feature use is
mostly standard vision generation, but some recipes and evals intentionally
reference preview model IDs. That should be decided with a small live
compatibility check in the repo rather than guessed from names alone.

## Open Questions

- Are the current `doc-web` preview model IDs available and behavior-compatible
  on the stable `v1` endpoint today?
- Do Storybook's `@ai-sdk/google` defaults change independently before or after
  Google's official SDK default change?
- Which CineForge Google media endpoints have stable `v1` equivalents, and
  which are expected to remain beta because of Imagen/Veo preview features?
