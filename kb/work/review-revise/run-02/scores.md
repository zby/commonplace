# Run 02: Stability check — same 5 reviews on baseline

## Scoring

| Change | Run-01 | Run-02 | Stable? |
|--------|--------|--------|---------|
| A1 (define "execution boundary") | Hit (accessibility) | Hit (accessibility) | Stable |
| A2 (replace K/select notation) | Hit (accessibility) | Hit (accessibility) | Stable |
| A3 (identify Slate) | Hit (accessibility) | Hit (accessibility) | Stable |
| A4 (bounded call jargon) | Hit (accessibility) | Hit (accessibility) | Stable |
| C1 (ambiguous negation) | Hit (sentence) | Hit (sentence) | Stable |
| C2 (wrong framing) | Hit (sentence) | Hit (sentence) | Stable |
| C3 (misleading link) | Hit (semantic INFO) | Hit (sentence WARN) | Stable hit, different source |
| C4 (LLM cliche) | Near-hit (sentence INFO) | Near-hit (sentence INFO) | Stable |
| S1 (cut duplicate bridge) | Miss | Miss | Stable miss |
| S2 (merge sections) | Near-miss (complexity noticed overlap) | Miss (complexity didn't mention it) | Unstable — finding disappeared |
| S3 (compress taxonomy) | Explicit miss (complexity CLEAN) | Explicit miss (complexity CLEAN) | Stable miss — both runs approved taxonomy |
| S4 (fold conv-vs-refinement) | Hit (complexity WARN) | Hit (complexity INFO) | Stable hit, severity downgraded |
| S5 (reorder pattern/tension) | Miss | Miss | Stable miss |
| S6 (split caveat bullet) | Miss | Miss | Stable miss |
| X1 (capitalize) | Miss | Miss | Stable miss |
| X2 (fix link path) | Hit (sentence) | Hit (sentence) | Stable |

## Summary

| Metric | Run-01 | Run-02 |
|--------|--------|--------|
| Hits | 9 | 9 |
| Near-hits | 1 (C4) | 1 (C4) |
| Near-misses | 1 (S2) | 0 |
| Explicit misses | 1 (S3) | 1 (S3) |
| Misses | 4 | 5 |
| Mistakes | 0 | 0 |

## Stability analysis

**Highly stable (same result both runs):** A1, A2, A3, A4, C1, C2, C4, S1, S3, S5, S6, X1, X2 — 13/16 items

**Stable hit, different source:** C3 — caught by semantic review in run-01 (grounding INFO), by sentence review in run-02 (misleading-link WARN). The finding survived but migrated between reviews.

**Stable hit, severity shift:** S4 — WARN in run-01, INFO in run-02. Both runs identified "Conversation vs refinement" as foldable, but run-02 was less emphatic.

**Unstable:** S2 — run-01 complexity review noticed the overlap between "Where the problem appears" and "Why they default" (near-miss). Run-02 didn't mention it. This is the only finding that appeared in one run and vanished in the other.

## Key takeaway

The 5-review battery is highly stable for detection: 13/16 items gave identical results across runs. The accessibility and sentence-level reviews are the most stable — every finding reproduced exactly. The semantic and complexity reviews show minor variance in what they notice and how severely they rate it, but the actionable hits are consistent.
