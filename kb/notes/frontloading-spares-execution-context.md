---
description: Pre-computing static parts of LLM instructions and inserting results spares execution context — the primary bottleneck in instructing LLMs; the mechanism is partial evaluation applied to instructions with underspecified semantics
type: note
traits: [has-external-sources]
areas: [kb-design]
status: seedling
---

# Frontloading spares execution context

When instructing LLMs, any part of the instructions whose inputs are known before the LLM runs should be computed beforehand and the result inserted directly. This spares execution context — the primary bottleneck in LLM-based systems.

[Indirection elimination](./indirection-is-costly-in-llm-instructions.md) and [build-time generation](./generate-instructions-at-build-time.md) involve frontloading, though they also involve [crystallisation](./crystallisation.md) — the pre-computed result happens to be deterministic, so both principles apply simultaneously.

## Why execution context is the bottleneck

The reason is simple: context is the scarce resource, and procedural instructions consume more of it than their results. A shell command that takes milliseconds and produces a definite result can replace an instruction the LLM would otherwise have to parse and execute on every invocation. For the broader cost model, see [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md).

## What qualifies for frontloading

The test: can this be computed without the LLM's runtime state (the conversation, the user's query, the evolving task)?

**Static (frontloadable):**
- Variable resolution — paths, project names, configuration values known at setup time (the [indirection elimination](./indirection-is-costly-in-llm-instructions.md) case)
- File listings — "here are the files in `kb/notes/`" rather than "list the files in `kb/notes/`"
- Aggregations — counts, summaries of known datasets, pre-computed indexes
- Template expansion — [build-time generation](./generate-instructions-at-build-time.md) of skills and instructions

**Dynamic (not frontloadable):**
- Anything that depends on the user's current request
- Judgments that require understanding the task context
- Searches whose query depends on the conversation

The boundary isn't always sharp — some sub-procedures depend partially on known and partially on runtime information. In those cases, frontload the known parts and leave the runtime-dependent parts as instructions.

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

Template expansion with `{{claw_root}}` → `commonplace/kb/` is textbook PE. The [generate-at-build-time](./generate-instructions-at-build-time.md) note describes a specialiser for skill templates.

### Where the PE analogy stretches

Standard PE assumes precise denotational semantics, exact equivalence, and time as the optimisation target. LLM instructions differ on all three points:

- The "program" has [underspecified semantics](./agentic-systems-interpret-underspecified-instructions.md), so there is no exact `[[P]]`
- Replacing a procedure with its result is only approximately equivalent
- The gain is context and reliability, not runtime speed

Those differences matter for theory, but not for the practical benefit. Frontloading saves context by removing procedures from the bounded LLM call. It is not the same as stabilisation: the frontloaded result may be deterministic or still underspecified; either way, the context saving comes from replacing derivation with insertion.

---

Relevant Notes:
- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — overlaps: variable resolution is both frontloading (spares context) and [crystallisation](./crystallisation.md) (replaces underspecified template with deterministic literal)
- [generate instructions at build time](./generate-instructions-at-build-time.md) — overlaps: template expansion is both frontloading and crystallisation; the notes already link to stabilisation for the semantic-commitment aspect
- [CLAUDE.md is a router, not a manual](./context-loading-strategy.md) — motivates: the context loading hierarchy is one response to execution context being the bottleneck
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — context: the underspecified semantics of LLM instructions is the domain PE operates in here; frontloading is not stabilisation — it spares context regardless of whether the result is deterministic or still underspecified
- [symbolic scheduling over bounded LLM calls is the right model for agent orchestration](./symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration.md) — extends: generalises single-step frontloading to a harness model where code holds exact state and LLM calls handle bounded semantic judgment

Topics:
- [kb-design](./kb-design.md)
