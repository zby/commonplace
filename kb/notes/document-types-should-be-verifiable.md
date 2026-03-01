---
description: Document types should assert verifiable structural properties, not subject matter — with a base type + traits model inspired by gradual and structural typing
type: note
traits: []
areas: [document-system]
status: current
---

# Document types should be verifiable

## What "verifiable" means

A document type should assert a structural property you can check. "This is a spec" is verifiable — you can look for Motivation, Design, Implementation sections. "This is a design note" is not — any note in a design KB is about design; the label adds no checkable information.

The test: after reading the type, can you say something concrete about the document's structure without opening it? If not, the type is subject matter, not structure — and subject matter belongs in the `areas` field.

## Why verifiable: unenforceable types are useless

In programming, types are useful because the compiler enforces them. If nothing checked that a `List` is actually a list, the type annotation would be decoration. The value of a type comes from enforcement — something in the system acts on it.

Here, the "compiler" is a mix of agents and scripts. An agent reading `type: spec` can decide to implement from it. A script can grep for `type: structured-claim` to find citable arguments with full Evidence/Reasoning sections. But they can only do this if the type asserts something checkable. `type: design` gives them nothing to act on — every note in a design KB is "about design." An unverifiable type is like an unenforced type annotation: technically present, practically invisible. The [text testing pyramid](./observations/automated-tests-for-text.md) sketches what enforcement could look like in practice: deterministic checks for structural contracts, LLM rubrics for judgment-dependent traits.

Types guide what the processor — an [LLM interpreting fuzzy specifications](./agentic-systems-interpret-fuzzy-specifications.md) — can do with the document. A `spec` tells an agent it can build against this. A `has-comparison` tells it there are alternatives to choose between. Since [agents navigate by deciding what to read next](./observations/agents-navigate-by-deciding-what-to-read-next.md), types and traits are precisely the hints that make those decisions informed rather than blind — the type tells the agent what it can do with the document *before opening it*. The type is only useful if the processor can trust it, and trust requires the ability to check.

## But our processor is stochastic

In conventional programming, types are crisp because the processor is deterministic. A compiler can verify that a value satisfies a type with certainty.

Our processor is an [LLM that interprets fuzzy specifications](./agentic-systems-interpret-fuzzy-specifications.md). This has a direct consequence: type *assignment* is also fuzzy. An agent classifying a document resolves the ambiguity inherent in the type definitions — the same document might be classified differently by different agents, or even the same agent on different runs. The fuzziness isn't a bug in the type system. It's a consequence of the specifications (both the document and the type definitions) being in natural language, which doesn't have precise denotations.

This means we need types that are useful despite fuzziness — types that assert structural properties you can check, even if the checking requires judgment rather than proof. Type assignment is itself a case of [storing an LLM output as stabilization](../notes/storing-llm-outputs-is-stabilization.md) — choosing to label a document `type: spec` collapses a distribution of possible classifications to a single point.

## What went wrong with flat types

The original type system used a flat enum: `design`, `analysis`, `insight`, `research`, `comparison`, `spec`, `review`, `index`.

**"design" says nothing structural.** A design note could be a spec, an exploration, a brainstorm, or a comparison. It describes subject matter (this is about design), which is what the `areas` field is for. As a type it dominated the KB — half the notes were "design" — which means it did no discriminatory work. An agent reading `type: design` learns nothing about what it can do with the document.

**Flat types force false choices.** Is a research note that reaches a crystallized conclusion an insight or research? Is an analysis that cites external sources research or analysis? A flat enum forces a single choice and loses information. In object-oriented terms, this is like having `class ResearchInsight` but being forced to inherit from only one of `Research` or `Insight`.

## Base types + traits

The solution borrows from subtyping and structural typing. Instead of a flat enum, use a **base type** (hard structural category) plus **traits** (independently checkable properties):

```yaml
type: note
traits: [has-comparison, has-external-sources]
```

**Base types** are structurally distinct with low ambiguity — like choosing between `List`, `Dict`, and `Set`:

| Base type | What it tells the agent |
|-----------|------------------------|
| `note` | Default — read it to find out what you can do with it |
| `spec` | You can implement from this; it has enough detail to build against |
| `review` | This examines specific code; expect findings and a date |
| `index` | This is a navigation hub; follow its links to find related notes |

**Traits** are independently checkable properties — like interfaces or protocols that a value can satisfy in any combination:

| Trait | What it tells the agent |
|-------|------------------------|
| `has-comparison` | You can use this to decide between alternatives |
| `has-external-sources` | This connects to material outside the project |
| `has-implementation` | This contains code sketches or concrete API proposals |

A note can satisfy multiple traits without conflict. What the old system called "research" becomes `note` + `has-external-sources`. What it called "insight" becomes `structured-claim` (if the argument is developed) or stays `note` (if the title is a claim but the body is free-form). A research note with a crystallized conclusion is `structured-claim` + `has-external-sources` — no forced choice.

## The verifiability gradient

`note` is the base type that makes no structural claim — like `Any` in a gradually typed language. This connects to the [verifiability gradient](../notes/deploy-time-learning-the-missing-middle.md): just as code starts stochastic and stabilizes to deterministic, documents start untyped and gain type information as they mature.

1. New content enters as `type: note` — soft, no structural claims
2. Traits accumulate as the document develops — `has-implementation` when code sketches appear, `has-external-sources` when citing external material
3. Base type gets promoted to `structured-claim`, `spec`, or `review` when hard structural criteria are met
4. A bare `note` with no traits that persists is a signal — maybe it needs splitting, promotion, or review

This is gradual typing applied to documents. The system works at every point on the spectrum, from fully untyped to fully classified.

## Programming language parallels

Several type system concepts map to specific aspects of this design:

- **Gradual typing** (Python, TypeScript) → the verifiability gradient. `note` is `Any`; type annotations accumulate as confidence grows
- **Protocols / structural typing** → traits. A document satisfies `has-external-sources` if it references external material, regardless of whether someone labeled it. We store the label for searchability rather than re-checking every time
- **Refinement types** (`{x: int | x > 0}`) → traits as predicates on `note`. Some are easy to check (`has-external-sources` — grep for URLs), others require judgment (`has-comparison` — is there a structured evaluation?)
- **Soft typing** (Scheme/Lisp) → tolerance of misclassification. The system infers types advisorily; violations are quality issues, not errors

## Tolerance of misclassification

Since types are assigned by a stochastic processor, the system must degrade gracefully when classifications are wrong:

- Search by type should be "usually right", not "guaranteed complete"
- A note typed `spec` that's really an exploration is a quality issue, not a system failure
- The trait list is a best-effort annotation, not a contract
- Nothing should break if a type or trait is missing or incorrect

The practical test: an agent that ignores the type field entirely and reads every document should still work — just less efficiently. Types are an optimization for navigation, not a correctness requirement.

---

Relevant Notes:
- [document-classification](./document-classification.md) — the spec implementing this design: base types, traits, and the migration table from old flat types
- [automated-tests-for-text](./observations/automated-tests-for-text.md) — enables enforcement: the test pyramid provides the "compiler" for type contracts (deterministic checks for structure, LLM rubrics for judgment-dependent traits)
- [storing-llm-outputs-is-stabilization](../notes/storing-llm-outputs-is-stabilization.md) — grounds the stochastic processor argument: type assignment is itself a stabilization decision, and the tolerance of misclassification mirrors the generator/verifier pattern
- [agents-navigate-by-deciding-what-to-read-next](./observations/agents-navigate-by-deciding-what-to-read-next.md) — types and traits are the navigation hints this note describes; they tell agents what a document offers before opening it
- [deploy-time-learning](../notes/deploy-time-learning-the-missing-middle.md) — the verifiability gradient that the type maturation path mirrors: `note` is untyped, traits accumulate, base types promote
- [001-generate-topic-links-from-frontmatter](./adr/001-generate-topic-links-from-frontmatter.md) — precedent: when a mapping is verifiable and deterministic (areas -> Topics), it was automated; the same principle drives the type system design

Topics:
- [document-system](./document-system.md)
