---
description: "Without backpropagation's chain rule, tracing a downstream failure back to the responsible entry in a growing, interdependent store of prose, hypotheses, and code becomes the scaling bottleneck of selection-based learning"
type: types/note.md
traits: [title-as-claim]
tags: [self-improving-systems, improvement-loop, continual-learning, learning-theory]
---

# Credit assignment without a chain rule bounds selection-based learning over an interdependent store

In gradient training, backpropagation applies the chain rule to compute how each parameter contributed to a loss, giving every coupled weight a local update signal. [Selection-based learning](./definitions/selection-based-learning.md) over a store of instructions, hypotheses, checks, and scripts has no chain rule. When a later task fails, nothing propagates blame automatically back through the retained artifacts that shaped the run.

While a store holds only a few isolated rules, credit assignment is straightforward: a failure trace points to the one rule that fired. As the store grows, artifacts become interdependent. A routing instruction points to a skill; the skill relies on a retained convention; a validator enforces part of that convention while leaving the rest to model judgment; a shared hypothesis justifies several rules at once. A single failure can come from a wrong premise, an over-broad routing trigger, a missing retrieval link, or two rules that interact poorly even though each looks sound alone.

That backward problem is the inverse of the **validation radius** in [the readable-artifact loop](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md). Validation asks the forward question—what downstream work could a proposed edit break? Credit assignment asks the backward question—which upstream retained edit, or combination of edits, caused an observed failure? Even when every artifact is readable on its own, answering the backward question gets harder as coupling grows.

Three obvious shortcuts break down at scale. Appending a local exception avoids locating the faulty entry altogether, adding coupling and accelerating store bloat until a credit-assignment failure turns into an accretion plateau ([raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md)). Trusting an agent's prose rationale is cheap, but [legibility is not faithfulness](./revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md): a plausible written rule need not be what actually drove the failure. Testing every retained artifact by withholding it one at a time settles causality, yet exhaustive ablation stops scaling once hundreds of notes, skills, and scripts interact.

Pushing the bottleneck back therefore requires separating cheap suspect narrowing from targeted causal checks. Execution traces that record which instructions, retrieved notes, and scripts actually loaded cut the search from the whole store to the active slice. [Near-decomposability](./near-decomposability-may-make-local-inspection-affordable.md) and explicit dependency links limit how many artifacts can interact inside that slice. When rules rest on an explicit [addressable theory](./definitions/addressable-theory.md) with stated predictions, a failed prediction points to a specific premise rather than leaving search to wander across downstream patches. Replaying the failing case with a shortlisted entry withheld or modified then checks causal responsibility directly instead of trusting prose. None of these replaces an exact chain rule; together they determine how large and coupled a store can grow before credit assignment stalls selection.

## Scope

- This bottleneck binds once retained artifacts interact across tasks. A flat lookup table of independent entries with per-entry feedback avoids most cross-artifact credit assignment.
- Credit assignment here means attributing a failure to retained artifacts in the deployed system's store, not explaining internal activations inside the frozen model's weights.

## Open Questions

- How fast does trace- and hypothesis-guided credit assignment degrade as store size and cross-artifact coupling grow?
- Can an autonomous selection loop preserve modular boundaries and dependency records well enough to keep credit assignment tractable without human refactoring?

---

Relevant Notes:

- [Selection-based learning](./definitions/selection-based-learning.md) — defined-in: the learning process whose scaling this bottleneck constrains
- [The readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — contrasts: validation radius is the forward problem of what an edit might break; credit assignment is the inverse problem of what caused a failure
- [Revision guided by rationale needs faithfulness, not just legibility](./revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md) — grounds: why reading prose explanations alone does not solve credit assignment
- [Near-decomposability may make local inspection affordable](./near-decomposability-may-make-local-inspection-affordable.md) — mechanism: modular structure as one candidate way to keep backward localization bounded
- [Addressable theory](./definitions/addressable-theory.md) — enables: stated premises that give credit assignment specific units to test
