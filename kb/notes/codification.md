---
description: Definition — codification is constraining that crosses a medium boundary from natural language to a symbolic medium (code), where the consumer changes (LLM → interpreter) and verification becomes exact — the far end of the constraining spectrum
type: note
traits: []
tags: [learning-theory]
status: current
---

# Codification

The far end of the [constraining](./constraining.md) spectrum — the point where constraining the interpretation space crosses a medium boundary. Natural language instructions become executable code. The medium changes (markdown → Python/script), the consumer changes (LLM → interpreter/runtime), and the verification regime changes (underspecified semantics → formal semantics, stochastic → deterministic). It is a phase transition — the nature of the artifact changes fundamentally.

Codification is not a separate mechanism from constraining; it's what constraining looks like when it goes all the way. Everything below codification on the constraining spectrum (conventions, structured sections, better descriptions) constrains the interpretation space while staying in natural language. Codification leaves natural language for a symbolic medium entirely.

## When to codify

Codify when a pattern has emerged across enough runs that you can confidently commit to one interpretation in code. Premature codification locks in brittle assumptions. The [constrain/relax cycle](./constraining.md) is the safety valve: if new requirements reveal the wrong commitment, relax back to an underspecified spec and let the LLM handle it until a better pattern emerges.

[Oracle strength](./oracle-strength-spectrum.md) determines what can codify. Operations with hard oracles (the output is unambiguously right or wrong) are natural candidates. Operations with weak oracles (correctness requires judgment) resist codification.

## Relationship to distillation

Codification can also be [distillation](./distillation.md) — when it draws on accumulated methodology or practice, it's both operations at once: extracting the automatable subset (distillation) and committing it to a symbolic medium (constraining at its extreme). One-shot codification — directly translating a spec into code with no larger body of reasoning behind it — is pure constraining without distillation.

Examples: replacing an LLM slug generator with `python-slugify`; moving CSV statistics from LLM arithmetic to Python's `statistics` module; extracting mechanical frontmatter checks from a validation skill into a Python script. In each case, the operation had a single correct interpretation that was being re-discovered by the LLM on every run.

Not codification: writing a convention (constraining within natural language); extracting a skill from methodology notes (distillation, stays in natural language).

---

Relevant Notes:

- [constraining](./constraining.md) — parent mechanism: codification is the far end of the constraining spectrum
- [distillation](./distillation.md) — orthogonal mechanism: targeted extraction; codification sometimes follows distillation (extract a procedure, then codify it to code)
- [deploy-time learning](./deploy-time-learning-the-missing-middle.md) — the verifiability gradient across which codification sits at the far end
- [spec-mining-as-codification](./spec-mining-as-codification.md) — the operational mechanism: observe behavior, extract patterns, write deterministic code
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — determines what can codify: hard oracles enable it, weak oracles resist it
- [Harness Engineering (Lopopolo, 2026)](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — exemplifies: encoding quality standards into linters that replace manual judgment is codification at production scale
