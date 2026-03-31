The note cites ~15 linked notes and uses David Deutsch's reach criterion as its primary external theoretical anchor. Central causal claims are traced below.

---

**Claim: "KB learning is broader than retrieval" / contextual competence as criterion**

Cited to [claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md]. The cited note argues that a Claw acts on behalf of the user across execution, classification, communication, planning, and pattern recognition — not just retrieval. It defines "contextual competence" as "the ability to act appropriately given accumulated knowledge about the domain, the user, and the project." The current note's use matches this exactly. ✓

**Claim: bounded context as the operative constraint**

Cited to [context-efficiency-is-the-central-design-concern-in-agent-systems.md]. The framing — that context is finite and degrades before it runs out — is consistent with the KB's broader treatment of this topic. ✓

**Claim: "there is no scoping mechanism to isolate what matters"**

Cited to [llm-context-is-composed-without-scoping.md]. Used correctly as grounding for why "just put everything in context" fails. ✓

**Claim: Deutsch distinguishes adaptive from explanatory knowledge; reach is the distinguishing property**

Cited to [first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md]. That note presents Deutsch's distinction with the gene/eye vs. Newton's optics example and defines reach as "applies beyond its original context because the explanation captures structure that isn't context-dependent." The current note's use is faithful. The attribution chain (Deutsch → linked note → this note) adds one layer of mediation. INFO — the attribution is accurate but one-link indirect; if the mediating note reframes Deutsch non-standardly, scope mismatch could propagate. The framing here is consistent with standard readings of *The Beginning of Infinity*.

**Claim: "accumulation is the most basic learning operation" with reach as its key property**

Cited to [learning-is-not-only-about-generality.md]. That note grounds learning in Simon's definition ("any change in a system that produces a more or less permanent change in its capacity") and explicitly states: "Accumulation — adding knowledge to the store — is itself a learning operation, and the most basic one." The reach framing is also present: "facts are adaptive knowledge... while theories are explanatory knowledge." The current note's use matches. ✓

**Claim: "constraining and distillation both trade generality for the reliability+speed+cost compound"**

Cited to [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md]. That note defines both operations, their distinct mechanisms (constraining narrows interpretation space; distillation extracts under context budget), and the shared trade-off. The current note's characterization is accurate. ✓

**Claim: discovery has a dual structure — positing a general concept while recognizing existing particulars as instances**

Cited to [discovery-is-seeing-the-particular-as-an-instance-of-the-general.md]. That note's core argument is exactly this dual structure, with three depths (shared feature → shared structure → generative model). The current note's use is faithful. ✓

**Claim: "distillation can preserve or destroy reach"**

This is the note's own inference, not directly attributed to a cited source. The reasoning: if a distilled skill captures the principle, reach is preserved; if it captures only the procedure, reach is lost. INFO — the inference is valid but not grounded in a cited source. The distinction between preserving principle vs. procedure is plausible but could be tested more sharply: does a procedure that produces identical outputs to the principle it was derived from have reach? The note implicitly says no (reach lives in explanatory structure, not input-output behavior), but this is assumed rather than argued.

**Claim: Thalo convergence suggests "the reach is real"**

Cited to [related-systems/thalo.md]. Convergent evolution from one independent system is a weak confirmatory signal. INFO — "suggests the reach is real" is appropriately hedged, but the argumentative role slightly overstates what one convergence case demonstrates. It shows the pattern is useful elsewhere, not that the pattern's explanatory structure transfers.

**Claim: sift-kg and Siftly produce adaptive rather than explanatory knowledge**

Cited to [related-systems/sift-kg.md] and [related-systems/siftly.md]. The note hedges: "This isn't a claim that extraction can never produce knowledge with reach." The characterization of entity-relation triples as having "no reach" is a reasonable inference from how extraction systems work — triples capture facts, not causal explanations. INFO — this generalizes from two specific systems to "current extraction systems"; the hedge is appropriate but the generalization is doing more argumentative work than two instances warrant.

---

No WARN-level misalignments. Four INFOs: indirect Deutsch attribution (one mediating link), ungrounded inference about distillation preserving/destroying reach, Thalo convergence as evidence for reach, and generalization from two extraction systems.
