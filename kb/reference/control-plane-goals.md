---
description: How Commonplace ships KB goals in always-loaded context — the AGENTS.md layout, the scaffolded AGENTS.md.template, and the install-time fill-in contract
type: kb/types/note.md
tags: []
---

# Control-plane goals

This note describes how KB goals live in always-loaded context in the shipped system: the scaffold contract, the always-loaded files, and the install-time fill-in flow.

## Where goals live in the shipped control plane

The control-plane file the system ships is `AGENTS.md`. KB goals live in a dedicated `## KB Goals and Scope` section near the top, structured into three subsections:

- **Purpose** — what decisions or actions the KB supports
- **Scope** — the domain boundary, made operational by in-scope and out-of-scope lists (the out-of-scope list is the guard against scope creep)
- **Quality bar** — domain-specific "good enough" standards

This placement is load-bearing on a runtime that loads root `AGENTS.md` with
binding force. In that consumption path, the goals are in context for every
write decision without a tool call, including a forked skill context whose
harness re-injects repository instructions. File placement alone does not
guarantee delivery: a worker packet may rely on this baseline only after its
runtime path has been verified. The section sits alongside the routing table,
vocabulary, version-control conventions, and other invariants the agent needs
from turn one.

## Delegation invariant

The shipped control plane names itself as Commonplace doctrine and makes a
handoff a task-specific delta from it. The delta carries purpose, deviations,
and deliberately open consequential choices, plus the authority, ownership,
constraints, commitments, acceptance, and return conditions that standing
doctrine cannot determine. The inherited defaults keep scheduling, integration,
and recovery with the parent and grant no nested-delegation authority. A worker
classifies an unstated choice as inherited, deliberately delegated, irrelevant,
or a gap. The detailed artifact-authoring contract lives in the instruction
type and collection so the always-loaded surface does not become a general
packet checklist.

This compression creates a broad dependency: changing the root delegation
rule changes the commission understood by every worker packet that omitted the
rule in reliance on it. Commonplace accepts that dependency for this universal
class instead of adding lineage fields to each packet. A root-rule edit must
therefore open a recorded search-and-review cohort of instructions and skills
that commission workers; those packets are not compressed against the changed
rule until reviewed. Narrower methodology-to-instruction dependencies continue
to use source-side lineage under the link contract.

## What varies per installation vs. what ships with the framework

| Concern | Per-installation or framework? | Where it lives |
|---|---|---|
| Purpose | Per-installation | `AGENTS.md` `## KB Goals and Scope` (filled in by the practitioner at install time) |
| Scope (boundary + in/out lists) | Per-installation | same |
| Quality bar | Per-installation | same |
| Routing table | Framework | `AGENTS.md` `## Using the KB`, generated/templated |
| Version-control expectation | Framework default; project workflow | `AGENTS.md` `## Version control` |
| Commonplace delegation doctrine | Framework | `AGENTS.md` `## Delegation` |
| Type system | Framework | `kb/types/` plus collection-local `kb/*/types/` directories with schemas and templates |
| Writing conventions | Framework | `kb/*/COLLECTION.md` (per-collection) |
| Link semantics | Framework | `kb/notes/links-README.md` and related guidance in `kb/instructions/` |

Only the per-installation rows require human input. Framework rows are shipped from Commonplace and can be updated mechanically on upgrade.

## The scaffold contract

`commonplace-init` copies `AGENTS.md.template` into the practitioner project as `AGENTS.md.template`, which the practitioner fills in and renames (or copies into) `AGENTS.md`. The template carries:

- A placeholder `## KB Goals and Scope` section with HTML comment guidance for each subsection, as concrete prose examples the practitioner replaces with their own answers
- A stock `## Version control` section that makes versioned maintenance the default while leaving commit, branch, and review semantics to the project
- A stock `## Delegation` section that makes task packets deltas from a verified Commonplace doctrine, preserves task authority and parent integration, and classifies unstated choices
- A stock `## Using the KB` routing section pointing at `kb/notes/`, `kb/reference/`, and `kb/instructions/`
- A stock Skills and Commands section listing the Commonplace-provided skills
- `{{project_name}}` placeholders that `init_project` substitutes with the directory name

The three-subsection layout in the template matches the structure the generated file expects, so the scaffold is self-demonstrating: the placeholder text shows the exact shape the practitioner is editing toward.

## The install-time fill-in flow

The installation guidance distils the "fill in the KB Goals section" step for practitioners. It walks through the five subsections with emphasis on the scope-boundary framing for Domain and the contrast-with-Include framing for Exclude.

Concretely, the install sequence is:

1. `commonplace-init --root .` creates the directory structure and scaffolds `AGENTS.md.template` with placeholder goals
2. The practitioner renames or copies the template to `AGENTS.md` and fills in the five subsections
3. Agents in a runtime configured to load root repository instructions receive `AGENTS.md` and see the populated goals on every invocation

The agent has no fallback if goals are left unfilled — an empty `## KB Goals` section is a silent failure mode, which is why the installation guidance treats the fill-in step as a first-run requirement rather than optional polish.

## Relationship to other Commonplace invariants

- The routing and navigation content (`## Using the KB`, including its Collection Routing and Navigation subsections) is generated from the framework and does not vary per installation.
- A vocabulary section is optional and project-specific; many installations will not need one.
- The version-control expectation is framework-shipped; commit, branch, review, and other development conventions are project-customizable.

---

Relevant Notes:

- [006-two-tree-installation-layout](./adr/006-two-tree-installation-layout.md) — decision: the installation step that creates the control-plane fragment and copies the template
- [014-scripts-as-python-package-one-tree-model](./adr/014-scripts-as-python-package-one-tree-model.md) — decision: `commonplace-init` as the scaffold entry point and the one-tree install model
- [architecture](./architecture.md) — shipped architecture: where the control-plane file sits inside the installed surface
- [Intent-framed delegation is a control regime; prompt length does not establish it](../notes/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) — rationale: the shared mechanism and conditional agent-side control surfaces behind the compact invariant
