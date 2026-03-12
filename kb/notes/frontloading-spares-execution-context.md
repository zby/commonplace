---
description: Pre-computing static parts of LLM instructions and inserting results spares execution context — the primary bottleneck in instructing LLMs; the mechanism is partial evaluation applied to instructions with underspecified semantics
type: note
traits: [has-external-sources]
areas: [kb-design]
status: seedling
---

# Frontloading spares execution context

When instructing LLMs, any part of the instructions whose inputs are known before the LLM runs should be computed beforehand and the result inserted directly. This spares execution context — the primary bottleneck in LLM-based systems.

## The context saving

[Context is the central scarce resource in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md). Frontloading addresses the complexity dimension of that scarcity: executing a procedure inside a bounded call costs more context than inserting its result. The procedure text itself may be small — "search for X in `kb/notes/`" is a single line — but execution generates artifacts that persist in the context window: tool calls, search results, reasoning traces, interpretation. All of that competes with the work that actually needs the LLM's judgment. A pre-computed listing costs only the bytes of the listing itself; the same listing produced at runtime costs the instruction, the tool call, the full output, and the LLM's interpretation of it — on every invocation.

## What qualifies for frontloading

The test: can this be computed without the LLM's runtime state (the conversation, the user's query, the evolving task)?

**Static (frontloadable):**
- Variable resolution — paths, project names, configuration values known at setup time (the [indirection elimination](./indirection-is-costly-in-llm-instructions.md) case)
- File listings — "here are the files in `kb/notes/`" rather than "list the files in `kb/notes/`"
- Aggregations — counts, summaries of known datasets, pre-computed indexes
- Template expansion — [build-time generation](./generate-instructions-at-build-time.md) of skills and instructions

Anything that depends on the user's current request, the conversation state, or the evolving task is dynamic and not frontloadable. The boundary isn't always sharp — some sub-procedures depend partially on known and partially on runtime information. In those cases, frontload the known parts and leave the runtime-dependent parts as instructions.

## Frontloading vs codification

[Indirection elimination](./indirection-is-costly-in-llm-instructions.md) and [build-time generation](./generate-instructions-at-build-time.md) are common cases of frontloading. In those cases the pre-computed result happens to be deterministic, so frontloading and [codification](./codification.md) (committing to a single deterministic output) apply simultaneously. But frontloading does not require determinism — the context saving comes from replacing derivation with insertion, whether the result is deterministic or still underspecified.

## The mechanism: partial evaluation or divide-and-conquer?

Frontloading looks like divide-and-conquer: solve a subproblem, pass the result to the next stage. Any system does this. But in LLM instruction systems, frontloading can also be viewed through the lens of partial evaluation.

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

### Where the PE analogy stretches

Standard PE assumes precise denotational semantics, exact equivalence, and time as the optimisation target. LLM instructions differ on all three points:

- The "program" has [underspecified semantics](./agentic-systems-interpret-underspecified-instructions.md), so there is no exact `[[P]]`
- Replacing a procedure with its result is only approximately equivalent
- The gain is context and reliability, not runtime speed

Those differences matter for theory, but not for the practical benefit. Frontloading saves context by removing procedures from the bounded LLM call. The homoiconicity of the medium is what makes the PE framing precise rather than merely metaphorical — without it, "pre-compute and insert" would be just divide-and-conquer.

## Relationship to the scheduling model

The [symbolic scheduling model](./bounded-context-orchestration-model.md) models frontloading as the single-step case of its separation between symbolic computation and bounded LLM calls: pre-compute what can be known, reserve the bounded call for what requires judgment.

---

Relevant Notes:

- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — overlaps: variable resolution is both frontloading (spares context) and [codification](./codification.md) (replaces underspecified template with deterministic literal)
- [generate instructions at build time](./generate-instructions-at-build-time.md) — overlaps: template expansion is both frontloading and codification; the notes already link to constraining for the semantic-commitment aspect
- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: frontloading addresses the complexity dimension of context scarcity
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — motivates: the context loading hierarchy is one response to execution context being the bottleneck
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — context: the underspecified semantics of LLM instructions is the domain PE operates in here
- [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — enables: homoiconicity is what makes frontloading partial evaluation rather than just divide-and-conquer — the pre-computed result re-enters the instruction stream without format conversion
- [symbolic scheduling over bounded LLM calls is the right model for agent orchestration](./bounded-context-orchestration-model.md) — models: frontloading is the single-step case of the scheduling model's separation between symbolic computation and bounded LLM calls

Topics:

- [kb-design](./kb-design.md)
