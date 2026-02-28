---
description: Text artifacts can be tested with the same pyramid as software — deterministic checks, LLM rubrics, corpus compatibility — built from real failures not taxonomy
type: note
traits: []
areas: [document-system]
status: current
---

# Automated tests for text

Text artifacts can be tested like software if you define contracts per document type. The same test pyramid applies: cheap deterministic checks at the base, LLM-based rubric grading in the middle, cross-document corpus checks at the top.

Since [document types should be verifiable](../document-types-should-be-verifiable.md), each type and trait asserts a checkable structural property — and those properties are exactly what testing contracts should verify. A `spec` needs Design/Implementation sections; `structured-claim` needs Evidence and Reasoning sections. The type system and the test pyramid are two sides of the same coin: types define what to check, tests do the checking.

Key principle: build contracts from real failures, not from a taxonomy of possible checks. Same way you build a test suite — add a test when something breaks, not before.

Levels we might use:
- **Deterministic** — required sections, description present, link validity, no dangling wiki-links, length
- **LLM rubric** — clarity, single clear thesis, claims sourced or marked as assumptions
- **Corpus compatibility** — contradiction check against existing notes, terminology alignment, duplicate detection

A knowledge base is a collection of stored LLM outputs — each note is a stabilized sample from a distribution. So note testing is an application of the broader [artifact testing problem](../../notes/storing-llm-outputs-is-stabilization.md). The distinction between testing the prompt (will it produce good notes?) and testing the artifact (is *this* note good?) matters here: the pyramid above is all artifact testing. This doubled testing surface is a direct consequence of [applying programming testing practices to probabilistic systems](../../notes/programming-practices-apply-to-prompting.md) — deterministic code has no gap between instructions and output, so only output testing exists.

We haven't built any of this yet. Start when we hit a concrete quality problem that a check would have caught.

Topics:
- [document-system](./document-system.md)
