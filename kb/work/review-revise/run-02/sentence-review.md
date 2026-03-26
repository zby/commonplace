=== SENTENCE-LEVEL REVIEW: baseline.md ===

Checks applied: 4

WARN:
- [parsing-ambiguity] "The mistake is not storing a trace." (line 16) — parses as either "The mistake is [not storing] a trace" (failing to store is the error) or "The mistake is not [storing a trace]" (storing is not the error). The intended reading is the second, but the first is plausible — especially because the note's opening frames "what should be stored" as one of its two questions, priming the reader toward storage concerns.
  Recommendation: Rephrase to remove the ambiguity. E.g., "The mistake is not that a trace was stored. The mistake is letting a session runtime decide..."

- [framing-mismatch] "For orchestration, that is usually the wrong trade" (line 40) — frames the problem as orchestration-specific. But the mechanism (trace accumulation wastes cognitive budget in bounded context) applies to any LLM call that needs its full context for a demanding task, not only to multi-step orchestration. The orchestration framing narrows the reader's takeaway unnecessarily.
  Recommendation: Reframe in terms of the general mechanism. E.g., "Under bounded context, that is usually the wrong trade" — then the orchestration case follows as the primary example rather than the definitional scope.

- [misleading-link-text] "This is the return-value problem from the [scoping note](./llm-context-is-composed-without-scoping.md) in architectural form." (line 48) — The target's "The return value problem" section (line 59 of the target) discusses progressive typing of sub-agent return values and interface contracts at frame boundaries — it asks "what should the return type be?" The baseline sentence uses it to mean "traces leak across boundaries instead of clean return values." A reader following the link expecting to find the trace-leakage argument would find the typing/contract argument instead.
  Recommendation: Either adjust the link text to match what the target section actually discusses (e.g., "the frame-boundary interface problem") or add a phrase clarifying the specific connection (e.g., "the return-value problem — when the boundary has no declared interface, the transcript becomes the implicit return value").

- [misleading-link-text] "[compression at the execution boundary](./distillation.md)" (line 74) — Two problems. First, the path `./distillation.md` appears to be broken; the distillation note lives at `./definitions/distillation.md`. Second, even with a corrected path, the target is a general definition of distillation ("compressing knowledge so a consumer can act on it within bounded context"), not specifically about compression at execution boundaries. The link text implies a more specific concept than the target delivers.
  Recommendation: Fix the path to `./definitions/distillation.md` and adjust link text to match the general concept, e.g., "[distillation](./definitions/distillation.md) at the execution boundary."

- [misleading-link-text] "the callee need not inherit the caller's search trace ([ad-hoc prompts](./ad-hoc-prompts-extend-the-system-without-schema-changes.md))" (line 77) — The target note argues that natural language prompts absorb new requirements without schema changes. It does not discuss preventing trace inheritance or the caller's judgment-heavy selection as a trace isolation mechanism. The reader following the link expecting an argument about trace isolation would find an argument about system extensibility.
  Recommendation: Either drop the link (the parenthetical doesn't need one) or replace with a link to a note that actually discusses the handoff boundary created by caller-side selection.

INFO:
- [parsing-ambiguity] "Raw history is the easiest way to preserve maximum information when the caller does not yet know what matters" (line 32) — "when" could attach to "easiest" (raw history is easiest in the situation when...) or to "preserve" (preserve information at times when...). The intended reading (attaches to "easiest") is more natural, and the alternative reading is unlikely enough that this does not mislead, but the sentence could be tighter.

- [stock-phrases] "This is not just summarization — it is interface design." (line 81) — Matches the "not just X — it is Y" elevation pattern. The reframe (from compression to interface design) adds mild value, but the next sentence ("the deeper question is what `select` should load...") carries the same point more precisely. Deleting the elevation sentence would not lose argumentative force.

CLEAN:
- [parsing-ambiguity] The rest of the note's sentences parse unambiguously. Pronoun references are clear throughout — "it preserves everything" (line 38) clearly refers to the trace-preserving handoff property introduced in the same sentence. Negation scope is clear everywhere except the one case flagged above.

- [framing-mismatch] Most mechanism claims are framed at the right level of generality. In particular, "the packaging layer starts deciding what later calls inherit — and it defaults to 'everything'" (line 28) correctly identifies the mechanism (packaging-layer default) rather than over-attributing to orchestration or under-attributing to a specific framework.

- [stock-phrases] The note is generally lean. The "key separation" formulation on line 62 uses a "not X but Y" structure but is the core argument of its section, not filler. The practical principle section (lines 95-102) uses bold emphasis for orientation without stock phrasing.

Overall: 5 warnings, 2 info
===
