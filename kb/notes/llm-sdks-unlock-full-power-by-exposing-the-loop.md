---
description: Tool calls harden execution, but full LLM leverage appears only when the SDK exposes the orchestration loop to the application layer so state and recursion live outside the conversation
type: note
traits: []
tags: [computational-model]
status: seedling
---

# LLM SDKs unlock full power by exposing the loop

LLM APIs with tool calling make it easy to confuse two different things: giving the model access to deterministic operations, and exposing orchestration to the application layer. The first is useful, but the second is the deeper architectural shift. This note is the SDK-design consequence of [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md): full LLM leverage appears only when the SDK exposes the loop rather than hiding it behind a chat abstraction or opaque `agent.run()` interface.

When the loop is exposed, the application layer can keep state outside the conversation, assemble fresh prompts, execute tools deterministically, and decide when to branch, retry, recurse, or terminate. The LLM can then be used where it is strongest: bounded semantic judgment under focused context. Relevance filtering, decomposition, synthesis, classification, and local planning all fit this shape. This preserves the [bounded-context orchestration model](./bounded-context-orchestration-model.md): semantic work stays in the LLM, bookkeeping stays on an exact substrate.

Exposure does **not** require every user to hand-write an imperative `while` loop. A loop can be exposed through ordinary application code, a declarative workflow DSL, a configurable state machine, or another explicit control surface. What matters is that state progression and recursion are inspectable and controllable outside the conversation, not that they take one particular programming form.

Tool calls alone do not achieve this. A chat loop that lets the model call tools but still relies on the conversation to remember partial progress, track branches, decide what remains, and reconstruct prior conclusions has only hardened the execution boundary. The scheduler is still inside bounded stochastic context. In that regime, tool calls save the model from doing file I/O mentally, but they do not save it from spending context on orchestration.

This is why "function calling is enough" is both true and false. It is true in the narrow sense that you do not need an elaborate agent framework to realise the clean model. A small application loop over an LLM API can do it, and so can higher-level workflow surfaces that still externalise progression. It is false in the stronger sense that turning on function calling inside a chat abstraction does not by itself recover the clean model. The decisive step is not the API feature; it is whether the SDK exposes state progression and control flow to the application layer.

The practical implication is that loop exposure is what converts model capability into system capability. Better models improve the quality of individual semantic steps, but the exposed application-layer loop determines whether those steps compound cleanly across time. Without that loop, the system keeps asking the model to simulate its own scheduler inside the same scarce medium it is meant to reason within.

This also clarifies what "good SDK design" means in this domain. A strong SDK is not one that hides the most machinery behind a single high-level agent call; it is one that gives the application layer a control surface over the loop while still making each bounded call and tool execution easy. That control surface might be raw code, a workflow graph, or a declarative runtime. Exposed-loop SDKs let developers or applications shape the scheduler. Closed-loop SDKs force them to accept the scheduler the library authors embedded.

The [RLM architecture](./rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md) is a useful boundary case. It shows that the deepest requirement is not that a human programmer manually scripts every step, but that the loop runs on an exact substrate outside the conversation. In RLM, the model itself may author dispatch by writing scheduler code, but the REPL still owns recursion depth and intermediate state. That still supports this note's claim about loop exposure: the power comes from moving the loop out of chat and onto an inspectable control surface, even if the model participates in authoring that surface.

This also clarifies why several partial approaches help but do not fully solve the problem. [Specification-level separation](./specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md) names control flow and externalises some state, recovering scoping benefits before hard reliability. Tool-use frameworks harden interface contracts at the boundary. Both are useful. But neither yields the full gain until the SDK exposes the recursive loop to the application layer rather than leaving it implicit inside the conversation.

---

Relevant Notes:

- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: this note extracts the architectural consequence of the model's symbolic-scheduler requirement
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — contrasts: explains what happens when the conversation, rather than application code, owns the loop
- [scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — grounds: loop exposure matters because bookkeeping and semantic work have different reliability properties
- [specification-level separation recovers scoping before it recovers error correction](./specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md) — boundary case: partial separation helps before loop exposure is complete
- [context engineering](./context-engineering.md) — applies: routing, loading, and scoping become application responsibilities when the SDK exposes the loop
- [RLM achieves the clean scheduler model but opts out of accumulation](./rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md) — boundary case: the model can author the loop, but the loop still has to run outside the conversation to recover the clean architecture
