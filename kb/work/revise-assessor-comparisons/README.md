# Comparing revise assessor instructions

Posed by the operator on 2026-11-23. Does asking the assessor to compare contested edits with a smaller repair improve the *plan*, rather than just lengthen its explanation? Test outside the live revise workflow. No change to a note, controller, shipped prompt or operator decision is authorized by the trial.

The [cross-model replay](./replication.md) adds Sol and Opus arms; across three families the amendment shows no consistent plan benefit.

## First trial

Replay the two retained assessment packets discussed when proposing the change. Both historical criteria match the live one at `318458e48`. Use fresh assessors for both conditions. Keep the original task, supplied note, pass catalog, findings, reports, optional operator inputs and output contract. Change only step 1 of the criterion by inserting [the amendment](./amendment.txt) before the paragraph beginning “When readers scan”. Rebase file locations and restrict reads to the replay packet; this tests the captured inputs, not historical tool use or an exact historical harness. The old results are not inputs or an answer key.

Use four calls, one per case and condition. Blind the output comparison to condition. For the mixed case, look for a concrete gain or loss in the executable scope of the structural edit, retention of straightforward ambiguity repairs (positive control within the same case), and protection of the operator’s commitments. For the stop case, check that the dependent-changing claim decision still stops ordinary passes. Record over-deferral and the amount the operator must read. Treat an explanation with an unchanged plan as an explanation result, not an edit benefit. Neither case was sampled randomly; one observation per cell cannot distinguish a stable effect from run variation.

The [manifest](./manifest.json) records the original launch locations, prompt digests and the SHA-256 of every declared input. `packets/{mixed,stop}/task.txt` retains the task and output schema without the machine-specific path footer. Files under each `inputs/` have the original bytes with `.txt` appended to their names to keep them from being published as current KB notes. For replay, strip this suffix, bind the task to those input paths and to fresh output paths, and use the unmodified criterion for baseline. The absent purpose, must-keep, brief and earlier-decisions roles were not silently reconstructed: mixed supplies purpose and must-keep; stop supplies neither; neither launch supplied the last two roles.

Keep a portable assessor-input snapshot and manifest here; keep raw trial bundles in `kb/reports/state/revise-assessor-comparisons/`. Retain a blinded appraisal and summarize the plans. Close after deciding whether to drop, narrow or test the amendment on more cases and actual edits. Do not promote on this pilot alone.

## Result: better explanation in one case, no clear plan advantage

Four fresh Pi assessor sessions (gpt-6.2-astra), one per cell, and a fifth fresh condition-blind reader. X was baseline and Y amended in both independently shuffled pairs. [Blind appraisal](./blind-appraisal.txt); exact assessments and plans under `answers/{mixed-x,mixed-y,stop-x,stop-y}/`. All four plans passed the controller’s local `read_plan` checks. No passes were applied.

| Case | Plan difference | Assessment words, baseline → amended |
|---|---|---:|
| Mixed edits (20 supplied files) | Both kept the library example in place, scheduled the ASCII-name and routing-table clarifications, and preserved the stated commitments. Baseline trimmed the example’s repeated ending; amended retained it and scheduled identifying Commonplace instead. Four entries each. The blind reader preferred the amended placement rationale, not its plan by a clear margin. | 1,051 → 1,252 |
| Required stop (21 supplied files) | Both stopped with no passes and sent the meaning of “requires” and its dependent citations to the operator. The amendment did not turn that authority boundary into a trade-off. | 1,147 → 1,250 |

The historical mixed plan moved the example; the fresh baseline did not. Comparing the amended run to the historical output alone would have misattributed that difference. The amendment did not earn adoption in this pilot. Word counts are a reading-load proxy, not measured operator time. Reader outcomes, execution cost and repeatability were not tested. If continuing, use an independent case where a disputed edit recurs under repeated baseline assessment, then compare actual candidate texts on the reader task before changing the shipped instruction.
