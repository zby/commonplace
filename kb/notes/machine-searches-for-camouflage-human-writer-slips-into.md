---
description: "A human relaxation is an unsearched slip; the LLM's is the argmax of a plausibility objective, selected to be undetectable — so it hides better, and a flagging objective could restore the stall"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory]
status: speculative
---

# The machine searches for the camouflage a human writer only slips into

When a generator cannot satisfy a goal it returns the argmax — [a relaxation that drops a constraint while looking solved](./llm-generation-relaxes-goals-where-human-writing-stalls.md). That failure mode is not unique to machines: a human can also smooth over a constraint they failed to meet — reviewers get carried by fluent argument, papers ship with hidden gaps — and you meet relaxations in human-authored text too. So the *failure mode* is shared.

What is not shared — this is the hypothesis — is the **search** for it. A human relaxation is an unsearched slip: an oversight or a self-deception, whatever happened to get written at the joint they failed to notice. The LLM relaxation is the *argmax* of an objective that rewards surface plausibility — next-token and preference training optimize for text that *looks* satisfied, so when no full witness is available the model does not drop a constraint at random; it selects the relaxation that looks most solved. (Borretti names that objective from the inside: "if I don't turn this garbage into something presentable the RLHF device will shock me again.")

That search is what drives the observability gap. The human, not optimizing to hide the gap, leaves residue a reader can use — the hedge, the labored passage, the three-week silence, the abandoned draft. The model, optimizing for exactly the plausible surface, leaves as little as it can: its camouflage is *selected* to be undetectable, not incidentally smooth. The failure is the same in kind; the process that produces it is not — and that difference in process is why the machine relaxation is the harder one to catch. The model also relaxes by default, with no stall to clear, so more under-constrained ideas reach finished prose to begin with.

## Training implication

Because the camouflage is the argmax of an *objective*, it is a property of that objective, not a fixed limit. The stall-signal a human emits may be suppressed by the plausibility objective rather than absent — and an objective that instead rewarded the model for *flagging* the constraint it dropped (marking the output a relaxation, or refusing) could train the stall back in. The catch is [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) inverted: such a target is cheapest where a verifier can label solved-vs-relaxed — code, math — which is where the loss was already smallest, and hardest to build in the oracle-poor prose where the stall would help most.

This is speculative on two counts: it assumes the shortfall is both representable in the model and rewardable, and that rewarding honest flagging would not simply teach decorative hedges — a relaxation of the *flagging* objective in its turn.

---

Relevant Notes:

- [LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on](./llm-generation-relaxes-goals-where-human-writing-stalls.md) — grounds: the mechanism this builds on — generation returns the argmax and never marks whether it was a full witness or a relaxation
- [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — exemplifies: the oracle-rich/poor asymmetry reappears as where the solved/relaxed label can be cheaply obtained
