# Cleanup regression: three pilots under the cleaned method

The operator commissioned this handoff on 2026-09-27 for execution in a new
session. Its purpose is to test whether the step 1 cleanup of the five
governing files still produces complete, valid, publishable analyses, with
no worker stopped by a gap where a step now points at a type instead of
restating its fields. It reruns the same three pilots at the same pins as the
[citation-generation test](../agentic-memory-refresh/next-pilot-test.md).
This document prepares the test; no new analysis has been started.

## Command for the next session

Paste this instruction into a fresh session at the Commonplace repository root:

```text
Run the cleanup regression described in
kb/work/agentic-analysis-output-documents/cleanup-rerun-test.md. Act as the
workshop coordinator and delegate each analysis to a fresh source-only
coordinator with its mandatory fresh memory specialist. Complete the three
runs, audit instruction loading and gaps, compare the outputs with the
baseline runs, and record the comparison in the workshop. Follow the fixed
source pins and execution boundaries in that file.
```

## What changed and what the test must show

Between commits `f63cfd6e` and the HEAD recorded at startup (seven commits on 2026-09-27), the five files
were reorganized under one rule: types state what a produced document
contains; the skill and instructions state how it is produced. The main
skill fell from 5,445 to about 3,500 words and now points at the result type
for record fields. The epistemic instruction fell from 3,432 to about 1,450
words; its six output blocks and controlled values now live in the result
type under Lens outputs, and it has no standalone mode. The memory
instruction fell from 1,184 to about 740 words; the report type owns its
section contents. The result type grew from 4,605 to about 6,100 words and
is now the largest file. The current counts are in the
[workshop README](./README.md#cleanup-progress-step-1).

The produced documents' shape did not change. The test must show that
workers can still fill them from the reorganized text, and must expose any
requirement the cleanup dropped or left without a home.

## Fixed inputs and baseline

Run Dynamic Cheatsheet, Mem0 and Napkin again, in that order, at these exact
revisions. Verify checkout origins and commit objects; read commit-addressed
source without changing source worktrees.

| System | Repository | Checkout relative to repository root | Full commit | Public destination |
|---|---|---|---|---|
| Dynamic Cheatsheet | https://github.com/suzgunmirac/dynamic-cheatsheet | `related-systems/suzgunmirac--dynamic-cheatsheet` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | `kb/agentic-systems/reviews/dynamic-cheatsheet.md` |
| Mem0 | https://github.com/mem0ai/mem0 | `related-systems/mem0ai--mem0` | `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` | `kb/agentic-systems/reviews/mem0.md` |
| Napkin | https://github.com/Michaelliv/napkin | `related-systems/Michaelliv--napkin` | `7582d6a46f5a11995956e60a59c41a5b242109f1` | `kb/agentic-systems/reviews/napkin.md` |

The baseline is the run each destination currently pins:
`AAS-2026-09-27-dynamic-cheatsheet-03`, `AAS-2026-09-27-mem0-03` and
`AAS-2026-09-27-napkin-04`, produced under the pre-cleanup files. Their
retained results and local run directories stay unchanged; the comparison
reads them after the new runs are frozen. The
[reliability audit](../agentic-memory-refresh/reliability-rerun-20260927.md)
of the earlier reruns recorded twelve truncated worker read deliveries; the
skill read then exceeded the outer delivery limit by 218 tokens.

At startup record HEAD, the SHA-256 of each of the five files, working-tree
status and the actual worker models. Existing pilot reviews, retained results
and workshop records include uncommitted work; preserve it. Allocate fresh,
unused run IDs using the execution date. Do not reuse or overwrite any
earlier run.

## Execution and isolation

Follow the current [analysis skill](../../agentic-systems/instructions/analyse-agentic-system/SKILL.md)
and its contracts. Run one coordinator plus its memory specialist at a time,
reserving capacity for the specialist. Both lenses remain mandatory. Use the
same worker model and configuration as the baseline runs where available and
record any difference.

Create each coordinator with fresh context (for the collaboration tool,
`fork_turns="none"`). Supply only its source identity, checkout, pin, public
destination, fresh run ownership and the current method instructions. Tell it
the purpose is a fresh source-grounded analysis under the current method.
Explicitly supply repository doctrine if its runtime does not load it.
Require a similarly fresh memory specialist under the current handoff
contract. Do not give either worker this document, the baseline analyses,
audits, findings or failure examples. The workshop coordinator owns
scheduling, recovery and the comparison; workers own their disjoint
skill-defined outputs. Use completion events and owned output paths, not
agent-status listings.

Do not edit the five governing files, the schemas or producer code during
the trial. Correctable draft failures may be repaired under the unchanged
method; retain their evidence in worker traces. When a worker meets a gap in
the instructions, record the step, the quoted instruction text, what the
worker did instead and the affected output, and let the run continue if the
worker can complete it under the type contract. Stop dependent work only if
the gap prevents valid completion. Never bypass validation. Prior-analysis
exposure or uncertain publication follows the skill's failure rule.

## Evidence and acceptance

After each run, independently check its completed-run handoff. Audit all six
worker traces, including nested tool results, exit statuses and stderr.
Retain trace paths, hashes and model identities in a new dated cache
directory under `kb/reports/cache/agentic-analysis-output-documents/`.
Report inaccessible trace portions as audit gaps, not zero findings.

For each coordinator and specialist, record:

- **Loading.** Which of the five files, the run-state type and the command
  reference it loaded, at which step, how many bytes each delivery returned,
  and whether any delivery was truncated. Note whether the coordinator loaded
  the result type and the epistemic instruction before its step 3, as the
  skill now directs, and whether the memory worker loaded the four result-type
  sections its instruction names.
- **Gaps and dangling references.** Each point where the worker asked a
  clarifying question, invented a field or value, or followed a pointer to a
  section that did not supply what the step needed. Quote the instruction
  text.
- **Epistemic lens.** Whether the section carries the six blocks in the
  type's order with its controlled values, and whether any architectural
  status or candidate state was translated into a conclusion status.
- **Memory report and profile.** Whether the report follows the type's
  sections, whether curation values were used as the result type now defines
  them, and whether integration preserved per-value evidence.
- **Completeness against the baseline.** For each system, the counts of
  `SRC-*`, `CMP-*`, `OBJ-*`, `RTE-*`, `CLM-*`, `ABS-*` and `BAP-*` records,
  quote anchors, limitations, and the fourteen `memory-comparison`
  assessments and values, beside the baseline's. Explain each difference as
  a source-supported change, a stochastic difference, or a finding the
  cleaned method no longer elicits. Name any finding present in the baseline
  and missing or weakened here.
- **Effort.** Truncation, retries, reconciliation rounds and specialist
  corrections, beside the reliability audit's figures.

Run the existing bounded matrix, table and statistics checks against exactly
the three newly completed reviews, writing a fresh cache output directory.
Verify their result identities and hashes. A blocked pilot remains explicit;
do not substitute an old result to make a three-row output.

Write a new dated `cleanup-rerun-<date>.md` report in this workshop and link
it from its README. Include run IDs, pins, the five file hashes at start and
end, trace evidence, the per-worker records above, final validation,
downstream checks, limitations and the comparison with the baseline. Answer
separately: did any worker meet a gap, did every produced document validate
and publish, did completeness hold against the baseline, and did loading or
truncation change. Claim zero observed issues only within the inspected
evidence; three stochastic analyses do not establish a general result.

This commission covers these three analyses, guarded publication, bounded
consumer checks and the workshop report. It does not start the remaining
corpus refresh, change the five governing files, draw the step 2 partition,
alter comparison outputs beyond the fresh cache directory, or authorize Git
commits. Finish with the evidence-backed result or concrete blockers; do not
expand the trial or repair the method without a new instruction.
