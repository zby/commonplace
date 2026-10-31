---
description: "Definition — codification is the symbolic region of constraining: a rule or operation is committed to an artifact with formal semantics or, more generally, fixed rules that determine what behavior is permitted"
type: types/definition.md
tags: [learning-theory, constraining]
---

# Codification

Codification commits a rule or operation stated in natural language to a symbolic artifact, such as code or a schema, with a **unique operational semantics**. Fixed rules, implemented by a runtime, parser, validator, type checker, query engine, or resolver, determine what behavior is permitted, including any variation they explicitly allow. The consumer changes from a model or human who reinterprets the text on each use to one bound by those rules, so what the artifact permits no longer depends on who reads it.

Codification is the symbolic region of [constraining](./constraining.md)—committing choices that narrow or rank permitted readings or behaviors. Making natural language more precise also constrains interpretation, but remains outside codification until the result has fixed rules for permitted behavior.

## Criterion and testing

"Operational semantics" here means the rules for permitted behavior that consumers held to one reference are expected to preserve. The reference fixes the language version and any implementation or execution parameters needed to settle what is permitted. When two consumers disagree about what those rules permit, one of them is wrong. Departures are failures to implement the committed rules, not alternative admissible interpretations. Execution can still fail: implementations can have bugs, and natural-language interpreters can also violate unambiguous instructions.

The best intuition is formal semantics: the artifact's meaning is fixed by rules rather than by whoever reads it. The criterion is slightly weaker, because most programming languages have no formal semantics, yet their implementations [aim at a unique operational semantics](../agentic-systems-interpret-underspecified-instructions.md). It conjectures that the reference rules admit a formal semantics for the artifact's language; consumer agreement is evidence for that conjecture, not its definition. That semantics may be unwritten and very complicated.

The clerk test locates where such a semantics can exist: Turing derived the formal machine by asking what a human computer can do when following exact instructions without insight ([Church–Turing](../../sources/church-turing-thesis-sep.ingest.md)). A rule is therefore a candidate for codification when a consumer forbidden insight could follow it. Whether it can is not established merely by inspecting the text. Trying many clerks against the same reference tests whether the rules leave choices that require interpretation.

Independent implementations and conformance tests can corroborate the conjecture by trying to reveal disagreements about the reference rules. Agreement alone is insufficient: clerks can share an assumption, compilers can share a bug, and a test suite can miss both. The reference must specify what is permitted independently of the observed agreement. A disagreement may reveal an implementation bug or a gap in the reference; repairing the latter fixes a previously unsettled choice. Testing does not prove uniqueness or guarantee convergence on it. A lone implementation can serve as the reference, but its repeatability alone does not show that another consumer could preserve the same rules. An artifact written in a language with independently tested semantics inherits that support within the tested scope.

Not all English passes the clerk test. The fragment that does is a programming language in the making. Where instructions still require judgment to settle what is permitted, they remain natural-language constraining: [two readings can both be reasonable](../agentic-systems-interpret-underspecified-instructions.md), and the committed rules do not settle the disagreement. The boundary concerns the rules supplied for the operation, not a claim that natural language could never have a complete formal semantics.

## Terminology

This is the KB's internal technical use of the word. It is narrower than ordinary "codification," which can mean putting norms into systematic written form, including legal codes, formal policies, or other precise prose.

"Operational semantics" here is not the programming-language term for a rule system that specifies a transition relation independently of any implementation ([Plotkin](../../sources/plotkin-origins-of-sos.ingest.md)), and it is not operationalism's definition of a concept by the operations that measure it ([operationalism](../../sources/operationalism-sep.ingest.md)). The [vocabulary collision ledger](../../reference/vocabulary-collision-ledger.md) records the senses.

## Scope

Use the term when a rule or operation has been committed to a symbolic artifact: code, scripts, schemas, validators, tests, parsers, route tables, grammars, type declarations, query expressions, or other artifacts with a unique operational semantics, instead of a model reinterpreting them on each use.

Examples: replacing an LLM slug generator with `python-slugify`; moving CSV statistics from LLM arithmetic to Python's `statistics` module; extracting mechanical frontmatter checks from a validation skill into a Python script; turning allowed frontmatter values into a schema enum; expressing a route decision as a table consumed by a resolver. Executable code is the main practical KB case because it inherits support from independently tested language semantics within the tested scope, and KB operations often need commands and validators.

## Exclusions

Writing a convention that stays in natural language constrains interpretation while keeping the model or human as the interpreter. A skill extracted from methodology notes is not codification while its instructions remain natural language, [since skills derive from methodology](../skills-derive-from-methodology.md) without changing [representational form](./representational-form.md)—how the content is encoded and consumed.

Turning a rule into legalese, a standards document, or a formal prose policy may be strong constraining while still depending on natural-language interpretation.

Structured Markdown, YAML, or JSON becomes codification only where a consumer gives fields, values, sections, or operations a unique operational semantics.

An exact numerical claim can be stated and tested in natural language; it needs symbolic form only when it must have a unique operational semantics, such as mechanically repeatable computation or acceptance.

## Codified parts of a theory

The same crossing gives a part of a retained theory consequences fixed by computation. A natural-language part's consequences depend on what its interpreter derives; a codified part's consequences are fixed by its operational semantics. Codification alone does not supply diagnosis or successful repair. A failed check must be connected to the theory commitments it tests before it can guide candidate edits. [Addressability](./addressable-theory.md) makes parts available for inspection and separate revision; it does not guarantee that the identified part caused the failure or that the revision repairs it.

## Codification and relaxing

[Progressive constraining](../progressive-constraining-commits-only-after-patterns-stabilize.md) commits a pattern to code once observed runs show it is stable; committing a single LLM output instead fixes an arbitrary reading. How far codification can go depends on the available checks: [hard oracles make it easier, weak oracles resist it](../oracle-strength-spectrum.md). Every codification is a bet that the committed reading stays right. [Relaxing](../codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) reverses it when the reading turns out to be a wrong proxy, or when a more general component handles the case well enough.

## Misuse Cases

- Calling every clearer instruction "codified" even though the consumer is still an LLM interpreting natural language.
- Calling legalistic or policy prose codified in this KB's technical sense just because it is formalized.
- Calling a natural-language skill codified merely because it has frontmatter. The frontmatter may be symbolic, but the instructions that guide behavior can still be natural-language.
- Treating agreement among consumers, or repeatability from one consumer, as sufficient for codification. The consumers must be held to reference rules that settle what is permitted independently of that agreement.
- Treating only executable code as codification. Schemas, grammars, tables, and other symbolic artifacts also codify when they have a unique operational semantics.
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
- [Copeland, The Church-Turing thesis](../../sources/church-turing-thesis-sep.ingest.md) — evidenced-by: the clerk test that locates the formalizable fragment; secondary scholarship, so it bounds the criterion rather than corroborating it
- [Plotkin, The origins of structural operational semantics](../../sources/plotkin-origins-of-sos.ingest.md) — see-also: the programming-language sense of operational semantics that this definition does not use
- [Operationalism](../../sources/operationalism-sep.ingest.md) — see-also: the measurement sense of operational that this definition does not use
