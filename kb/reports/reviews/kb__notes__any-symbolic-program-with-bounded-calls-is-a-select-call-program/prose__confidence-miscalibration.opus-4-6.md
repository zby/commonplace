---
gate: prose/confidence-miscalibration
verdict: pass
---

The note's main construction is explicitly labeled "**Claim.**" with a "**Why.**" justification and a "**Consequence.**" — the argumentative structure is transparent. The claim is a logical/structural observation (if inter-call computation is symbolic and calls are bounded, you can refactor into the select/call form), not an empirical one, so assertive language is appropriate.

Calling it a "decomposition lemma" in the heading implies mathematical rigor while the "Why" is an informal sketch rather than a formal proof. However, the argument is straightforward enough (it's essentially the observation that any program can be refactored into a state-machine loop, applied to LLM-call programs) that the gap between the label and the formality level is minor. The claim is not speculative — it's an analytical move that follows from well-understood CS concepts.
