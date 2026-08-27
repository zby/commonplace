---
description: Document types should assert verifiable structural properties, not subject matter — with a base type + traits model inspired by gradual and structural typing
type: kb/types/note.md
traits: [title-as-claim]
tags: [type-system]
---

# Document types should be verifiable

## What "verifiable" means

A document type should assert a structural property you can check. "This is a spec" is verifiable — you can look for Motivation, Design, Implementation sections. "This is a design note" is not — any note in a design KB is about design; the label adds no checkable information.

The test: after reading the type, can you say something concrete about the document's structure without opening it? If not, the type is subject matter, not structure — and subject matter belongs in the `areas` field.

## Why verifiable: unenforceable types are useless

In programming, types are useful because the compiler enforces them. If nothing checked that a `List` is actually a list, the type annotation would be decoration. The value of a type comes from enforcement — something in the system acts on it.

Here, the "compiler" is a mix of agents and scripts. An agent reading `type: kb/reference/types/adr.md` can expect Context, Decision, and Consequences sections. A script validating `type: kb/notes/types/structured-claim.md` can require Evidence and Reasoning headings. They can only act this way if the resolved type spec asserts something checkable. A subject-matter label such as the retired `design` value gives them nothing to act on — every note in a design KB is "about design." An unverifiable type is like an unenforced type annotation: technically present, practically invisible. The [text testing pyramid](./automated-tests-for-text.md) sketches the enforcement split: deterministic checks for structural contracts, LLM rubrics for judgment-dependent traits.

Types guide what the processor — an [LLM interpreting underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — can do with the document. A `spec` tells an agent it can build against this. A `has-comparison` tells it there are alternatives to choose between. Since [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md), types and traits are precisely the hints that make those decisions informed rather than blind — the type tells the agent what it can do with the document *before opening it*. The type is only useful if the processor can trust it, and trust requires the ability to check.

## But our processor interprets underspecified instructions

In conventional programming, types are crisp because the processor is deterministic. A compiler can verify that a value satisfies a type with certainty.

Our processor is an [LLM that interprets underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md). This has a direct consequence: type *assignment* is also underspecified. An agent classifying a document resolves the ambiguity inherent in the type definitions — the same document might be classified differently by different agents, or even the same agent on different runs. The underspecification isn't a bug in the type system. It's a consequence of the specifications (both the document and the type definitions) being in natural language, which doesn't have precise denotations.

This means we need types that are useful despite underspecification — types that assert structural properties you can check, even if the checking requires judgment rather than proof. Type assignment has the same selection boundary as [selecting an LLM output](./selecting-an-llm-output-fixes-a-result-not-its-interpretation.md): choosing `type: kb/notes/types/structured-claim.md` fixes which contract downstream tools consume, but it does not make the natural-language parts of that contract unambiguous.

## What went wrong with flat types

The original type system used a flat enum: `design`, `analysis`, `insight`, `research`, `comparison`, `spec`, `review`, `index`.

**"design" says nothing structural.** A design note could be a spec, an exploration, a brainstorm, or a comparison. It describes subject matter (this is about design), which is what the `areas` field is for. As a type it dominated the KB — half the notes were "design" — which means it did no discriminatory work. In the retired flat encoding, an agent reading `type: design` learned nothing about what it could do with the document.

**Flat types force false choices.** Is a research note that reaches a codified conclusion an insight or research? Is an analysis that cites external sources research or analysis? A flat enum forces a single choice and loses information. In object-oriented terms, this is like having `class ResearchInsight` but being forced to inherit from only one of `Research` or `Insight`.

## Base types + traits

The solution borrows from subtyping and structural typing. Instead of a flat enum, use a **base type** (hard structural category) plus **traits** (independently checkable properties):

```yaml
type: kb/types/note.md
traits: [has-comparison, has-external-sources]
```

**Base types** are structurally distinct with low ambiguity — like choosing between `List`, `Dict`, and `Set`:

| Base type | What it tells the agent |
|-----------|------------------------|
| `kb/types/note.md` | Default — read it to find out what you can do with it |
| `kb/notes/types/structured-claim.md` | This argument supplies Evidence and Reasoning sections |
| `kb/reference/types/adr.md` | This records a decision through Context, Decision, and Consequences |
| `kb/types/generated-index.md` | This is a build-generated listing; use it to enumerate the directory it covers |

**Traits** are independently checkable properties — like interfaces or protocols that a value can satisfy in any combination:

| Trait | What it tells the agent |
|-------|------------------------|
| `has-comparison` | You can use this to decide between alternatives |
| `has-external-sources` | This connects to material outside the project |
| `has-implementation` | This contains code sketches or concrete API proposals |

A note can satisfy multiple traits without conflict. What the old system called "research" becomes `kb/types/note.md` + `has-external-sources`. What it called "insight" uses `kb/notes/types/structured-claim.md` if the argument is developed, or stays `kb/types/note.md` if the title is a claim but the body is free-form. A research note with a codified conclusion is `kb/notes/types/structured-claim.md` + `has-external-sources` — no forced choice.

## The verifiability gradient

[`kb/types/note.md`](../types/note.md) is the base structured type that makes few body-shape claims — like `Any` in a gradually typed language. This connects to the [verifiability gradient](./verifiability-gradient.md): just as logic starts underspecified and constrains toward precision, documents can start as frontmatter-free text and gain checkable structure.

1. New content enters as implicit `text` or as `type: kb/types/note.md` — soft, with no required body sections
2. Traits accumulate as the document develops — `has-implementation` when code sketches appear, `has-external-sources` when citing external material
3. The type pointer changes to a narrower contract such as `type: kb/notes/types/structured-claim.md` when its structural criteria are met
4. A base note with no traits may still be the right final shape; when its body makes stronger promises, a narrower type or trait makes those promises checkable

This is gradual typing applied to documents. The system works at every point on the spectrum, from fully untyped to fully classified.

## Programming language parallels

Several type system concepts map to specific aspects of this design:

- **Gradual typing** (Python, TypeScript) → the verifiability gradient. `note` is `Any`; type annotations accumulate as confidence grows
- **Protocols / structural typing** → traits. A document satisfies `has-external-sources` if it references external material, regardless of whether someone labeled it. We store the label for searchability rather than re-checking every time
- **Refinement types** (`{x: int | x > 0}`) → traits as predicates on `note`. Some are easy to check (`has-external-sources` — grep for URLs), others require judgment (`has-comparison` — is there a structured evaluation?)
- **Soft typing** (Scheme/Lisp) → tolerance of misclassification. The system infers types advisorily; violations are quality issues, not errors

## Tolerance of misclassification

Since types are assigned by a processor that interprets underspecified instructions, deterministic and semantic mismatch need different handling:

- A missing or non-path `type:` value on a frontmatter-bearing artifact is a validation error.
- A declared type whose required fields or sections are absent is a validation error.
- A structurally conforming artifact assigned to the wrong semantic type is a review-quality problem; schema validation cannot settle authorial intent.
- Traits are stored review expectations. A false or missing trait degrades review routing even when it does not break structural validation.

An agent can still understand content by reading the whole artifact, but authoring and type-directed operations should follow the path-valued contract. Type metadata is both a navigation affordance and a structural correctness boundary.

---

Relevant Notes:

- [collections and types](../reference/collections-and-types.md) — implemented-by: the current path-valued type model and its schema/review enforcement split
- [automated-tests-for-text](./automated-tests-for-text.md) — enables enforcement: the test pyramid provides the "compiler" for type contracts (deterministic checks for structure, LLM rubrics for judgment-dependent traits)
- [Selecting an LLM output fixes a result, not its interpretation](./selecting-an-llm-output-fixes-a-result-not-its-interpretation.md) — grounds: type assignment selects one classification for operative use without proving that it is the only valid reading, so the chosen classification still needs verification
- [agents-navigate-by-deciding-what-to-read-next](./agents-navigate-by-deciding-what-to-read-next.md) — types and traits are the navigation hints this note describes; they tell agents what a document offers before opening it
- [the verifiability gradient](./verifiability-gradient.md) — the ladder that the type maturation path mirrors: `note` is untyped, traits accumulate, base types promote
