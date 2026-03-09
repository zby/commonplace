---
description: Definition — crystallisation is stabilisation that crosses a medium boundary, the phase transition from natural language to executable code where medium, consumer, and verification regime all change — the far end of the stabilisation spectrum
type: note
traits: []
areas: [learning-theory]
status: current
---

# Crystallisation

The far end of the [stabilisation](./stabilisation.md) spectrum — the point where constraining the interpretation space crosses a medium boundary. Natural language instructions become executable code. The medium changes (markdown → Python/script), the consumer changes (LLM → interpreter/runtime), and the verification regime changes (underspecified semantics → precise semantics, indeterministic → deterministic). It is a phase transition — the nature of the artifact changes fundamentally.

Crystallisation is not a separate mechanism from stabilisation; it's what stabilisation looks like when it goes all the way. But the phase transition is qualitatively significant enough to name. Everything below crystallisation on the stabilisation spectrum (conventions, structured sections, better descriptions) constrains the interpretation space while staying in natural language. Crystallisation leaves natural language entirely.

## Why it matters

Crystallisation produces the largest compound gain in reliability, speed, and cost because it removes the LLM from the loop entirely for the crystallised operation. The trade-off is generality: the code handles exactly what it handles, nothing more.

The [verifiability gradient](./deploy-time-learning-the-missing-middle.md) runs from restructured prompts through schemas and evals to deterministic code. Crystallisation sits at the far end — full verifiability, full determinism, zero LLM cost. Moving along this gradient is progressive stabilisation; crossing into code is crystallisation.

## When to crystallise

Crystallise when a pattern has emerged across enough runs that you can confidently commit to one interpretation in code. Premature crystallisation — committing before you've observed enough variation — locks in brittle assumptions. The [stabilise/soften cycle](./stabilisation.md) is the safety valve: if new requirements reveal that you committed to the wrong interpretation, soften back to an underspecified spec and let the LLM handle it until a better pattern emerges.

[Oracle strength](./oracle-strength-spectrum.md) determines what can crystallise. Operations with hard oracles (the output is unambiguously right or wrong) are natural candidates. Operations with weak oracles (correctness requires judgment) resist crystallisation — you can stabilise them within natural language but can't cross the medium boundary.

## Crystallisation as distillation

Crystallisation can also be [distillation](./distillation.md) — targeted extraction where the target is "runs fast and cheap." This codebase demonstrates the pattern: methodology notes describe how to validate frontmatter — required fields, description quality criteria, type enums, status values. Those get distilled into the `/validate` skill (methodology → procedure, staying in natural language). Then someone notices that some checks are purely mechanical — does the description field exist? Is the type value in the valid enum? Those checks get crystallised into a Python validation script.

The script is both crystallised and distilled. An earlier version included LLM-based checks (like whether the description matches the note's content), but those were dropped — not because they weren't useful, but because the target was a quick, cheap check you can run constantly. The target selected what to extract. A different distillation targeting thorough review would keep the LLM checks and produce a different artifact from the same source. The methodology notes remain as the common pool serving both targets.

The same pattern produced `generate_notes_index.py`: methodology notes describe when to create indexes, how to format entries, what editorial context to include. The script crystallises only the mechanical part. Curated area indexes stay in natural language because they require judgment about grouping and context.

Not every crystallisation is distillation. One-shot crystallisation — directly translating a spec into code with no larger body of reasoning behind it — is pure stabilisation. But when crystallisation draws on accumulated methodology or practice, it's both operations at once: extracting the automatable subset (distillation) and committing it to a deterministic medium (stabilisation at its extreme).

## Other examples

Replacing an LLM slug generator with `python-slugify`; moving CSV statistics from LLM arithmetic to Python's `statistics` module. In each case, the operation had a single correct interpretation that was being re-discovered by the LLM on every run.

Not crystallisation: writing a convention (stabilisation — constrains the interpretation space without changing medium); extracting a skill from methodology notes (distillation — targeted extraction, stays in natural language).

---

Relevant Notes:

- [stabilisation](./stabilisation.md) — parent mechanism: crystallisation is the far end of the stabilisation spectrum
- [distillation](./distillation.md) — orthogonal mechanism: targeted extraction; crystallisation sometimes follows distillation (extract a procedure, then crystallise it to code)
- [deploy-time learning](./deploy-time-learning-the-missing-middle.md) — the verifiability gradient across which crystallisation sits at the far end
- [spec-mining-as-crystallisation](./spec-mining-as-crystallisation.md) — the operational mechanism: observe behavior, extract patterns, write deterministic code
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — determines what can crystallise: hard oracles enable it, weak oracles resist it
- [Harness Engineering (Lopopolo, 2026)](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — exemplifies: encoding quality standards into linters that replace manual judgment is crystallisation at production scale

Topics:

- [learning-theory](./learning-theory.md)
