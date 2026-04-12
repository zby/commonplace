---
description: Scenario-derived shipped architecture — one-tree installed KB, package-provided commands, promoted skills, and a measurable scenario decomposition
type: note
tags: []
status: current
---

# Scenario architecture

How commonplace instantiates scenario-derived architecture in the shipped system. This note describes the installed one-tree KB surface, the command-and-skill split that supports it, and the measurable scenario decomposition that explains those choices.

## The shipped operating context

An installed project has one KB tree under `kb/`, plus two supporting runtime surfaces:

- `commonplace-*` commands provided by the installed Python package
- promoted framework skills under `.claude/skills/` and `.agents/skills/`

There is no separate vendored `commonplace/` framework tree anymore. The agent's normal path stays inside the project:

- route from `AGENTS.md`
- read `kb/instructions/WRITING.md`
- load the relevant type definition from `kb/types/` or `kb/*/types/`
- write into `kb/`
- invoke a promoted skill or CLI command when the workflow needs one

## Write a note, decomposed against the shipped layout

| Step | Context needed | Where it lives |
|------|---------------|----------------|
| Route to the correct location | Routing table | `AGENTS.md` |
| Decide whether it belongs | KB goals and scope boundary | `AGENTS.md` `## KB Goals` |
| Find related notes | Searchable note library | `kb/notes/` |
| Know how to write well | Writing conventions | `kb/instructions/WRITING.md` |
| Know the structure | Global or collection-local type definitions | `kb/types/`, `kb/*/types/` |
| Write the file | All of the above | `kb/notes/` or another collection |
| Connect it to existing knowledge | Skill or manual linking workflow | promoted `cp-skill-connect` skill plus indexes |

The key architectural property is locality: the common write path does not require the agent to leave the installed tree.

## When the common path is not enough

The shipped system still needs a place for deeper explanation, but that explanation now lives inside the same KB surface rather than in a separate framework checkout:

- `kb/reference/` explains how the shipped system works
- `kb/reference/adr/` records why major architectural choices were made
- project-local notes can extend that explanation when the shipped docs are not enough

That is the important reversal from the old two-tree design: explanatory material is part of the installed surface, not an external escalation target.

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
