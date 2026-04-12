---
description: Index of notes about the document type system — why types exist, what roles they serve, how they improve output quality, and how they're structured
type: index
index_source: tag
index_key: types
tags: [document-system]
status: current
---

# Type system

Why documents have types, what the type system does, and how structured writing improves quality. Sub-area of [document-system](./document-system-index.md).

## Overview

A **type** in commonplace is a structural contract for a markdown file. It names what metadata the file must carry, what sections its body must contain, and how validators and agents should treat it. The `type:` field in frontmatter is the pointer; the type's template, instructions, and schema files in a `types/` directory are the contract.

The type system sits on a maturity ladder. At the bottom, [text](../types/text.md) has no frontmatter and no structure — it is raw capture and is always valid. One step up, every structured document extends [note](../types/note.md), which requires a non-empty `description` and carries shared metadata (`status`, `traits`, `tags`). Specialised types — `definition`, `adr`, `structured-claim`, `related-system`, and others — extend `note` with additional required sections and schema checks. Content starts as `text`, graduates to `note` once it earns frontmatter, and may graduate further once an argument or structure crystallises.

The `type:` field is a free-form string rather than a closed enum. Each collection (top-level `kb/` subdirectory) can define its own specialised types under a local `types/` directory, and the validator and write skills resolve a type name by looking in the owning collection first, then in the global `kb/types/`. This keeps the always-loaded global layer thin while letting new domains add types locally without global coordination.

Types serve six roles, each developed in [why-notes-have-types](./why-notes-have-types.md): they give agents structural hints before they open a document, force metadata to exist reliably, provide verifiable structural properties for validation, support local extensibility per collection, raise output quality by shaping what gets written, and let content mature by tightening constraints over time.

For the inventory of types shipped by the commonplace scaffold, see [available-types](../reference/available-types.md). For the resolution mechanism that loads a type's contract files at authoring or validation time, see [type-loading](../reference/type-loading.md).

## Type Roles

- [types-give-agents-structural-hints-before-opening-documents](./types-give-agents-structural-hints-before-opening-documents.md) — navigation: type + description let agents route without loading full documents
- [type-system-enforces-metadata-that-navigation-depends-on](./type-system-enforces-metadata-that-navigation-depends-on.md) — enforcement: descriptions exist because the note base type requires them; without enforcement, navigation degrades
- [document-types-should-be-verifiable](./document-types-should-be-verifiable.md) — verification: types assert structural properties, not subject matter; verification gradient from deterministic to corpus-level
- [directory-scoped-types-are-cheaper-than-global-types](./directory-scoped-types-are-cheaper-than-global-types.md) — extensibility: global types tax every session; local types load only when working in that directory
- [type-loading](../reference/type-loading.md) — loading mechanism: how authoring skills and validation resolve a note's type contract through collection-scoped lookup, with `note` inlined into WRITING.md as the exception

## Output Quality

Three independent arguments for why structured document types improve what gets written:

- [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](./human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) — failure-mode transfer: LLMs exhibit human-like failures, so structures that prevent those failures in humans prevent them in LLMs too
- [structure-activates-higher-quality-training-distributions](./structure-activates-higher-quality-training-distributions.md) — distribution selection: structured templates steer autoregressive generation toward scientific papers and formal arguments
- [structured-output-is-easier-for-humans-to-review](./structured-output-is-easier-for-humans-to-review.md) — reviewability: separated sections let readers check facts and logic independently

## Structure Dimensions

- [process-structure-and-output-structure-are-independent-levers](./process-structure-and-output-structure-are-independent-levers.md) — constraining what reasoning steps must occur (process structure) is independent from constraining result format (output structure); the KB's output quality arguments apply differently to each

## Type Definitions

- [claim-notes-should-use-toulmin-derived-sections-for-structured-argument](./claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) — the `structured-claim` type: Toulmin-derived Evidence/Reasoning/Caveats sections
- [wikiwiki-principle-lowest-friction-capture-then-progressive-refinement](./wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) — the type ladder: zero-friction capture, then progressive refinement as thoughts earn structure

## Related Tags

- [document-system](./document-system-index.md) — parent area; type system is one component of the document infrastructure
- [learning-theory](./learning-theory-index.md) — the type ladder instantiates the constraining gradient for documents

## Other tagged notes <!-- generated -->

