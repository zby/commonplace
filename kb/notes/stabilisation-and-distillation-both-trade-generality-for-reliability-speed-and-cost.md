---
description: Both learning mechanisms — stabilisation (constraining) and distillation (extracting) — sacrifice generality for compound gains in reliability, speed, and cost; they differ in the operation and how much compound they yield
type: note
traits: []
status: current
areas: [learning-theory]
---

# Stabilisation and distillation both trade generality for reliability, speed, and cost

[Capacity decomposes into generality and a compound](./learning-is-not-only-about-generality.md) of reliability, speed, and cost. The two learning mechanisms — [stabilisation](./stabilisation.md) and [distillation](./distillation.md) — both operate on this trade-off, but through different operations.

## The trade-off in action

An LLM can multiply numbers. A calculator can multiply numbers. The calculator has far more capacity for multiplication — it never hallucinates 7×8=54, it handles arbitrarily large numbers, it runs in microseconds. But the LLM has more generality — it can also translate, summarise, write prose.

This is the trade-off made concrete. Moving from the LLM to the calculator sacrifices generality for a dramatic gain in the compound: reliability (never wrong), speed (microseconds), and cost (free). These three dimensions move together because the substrate changes — from stochastic LLM to deterministic code.

## How stabilisation trades generality for compound

[Stabilisation](./stabilisation.md) constrains the interpretation space. Each constraint narrows what the system can do (less generality) but makes what it does do more reliable, faster, and cheaper.

[Crystallisation](./crystallisation.md) — the far end of the stabilisation spectrum — is the most dramatic compound gain. Replacing an LLM validation check with a Python script doesn't change *what* gets checked — it changes how reliably (never hallucinates), how fast (milliseconds vs seconds), and how cheaply (free vs API call) it gets checked. What you give up is generality: the script handles exactly what it handles, nothing more.

But the compound isn't exclusive to crystallisation. Stabilisation short of crystallisation (storing outputs, writing conventions) also improves reliability and speed, just less dramatically. The full stabilisation spectrum trades generality at every point — crystallisation is just where the compound gain is largest because the medium itself changes.

## How distillation trades generality for compound

[Distillation](./distillation.md) extracts from a larger body of reasoning into a focused artifact shaped by a specific use case, context budget, or agent. The extracted artifact is narrower than the source (less generality) but operationally more efficient (compound gain).

A skill distilled from fifteen methodology notes fits in a single context window (speed, cost) and delivers consistent procedure (reliability). The methodology notes remain for edge cases — the distilled skill can't handle everything they cover. This is the same trade-off: generality for compound, through extraction rather than constraint.

## The mechanisms differ in operation

| | Stabilisation | Distillation |
|---|---|---|
| **Operation** | Constrain — narrow the interpretation space | Extract — select and compress from a larger body |
| **What changes** | The same artifact becomes more constrained | A new, focused artifact is produced from a larger source |
| **Medium transition** | Ranges from none (conventions) to full (crystallisation) | Typically none — stays in natural language |
| **Compound yield** | Highest at crystallisation (substrate change) | Moderate — speed and cost gains from reduced context |

Both directions are [capacity change](./learning-is-not-only-about-generality.md). The reverse — softening a stabilised component, or loading the full source instead of the distillate — trades compound back for generality.

---

Relevant Notes:

- [learning is not only about generality](./learning-is-not-only-about-generality.md) — foundation: defines the capacity decomposition (generality vs compound) that this note's trade-off operates on
- [stabilisation](./stabilisation.md) — one mechanism: constrains the interpretation space; crystallisation is the far end
- [distillation](./distillation.md) — the other mechanism: targeted extraction under context budget constraints
- [crystallisation](./crystallisation.md) — where stabilisation yields the largest compound gain, because the substrate itself changes
- [bitter lesson boundary](./bitter-lesson-boundary.md) — determines when the generality-vs-compound trade-off is permanent (calculators) vs when softening is needed (vision features)

Topics:

- [learning-theory](./learning-theory.md)
