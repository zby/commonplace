---
description: Index of notes about document types, writing conventions, validation, and structural quality — how notes are classified, structured, and checked
type: index
status: current
---

# Document system

How documents are classified, structured, and quality-checked. These notes define the type system, writing conventions, and testing framework that make knowledge artifacts machine-verifiable and human-readable.

## Foundations

- [note base type](../../types/note.md) — the base structured type: global fields (description, status, traits, areas), status ladder, traits system, design principles
- [text root type](../../types/text.md) — the empty root type: no frontmatter, always valid
- [human-llm-differences-are-load-bearing-for-knowledge-system-design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — knowledge systems produce dual-audience documents (human + LLM), making cognitive differences a first-class design concern for type and convention design
- [why-directories-despite-their-costs](./why-directories-despite-their-costs.md) — directories buy one-two orders of magnitude of navigable scale but each new directory taxes routing, search config, and cross-directory linking

## Writing Conventions

- [title-as-claim-enables-traversal-as-reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — claim titles make link traversal read as reasoning chains; topical titles break this, and multi-claim documents get different title conventions

## Testing

- [automated-tests-for-text](./automated-tests-for-text.md) — text artifacts can be tested with the same pyramid as software: deterministic checks, LLM rubrics, corpus compatibility
- [text-testing-framework](./text-testing-framework.md) — reference framework: contracts per document type, test pyramid (deterministic/LLM rubric/corpus), production workflow
- [deterministic-validation-should-be-a-script](./deterministic-validation-should-be-a-script.md) — half of /validate's checks are hard-oracle (enums, link resolution, frontmatter structure) and could run as a Python script instead of burning LLM tokens
- [unit-testing-llm-instructions-requires-mocking-the-tool-boundary](./unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md) — skills are programs whose I/O boundary is tool calls; mocking that boundary enables instruction-level testing that complements text artifact testing

## Decisions

- [002-inline-global-types-in-writing-guide](./adr/002-inline-global-types-in-writing-guide.md) — inline note and structured-claim templates into WRITING.md, eliminating one hop for the two most common note types

## Related Tags

- [type-system](./type-system-index.md) — sub-area: why documents have types, their roles, and how structured writing improves quality
- [kb-design](./kb-design-index.md) — the document system is infrastructure for the KB; architecture decisions about files-not-database and context loading depend on document structure
- [links](./links-index.md) — [title-as-claim](./title-as-claim-enables-traversal-as-reasoning.md) bridges both areas: it's a writing convention that enables link semantics
- [learning-theory](./learning-theory-index.md) — the type ladder instantiates the constraining gradient for documents

## All notes <!-- generated -->

- [002-inline-global-types-in-writing-guide](./adr/002-inline-global-types-in-writing-guide.md) — Decision to inline note and structured-claim templates into WRITING.md so the agent gets type structure and writing conventions in a single hop — eliminates one read for the two most common note types
- [Automated tests for text](./automated-tests-for-text.md) — Text artifacts can be tested with the same pyramid as software — deterministic checks, LLM rubrics, corpus compatibility — built from real failures not taxonomy
- [Deterministic validation should be a script](./deterministic-validation-should-be-a-script.md) — Half of /validate's checks are hard-oracle (enums, link resolution, frontmatter structure) and could run as a Python script in milliseconds instead of burning LLM tokens via the skill
- [Human-LLM differences are load-bearing for knowledge system design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — Knowledge systems both inherit human-oriented materials and produce dual-audience documents (human + LLM), making human-LLM cognitive differences a first-class design concern rather than a generic disclaimer
- [Text testing framework — source material](./text-testing-framework.md) — Reference framework for automated text testing — contracts per document type, test pyramid (deterministic/LLM rubric/corpus), production workflow
- [Title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — When note titles are claims rather than topics, following links between them reads as a chain of reasoning — the file tree becomes a scan of arguments, and link semantics (since, because, but) encode relationship types
- [Unit testing LLM instructions requires mocking the tool boundary](./unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md) — Skills are programs whose I/O boundary is tool calls — mocking that boundary creates controlled environments for testing whether instructions produce correct behavior, complementing text artifact testing with instruction-level regression detection
- [Why directories despite their costs](./why-directories-despite-their-costs.md) — Directories buy one–two orders of magnitude of human-navigable scale over flat files, and enable local conventions per subsystem — but each new directory taxes routing, search config, skills, and cross-directory linking
