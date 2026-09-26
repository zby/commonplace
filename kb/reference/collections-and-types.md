---
description: "How Commonplace composes collection and type contracts, names every type by its spec's path under a KB root, and finds the spec on the library-and-KB search path"
type: types/note.md
tags: []
---

# Collections and types

Every authored artifact in Commonplace is governed by two independent contracts:

- Its location selects a [**collection**](./definitions/collection.md). The nearest containing `COLLECTION.md` supplies that collection's [text contract](./definitions/collection.md#text-contract): purpose, quality goal, title and description conventions, lifecycle, and outbound-link rules.
- Its `type:` frontmatter points to a **type spec**. The type spec supplies the artifact's structural and semantic contract: frontmatter fields, required sections, schema, authoring guidance, and any template.

The collection answers what role the artifact serves in this part of the KB. The type answers what shape the artifact takes. A `note` in `kb/notes/` is theoretical, while a `note` in `kb/reference/` describes the shipped system; both use the same structural type contract. A collection does not redefine the meaning of a type's fields.

## How an artifact uses a type

A typed artifact names its type spec in `type:`. The value is the spec's path under a KB root, with its `.md` extension. A global type is named by its path under the library root:

```yaml
---
description: Why this artifact is useful to a reader
type: types/note.md
tags: []
---
```

A collection-local type is named by its path under the KB root, starting with its collection. For example, an ADR under `kb/reference/adr/` carries:

```yaml
type: reference/types/adr.md
```

A value resolves on a search path of two roots:

1. the Commonplace library root, for global types only: a value resolves there only when it names `types/<name>.md`;
2. the root of the KB that holds the artifact: the project's `kb/` for a project artifact, and the library root for a library file.

In an installed project, `types/note.md` names a file in the installed package's library, whose path `.commonplace/library.md` gives. In the source repository and for every library file, both roots are the same directory, so the value is the path to open under `kb/`, such as `kb/types/note.md`. The library's collection-local types are not on a project's search path. If the library is not installed, validation reports that the Commonplace library is not available rather than a broken type.

A value that resolves under both roots to two different files is an error: validation fails and names both files. No root takes precedence, so a project file never silently overrides a library type. A leftover copy of a library type in a project's `kb/types/` collides this way; delete it or move its change into the project's own collections. A project's `kb/types/` has no special standing, and types a whole project needs are global library types.

A type has one spelling everywhere, so an artifact can move within its collection without changing its type. Values starting with `./`, `../`, or `kb/`, bare names such as `note`, absolute paths, URLs, missing files, and `text` as an explicit type fail validation. The same form applies wherever a type is named: `type:` in frontmatter, gates' `requires_type:`, and type specs' own `type:`.

The written value is the type's identity, such as `types/note.md` or `reference/types/adr.md`. Two type specs with the same `name:` at different paths are different contracts.

For an existing artifact, an agent follows `type:` and opens that document; no catalogue lookup is needed. For a new artifact, a user or workflow may supply the exact type value. A shorthand name is resolved by inspecting type-spec frontmatter among the global types and under the collection `types/` directories and requiring one exact `name:` match; the match is written as its path under its root. Duplicate names remain ambiguous until a value is supplied. A general write with no supplied type defaults to `types/note.md`. A workflow that requires another type supplies its exact value. Implicit `text` is an explicit choice to write frontmatter-free Markdown, not a fallback from failed type lookup.

Lookup identifies the contract but does not authorize it for a collection. For an artifact inside a declared collection, validation permits global types and local specs under that collection's own `types/` directory. A peer collection's local type fails. The entire `kb/work/` subtree is the lifecycle exception: a workshop may reference any valid type spec so that it can stage work for any target collection or test the real contract. Files outside declared collections retain referential validation only.

## What a type spec contains

A type spec is itself a typed Markdown document. Its frontmatter has this shape:

```yaml
---
type: types/type-spec.md
name: adr
description: Architecture decision record for accepted or proposed system decisions
schema: ./adr.schema.yaml
---
```

The body contains the natural-language authoring contract and may include a template. `schema:` points to a JSON Schema sidecar expressed as YAML; `schema: null` means that the type has no structural schema. [`type-spec`](../types/type-spec.md) is the self-referential root contract.

A local schema that builds on a global schema refers to it as `commonplace:types/<name>.schema.yaml`, for example `$ref: "commonplace:types/note.schema.yaml"`. The validator resolves that reference in the library, so a local schema inherits exactly what it names, wherever the library is installed.

The type contract is consumed in two ways:

1. `commonplace-validate` checks the artifact against the resolved schema and the framework's deterministic base rules.
2. Type-conformance review uses the type spec's body as the semantic criterion, covering requirements that a schema cannot decide.

The collection contract is reviewed separately against the artifact's containing `COLLECTION.md`. This keeps structural type semantics independent from collection-specific writing and routing conventions.

## Where type specs live

The filesystem is the live inventory. There are two normal locations:

- **Global type specs** live in the library's `types/` directory, authored in this repository as [`kb/types/`](../types/README.md). They are intended for reuse across collections, and a project does not hold copies of them.
- **Collection-local type specs** live in the owning collection's `types/` directory, such as [`kb/reference/types/`](./types/adr.md) and [`kb/notes/types/`](../notes/types/structured-claim.md).

Open those directories—or follow an artifact's `type:` value—to see the current definitions. From an installed project, `.commonplace/library.md` gives the path of the library's `types/` directory. A prose list elsewhere is only a snapshot and is not the authority for what exists.

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
| [`snapshot`](../types/snapshot.md) | global | Local faithful captures of external source material, kept under `kb/sources/.snapshots/`. |
| [`connect-report`](../types/connect-report.md) | global | Discovery-only connection output, written under the reports collection's retention policy. |

Each linked type spec, not this table, defines the type.

## Authoring composition

The ordinary writing path composes three files at read time:

1. the writing skill for the general procedure;
2. the target collection's `COLLECTION.md` for its text and link contract;
3. the selected type spec for artifact shape and type-specific guidance.

There is no generated write-context packet or resolver command. After writing, validation is authoritative for deterministic conformance.

A document may add one artifact-specific input: an optional [write brief](../types/write-brief.md). The brief is the document's preface for writers and part of it. It is kept in the sibling `<stem>.brief.md`, which the document declares with `brief: <stem>.brief.md`, for two reasons: it stays outside the text a write edits, so a drifting edit cannot rewrite it, and it stays out of the reader's view. The writing skill reads it as retained intent for that document only. It binds as intent until a user amends it, and current user direction prevails ([ADR 092](./adr/092-write-briefs-are-optional-sidecars-named-by-a-validated-pointer.md)).

No other file joins this composition. A subdirectory inside a collection carries no binding rules, and a README there is navigation only. A rule that binds one kind of artifact goes in that kind's type spec — collection-local when the kind exists in one collection — and a rule about what may live where goes in `COLLECTION.md`. Lifecycle operations are instructions in `kb/instructions/`, named from the type spec ([ADR 084](./adr/084-kind-rules-live-in-type-specs-and-operations-in-instructions.md)).

---

Relevant documentation:

- [Collection and text contract](./definitions/collection.md) — defined-in: the precise collection boundary and the binding local declaration in `COLLECTION.md`
- [Validation contract](./validation-contract.md) — part-of: deterministic base rules, type-owned schemas, and semantic conformance review
- [Collections never own frontmatter semantics](./collections-never-own-frontmatter-semantics.md) — extends: why a type owns its fields while a collection owns text-level conventions
- [Architecture](./architecture.md) — part-of: where global and installed collection-local types sit in the shipped layout
- [Type system](../tags/type-system-README.md) — see-also: theory explaining why document types exist and what they enable
- [ADR 018](./adr/018-types-are-path-references-to-instruction-docs.md) — evidenced-by: the decision establishing path-valued type identity, restored for every type by the two-root search path
