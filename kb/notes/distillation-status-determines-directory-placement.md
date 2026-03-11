---
description: Hunch that procedural artifacts distilled for execution belong in kb/instructions/ — the directory boundary is "distilled into a procedure", not "compressed" or "frequently loaded"
type: note
traits: []
areas: [kb-design]
status: seedling
---

# Distillation status determines directory placement

The `kb/instructions/` directory collects procedures distilled for execution. The `kb/notes/` directory collects discursive reasoning. This note proposes sharpening that boundary into an organizational principle: if an artifact has been distilled *into a procedure* — reasoning stripped, steps sequenced, optimized for an agent that needs to act — it belongs in `instructions/`. The criterion is not "compressed" or "frequently loaded" but specifically "distilled into an executable procedure."

The immediate trigger: `kb/instructions/WRITING.md` sits at the top of the KB directory as a writing guide. It is a procedure — checklists, templates, imperative steps extracted from methodology notes. An agent loading WRITING.md is executing a procedure (how to write a note), not reasoning about knowledge design. By the procedural-distillation criterion, it belongs in `kb/instructions/`.

## Why this might work

**Maintenance becomes directory-scoped.** If all procedural distillations live in one place, you can audit them as a set: are they current relative to their source notes? Are they compressed enough? Do they overlap? Today, procedural artifacts are scattered (WRITING.md at `kb/`, skills in `instructions/` subdirectories).

**The boundary is legible.** "Is this a procedure an agent executes, or reasoning an agent deliberates with?" is a question agents and humans can answer quickly. It maps directly to the reading mode: follow steps vs. build understanding.

**It aligns with the loading hierarchy.** [Context-loading strategy](./context-loading-strategy.md) describes a hierarchy from always-loaded to on-demand. Procedures are loaded when an agent needs to act; discursive notes are loaded when an agent needs to reason. Grouping by reading mode makes the hierarchy concrete in the filesystem.

## How to evaluate

**Confirming evidence** (look for these over the next few maintenance cycles):

- Maintenance operations on `kb/instructions/` feel coherent — auditing and updating procedures is easier because they're co-located
- Moving WRITING.md to instructions doesn't break workflows or reduce its discoverability (CLAUDE.md routes to it regardless of path)
- The boundary helps when deciding where new artifacts go — "is this a procedure to execute?" is a faster routing question than the current type-based routing

**Disconfirming evidence** (any of these would weaken the principle):

- Some artifacts are genuinely mixed — partly distilled procedure, partly discursive reasoning — and the boundary forces an awkward split
- The `instructions/` directory becomes too large or heterogeneous to audit as a set (undermining the maintenance benefit)
- The prominence loss from moving WRITING.md out of `kb/` causes agents to miss it despite CLAUDE.md routing

## Open Questions

- Should this apply retroactively to all existing artifacts, or only to new ones?
- Does the skill/instruction distinction (automatic routing vs. manual invocation) still matter as a sub-boundary within `instructions/`, or does it collapse into a single collection?
- How does this interact with the [constraining gradient](./methodology-enforcement-is-constraining.md)? Distillation and constraining are different operations — does the directory boundary conflate them?

---

Relevant Notes:

- [skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) — foundation: defines the distillation relationship this note proposes using as a directory boundary
- [instructions are skills without automatic routing](./instructions-are-skills-without-automatic-routing.md) — context: the existing instruction/note boundary that this principle would sharpen
- [context-loading strategy](./context-loading-strategy.md) — enables: the loading hierarchy that distillation-based placement aligns with
- [areas exist because useful operations require reading notes together](./areas-exist-because-useful-operations-require-reading-notes-together.md) — parallel: areas organize notes for comparative reading; distillation status organizes artifacts for maintenance operations

Topics:

- [kb-design](./kb-design.md)
