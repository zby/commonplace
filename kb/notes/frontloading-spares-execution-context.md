---
description: Pre-computing static parts of LLM instructions and inserting results spares execution context — the primary bottleneck in instructing LLMs; the mechanism is partial evaluation applied to instructions with underspecified semantics
type: note
traits: [has-external-sources]
areas: [claw-design]
status: seedling
---

# Frontloading spares execution context

When instructing LLMs, any part of the instructions whose inputs are known before the LLM runs should be computed beforehand and the result inserted directly. This spares execution context — the primary bottleneck in LLM-based systems.

[Indirection elimination](./indirection-is-costly-in-llm-instructions.md) and [build-time generation](./generate-instructions-at-build-time.md) involve frontloading, though they also involve [crystallisation](./crystallisation.md) — the pre-computed result happens to be deterministic, so both principles apply simultaneously.

## Why execution context is the bottleneck

The execution context — the total content the LLM processes in a session — is the most important limiting factor in instructing LLMs:

- **Finite window.** Context has a hard token limit. Every token spent on derivable information is a token unavailable for the actual task.
- **Attention degradation.** Even within the window, more content means weaker attention to any given part. Instructions compete with each other.
- **Interpretation cost.** Procedural instructions ("first do X, then use the result to do Y") cost more than their results ("here is Z"). The LLM must parse, understand, and execute the procedure — or just receive the answer.

The cost asymmetry is dramatic: a shell command that takes milliseconds and produces a definite result replaces an instruction that the LLM must interpret on every invocation, potentially differently each time. The context window is scarce; external computation is abundant.

## What qualifies for frontloading

The test: can this be computed without the LLM's runtime state (the conversation, the user's query, the evolving task)?

**Static (frontloadable):**
- Variable resolution — paths, project names, configuration values known at setup time (the [indirection elimination](./indirection-is-costly-in-llm-instructions.md) case)
- File listings — "here are the files in `kb/notes/`" rather than "list the files in `kb/notes/`"
- Search results — pre-run a search and include results rather than instructing the LLM to search
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

Template expansion with `{{claw_root}}` → `project_claw/` is textbook PE. The [generate-at-build-time](./generate-instructions-at-build-time.md) note describes a specialiser for skill templates.

### Where the PE definition stretches

Standard PE assumes precise denotational semantics — `[[P]]` has an exact meaning and the equivalence is exact. LLM instructions differ:

**1. The "program" has underspecified semantics.** Natural language instructions don't have precise denotations. This is the property that [distinguishes LLM-based systems from traditional programming](./agentic-systems-interpret-underspecified-instructions.md). There is no exact `[[P]]` — the instruction admits a space of valid interpretations.

**2. Equivalence is approximate.** Replacing "list the files in kb/notes/" with an actual file listing is *probably* equivalent, but the LLM might have done something slightly different if it ran the listing itself.

**3. The optimisation target is context, not time.** Standard PE makes the residual faster. Here the gain is freeing context window and improving reliability by removing interpretation steps.

The stretches matter for understanding the mechanism, but not for the context-sparing benefit. Frontloading saves context regardless of whether the pre-computed result is deterministic (a file listing) or still underspecified when the LLM reads it (a pre-computed summary). The savings come from removing the *procedure* from context, not from changing the *semantics* of the result. Frontloading is not stabilisation — it doesn't require moving from underspecified to precise semantics. It may happen to do so (variable resolution produces a literal), but that's incidental.

---

Relevant Notes:
- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — overlaps: variable resolution is both frontloading (spares context) and [crystallisation](./crystallisation.md) (replaces underspecified template with deterministic literal)
- [generate instructions at build time](./generate-instructions-at-build-time.md) — overlaps: template expansion is both frontloading and crystallisation; the notes already link to stabilisation for the semantic-commitment aspect
- [CLAUDE.md is a router, not a manual](./context-loading-strategy.md) — motivates: the context loading hierarchy is one response to execution context being the bottleneck
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — context: the underspecified semantics of LLM instructions is the domain PE operates in here; frontloading is not stabilisation — it spares context regardless of whether the result is deterministic or still underspecified

Topics:
- [claw-design](./claw-design.md)
