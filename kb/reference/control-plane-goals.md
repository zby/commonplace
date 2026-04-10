---
description: How commonplace realises KB goals in always-loaded context today — the AGENTS.md layout, the scaffolded AGENTS.md.template, the install-time fill-in contract, and INSTALL.md distillation
type: note
tags: [architecture]
status: current
---

# Control-plane goals

How commonplace currently instantiates the [KB goals in always-loaded context](../notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) argument. This is a current-state description of the scaffold contract, the always-loaded files, and the install-time fill-in flow. For the general claim that goals belong in always-loaded control-plane context, see the theory note.

## Where goals live in commonplace

The control-plane file in commonplace is `AGENTS.md` (with `CLAUDE.md` as a symlink to it). KB goals live in a dedicated `## KB Goals` section near the top, structured into five subsections:

- **Purpose** — what decisions or actions the KB supports
- **Domain** — scope boundary
- **Include** — types of knowledge that belong
- **Exclude** — types of knowledge that don't belong despite seeming relevant
- **Quality bar** — domain-specific "good enough" standards

This placement is load-bearing. `AGENTS.md` is loaded on every agent invocation, so the goals are in context for every write decision without any tool call. The section sits alongside the routing table, vocabulary, git conventions, and other invariants the agent needs from turn one.

## What varies per installation vs. what ships with the framework

| Concern | Per-installation or framework? | Where it lives |
|---|---|---|
| Purpose | Per-installation | `AGENTS.md` `## KB Goals` (filled in by the practitioner at install time) |
| Domain | Per-installation | same |
| Include | Per-installation | same |
| Exclude | Per-installation | same |
| Quality bar | Per-installation | same |
| Routing table | Framework | `AGENTS.md` `## Using the KB`, generated/templated |
| Type system | Framework | `kb/*/types/` directories with schemas and templates |
| Writing conventions | Framework | `kb/instructions/WRITING.md` |
| Link semantics | Framework | `kb/notes/links-index.md` and supporting theory notes |

Only the per-installation rows require human input. Framework rows are shipped from commonplace and can be updated mechanically on upgrade.

## The scaffold contract

`commonplace-init` copies `AGENTS.md.template` into the practitioner project as `AGENTS.md.template`, which the practitioner fills in and renames (or copies into) `AGENTS.md`. The template carries:

- A placeholder `## KB Goals` section with HTML comment guidance for each subsection, as concrete prose examples the practitioner replaces with their own answers
- A stock `## Using the KB` routing section pointing at `kb/notes/`, `kb/reference/`, and `kb/instructions/`
- A stock Skills and Commands section listing the commonplace-provided skills
- `{{project_name}}` placeholders that `init_project` substitutes with the directory name

The five-subsection layout in the template matches the layout used here in commonplace's own `AGENTS.md`, so the scaffold is self-demonstrating: the canonical reference for what a filled-in Goals section looks like is the file the practitioner is currently editing against.

## The install-time fill-in flow

[INSTALL.md](../../INSTALL.md) distils the "fill in the KB Goals section" step for practitioners. It walks through the five subsections with emphasis on the scope-boundary framing for Domain and the contrast-with-Include framing for Exclude. The distillation is deliberately short: the full argument lives in the [theory note](../notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md), while INSTALL.md gives the operator just enough to act.

Concretely, the install sequence is:

1. `commonplace-init --root .` creates the directory structure and scaffolds `AGENTS.md.template` with placeholder goals
2. The practitioner renames or copies the template to `AGENTS.md` and fills in the five subsections
3. First-session agents load `AGENTS.md` and see the populated goals on every invocation

The agent has no fallback if goals are left unfilled — an empty `## KB Goals` section is a silent failure mode, which is why INSTALL.md flags the fill-in step as a first-run requirement rather than an optional polish.

## Relationship to other commonplace invariants

- The routing table (`## Using the KB` and `## Key Indexes`) is generated from the framework and does not vary per installation.
- The vocabulary section in commonplace's own `AGENTS.md` is specific to this KB's methodology terms; practitioner projects normally don't need one.
- Git and development conventions are framework-shipped but customizable.

---

Relevant Notes:

- [kb-goals-in-always-loaded-context-guide-inclusion-decisions](../notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) — theory: the general claim that goals belong in always-loaded control-plane context, with the full argument for why every write is an inclusion decision
- [006-two-tree-installation-layout](./adr/006-two-tree-installation-layout.md) — decision: the installation step that creates the control-plane fragment and copies the template
- [014-scripts-as-python-package-one-tree-model](./adr/014-scripts-as-python-package-one-tree-model.md) — decision: `commonplace-init` as the scaffold entry point and the one-tree install model
- [architecture](./architecture.md) — current-state: where the control-plane file sits inside the broader repo layout
- [INSTALL.md](../../INSTALL.md) — distilled operator guidance for filling in the KB Goals section at install time
