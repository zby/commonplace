---
description: Scenario-derived shipped architecture — the user's KB in the project, the library read in place from the installed package, package-provided commands, promoted skills, and a measurable scenario decomposition
type: types/note.md
tags: []
---

# Scenario architecture

How Commonplace instantiates scenario-derived architecture in the shipped system. This note describes the installed KB surface (the user's collections in the project and the library in the installed package), the command-and-skill split that supports it, and the measurable scenario decomposition that explains those choices.

## The shipped operating context

An installed project works with two surfaces:

- the project's `kb/` — the user's own collections (`kb/notes/`, `kb/reference/`, `kb/instructions/`, and the rest), scaffolded without user-authored artifacts but with starter `COLLECTION.md` contracts and `README.md` landings;
- the Commonplace library — methodology notes, reference, instructions, and the global types — read in place from the installed package. `.commonplace/library.md` gives its location on the machine.

Plus two supporting runtime surfaces:

- `commonplace-*` commands provided by the installed Python package
- promoted framework skills, reached through stubs under `.claude/skills/` and `.agents/skills/` that point to the real skill directories in the library

The project holds no copy of the library. The agent's normal path:

- route from `AGENTS.md`, and read `.commonplace/library.md` for the library's location (Claude Code has it in context through `CLAUDE.md`)
- read the target collection's `COLLECTION.md` (the user's own when writing, or the library's for established conventions)
- load the relevant type definition: a global type from the library's `types/`, or a collection-local type from `kb/<collection>/types/`
- write into the user's `kb/`
- invoke a promoted skill or CLI command when the workflow needs one

## Write a note, decomposed against the shipped layout

| Step | Context needed | Where it lives |
|------|---------------|----------------|
| Route to the correct location | Routing table, library location | `AGENTS.md`, `.commonplace/library.md` |
| Decide whether it belongs | KB goals and scope boundary | `AGENTS.md` `## KB Goals and Scope` |
| Find related notes | Searchable user and library notes | `kb/notes/`, the library's `notes/` |
| Know how to write well | Writing conventions | target collection's `COLLECTION.md` (e.g. `kb/notes/COLLECTION.md`) |
| Know the structure | Global or collection-local type definitions | the library's `types/`, `kb/<collection>/types/` |
| Write the file | All of the above | `kb/notes/` or another user collection |
| Connect it to existing knowledge | Skill or manual linking workflow | promoted `cp-skill-connect` skill plus indexes |

The key architectural property is a fixed read/write split: writes always target the user's collections inside the project, and the library is consulted read-only at the location `.commonplace/library.md` names. Reading the library costs the agent one read of that file per session at most, and nothing in Claude Code, which imports it.

## When the common path is not enough

The shipped system still needs a place for deeper explanation, and that explanation lives in the library:

- the library's `reference/` explains how the shipped system works
- the library's `reference/adr/` records why major architectural choices were made
- project-local notes in `kb/notes/` can extend that explanation when the shipped docs are not enough

Explanatory material is part of the installed library, not an external escalation target. It stays outside the project's collection paths, so project searches and version history show only the project's own files.

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
