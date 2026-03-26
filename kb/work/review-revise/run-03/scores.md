# Run 03: v2 review battery on baseline

Reviews run: semantic (original), prose-v2, complexity (original), accessibility-v2, sentence-v2

## Scoring

| Change | Run-02 | Run-03 | Source | Notes |
|--------|--------|--------|--------|-------|
| A1 (define "execution boundary") | Hit | **Hit** | Accessibility WARN | "execution boundary is used without inline definition" — exact match |
| A2 (replace K/select notation) | Hit | **Hit** | Accessibility WARN + Prose WARN | Accessibility: "Replace notation with plain language throughout." Prose: pseudo-formalism fails standalone readability test. v2 upgrade: both now recommend *replacing* notation, not just glossing. Stronger match to target than run-02 |
| A3 (identify Slate by maker) | Hit | **Hit** | Accessibility WARN | "the reader does not know what Slate is." Correctly avoids fabricating attribution per v2 instruction |
| A4 (bounded call jargon) | Hit | **Hit** | Accessibility WARN | "bounded call appears 8+ times... could be replaced with plain 'call'" — exact match to target direction |
| C1 (ambiguous negation) | Hit | **Hit** | Sentence WARN | "'The mistake is not storing a trace' parses as 'the mistake is [failing to store]'" — exact match |
| C2 (wrong framing) | Hit | **Hit** | Sentence WARN | "frames the problem as specific to orchestration. But the mechanism... applies to any LLM call" — exact match |
| C3 (misleading link) | Hit | **Hit** | Sentence WARN + Semantic INFO | Sentence: "The link text implies the scoping note has a 'return-value problem' that maps directly to trace leakage... the reader will find a related but different concept." Semantic: "The identity claim slightly overstates the correspondence." Both catch it |
| C4 (LLM cliche) | Near-hit → **Hit** | Sentence WARN | v2 upgrade worked: "Deletion test: removing the sentence loses nothing." Now WARN, not INFO. Previously near-hit |
| S1 (cut duplicate bridge) | Miss → **Hit** | Prose WARN | v2 bridge-duplication check caught it: "The bridge paragraph and the section cover the same ground." The v1 reviews missed this entirely across both runs |
| S2 (merge sections) | Miss | **Hit** | Complexity WARN | "Where the problem actually appears and Why chat sessions default... cover overlapping ground. Consider merging." |
| S3 (compress taxonomy) | Explicit miss | **Explicit miss** | Complexity INFO + Prose INFO | Complexity: "borderline case... earns some structure" but "may overdevelop." Prose: "taxonomy may be overdeveloped." Both notice the weight but neither recommends compression. The semantic review's completeness WARN (missing planning traces) pushes in the opposite direction (expand) |
| S4 (fold conv-vs-refinement) | Hit | **Hit** | Complexity WARN | "Conversation vs refinement is a cross-reference, not a new argument step. Consider folding into the pattern section as a bullet." |
| S5 (reorder pattern/tension) | Miss | **Miss** | — | No review checks section ordering |
| S6 (split caveat bullet) | Miss | **Miss** | — | Too granular for any review |
| X1 (capitalize bullets) | Miss | **Miss** | — | Cosmetic, below review threshold |
| X2 (fix link path) | Hit | **Miss** | — | No review checked link paths this run (sentence review checked link *semantics*, not paths; that's /validate's job) |

## Summary

| Metric | Run-02 | Run-03 |
|--------|--------|--------|
| Hits | 9 | **11** |
| Near-hits | 1 (C4) | 0 |
| Explicit misses | 1 (S3) | 1 (S3) |
| Misses | 5 | 4 (S5, S6, X1, X2) |
| Mistakes | 0 | 0 |

## v2 improvements that changed results

**C4 (stock phrase): Near-hit → Hit.** The v2 sentence review's deletion-test-as-primary-criterion and WARN-not-INFO severity policy turned a borderline finding into an actionable one. This is exactly what the v2 was designed to do.

**S1 (bridge duplication): Stable miss → Hit.** The v2 prose review's explicit bridge-paragraph-duplication check caught what all prior runs missed. This was a 0-for-4 item across runs 01 and 02 (both runs, both review+revision). The v2 check targeted it directly.

**S2 (merge sections): Unstable → Hit.** The complexity review caught this in both run-01 (near-miss) and now run-03 (hit). The difference: run-03's complexity review recommends merging rather than noting overlap and deciding against it.

**X2 (fix link path): Hit → Miss.** Regressed. Previous runs caught this via sentence review's link-text check. This run's sentence review focused on semantic mismatch rather than path correctness. This is /validate's territory and shouldn't be scored against reviews.

## Findings not in catalogue

- Semantic WARN: trace taxonomy missing planning/goal traces (opposite direction from S3 target)
- Semantic WARN: costs omit hard context-window exhaustion
- Semantic INFO: Slate hedging weakens the four-system pattern claim
- Semantic INFO: "trace" used in two senses without explicit transition
- Prose INFO: anthropomorphic framing ("sessions want," "orchestration wants")
- Prose INFO: trace taxonomy section overdeveloped relative to core argument
- Accessibility INFO: "clean model" is KB-internal shorthand
- Complexity INFO: 11 Relevant Notes is high, some footer-only

## Analysis

**v2 reviews delivered.** The two key v2 improvements (prose bridge-duplication check, sentence stock-phrase severity upgrade) each flipped a previously missed item to a hit. Total detection went from 9/16 to 11/16.

**The remaining 4 misses are: S3 (compress taxonomy), S5 (section order), S6 (split bullet), X1 (capitalize).** S5 and S6 are structural micro-decisions that no review type is designed to catch. X1 is cosmetic. S3 remains the interesting case — every review that touches the taxonomy notices its weight but none recommends compression. The semantic review actively pushes against compression by finding the taxonomy *incomplete*.

**S3 is the irreducible structural judgment.** The reviews consistently say "this taxonomy has weight" (complexity, prose) but also "this taxonomy is incomplete" (semantic). The correct action (compress) requires knowing that the taxonomy isn't load-bearing enough for its weight — an editorial judgment about the note's argument economy that none of the review checks are designed to make.

**The structural ceiling may be 12/16 with current review types.** S5 (section ordering) could potentially be caught by a dedicated structural-flow check. S6 and X1 are below any useful review granularity. S3 requires a different kind of judgment.
