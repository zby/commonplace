The note presents one formal claim (the decomposition lemma) with two explicit preconditions, a consequence, and two scope limitations.

---

**Framework: The decomposition lemma**

Grounding: "Any program whose operations are (a) symbolic computation over state K and (b) bounded LLM calls r = call(P) can be mechanically converted into the base loop."

- Simplest: a program with one bounded call. `select(K)` is trivially the prompt constructor. The lemma holds. ✓
- Most extreme: a deeply nested program with many conditional branches, loops, and sequential calls. The lemma guarantees conversion by encoding all branching into `select(K)`. The argument (everything available at each call site is original inputs + prior results = K) is valid. ✓
- Between: a program with dynamic call count (bounded but data-dependent). The lemma requires bounded calls but doesn't require the count to be statically known. As long as each call's prompt is deterministically constructible from K, it qualifies. ✓

**Scope limitation 1: LLM-mediated scheduling**

"When the program uses an LLM call to decide what to do next, precondition (a) is violated." This is a clean boundary — the lemma's claim and its scope are aligned. ✓

**Scope limitation 2: Concurrent shared state**

"Independent fan-out fits the model fine. But calls that need mid-flight visibility into each other's results require synchronisation." This correctly identifies that the sequential base loop doesn't express concurrency. ✓

**Adjacent concept: stochastic programs**

A program where inter-call computation uses randomness (not an LLM, just random sampling). This satisfies precondition (a) if "symbolic" includes non-LLM stochastic computation. The note says "symbolic computation" which typically means deterministic. INFO — the note doesn't address whether stochastic-but-not-LLM inter-call computation satisfies the preconditions. This is a minor edge case.

No WARN. One INFO on stochastic non-LLM computation edge case.
