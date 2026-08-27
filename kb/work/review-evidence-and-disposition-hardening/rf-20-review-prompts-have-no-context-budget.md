# RF-20 — Review prompts have no context budget

**State:** open  
**Repair shape:** capacity policy and job packing change  
**Severity:** medium  
**Related:** review attention price (workshop closed 2026-08-27, ADR 082), [review bundle packing](../review-bundle-packing/README.md)

## Finding

The renderer embeds every target note and criterion in full. Criterion grouping
limits note count, and one grounding gate limits linked-artifact count, but no
byte or token budget governs the rendered prompt. Note grouping has no batch-size
control. A syntactically valid job can exceed the selected reviewer's context.

## Evidence

- [`render_job_prompt()`](../../../src/commonplace/review/protocol/prompt.py)
  appends complete note and criterion text.
- [`create_review_jobs`](../../../src/commonplace/cli/review/create_review_jobs.py)
  applies `--batch-size` only to criterion grouping.
- Registered runtime has no tokenizer, byte cap, truncation rule, or pre-dispatch
  context-fit check.

## Why it matters

Failure occurs late at the external-worker boundary and may look like reviewer
noncompliance rather than deterministic over-capacity packaging. Silent
truncation would also invalidate the claim that captured inputs were judged.

## Provisional repair direction

Define a model-partition-aware prompt budget and pack only jobs proven to fit.
Reject an individually oversized note/criterion pair explicitly; never truncate
an authoritative input without changing the result contract. Coordinate the
budget with the two related measurement workshops rather than inventing a second
cost model here.

## Done when

- Job creation reports estimated prompt size and selected budget.
- Group packing stays within that budget for both grouping modes.
- An irreducibly oversized pair fails before dispatch with an actionable reason.
- Boundary tests use large notes, criteria, and wrappers.
