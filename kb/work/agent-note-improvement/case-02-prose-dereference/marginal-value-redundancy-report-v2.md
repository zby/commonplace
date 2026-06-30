# Marginal-Value Redundancy Review v2

**Gate:** kb/work/agent-note-improvement/compression/marginal-value-redundancy.md
**Target:** kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md

## Result
WARN

## Findings
- PASS: opening mechanism paragraphs — deleting any of these would weaken the central contrast between code dereference, prose interpretation, and denormalized reinforcement; each paragraph advances the mechanism rather than recapping it.
- PASS: denormalization/check paragraph — keeps a necessary distinction between denormalized reader-facing copy and a normalized external verifier; deletion would make the recommended action less safe.
- PASS: Costs section — adds new constraints on the recommendation: bulk, conditional applicability, and verifier work. These are not already available in the opening claim and they prevent over-application.
- WARN: Scope section — the representational-form gradient is useful, but the standalone section mostly repeats the note's established contrast between codified dereference and prose reinforcement. Deleting the section would not change the core claim; folding the graded boundary into the earlier mechanism would preserve the useful phrase at lower context cost.
- PASS: Testing it section — supplies the falsifiable form, ablation, and disconfirmation condition. Deleting it would make the note less grounded and easier to treat as settled rather than seedling.
- PASS: Relevant Notes entries — each entry gives a distinct navigational relation: grounding, contrast, exemplification, extension, or relationship to scoping. The entries are not merely title repetition.

## Suggested Revision
Delete `## Scope` as a standalone section. Fold its marginal value into the second or third body paragraph, for example by adding that the need for reinforcement is graded by representational form, locality, and obviousness: codified declarations dereference reliably, while prose-like, distant, and non-obvious applications need more point-of-use reinforcement. Keep the Costs and Testing sections unchanged.
