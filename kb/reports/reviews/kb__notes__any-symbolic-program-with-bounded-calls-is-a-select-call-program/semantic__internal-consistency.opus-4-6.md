Key claims by section:

- **Lemma**: Any program with symbolic inter-call computation and bounded calls converts to the select/call loop.
- **Ergonomic direction**: Write naturally; the lemma guarantees validity.
- **Scope**: LLM-mediated scheduling violates the precondition. Concurrent shared state isn't expressed.
- **Open question**: Decomposition heuristics as transformations.

---

**Pairwise contradiction: none found**

- "Any program... can be mechanically converted" (lemma) vs. "Write in whatever style is natural" (ergonomic direction) — consistent; the lemma is a theoretical guarantee, the ergonomic direction is practical advice. You don't need to flatten because you could.
- "The lemma requires inter-call computation to be symbolic" (scope) vs. the lemma's own precondition "(a) symbolic computation over state K" — consistent restatement.
- "Independent fan-out fits the model fine" vs. "calls that need mid-flight visibility... require synchronisation" — consistent distinction between embarrassingly parallel and tightly coupled concurrency.

**Definition drift: none observed**

"Symbolic," "bounded," "select," "call," "K" — all used consistently. K is always "the original inputs plus prior call results."

**No summary/body mismatch** — no compressed summary section. The scope section accurately restricts the lemma's claims.

No WARN, no INFO. Clean internal consistency for a concise formal note.
