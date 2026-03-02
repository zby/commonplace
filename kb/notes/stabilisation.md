---
description: Definition — stabilisation is any act that narrows the space of valid interpretations an underspecified spec admits, trading generality for gains in reliability, speed, and cost — from same-medium narrowing to full crystallisation (medium change)
type: note
traits: []
areas: [learning-theory]
status: current
---

# Stabilisation

The learning mechanism where the space of valid interpretations is narrowed. Storing an LLM output, writing a convention, adding structured sections to a document type, sharpening a description, extracting a deterministic function — all are stabilisation. What's being narrowed is the [semantic underspecification](./agentic-systems-interpret-underspecified-instructions.md) — the range of interpretations the spec admits — not just execution variance. Stabilisation ranges from same-medium narrowing (a better description field) to full medium change ([crystallisation](./crystallisation.md) — the most dramatic form).

Stabilisation is the broadest of the three mechanisms and includes the smallest acts of learning. It starts before crystallisation and covers acts that never need to crystallise — a well-written description field is stabilised (findable, predictable) but will never become code.

Softening — replacing a stabilised component with a general-purpose one — is the reverse. It increases generality at the cost of the compound. The stabilise/soften cycle is a learning cycle.

Examples: storing an LLM output as a permanent artifact; writing a description field that enables search; creating a naming convention; adding structured sections to a document type.

Not stabilisation: extracting a skill from methodology notes (distillation — the operation is extraction, not narrowing).

See [agentic systems learn through three distinct mechanisms](./agentic-systems-learn-through-three-distinct-mechanisms.md) for the full vocabulary.

---

Relevant Notes:
- [crystallisation](./crystallisation.md) — sibling mechanism: the phase transition to code; the most dramatic form of stabilisation
- [distillation](./distillation.md) — sibling mechanism: extracts procedures from reasoning
- [agentic systems learn through three distinct mechanisms](./agentic-systems-learn-through-three-distinct-mechanisms.md) — the umbrella note defining all three
- [storing LLM outputs is stabilisation](./storing-llm-outputs-is-stabilization.md) — the simplest instance
- [methodology enforcement is stabilisation](./methodology-enforcement-is-stabilisation.md) — stabilisation applied to methodology: instruction → skill → hook → script

Topics:
- [learning-theory](./learning-theory.md)
