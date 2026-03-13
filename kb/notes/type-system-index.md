---
description: Index of notes about the document type system — why types exist, what roles they serve, how they improve output quality, and how they're structured
type: index
tags: [document-system]
status: current
---

# Type system

Why documents have types, what the type system does, and how structured writing improves quality. Sub-area of [document-system](./document-system-index.md).

## Overview

- [why-notes-have-types](./why-notes-have-types.md) — six roles of the type system: navigation hints, metadata enforcement, verifiable structure, local extensibility, output quality, and maturation through constraining
- [document-classification](./document-classification.md) — taxonomy: base types table (text, note, spec, review, index, adr) and migration history

## Type Roles

- [types-give-agents-structural-hints-before-opening-documents](./types-give-agents-structural-hints-before-opening-documents.md) — navigation: type + description let agents route without loading full documents
- [type-system-enforces-metadata-that-navigation-depends-on](./type-system-enforces-metadata-that-navigation-depends-on.md) — enforcement: descriptions exist because the note base type requires them; without enforcement, navigation degrades
- [document-types-should-be-verifiable](./document-types-should-be-verifiable.md) — verification: types assert structural properties, not subject matter; verification gradient from deterministic to corpus-level
- [directory-scoped-types-are-cheaper-than-global-types](./directory-scoped-types-are-cheaper-than-global-types.md) — extensibility: global types tax every session; local types load only when working in that directory

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
