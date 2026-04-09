# Conductor Spec

This spec records the active constraints around the supervisor project.

## spec:1 Project Registry & Routing

### spec:1.1 Tracked project registry

Conductor keeps one machine-readable registry in `projects.yaml` describing the
active projects, local paths, and comparison surfaces.

### spec:1.2 Single capture surface

Cross-project notes, sync requests, and raw links land in `inbox.md` first.
They should not require immediate structure to be captured.

## spec:2 Cross-Project Alignment

### spec:2.1 Distributed harness reality

The AI framework remains distributed across the tracked projects. Conductor does
not own a canonical copy of the skills or methodology artifacts.

### spec:2.2 Recommendation-first sync

Alignment work should classify differences as:

- intentional local adaptation
- portable improvement
- conflicting methodology change
- unclear drift

Conductor recommends next actions before applying blanket synchronization.

## spec:3 Scouting & External Research

### spec:3.1 Central scout intake

External sources can be dropped into `inbox.md` or promoted directly into scout
entries. Conductor evaluates them once, then maps likely value across projects.

### spec:3.2 Per-project adoption framing

Scout outputs must answer:

- what this source offers
- which project(s) should care
- whether the move is adopt, adapt, defer, reject, or spike

## spec:4 Story & Decision Preparation

### spec:4.1 Same story loop as other projects

Conductor should support the same practical loop as the other projects:

- triage
- create story
- build
- validate
- close out

### spec:4.2 Supervisor outputs are real work artifacts

Prepared sync tasks, scout recommendations, and methodology conflicts should
land as stories, ADRs, alignment logs, or scout logs rather than evaporating in
chat.

## spec:5 Memory & Operator Leverage

### spec:5.1 Alignment memory

`docs/align-projects.md` and `docs/alignments/` record cross-project comparison
history so the same drift investigation does not restart from zero.

### spec:5.2 Scout memory

`docs/scout.md` and `docs/scout/` record external research, adoption decisions,
and reusable conclusions.

### spec:5.3 Lightweight by design

Conductor should add the minimum structure needed to make recurring work
cheaper. If a new artifact does not save future time, it should not exist.

