---
description: "Rules every job of an analyse-agentic-system workflow run follows: authority, command discipline, source reading, quotation, and prior-analysis exposure"
type: types/instruction.md
---

# Follow the worker rules of an analysis run

Produce the result of one code-scheduled analysis job within its assigned
evidence and write scope. Code schedules the job and judges its output.

## Invocation and authority

Every job uses these parameters; its instruction defines additional ones:

| Parameter | Meaning |
|---|---|
| `system` | Source-native system name |
| `run-state` | Absolute path passed to `commonplace-quote`; not an evidence input |
| `output` | Absolute path for the completed result |
| `problem` | Absolute path for the reason the job cannot finish |
| `scratch` | Absolute directory for intermediate files, including selections and extracts |

Use supplied paths unchanged. Read every `read-first` dependency before
the task. Missing required parameters, unavailable required inputs,
source access or scope decisions that prevent completion, and needed
expansion beyond the frozen boundary require `problem`; do not reconstruct
paths, expand scope or submit a blocked member. A justified unknown that
only limits a conclusion remains in `output`, naming that conclusion.
Retry refusal feedback applies to the same job and does not change its
analytical round.

Write only `output` or `problem`, plus intermediate files in `scratch`.
The boundary job may create and freeze sources as its instruction permits.
Do not edit other run files, publish, delegate, stage or commit, or read or
change `workflow-state/`. When finished, reply in one line naming the file
written, without summarizing it. Follow higher-priority runtime requirements
for progress messages.

## Commands

Run acceptance commands separately and inspect each exit status, or chain dependent commands with `&&`. Shell pipelines need `set -o pipefail`. When wrapping tool calls, retain status and stderr as well as stdout; a later successful command does not clear an earlier failure. State a check's result in your output only after you have run the check.

With standard Codex tools, return the complete command result, not just
`result.output`. For example, one bounded read through `functions.exec` is:

```javascript
const result = await tools.exec_command({
  cmd: "sed -n '1,100p' /absolute/path/from/the/invocation.md",
  max_output_tokens: 3000
});
text(result);
```

Replace the example path with the supplied path. Read each instruction,
contract, and input separately, in successive bounded ranges until its
end; do not concatenate them into one command. The range is a starting
budget, not a guarantee: long lines can still overflow it. Inspect the
complete returned object for `exit_code`, errors, and truncation. A running
command has no final exit status yet; wait for its completion. If either
the command or outer tool delivery is truncated, repeat that range with a
smaller range before advancing. Raising only the inner token limit does
not raise the outer delivery limit. Apply the same pattern to source
searches and reads. Use one command per call for file preparation and
acceptance checks, or `&&` when they must share a shell invocation.

## Sources

After the boundary job freezes the sources, read evidence only within that frozen boundary: use `boundary` when supplied, or the Boundary and evidence and Source register in `overview-draft` for verification. For Git, read and grep the files of the checkout at `source.path`: the boundary job checked it out at the recorded commit, and code refused the boundary unless its `git status` was empty. Do not modify, check out or fetch in that checkout, and do not extract another copy of the source. For a capture, read the recorded file and check its SHA-256.

## Quotation

Use the supplied `run-state` path directly. Keep selection files in `scratch`.

Generate every quote block with `commonplace-quote <run-state> --source-path <commit-relative-path> --text-file <selection-file>`, omitting `--source-path` for the run's capture, or `--selections <json-file>` for many selections. Choose the occurrence whose context supports the finding and insert its citation unchanged. Request discontiguous passages separately. Only a quote attribution carries a line range; cite a source in prose by path only. A failed lookup requires rereading the source and revising the selection; never format a citation or calculate a range by hand. A generated citation proves occurrence, not support; judge support yourself.

## Prior analyses

Do not call agent listings for status; their payloads may include prior analyses even with a path filter. Do not read style exemplars or `kb/agent-memory-systems/`, `kb/agentic-systems/reviews/`, `kb/agentic-systems/reviews-archive/`, `kb/reports/retained/agentic-system-analysis/`, `kb/reports/retained/agentic-system-analysis-archive/`, `kb/work/analyse-agentic-system/`, other runs under `kb/reports/state/agentic-system-analysis/`, surveys, comparison outputs, or agent listings. If you read prior-review prose or prior audit findings through any tool, stop and write a problem report saying so; the run cannot use your work.
