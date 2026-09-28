# Alignment 049 — Dossier Sonnet 5.5 access follow-through

2026-09-28. User requested changing Story174's replacement target from Sonnet5
to newly released Sonnet5.5, conditional on API callability. Single owner,
single synthetic access/tool probe, USD0.01 cap, no retries or private payloads.

Owner: `/Users/cam/.codex/worktrees/dossier-retired-sonnet-live-tests`;
branch `fix/retired-sonnet-live-test-opt-in`, base `543fecd0`.
Evidence: `docs/evals/attempts/sonnet55-access-20260928.md` and
`docs/evals/artifacts/sonnet55-access-20260928/probe.json` under that worktree.
Raw artifact records the exact dirty adapter hash, synthetic payload/response,
usage, served identity, finish reason and time. Owner shell credential was used
without copying or changing it. No central credential was injected.

At 19:29:13 UTC, exactly claude-sonnet-5-5 returned a valid Ack tool call through
the updated owner adapter. One POST: 427 input/48 output tokens, USD0.001334,
1.622 seconds, standard/global service. Automatic tool choice replaces rejected
forced tool choice for this exact model; local Pydantic validation remains.
This is tiny-contract access evidence, not strict native-schema, full extraction,
quality, reliability, or comparative latency evidence. Test and benchmark slots
changed at user request; runtime defaults did not.

First-party release: https://www.anthropic.com/claude-sonnet-5-5
Migration: https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide
Same USD2/10 per million input/output token pricing as Sonnet5; advertised
30%+ speed and up-to-30% task-cost improvements are vendor claims, unmeasured here.


## Verified landing — 2026-09-28

User authorized close-out. Dossier commit
[f93fefb595f020f128a56f555df996e33a890f2c](https://github.com/copperdogma/dossier/commit/f93fefb595f020f128a56f555df996e33a890f2c)
landed on verified remote main, with Story174 closed and live API tests explicitly
opt-in. Evidence and adapter changes are now durable in that commit:
[access record](https://github.com/copperdogma/dossier/blob/f93fefb595f020f128a56f555df996e33a890f2c/docs/evals/attempts/sonnet55-access-20260928.md).
Reused 177 passing focused tests and 55-skipped gate proof; final review and
methodology/whitespace checks passed. Seven pre-existing offline resolution
fixture failures remain outside scope. No additional inference during landing.
Primary checkout remains untouched; task worktree retained.
