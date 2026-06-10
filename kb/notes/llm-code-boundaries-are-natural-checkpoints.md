---
description: At each LLM↔code transition both semantic underspecification and execution indeterminism collapse simultaneously, making these boundaries natural places to anchor debugging, testing, and refactoring
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, computational-model, constraining]
status: seedling
---

# LLM↔code boundaries are natural checkpoints

Agentic systems interleave LLM components and deterministic code. The two sides have opposite semantic properties: LLMs interpret natural-language specs (semantically underspecified) and sample from distributions (execution indeterminism); code commits to one precise meaning and returns the same result for the same arguments. See [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) for the two-phenomena model this note depends on.

At each crossing both properties flip simultaneously:

- **LLM → code**: semantic underspecification resolves — the code treats the LLM's output as a concrete value, regardless of what other interpretations were possible. Indeterminism collapses — given the same arguments, the code returns the same result.
- **Code → LLM**: both are reintroduced. A concrete value enters a component that interprets a natural-language spec to decide what to do with it. The spec doesn't uniquely determine the behavior, and sampling adds further variation.

The two phenomena are conceptually distinct but travel together in practice: LLM components have both, code has neither. This coupling is why the boundaries are natural **checkpoints** — the deterministic side doesn't care how it was reached, only what arguments it received. Once execution crosses into code, everything upstream has been collapsed to a value the code can treat as an input.

This matters in three operational ways:

- **Debugging**: you can bisect a failure at the nearest checkpoint — inspect what arrived at the code side, and separate "LLM produced a bad argument" from "code handled a good argument wrongly." Upstream of the checkpoint, failures may not reproduce; downstream, they will.
- **Testing**: code paths downstream of a checkpoint are traditionally testable with equality assertions. The LLM projection upstream needs distribution-style testing — running the same input many times and characterising the output space.
- **Refactoring**: moving logic across the boundary (constraining or relaxing) is a local operation — the checkpoint hides the upstream mess from everything further down, so call sites don't need to change when the implementation switches sides.

Boundaries aren't fixed. As systems evolve, logic moves across them through [constraining](./definitions/constraining.md) and relaxing — but each new boundary is another checkpoint where both phenomena collapse at once.

---

Relevant Notes:

- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: the two-phenomena model; the checkpoint property follows from LLM components having both phenomena while code has neither
- [constraining](./definitions/constraining.md) — related: each constraining move creates a new checkpoint by collapsing an LLM component's properties to deterministic ones
- [llm debugging starts with retry-versus-rewrite triage](./llm-debugging-starts-with-retry-versus-rewrite-triage.md) — applies: debugging at a checkpoint is how you separate the retry case from the rewrite case
