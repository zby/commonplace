---
description: A model can possess knowledge yet fail to activate it in a given context; high-utility knowledge often fails to surface without explicit retrieval scaffolds
type: note
traits: [has-external-sources]
tags: [llm-interpretation-errors, failure-modes, evaluation]
status: seedling
---

# Knowledge possession does not imply contextual activation

A model can contain relevant knowledge and still fail to surface it when it matters. Possession and activation are distinct.

The operative distinction is not *knows* vs. *does not know* — it is *stored* vs. *elicited in this context*.

For candidate insight `x` and context `c`, define:

- `R_x`: retrievability under direct probing ("can it produce x when explicitly asked?")
- `A_x(c)`: spontaneous activation in context `c` ("will x surface without explicit request?")
- `U_x(c)`: utility in context `c` ("would surfacing x materially improve the outcome?")

Activation failure is the regime where `R_x` is high, `A_x(c)` is low, and `U_x(c)` is high.

## Why this happens

Activation requires more than stored capability:

1. **Cue match** -- current context must hit the right retrieval cues.
2. **Priority arbitration** -- activated candidates compete for limited reasoning budget.
3. **Commitment** -- the model must decide to externalize the candidate insight.

Most "model can do X" demonstrations pre-supply these stages by asking directly for `X`. They test execution after activation, not activation itself.

## Human analogue: inspiration

Humans show the same structure. Successful late activation is "inspiration" — the right cue arrangement brings available knowledge into working attention. The negative form is ordinary too: "I knew this, but it didn't occur to me."

This is not a uniquely LLM pathology — it is a general bounded-reasoner retrieval problem. LLM systems make it more operationally visible because prompt context is an explicit control surface.

## Measurement implication

For any target insight class `x`, evaluate both:

1. **Probed condition:** explicitly query for `x` (estimates `R_x`).
2. **Open condition:** broad task where `x` is useful but unrequested (estimates `A_x(c)` when `U_x(c)` is high).

Report the activation gap: high probe success with low open emergence.

## Design implication

If activation is unreliable, do not rely on spontaneous recall of high-utility knowledge. Add retrieval scaffolds:

- mandatory perspective passes
- explicit failure-mode probes
- structured assumption and escalation checks
- staged review prompts that force cue diversity

This complements discrimination/oracle theory: a strong checker is still useless if it is never triggered.

## Open questions

- Which scaffold designs increase `A_x(c)` without unacceptable token/runtime cost?
- Can memory raise activation reliability, or mostly improve post-activation execution?
- Which insight classes are activation-limited vs. execution-limited in practice?

---

Relevant Notes:

- [the-augmentation-automation-boundary-is-discrimination-not-accuracy](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — complements: distinguishes per-instance correctness discrimination from aggregate accuracy; this note adds the prior activation requirement
- [evaluation-automation-is-phase-gated-by-comprehension](./evaluation-automation-is-phase-gated-by-comprehension.md) — parallels: both require stage separation instead of aggregate score reading
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — enables: retrieval scaffolds are oracle-hardening moves for activation-limited settings
- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: prompt context determines which interpretations are activated
- [silent-disambiguation-is-the-semantic-analogue-of-tool-fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — example: low activation of critical branches can be masked by superficially successful outputs
- [the-bug-that-shipped-2035319413474206122](../sources/the-bug-that-shipped-2035319413474206122.md) — evidence: deployment-failure insights retrievable on probe but often absent in undirected review
- [towards-a-science-of-ai-agent-reliability](../sources/towards-a-science-of-ai-agent-reliability.md) — context: reliability dimensions motivate separating stored capability from operationally activated behavior
