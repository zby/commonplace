# Codification (proposed definition)

Workshop draft, 2026-11-01. This file is the complete proposed text of the library's [codification](../../theory/definitions/codification.md) definition, written from the [account of symbolic form](./symbolic-form-and-codification.md). The criterion moves into [symbolic form](./representational-form-definition.md), and codification becomes the move into that form. The opening, the criterion section, the clerk and testing paragraphs, the terminology section and two misuse cases are new or rewritten; the scope, examples, exclusions, codified-parts and relaxing sections are carried over with the retired phrase replaced. Links are written for this file's location and change on promotion. The library definition remains authoritative until then. Open questions are at the end.

---

Codification moves a rule or operation stated in natural language into [symbolic form](./representational-form-definition.md): into an artifact, such as code or a schema, in a language that has a formal semantics or is close to one. Fixed rules, implemented by a runtime, parser, validator, type checker, query engine, resolver, or adopted model package, determine what behavior is permitted, including any variation, external selection, or clarification step they explicitly provide for. The consumer changes from a model or human who reinterprets the text on each use to one bound by those rules, so what the artifact permits no longer depends on who reads it.

Codification is the symbolic region of [constraining](../../theory/definitions/constraining.md), committing choices that narrow or rank permitted readings or behaviors. Making natural language more precise also constrains interpretation, but remains outside codification until a reference the language's users hold consumers to settles what the result permits.

## Criterion

The criterion is the one symbolic form states: the artifact's language has a formal semantics or is close to one, where close means its users hold consumers to a reference, a standard or an implementation, from which a formal semantics could be derived. The move is made in one of two ways. Rewriting the artifact in such a language is the ordinary way. Adopting a consumer as the reference for an operation, such as a pinned model package with its decoding procedure, is the other: the text does not change, and its form under that consumption path does, because the adopting system is then a user of the language of prompts as that package reads them, and it holds the consumer to it.

What the reference leaves open is permitted variation, a required external selection, or a defect, and only the last is a failure of the reference. An artifact whose consequences no reference fixes is reinterpreted on each consumption, and two readings of it can both be reasonable. Execution can still fail: implementations can have bugs, and natural-language interpreters can also violate unambiguous instructions.

A formalization of a consumer is not the semantics of the language. Any implemented consumer together with a machine model supplies a formal account of its own behavior, and this holds for a frozen language model as much as for a compiler. That account is the semantics of a language only when the language's users hold consumers to it, so adopting a frozen model codifies the operation it is adopted for and leaves the semantics of English untouched. A codified artifact can be opaque, in the sense symbolic form gives the modifier: a large codebase from its scale, an adopted model package from the form of its reference. Opacity sets how the artifact is checked and where it is revised; it does not set whether the artifact is codified. An opaque codification lacks the advantages of ordinary code and is still a codification.

## The clerk and testing

Turing derived the formal machine by asking what a human computer can do when following exact instructions without insight ([Church–Turing](../../sources/church-turing-thesis-sep.ingest.md)). That is why a formal semantics can be derived from a reference whose every step of application is mechanically checkable, and why none can be derived from a human judge. The clerk explains derivability; it is not the criterion's wording. The condition is on the steps, not a claim that every consequence of the reference is decidable, which is stronger and often false.

Independent implementations and conformance tests corroborate conformance to the reference by trying to reveal disagreements about what it permits. Agreement alone is insufficient: clerks can share an assumption, compilers can share a bug, and a test suite can miss both. The reference must specify what is permitted independently of the observed agreement. A disagreement may reveal an implementation bug or a defect in the reference; repairing the latter fixes a previously unsettled choice. Testing does not prove conformance outside the tested cases. A lone implementation can serve as the reference once its users hold consumers to it, but its repeatability alone does not show that another consumer could preserve the same rules. An artifact written in a language with independently tested semantics inherits that support within the tested scope.

Not all English passes the clerk. The fragment that does, once its users hold consumers to a reference, is a programming language in the making. Where instructions still require judgment to settle what is permitted, they remain natural-language constraining: [two readings can both be reasonable](../../theory/agentic-systems-interpret-underspecified-instructions.md), and no reference settles the disagreement. The boundary concerns the rules supplied for the operation, not a claim that no fragment of natural language can have a formal semantics.

## Terminology

This is the KB's internal technical use of the word. It is narrower than ordinary "codification," which can mean putting norms into systematic written form, including legal codes, formal policies, or other precise prose. The programming-language term operational semantics ([Plotkin](../../sources/plotkin-origins-of-sos.ingest.md)) and operationalism's definition of a concept by measurement ([operationalism](../../sources/operationalism-sep.ingest.md)) are not used here; the [vocabulary collision ledger](../../reference/vocabulary-collision-ledger.md) records the senses.

## Scope

Use the term when a rule or operation has been committed to a symbolic artifact: code, scripts, schemas, validators, tests, parsers, route tables, grammars, type declarations, query expressions, or other artifacts whose language has a formal semantics or is close to one, instead of a model reinterpreting them on each use.

Examples: replacing an LLM slug generator with `python-slugify`; moving CSV statistics from LLM arithmetic to Python's `statistics` module; extracting mechanical frontmatter checks from a validation skill into a Python script; turning allowed frontmatter values into a schema enum; expressing a route decision as a table consumed by a resolver. Executable code is the main practical KB case because it inherits support from independently tested language semantics within the tested scope, and KB operations often need commands and validators.

## Exclusions

Writing a convention that stays in natural language constrains interpretation while keeping the model or human as the interpreter. A skill extracted from methodology notes is not codification while its instructions remain natural language, [since skills derive from methodology](../../theory/skills-derive-from-methodology.md) without changing [representational form](./representational-form-definition.md), how the content is encoded and consumed.

Turning a rule into legalese, a standards document, or a formal prose policy may be strong constraining while still depending on natural-language interpretation.

Structured Markdown, YAML, or JSON becomes codification only where a consumer holds fields, values, sections, or operations to a reference.

An exact numerical claim can be stated and tested in natural language; it needs symbolic form only when it must be settled by a reference, such as mechanically repeatable computation or acceptance.

## Codified parts of a theory

The same crossing gives a part of a retained theory consequences fixed by computation. A natural-language part's consequences depend on what its interpreter derives; a codified part's consequences are fixed by its reference. Codification alone does not supply diagnosis or successful repair. A failed check must be connected to the theory commitments it tests before it can guide candidate edits. [Addressability](../../theory/definitions/addressable-theory.md) makes parts available for inspection and separate revision; it does not guarantee that the identified part caused the failure or that the revision repairs it.

## Codification and relaxing

[Progressive constraining](../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md) commits a pattern to code once observed runs show it is stable; committing a single LLM output instead fixes an arbitrary reading. How far codification can go depends on the available checks: [hard oracles make it easier, weak oracles resist it](../../theory/oracle-strength-spectrum.md). Every codification is a bet that the committed reading stays right. [Relaxing](../../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) reverses it when the reading turns out to be a wrong proxy, or when a more general component handles the case well enough.

## Misuse Cases

- Calling every clearer instruction "codified" even though the consumer is still an LLM interpreting natural language.
- Calling legalistic or policy prose codified in this KB's technical sense just because it is formalized.
- Calling a natural-language skill codified merely because it has frontmatter. The frontmatter may be symbolic, but the instructions that guide behavior can still be natural-language.
- Treating agreement among consumers, or repeatability from one consumer, as sufficient for codification. The consumers must be held to a reference that settles what is permitted independently of that agreement.
- Denying that adopting a pinned model codifies the instructions it reads. It does; the codification is opaque, which is why it lacks the advantages of ordinary code.
- Treating only executable code as codification. Schemas, grammars, tables, and other symbolic artifacts also codify when their users hold consumers to a reference.
- Treating a codified check as a codified requirement. A validator excludes readings only within the predicate it checks; when that predicate is a [proxy](../../theory/exact-implementation-does-not-validate-a-requirement.md), the requirement itself remains interpreted.

---

Relevant Notes:

- [constraining](../../theory/definitions/constraining.md) — defined-in: codification is the symbolic region of constraining, where a held-to reference settles what the artifact permits
- [representational form](./representational-form-definition.md) — defined-in: what makes an artifact symbolic, and the opaque modifier
- [addressable theory](../../theory/definitions/addressable-theory.md) — defined-in: parts of a theory available for inspection and separate revision
- [skills derive from methodology](../../theory/skills-derive-from-methodology.md) — contrasts: derivation that stays natural language, where codification changes representational form
- [progressive constraining commits only after patterns stabilize](../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md) — extends: when a pattern is stable enough to codify
- [spec mining as codification](../../theory/spec-mining-as-codification.md) — mechanism: observe behavior, extract patterns, write deterministic code
- [oracle strength spectrum](../../theory/oracle-strength-spectrum.md) — extends: how the available checks limit codification
- [codification and relaxing navigate the bitter-lesson boundary](../../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — extends: when to reverse a codification
- [fixed artifacts split into exact specs and proxy theories](../../theory/exact-implementation-does-not-validate-a-requirement.md) — extends: when a codified check stands in for its requirement
- [the verifiability gradient](../../theory/verifiability-gradient.md) — extends: the checks that decide how far constraining can go with confidence
- [Copeland, The Church-Turing thesis](../../sources/church-turing-thesis-sep.ingest.md) — evidenced-by: the clerk that explains why a formal semantics can be derived from a mechanically checkable reference; secondary scholarship, so it bounds the criterion rather than corroborating it
- [Plotkin, The origins of structural operational semantics](../../sources/plotkin-origins-of-sos.ingest.md) — see-also: the programming-language sense of operational semantics, no longer used here
- [Operationalism](../../sources/operationalism-sep.ingest.md) — see-also: the measurement sense of operational, no longer used here

---

## Open questions about the wording

1. Is dropping the Plotkin and operationalism contrasts to a see-also safe once the colliding phrase is gone, or do readers still arrive with the programming-language sense of "semantics"?
2. Does any library note rely on the formalizability conjecture rather than on the criterion in symbolic form? The migration list in [follow-up library changes](./follow-up-library-changes.md) should check each use of the retired phrase, not only replace it.
3. "Adopted model package" appears in the list of implementing consumers. Does the library want that consequence stated in the opening, or only in the misuse case?
4. The parser-versus-agent distinction in the [account](./symbolic-form-and-codification.md) rests on the input-versus-artifact wording. Does that wording need to be explicit here, or does the execution-contract framing carry it?
