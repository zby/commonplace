=== SENTENCE-LEVEL REVIEW v2: baseline.md ===

Checks applied: 4

WARN:
- [parsing-ambiguity] "The mistake is not storing a trace. The mistake is letting a session runtime decide..." — On first read, "The mistake is not storing a trace" parses as "the mistake is [failing to store] a trace." The intended meaning is the opposite: "storing a trace is not the mistake." The two-sentence structure resolves the ambiguity, but the first sentence alone misleads.
  Recommendation: Rewrite to "Storing a trace is fine — the mistake is letting..."

- [framing-mismatch] "For orchestration, that is usually the wrong trade" — frames the problem as specific to orchestration. But the mechanism (context pollution degrades LLM performance) applies to any LLM call that needs focused attention, not just orchestration calls. The real issue is cognitive capacity, not the orchestration use case.
  Recommendation: Ground in the general mechanism: "LLMs degrade with context complexity — every token spent parsing irrelevant history is cognitive budget not spent on the actual task."

- [stock-phrases] "This is not just summarization — it is interface design." — Deletion test: the next sentence ("The execution boundary is the natural place to compress, but the deeper question is what `select` should load from stored state into the next bounded context") already states the substantive point. Removing the "not just X — it is Y" sentence loses nothing.
  Recommendation: Delete the sentence.

- [misleading-link-text] "This is the return-value problem from the [scoping note](./llm-context-is-composed-without-scoping.md) in architectural form" — The link text implies the scoping note has a "return-value problem" that maps directly to trace leakage. Reading the scoping note, its "return value" section discusses progressive typing of sub-agent returns (untyped → structured), not the question of whether transcripts leak across boundaries. The reader who follows the link will find a related but different concept.
  Recommendation: Reframe: "In a properly scoped system, each sub-agent gets a clean frame and the caller sees only the return value, not the internal conversation."

INFO:
(none)

CLEAN:
- [parsing-ambiguity] Other sentences with negation and modifier attachment were checked. "Raw history is the easiest way to preserve maximum information when the caller does not yet know what matters" — the "when" clause attaches slightly ambiguously (to "preserve" or to "easiest"?) but both readings support the same argument, so no misleading parse.

Overall: 4 warnings, 0 info
===
