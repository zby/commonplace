# Run 04: Revision scores (iteration — second revision pass)

Scored against the original change catalogue, comparing run-04/revised.md to the target.

## Per-change scoring

| Change | Run-03 | Run-04 | Notes |
|--------|--------|--------|-------|
| A1 (define execution boundary) | Hit | **Hit** | Preserved from run-03 |
| A2 (replace K/select notation) | Hit | **Hit** | Preserved from run-03 |
| A3 (identify Slate) | Hit | **Hit** | Preserved from run-03 |
| A4 (bounded call jargon) | Hit | **Hit** | Preserved from run-03 |
| C1 (ambiguous negation) | Hit | **Hit** | Preserved from run-03 |
| C2 (wrong framing) | Hit | **Hit** | Preserved from run-03 |
| C3 (misleading link) | Hit | **Hit** | Preserved from run-03 |
| C4 (LLM cliche) | Hit | **Hit** | Preserved from run-03 |
| S1 (cut duplicate bridge) | Hit | **Hit** | Preserved from run-03 |
| S2 (merge sections) | Hit | **Hit** | Preserved from run-03 |
| S3 (compress taxonomy) | Wrong direction | **Hit** | RECOVERED. Run-03 expanded the taxonomy (4 detailed bullets). Run-04's reviews (complexity WARN, prose WARN) flagged the expansion as heavier than warranted. Reviser compressed to two flowing sentences. This is the key iteration result — the second pass corrected the first pass's mistake |
| S4 (fold conv-vs-refinement) | Hit | **Hit** | Preserved from run-03 |
| S5 (reorder) | Miss | **Miss** | Tension still before pattern. No review checks ordering |
| S6 (split caveat bullet) | Miss | **Miss** | Same compound bullet structure |
| X1 (capitalize) | Miss | **Miss** | Still lowercase |
| X2 (fix link path) | Miss | **Miss** | distillation.md still not updated to definitions/distillation.md. Semantic review flagged it as INFO but reviser didn't act |

## Summary

| Metric | Run-01 | Run-02 | Run-03 | Run-04 |
|--------|--------|--------|--------|--------|
| Hits | 6 | 6 | 11 | **12** |
| Partial | 3 | 2 | 0 | 0 |
| Misses | 6 | 7 | 4 | **4** |
| Wrong direction | 1 | 0 | 1 | **0** |
| Factual errors | 0 | 1 | 0 | **0** |

## Key findings

**Iteration corrected the S3 wrong-direction failure.** This is the headline result. Run-03's semantic review said the taxonomy was incomplete → reviser expanded it. Run-04's complexity + prose reviews said the expanded taxonomy was too heavy → reviser compressed it. The second review pass caught and corrected the first revision pass's error. The final taxonomy (two flowing sentences) is close to the target's compressed form.

**Iteration converged, didn't oscillate.** The 11 hits from run-03 all survived into run-04. No fix was undone. The only change was S3 moving from wrong-direction to hit. This answers one of the workshop's key questions: "Does iterating converge or oscillate?" — it converges, at least for this note.

**The ceiling is 12/16.** The remaining 4 misses (S5, S6, X1, X2) are structural micro-decisions and cosmetic items that no review type catches. These are below the review system's resolution.

**Two passes suffice for this note.** Pass 1 (run-03) caught 11/16. Pass 2 (run-04) caught 1 more and corrected 1 error. A third pass would likely find no actionable findings — the second-pass review already went CLEAN on accessibility and had only 4 WARNs total, all targeting the S3 expansion which is now fixed.

## Comparison with target

The run-04 revised note is structurally close to the manually edited target:
- Same section structure (merged "where/why," folded conv-vs-refinement)
- Same accessibility fixes (glossed execution boundary, plain language for notation, identified Slate)
- Same clarity fixes (ambiguity, framing, cliche, link)
- Similar taxonomy compression (prose summary rather than detailed enumeration)
- Main differences: section ordering (S5), bullet formatting (S6, X1), link path (X2)
