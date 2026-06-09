---
description: A detail the executor will see for itself is an authoring-time snapshot — stale by the author's ignorance or by the system's evolution; leave those to the executor, and fix only the goal, constraints, and the arbitrary choices an underdetermined situation leaves the executor unable to settle
type: kb/types/note.md
traits: [title-as-claim]
tags: []
status: seedling
---

# An instruction should fix what the executor can't see, not what it will

An instruction is written before it runs, and the executor acts later, on the live system. Any detail the instruction fixes is a snapshot taken at authoring time, and it diverges from what the executor actually faces for two reasons: at writing time the author saw only part of the situation, and the situation keeps changing — which we *want* it to. So a fixed detail goes stale, by ignorance or by drift. When it does, the executor is stuck: follow the stale detail and get it wrong, or override the instruction it was handed. Either way the detail meant to help has discarded what the executor can see now. That is why over-specified instructions are brittle. (It also buries the details that matter among the ones that don't.)

The usual heuristic — *say what you want, not how to do it* — gestures at this, because the *how* is so often the part that depends on the situation. But the real line isn't how-versus-what: a *what* can be a snapshot too (which functions currently call it, what the config already contains), and some *how* is genuinely the author's to fix. The real test is what the executor can see for itself. Leave that to the executor — its output then tracks the system as it evolves, not a past version of it. Fix only what it can't see: the goal, the constraints, what *done* means, and any privileged fact the author holds but the executor can't reach.

Arbitrary choices fall on the same side: they too are something the executor can't see, because the answer isn't in the situation at all. They include the obvious conventions — output paths, file names, templates — but also *which of several valid interpretations to follow* when the situation picks out none. One of the many has to be chosen, and only the author can choose it once and the same way. This is the mirror of the situational case: a situational detail goes stale because the situation settles it and then keeps moving, while an arbitrary choice can't, because the situation never settled it — which is just why pinning the first is brittle and pinning the second safe.

This is not a rival to [frontloading](./frontloading-spares-execution-context.md); it is a cost frontloading's decision has to weigh. Frontloading asks whether inserting a value saves context — but inserting one the executor would be better placed to choose forfeits its runtime advantage, so a value can be worth inserting for context and still be wrong to fix. Both pulls live in the same decision.

Two premises hold the claim up, and dropping either flips it. If the executor isn't [competent enough to decide for itself](./design-for-the-first-time-human-except-on-access-cost.md), fixing the detail is help, not harm. And if the author can fully see the situation when writing *and* it won't change afterward — a static, fully-determined task — there is no snapshot to go stale. Over-specification bites in the common middle: a capable executor acting on a system the author could only half-foresee and that keeps moving.

---

Relevant Notes:

- [Design for the competent first-time human, except on access cost](./design-for-the-first-time-human-except-on-access-cost.md) — grounds: the competent-executor premise this claim rests on
- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — extends: the robustness cost here is a term frontloading's insert-to-save-context decision must weigh
- [Agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — contrasts: under-specification is the dual failure; the skill is picking the right axis, not the right amount
