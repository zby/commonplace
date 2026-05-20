---
description: The partial-evaluation framing for LLM frontloading is structurally precise, not metaphorical, because LLM context is a homoiconic medium; without homoiconicity, it would just be divide-and-conquer
type: kb/types/note.md
traits: []
tags: []
status: seedling
---

# Frontloading is partial evaluation, not divide-and-conquer

[Frontloading](./frontloading-spares-execution-context.md) — pre-computing static parts of an LLM instruction and inserting the result — looks like divide-and-conquer at first glance: solve a subproblem, pass the result to the next stage. Any system does this. But in LLM instruction systems, frontloading is more precisely viewed through the lens of partial evaluation, and the difference is not cosmetic.

The key: LLM context is a [homoiconic medium](./llm-context-is-a-homoiconic-medium.md). Instructions and data are both natural language tokens. When you pre-compute a file listing and insert it into an instruction, the result is still a valid instruction — you've specialised a program with respect to known inputs, producing a residual program in the same medium. That's partial evaluation, not just preprocessing. In a non-homoiconic system, the pre-computed result would need a format conversion to re-enter the instruction stream; here it flows in directly because everything is text.

Standard PE specialises a program P with respect to known **static** inputs s, producing a **residual program** Ps that needs only the remaining **dynamic** inputs d:

```
[[Ps]](d) = [[P]](s, d)
```

| PE concept | Frontloading equivalent |
|---|---|
| Program P | The instruction set (CLAUDE.md, skills, prompts) |
| Static inputs s | Everything known before the LLM runs (paths, file listings, config, search results over stable content) |
| Dynamic inputs d | The user's request, conversation state, evolving task |
| Residual program Ps | The frontloaded instructions — static sub-procedures replaced with their results |
| Binding-time analysis | The author's judgment about what depends on runtime context vs what doesn't |
| Specialisation | The build-time/setup-time step that produces concrete instructions |

Template variable expansion is textbook PE. The [generate-at-build-time](./generate-instructions-at-build-time.md) note describes a specialiser for skill templates.

## Where the analogy stretches

Standard PE assumes precise denotational semantics, exact equivalence, and time as the optimisation target. LLM instructions differ on all three points:

- The "program" has [underspecified semantics](./agentic-systems-interpret-underspecified-instructions.md), so there is no exact `[[P]]`
- Replacing a procedure with its result is only approximately equivalent
- The gain is context and reliability, not runtime speed

Those differences matter for theory, but not for the practical benefit. Frontloading saves context by removing procedures from the LLM call. The homoiconicity of the medium makes the PE framing structurally useful rather than a loose metaphor: it is precise about medium-preserving substitution, while semantic equivalence remains approximate. Without that shared text medium, "pre-compute and insert" would be just divide-and-conquer.

---

Relevant Notes:

- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — operational context: this note is the theoretical mechanism for the operational claim defended there
- [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — enabling property: homoiconicity is what makes the PE framing precise rather than metaphorical
- [Agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — caveat: the underspecified semantics of LLM instructions is the domain PE operates in here
- [Generate KB skills at build time, don't parameterise them](./generate-instructions-at-build-time.md) — instance: template expansion is textbook PE
- [Indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — instance: variable resolution is a PE specialisation step
- [Bounded-context orchestration model](./bounded-context-orchestration-model.md) — broader frame: the scheduling model treats frontloading as the single-step case
