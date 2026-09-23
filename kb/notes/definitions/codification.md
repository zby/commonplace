---
description: "Definition — codification is the symbolic region of constraining: a rule or operation is committed to an artifact with formal semantics or, more generally, fixed rules that determine what behavior is permitted"
type: kb/types/definition.md
tags: [learning-theory, constraining]
---

# Codification

Codification is the symbolic region of [constraining](./constraining.md): a rule or operation stated in natural language is committed to a symbolic artifact with a **unique operational semantics**: fixed rules, implemented by a runtime, parser, validator, type checker, query engine, or resolver, determine what behavior is permitted, including any variation they explicitly allow. When two consumers disagree about what those rules permit, one of them is wrong. The consumer changes from a model or human who reinterprets the text on each use to one bound by those rules, so what the artifact permits no longer depends on who reads it, and departures from it are bugs rather than an expected failure rate. Executable code is the main practical KB case. The best intuition is formal semantics: the artifact's meaning is fixed by rules rather than by whoever reads it. The criterion is slightly weaker, because most programming languages have no formal semantics, yet their implementations [aim at a unique operational semantics](../agentic-systems-interpret-underspecified-instructions.md).

This is the KB's internal technical use of the word. It is narrower than ordinary "codification," which can mean putting norms into systematic written form, including legal codes, formal policies, or other precise prose. In this KB, making natural language more precise is constraining, but not codification unless the result is a symbolic artifact with a unique operational semantics.

## Scope

Use the term when a rule or operation has been committed to a symbolic artifact: code, scripts, schemas, validators, tests, parsers, route tables, grammars, type declarations, query expressions, or other artifacts with a unique operational semantics, instead of a model reinterpreting them on each use.

Examples: replacing an LLM slug generator with `python-slugify`; moving CSV statistics from LLM arithmetic to Python's `statistics` module; extracting mechanical frontmatter checks from a validation skill into a Python script; turning allowed frontmatter values into a schema enum; expressing a route decision as a table consumed by a resolver. Executable code is the common case because KB operations often need commands and validators.

## Exclusions

Writing a convention is not codification when it stays in natural language; it constrains interpretation but keeps the model or human as the interpreter. A skill extracted from methodology notes is not codification while its instructions remain natural language, [since skills derive from methodology](../skills-derive-from-methodology.md) without changing representational form.

Turning a rule into legalese, a standards document, or a formal prose policy is not codification in this KB's technical sense. It may be strong constraining, but the artifact still depends on natural-language interpretation.

Structured Markdown, YAML, or JSON is not automatically codification. It becomes codification only where a consumer gives fields, values, sections, or operations a unique operational semantics.

Numerical content does not by itself require codification. An exact numerical claim can be stated and tested in natural language; it needs symbolic form only when it must have a unique operational semantics, such as mechanically repeatable computation or acceptance.

## Codified parts of a theory

The same crossing gives a part of a retained theory a computed consequence relation. A natural-language part's consequences depend on what its interpreter derives; a codified part's consequences are fixed by its operational semantics. Codification alone does not supply diagnosis or successful repair. A failed check must be connected to the theory commitments it tests before it can guide candidate edits. [Addressability](./addressable-theory.md) makes parts available for inspection and separate revision; it does not guarantee that the identified part caused the failure or that the revision repairs it.

## Codification and relaxing

[Progressive constraining](../progressive-constraining-commits-only-after-patterns-stabilize.md) commits a pattern to code once observed runs show it is stable; committing a single LLM output instead freezes an arbitrary reading. How far codification can go depends on the available checks: [hard oracles make it easier, weak oracles resist it](../oracle-strength-spectrum.md). Every codification is a bet that the committed reading stays right. [Relaxing](../codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) reverses it when the reading turns out to be a wrong proxy, or when a more general component handles the case well enough.

## Misuse Cases

- Calling every clearer instruction "codified" even though the consumer is still an LLM interpreting natural language.
- Calling legalistic or policy prose codified in this KB's technical sense just because it is formalized.
- Calling a natural-language skill codified merely because it has frontmatter. The frontmatter may be symbolic, but the operative guidance can still be natural-language.
- Treating only executable code as codification. Code is the main practical case, but schemas, grammars, tables, and other symbolic artifacts also codify when they have a unique operational semantics.
- Treating a codified check as a codified requirement. A validator excludes readings only within the predicate it checks; when that predicate is a [proxy](../exact-implementation-does-not-validate-a-requirement.md), the requirement itself remains interpreted.

---

Relevant Notes:

- [constraining](./constraining.md) — defined-in: codification is the symbolic region of constraining, where fixed rules settle what the artifact permits
- [representational form](./representational-form.md) — defined-in: what makes an artifact symbolic: a unique operational semantics, localized in an identifiable unit
- [addressable theory](./addressable-theory.md) — defined-in: parts of a theory available for inspection and separate revision
- [skills derive from methodology](../skills-derive-from-methodology.md) — contrasts: derivation that stays natural language, where codification changes representational form
- [progressive constraining commits only after patterns stabilize](../progressive-constraining-commits-only-after-patterns-stabilize.md) — extends: when a pattern is stable enough to codify
- [spec mining as codification](../spec-mining-as-codification.md) — mechanism: observe behavior, extract patterns, write deterministic code
- [oracle strength spectrum](../oracle-strength-spectrum.md) — extends: how the available checks limit codification
- [codification and relaxing navigate the bitter-lesson boundary](../codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — extends: when to reverse a codification
- [fixed artifacts split into exact specs and proxy theories](../exact-implementation-does-not-validate-a-requirement.md) — extends: when a codified check stands in for its requirement
- [the verifiability gradient](../verifiability-gradient.md) — extends: the checks that decide how far constraining can go with confidence
