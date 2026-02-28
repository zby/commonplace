---
description: Index of notes about document types, writing conventions, validation, and structural quality — how notes are classified, structured, and checked
type: index
status: current
---

# Document system

How documents are classified, structured, and quality-checked. These notes define the type system, writing conventions, and testing framework that make knowledge artifacts machine-verifiable and human-readable.

## Foundations

- [why-notes-have-types](./why-notes-have-types.md) — six roles of the type system: navigation hints, metadata enforcement, verifiable structure, local extensibility, output quality, and maturation through stabilisation
- [document-types-should-be-verifiable](./document-types-should-be-verifiable.md) — types assert verifiable structural properties, not subject matter; base type + traits model inspired by gradual and structural typing
- [document-classification](./document-classification.md) — taxonomy overview: base types table (text, note, spec, review, index, adr), migration from old flat types
- [note base type](../../types/note.md) — the base structured type: global fields (description, status, traits, areas), status ladder, traits system, design principles
- [text root type](../../types/text.md) — the empty root type: no frontmatter, always valid
- [human-llm-differences-are-load-bearing-for-knowledge-system-design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — knowledge systems produce dual-audience documents (human + LLM), making cognitive differences a first-class design concern for type and convention design

## Types

- [wikiwiki-principle-lowest-friction-capture-then-progressive-refinement](./wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) — Ward Cunningham's design principle animates the type ladder: capture with zero friction, refine in place, each step adds structure only when the thought has earned it
- [directory-scoped-types-are-cheaper-than-global-types](./directory-scoped-types-are-cheaper-than-global-types.md) — global types tax every session's context; directory-scoped types load only when working in that directory
- [why-directories-despite-their-costs](./why-directories-despite-their-costs.md) — directories buy one-two orders of magnitude of navigable scale but each new directory taxes routing, search config, and cross-directory linking

## Writing Conventions

- [title-as-claim-enables-traversal-as-reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — claim titles make link traversal read as reasoning chains; topical titles break this, and multi-claim documents get different title conventions
- [claim-notes-should-use-toulmin-derived-sections-for-structured-argument](./claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) — three independent threads converged on Toulmin's argument structure, leading to the `structured-claim` type with Evidence/Reasoning/Caveats sections

## Testing

- [automated-tests-for-text](./automated-tests-for-text.md) — text artifacts can be tested with the same pyramid as software: deterministic checks, LLM rubrics, corpus compatibility
- [text-testing-framework](./text-testing-framework.md) — reference framework: contracts per document type, test pyramid (deterministic/LLM rubric/corpus), production workflow
- [deterministic-validation-should-be-a-script](./deterministic-validation-should-be-a-script.md) — half of /validate's checks are hard-oracle (enums, link resolution, frontmatter structure) and could run as a Python script instead of burning LLM tokens

## Decisions

- [002-inline-global-types-in-writing-guide](./adr/002-inline-global-types-in-writing-guide.md) — inline note and structured-claim templates into WRITING.md, eliminating one hop for the two most common note types

## Related Areas

- [claw-design](./claw-design.md) — the document system is infrastructure for the claw; architecture decisions about files-not-database and context loading depend on document structure
- [links](./links.md) — [title-as-claim](./title-as-claim-enables-traversal-as-reasoning.md) bridges both areas: it's a writing convention that enables link semantics
- [learning-theory](./learning-theory.md) — the type ladder instantiates the stabilisation gradient for documents
