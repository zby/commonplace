---
description: Definition — distillation is the extraction of operational procedures from discursive reasoning, staying in the same medium but changing rhetorical mode from argumentative to procedural
type: note
traits: []
areas: [learning-theory]
status: current
---

# Distillation

The learning mechanism where a body of discursive reasoning (methodology notes, design arguments, source reviews) becomes operational procedure (skills). Both input and output are natural language consumed by an LLM — there is no phase transition. What changes is the rhetorical mode: exploratory, multi-perspective argument becomes step-sequenced instruction.

The separation is deliberate: reasoning is factored out of the operational path, not lost. The methodology KB remains accessible for edge cases the distilled skill doesn't cover. Distillation is a context-budget operation — it exists because loading the full reasoning every session is too expensive.

The distillate can't reconstruct the source. Someone reading only the skill can follow the steps but can't adapt them to novel situations. The reasoning that produced those steps is absent from the output.

Examples: the `/connect` skill distils the Toulmin argument structure, Notes Without Reasons review, title-as-claim convention, and link contracts framework into a step-by-step connection procedure.

Not distillation: moving a validation check to code (crystallisation — the medium changes); storing an LLM output (stabilisation — no extraction from reasoning involved).

See [skills derive from methodology through distillation](../claw-design/skills-derive-from-methodology-through-distillation.md) for the full argument and [agentic systems learn through three distinct mechanisms](./agentic-systems-learn-through-three-distinct-mechanisms.md) for the vocabulary.

---

Relevant Notes:
- [crystallisation](./crystallisation.md) — sibling mechanism: the phase transition to code
- [stabilisation](./stabilisation.md) — sibling mechanism: narrows distribution without changing medium
- [agentic systems learn through three distinct mechanisms](./agentic-systems-learn-through-three-distinct-mechanisms.md) — the umbrella note defining all three
- [skills derive from methodology through distillation](../claw-design/skills-derive-from-methodology-through-distillation.md) — the full argument for distillation as a distinct mechanism
- [agent statelessness makes skill layers architectural](../claw-design/agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md) — why distillation is architecturally necessary, not just convenient

Topics:
- [learning-theory](./learning-theory.md)
