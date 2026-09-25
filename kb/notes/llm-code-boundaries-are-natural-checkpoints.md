---
description: "LLM↔code boundaries expose concrete inputs and outputs for inspection and replay; deterministic execution preserves rather than corrects a wrongly interpreted argument"
type: types/note.md
traits: [title-as-claim]
tags: [learning-theory, computational-model, constraining]
---

# LLM↔code boundaries are natural checkpoints

Agentic systems that pass explicit values between LLM components and code expose natural checkpoints for debugging and testing. At an LLM → code crossing, an interpretation becomes a concrete argument that can be inspected, validated, and replayed. At a code → LLM crossing, the returned value can be checked before it enters the next model input. These observations let a debugger separate what arrived at a component from what the component did with it.

The boundary does not establish that the value expresses the intended meaning. [Three-way diagnosis](./llm-output-deviation-requires-three-way-diagnosis.md) distinguishes a specification admitting unwanted readings, sampling variation, and failure to follow the specification. Any of these can produce an unwanted argument that crosses into code unchanged. Deterministic execution fixes the result conditional on that argument and the relevant state; it does not repair the upstream defect.

For example, a request to reserve two seats produces a well-typed argument `count=3`. A deterministic booking function can correctly reserve three seats. The call boundary exposes the mismatch between the request and the argument, while replay confirms how the function handles that argument. If the code's validation checks only that `count` is a positive integer, the wrong value passes. Detecting the mistake requires a check against the request, not just the argument's type.

This supports three operations:

- **Debugging:** inspect the argument against the request and the result against the code's contract. Both checks are needed: an upstream mistake and a code bug can occur in the same call.
- **Testing:** captured arguments and state support repeatable tests of deterministic code. Repeated model calls characterize output variation; separate checks establish whether the outputs satisfy the specification and whether the specification captures the intent.
- **Refactoring:** captured boundary cases provide comparison inputs when logic moves between a prompt and code through [constraining](./definitions/constraining.md). Keeping the interface stable can preserve call sites, but preserving the interface alone does not establish equivalent behavior.

## Scope

Replay requires the state and external dependencies that affect the result, not just the visible arguments. Code that reads a changing database or invokes another model is not deterministic merely because it is code. A boundary with hidden state or opaque values is a weaker checkpoint. Inspecting one boundary localizes evidence; it does not by itself identify which upstream diagnostic relation failed.

---

Relevant Notes:

- [LLM output deviation requires three-way diagnosis](./llm-output-deviation-requires-three-way-diagnosis.md) — grounds: the upstream defects that a concrete argument can carry across a boundary
- [constraining](./definitions/constraining.md) — defined-in: narrowing valid interpretations, including moves from prompts into code
