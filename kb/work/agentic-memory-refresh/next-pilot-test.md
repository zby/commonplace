# Next test: three pilots using generated citations

The operator commissioned this handoff on 2026-09-27 for execution in a new
session. Its purpose is to test whether the citation-generation workflow in
commit `5057c874` reduces quotation authoring errors in the same three pilots.
This document prepares the test; no new analysis has been started.

## Command for the next session

Paste this instruction into a fresh session at the Commonplace repository root:

```text
Run the three-pilot citation-generation test described in
kb/work/agentic-memory-refresh/next-pilot-test.md. Act as the workshop
coordinator and delegate each analysis to a fresh source-only coordinator,
with its mandatory fresh memory specialist. Complete the three runs, audit
generator use and quotation failures, and record the comparison in the
workshop. Follow the fixed source pins and execution boundaries in that file.
```

## Fixed inputs and baseline

Run Dynamic Cheatsheet, Mem0 and Napkin again, in that order, at these exact
revisions. The fixed pins override the workshop's general upstream-refresh
instruction for this test. Verify checkout origins and commit objects; read
commit-addressed source without changing source worktrees.

| System | Repository | Checkout relative to repository root | Full commit | Public destination |
|---|---|---|---|---|
| Dynamic Cheatsheet | https://github.com/suzgunmirac/dynamic-cheatsheet | `related-systems/suzgunmirac--dynamic-cheatsheet` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | `kb/agentic-systems/reviews/dynamic-cheatsheet.md` |
| Mem0 | https://github.com/mem0ai/mem0 | `related-systems/mem0ai--mem0` | `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` | `kb/agentic-systems/reviews/mem0.md` |
| Napkin | https://github.com/Michaelliv/napkin | `related-systems/Michaelliv--napkin` | `7582d6a46f5a11995956e60a59c41a5b242109f1` | `kb/agentic-systems/reviews/napkin.md` |

The workshop coordinator may read the [previous trial](./quote-rerun-20260927.md)
and [implementation acceptance](./citation-generation-change.md). The previous
trial had five failed source-check attempts, eight ambiguous quote blocks,
one altered quote block, eight out-of-bounds citation occurrences, six bare-URL
attribution errors and one copied-image-link error. Those categories overlap
within attempts. All final publications passed; final success alone is not
evidence of fewer authoring errors. The old `verify-sources` operation is gone,
so compare defect categories and denominators as well as command failures.

The implementation passed 950 tests and the final publication cleanup passed
23 targeted tests. This next test evaluates real authoring, not another unit
test run. At startup record HEAD, relevant code/instruction hashes, working-tree
status and actual worker models. Check whether the producer differs from
`5057c874`; if it does, establish and document the intended test revision before
launching workers. Do not silently test intervening producer changes.

Existing pilot reviews, retained results and workshop records include
uncommitted work. Preserve it. Use guarded publication to replace only the
three commissioned review destinations; allocate fresh, unused run IDs using
the execution date. Do not reuse or overwrite any earlier run.

## Execution and isolation

Follow the current [analysis skill](../../agentic-systems/instructions/analyse-agentic-system/SKILL.md)
and its contracts. Run one coordinator plus its memory specialist at a time,
reserving capacity for the specialist. Both lenses remain mandatory. Preserve
the previous worker model/configuration where available and record differences;
the previous six workers used `gpt-6-astra`.

Create each coordinator with fresh context (for the collaboration tool,
`fork_turns="none"`). Supply only its source identity, checkout, pin, public
destination, fresh run ownership and current method instructions. Tell it the
purpose is a fresh source-grounded analysis under the current citation workflow.
Explicitly supply repository doctrine if its runtime does not load it. Require
a similarly fresh memory specialist under the current handoff contract. Do not
give either worker this test document, earlier analyses, inventories, audits,
findings, or failure examples. The workshop coordinator owns scheduling,
recovery and the comparison; workers own their disjoint skill-defined outputs.
Use completion events and owned output paths, not agent-status listings.

Authors must receive the current citation instructions through the skill and
type contracts: use `commonplace-quote`, choose an occurrence, insert its
citation unchanged, and assess semantic support themselves. One occurrence
emits Markdown; two to ten emit candidates with metadata; more than ten asks
for a longer selection. Ordinary navigation references omit ranges unless
reusing generated locations. Do not add separate author quote checks or revive
`verify-sources`. Publication uses the regular validator. Keep prepare/publish
and the completed-run handoff checks prescribed by the skill.

Correctable draft failures may be repaired under the unchanged method; retain
their evidence in worker traces. Do not fix producer code or instructions
mid-trial. Record a discovered producer defect and its affected boundary; stop
dependent work if it prevents valid completion. Never bypass validation. Prior
analysis exposure or uncertain publication follows the skill's failure rule.

## Evidence and acceptance

After each run, independently check its completed-run handoff. Audit all six
worker traces, including nested tool results, exit statuses and stderr. Retain
trace paths, hashes and model identities in a new dated cache directory under
`kb/reports/cache/agentic-memory-refresh/`. Report inaccessible trace portions
as audit gaps, not zero failures. Avoid creating a worker-side phase or retry
ledger; the workshop audit summarizes the traces afterward.

For each coordinator and specialist, record:

- Whether the citation instructions were loaded and `commonplace-quote` was
  used; successful calls, rejected requests, and reasons. Count requests above
  ten occurrences separately as expected requests for a longer selection.
- Whether inserted citations match returned candidates unchanged, including
  citations copied from specialist to result. Record manual construction or
  alteration and cases where provenance cannot be established. This audits
  tool use; it is not another source-verification implementation.
- Quotation and range errors reaching structural validation or publication:
  failed attempts, individual diagnostics, distinct affected passages and
  repeated diagnostics. Separate lookup/selection retries from malformed
  emitted citations, insertion mistakes, validator defects and schema failures.
- Final quote counts by result, specialist report and compact review. Count
  the identical local and retained result only once. Report truncation and
  delegation problems separately, with recovery evidence where available.

Run the existing bounded matrix, table and statistics checks against exactly
the three newly completed reviews, writing a fresh cache output directory.
Inspect the existing scripts' help for their current interfaces. Verify their
result identities and hashes. Update only the three inventory pointers after
validated publication, preserving all other rows. A blocked pilot remains
explicit; do not substitute an old result to make a three-row output.

Write a new dated `citation-generation-rerun-<date>.md` report in this workshop
and link it from its README. Include run IDs, pins, producer start/end hashes,
trace evidence, failure denominators, final validation, downstream checks,
limitations and a comparison with the previous trial. Answer separately:
did authors use the generator, did it emit valid citations, did authoring
friction decrease, and did invalid quotations survive publication? Claim
zero observed issues only within the inspected evidence; three stochastic
analyses do not establish a general zero-error rate.

This commission covers these three analyses, guarded publication, bounded
consumer checks, inventory updates and the workshop audit. It does not start
the remaining corpus refresh, create a new landscape synthesis, change public
comparison outputs, alter the output-document design, or authorize Git commits.
Finish with the evidence-backed result or concrete blockers; do not expand
the trial or repair the producer without a new instruction.
