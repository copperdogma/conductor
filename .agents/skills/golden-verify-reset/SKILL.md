---
name: golden-verify-reset
description: Reset verification status for selected golden fixtures while preserving their audit history.
user-invocable: true
---

# /golden-verify-reset [--all | fixture id]

Reset only the target project's verification tracker so selected fixtures can
be reviewed again. This is useful after a relevant schema, source, or
verification-contract change. It does not edit expected outputs or source
inputs. Conductor's supervisor evidence does not use product golden fixtures.

Read the shared [evidence contract](../setup-methodology/assets/evidence/README.md)
and follow the target project's local tracker format.

Inspect the tracker format first. By default reset only fixtures previously
marked verified; `--all` may include pending or previously failed fixtures.
If no fixture id is supplied, show the affected count and statuses before
changing a large tracker. Preserve the previous status, reset date, and reason
in the existing audit field. If the tracker cannot preserve that history,
stop and report the needed migration rather than erasing it. Report what was
reset and leave verification itself to `/golden-verify`.
