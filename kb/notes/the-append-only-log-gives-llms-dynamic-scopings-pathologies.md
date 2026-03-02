---
description: The flat conversation log is dynamic scoping — everything is visible to everything, context accumulates globally, producing the same pathologies (spooky action at a distance, name collision, inability to reason locally) that Lisp communities spent decades moving away from
type: note
traits: []
areas: [computational-model]
status: seedling
---

# The append-only log gives LLMs dynamic scoping's pathologies

In dynamically scoped Lisp, a function sees whatever bindings happen to be on the call stack at runtime, regardless of where the function was defined. The flat conversation log works the same way: every message the LLM processes is "in scope," including irrelevant earlier turns, abandoned reasoning paths, user corrections that shouldn't be internalized as instructions, and tool outputs from completed sub-tasks. The problems are identical to dynamic scoping's classic failures:

**Spooky action at a distance.** An early turn subtly biases a later response. The LLM has no mechanism to mark a binding as out of scope — once something enters the log, it influences everything downstream. This is the [three-space memory claim's](./three-space-memory-separation-predicts-measurable-failure-modes.md) "operational debris pollutes search" failure mode, restated as a scoping problem.

**Name collision.** The word "table" meant an HTML element in turn 3 but a database table in turn 12, and the model conflates them. In a flat log there are no scope boundaries to disambiguate — every use of a term is in the same namespace.

**Inability to reason locally.** You cannot predict what a sub-task will do by reading its prompt alone, because its behavior depends on the entire accumulated history. This is the defining problem of dynamic scope: the meaning of a name depends on the call stack, not the definition site.

## The mapping is structural

In both cases:
- Bindings accumulate at runtime rather than being declared at definition time
- Every consumer sees the full accumulated environment, not a curated subset
- There is no mechanism for a sub-computation to limit what it inherits
- Debugging requires inspecting the full runtime history, not just the local code

The [context window as homoiconic medium](./llm-context-is-a-homoiconic-medium.md) makes this worse: instructions and data share the same representation, so there isn't even a type-level distinction between "this is a binding the sub-task should see" and "this is leftover from an earlier computation."

## What flat logs buy

Dynamic scoping survived in Emacs Lisp for decades because it has a real advantage: implicit communication. Functions can influence each other without explicit parameter passing. The flat log has the same property. When a user says "use a more formal tone" in turn 5, they want that to implicitly affect all subsequent turns without re-parameterizing anything. That's dynamic binding of a `*tone*` special variable, and it works precisely because the log is flat and globally visible.

The right model isn't "always avoid flat logs" but rather what Common Lisp settled on: [lexical scope by default, dynamic scope when explicitly requested](./llm-context-is-composed-without-scoping.md) — but within a single context there is no scoping at all, only weak conventions. One architectural response is [automatic context injection](./agent-statelessness-means-harness-should-inject-context-automatically.md) — the harness constructs curated frames instead of exposing the full accumulated environment, addressing dynamic scoping's pathologies by curating what enters scope.

---

Relevant Notes:
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — the resolution: sub-agents provide isolation through lexically scoped frames; within a single context, only weak conventions exist
- [llm context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — amplifies: instructions and data sharing the same medium means scoping failures have no type-level guardrails
- [three-space memory separation predicts measurable failure modes](./three-space-memory-separation-predicts-measurable-failure-modes.md) — the failure modes (search pollution, identity scatter, insight trapping) are symptoms of dynamic scoping applied to memory
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: the semantic boundary model explains why scope contamination matters — underspecified instructions are sensitive to everything in context
- [agent statelessness means the harness should inject context automatically](./agent-statelessness-means-harness-should-inject-context-automatically.md) — addresses: automatic context injection constructs curated frames rather than exposing the accumulated environment, attacking dynamic scoping at the architecture level

Topics:
- [computational-model](./computational-model.md)
