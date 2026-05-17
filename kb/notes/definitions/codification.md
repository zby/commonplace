---
description: Definition — codification is constraining that crosses a medium boundary from natural language to a symbolic medium (code), where the consumer changes (LLM → interpreter) and verification becomes exact — the far end of the constraining spectrum
type: kb/types/definition.md
tags: [learning-theory]
status: current
---

# Codification

The far end of the [constraining](./constraining.md) spectrum — the point where constraining the interpretation space crosses a medium boundary. Natural language instructions become executable code. The medium changes (markdown → Python/script), the consumer changes (LLM → interpreter/runtime), and the verification regime changes (underspecified semantics → formal semantics, stochastic → deterministic). It is a phase transition — the nature of the artifact changes fundamentally.

Codification is not a separate mechanism from constraining; it's what constraining looks like when it goes all the way. Everything below codification on the constraining spectrum (conventions, structured sections, better descriptions) constrains the interpretation space while staying in natural language. Codification leaves natural language for a symbolic medium entirely.

## Scope

Use codification when a recurring operation or rule has been committed to a symbolic consumer: code, scripts, schemas, validators, tests, parsers, route tables, or other artifacts whose consequences are assigned by an interpreter or runtime rather than reinterpreted by an LLM each time.

Codification may follow distillation, but it does not have to. When accumulated methodology is extracted into a script, the operation is both distillation and codification. When a one-off spec is directly translated into code, it is codification without much distillation.

## When to codify

Codify when a pattern has emerged across enough runs that you can confidently commit to one interpretation in code. Premature codification locks in brittle assumptions. The [constrain/relax cycle](./constraining.md) is the safety valve: if new requirements reveal the wrong commitment, relax back to an underspecified spec and let the LLM handle it until a better pattern emerges.

[Oracle strength](../oracle-strength-spectrum.md) determines what can codify. Operations with hard oracles (the output is unambiguously right or wrong) are natural candidates. Operations with weak oracles (correctness requires judgment) resist codification.

## Relationship to distillation

Codification can also be [distillation](./distillation.md) — when it draws on accumulated methodology or practice, it's both operations at once: extracting the automatable subset (distillation) and committing it to a symbolic medium (constraining at its extreme). One-shot codification — directly translating a spec into code with no larger body of reasoning behind it — is pure constraining without distillation.

Examples: replacing an LLM slug generator with `python-slugify`; moving CSV statistics from LLM arithmetic to Python's `statistics` module; extracting mechanical frontmatter checks from a validation skill into a Python script. In each case, the operation had a single correct interpretation that was being re-discovered by the LLM on every run.

## Exclusions

Writing a convention is not codification when it stays in natural language; it constrains interpretation but keeps the LLM or human as the interpreter. Extracting a skill from methodology notes is not codification when the skill remains prose instructions; it is distillation that stays in natural language.

Structured Markdown, YAML, or JSON is not automatically codification. It becomes codification only where a consumer assigns defined consequences to fields, values, sections, or operations.

## Misuse Cases

- Calling every clearer instruction "codified" even though the consumer is still an LLM interpreting prose.
- Treating codification as always good. Premature codification freezes a proxy theory and may need relaxing when new cases appear.
- Calling a distilled skill codified merely because it has frontmatter. The frontmatter may be symbolic, but the operative guidance can still be prose.

---

Relevant Notes:

- [constraining](./constraining.md) — parent mechanism: codification is the far end of the constraining spectrum
- [distillation](./distillation.md) — orthogonal mechanism: targeted extraction; codification sometimes follows distillation (extract a procedure, then codify it to code)
- [the verifiability gradient](../verifiability-gradient.md) — the ladder across which codification sits at the far end
- [spec-mining-as-codification](../spec-mining-as-codification.md) — the operational mechanism: observe behavior, extract patterns, write deterministic code
- [oracle-strength-spectrum](../oracle-strength-spectrum.md) — determines what can codify: hard oracles enable it, weak oracles resist it
- [Harness Engineering (Lopopolo, 2026)](https://openai.com/index/harness-engineering/) — exemplifies: encoding quality standards into linters that replace manual judgment is codification at production scale
