---
description: Definition — codification is constraining that crosses a medium boundary, the phase transition from natural language to executable code where medium, consumer, and verification regime all change — the far end of the constraining spectrum
type: note
traits: []
areas: [learning-theory]
status: current
---

# Codification

The far end of the [constraining](./constraining.md) spectrum — the point where constraining the interpretation space crosses a medium boundary. Natural language instructions become executable code. The medium changes (markdown → Python/script), the consumer changes (LLM → interpreter/runtime), and the verification regime changes (underspecified semantics → precise semantics, indeterministic → deterministic). It is a phase transition — the nature of the artifact changes fundamentally.

Codification is not a separate mechanism from constraining; it's what constraining looks like when it goes all the way. But the phase transition is qualitatively significant enough to name. Everything below codification on the constraining spectrum (conventions, structured sections, better descriptions) constrains the interpretation space while staying in natural language. Codification leaves natural language entirely.

## Why it matters

Codification produces the largest compound gain in reliability, speed, and cost because it removes the LLM from the loop entirely for the codified operation. The trade-off is generality: the code handles exactly what it handles, nothing more.

The [verifiability gradient](./deploy-time-learning-the-missing-middle.md) runs from restructured prompts through schemas and evals to deterministic code. Codification sits at the far end — full verifiability, full determinism, zero LLM cost. Moving along this gradient is progressive constraining; crossing into code is codification.

## When to codify

Codify when a pattern has emerged across enough runs that you can confidently commit to one interpretation in code. Premature codification — committing before you've observed enough variation — locks in brittle assumptions. The [constrain/relax cycle](./constraining.md) is the safety valve: if new requirements reveal that you committed to the wrong interpretation, relax back to an underspecified spec and let the LLM handle it until a better pattern emerges.

[Oracle strength](./oracle-strength-spectrum.md) determines what can codify. Operations with hard oracles (the output is unambiguously right or wrong) are natural candidates. Operations with weak oracles (correctness requires judgment) resist codification — you can constrain them within natural language but can't cross the medium boundary.

## Codification as distillation

Codification can also be [distillation](./distillation.md) — targeted extraction where the target is "runs fast and cheap." This codebase demonstrates the pattern: methodology notes describe how to validate frontmatter — required fields, description quality criteria, type enums, status values. Those get distilled into the `/validate` skill (methodology → procedure, staying in natural language). Then someone notices that some checks are purely mechanical — does the description field exist? Is the type value in the valid enum? Those checks get codified into a Python validation script.

The script is both codified and distilled. An earlier version included LLM-based checks (like whether the description matches the note's content), but those were dropped — not because they weren't useful, but because the target was a quick, cheap check you can run constantly. The target selected what to extract. A different distillation targeting thorough review would keep the LLM checks and produce a different artifact from the same source. The methodology notes remain as the common pool serving both targets.

The same pattern produced `generate_notes_index.py`: methodology notes describe when to create indexes, how to format entries, what editorial context to include. The script codifies only the mechanical part. Curated area indexes stay in natural language because they require judgment about grouping and context.

Not every codification is distillation. One-shot codification — directly translating a spec into code with no larger body of reasoning behind it — is pure constraining. But when codification draws on accumulated methodology or practice, it's both operations at once: extracting the automatable subset (distillation) and committing it to a deterministic medium (constraining at its extreme).

## Other examples

Replacing an LLM slug generator with `python-slugify`; moving CSV statistics from LLM arithmetic to Python's `statistics` module. In each case, the operation had a single correct interpretation that was being re-discovered by the LLM on every run.

Not codification: writing a convention (constraining — constrains the interpretation space without changing medium); extracting a skill from methodology notes (distillation — targeted extraction, stays in natural language).

---

Relevant Notes:

- [constraining](./constraining.md) — parent mechanism: codification is the far end of the constraining spectrum
- [distillation](./distillation.md) — orthogonal mechanism: targeted extraction; codification sometimes follows distillation (extract a procedure, then codify it to code)
- [deploy-time learning](./deploy-time-learning-the-missing-middle.md) — the verifiability gradient across which codification sits at the far end
- [spec-mining-as-codification](./spec-mining-as-codification.md) — the operational mechanism: observe behavior, extract patterns, write deterministic code
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — determines what can codify: hard oracles enable it, weak oracles resist it
- [Harness Engineering (Lopopolo, 2026)](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — exemplifies: encoding quality standards into linters that replace manual judgment is codification at production scale

Topics:

- [learning-theory](./learning-theory.md)
