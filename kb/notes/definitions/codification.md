---
description: Definition — codification is constraining that crosses from natural language into a symbolic artifact with formal semantics or assigned consequences; executable code is the main practical KB case
type: kb/types/definition.md
tags: [learning-theory, constraining]
---

# Codification

The far end of the [constraining](./constraining.md) spectrum — the point where constraining the interpretation space crosses from natural language into a symbolic artifact with formal semantics or assigned consequences. In the main practical KB case, natural language instructions become executable code. More generally, the medium changes from prose interpreted by an LLM or human into a symbolic form interpreted by a runtime, parser, validator, type checker, query engine, or other formal consumer. It is a phase transition: the nature of the artifact changes fundamentally.

This is the KB's internal technical use of the word. It is narrower than ordinary "codification," which can mean putting norms into systematic written form, including legal codes, formal policies, or other precise prose. In this KB, prose-to-prose formalization is constraining, but not codification unless the result is a symbolic artifact whose elements have formal semantics or defined operational consequences.

Codification is not a separate mechanism from constraining; it's what constraining looks like when it goes all the way. Everything below codification on the constraining spectrum (definitions, conventions, structured sections, clearer descriptions) constrains the interpretation space while staying in natural language. Codification leaves natural-language interpretation for a symbolic medium.

## Scope

Use the term codification when an operation or rule has been committed to a symbolic consumer: code, scripts, schemas, validators, tests, parsers, route tables, grammars, type declarations, query expressions, or other artifacts whose consequences are assigned by a formal system rather than reinterpreted by an LLM each time.

Codification may draw on a larger body of recorded reasoning, but it does not have to. When accumulated methodology is worked into a script, the artifact is both source-derived and codified. When a one-off spec is directly translated into a schema, table, or program, it is codification with no larger body of reasoning behind it.

## Codification and source lineage

Codification can also be source-derived. When it draws on accumulated methodology or practice, it transforms source material for a bounded consumer and commits the result to a symbolic medium — the `derived-from` lineage labels carry that relationship. One-shot codification — directly translating a spec into code with no larger body of reasoning behind it — is constraining without source lineage.

Examples: replacing an LLM slug generator with `python-slugify`; moving CSV statistics from LLM arithmetic to Python's `statistics` module; extracting mechanical frontmatter checks from a validation skill into a Python script; turning allowed frontmatter values into a schema enum; or expressing a route decision as a table consumed by a resolver. Executable code is the common case because KB operations often need commands and validators, but the broader point is symbolic commitment: the operation has consequences assigned by the artifact's formal semantics.

## Exclusions

Writing a convention is not codification when it stays in natural language; it constrains interpretation but keeps the LLM or human as the interpreter. Extracting a skill from methodology notes is not codification when the skill remains prose instructions; it is same-medium derivation, [since skills derive from methodology](../skills-derive-from-methodology.md) without a phase change.

Turning a rule into legalese, a standards document, or a formal prose policy is not codification in this KB's technical sense. It may be strong constraining, but the artifact still depends on natural-language interpretation.

Structured Markdown, YAML, or JSON is not automatically codification. It becomes codification only where a formal consumer assigns defined consequences to fields, values, sections, or operations.

## Misuse Cases

- Calling every clearer instruction "codified" even though the consumer is still an LLM interpreting prose.
- Calling legalistic or policy prose codified in this KB's technical sense just because it is formalized.
- Calling a prose skill codified merely because it has frontmatter. The frontmatter may be symbolic, but the operative guidance can still be prose.
- Treating only executable code as codification. Code is the main practical case, but schemas, grammars, tables, and other symbolic artifacts can also codify when their formal semantics drive behavior.

---

Relevant Notes:

- [constraining](./constraining.md) — parent mechanism: codification is the far end of the constraining spectrum
- [skills derive from methodology](../skills-derive-from-methodology.md) — contrasts: same-medium derivation, the reshaping that stays prose where codification crosses into a symbolic artifact
- [the verifiability gradient](../verifiability-gradient.md) — the ladder across which codification sits at the far end
- [spec-mining-as-codification](../spec-mining-as-codification.md) — the operational mechanism: observe behavior, extract patterns, write deterministic code
- [oracle-strength-spectrum](../oracle-strength-spectrum.md) — operational guidance: hard oracles make codification easier, weak oracles resist it
- [Harness Engineering (Lopopolo, 2026)](https://openai.com/index/harness-engineering/) — exemplifies: encoding quality standards into linters that replace manual judgment is codification at production scale
