---
description: "How Commonplace composes collection and type contracts, names global types by bare name and collection-local types by path, and locates both kinds of type spec"
type: note
tags: []
---

# Collections and types

Every authored artifact in Commonplace is governed by two independent contracts:

- Its location selects a [**collection**](./definitions/collection.md). The nearest containing `COLLECTION.md` supplies that collection's [text contract](./definitions/collection.md#text-contract): purpose, quality goal, title and description conventions, lifecycle, and outbound-link rules.
- Its `type:` frontmatter points to a **type spec**. The type spec supplies the artifact's structural and semantic contract: frontmatter fields, required sections, schema, authoring guidance, and any template.

The collection answers what role the artifact serves in this part of the KB. The type answers what shape the artifact takes. A `note` in `kb/notes/` is theoretical, while a `note` in `kb/reference/` describes the shipped system; both use the same structural type contract. A collection does not redefine the meaning of a type's fields.

## How an artifact uses a type

A typed artifact names its type spec in `type:`. A global type is named by its bare name:

```yaml
---
description: Why this artifact is useful to a reader
type: note
tags: []
---
```

A bare name such as `note` resolves to `types/note.md` under the Commonplace library root: in an installed project that is the installed package's library, and in the source repository it is `kb/types/note.md`. The global types are a small set that the package owns, so the same pointer works in every project. If the library is not installed, validation reports that the Commonplace library is not available rather than a broken type.

A collection-local type is named by its path, repository-relative (`kb/...`) or file-relative (`./...` or `../...`). The path must end in `.md`, resolve beneath `kb/`, and identify a type-spec document. For example, an ADR under `kb/reference/adr/` can carry:

```yaml
type: ../types/adr.md
```

The form alone tells the resolver which kind of type it has; there is no fallback between them. A path that lands on a global type fails validation with the bare name to use instead, so a global type has exactly one spelling. Absolute paths, URLs, repository-relative paths containing `..`, missing files, and `text` as an explicit type also fail.

The pointer is the type's identity: a global type's bare name, or a local type's normalized `kb/...` path. Two type specs with the same `name:` at different paths are different contracts, and a local type never shadows a global one.

For an existing artifact, an agent follows `type:` and opens that document; no catalogue lookup is needed. For a new artifact, a user or workflow may supply the exact type pointer. A shorthand name is resolved by inspecting type-spec frontmatter among the global types and under the collection `types/` directories and requiring one exact `name:` match; a global match is written as its bare name and a local match as its path. Duplicate names remain ambiguous until a pointer is supplied. A general write with no supplied type defaults to `note`. A workflow that requires another type supplies its exact pointer. Implicit `text` is an explicit choice to write frontmatter-free Markdown, not a fallback from failed type lookup.

Lookup identifies the contract but does not authorize it for a collection. For an artifact inside a declared collection, validation permits global types and local specs under that collection's own `types/` directory. A peer collection's local type fails. The entire `kb/work/` subtree is the lifecycle exception: a workshop may reference any valid type spec so that it can stage work for any target collection or test the real contract. Files outside declared collections retain referential validation only.

## What a type spec contains

A type spec is itself a typed Markdown document. Its frontmatter has this shape:

```yaml
---
type: type-spec
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
- **Collection-local type specs** live in the owning collection's `types/` directory, such as [`kb/reference/types/`](./types/adr.md), [`kb/notes/types/`](../notes/types/structured-claim.md), [`kb/sources/types/`](../sources/types/snapshot.md), and [`kb/reports/types/`](../reports/types/connect-report.md).

Open those directories—or follow an artifact's `type:` pointer—to see the current definitions. From an installed project, `.commonplace/library.md` gives the path of the library's `types/` directory. A prose list elsewhere is only a snapshot and is not the authority for what exists.

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
| [`connect-report`](../reports/types/connect-report.md) | `kb/reports/` | Discovery-only connection output under the reports collection's retention policy. |

Each linked type spec, not this table, defines the type.

## Authoring composition

The ordinary writing path composes three files at read time:

1. the writing skill for the general procedure;
2. the target collection's `COLLECTION.md` for its text and link contract;
3. the selected type spec for artifact shape and type-specific guidance.

There is no generated write-context packet or resolver command. After writing, validation is authoritative for deterministic conformance.

No third file joins this composition. A subdirectory inside a collection carries no binding rules, and a README there is navigation only. A rule that binds one kind of artifact goes in that kind's type spec — collection-local when the kind exists in one collection — and a rule about what may live where goes in `COLLECTION.md`. Lifecycle operations are instructions in `kb/instructions/`, named from the type spec ([ADR 084](./adr/084-kind-rules-live-in-type-specs-and-operations-in-instructions.md)).

---

Relevant documentation:

- [Collection and text contract](./definitions/collection.md) — defined-in: the precise collection boundary and the binding local declaration in `COLLECTION.md`
- [Validation contract](./validation-contract.md) — part-of: deterministic base rules, type-owned schemas, and semantic conformance review
- [Collections never own frontmatter semantics](./collections-never-own-frontmatter-semantics.md) — extends: why a type owns its fields while a collection owns text-level conventions
- [Architecture](./architecture.md) — part-of: where global and installed collection-local types sit in the shipped layout
- [Type system](../notes/type-system-README.md) — see-also: theory explaining why document types exist and what they enable
- [ADR 018](./adr/018-types-are-path-references-to-instruction-docs.md) — evidenced-by: the decision establishing path-valued type identity, which bare global names partly reverse
