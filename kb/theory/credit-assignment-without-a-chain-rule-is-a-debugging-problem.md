---
description: "Without backpropagation's chain rule, attributing failures in a growing, interdependent store is a debugging problem—tractable like large codebases where debuggable, harder where prose instructions weaken traces and reproduction"
type: types/note.md
traits: [title-as-claim]
tags: [self-improving-systems, improvement-loop, continual-learning, learning-theory]
---

# Credit assignment without a chain rule is a debugging problem over an interdependent store

In gradient training, backpropagation applies the chain rule to compute how each parameter contributed to a loss, scaling across billions of tightly coupled weights in a single backward pass. [Selection-based learning](./definitions/selection-based-learning.md) over a store of instructions, hypotheses, checks, and scripts has no chain rule, so its credit assignment is far less scalable than gradient learning. Software debugging offers another way to locate a fault: reproduce the failure, use traces and recent changes to narrow the suspects, then test a suspected cause. The question is how well those steps work when the store contains prose instructions as well as executable code.

In a flat lookup table of independent entries, feedback on one entry tells the debugger where to look, not what went wrong inside that entry. The problem changes when artifacts depend on one another: a routing instruction points to a skill; the skill relies on a retained convention; a validator enforces part of that convention while leaving the rest to model judgment; a shared hypothesis justifies several rules at once. Locating which upstream edit (or combination of edits) caused an observed failure is the backward inverse of the **validation radius** in [the readable-artifact loop](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), which asks what downstream work a proposed edit might break.

What makes a mixed prose-and-code store harder to debug than ordinary software is not the lack of gradients, but three properties that weaken ordinary debugging tools:

- **Softer traces.** In deterministic code, a stack trace records the exact call path that executed. When an LLM loads natural-language instructions into context, recording which files loaded does not prove which sentence steered the decision, because [legibility is not faithfulness](./revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md).
- **Implicit coupling.** Code dependencies are declared through imports, types, and interfaces. Prose conventions can interact semantically across unrelated tasks without any explicit link in the store.
- **Noisier, diffuse failures.** A bad rule need not trigger a clean crash; it may quietly degrade unrelated tasks through context saturation or subtle prompt interference, making reproduction and `git bisect`-style isolation noisier than a failing unit test.

**Conjecture.** Two instructions might work well separately but conflict when read together. For example, “keep answers short” might suppress a qualification required by “state what the evidence does not show.” A load trace would show both rules in context, not whether one changed how the model applied the other. If the omission occurs only on some runs, even a replay that restores the qualification could be a coincidence. On the same evidence-limited cases, the conjecture predicts more omissions with both rules present than with the qualification rule alone. Repeated comparisons that show no such difference would count against this explanation for those cases.

Some shortcuts miss the cause; others cost too much as the store grows. Appending a local exception avoids debugging altogether, adding coupling and accelerating store bloat until further additions stop improving the system ([raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md)). Trusting an agent's prose rationale guesses blame without checking causal faithfulness. Removing each entry in turn costs at least one replay per entry. Even in a small store, that comparison can miss a failure that persists unless two entries are removed together.

Scaling credit assignment therefore turns on making the retained store **debuggable**—separating cheap suspect narrowing from targeted causal checks, just as software engineering does. Execution traces recording which instructions, retrieved notes, and scripts actually loaded narrow suspects from the whole store to the active slice. Where interactions across modules are weak enough for the failure under investigation, [local inspection may suffice](./near-decomposability-may-make-local-inspection-affordable.md). Explicit dependency links suggest where to look first; missing links do not rule out interactions. When rules rest on an explicit [addressable theory](./definitions/addressable-theory.md) with stated predictions, a failed prediction points to candidate premises to check, though it rarely isolates a single faulty one.

Compare the same case with and without a suspect entry. If outcomes vary, repeat both conditions. If two edits may interact, test them separately and together. Settled rules expressed as deterministic scripts can instead be traced and tested as ordinary code. Whether an automated debugger can keep those comparisons affordable as a mixed store grows remains open.

## Scope

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
