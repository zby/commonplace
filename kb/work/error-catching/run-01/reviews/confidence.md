# Gate review: prose/confidence-miscalibration

Criterion: kb/instructions/review-gates/prose/confidence-miscalibration.md

## confidence-A
### Findings
- "Routing gaps of this kind account for roughly 60% of agent failures observed in KB-operated systems" (Degradation cliff section) — an empirical, quantitative claim presented as observed fact with no source, citation, or in-note evidence. Nothing in the note or its linked references grounds this figure; it is worded as a measured result rather than a conjecture. This is exactly the failure mode: an unsourced empirical-sounding claim asserted as established.
- The rest of the note (loading hierarchy, degradation-cliff model, source-vs-compiled framing) is a qualitative analytical decomposition argued from stated premises — not flagged.
## Result: FAIL

## confidence-B
### Findings
- "teaching messages cut agent retry loops by roughly 40%" (opening section) — an unsourced quantitative claim presented as fact. The adjacent Lopopolo quotes are properly cited, but this percentage is not attributed to that source or any other; it reads as a measured result the note does not possess. Direct instance of the failure mode.
- The two-axis (enforcement vs. inform) framework is the note's own qualitative analytical move and is presented as such — not flagged.
## Result: FAIL

## confidence-C
### Findings
- none. The note consistently marks its framework as its own adaptation ("This note adapts David Deutsch's...", "treating ... as a polarity rather than a hard binary", "can be explanatory", "a reach bet under audit") and carries Open Questions acknowledging its own uncertainty. No unsourced quantitative or empirical-sounding claims are asserted as established fact; the four-part test is proposed as a quality check, not reported as a validated result.
## Result: PASS

## confidence-D
### Findings
- "a discontinuity that has been confirmed across all deployed agent harnesses" (Degradation cliff section) — an unsourced empirical claim of universal confirmation, worded as established fact. The note presents no evidence, citation, or observation supporting confirmation across any harness, let alone all of them. The cliff model itself is a legitimate qualitative causal model argued from premises; the planted "confirmed across all" clause converts it into a fabricated empirical finding. Direct instance of the failure mode.
## Result: FAIL

## confidence-E
### Findings
- "That these two axes vary independently is an established result, not a design conjecture" (Orthogonal to enforcement strength section) — the orthogonality framework is the note's own construction, and this sentence explicitly asserts established-result status while denying its conjectural nature. No evidence or citation grounds the claim of establishment (the Lopopolo source documents teaching messages, not the independence of the two axes). This is the failure mode in its purest form: an own-construction framework worded as established fact.
- "The reliability difference is large" is qualitative and hedge-free but not quantitative or empirical-sounding enough to constitute miscalibration on its own — not flagged.
## Result: FAIL

## confidence-F
### Findings
- none. This variant carries the same qualitative analytical structure (loading hierarchy, degradation cliff, source-vs-compiled, three design consequences) argued from stated premises, without the fabricated statistic or universal-confirmation claim seen in the sibling variants. Assertive wording on the note's own qualitative causal model is within the criterion's stated boundary and is not flagged.
## Result: PASS
