---
description: Accepted decision to use collection-level COLLECTION.md files as the register convention boundary while keeping types structural and allowing mixed-register collections
type: ../types/adr.md
tags: []
status: accepted
---

# 017-collection-md-is-the-register-convention-boundary

**Status:** accepted
**Date:** 2026-04-13

## Context

Commonplace had a global writing guide (`kb/instructions/WRITING.md`) plus type templates. That split optimized for the early write path, where most artifacts were theory notes. It became the wrong boundary once the KB had several collections with different writing goals:

- `kb/notes/` optimizes for theoretical reach.
- `kb/reference/` optimizes for descriptive fidelity and economy.
- `kb/instructions/` optimizes for executable precision.
- `kb/agent-memory-systems/` is primarily descriptive, but allows root-level analyses that can become claim-shaped when they make a cross-system argument.

The pressure was not that register intrinsically belongs to a collection. Register could have been encoded in types, an explicit `register:` frontmatter field, subdirectories, or convention alone. But the existing collection boundary already carried related operational meaning: it owned indexes, scoped tags, gave the agent a search boundary, and already participated in collection-local type lookup.

Types were a poor fit for this job because they describe structural contracts. A `note` in `kb/notes/` and a `note` in `kb/reference/` can share the same frontmatter and body structure while needing different title style, quality goal, and linking rules. Making types carry register would blur the type/trait/placement split from [ADR-012](./012-types-for-structure-traits-for-review.md).

Frontmatter was more flexible, but it would require another field on every structured artifact and would be easy to set incorrectly. Convention alone was lighter, but invisible to tools and too easy for agents to skip.

The important boundary is therefore not "one collection must contain exactly one register." The important boundary is "the collection tells the agent what register profile and exceptions apply here."

## Decision

Commonplace uses each collection's `COLLECTION.md` as the register convention boundary.

Every writable collection must provide a root-level `COLLECTION.md` that tells agents and maintainers how to write in that collection. At minimum, it records the collection's register profile, quality goal, title and description conventions, outbound linking conventions, and placement exclusions.

A collection may be mixed-register. When it is, its `COLLECTION.md` must say so explicitly and describe the local rules. For example, a primarily descriptive collection can allow claim-shaped root-level analyses while keeping individual reviews descriptive.

The write workflow is:

1. Resolve the target collection.
2. Read `kb/<collection>/COLLECTION.md` for collection/register conventions.
3. Resolve the artifact type for structural scaffolding.
4. Apply universal mechanics from the write skill.

This keeps responsibilities separate:

- **Collections** own register conventions and placement rules.
- **Types** own structural contracts: templates, type instructions, and schemas.
- **Skills** own universal mechanics and the default write flow.
- **Indexes and reports** use the collection boundary for scoped discovery.

`WRITING.md` is removed. ADR-002's global-writing-guide optimization is superseded. ADR-016's template/instructions pair for specialized types remains accepted, but its assumption that `WRITING.md` is the generic always-loaded guide is superseded by this decision.

## Consequences

**Easier:**
- The same structural type can be reused across registers. `type: kb/types/note.md` means "uses the note contract," not "is theoretical."
- New collections can add their own writing convention surface without editing a central writing guide or changing the type system.
- Mixed-register collections have a place to document their local exceptions instead of forcing a premature split or a new type.
- Agents get a stable loading path: collection conventions first, then type structure.
- Types stay structural, preserving the type/trait/placement boundary from ADR-012.

**Harder:**
- Directory placement now has semantic weight. Moving a file between collections can change its expected writing conventions even if its `type:` does not change.
- Every writable collection needs a good `COLLECTION.md`; a missing or vague one is an operational defect.
- Mixed-register collections need careful prose rules because the model no longer assumes purity at the directory boundary.
- Register correctness is not a deterministic validation check. It remains a writing/review concern unless future review gates are added. (Amended 2026-07-08: [ADR-041](./041-collection-conformance-reviews-use-collection-md-as-the-gate.md) adds that check — a note is reviewable against its `COLLECTION.md` as a collection-conformance pair; correctness stays a review judgment, not a validator check.)
- Global searches by register are less direct than a frontmatter field would be; the collection topology, not each note's frontmatter, is the register map.

---

Relevant Notes:

- [Register](../../notes/definitions/text-contract.md) - defines register as a content mode and notes that collection-level encoding is a design choice, not a theoretical necessity
- [A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking](../../notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) - foundation: the three-register theory and the argument for per-register conventions
- [Type loading](../type-loading.md) - describes how authoring and validation resolve structural type contracts after the collection convention boundary is selected
- [ADR-012: types for structure, traits for review](./012-types-for-structure-traits-for-review.md) - foundation: keeps structural type identity separate from semantic review and placement conventions
- [ADR-016: custom types use template/instruction pairs](./016-custom-types-use-template-instruction-pairs.md) - preserved for specialized type packaging, but its `WRITING.md` loading assumption is superseded here
