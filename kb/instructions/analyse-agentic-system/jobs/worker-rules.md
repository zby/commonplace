---
description: "Rules every job of an analyse-agentic-system workflow run follows: authority, command discipline, source reading, quotation, and prior-analysis exposure"
type: types/instruction.md
---

# Follow the worker rules of an analysis run

You are one job of a code-scheduled `analyse-agentic-system` run. Code scheduled you and will judge your output. Write only `output`, or `problem` when you cannot finish, and intermediate files (selection files, extracted sources) in `scratch`. When you finish, reply in one line naming the file you wrote without repeating or summarizing its content, and send no other message while you work. The boundary job may create and freeze source checkouts or captures as its instruction permits. Do not edit other files of the run, publish, delegate, stage, or commit. Anything under `workflow-state/` is not yours to read or change.

## Commands

Run acceptance commands separately and inspect each exit status, or chain dependent commands with `&&`. Shell pipelines need `set -o pipefail`. When wrapping tool calls, retain status and stderr as well as stdout; a later successful command does not clear an earlier failure. State a check's result in your output only after you have run the check.

## Sources

After the boundary job freezes the sources, read evidence only within that frozen boundary: use `boundary` when supplied, or the Boundary and evidence and Source register in `overview-draft` for verification. For Git, read and grep the files of the checkout at `source.path`: the boundary job checked it out at the recorded commit, and code refused the boundary unless its `git status` was empty. Do not modify, check out or fetch in that checkout, and do not extract another copy of the source. For a capture, read the recorded file and check its SHA-256.

Select files and line ranges before reading content. Budget the combined output of parallel reads against the tool wrapper's delivery limit. Check delivered output for truncation at both the command and the wrapper level; truncated output is not evidence. Narrow and repeat the read before citing it, and do not infer coverage from a successful command or its requested range.

## Quotation

Use the supplied `run-state` path directly. Keep selection files in `scratch`.

Generate every quote block with `commonplace-quote <run-state> --source-path <commit-relative-path> --text-file <selection-file>`, omitting `--source-path` for the run's capture, or `--selections <json-file>` for many selections. Choose the occurrence whose context supports the finding and insert its citation unchanged. Request discontiguous passages separately. Only a quote attribution carries a line range; cite a source in prose by path only. A failed lookup requires rereading the source and revising the selection; never format a citation or calculate a range by hand. A generated citation proves occurrence, not support; judge support yourself.

## Prior analyses

Do not call agent listings for status; their payloads may include prior analyses even with a path filter. Do not read style exemplars or `kb/agent-memory-systems/`, `kb/agentic-systems/reviews/`, `kb/agentic-systems/reviews-archive/`, `kb/reports/retained/agentic-system-analysis/`, `kb/reports/retained/agentic-system-analysis-archive/`, `kb/work/analyse-agentic-system/`, other runs under `kb/reports/state/agentic-system-analysis/`, surveys, comparison outputs, or agent listings. If you read prior-review prose or prior audit findings through any tool, stop and write a problem report saying so; the run cannot use your work.
