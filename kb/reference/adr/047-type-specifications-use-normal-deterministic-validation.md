---
description: Type-spec documents run through ordinary note validation, with a type-owned referential rule resolving their declared schemas; the former workspace sweep is removed
type: ../types/adr.md
tags: []
status: accepted
---

# 047-Type specifications use normal deterministic validation

**Status:** accepted
**Date:** 2026-07-13

## Context

[ADR 018](./018-types-are-path-references-to-instruction-docs.md) made each type definition a Markdown note whose own `type:` is `kb/types/type-spec.md`. The deterministic validator nevertheless excluded `types/` directories from collection targets and compensated with `validate_type_specs`, a workspace-wide batch pass.

That pass did not validate a candidate as a type-spec note. It parsed each file and resolved the artifact type named by its `type:` field; for a normal candidate, this repeatedly resolved the root `type-spec` definition. It did not apply `type-spec.schema.yaml` to the candidate or resolve the candidate's own `schema:` declaration. Used types received stronger incidental checking when an instance resolved them, while unused types could remain malformed.

The split contradicted the type system's own representation. A type specification already has an ordinary schema for its intra-document shape. Its one additional requirement — a non-null `schema:` path must resolve to a loadable schema — is a type-owned referential check of the same kind as other imperative type rules.

## Decision

Type-spec documents use the normal deterministic validation pipeline.

- Collection validation includes every visible `.md` artifact under the collection's `types/` directories. The retired `.template.md` and `.instructions.md` suffixes carry no validation semantics. `text.md` remains absent only from the dedicated `types` target because its lack of frontmatter defines the implicit root rather than a type-spec artifact.
- The `type-spec` type registers an imperative rule that resolves the validated document itself as a type definition. This checks its `name`, `description`, and `schema` declaration and loads the declared schema when non-null. `type-spec.schema.yaml` remains responsible for intra-document structure; the imperative rule owns dereferencing.
- `validate_type_specs` and its special batch-report section are removed.
- `commonplace-validate types` validates the complete global and collection-local type-spec inventory through the same per-artifact result pipeline. Validating a collection also validates its local type specs.
- The authored-link orphan signal remains a content-note check. Type use is expressed by frontmatter rather than a narrated Markdown edge, so lack of an inbound prose link is not evidence that a type spec is unused.

This amends [ADR 039](./039-tool-visibility-is-package-owned-and-git-is-never-invoked.md): `types/` is not categorically invisible collection content. Individual consumers may still omit type definitions when their domain excludes contracts — generated content indexes and review target selection do — but validation does not.

## Consequences

Easier:

- Type definitions receive base checks, `type-spec` schema checks, and referential schema resolution through one familiar result format.
- An unused type with a missing or malformed declared schema fails `commonplace-validate types` instead of waiting for an instance to reference it.
- The validator loses one batch-only algorithm and one misleading summary pass.
- Collection-local contracts are checked alongside the artifacts whose collection exposes them.

Harder:

- Collection validation reports type-spec blocks in addition to content-note blocks.
- Consumers of the shared collection enumerator that do not want type definitions must state that exclusion themselves instead of inheriting it accidentally from validation's old target list.

Risks:

- A future support document placed under `types/` enters collection validation. It must therefore be a valid artifact; filename suffixes do not create a hidden second classification system alongside frontmatter `type:`.

## Links

- [Validation contract](../validation-contract.md) — implemented-by: the normal schema/type-rule split applied to type-spec documents
- [ADR 050 — Validation runs share parsed artifacts and collection indexes](./050-validation-runs-share-parsed-artifacts-and-collection-indexes.md) — part-of: type-spec validation runs through the same artifact-anchored execution surface
