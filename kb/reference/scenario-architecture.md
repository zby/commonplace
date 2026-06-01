---
description: Scenario-derived shipped architecture — single KB root with a library/user split under kb/commonplace/, package-provided commands, promoted skills, and a measurable scenario decomposition
type: kb/types/note.md
tags: []
status: current
---

# Scenario architecture

How Commonplace instantiates scenario-derived architecture in the shipped system. This note describes the installed KB surface (library and user collections under one `kb/` root), the command-and-skill split that supports it, and the measurable scenario decomposition that explains those choices.

## The shipped operating context

An installed project has one `kb/` root containing two coexisting surfaces:

- `kb/commonplace/` — the shipped library (read-only by convention): methodology notes, reference, instructions, and agent-memory-system reviews.
- `kb/notes/`, `kb/reference/`, `kb/instructions/` — the user's own collections, scaffolded empty with a starter `COLLECTION.md`.

Plus two supporting runtime surfaces:

- `commonplace-*` commands provided by the installed Python package
- promoted framework skills under `.claude/skills/` and `.agents/skills/` (symlinks into `kb/commonplace/instructions/`)

There is no separate vendored `commonplace/` framework tree. The agent's normal path stays inside the project:

- route from `AGENTS.md`
- read the target collection's `COLLECTION.md` (the user's own when writing, or the library's for established conventions)
- load the relevant type definition from `kb/types/` (shared global) or `kb/<collection>/types/` (collection-local)
- write into the user's `kb/`
- invoke a promoted skill or CLI command when the workflow needs one

## Write a note, decomposed against the shipped layout

| Step | Context needed | Where it lives |
|------|---------------|----------------|
| Route to the correct location | Routing table | `AGENTS.md` |
| Decide whether it belongs | KB goals and scope boundary | `AGENTS.md` `## KB Goals` |
| Find related notes | Searchable library and user notes | `kb/notes/`, `kb/commonplace/notes/` |
| Know how to write well | Writing conventions | target collection's `COLLECTION.md` (e.g. `kb/notes/COLLECTION.md`) |
| Know the structure | Global or collection-local type definitions | `kb/types/`, `kb/<collection>/types/` |
| Write the file | All of the above | `kb/notes/` or another user collection |
| Connect it to existing knowledge | Skill or manual linking workflow | promoted `cp-skill-connect` skill plus indexes |

The key architectural property is locality: the common write path does not require the agent to leave the installed tree. Writes always target the user's collections; the library is consulted read-only.

## When the common path is not enough

The shipped system still needs a place for deeper explanation, and that explanation lives inside the library under `kb/commonplace/`:

- `kb/commonplace/reference/` explains how the shipped system works
- `kb/commonplace/reference/adr/` records why major architectural choices were made
- project-local notes in `kb/notes/` can extend that explanation when the shipped docs are not enough

Explanatory material is part of the installed surface under `kb/commonplace/`, not an external escalation target. The split from the earlier model is that it now lives in its own namespace rather than sharing the user's collection paths.

## The control-plane contract

`AGENTS.md` is still the always-loaded routing layer that makes the scenario executable. It carries:

- the KB goals that decide inclusion
- the routing table for collections
- the search hints for finding prior knowledge
- the skill and command affordances the agent can invoke

Because this file is always loaded, it anchors the scenario decomposition: the agent knows where to start before it has opened any other artifact.

## Measurement surface

The decomposition can be represented as scenario files that name the source artifacts each step depends on and let evaluation tooling measure instruction bytes against the current files.

This gives the architecture a falsifiable surface:

- hop structure is encoded in the scenario description
- instruction bytes are measured dynamically from the real files
- architecture changes can be re-evaluated without rewriting the measurement method

---

Relevant Notes:

- [014-scripts-as-python-package-one-tree-model](./adr/014-scripts-as-python-package-one-tree-model.md) — decision: the one-tree shipped model this scenario note describes
- [architecture](./architecture.md) — the broader shipped architecture this scenario view decomposes
- [control-plane-goals](./control-plane-goals.md) — how the always-loaded control plane carries the inclusion and routing context the scenario depends on
- [instruction-generation](./instruction-generation.md) — how `commonplace-init` materialises the files this scenario consumes
