---
description: "Without backpropagation's chain rule, attributing failures in a growing, interdependent store is a debugging problem—tractable like large codebases where debuggable, harder where prose instructions weaken traces and reproduction"
type: types/note.md
traits: [title-as-claim]
tags: [self-improving-systems, improvement-loop, continual-learning, learning-theory]
---

# Credit assignment without a chain rule is a debugging problem over an interdependent store

In gradient training, backpropagation applies the chain rule to compute how each parameter contributed to a loss, scaling across billions of tightly coupled weights in a single backward pass. [Selection-based learning](./definitions/selection-based-learning.md) over a store of instructions, hypotheses, checks, and scripts has no chain rule, so its credit assignment is far less scalable than gradient learning. Yet that does not block full automation: large software codebases have no chain rule either, and engineers and coding agents routinely localize faults across hundreds of interdependent modules by **debugging**—reproducing failures, reading traces, inspecting recent diffs, narrowing suspects across module boundaries, and verifying fixes with tests.

While a store holds only a few isolated rules, debugging is trivial. As the store grows, artifacts become interdependent: a routing instruction points to a skill; the skill relies on a retained convention; a validator enforces part of that convention while leaving the rest to model judgment; a shared hypothesis justifies several rules at once. Locating which upstream edit (or combination of edits) caused an observed failure is the backward inverse of the **validation radius** in [the readable-artifact loop](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), which asks what downstream work a proposed edit might break.

What makes a mixed prose-and-code store harder to debug than ordinary software is not the lack of gradients, but three properties that weaken ordinary debugging tools:

- **Softer traces.** In deterministic code, a stack trace records the exact call path that executed. When an LLM loads natural-language instructions into context, recording which files loaded does not prove which sentence steered the decision, because [legibility is not faithfulness](./revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md).
- **Implicit coupling.** Code dependencies are declared through imports, types, and interfaces. Prose conventions can interact semantically across unrelated tasks without any explicit link in the store.
- **Noisier, diffuse failures.** A bad rule need not trigger a clean crash; it may quietly degrade unrelated tasks through context saturation or subtle prompt interference, making reproduction and `git bisect`-style isolation noisier than a failing unit test.

Because of those three differences, naive workarounds still break down at scale. Appending a local exception avoids debugging altogether, adding coupling and accelerating store bloat into an accretion plateau ([raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md)). Trusting an agent's prose rationale guesses blame without checking causal faithfulness. Exhaustive one-by-one ablation verifies causality cleanly on small stores, but becomes prohibitively expensive once hundreds of artifacts interact.

Scaling credit assignment therefore turns on making the retained store **debuggable**—separating cheap suspect narrowing from targeted causal checks, just as software engineering does. Execution traces recording which instructions, retrieved notes, and scripts actually loaded narrow suspects from the whole store to the active slice. [Near-decomposability](./near-decomposability-may-make-local-inspection-affordable.md) and explicit dependency links bound how many artifacts can interact. When rules rest on an explicit [addressable theory](./definitions/addressable-theory.md) with stated predictions, a failed prediction names a specific premise to check. Replaying the failing case with a shortlisted entry withheld or modified verifies causal responsibility directly, and codifying settled rules into deterministic scripts moves them back into ordinary software debugging. Debugging will not match backpropagation's scale across billions of coupled parameters, but over a modular store of hundreds or thousands of artifacts it gives a plausible path to fully automated credit assignment.

## Scope

- This problem binds once retained artifacts interact across tasks. A flat lookup table of independent entries with per-entry feedback avoids most cross-artifact debugging.
- Credit assignment here means attributing a failure to retained artifacts in the deployed system's store, not explaining internal activations inside the frozen model's weights.

## Open Questions

- How well do coding-agent debugging practices (trace inspection, diff bisection, hypothesis-guided narrowing, and targeted replay) carry over as the share of natural-language artifacts and cross-artifact coupling grows?
- Can an autonomous selection loop maintain modular boundaries, dependency links, and replay fixtures well enough to keep the store debuggable without human refactoring?

---

Relevant Notes:

- [Selection-based learning](./definitions/selection-based-learning.md) — defined-in: the learning process whose scaling depends on store debuggability
- [The readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — contrasts: validation radius is the forward problem of what an edit might break; credit assignment is the inverse problem of what caused a failure
- [Revision guided by rationale needs faithfulness, not just legibility](./revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md) — grounds: why traces of loaded prose are weaker than deterministic stack traces
- [Near-decomposability may make local inspection affordable](./near-decomposability-may-make-local-inspection-affordable.md) — mechanism: modular structure as one candidate way to keep backward localization bounded
- [Addressable theory](./definitions/addressable-theory.md) — enables: stated premises that give debugging specific units to test
