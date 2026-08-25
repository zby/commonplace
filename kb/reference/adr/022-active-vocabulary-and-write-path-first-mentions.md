---
description: Accepted decision to define active vocabulary in AGENTS.md while making first-mention glossing a cp-skill-write authoring behavior
type: ../types/adr.md
tags: []
status: accepted
---

# 022-active-vocabulary-and-write-path-first-mentions

**Status:** accepted
**Date:** 2026-05-17
**Refines:** [ADR-011](./011-notes-must-be-accessible-to-external-readers.md), [ADR-017](./017-collection-md-is-the-register-convention-boundary.md), [ADR-019](./019-collection-owned-link-vocabulary.md)

## Context

Commonplace needs a small vocabulary that agents and maintainers can treat as having KB-specific meanings. Placing the first-mention rule in the `AGENTS.md` Vocabulary section beside the term list keeps the rule near the terms it governs, but blurs two responsibilities:

- `AGENTS.md` declares always-loaded project context.
- `cp-skill-write` owns authoring behavior when writing or materially editing KB artifacts.

The first-mention rule is an authoring behavior. It should shape prose written through the writing path, not every search, review, planning, or conversational action an agent performs after loading `AGENTS.md`.

Collections already own register and linking conventions through `COLLECTION.md` ([ADR-017](./017-collection-md-is-the-register-convention-boundary.md)). They also authorize link labels such as `defined-in` through collection-owned outbound rules ([ADR-019](./019-collection-owned-link-vocabulary.md)). Making collections declare vocabulary scope now would be premature: the current need is only a KB-global term list, and collection-local or type-specific vocabularies can be added later when a real collection or type needs them.

Installed projects add another boundary. Shipped Commonplace definitions may remain available as library material under `kb/commonplace/`, but a user project should not inherit Commonplace's methodology vocabulary as its own active vocabulary unless its project-owned `AGENTS.md` declares it.

## Decision

Introduce **active vocabulary** as the name for the KB-global list of terms declared in `AGENTS.md`.

For v1, active vocabulary has one source only:

- `AGENTS.md` declares the active vocabulary for the current KB.

Do not add collection-local vocabulary, type-specific vocabulary, vocabulary manifests, scope metadata, imports, or collision handling yet.

Move the operative first-mention rule to `cp-skill-write`:

- When writing or materially editing prose, use the active vocabulary declared in `AGENTS.md`.
- On first meaningful mention of an active vocabulary term in the artifact, gloss and link it when the reader may not know the term.
- Do not churn untouched passages only to add vocabulary links.

Keep `COLLECTION.md` responsible for link authorization, not vocabulary declaration. A collection may authorize `defined-in` as a link label and define which destination holds definition notes, but that does not by itself make a term active vocabulary.

Definition notes remain backing documentation. In this repo, active vocabulary terms normally point to `kb/notes/definitions/`. In an installed project, user-owned active vocabulary should point to user-owned definition notes unless the project explicitly chooses to link to shipped library definitions under `kb/commonplace/`.

ADR-011's accessibility requirement still stands: authored notes should be readable without assuming the reader loaded `AGENTS.md`. This ADR narrows where the authoring rule is taught and executed.

## Consequences

**Easier:**

- `AGENTS.md` has a cleaner role: it declares active vocabulary instead of carrying write-procedure details.
- `cp-skill-write` becomes the single operational home for first-mention glossing and definition-link behavior.
- Agents are less likely to over-apply first-mention behavior during non-writing tasks.
- Installed projects can define their own active vocabulary without inheriting Commonplace's methodology terms as project law.
- The design has a simple expansion path: later ADRs can add collection-local or type-specific vocabulary only when needed.

**Harder:**

- The term list and the authoring behavior are no longer colocated, so the write skill must explicitly name and load `AGENTS.md` active vocabulary.
- Collection authors may expect vocabulary to live beside link rules in `COLLECTION.md`; v1 intentionally declines that extra policy surface.

**Not changing:**

- `defined-in` remains a link label authorized by collection outbound-linking rules.
- Definition notes remain normal typed KB artifacts, not a separate vocabulary database.
- `cp-skill-write` still reads the target collection's `COLLECTION.md` and selected type spec before writing.
- Reader accessibility remains the reason for first-mention glosses and definition links.

---

Relevant Notes:

- [AGENTS.md](../../../AGENTS.md) - declares: the active vocabulary for this KB
- [cp-skill-write](../../instructions/cp-skill-write/SKILL.md) - implements: the write-path first-mention behavior
- [ADR-011: notes must be accessible to external readers](./011-notes-must-be-accessible-to-external-readers.md) - rationale: why first mentions need glosses and definition links
- [ADR-017: COLLECTION.md is the register convention boundary](./017-collection-md-is-the-register-convention-boundary.md) - foundation: collection-owned writing conventions
- [ADR-019: collection-owned link vocabulary](./019-collection-owned-link-vocabulary.md) - foundation: collection-owned authorization for labels such as `defined-in`
