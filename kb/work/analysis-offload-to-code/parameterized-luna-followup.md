# Luna follow-up: validator repairs work; reading and coverage remain uneven

- **Commission:** the operator approved native Codex tool guidance, source-operation coverage and record-overlap instructions, checks for detectable report defects, and two fresh Luna trials after the [first trace audit](./parameterized-luna-trace-audit.md).
- **Recorded:** 2026-10-01.
- **Result:** both final submissions pass their actual workflow validators; all nine retained quotations resolve. The new checks caused both workers to repair defects before submission. Traces still show incomplete reading, dropped statuses and unsupported inspection claims. Epistemic again omits the tidy route without marking it unassessed.

## Implemented method and verification

The worker rules give an ordinary `functions.exec` / `exec_command` example
that returns the whole command result, including status. They require
separate bounded reads, recovery of truncation at both tool levels, and
separate commands or `&&` for dependent work. No custom agent tool or
runtime wrapper was added.

Memory and epistemic instructions require source entry-point checks beyond
the supplied runtime, including evaluation, cleanup, rejection, withdrawal,
retained results and later consumers. Their contracts require a coverage
table and comparison with supplied record referents before declaring new
records. Operative parts with different checks or consumers need separate
assessment; reconciliation retains ownership of canonical splits.

Validation now rejects a complete memory report retaining
`Validation: pending`. Epistemic validation checks contiguous table grammar,
cell counts and controlled function/status values, or literal compact
record labels with those controlled values. These checks do not establish
semantic coverage, support, or completeness of the other ledger fields.

The method tested is `4dc11108ce8aa119bfefea35f41f324c16a4d253`.
A concurrent contract reorganization landed as `d77388b4`, with a further
gap record in `8d1fa549`, before the validator commit `4dc11108`. It included
the instruction edits and replaced broad required reads with shared source
and record contracts. This trial tests the combined version; it cannot
attribute changes to one instruction edit or separate them from that
reorganization.

- Final combined checkout: `uv run pytest -q`, **1,197 passed** in 120.51 seconds.
- Active code: `uv run ruff check src scripts tests hatch_build.py`, passed.
- Edited instructions and types passed their targeted KB checks.
- Preserved old report bytes were reconstructed from the original write and repair calls and matched their recorded hashes. Current validation rejects old memory for the pending line and old epistemic for seven orphan ledger rows. Controlled-value rejection also has unit coverage.

## Trial inputs and acceptance

Both trials use copied inputs from
`AAS-2026-09-30-instinctual-memory-02`, prepared by the current
`scripts/analyst_trial.py` and delivered as saved invocations to fresh
`gpt-6-luna` sub-agents. There was no parent feedback, report edit or retry.

The frozen source is `https://github.com/jasonkneen/instinctual-memory`
at `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`. Boundary and runtime hashes
match the original trials:

| Input | SHA-256 |
|---|---|
| Boundary | `d0648cbb2f10839af6de820f41d99640bbb2d0cee039c4fd6c9ce106ce0e5367` |
| Runtime | `83f57ac2ea000c71dbbda2fbb4afbbcd057f71b42e6afc685d0841ccae1928d1` |

Temporary root: `/tmp/commonplace-luna-followup-51jet1_g`. The trial directories
under its `kb/reports/state/agentic-system-analysis/` are:

- `AAS-2026-10-01-trial-memory-guided-luna-instinctual-memory-01`
- `AAS-2026-10-01-trial-epistemic-guided-luna-instinctual-memory-01`

Each retains `prompt.md` and `trial.json` with dependency hashes. The root
retains baseline reports, `verification.json`, command/delivery extracts
and `trace-audit-metadata.json`. These temporary files can disappear;
the local rollout filenames and output hashes below identify the evidence.

| Final submission | Workflow refusals | Quote passes / failures | Output SHA-256 |
|---|---|---|---|
| Memory | none | 2 / 0 | `17a73afbd93c6a04d123f7303906b496a9579d6dc18b391501c847e8a82198bd` |
| Epistemic | none | 7 / 0 | `c1155605df9bad36ef4a06e696e1e96702d85c263e71e79709d7600e0d627319` |

Every declared input hash stayed unchanged. The source checkout remained
clean at the frozen commit. These are isolated analyst checks, not a
full-set assembly or publication test. Copied boundary/runtime retain the
original run ID, and the reset run-state retains the original publication
outcome in its body; output and state frontmatter use trial IDs. Those
fixture details need adjustment before an end-to-end workflow trial.

## Observable execution

Rollouts live locally under `/home/zby/.codex/sessions/2026/10/01/`.
All line numbers refer to their JSONL files.

| Analyst | Rollout filename | Calls / outputs | Truncated deliveries | Calls dropping status |
|---|---|---|---|---|
| Memory | `rollout-2026-10-01T06-56-35-01a0f5d2-4d4f-7d52-a1a6-69e7ea3e9e60.jsonl` | 41 / 41 | 18, 53, 81 | 15 |
| Epistemic | `rollout-2026-10-01T06-57-17-01a0f5d2-f33e-7be1-8a32-311ed128fbad.jsonl` | 36 / 36 | 18, 39, 88 | 15, 106, 113, 120, 145, 152, 159, 190, 256 |

Rollout SHA-256: memory
`99b04c21e691e24f2f6fba9e2bcd9293d76ebff8682831413d879f99425f6292`;
epistemic `252424c6f3d4b4d2b32284cd28e50f8ccaab8a6d190259f247b5cb4696df886b`.
Both turn contexts identify `gpt-6-luna`. Task text and parent spawn arguments
are encrypted in the local logs, so delivered task bytes cannot be
independently compared with saved prompt bytes.

The parent initially miscopied epistemic's output parameter as its problem
path. That worker was interrupted and replaced with a fresh worker receiving
the correct invocation. The excluded rollout ends
`06-56-54-01a0f5d2-9808-7cc1-a036-da498e6f908b.jsonl`; it contains zero tool
calls and no report write. The table describes the replacement.

### Reading and command handling

Both initial calls concatenate required files and forward only `r.output`,
despite the shared guidance. Initial truncation is therefore still a
bootstrap failure: the worker reads the rule while violating it.

Memory subsequently returns complete command objects on 40 of 41 calls.
It rereads its method, type, record contract and boundary. Its runtime read
at line 53 remains truncated; combining it with the initial delivery still
leaves runtime lines 50–95 undelivered, plus partial runtime lines 49 and
96. That gap includes component fixity and the journal definition. Its
later heading-only search names records but does not recover their content.
The broad search at line 81 also fails on nonexistent `src/search.rs`.

Epistemic recovers its record contract, type and complete runtime through
bounded rereads, but later drops statuses again. Its broad source search
at line 88 omits 1,551 tokens; selected excerpts follow without a complete
search recovery. Several later calls concatenate source excerpts, contrary
to the guidance. No failed status can be inferred from the calls whose
status was discarded.

Memory has eight visible nonzero command results: a guessed runtime path,
a guessed search file, shell quoting, a guessed cleanup file, two failed
tidy quotation lookups, and two validation failures. The path and quote
problems are repaired or worked around; they are not successful executions.
The quotation-repair call at line 262 and all three edit/validate calls
still use newline-separated dependent commands rather than `&&`.

Epistemic has two visible nonzero results: two bad selections in one quote
batch, then an unlabeled compact ledger rejected by the new validator.
Both are repaired. The quote batch and failed ledger retain their statuses;
the dropped-status calls remain an observability limitation.

### Repairs and remaining report defects

Memory's first validation (line 286) rejects a missing closing frontmatter
delimiter. The second (293) rejects the pending check line; the worker edits
that line and the third (300) passes. This demonstrates the new rule's
effect. Its retained check history nevertheless describes the pending
failure as the first validation, omits the delimiter failure, and does not
explicitly state the final pass. Parent verification confirms the pass.

Epistemic's first validation (236) rejects its compact ledger's missing
literal `Route ID:` labels. The repair formats nine records; later checks
at 252 and 273 pass. The records use controlled function/status values and
avoid the original interrupted-table defect. Formatting acceptance leaves
semantic field completeness and function separation to review.

Memory now annotates supplied objects, routes and authority paths, records
their overlap dispositions, and declares only one new absence record.
Epistemic separates hook text from writeback in its object inventory and
compares its new claim with supplied claims. However, it still groups
hook/writeback in one ledger entry and does not separately inventory the
material control parts of the published memory tree. Memory distinguishes
some parts in prose without identifying a needed canonical split.

Memory reads `src/tidy.rs` and the consolidation controls consumer. It
describes model-assisted session-only judgments and withdrawal from later
retrieval. Epistemic never reads that implementation, does not assess the
route, and does not list it as unassessed. Its broader negative findings
therefore still lack complete evaluation/criticism coverage. This omission
does not establish that tidy checks factual truth or produces knowledge.

Memory's table is headed “Directly inspected scope” but includes
`src/journal.rs`, `src/backfill.rs`, `src/search/rerank.rs`, `src/repo.rs`,
`src/http_serve.rs` and `src/shell.rs`. No source contents from these files
are delivered by the trace. Other listed paths receive only search hits:
for example, line 192 delivers one eligibility-filter line from
`src/search/lexical.rs` and several retraction hits from `src/controls.rs`.
Supplied runtime findings and references inside other files do not establish
direct inspection of those files. The table needs to distinguish delivered
source excerpts, search hits and supplied findings; it is not an inspection
receipt.

No observed command reads a forbidden prior analysis, the other analyst's
report, or workflow-state. Neither worker delegates, publishes, commits,
changes the source checkout, or writes outside its report and scratch scope.

## Consequence for the next decision

Keep the shipped structural checks: they rejected old defects and prompted
repairs in fresh runs. Keep the overlap and coverage requirements, whose
uptake was partial. Do not describe this result as clean execution or
complete analysis.

A next experiment should make the initial bounded reads concrete in the
saved invocation, before the worker must load the shared rules, and check
actual delivered coverage against the source-operation inventory. It should
test those changes separately from broader contract reductions. This is a
proposed next experiment, not an additional implemented tool or an approval
to expand this task.
