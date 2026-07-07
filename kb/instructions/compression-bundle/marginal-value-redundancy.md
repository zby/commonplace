---
gate_id: compression/marginal-value-redundancy
name: Marginal-value redundancy
description: 'A true, consistent passage consumes space without adding enough marginal value to justify keeping it in its current form.'
type: kb/types/review-gate.md
lens: compression
watches: [body]
staleness: changed
---

## Failure mode

A passage is true and locally coherent, but it does not earn its space. The problem is not falsity or inconsistency; the problem is that the passage consumes context and attention without enough change in what the reader can understand, decide, verify, or do.

This gate catches redundancy that quality gates often miss because the redundant passage is defensible in isolation. A reviewer should ask whether the passage earns its space relative to the rest of the artifact, not whether it is accurate.

Bias this gate toward compression. Agent-written notes tend to accumulate defensible detail, caveats, and recap paragraphs. A passage should stay only when its current size and placement do work. If one phrase is useful but the passage as a whole is redundant, report WARN and recommend folding the phrase elsewhere.

Do not treat all restatement as redundancy. A passage may repeat a condition or contrast because its job is to change the reader's stance: closing the argument, marking the decision boundary, or making the consequence memorable. The question is whether the restatement adds uptake, not whether the proposition has appeared before.

## Test

Review the artifact's meaningful chunks at the granularity the text presents them. Do not preserve a chunk merely because it is true, well-written, or contains one useful phrase.

Run the deletion/folding test:

- What would break in the note's stated support route if this chunk disappeared?
- Is the value it adds proportional to the space and attention it takes?
- Could the useful part be folded into nearby prose with less context cost?
- Does the chunk change the reader's takeaway, decision, contrast, or memory of the argument?

Report **WARN** when the chunk should not remain in its current form. This includes chunks that are entirely deletable and chunks where a small useful part should be folded elsewhere.

Report **INFO** only when the reviewer is genuinely unsure whether the chunk is doing necessary reader work.

Report **PASS** when the chunk earns its current form: deleting or folding it would make the artifact harder to use, easier to misread, less grounded, less actionable, or less forceful as an argument.

Do not flag repetition merely because two sentences use similar words. Flag only when the later unit has no additional job. Do not flag deliberate restatement required by the artifact's own argument or workflow unless the restatement is placed where no reader or agent action depends on it.

Conclusions get one extra check before WARN: a conclusion may restate the core condition if it turns the mechanism into a stance, a warning, or an operational bet. Warn only when the conclusion merely repeats earlier text or smuggles in an unsupported stronger claim.

In the review output, report WARN and INFO findings for the chunks that need attention. Do not emit a PASS finding for every chunk inspected. If the gate passes, write one concise PASS summary for the artifact as a whole. If the gate warns, omit passing chunks unless one non-obvious pass prevents a likely false positive.

## Example (fail)

A note argues throughout that a rule applies only when a verifier is absent. A final `## Scope` section says: "This rule applies where no verifier exists; where a verifier exists, the verifier should decide. Mixed cases sit on a gradient." The gradient phrase is useful, but the standalone section mostly recaps what the note already established. Report WARN and recommend folding the gradient into the earlier mechanism paragraph.

## Example (pass)

A note argues that a rule applies only when a verifier is absent, then a `## Scope` section distinguishes tests, validators, human review, and model self-critique because readers commonly confuse them. The section adds boundary cases and prevents a likely misapplication, so it is not redundant.

A note states its condition in the mechanism paragraph, then returns to it in the conclusion as the practical stance the reader should remember. If the conclusion converts the condition into a clear decision rule or bet, do not flag it merely for restating the condition. Flag only any unsupported strengthening inside the conclusion.
