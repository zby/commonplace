---
description: When agents and tools share a calling convention, components can move between neural and symbolic without changing call sites — llm-do illustrates this with name-based dispatch over a hybrid VM
type: types/note.md
traits: [has-external-sources, title-as-claim]
tags: [learning-theory, computational-model, constraining]
---

# A unified interface lets programmers choose prompts or code without changing callers

A caller uses the same name, arguments, and result format whether a prompt-backed agent or a function handles the call. An LLM caller also sees the same description of the operation. This is **information hiding**: the interface tells callers how to use the operation without making them depend on how the programmer implements it. The programmer can replace a prompt with code once a rule is clear, or put a prompt behind the same interface to try a different rule.

The claim answers a practical question. The [English account of prompting](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) treats an instruction as permitting a set of readings, from which an LLM executor produces one. It treats extracting a repeated operation into code as a separate intervention whose trade-off must be assessed. This note extends that into a premise of its own: components should move between underspecified (LLM-interpreted) and precise (code) semantics as systems evolve — constrain patterns to code, relax rigid code back to LLM. That premise doesn't say how to make the boundary movable in practice; the unified calling convention does.

## The mechanism

[llm-do](https://github.com/zby/llm-do) is a runtime in which LLM-backed agents and Python tools can call each other by name. The programmer binds `ticket_classifier` to an implementation: either a prompt-backed agent or a Python function. When the caller invokes `ticket_classifier`, the runtime looks up that binding. The programmer chooses the implementation for the run; the runtime does not decide ticket by ticket whether to use code or a model.

```
Agent ──calls──▶ Tool ──calls──▶ Agent ──calls──▶ Tool ...
neural          symbolic         neural          symbolic
```

## Scope

What stays unchanged is the call, not necessarily its effect. A classifier that returns the same queue labels can still send a ticket to a different queue. A caller that relied on the old decisions or error behavior needs testing after a swap. If the new implementation requires structured arguments instead of free text, even the call must change unless an adapter preserves the old interface.

## Why this matters for constraining

[Constraining](./definitions/constraining.md) and [codification](./definitions/codification.md) describe the learning mechanisms — narrowing the interpretation space, changing medium. But in a system that exposes agents and tools through different invocation surfaces, a codification step that moves a component from one surface to the other is a breaking change: call sites must be updated, prompt structure must change, and the agent's view of available operations shifts. This friction would likely discourage incremental refactoring and push toward big-bang rewrites. That effect is an expectation, not an observed result.

Suppose the team starts with a prompt for `ticket_classifier` while it learns how tickets should be assigned. By checking the agent's decisions against the queues that actually resolve the tickets, the team identifies a topic-based rule it wants to keep. This is [spec mining](./spec-mining-as-codification.md). If the team wants to keep the same routing behavior, replacing the prompt with a Python function is a refactoring: the programmer changes the implementation, not the rule. The programmer binds `ticket_classifier` to the function. Callers still supply a ticket and receive a queue label.

Later the team wants to try assigning tickets by the action the customer needs rather than by topic. The Python function still meets the old requirement. For a test run, the programmer binds `ticket_classifier` to a prompt instead. The team edits the prompt and compares assignments on the same sample tickets without implementing each candidate policy in Python. If that makes the alternatives quicker to test, the prompt has served its purpose even if the programmer puts the chosen rule back into code for production.

## The scheduler layer

On top of the hybrid VM, llm-do adds an imperative scheduler: Python code, not a graph DSL, owns control flow. This deliberately contrasts with graph-defined orchestration, such as LangGraph's, which defines orchestration as node-edge graphs.

| Aspect | Graph DSLs | llm-do Scheduler |
|--------|------------|----------------|
| Orchestration | Declarative: Node A → Node B | Imperative: Agent A calls Agent B as a function |
| State | Global context through graph | Local scope — each agent gets only its arguments |
| Refactoring | Redraw edges, update graph | Change code — extract functions, inline agents |
| Control flow | DSL constructs | Native Python: `if`, `for`, `try/except` |

## The connection to typed callables

[Instructions are typed callables](./instructions-are-typed-callables.md) argues that skills, tasks and workflows are callable in a limited sense: they take and return typed documents and can declare signatures, though a signature does not turn a natural-language procedure into a conventional function. This note extends that callable structure to tools. llm-do operationalises it: `.agent` files are YAML frontmatter (type signature) plus system prompt (implementation), and tools are Python functions with type annotations. The unified calling convention is what makes this callable view practical across the neural-symbolic boundary rather than just analogical.

## Open Questions

- Does unified calling break down at scale, when the namespace grows to hundreds of components and name collisions become likely?
- How does debugging work when a call chain crosses the neural-symbolic boundary multiple times — do existing observability tools handle this, or does the hybrid VM need its own tracing?
- Is the imperative scheduler pattern specific to Python, or does it transfer to other host languages?

---

Relevant Notes:

- Abstracted into: [RLM, Tendril, and llm-do place symbolic work at different persistence boundaries](./rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md)
- [Prompting changes failure diagnosis with the semantic reference](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — grounds: the English account, under which an instruction permits several readings, that this note makes architecturally concrete
- [constraining](./definitions/constraining.md) — the mechanism that unified calling makes frictionless
- [codification](./definitions/codification.md) — the phase transition from neural to symbolic that unified calling makes a local operation
- [spec-mining-as-codification](./spec-mining-as-codification.md) — the operational mechanism: observe agent behavior, extract to code — enabled by stable call sites
- [instructions-are-typed-callables](./instructions-are-typed-callables.md) — the type-theoretic view that llm-do operationalises
- [Programming practices for prompts need evidence matched to the question](./programming-practices-for-prompts-need-question-specific-evidence.md) — extends: extract-function and inline refactoring transfer directly when calling conventions are unified
- [operational-signals-that-a-component-is-a-relaxing-candidate](./operational-signals-that-a-component-is-a-relaxing-candidate.md) — extends: relaxing signals answer "when should you relax?" — unified calling makes the relaxing refactoring cheap once the signal fires
