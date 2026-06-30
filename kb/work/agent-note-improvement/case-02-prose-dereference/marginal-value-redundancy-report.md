# Marginal-Value Redundancy Review

**Gate:** kb/work/agent-note-improvement/compression/marginal-value-redundancy.md
**Target:** kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md

## Result
INFO

## Findings
- PASS: opening mechanism, paragraphs 1-4 — deletion would weaken the note's central claim: these paragraphs establish the code/prose contrast, the missing dereference operation, the point-of-use restatement prescription, and the normalized-check constraint.
- PASS: Costs section — deletion would remove new operational consequences: bulk, conditional branching, and verifier work are distinct costs that are not already made available by the mechanism paragraphs.
- INFO: Scope section — it repeats the earlier formal-system/prose contrast and the distance/non-obviousness condition, so the gate catches it as a likely marginal-value problem; however, it also adds a graded representational-form boundary that blocks the likely misread that every prose-adjacent artifact needs the same amount of restatement. Deleting it outright would lose that constraint, but keeping it as a standalone section spends more attention than the new content earns.
- PASS: Testing it section — deletion would remove the note's falsifiable form and ablation design, which are not supplied elsewhere.
- PASS: Relevant Notes entries — each entry gives a navigational relation with a distinct role: grounds, contrasts, exemplifies, or extends. They are not interchangeable repeats.

## Suggested Revision
Fold the Scope section into the main mechanism instead of deleting it. Keep the representational-form gradient, but attach it near the first formal-system/prose contrast or the prescription paragraph: codified artifacts dereference reliably; prose does not; mixed or local/obvious cases need proportionally less reinforcement. This preserves the useful boundary while removing the standalone recap.
