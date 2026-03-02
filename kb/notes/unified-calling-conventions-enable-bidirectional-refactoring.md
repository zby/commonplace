---
description: When agents and tools share a calling convention, components can move between neural and symbolic without changing call sites — llm-do demonstrates this with name-based dispatch over a hybrid VM
type: note
traits: [has-external-sources]
areas: [learning-theory]
status: current
---

# Unified calling conventions enable bidirectional refactoring between neural and symbolic

The [underspecified instructions framing](./agentic-systems-interpret-underspecified-instructions.md) says components should move between underspecified (LLM-interpreted) and precise (code) semantics as systems evolve — stabilise patterns to code, soften rigid code back to LLM. But the framing doesn't say how to make the boundary movable in practice. The answer is a unified calling convention: if neural and symbolic components present the same interface, callers don't need to know which they're talking to, and refactoring across the boundary becomes a local operation.

## The mechanism

[llm-do](https://github.com/zby/llm-do) implements this through a hybrid VM where agents (`.agent` files, LLM-backed) and tools (Python functions) share a single namespace. The LLM sees both as callable functions. A call to `ticket_classifier` might dispatch to an agent today and a Python function tomorrow — the prompt that invokes it doesn't change.

This requires **name-based dispatch**: components are identified by string name rather than direct object reference. Names enable dynamic resolution (the LLM outputs a string, the runtime looks it up), late binding (the callee needn't exist when the caller is defined), and implementation-agnostic interfaces (the same name can resolve to either neural or symbolic).

```
Agent ──calls──▶ Tool ──calls──▶ Agent ──calls──▶ Tool ...
neural          symbolic         neural          symbolic
```

The calling convention is uniform across the chain. Each link can be independently refactored without disturbing the rest.

## Why this matters for stabilisation

[Stabilisation](./stabilisation.md) and [crystallisation](./crystallisation.md) describe the learning mechanisms — narrowing distributions, changing medium. But without a unified interface, each crystallisation step is a breaking change: call sites must be updated, prompt structure must change, the agent's view of available operations shifts. This friction discourages incremental refactoring and pushes toward big-bang rewrites.

With unified calling, the progression is smooth:

1. **Start neural** — define an agent to handle a task. Quick to add, handles ambiguity.
2. **Observe patterns** — the agent consistently lowercases and replaces spaces with underscores. This is [spec-mining](./spec-mining-as-crystallisation.md) — discovering that an underspecified spec consistently resolves to one interpretation, then committing to it in code.
3. **Crystallise** — extract `sanitize_filename()` to Python. The agent still handles ambiguous cases. The call site doesn't change.
4. **Extend via softening** — new requirements emerge (handle Unicode, detect dates). Add an LLM call for the new cases. Again, the call site doesn't change.

Each step is local. The system evolves without coordination cost.

## The harness layer

On top of the hybrid VM, llm-do adds an imperative harness — Python code that owns control flow rather than a graph DSL. This is a deliberate contrast with declarative agent frameworks (LangGraph, CrewAI) where orchestration is defined as node-edge graphs.

| Aspect | Graph DSLs | llm-do Harness |
|--------|------------|----------------|
| Orchestration | Declarative: Node A → Node B | Imperative: Agent A calls Agent B as a function |
| State | Global context through graph | Local scope — each agent gets only its arguments |
| Refactoring | Redraw edges, update graph | Change code — extract functions, inline agents |
| Control flow | DSL constructs | Native Python: `if`, `for`, `try/except` |

The imperative style means refactoring between neural and symbolic uses the same patterns as normal code refactoring — extract function, inline, rename. No graph topology to update.

## The connection to typed callables

[Instructions are typed callables](./instructions-are-typed-callables.md) argues that prompts, skills, and tools share a callable structure with typed inputs and outputs. llm-do operationalises this: `.agent` files are YAML frontmatter (type signature) plus system prompt (implementation), and tools are Python functions with type annotations. Both are callables with defined interfaces. The unified calling convention is what makes the type-theoretic view practical rather than just analogical.

## Open Questions

- Does unified calling break down at scale, when the namespace grows to hundreds of components and name collisions become likely?
- How does debugging work when a call chain crosses the neural-symbolic boundary multiple times — do existing observability tools handle this, or does the hybrid VM need its own tracing?
- Is the imperative harness pattern specific to Python, or does it transfer to other host languages?

---

Relevant Notes:
- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: the underspecified instructions framing that this note makes architecturally concrete
- [stabilisation](./stabilisation.md) — the mechanism that unified calling makes frictionless
- [crystallisation](./crystallisation.md) — the phase transition from neural to symbolic that unified calling makes a local operation
- [spec-mining-as-crystallisation](./spec-mining-as-crystallisation.md) — the operational mechanism: observe agent behavior, extract to code — enabled by stable call sites
- [instructions-are-typed-callables](./instructions-are-typed-callables.md) — the type-theoretic view that llm-do operationalises
- [programming-practices-apply-to-prompting](./programming-practices-apply-to-prompting.md) — extends: extract-function and inline refactoring transfer directly when calling conventions are unified

Topics:
- [learning-theory](./learning-theory.md)
