---
description: "Use with the new engine's analysis boundary hand-out for input reading, write authority, source restrictions, retry feedback and content checks"
type: types/instruction.md
---

# Follow the engine analysis worker rules

Produce one assigned analysis output from its pinned inputs without changing the target, evidence boundary or coordinator-owned state.

These rules currently serve the new engine's boundary job. The live legacy
workflow continues to load its own worker rules. The coordinator owns
scheduling, acceptance, integration and recovery; this hand-out grants neither
delegation nor publication authority.

## Read the hand-out

Read the invocation prompt completely, recovering every truncated part. Read
the named instruction first, then every Input reading batch in printed order.
Use supplied paths unchanged. Complete a batch before beginning the next;
read oversized files in the printed bounded ranges until their end. Read
source files and searches in bounded ranges too. No legacy `read-first`
parameter or legacy reading-order section is required.

Inspect the complete tool result, including status, errors and truncation.
Recover a truncated read with a smaller range; a larger inner token limit
cannot fix outer delivery truncation. A running command has no final status
until it completes. Use the available read tool for files when the runtime
requires it. Group reads only when that tool supports complete batch delivery.

| Name | Meaning |
|---|---|
| `system`, `run-id` | Fixed target name and exact run identity |
| `job`, `attempt` | Assigned job and open attempt |
| Named inputs | Absolute paths; `absent` means the optional input is missing |
| `refusal` | Optional refusal report: refused version, identity, scope and findings |
| `previous-boundary` | Prior completed boundary by identity, when supplied; not a current input |
| `validation-set`, `validation-member` | Intended set directory and member slot for content validation |
| `output`, `problem` | Result file or inability report |
| `workspace`, `scratch` | Per-attempt workspace and intermediate-file directory |

The supplied contracts give the operative definitions for this job. Linked
background definitions are not extra mandatory inputs. An unavailable
required input, needed target or source-identity change, or consequential
scope decision not authorized by the instruction requires `problem`. An
uncertainty that only limits a conclusion stays beside that conclusion in
`output`; do not discard supported findings to make coverage uniform.

## Stay within authority

Write only `output`, `problem` and intermediate files under `scratch`. The
boundary instruction separately permits immutable captures or bundles under
`capture-directory` in `opening`, including creation of that directory. Do not
modify existing captures. Closed hand-out workspaces are disposable; captures
must survive them. All supplied inputs, previous output and source checkouts
are read-only.
Do not create other workspace files, edit the working set or another job's
workspace, alter attempts, versions, judgments or run metadata, or write
legacy `workflow-state/` or `output/` copies. The layout is authority, not a
filesystem sandbox.

Do not publish, stage, commit, delegate or invoke a worker. Read engine state
only through this prompt's supplied inputs and previous output; do not inspect
other attempts or reconstruct run-state paths. Code materializes accepted
members; writing a candidate does not install it.

If refusal findings are supplied, repair those defects and their consequences
against the frozen source, preserving unrelated work. Use the supplied
previous output as the baseline, not a mutable member copy. Do not repeat the
whole analysis. The engine's max attempts do not reset after acceptance.

## Inspect sources, not target execution

Analyse source text and evidence within the assigned frozen boundary. Do not
execute the target, tests or examples, call its model providers or services,
install dependencies or create runtime fixtures. Source reading, quotation,
source capture authorized by the boundary instruction, and Commonplace
validation remain in scope. Missing execution evidence limits conclusions;
it does not authorize setting up a runtime check.

For Git, read and search the files at the registered commit under its frozen
`path`. Initially inspected paths are coverage, not an allowlist. Inspecting
another file at that commit does not expand the source boundary. An excluded
path may be inspected for relevance, not silently included. A material
shipped responsibility outside the selected functional boundary requires
`problem` with its path, responsibility and prevented conclusion. Treat the
checkout as read-only. For a capture, read only its frozen contents.

## Check content and quotation

Read `opening` for `command-path`, the prepared worktree's command directory.
If it is missing or the command is unavailable, write `problem`; do not use
a shared installation as a substitute. Run:

```text
<command-path>/commonplace-validate <output> --set <validation-set> --member <validation-member>
```

Use each supplied value unchanged. Run commands separately and inspect every
exit status, or chain dependent commands with `&&`. Pipelines require
`set -o pipefail`. Retain stderr as well as stdout. Repair findings and rerun
until the content check passes; do not report a check you did not execute.
Validation is read-only and reports this slot's content and relation findings.
A content pass establishes form and quotation occurrence, not claim support,
analytical correctness or job acceptance. Code also checks invocation-specific
identity and source conditions.

Use the source contract's quotation form; do not calculate attribution ranges
or revisions. Resolve ambiguity by printed context or a longer quote. For a
missing quote, reread the source and recheck the claim. Narrow or withdraw a
finding only when the evidence cannot support it, never merely to pass a check.
Record each finding narrowed or withdrawn during check repair, with its
reason, in `scratch/check-repairs.md`.

## Avoid prior-analysis exposure

Do not call agent listings or read style exemplars, prior reviews or audits,
`kb/agent-memory-systems/`, `kb/agentic-systems/reviews/`,
`kb/agentic-systems/reviews-archive/`, `kb/agentic-systems/reports/`,
`kb/agentic-system-analyses/retained/`,
`kb/agentic-system-analyses/retained-archive/`,
`kb/work/analyse-agentic-system/`, other runs under
`kb/agentic-system-analyses/state/`, surveys or comparison outputs. A path
filter does not make an agent listing safe. If any tool exposes prior-review
prose or audit findings, stop and write `problem` saying so; this run cannot
use your work.

When finished, reply in one line naming the file written, without summarizing
it. Follow higher-priority runtime requirements for progress messages.
