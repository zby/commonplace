# Run 02: Revision scores

## Per-change scoring

| Change | Result | Notes |
|--------|--------|-------|
| A1 (define execution boundary) | **Hit** | "any point where one LLM call ends and another begins" — exact match |
| A2 (replace K/select notation) | **Partial** | K and select(K) glossed on first use. Notation persists in body |
| A3 (identify Slate) | **Factual error** | "described by Yohei Nakajima" — WRONG. Slate is by Random Labs, not Nakajima. The review said to identify Slate; the agent hallucinated the attribution |
| A4 (bounded call jargon) | **Partial** | Defined in parenthetical but kept using throughout |
| C1 (ambiguous negation) | **Hit** | "The mistake is not that a trace was stored" — fixes ambiguity |
| C2 (wrong framing) | **Hit** | "Under bounded context" — correct reframe |
| C3 (misleading link) | **Hit** | Reframed to "frame-boundary interface problem" with clarifying clause |
| C4 (LLM cliche) | **Hit** | "This is not just summarization" sentence removed |
| S1 (cut duplicate bridge) | **Miss** | Bridge paragraph still there |
| S2 (merge sections) | **Miss** | Sections still separate |
| S3 (compress taxonomy) | **Miss** | Not compressed, but also not expanded (neutral) |
| S4 (fold conv-vs-refinement) | **Miss** | Section kept — complexity review only flagged as INFO, agent didn't act on it |
| S5 (reorder) | **Miss** | Same order |
| S6 (split caveat bullet) | **Miss** | Same structure |
| X1 (capitalize) | **Miss** | Still lowercase |
| X2 (fix link path) | **Hit** | Fixed to ./definitions/distillation.md |

## Summary

- **Hits: 5** (A1, C1, C2, C3, C4, X2) — actually 6
- **Partial: 2** (A2, A4)
- **Misses: 7** (S1, S2, S3, S4, S5, S6, X1)
- **Factual error: 1** (A3 — hallucinated Slate attribution)
- **Other mistakes: 1** (dropped ad-hoc prompts link from body based on sentence review finding)
