---
description: How collections and types compose in commonplace - collections own register conventions and link rules, types own structural contracts declared in type-spec docs, and the two meet through path-valued type pointers listed in COLLECTION.md; covers the COLLECTION.md surface, the compiled collection-topology used by the connect skill, and the compile-collections skill that produces it
type: kb/types/note.md
tags: []
status: current
---

# Collections and types

Every authored artifact in commonplace makes two independent decisions:

- **Which collection it lives in** — picks the *register* (theoretical, descriptive, prescriptive), the writing conventions, and the rules for how it links to artifacts in other collections.
- **Which type it instantiates** — picks the *structural contract*: what frontmatter the artifact carries and what required sections the body must contain.

Collections and types are orthogonal. The collection answers "what kind of thing does this aim to be (a claim, a description, a procedure)?"; the type answers "what shape does the file have?". They meet in `COLLECTION.md`: each collection's `## Types` section lists the type-spec docs it offers for new writes, and an artifact's `type:` frontmatter stores the path of the chosen type-spec doc directly.

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

A **type** is a structural contract expressed as a hand-authored **type-spec doc**: a markdown file carrying type-spec frontmatter (`type: kb/types/type-spec.md`, `name`, `description`, `schema`) plus authoring prose and an optional template block. Every artifact with frontmatter has exactly one type, declared as the repo-relative path to its type-spec doc in the `type:` field — for example `type: kb/reference/types/adr.md`. Consuming projects add types by dropping a new type-spec doc (and, when structural validation is desired, a sibling `.schema.yaml`) into the appropriate `types/` directory and listing it in the owning collection's `COLLECTION.md`.

Two scopes:

- **Global type-spec docs** live in `kb/types/`. The shipped globals are `type-spec` (the self-referential root), `note` (the base structured type), `instruction` (prescriptive procedures and review gates), `definition` (vocabulary), and `index` (navigation hubs). Globals are global because they can occur in any collection. `kb/types/text.md` documents the implicit no-frontmatter case and is not itself a selectable type.
- **Collection-local type-spec docs** live in `kb/<collection>/types/`. They apply only to artifacts in that collection. Examples: `adr` in `kb/reference/types/`, `structured-claim` in `kb/notes/types/`, `snapshot`, `ingest-report`, and `source-review` in `kb/sources/types/`, `connect-report` in `kb/reports/types/`.

Type resolution is lexical: the path stored in `type:` names the type-spec doc directly. The collection does not participate in explicit type resolution; collection scoping shows up only in `COLLECTION.md`'s `## Types` menu when an author is picking a type for a new write. See [type-loading](./type-loading.md) for the full mechanics.

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
2. The artifact's `type:` frontmatter names the path of its type-spec doc directly. The validator opens that doc, confirms it is itself a type spec (its own `type:` resolves to `kb/types/type-spec.md`), and loads the schema declared in the doc's `schema:` field — or skips schema validation when `schema:` is `null`. The schema defines what frontmatter is required and what body sections must exist; authoring prose and any template block live in the same doc.
3. The validator checks structural conformance (type contract). Review gates check semantic conformance (the `traits` axis).

When authoring a new artifact, the same two decisions happen in reverse: pick the collection (which register fits the intent?), then pick the type (what shape best carries the content?).

---

Relevant Notes:

- [available-types](./available-types.md) — extends: the catalog of shipped global and collection-scoped types
- [type-loading](./type-loading.md) — extends: the resolution mechanics for path-valued `type:` pointers and their type-spec docs
- [definitions/collection](./definitions/collection.md) — extends: the precise definition of "collection" with scope, exclusions, and misuse cases
- [ADR-012: types for structure, traits for review](./adr/012-types-for-structure-traits-for-review.md) — grounds: the decision to keep structural types and semantic-review traits on separate axes
- [ADR-017: COLLECTION.md is the register convention boundary](./adr/017-collection-md-is-the-register-convention-boundary.md) — grounds: the decision to host register conventions in `COLLECTION.md` rather than in type definitions
