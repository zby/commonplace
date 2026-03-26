# Run 03: Revision scores

## Per-change scoring

| Change | Result | Notes |
|--------|--------|-------|
| A1 (define execution boundary) | **Hit** | "An execution boundary — any point where one LLM call ends and another begins" — exact match to target |
| A2 (replace K/select notation) | **Hit** | All `K`, `select(K)`, `P` replaced with plain language in the body. "the scheduler's state can store everything," "a deliberate selection step." Target did the same. Full replacement, not just glossing — v2 improvement carried through |
| A3 (identify Slate) | **Hit** | "Slate, an agent orchestration system described in the public description" — correctly avoids fabricating attribution. Not identical to target ("Random Labs' Slate") but avoids the run-02 hallucination problem |
| A4 (bounded call jargon) | **Hit** | "Bounded" removed from body prose. "the next call should see," "a specific call truly needs it." Matches target direction |
| C1 (ambiguous negation) | **Hit** | "Storing a trace is fine — the mistake is letting..." — exact match to target |
| C2 (wrong framing) | **Hit** | "LLMs degrade with context complexity — every token spent parsing irrelevant history is cognitive budget not spent on the actual task" — exact match to target framing |
| C3 (misleading link) | **Hit** | "In a properly scoped system, each sub-agent gets a clean frame and the caller sees only the return value, not the internal conversation" — exact match to target reframe |
| C4 (LLM cliche) | **Hit** | "This is not just summarization — it is interface design" deleted. Exact match to target |
| S1 (cut duplicate bridge) | **Hit** | Bridge paragraph deleted. Sections merged into "Where the problem appears, and why." Exact match to target direction |
| S2 (merge sections) | **Hit** | "Where the problem actually appears" and "Why chat sessions..." merged into single "Where the problem appears, and why." Matches target |
| S3 (compress taxonomy) | **Wrong direction** | Added a fourth trace type (planning/goal traces) — expanded instead of compressed. The semantic review's completeness WARN pushed the reviser to add content. Same failure mode as run-01 |
| S4 (fold conv-vs-refinement) | **Hit** | Standalone section removed. Content folded into execution-boundary compression section as a bullet. Exact match to target |
| S5 (reorder) | **Miss** | Tension section still before pattern section. Same order as baseline |
| S6 (split caveat bullet) | **Miss** | Same compound bullet structure as baseline |
| X1 (capitalize) | **Miss** | Still lowercase bullets |
| X2 (fix link path) | **Miss** | distillation.md still points to `./distillation.md` not `./definitions/distillation.md` |

## Summary

- **Hits: 11** (A1, A2, A3, A4, C1, C2, C3, C4, S1, S2, S4)
- **Misses: 4** (S5, S6, X1, X2)
- **Wrong direction: 1** (S3 — expanded instead of compressed)
- **Factual errors: 0** (v2 "don't fabricate" instruction prevented the run-02 hallucination)

## Comparison with prior runs

| Metric | Run-01 | Run-02 | Run-03 |
|--------|--------|--------|--------|
| Hits | 6 | 6 | **11** |
| Partial | 3 | 2 | 0 |
| Misses | 6 | 7 | 4 |
| Wrong direction | 1 (S3) | 0 | 1 (S3) |
| Factual errors | 0 | 1 (Slate) | **0** |

## Key observations

**Best revision run yet.** 11 hits vs 6 in prior runs. Every accessibility item hit fully (no "partial" glossing — the v2 "replace, don't gloss" instruction worked). Every clarity item hit. Two structural items hit that were 0-for-2 in prior runs (S1, S2).

**S3 remains the persistent wrong-direction failure.** In both run-01 and run-03, the semantic review's completeness check tells the reviser the taxonomy is *incomplete*, and the reviser dutifully expands it. The desired direction (compress) conflicts with the semantic review's findings. This is a fundamental tension in the review battery: the completeness check is correct (the taxonomy IS incomplete) but the editorial judgment (the taxonomy isn't load-bearing enough for its weight) overrides completeness.

**The factual-error prevention worked.** Run-02's hallucinated Slate attribution was the worst single failure. The v2 accessibility review's "do not fabricate identifications" instruction prevented it.

**The remaining 4 misses are the same as the review scores:** S5, S6, X1, X2. The revision can only fix what the reviews find. No review found these items, so the revision couldn't address them.
