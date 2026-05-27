---
description: How collections and types compose in commonplace - collections own register conventions and per-destination outbound linking rules, types own structural contracts declared in type-spec docs, and the two meet through path-valued type pointers listed in COLLECTION.md; covers the COLLECTION.md surface and the live per-destination model the write and connect skills consume
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

A **collection** is a subtree under `kb/` whose root contains `COLLECTION.md`. That file is the local authoring and routing contract for artifacts in the subtree: purpose, register or mode, quality goal, placement boundaries, title and description conventions, type guidance, outbound-link policy, labels, search guidance, and lifecycle rules. Subdirectories inside a collection are normally *areas* under the same contract. A `COLLECTION.md` inside a non-collection namespace, such as installed `kb/commonplace/notes/`, is an ordinary collection; a `COLLECTION.md` inside another collection is invalid.

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

`kb/types/` sits at the top level under `kb/` but is not a collection in this sense — it is the global type layer. Namespace directories such as installed `kb/commonplace/` are likewise not collections unless they carry their own `COLLECTION.md`; their descendant `COLLECTION.md`-bearing directories are the collections. Some collections, such as `kb/instructions/`, are framework-shipped rather than primarily practitioner-authored, but they still carry authored artifacts and local authoring/routing contracts. See the [collection definition](./definitions/collection.md) for the full boundary.

## Types

A **type** is a structural contract expressed as a hand-authored **type-spec doc**: a markdown file carrying type-spec frontmatter (`type: kb/types/type-spec.md`, `name`, `description`, `schema`) plus authoring prose and an optional template block. Every artifact with frontmatter has exactly one type, declared as the path to its type-spec doc in the `type:` field — for example `type: ../types/adr.md` or `type: kb/reference/types/adr.md`. Consuming projects add types by dropping a new type-spec doc (and, when structural validation is desired, a sibling `.schema.yaml`) into the appropriate `types/` directory and listing it in the owning collection's `COLLECTION.md`.

Two scopes:

- **Global type-spec docs** live in `kb/types/`. The shipped globals are `type-spec` (the self-referential root), `note` (the base structured type), `instruction` (prescriptive procedures, skill bodies, wrapper prompts, work packets), `review-gate` (one quality check for the review system), `definition` (vocabulary), and `index` (navigation hubs). Globals are global because they can occur in any collection. `kb/types/text.md` documents the implicit no-frontmatter case and is not itself a selectable type.
- **Collection-local type-spec docs** live in `kb/<collection>/types/`. They apply only to artifacts in that collection. Examples: `adr` in `kb/reference/types/`, `structured-claim` in `kb/notes/types/`, `snapshot`, `ingest-report`, and `source-review` in `kb/sources/types/`, `connect-report` in `kb/reports/types/`.

Type resolution is lexical: the path stored in `type:` names the type-spec doc directly. The collection does not participate in explicit type resolution; collection scoping shows up only in `COLLECTION.md`'s `## Types` menu when an author is picking a type for a new write. See [type-loading](./type-loading.md) for the full mechanics.

Types describe structure, not semantics. Semantic review expectations live on a separate axis — the `traits` field on `note`-derived types — per [ADR-012](./adr/012-types-for-structure-traits-for-review.md).

## Cross-collection linking

The collection determines the *register* of an artifact, and links between registers carry different meaning than links inside one. A theoretical note linking to a descriptive note is citing evidence; a descriptive note linking to a theoretical note is citing rationale.

Each `COLLECTION.md`'s "Outbound linking conventions" section is **the single authoritative source** for that collection's outbound rules. The section is organised **per destination collection** — one block per destination the source may link to. Each destination block declares two things:

- **Search guidance** — when to prospect this destination from the current source. Used by the connect skill to decide breadth and by writers manually choosing where to look for link candidates.
- **Authorised labels** — labels the writer may use for links to this destination, each with a one-line reader-need context specific to the *source → destination* pairing. Per-destination authorisation lets `kb/notes/ → kb/reference/` differ from `kb/notes/ → kb/agent-memory-systems/` even though both targets share the descriptive register.

Two skills consume this directly:

- **[cp-skill-write](../instructions/cp-skill-write/SKILL.md)** reads the source `COLLECTION.md`, treats its outbound section as the authoritative label and reader-need reference, and prospects per destination using cheap surfaces (dir-index, already-loaded context, user-named targets).
- **[cp-skill-connect](../instructions/cp-skill-connect/SKILL.md)** reads the source `COLLECTION.md`, enumerates destination blocks, runs the full prospecting procedure on each (search guidance, dir-index, tag indexes, body search, link-following), and labels candidates from the destination's authorised set. Candidates that pass the articulation test but fall outside any authorised label go in a dedicated "Off-authorisation candidates" report section as a signal for the collection author.

There is no compiled topology and no separate vocabulary document for the skills to read; live `COLLECTION.md` reads remove the drift risk a compile step would introduce. A separate authoring resource at [`link-vocabulary.md`](./link-vocabulary.md) catalogues labels and authoring guidance for `COLLECTION.md` authors revising the outbound rules; note writers and the connect skill do not read it.

The architecture and the per-destination structure are pinned by [ADR-019](./adr/019-collection-owned-link-vocabulary.md) (which extends ADR 017's COLLECTION.md boundary) and [ADR-020](./adr/020-theoretical-default-contrasts-mechanism.md) (which extends ADR 009's vocabulary).

## How an artifact comes together

For an existing artifact, the two axes resolve like this:

1. The artifact's path identifies its collection. The collection's `COLLECTION.md` defines the writing conventions that apply, and its per-destination outbound linking section defines what relationship labels to use when linking outward.
2. The artifact's `type:` frontmatter names the path of its type-spec doc directly. The validator opens that doc, confirms it is itself a type spec (its own `type:` resolves to `kb/types/type-spec.md`), and loads the schema declared in the doc's `schema:` field — or skips schema validation when `schema:` is `null`. The schema defines what frontmatter is required and what body sections must exist; authoring prose and any template block live in the same doc.
3. The validator checks structural conformance (type contract). Review gates check semantic conformance (the `traits` axis).

When authoring a new artifact, the same two decisions happen in reverse: pick the collection (which register fits the intent?), then pick the type (what shape best carries the content?).

---

Relevant Notes:

- [available-types](./available-types.md) — part-of: the catalog of shipped global and collection-scoped types
- [type-loading](./type-loading.md) — part-of: the resolution mechanics for path-valued `type:` pointers and their type-spec docs
- [definitions/collection](./definitions/collection.md) — defined-in: the precise definition of "collection" with scope, exclusions, and misuse cases
- [link-vocabulary](./link-vocabulary.md) — part-of: the label catalogue and authoring guidance COLLECTION.md authors consult when writing outbound rules
- [ADR-012: types for structure, traits for review](./adr/012-types-for-structure-traits-for-review.md) — rationale: the decision to keep structural types and semantic-review traits on separate axes
- [ADR-017: COLLECTION.md is the register convention boundary](./adr/017-collection-md-is-the-register-convention-boundary.md) — rationale: the decision to host register conventions in `COLLECTION.md` rather than in type definitions
- [ADR-019: collection-owned link vocabulary](./adr/019-collection-owned-link-vocabulary.md) — rationale: the decision pinning the per-destination outbound structure inside COLLECTION.md and retiring the compiled topology
