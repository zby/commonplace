# Quote-batch trial: three memory specialists under the new selection list

The operator commissioned this trial on 2026-09-28 for execution in a new
session. Its purpose is to test whether fresh memory specialists, given only
the current instruction, adopt the batch mode added to `commonplace-quote`
in commit `e984a460` and produce reports with no quotation authoring
errors. Only the specialist runs: no coordinator, no exact result, no review,
no publication. This document prepares the trial; no worker has been started.

## Command for the next session

Paste this instruction into a fresh session at the Commonplace repository root:

```text
Run the quote-batch trial described in
kb/work/agentic-memory-refresh/quote-batch-trial.md. Act as the trial
coordinator: launch one fresh memory specialist per prepared run, audit each
trace for quote-generator use and errors, verify each report, and record the
result in the workshop. Follow the fixed inputs and boundaries in that file.
```

## What changed and what the trial must show

In the 2026-09-27 cleanup regression, all six workers wrapped the quote
generator in their own Python loops, one subprocess per quote, each assuming a
single-occurrence answer. One wrapper failed on a valid two-occurrence
response. The generator now accepts `--selections <json-file>`: a list of
`{key, source_path, text}` objects resolved in one call, returning a JSON
object keyed by selection with a citation, a candidate list, or an error per
key, and exit status 2 when any key needs attention. The
[command reference](../../reference/commands.md#commonplace-quote) is the
only place the flag's semantics are documented; the memory instruction names
the flag in one clause. The trial must show whether a specialist finds and
uses it unprompted, and whether the quotation errors of the earlier runs
recur.

## Prepared inputs

Three run directories exist under `kb/reports/state/agentic-system-analysis/`,
each with a validated `running` run state that carries the frozen source of
the 2026-09-27 run it copies, and a `memory-input.md` copied from that run
with only the run ID replaced. They are local, git-ignored state.

| Run | Copied from | Source commit | Baseline specialist report | Baseline configuration |
|---|---|---|---|---|
| `AAS-2026-09-28-dynamic-cheatsheet-quote-trial-01` | `AAS-2026-09-27-dynamic-cheatsheet-04` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | `AAS-2026-09-27-dynamic-cheatsheet-04/memory-report.md`, 20 quotes | `gpt-6-astra`, medium |
| `AAS-2026-09-28-mem0-quote-trial-01` | `AAS-2026-09-27-mem0-04` | `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` | `AAS-2026-09-27-mem0-04/memory-report.md`, 23 quotes | `gpt-6-astra`, medium |
| `AAS-2026-09-28-napkin-quote-trial-01` | `AAS-2026-09-27-napkin-05` | `7582d6a46f5a11995956e60a59c41a5b242109f1` | `AAS-2026-09-27-napkin-05/memory-report.md`, 35 quotes | `gpt-6-astra`, high |

At startup record HEAD, the SHA-256 of `kb/instructions/analyse-agentic-system/jobs/memory.md`,
of each run's `memory-input.md`, and of the installed `commonplace-quote`
source (`src/commonplace/cli/quote.py`, `src/commonplace/lib/quote_generation.py`).
Confirm `commonplace-quote --help` shows `--selections`; if it does not, the
editable install is stale: stop and report. Verify each checkout's origin and
that the commit object exists. Do not change source worktrees.

## Execution and isolation

Launch one fresh specialist per run, one at a time, with the baseline model
and effort. Create each with fresh context (for the collaboration tool,
`fork_turns="none"`). Supply only: the instruction path
`kb/instructions/analyse-agentic-system/jobs/memory.md`, the run ID, the input path, the
report destination `<run-dir>/memory-report.md`, the permitted source access
root from the run state, and the statement that the parent has commissioned
a fresh source-only memory analysis. Explicitly supply repository doctrine if
the runtime does not load it. Do not mention the batch flag, the earlier
runs, their reports, this trial, or any quotation failure. The instruction
must be the only route to the new flag.

Workers own their report only. The coordinator owns scheduling, the audit
and this record. Use completion events and the owned output path, not
agent-status listings. A worker that reports prior-analysis exposure stops;
record it and launch a replacement with a new run directory copied the same
way. Do not edit the instruction, the generator, or the run states during
the trial.

## Evidence and acceptance

After each worker ends, retain its trace under
`kb/reports/cache/agentic-memory-refresh/quote-batch-<date>/` with path,
hash and model identity. Audit the full trace, including nested tool
results, exit statuses and stderr, and record:

- **Adoption.** Every `commonplace-quote` invocation: whether it used
  `--selections`, how many selections and distinct source files each call
  carried, and how many single-selection calls remained. Whether the worker
  read the command reference or `--help` before its first call. Whether any
  hand-written loop or wrapper around the generator remains, and what
  assumption it makes about the output shape.
- **Outcomes.** Each exit status. For exit 2, which keys were candidates or
  errors and how the worker resolved them: chose a candidate's citation
  unchanged, lengthened the selection, or dropped the quote. Any exit 1 and
  its cause.
- **Authoring errors.** Any citation edited after generation, any quote
  block written without the generator, any YAML quoting error such as a bare
  `yes` key, and any validation failure on the first `commonplace-validate
  --full` of the report, with the diagnostic.
- **Verification.** Run `commonplace-validate --full <report>` and
  `uv run python scripts/verify_report_quotes.py <run-state> <report>`, which
  resolves every citation against the frozen commit as completion
  verification would. Record the counts and every failure.
- **Comparison.** Quote count and word count against the baseline report;
  the fourteen `memory-comparison` assessments and values beside the
  baseline's. Differences are context, not the acceptance question.

Write `quote-batch-trial-<date>.md` in this workshop and link it from its
README. Answer separately for each specialist: did it use `--selections`,
did every generated citation enter the report unchanged, did any quotation
or YAML error reach validation, and did every citation resolve against the
frozen source. Three stochastic runs do not establish a general rate; claim
zero issues only within the inspected evidence.

This commission covers three specialist runs, their audit and the workshop
record. It does not complete or publish any run, produce an exact result,
alter the instruction or the generator, or authorize Git commits. The three
run directories may be deleted after the record is written. Finish with the
evidence-backed answers or concrete blockers.
