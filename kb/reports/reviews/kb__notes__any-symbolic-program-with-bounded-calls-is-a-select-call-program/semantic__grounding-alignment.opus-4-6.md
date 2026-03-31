The note cites three KB notes. The central claim is a self-contained formal argument.

---

**Claim: the base loop is formalized by the bounded-context orchestration model**

Cited to [bounded-context-orchestration-model.md]. The `while not satisfied(K): P = select(K); r = call(P); K = K + r` loop is directly referenced. ✓

**Claim: LLM-mediated scheduling is a degraded variant that violates precondition (a)**

Cited to [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md]. The characterization — LLM-mediated scheduling puts scheduling inside the stochastic engine rather than symbolic code — is consistent with the cited note's thesis. ✓

**Claim: decomposition heuristics might be expressible as transformations between valid select/call programs**

Cited to [decomposition-heuristics-for-bounded-context-scheduling.md]. This is framed as an open question, not a claim. ✓

**The lemma's own argument**

The core reasoning is: "At each call site, everything available to decide the next prompt is the original inputs plus prior call results — exactly K." This is a valid argument by construction. The analogy to state-machine loop refactoring is appropriate. The note doesn't overclaim — it says the conversion is "mechanical," not that it's practical or ergonomic.

**Self-grounding is appropriate here.** The lemma is a formal argument, not an empirical claim. It doesn't need external grounding beyond the base model it references. ✓

---

No WARN. No INFO. Clean grounding for a formal note.
