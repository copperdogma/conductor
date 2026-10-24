# Reference Library

Useful tools, libraries, papers, and techniques to remember for future projects.
Entries get a small source check so we can find the real project again and know
what still needs testing. Saving a reference creates no adoption or backlog task.

## Browse

| Reference | Useful when | Tags | Last checked | Evidence |
| --- | --- | --- | --- | --- |
| [image-blaster](reference/image-blaster.md) | Starting a 3D environment from a photo or concept image | image-to-3D, world-generation, meshes, gaussian-splats, game-dev, previz | 2026-10-24 | Source-checked; untested |

## During project kickoff and setup

`/init-project` and `/setup-methodology` browse this index for capabilities the
new project needs. Bring useful tools or working implementations into the user
discussion, even when they mainly inform a custom build. Recheck current sources
and alternatives before recommending adoption; a saved reference is a starting
point, not a preferred dependency. Record fit and the reuse/adapt/build rationale
in existing kickoff or setup notes. No match is an acceptable result.

## Adding a reference

1. Capture raw links in [inbox.md](../inbox.md), or process a direct request in
   the same session and leave a handled receipt there.
2. Resolve the original post to the official repository, documentation, or paper.
   Use the source-specific connector when available; record retrieval gaps.
3. Make a bounded check: does it exist, what does it offer, what does it require,
   and what obvious limitations affect future use? Read primary sources; no
   install, paid run, benchmark, or portfolio-wide investigation is needed.
4. Search this index and `docs/reference/` for duplicates. Update an existing
   entry by canonical project identity, or add a short, descriptively named file.
5. Add an index row with use case, searchable tags, check date, and evidence level.
   Keep claims from the author separate from anything demonstrated locally.

Each entry records:

- Name, canonical link, one-sentence capability, and useful-when examples.
- Tags, original discovery link, primary sources, and last-check date.
- Requirements, license, service/cost caveats, and important limitations.
- Evidence: **Unresolved** (identity/link not confirmed), **Source-checked**
  (primary material inspected), or **Locally tested** (link the actual test and
  its limits). A project can exist without its advertised quality being proven.
- Disposition and a concrete trigger for revisiting it.

When a project actually needs the capability, recheck changing facts and use
[/scout](../.agents/skills/scout/SKILL.md) for adoption analysis, linking back
here. Full research and decisions live in [scout memory](scout.md); this library
is the capability-oriented lookup surface. Existing scouts stay where they are;
add library pointers selectively when useful. References without a current owner
stay here rather than creating speculative work in target repositories.
