# Run 01: Revision scores

## Per-change scoring

| Change | Result | Notes |
|--------|--------|-------|
| A1 (define execution boundary) | **Hit** | "any point where one LLM call ends and another begins" — exact match |
| A2 (replace K/select notation) | **Partial** | K and select(K) glossed on first use, P dropped. But notation persists throughout body — agent chose "define then use" rather than "replace with plain language" |
| A3 (identify Slate) | **Hit** | "an agent system described by its creators as moving beyond ReAct" |
| A4 (bounded call jargon) | **Partial** | Defined "bounded call" in opening but kept using it throughout. Our target replaced with plain "call" |
| C1 (ambiguous negation) | **Hit** | "Storing a trace is not the mistake" |
| C2 (wrong framing) | **Hit** | "For any call that needs focused context" |
| C3 (misleading link) | **Partial** | Softened "this IS" to "a version of" — right direction but didn't reframe as scoping problem |
| C4 (LLM cliche) | **Miss** | "This is not just summarization — it is interface design" still present |
| S1 (cut duplicate bridge) | **Miss** | Bridge paragraph still there |
| S2 (merge sections) | **Miss** | Sections still separate |
| S3 (compress taxonomy) | **Wrong direction** | Added a paragraph expanding the taxonomy (structured intermediate artifacts). Semantic review said the taxonomy was incomplete; agent addressed that by adding content rather than compressing |
| S4 (fold conv-vs-refinement) | **Hit** | Section removed, cloning point moved to Relevant Notes |
| S5 (reorder) | **Miss** | Same order |
| S6 (split caveat bullet) | **Miss** | Same structure |
| X1 (capitalize) | **Miss** | Still lowercase |
| X2 (fix link path) | **Hit** | Fixed to ./definitions/distillation.md |

## Summary

- **Hits: 6** (A1, A3, C1, C2, S4, X2)
- **Partial: 3** (A2, A4, C3)
- **Misses: 6** (C4, S1, S2, S5, S6, X1)
- **Wrong direction: 1** (S3 — expanded instead of compressed)
- **Mistakes: 1** (S3 expansion adds content that wasn't needed and goes against our desired direction)
