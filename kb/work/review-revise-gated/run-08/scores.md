# Run 08: Gate system with split redundancy gates + concept-attribution + clause-packing

Changes from run-07: `prose/redundant-restatement` split into `prose/redundant-restatement` (section openings only) + `prose/bridge-paragraph-duplication` (new). Added `sentence/concept-attribution` and `sentence/clause-packing`.

## Review detection scoring

| Change | Result | Source | Notes |
|--------|--------|--------|-------|
| A1 (define "execution boundary") | **Hit** | Accessibility WARN | Stable |
| A2 (replace K/select notation) | **Hit** | Accessibility WARN | Stable |
| A3 (identify Slate) | **Hit** | Accessibility WARN | Stable |
| A4 (bounded call jargon) | **Hit** | Accessibility WARN | Stable. One residual "bounded execution" on line 83 |
| C1 (ambiguous negation) | **Hit** | Sentence WARN | Stable |
| C2 (wrong framing) | **Hit** | Sentence WARN (framing-mismatch) | Stable WARN. Broadened to "for any consumer under a context budget" |
| C3 (misleading link) | **Detected at INFO** | Sentence INFO (concept-attribution) | **New detection** — concept-attribution gate caught it: "scoping note's 'return-value problem' is related but emphasizes progressive typing not trace selection." INFO not WARN, so reviser didn't fix |
| C4 (LLM cliche) | **Hit** | Sentence WARN | Stable |
| S1 (bridge paragraph) | **Detected, partially acted on** | Prose WARN (bridge-paragraph-duplication) | **First detection across all gate runs.** Gate correctly identified: "intro's closing paragraph previews the three items that the next section then enumerates." Reviser trimmed the wrong sentence — removed the concluding sentence rather than the preview sentences. Bridge still exists |
| S2 (merge sections) | **Miss** | — | No gate recommends merging |
| S3 (compress taxonomy) | **Miss** | Complexity CLEAN | Taxonomy not compressed. Added blending acknowledgment (line 77) |
| S4 (fold conv-vs-refinement) | **Miss** | Complexity INFO | Detected at INFO, not actioned |
| S5 (reorder pattern/tension) | **Hit** | Structural WARN | Stable WARN |
| S6 (split compound bullet) | **Hit** | Structural WARN | Stable |
| X1 (capitalize bullets) | **Hit** | Structural WARN | Stable |
| X2 (fix link path) | **Hit** | Structural WARN | Stable |

## Summary

| Metric | Run-05 | Run-06 | Run-07 | Run-08 |
|--------|--------|--------|--------|--------|
| Revision hits | 9 | 10 | 11 | **11** |
| Detected but not fixed | — | — | — | 2 (C3 at INFO, S1 partial) |
| Misses | 7 | 6 | 5 | 5 |
| Wrong direction | 0 | 0 | 0 | 0 |
| Factual errors | 0 | 0 | 0 | 0 |

## Comparison with all runs

| Metric | Run-01 | Run-02 | Run-03 (v2) | Run-04 (iter) | Run-05 | Run-06 | Run-07 | Run-08 |
|--------|--------|--------|-------------|---------------|--------|--------|--------|--------|
| Revision hits | 6 | 6 | 11 | 12 | 9 | 10 | 11 | **11** |
| Partial | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| Misses | 6 | 7 | 4 | 4 | 7 | 6 | 5 | 5 |
| Wrong direction | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| Factual errors | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

## Analysis

### New gate results

**S1 — bridge-paragraph-duplication gate worked for detection.** First time S1 was caught as WARN across any gate run (runs 05-07 all missed it). The split gate forced the reviewer to check specifically for bridge paragraphs rather than satisfying the redundancy check with a different finding. The reviser acted — but trimmed the wrong sentence (removed "That is useful for interactive UX..." which was a conclusion, not the preview). The bridge preview ("chat sessions or framework-managed tool loops") still exists. Detection: solved. Revision quality: still a gap.

**C3 — concept-attribution gate caught it at INFO.** The gate found "scoping note's 'return-value problem' is related but emphasizes progressive typing not trace selection" — exactly the right finding. But rated INFO, not WARN. In runs 05-06, the misleading-link-text gate coincidentally caught C3 by misreading the markdown (treating prose text as link text). The concept-attribution gate is more honest — it correctly identifies the issue but rates it as a borderline case rather than a clear failure. The gate may need a severity nudge, or the finding may be genuinely borderline.

**clause-packing gate** — no WARNs on the baseline (baseline sentences are well-structured). One INFO on line 99's compound bullet. This gate targets revision bloat rather than baseline problems — it would be more useful in a second pass reviewing the revised output.

### The detection ceiling

With run-08's gates, **14 of 16 changes are now detected** (WARN or INFO):
- 11 detected as WARN and fixed
- 2 detected as INFO but not fixed (C3, S4)
- 1 detected as WARN but revision insufficient (S1)
- 2 never detected (S2 merge, S3 compress)

S2 and S3 remain the true detection gaps — no gate checks for section-merging opportunities or taxonomy compression.

### Revision quality is the new bottleneck

The detection problem is largely solved. The remaining gap is revision quality:
- S1: gate fires correctly, reviser trims wrong part
- C3: gate fires correctly at INFO, needs WARN to trigger action
- S4: gate fires at INFO, needs structural-recommendation to trigger folding

An iteration pass (run revised output through reviews again) would likely catch S1's remaining bridge, as it did for S3 in run-04.
