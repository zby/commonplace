---
description: Pre-computing static parts of LLM instructions and inserting results spares execution context — the primary bottleneck in instructing LLMs; the mechanism is partial evaluation applied to instructions with underspecified semantics
type: note
traits: [has-external-sources]
areas: [kb-design]
status: seedling
---

# Frontloading spares execution context

When instructing LLMs, any part of the instructions whose inputs are known before the LLM runs should be computed beforehand and the result inserted directly. This spares execution context — the primary bottleneck in LLM-based systems.

## Why execution context is the bottleneck

Procedures consume more context than their results. A procedure carries parsing overhead, error-handling branches, and step-by-step reasoning that collapse to a compact output. An instruction like "list the files in `kb/notes/`" costs the LLM a tool call, the round-trip, and the interpretation of the result — on every invocation. The pre-computed listing costs only the bytes of the listing itself, once.

This asymmetry is general: whenever a sub-procedure's inputs are known before the LLM runs, the procedure is pure overhead inside bounded context. For the broader cost model, see [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md).

[Indirection elimination](./indirection-is-costly-in-llm-instructions.md) and [build-time generation](./generate-instructions-at-build-time.md) are common cases of frontloading. In those cases the pre-computed result happens to be deterministic, so frontloading and [crystallisation](./crystallisation.md) (committing to a single deterministic output) apply simultaneously. But frontloading does not require determinism — the context saving comes from replacing derivation with insertion, whether the result is deterministic or still underspecified.

## What qualifies for frontloading

The test: can this be computed without the LLM's runtime state (the conversation, the user's query, the evolving task)?

**Static (frontloadable):**
- Variable resolution — paths, project names, configuration values known at setup time (the [indirection elimination](./indirection-is-costly-in-llm-instructions.md) case)
- File listings — "here are the files in `kb/notes/`" rather than "list the files in `kb/notes/`"
- Aggregations — counts, summaries of known datasets, pre-computed indexes
- Template expansion — [build-time generation](./generate-instructions-at-build-time.md) of skills and instructions

Anything that depends on the user's current request, the conversation state, or the evolving task is dynamic and not frontloadable. The boundary isn't always sharp — some sub-procedures depend partially on known and partially on runtime information. In those cases, frontload the known parts and leave the runtime-dependent parts as instructions.

## The mechanism: partial evaluation

Frontloading is partial evaluation applied to a domain where the "program" being specialised has [underspecified semantics](./agentic-systems-interpret-underspecified-instructions.md).

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

Those differences matter for theory, but not for the practical benefit. Frontloading saves context by removing procedures from the bounded LLM call.

## Relationship to the scheduling model

Frontloading is a special case of the [symbolic scheduling model](./symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration.md). In that model, the scheduler performs whatever work can be done before the current bounded call — often symbolically and exactly, but frontloading also covers precomputed results that remain underspecified. Frontloading is the single-step version: pre-compute what can be known, insert the result, and let the LLM focus on what requires judgment. The scheduling model generalises this to multi-step orchestration where the scheduler iteratively builds state and issues bounded calls.

---

Relevant Notes:
- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — overlaps: variable resolution is both frontloading (spares context) and [crystallisation](./crystallisation.md) (replaces underspecified template with deterministic literal)
- [generate instructions at build time](./generate-instructions-at-build-time.md) — overlaps: template expansion is both frontloading and crystallisation; the notes already link to stabilisation for the semantic-commitment aspect
- [CLAUDE.md is a router, not a manual](./context-loading-strategy.md) — motivates: the context loading hierarchy is one response to execution context being the bottleneck
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — context: the underspecified semantics of LLM instructions is the domain PE operates in here
- [symbolic scheduling over bounded LLM calls is the right model for agent orchestration](./symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration.md) — subsumes: frontloading is the single-step case of the scheduling model's separation between symbolic computation and bounded LLM calls

Topics:
- [kb-design](./kb-design.md)
