---
description: How collections and types compose in commonplace - collections own register conventions and link rules, types own structural contracts, and the two meet at collection-scoped type lookup; covers the COLLECTION.md surface, the compiled collection-topology used by the connect skill, and the compile-collections skill that produces it
type: kb/types/note.md
tags: []
status: current
---

# Collections and types

Every authored artifact in commonplace makes two independent decisions:

- **Which collection it lives in** — picks the *register* (theoretical, descriptive, prescriptive), the writing conventions, and the rules for how it links to artifacts in other collections.
- **Which type it instantiates** — picks the *structural contract*: what frontmatter the artifact carries and what required sections the body must contain.

Collections and types are orthogonal. The collection answers "what kind of thing does this aim to be (a claim, a description, a procedure)?"; the type answers "what shape does the file have?". They meet at one place: the type resolver looks for a type's definition first inside the artifact's collection, then falls back to the global layer.

Read this document to get the model. For the type catalog see [available-types](./available-types.md); for the resolution mechanics see [type-loading](./type-loading.md); for the precise definition of "collection" see [definitions/collection](./definitions/collection.md).

## Collections

A **collection** is a top-level subdirectory of `kb/` that groups artifacts sharing a domain, owns or inherits a type contract, and is the unit at which context-budget decisions (validation scope, connect discovery, area splits) are made. Subdirectories inside a collection are *areas* — they share the collection's type contract and budget rather than defining their own.

The shipped collections:

| Collection | Register | Quality goal |
|---|---|---|
| `kb/notes/` | theoretical | reach |
| `kb/reference/` | descriptive | fidelity + economy |
| `kb/instructions/` | prescriptive | executability + precision |
| `kb/agent-memory-systems/` | descriptive (with root-level analysis exceptions) | fidelity + economy |
| `kb/sources/` | descriptive (ingested external content) | faithful capture |
| `kb/work/` | catch-all workshop layer | move active work forward; extract durable conclusions |

Each collection's writing conventions live in its own `COLLECTION.md` at the collection root: title conventions, quality discipline, what does and does not belong, and the outbound linking table for that register. [ADR-017](./adr/017-collection-md-is-the-register-convention-boundary.md) is the decision that pinned register conventions to `COLLECTION.md` rather than to the type definitions.

`kb/types/` sits at the top level under `kb/` but is not a collection in this sense — it is the global type layer. Some collections, such as `kb/instructions/`, are framework-shipped rather than primarily practitioner-authored, but they still carry authored artifacts, register conventions, and type contracts. See the [collection definition](./definitions/collection.md) for the full exclusion list.

## Types

A **type** is a structural contract — a JSON Schema plus a template plus authoring instructions. Every artifact has exactly one type, declared in its `type:` frontmatter field. The `type:` field is a free-form string, not an enum, so consuming projects can add types locally by dropping a template, instructions, and schema into a collection's `types/` directory.

Two scopes:

- **Global types** live in `kb/types/`. The shipped global types are `text` (no frontmatter, always valid — the root of the type ladder), `note` (the base structured type all others inherit from), `instruction` (prescriptive procedures and review gates), `definition` (vocabulary), and `index` (navigation hubs). Globals are global because they can occur in any collection.
- **Directory-scoped types** live in `kb/<collection>/types/`. They apply only to artifacts in that collection. Examples: `adr` in `kb/reference/types/`, `source-review` and `ingest-report` in `kb/sources/types/`, `connect-report` in `kb/reports/types/`.

Type resolution is a path walk: from the artifact's path the resolver checks the collection's `types/` first, then falls back to `kb/types/`. See [type-loading](./type-loading.md) for the full mechanics.

Types describe structure, not semantics. Semantic review expectations live on a separate axis — the `traits` field on `note`-derived types — per [ADR-012](./adr/012-types-for-structure-traits-for-review.md).

## Cross-collection linking

The collection determines the *register* of an artifact, and links between registers carry different meaning than links inside one. A theoretical note linking to a descriptive note is citing evidence; a descriptive note linking to a theoretical note is citing rationale. Each collection's `COLLECTION.md` carries an outbound linking table for these cases.

To avoid every author having to read every `COLLECTION.md` before adding a link, the linking rules are compiled into one place:

- **`kb/reports/collection-topology.md`** — a compiled, compact view of the collection registry plus a register-pair linking matrix. Optimized for an agent loading it into bounded context to make one decision: what relationship label to use when linking from collection A to collection B.
- **[cp-skill-compile-collections](../instructions/cp-skill-compile-collections/SKILL.md)** — the skill that reads every `COLLECTION.md`, distills the registers, quality goals, and outbound linking tables into the topology document, and writes it to `kb/reports/collection-topology.md`. Run it when a `COLLECTION.md` changes or before a connection sweep.
- **[cp-skill-connect](../instructions/cp-skill-connect/SKILL.md)** — the skill that loads the topology document during discovery so it can pick relationship labels appropriate to the source/target register pair without re-reading every collection's conventions.

The topology document is regenerated from the `COLLECTION.md` files; treat it as cache, not source. If a linking rule needs to change, edit the relevant `COLLECTION.md` and rerun `cp-skill-compile-collections`. The compile skill is LLM-driven (it reads each `COLLECTION.md` as prose), so two runs on identical input can produce different bytes that say the same thing — that's why the trigger is "rerun on edit," not "regenerate-and-diff in CI."

`commonplace-init` ships a default `kb/reports/collection-topology.md` compiled from the default `COLLECTION.md` files in the scaffold, so the connect skill works on first run. Any project that adds collections, edits a `COLLECTION.md`, or changes a register's outbound linking table is responsible for rerunning the compile skill — there is no automatic staleness check today.

## How an artifact comes together

For an existing artifact, the two axes resolve like this:

1. The artifact's path identifies its collection. The collection's `COLLECTION.md` defines the writing conventions that apply, and the collection's outbound linking table (compiled into the topology) defines what relationship labels to use when linking outward.
2. The artifact's `type:` frontmatter identifies its type. The type resolver walks from the artifact's path through the collection's `types/` to `kb/types/` to find the type's schema, template, and instructions. The schema defines what frontmatter is required and what body sections must exist.
3. The validator checks structural conformance (type contract). Review gates check semantic conformance (the `traits` axis).

When authoring a new artifact, the same two decisions happen in reverse: pick the collection (which register fits the intent?), then pick the type (what shape best carries the content?).

---

Relevant Notes:

- [available-types](./available-types.md) — extends: the catalog of shipped global and collection-scoped types
- [type-loading](./type-loading.md) — extends: the resolution mechanics that walk from artifact path to type definition
- [definitions/collection](./definitions/collection.md) — extends: the precise definition of "collection" with scope, exclusions, and misuse cases
- [ADR-012: types for structure, traits for review](./adr/012-types-for-structure-traits-for-review.md) — grounds: the decision to keep structural types and semantic-review traits on separate axes
- [ADR-017: COLLECTION.md is the register convention boundary](./adr/017-collection-md-is-the-register-convention-boundary.md) — grounds: the decision to host register conventions in `COLLECTION.md` rather than in type definitions
