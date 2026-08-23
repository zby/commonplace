---
description: "Improvements accumulate when later improvement consumes or preserves retained results; compounding requires an earlier benefit to counterfactually improve a later episode, directly or through reinvested savings"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Improvements can accumulate without compounding

Useful changes can persist and build a growing stock without making later improvement any easier. That is **accumulation**: a later improvement episode consumes, transforms, or preserves an earlier retained result. [Cumulativity through the retained result](./accumulation-counts-dependence-through-the-retained-result.md) provides a more precise test. **Compounding** adds a productivity effect. Holding the later problem, evidence, randomness, and resource budget fixed, removing the earlier result's benefit would reduce the later gain or increase its cost. A system that retains each useful rule while every new rule remains equally difficult to discover accumulates without compounding.

Compounding is therefore a causal claim about a pathway across episodes, not a label for one artifact or for reuse alone.

## Feedback into later improvement is the distinction

Accumulation asks whether later improvement uses or preserves what earlier work retained. Compounding adds one causal question: **did the benefit of that retained result make a later improvement more productive?** The result and its benefit are distinct. A validator is a retained result; the time or errors it saves are benefits. Those benefits can reach later improvement in two ways:

- **Direct contribution.** The benefit reaches later improvement without resource reallocation. The later episode may use the retained result itself or consume a benefit-bearing output, such as observations or training data that the result improved. Better retrieval, evaluation, or revision contributes this way only when removing the benefit lowers the later gain or raises its cost.
- **Indirect contribution.** The retained result frees time, compute, or judgment elsewhere. An observed reinvestment path makes that capacity available to improvement work, and later work consumes it to produce another retained gain. Fewer recurring failures or faster execution can contribute this way. An unused saving, or one absorbed by another bottleneck, does not.

The indirect path is where the practical boundary between accumulation and compounding becomes fuzzy. A retained result may clearly accumulate and save divisible resources, while an allocator reinvests only part of the saving and another bottleneck absorbs the rest. At the artifact boundary, this looks like accumulation plus an operational benefit. At a wider boundary that includes allocation and later improvement, the reinvested portion can be a compounding contribution. The classification therefore depends on the system boundary, horizon, and causal resolution even if the endpoint definitions remain distinct.

Feedback that reduces performance against the declared objective amplifies error rather than compounding under this gain-specific definition. A pathway can still compound toward a normatively bad declared objective; desirability is a separate question.

## The evidence comes from later episodes

The metric used to accept a change tests its immediate target. For example, a validator accepting a change shows that the change passes its immediate check; it does not show that later revision became more productive. Evidence for compounding must therefore come from [later improvement episodes](./compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md), be measured on a productivity dimension other than the accepting metric, and be connected to the earlier benefit by a causal trace.

A later episode provides local evidence of a compounding contribution only when the displaced measure and causal trace support the counterfactual: without the earlier benefit, the episode would have produced less gain or required more input. A sequence supports sustained compounding only when each successive contribution carries that evidence. The effect need not be exponential, smooth, or permanent. It may be modest, irregular, and eventually saturate.

## Report feedback, duration, constraints, and frame separately

An observation of the pathway should report four features separately:

- **Feedback.** State which earlier benefit counterfactually changed a later gain or its cost, and whether the path was direct or required reinvestment.
- **Duration.** One traced contribution is local evidence; a sequence of traced contributions supports sustained compounding.
- **Constraints and level.** Human attention, evaluation, compute, or another bottleneck may flatten the whole pathway even as one component becomes more productive. Name the component and system boundary instead of treating a latent component effect as a whole-pathway result.
- **Frame.** Declare the system boundary, objective, and horizon. Provide evidence of indirect reinvestment rather than inferring it, and report objective-relative improvement separately from whether the objective is desirable.

The test is architecture-neutral. A learned optimizer may produce feedback through opaque parameter changes. [Reflection makes the relevant components addressable](./reflection-buys-addressability.md), but explicit representation alone does not establish the causal trace. Bare automation is likewise not compounding. Nor can evaluation beyond [the domain it can warrant](./warranted-autonomy-is-bounded-by-oracle-domain.md) justify a feedback claim.

## Open Questions

- Whether repository and session histories contain enough timing, uptake, and decision evidence to reconstruct indirect reinvestment after the fact.
- Whether improvement quality can be compared across heterogeneous episodes without collapsing it into one misleading scalar.
- Which evaluation investments most reliably extend compounding rather than merely increasing candidate throughput.

---

Relevant Notes:

- [Compounding is tested in later improvement, not by the accepting metric](./compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) — extends: supplies the displaced measures, causal traces, and baselines needed to test the feedback
- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](./increasing-computational-autonomy-relocates-human-effort.md) — mechanism: explains why fixed human attention can limit the expression and duration of compounding
- [Oracle accumulation improves selection for later candidates in its maintained domain](./oracle-accumulation-improves-the-selection-environment.md) — mechanism: a retained check can improve later selection and widen computational capacity at once
- [Self-improving system](./definitions/self-improving-system.md) — defined-in: supplies the boundary, objective, and horizon to which the reading is relative
- [Commonplace as a reflective system](./evidence/commonplace-as-a-reflective-system.md) — evidenced-by: analyzes Commonplace, the human-inclusive repository system, and supplies candidate episodes whose contribution to compounding remains to be measured
