---
description: "The default of writing-to-think is an unsearched slip; the LLM's relaxation is shaped by a plausibility objective into camouflage that hides better — and a flagging objective could restore the stall"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, llm-interpretation-errors]
status: speculative
---

# The machine searches for the camouflage a human writer usually slips into

When a generator cannot satisfy a goal, it emits the most plausible-looking artifact it can — [a relaxation that drops a constraint while looking solved](./llm-generation-relaxes-goals-where-human-writing-stalls.md). That failure mode is not unique to machines: a human can also smooth over a constraint they failed to meet — reviewers get carried by fluent argument, papers ship with hidden gaps. So the *failure mode* is shared.

What differs — this is the hypothesis — is the **default**. Humans can and do search to conceal: rhetoric, motivated reasoning, the practiced paper that buries its weakest step. But that concealment is effortful and optional; the unmarked human default, when you are writing to think, is the unsearched slip or the involuntary stall, not optimized camouflage. For the LLM the order is reversed. Next-token and preference training optimize the policy for text that *looks* satisfied, so plausible surface is the objective itself. When no full witness — no concrete artifact satisfying every constraint — is available, the relaxation the policy emits is not a constraint dropped at random but the most-plausible-looking one. The camouflage is shaped by training, not chosen per output — but training is what made it the default. (Fernando Borretti, in "Human Routers of Machine Words," gives the polemical inside-view of this pressure: "if I don't turn this garbage into something presentable the RLHF device will shock me again.")

That default is what drives the observability gap. The human writing to think, not optimizing to hide the gap, leaves residue a reader can use — the hedge, the labored passage, the three-week silence, the abandoned draft. The trained policy leaves less of that residue: its output is shaped toward plausible completion, and plausibility — not an aim at undetectability as such — is what thins it. The failure is the same in kind; the default process that produces it is not — and that difference is why the machine relaxation is the harder one to catch. The model also relaxes freely, with no stall to clear, so more under-constrained ideas reach finished prose to begin with.

## Training implication

Because the camouflage is shaped by an *objective*, it is a property of that objective, not a fixed limit. The stall-signal a human emits may be suppressed by the plausibility objective rather than absent — and an objective that instead rewarded the model for *flagging* the constraint it dropped (marking the output a relaxation, or refusing) could train the stall back in. The catch is [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) inverted. Such a target is cheapest where a verifier can label solved-vs-relaxed — code, math — which is where the loss was already smallest; it is hardest to build in the oracle-poor prose where the stall would help most.

This is speculative on two counts: it assumes the shortfall is both representable in the model and rewardable, and that rewarding honest flagging would not simply teach decorative hedges — a relaxation of the *flagging* objective in its turn.

---

Relevant Notes:

- [LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on](./llm-generation-relaxes-goals-where-human-writing-stalls.md) — grounds: the mechanism this builds on — generation emits the most-plausible-looking artifact and never marks whether it was a full witness or a relaxation
- [An LLM's generation confidence tracks typicality, not soundness](./llm-generation-confidence-tracks-typicality-not-soundness.md) — mechanism: plausibility-trained output can hide a dropped constraint because confidence tracks typicality, not soundness — the decoupling the "shaped toward plausible completion" claim rests on
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — exemplifies: the oracle-rich/poor asymmetry reappears as where the solved/relaxed label can be cheaply obtained
- [Human writing structures transfer to LLMs because failure modes overlap](./human-writing-structures-transfer-to-llms-because-failure-modes.md) — contrasts: that note treats shared human/LLM failure modes as grounds for convention transfer; this sharpens the boundary — same failure mode, different default process and observability
- [Human-LLM differences are load-bearing for knowledge system design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — exemplifies: a concrete case of weighing resemblance against difference — a shared failure class still needs different mitigation when the default process differs
- [Human Routers of Machine Words](../sources/borretti-human-routers-of-machine-words.md) — derived-from: the note quotes Borretti's RLHF / "presentable" framing directly as the inside view of the plausibility objective
