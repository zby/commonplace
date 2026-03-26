=== SENTENCE-LEVEL REVIEW: baseline.md ===

Checks applied: 4

WARN:
- [parsing-ambiguity] "The mistake is not storing a trace. The mistake is letting a session runtime decide..." — "not" can negate "mistake" (it's no mistake to store) or "storing" (the mistake is failing to store). Both readings are plausible on first pass; the intended meaning (storing is fine, the mistake is something else) only becomes clear from the next sentence.
  Recommendation: Rewrite to remove the negation ambiguity, e.g. "Storing a trace is not the mistake. The mistake is letting..."

- [framing-mismatch] "For orchestration, that is usually the wrong trade" — frames the problem as orchestration-specific, but the mechanism (irrelevant history consuming bounded context) applies to any LLM call that needs full cognitive capacity. The bullet list that follows is already general (context pollution, implicit interfaces, re-interpretation cost). The orchestration framing understates the scope.
  Recommendation: Drop the orchestration qualifier or widen the framing, e.g. "For any call that needs focused context, that is usually the wrong trade."

- [misleading-link-text] "[compression at the execution boundary](./distillation.md)" (line 74) — the link target `kb/notes/distillation.md` does not exist (the distillation definition lives at `kb/notes/definitions/distillation.md`). Even if it resolved, the link text "compression at the execution boundary" implies a note specifically about boundary compression, but the target is a general definition of distillation as a knowledge-compression concept. A reader following this link would find a broader definition than the link text promised.
  Recommendation: Fix the broken path to `./definitions/distillation.md` and adjust the link text to "distillation," or keep the current text and link to a section that specifically discusses execution-boundary compression.

INFO:
- [parsing-ambiguity] "Raw history is the easiest way to preserve maximum information when the caller does not yet know what matters" — "when" can attach to "easiest" (easiest in the circumstance when the caller doesn't know) or to "preserve" (preserve information during the period when the caller doesn't know). The intended reading (easiest in that circumstance) dominates, but a reader skimming may initially attach "when" to the closer verb "preserve."

- [misleading-link-text] "[ad-hoc prompts](./ad-hoc-prompts-extend-the-system-without-schema-changes.md)" (line 77) in "the callee need not inherit the caller's search trace (ad-hoc prompts)" — the sentence uses ad-hoc prompts to exemplify clean handoff boundaries, but the target note is about extensibility without schema changes, not about trace inheritance or handoff. The connection exists (ad-hoc prompts do create selection boundaries) but requires the reader to make an inferential leap the link text does not signal.

- [stock-phrases] "This is not just summarization — it is interface design." (line 81) — uses the "not just X — it is Y" elevation move. The reframe from content operation to architectural concern does add something the bullets above do not state, so it is not pure filler. Borderline.

CLEAN:
- [stock-phrases] No other sentences matched the stock-phrase deletion test. Sentences like "The key separation is not 'store vs discard' but 'persist in symbolic state vs load into bounded context'" use the contrastive form but carry the note's core argument — deleting them would lose information.
- [parsing-ambiguity] Remaining sentences parse unambiguously. Pronoun references ("it preserves everything" on line 38 — antecedent is "trace-preserving handoff" from earlier in the sentence) are clear.
- [misleading-link-text] The other three checked links — [bounded-context orchestration model], [tool loop index], [scoping note] — set expectations that match their targets.

Overall: 3 warnings, 3 info
===
