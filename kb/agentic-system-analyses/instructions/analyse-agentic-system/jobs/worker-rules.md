---
description: "Rules every job of an analyse-agentic-system workflow run follows: authority, command discipline, source reading, quotation, and prior-analysis exposure"
type: types/instruction.md
---

# Follow the worker rules of an analysis run

Produce the result of one code-scheduled analysis job within its assigned
evidence and write scope. Code schedules the job and judges its output.

## Invocation and authority

Read the supplied invocation prompt completely and recover any truncated
read before proceeding. Use its job parameters and retry feedback unchanged.

Every job uses these parameters; its instruction defines additional ones:

| Parameter | Meaning |
|---|---|
| `system` | Source-native system name |
| `run-id` | Exact run identity; copy unchanged when the member type requires it |
| `run-state` | Absolute path passed to `commonplace-quote`; not an evidence input |
| `output` | Absolute path for the completed result |
| `problem` | Absolute path for the reason the job cannot finish |
| `workspace` | Absolute per-job writable directory, when supplied by the workflow |
| `scratch` | Absolute directory for intermediate files, including selections and extracts |

A repair invocation may also supply `previous-output`, the absolute path of
the preserved report from the refused attempt. Read that file as the baseline.
Amend the reported failures and any dependent findings, preserving unrelated
analysis and records. Write the amended report to `output`; do not repeat the
full analysis. For quote repairs, check whether the corrected passage supports
the associated claim and carry any change through dependent conclusions. If
the source cannot support the claim, narrow or withdraw it and update the text.

Use supplied paths unchanged. Read every `read-first` dependency before
the task. Missing required parameters, unavailable required inputs,
source access or scope decisions that prevent completion, and needed
changes to the selected target or frozen source identity require `problem`.
Do not reconstruct paths, expand scope or submit a blocked member. A justified
unknown that only limits a conclusion remains in `output`, naming that conclusion.
Reading another file at the registered Git commit is not a source-boundary
expansion. If inspection shows that an explicit functional exclusion or
boundary kind omits a material shipped responsibility of the selected
target, name the path, responsibility and prevented conclusion in `problem`
instead of accepting the exclusion as missing evidence. The verification
job's instructions govern its disposition of such a defect.
Retry refusal feedback applies to the same job and does not change its
analytical round.

Write only `output` or `problem`, plus intermediate files in `scratch`.
When `workspace` is supplied, all three destinations are inside that job's
workspace. Supplied inputs outside it are read-only. Do not create other files
in the workspace or write to another job's workspace. Code copies accepted
results to coordinator-owned paths for later consumers; do not write those
copies yourself. This layout expresses authority but is not a filesystem sandbox.
The boundary job may create and freeze sources as its instruction permits.
Do not edit other run files, publish, delegate, stage or commit, or change
`workflow-state/`. Only the supplied invocation prompt and `previous-output`
may be read there. When finished, reply in one line naming the file
written, without summarizing it. Follow higher-priority runtime requirements
for progress messages.

## Commands

Run acceptance commands separately and inspect each exit status, or chain
dependent commands with `&&`. Shell pipelines need `set -o pipefail`. When
wrapping tool calls, retain status and stderr as well as stdout; a later
successful command does not clear an earlier failure. State a check's result
in your output only after you have run the check.

With standard Codex tools, return the complete command result, not just
`result.output`. For example, one bounded read through `functions.exec` is:

```javascript
const result = await tools.exec_command({
  cmd: "sed -n '1,100p' /absolute/path/from/the/invocation.md",
  max_output_tokens: 3000
});
text(result);
```

Replace the example path with a supplied path or the invocation's batch of
paths. Read the named job instruction before the Input reading batches.
Follow those batches in order, completing Read-first before
Task inputs. Read each batch in one tool call; a batch marked for bounded
ranges requires successive smaller reads until the file's end. Read files
outside the batch list, including `previous-output` and source searches, in
bounded ranges. The suggested grouping is a starting budget, not a guarantee:
long lines can still overflow it. Inspect the
complete returned object for `exit_code`, errors, and truncation. A running
command has no final exit status yet; wait for its completion. If either
the command or outer tool delivery is truncated, repeat that range with a
smaller range before advancing. Raising only the inner token limit does
not raise the outer delivery limit. Apply the same pattern to source
searches and reads. Use one command per call for file preparation and
acceptance checks, or `&&` when they must share a shell invocation.

## Sources

Analyse source text and evidence supplied within the frozen boundary.
Do not execute the target, its tests or examples, call its model providers
or services, install its dependencies, or create runtime fixtures.
Source-reading, quotation and Commonplace validation commands remain in
scope. Missing execution evidence limits conclusions; it does not require
planning a check or setting up an environment.

Read evidence only from the sources the supplied `boundary` registers. For
Git, read and grep the files under `source.path`; that directory holds
exactly the reviewed commit's files. Listed register paths describe initial
inspection, not reading permission: other files at that commit may be
inspected and cited for the selected target. Record additional coverage in
your member, following the source contract. You may inspect an excluded
path to check its relevance; that does not authorize changing functional
scope. Treat the checkout as read-only: do not fetch,
check out or copy the source elsewhere. For a capture, read the recorded
file.

## Quotation

Use the supplied `run-state` path directly. Keep selection files in `scratch`.
The boundary job's source-registration instructions govern quotation
availability during that job.

Generate every quote block with
`commonplace-quote <run-state> --source-path <commit-relative-path> --text-file <selection-file>`,
omitting `--source-path` for the run's capture, or
`--selections <json-file>` for many selections. Choose the occurrence whose
context supports the finding and insert its citation unchanged. Request
discontiguous passages separately. Only a quote attribution carries a line
range; cite a source in prose by path only. A failed lookup requires
rereading the source and revising the selection; never format a citation or
calculate a range by hand. A generated citation proves occurrence, not
support; judge support yourself.

Code matches the written runtime, memory and epistemic quotations against the
frozen source before accepting each output. A mismatch requests amendment of
the preserved report. Regenerate the citation, insert it unchanged, and check
its effect on the report's claims before resubmitting.

## Prior analyses

Do not call agent listings for status; their payloads may include prior
analyses even with a path filter. Do not read style exemplars or
`kb/agent-memory-systems/`, `kb/agentic-systems/reviews/`,
`kb/agentic-systems/reviews-archive/`,
`kb/agentic-systems/reports/retained/`,
`kb/agentic-systems/reports/retained-archive/`,
`kb/work/analyse-agentic-system/`, other runs under
`kb/agentic-systems/reports/state/`, surveys, comparison outputs, or
agent listings. If you read prior-review prose or prior audit findings
through any tool, stop and write a problem report saying so; the run cannot
use your work.
