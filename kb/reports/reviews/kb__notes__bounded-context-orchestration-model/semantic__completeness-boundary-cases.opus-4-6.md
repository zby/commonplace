The note presents a formal model: the select/call loop over symbolic state K with bounded LLM calls, plus analysis of what makes selection hard.

---

**Framework: The select/call loop**

Grounding: "a symbolic scheduler over bounded LLM calls."

- Simplest: a single LLM call with no loop. K = initial state, one select, one call, done. ✓
- Most extreme: a million-step decomposition (MAKER is cited as an extreme instance). ✓
- Between: LLM-mediated scheduling (using an LLM call to decide the next step). Explicitly addressed as a "degraded variant" where the symbolic-orchestration invariant no longer holds. ✓
- Between: tool calling within a call. Explicitly addressed — "a useful inversion of control, but it does not change the architecture." ✓
- Between: parallel fan-out. Addressed: "changes the scheduling problem... but not the core structure." ✓
- Adjacent: **streaming/incremental calls** where the model produces partial results that affect the next token's generation. The model assumes discrete bounded calls, not streaming. INFO — streaming calls blur the boundary between "inside a call" and "between calls," which the model's clean separation doesn't address.

**What makes selection hard**

Three factors (sequential dependence, dual cost dimensions, framing matters). Each is well-grounded and connects to other KB notes. ✓

**The decomposition lemma** guarantees universality for programs satisfying preconditions. Boundary cases are addressed in the lemma's own note. ✓

No WARN. One INFO on streaming calls.
