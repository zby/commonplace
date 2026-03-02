---
description: Definition — crystallisation is the phase transition from natural language instructions to executable code, changing medium, consumer, and verification regime
type: note
traits: []
areas: [learning-theory]
status: current
---

# Crystallisation

The learning mechanism where natural language instructions become executable code. The medium changes (markdown → Python/script), the consumer changes (LLM → interpreter/runtime), and the verification regime changes (underspecified semantics → precise semantics, indeterministic → deterministic). It is a phase transition — the nature of the artifact changes fundamentally.

Crystallisation produces the largest compound gain in reliability, speed, and cost because it removes the LLM from the loop entirely for the crystallised operation. The trade-off is generality: the code handles exactly what it handles, nothing more.

Examples: replacing an LLM slug generator with `python-slugify`; moving CSV statistics from LLM arithmetic to Python's `statistics` module; converting a skill-level validation check into a Python script.

Not crystallisation: writing a convention (stabilisation — same medium, more committed interpretation); extracting a skill from methodology notes (distillation — same medium, different rhetorical mode).

See [agentic systems learn through three distinct mechanisms](./agentic-systems-learn-through-three-distinct-mechanisms.md) for the full vocabulary and [deploy-time learning](./deploy-time-learning-the-missing-middle.md) for the verifiability gradient.

---

Relevant Notes:
- [stabilisation](./stabilisation.md) — sibling mechanism: narrows the interpretation space without changing medium
- [distillation](./distillation.md) — sibling mechanism: extracts procedures from reasoning without changing medium
- [agentic systems learn through three distinct mechanisms](./agentic-systems-learn-through-three-distinct-mechanisms.md) — the umbrella note defining all three
- [deploy-time learning](./deploy-time-learning-the-missing-middle.md) — the verifiability gradient across which crystallisation sits at the far end
- [spec-mining-as-crystallisation](./spec-mining-as-crystallisation.md) — the operational mechanism: observe behavior, extract patterns, write deterministic code

Topics:
- [learning-theory](./learning-theory.md)
