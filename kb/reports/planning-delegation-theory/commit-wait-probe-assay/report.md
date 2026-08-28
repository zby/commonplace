# Commit / wait / probe assay evidence

## Result

The assay was inconclusive and is not decision-useful. Treatment posture
accuracy was 8/8; control accuracy was 7/8. The preregistered rule required a
two-case advantage. Neither arm produced false deferral or unnecessary
overhead, and both met all 27 substantive case requirements.

| Measure | Control | Treatment |
|---|---:|---:|
| Expected posture | 7/8 | 8/8 |
| Correct option activation | 7/8 | 7/8 |
| False deferrals | 0 | 0 |

The sole difference was a label. When an authorized first phase would later
produce discriminating evidence, control proposed the right bounded action but
called it a `probe`; treatment called it `wait`. This does not establish a
material planning improvement.

No instruction, skill, schema, validator, or code change follows from this
result. The current wording remains in place by status quo, not because this
assay validated it.

## Retained evidence

The [preregistered design](./README.md), cases, rubric, runner, frozen packets,
planner responses, blind judgment, opaque codebooks, and
[joined scores](./generated/scored-results.json) remain in this directory. They
pin the exact instruction variants and are sufficient to audit or redesign the
assay.

Sixteen fresh `gpt-5.6-sol` planners at medium reasoning produced one response
per cell. A separate fresh judge scored shuffled responses before the condition
mapping was joined. One treatment response contained a stray closing
parenthesis. The [original malformed output](./generated/invalid-responses/trial-d738b4a5763e.attempt-1.invalid.txt)
and same-agent syntax-only correction are both retained. Counting that first
attempt as failed would still leave the result inconclusive.

## Before repeating

The output contract named and defined every decision class, likely teaching the
control much of the tested distinction. The explicit cases also produced a
ceiling effect, and one run per cell supplied no variance estimate. The option-
activation rubric additionally conflated declining unwarranted work with
entering the costly-commitment comparison.

A repeat should:

- request an ordinary recommendation, then classify it independently;
- run each cell more than once;
- use less explicit boundary cases; and
- fix the option-activation rule before dispatch.
