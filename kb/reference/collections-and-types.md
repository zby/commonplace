---
description: "How Commonplace composes collection and type contracts, uses path-valued type pointers, and locates global and collection-local type specs"
type: kb/types/note.md
tags: []
---

# Collections and types

Every authored artifact in Commonplace is governed by two independent contracts:

- Its location selects a **collection**. The nearest containing `COLLECTION.md` supplies the text contract: purpose, quality goal, title and description conventions, lifecycle, and outbound-link rules.
- Its `type:` frontmatter points to a **type spec**. The type spec supplies the artifact's structural and semantic contract: frontmatter fields, required sections, schema, authoring guidance, and any template.

The collection answers what role the artifact serves in this part of the KB. The type answers what shape the artifact takes. A `note` in `kb/notes/` is theoretical, while a `note` in `kb/reference/` describes the shipped system; both use the same structural type contract. A collection does not redefine the meaning of a type's fields.

## How an artifact uses a type

A typed artifact stores the path to its type spec directly:

```yaml
---
description: Why this artifact is useful to a reader
type: kb/types/note.md
tags: []
---
```

The pointer may be repository-relative (`kb/...`) or file-relative (`./...` or `../...`). It must end in `.md`, resolve beneath `kb/`, and identify a type-spec document. Absolute paths, URLs, repository-relative paths containing `..`, missing files, and `kb/types/text.md` as an explicit type all fail validation.

File-relative pointers keep collection-local types stable when shipped content moves under an installed namespace. For example, an ADR under `kb/reference/adr/` can carry:

```yaml
type: ../types/adr.md
```

The path is the type's identity. Two type specs with the same `name:` at different paths are different contracts.

For an existing artifact, an agent follows `type:` and opens that document; no catalogue lookup is needed. When writing a new artifact, the agent first selects the collection, then selects and opens a type spec appropriate to that collection before drafting.

The current writing skills use each collection's `## Types` section as the shorthand selection menu for new writes. Explicit type resolution does not use that menu: the validator follows the stored path directly. It currently checks that the pointer and target are valid, loads the type's schema, and validates the artifact, but does not enforce that a collection-local type belongs to the artifact's collection.

## What a type spec contains

A type spec is itself a typed Markdown document. Its frontmatter has this shape:

```yaml
---
type: kb/types/type-spec.md
name: adr
description: Architecture decision record for accepted or proposed system decisions
schema: ./adr.schema.yaml
---
```

The body contains the natural-language authoring contract and may include a template. `schema:` points to a JSON Schema sidecar expressed as YAML; `schema: null` means that the type has no structural schema. [`kb/types/type-spec.md`](../types/type-spec.md) is the self-referential root contract.

The type contract is consumed in two ways:

1. `commonplace-validate` checks the artifact against the resolved schema and the framework's deterministic base rules.
2. Type-conformance review uses the type spec's body as the semantic criterion, covering requirements that a schema cannot decide.

The collection contract is reviewed separately against the artifact's containing `COLLECTION.md`. This keeps structural type semantics independent from collection-specific writing and routing conventions.

## Where type specs live

The filesystem is the live inventory. There are two normal locations:

- **Global type specs** live in [`kb/types/`](../types/README.md). They are intended for reuse across collections.
- **Collection-local type specs** live in the owning collection's `types/` directory, such as [`kb/reference/types/`](./types/adr.md), [`kb/notes/types/`](../notes/types/structured-claim.md), and [`kb/sources/types/`](../sources/types/snapshot.md).

Open those directories—or follow an artifact's `type:` pointer—to see the current definitions. A prose list elsewhere is only a snapshot and is not the authority for what exists.

## Common examples

These examples illustrate the model; they are not an exhaustive catalogue.

| Type | Scope | Typical use |
|---|---|---|
| [`text`](../types/text.md) | implicit | A Markdown file with no frontmatter; capture without a selectable `type:` value. |
| [`note`](../types/note.md) | global | The base structured knowledge artifact. |
| [`instruction`](../types/instruction.md) | global | Procedures, skills, prompts, and work packets. |
| [`definition`](../types/definition.md) | global | Operational vocabulary definitions. |
| [`adr`](./types/adr.md) | `kb/reference/` | Architecture decisions about the shipped system. |
| [`structured-claim`](../notes/types/structured-claim.md) | `kb/notes/` | Developed arguments whose shape fits its Evidence and Reasoning contract. |
| [`snapshot`](../sources/types/snapshot.md) | `kb/sources/.snapshots/` | Local faithful captures of external source material. |

Each linked type spec, not this table, defines the type.

## Authoring composition

The ordinary writing path composes three files at read time:

1. the writing skill for the general procedure;
2. the target collection's `COLLECTION.md` for its text and link contract;
3. the selected type spec for artifact shape and type-specific guidance.

There is no generated write-context packet or resolver command. After writing, validation is authoritative for deterministic conformance.

---

Relevant documentation:

- [Collection](./definitions/collection.md) — defined-in: the precise collection boundary and the role of `COLLECTION.md`
- [Validation contract](./validation-contract.md) — part-of: deterministic base rules, type-owned schemas, and semantic conformance review
- [Collections never own frontmatter semantics](./collections-never-own-frontmatter-semantics.md) — extends: why a type owns its fields while a collection owns text-level conventions
- [Architecture](./architecture.md) — part-of: where global and installed collection-local types sit in the shipped layout
- [Type system](../notes/type-system-README.md) — see-also: theory explaining why document types exist and what they enable
- [ADR 018](./adr/018-types-are-path-references-to-instruction-docs.md) — evidenced-by: the decision establishing path-valued type identity
