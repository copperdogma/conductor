# Conductor

Conductor is the supervisor project for Cam's active AI-first projects.

It exists to reduce cross-project busywork by turning vague notes into ready
work, comparing shared infrastructure surfaces across projects, and scouting
external ideas for project-specific adoption. It also maintains the canonical
reusable skills and methodology for new and existing projects. Model evaluation
serves those projects by testing whether alternatives are worth adopting.

To start a new project, point its agent at
[init-project](.agents/skills/init-project/SKILL.md) for Ideal/spec intake, then
[setup-methodology](.agents/skills/setup-methodology/SKILL.md) to select and
install the relevant package. Projects retain their own requirements, evidence,
and justified adaptations.

## Core loops

- `inbox.md` captures cross-project notes, links, and sync requests.
- `/triage` turns inbox items and backlog pressure into one recommended action.
- [`/quota-burn`](.agents/skills/quota-burn/SKILL.md) proposes ready projects from
  Cam's eligible pool, waits for approval, then runs their triage goals and
  coordinates validation, commit/push and summary at 20% remaining quota.
- `/align-projects` compares infrastructure drift across tracked projects.
- `/scout` investigates external sources and recommends which projects should
  adopt what.
- `/finish-and-push` completes and lands current work, including linked repo
  changes from the same request. Use `--audit-only` for a read-only readiness
  review and `--cleanup` to remove eligible task-owned local worktrees and branches.

## Reference library

Save useful tools and techniques in the [reference library](docs/reference.md).
Each entry gets a small source check, canonical links, use cases, and limitations
so future projects can find it without repeating discovery. Start with
[image-blaster](docs/reference/image-blaster.md) for image-to-3D environments.

## Key surfaces

For “host it like our other projects,” start with the
[shared service catalog](docs/services.md): DreamHost, Fly.io, Cloudflare and
Google Auth recipes, existing examples and selected private credential access.
Secret copies stay in the local ignored `.private/` store and are not included
in Git clones.

- `projects.yaml`
- `inbox.md`
- `docs/ideal.md`
- `docs/spec.md`
- `docs/methodology/state.yaml`
- `docs/methodology/graph.json`
- `docs/align-projects.md`
- `docs/scout.md`

## Reusable setup package

Conductor is a source library with shared guidance and explicit product variants,
not a whole-repo template. The [package guide](.agents/skills/setup-methodology/references/package-installation.md)
explains selection, preservation of local rules, and conditional modules. Audit
available source resources with:

```bash
python3 .agents/skills/setup-methodology/scripts/package.py audit
```

New-project installation requires reviewed Ideal/spec intake and a separate
explicit target. It preserves existing files and never generates an Ideal,
Spec, runtime, model call, or product proof.

For recurring collection, monitoring or reports, start with the optional
[deterministic scheduled-work kit](.agents/skills/setup-methodology/assets/scheduled-work/README.md).
It includes a runnable collector/gate, scheduler templates, recovery runbook,
and token-accounting guidance. Select it only when recurring work exists;
installation does not enable a timer or model transport. The
[source comparison](docs/scout/scout-101-deterministic-scheduled-work.md)
records what Bishop, Financial Monthly Analysis and AI Health actually prove.

## Commands

```bash
make methodology-compile
make methodology-check
make skills-sync
make skills-check
make lint
make test
```

For close-out, use the shared `/finish-and-push` validation policy to select and
reuse checks. Conductor's document/record checks are `make methodology-check`
and `make lint`; skill changes use `make skills-check`. Script or repo-check
changes use focused tests, broadening to `make test` when shared effects warrant
it. Refresh generated planning surfaces with `make methodology-compile` when
their sources change, before the final methodology check. Commits and story
bookkeeping do not require repeating checks over unchanged inputs.

Long-running `/loop-review` and `/loop-verify` work uses bounded problem-class
research and periodic strategy checkpoints within existing scope, budgets,
and stop rules; see [Alignment 053](docs/alignments/align-053-research-before-reinvention.md).
