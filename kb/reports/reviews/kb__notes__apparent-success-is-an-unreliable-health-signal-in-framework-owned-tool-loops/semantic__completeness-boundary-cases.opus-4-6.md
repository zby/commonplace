The note presents one main framework: three outcome types (primary-path success, fallback success, hard failure) with frameworks compressing the first two into "success."

---

**Framework: Three outcome types**

Grounding: "The standard tool loop merges three different outcomes into one visible state."

- Simplest: a tool call that succeeds on the primary path. No signal degradation. ✓
- Most extreme: a complex multi-step task where every tool call fails and the agent improvises an entirely different approach. The output looks normal but the infrastructure is completely broken. ✓
- Between: a task where most tool calls succeed via primary path but one triggers a fallback. The note's framework handles this — the single fallback masks one infrastructure issue. ✓
- Adjacent: **partial success via mixed paths** — a task partially completed via primary path and partially via fallback, where the user can see which parts worked differently. The note's framework treats outcomes as task-level (whole task success vs. failure), not step-level. INFO — the note could address step-level observability: knowing which specific tool calls fell back would be more actionable than knowing the overall task had "some fallback."
- Adjacent: **fallback producing a better result** — an LLM might find a more creative solution when the prescribed path fails. The note assumes fallback = degraded ("fidelity dropped"), but fallback could occasionally produce superior outcomes. INFO — the note frames fallback success as inherently degraded without acknowledging the possibility that improvised paths can sometimes be superior. This edge case doesn't undermine the core argument (the health signal is still unreliable either way) but the "degraded" framing is one-directional.

**Two observability remedies**

Synchronous reporting and asynchronous observation. Both are well-defined. The note doesn't claim these are exhaustive. ✓

No WARN. Two INFOs: step-level vs. task-level observability, and fallback-as-possibly-superior edge case.
