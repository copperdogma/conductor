# Scout 068 — Qwen3.8 Max 0902 Doc Web Re-evaluation

**Date:** 2026-09-06
**Status:** Evaluated; do not adopt the frozen detector arm
**Scope:** Doc Web only; bounded qualification and crop evaluation, not adoption.

## Exact identity and changed access gate

Public OpenRouter metadata now lists `qwen/qwen3.8-max-0902`, canonical
`qwen/qwen3.8-max-20260902`, through an active Alibaba endpoint. This is distinct
from the August checkpoint evaluated in Doc Web Attempt 024. The September 2
access stop reported in the earlier session did not measure capability; its
uncommitted Scout 063 and Attempt 032 files are absent from the current primary
checkouts. This record preserves the new campaign separately.

Catalog pricing is US$2/M uncached input and US$6/M output tokens, with image,
text, and video input, 1,000,000 context and 131,072 maximum output tokens.
Structured outputs and low reasoning are advertised. Catalog identity and
endpoint status do not prove callability or strict-schema enforcement.

Sources checked 2026-09-06:

- [OpenRouter catalog](https://openrouter.ai/api/v1/models)
- [Exact endpoint](https://openrouter.ai/api/v1/models/qwen/qwen3.8-max-20260902/endpoints)
- [Provider privacy](https://openrouter.ai/docs/guides/privacy/provider-logging)
- [OpenRouter data collection](https://openrouter.ai/docs/guides/privacy/data-collection)

## Approved proposal

Cam selected evaluation 1: Doc Web's maintained `image-crop-extraction`
ladder, with a **US$0.75 total ceiling**, including probes, retries, controls,
and any conditional safety checks.

- Qualify exact Alibaba/OpenRouter identity, terminal responses, strict image
  schema and native/harness parity on synthetic/public fixtures.
- Freeze low reasoning and the maintained `conservative-count` prompt. Test
  Image011's prior seal/signature failure before the full 13-case detector.
- Require 13/13, overall >=0.95, and zero transport/schema errors to advance.
- Compare with maintained Gemini 3 Flash 13/13 and 0.9703. Run a fresh control
  only if the candidate qualifies and conservative remaining budget covers it.
- Conditional page-context safety starts with `page-122-001`; stop on a false
  pass. The remaining maintained 22-case suite is conditional on success and
  remaining budget. The proposal initially cited the older primary checkout's
  held-out restriction; the refreshed upstream runbook instead treats current
  hand-authored goldens as authoritative bounded selection evidence and prior
  exposure as a generalization limit. This current owner rule applies. Runtime
  adoption still requires all production-output safety gates and separate approval.
- Public owner-identified fixtures and synthetic probes only. Alibaba endpoint
  retention/training guarantees remain unverified; Cam approved this uncertainty
  for those inputs. No private fixtures or provider-account changes.
- No default changes, commits, pushes, merges, or deployment.

## Owner execution provenance

Worktree: `/Users/cam/.codex/worktrees/qwen38-max-0902-20260906/doc-web`

Branch: `codex/qwen38-max-0902-eval-20260906`

Current remote base: `b67f001481307ed1d4f2a4194436620dda16528b`

The dedicated owner agent ran Doc Web's maintained harness and owns its
artifacts. Conductor reviewed the returned evidence. Only the OpenRouter eval
credential was temporarily injected as `DOC_WEB_OPENROUTER_API_KEY` in the
isolated ignored `.env`; it was removed after the owner stopped.

## 2026-09-06 follow-through

The exact 0902 model and Alibaba provider were returned by all three terminal
strict-schema calls. Native and owner-adapter synthetic vision probes correctly
localized the square. The maintained Image011 differentiator then failed:
three predicted regions versus two source-backed expected regions, score
**0.6001**, zero transport/schema errors. Qwen again separated the seal and
adjacent signatures despite the explicit prompt rule requiring one combined
image. Both the owner and coordinator visually inspected the source page and
reviewed the exact raw response and scorer details.

| Stage | Spend | Native request latency |
| --- | ---: | ---: |
| Native synthetic vision | US$0.001732 | 6,229 ms |
| Owner-adapter synthetic parity | US$0.001720 | 6,163 ms |
| Image011 maintained differentiator | US$0.010512 | 19,958 ms |
| Total | **US$0.013964 / US$0.75** | |

Image011 harness latency was 20,097 ms; native request time is listed separately
above. This single failed case is not a 13-case aggregate or a contemporary
full comparison with Gemini. The full detector, fresh incumbent, page-context
differentiator, and full safety gate were not run under the approved early stop.

- Access: qualified for the exact model/account/route in this attempt.
- Transport: native strict vision and owner harness qualified.
- Reliability: three completed responses, zero observed errors; broader
  reliability remains unmeasured.
- Capability: failed a source-verified required grouping behavior on Image011.
- Economics: the three calls above are measured; broad latency/value unmeasured.
- Adoption: do not adopt this frozen low-reasoning detector arm. Page-context
  capability is not measured, not failed.

The temporary `DOC_WEB_OPENROUTER_API_KEY` was removed via the custody helper
after the owner confirmed all paid calls were finished. The evaluation itself
changed no defaults and performed no commits, pushes, or deployment. Cam later
separately authorized the scoped check-in and push recorded below.

## Retry condition

Do not repeat the unchanged low-reasoning arm. Reopen for a materially revised
checkpoint or a source-backed owner-contract change that addresses this grouping
failure; an explicitly approved different configuration is a new bounded arm,
not evidence that this failed result disappeared.

## Owner evidence and validation

- [Doc Web Attempt 035](/Users/cam/.codex/worktrees/qwen38-max-0902-20260906/doc-web/docs/evals/attempts/035-qwen38-max-0902-evaluate-model.md)
- [Owner evidence manifest](/Users/cam/.codex/worktrees/qwen38-max-0902-20260906/doc-web/docs/evals/evidence/035-qwen38-max-0902-manifest.json)

The manifest preserves exact owner-wrapper commands, code/fixture identities,
all three raw responses, verified request bodies, the ledger, and reproduction
limits. The coordinator independently verified SHA-256 and sizes for all 24
manifest entries and matched all three reconstructed request hashes to the
pre-send hashes. The owner reports 18/18 focused offline adapter/spend-guard
tests passed. Nonfinite-cost rejection in the campaign guard and code formatting
were applied after the run; original executed sources are retained and hashed separately.
Owner Ruff, methodology compile/check, and diff checks passed; the final focused
test run passed 18/18. The screen is recorded only in attempt history so it does
not replace the graph's comparable full-suite score. Conductor lint and diff
checks passed. No runtime code changed, so a pipeline
run or broad unrelated test suite was not used as evidence for this screen.

## Authorized check-in follow-through

Cam separately approved checking in and pushing the scoped evaluation records
and supporting changes. The check-in reran Doc Web's complete test suite because
Python helpers changed: **959 passed**, with four existing Pydantic deprecation
warnings, in 1015.12 seconds. Lint, helper lint, methodology and diff checks
also passed. This validation made no model calls and did not change the recorded
spend or verdict. Conductor's methodology compile/check and lint passed.
