# Execution-log scan tools

Harness-specific, read-only scanners supply leads for execution-health reviews.
Pi, Codex and Claude Code have separate parsers; do not pass other harness
formats to them: foreign records are reported as input issues, not clean scans.

## Provisional implementation and replacement review

These scanners are a provisional, locally maintained implementation. The v2
result contract is supported by current consumers; the parser architecture is
not a long-term commitment. Keep the scanners usable until a replacement is
selected and validated. This is not disposable one-off tooling under the
`scripts/README.md` cleanup norm.

Outstanding follow-up: survey existing session-log parsers and execution-audit
solutions before substantially expanding this subsystem. Compare native and
streaming format coverage, call/branch correlation, nested results, explicit
coverage gaps, exact evidence locators, offline operation and privacy, licensing,
and maintenance effort. Use retained representative traces and the contract
tests to assess adoption, adaptation or continued local ownership. No external
solution has yet been evaluated by this work.

## Common result contract (v2)

All scanner CLIs emit [result.schema.json](result.schema.json). The same trace
objects are returned by their Python `scan` functions and embedded in the
analysis workflow's audit report. Construction lives in
[`commonplace.lib.trace_scan`](../../src/commonplace/lib/trace_scan.py); parsing
and correlation remain harness-specific. Python 3 and the checkout's `src/`
tree are required; runtime scanning uses only the standard library. The schema
is checked in tests, not loaded on each scan.

- `schema_version: 2` identifies the report; `scope` states input selection.
- `traces` holds identity, format, `coverage`, `tool_results_seen`, `findings`,
  `observations`, `input_issues`, and harness-specific `details`.
- `finding_count` sums the trace findings. It counts failed outer tool-result
  candidates, not shell commands, root causes or confirmed defects. Zero says
  nothing about unscanned inputs. Aggregate consumers must retain unscanned
  input counts; the audit's all-unscanned status reports a null finding count.
- Each finding has call and result locators, arguments, an optional command,
  and one or more `evidence` items. Evidence carries `signals`, an optional exit
  code, a diagnostic excerpt of at most 600 characters, truncation status, and
  native signal names in `details.native_signals`. `isError` and `is_error`
  normalize to `tool_error`; native spelling remains available.
- `tool_results_seen` counts processed result records under the parser's
  correlation/deduplication rules. It does not assert process completion:
  a yielded command can produce a result while still running. It is not a
  cross-file unique execution count.
- Observations distinguish provider errors, interruptions, compactions and
  permission denials. They are not automatically tool failures. A denial may
  also explain a failed tool result; do not sum observations and findings as
  independent incidents. Native observation fields live in `details`.
- `coverage.checks` declares supported checks, not exhaustive detection.
  `input_status: partial` identifies input or correlation issues; `read` means
  no such issues were detected. Unsupported checks cannot yield a clean bill
  of health. Recovery and output quality remain unsupported by all scanners.
- Coverage records the last inspected physical line, first/last observed event
  timestamps and inspection time (`cutoff_utc`). These are not inferred from
  file mtime. Null means unavailable. `branch_scope` describes stored branches,
  stored records or a stream; it does not identify the delivered branch.
- `input_issues` contains `{line, message}` records. Root issues concern input
  enumeration; trace issues concern that file. Line numbers are one-based;
  content block indexes are zero-based. Absent IDs/timestamps are null.
- `details` is the extension space. Malformed native identity/command fields
  and exit codes become null in common fields, retain their original values
  in `details`, and produce input issues. Consumers may ignore extensions
  without losing the common evidence; they must not assume a native final result proves success.

Exit 0 means no detected input issues, even with findings. Exit 2 preserves
partial evidence and reports input issues. Existing v1 reports remain unchanged;
this implementation does not provide a v1 reader or emit both shapes. Current
consumers migrate together. Incompatible contract changes require a new version.


## Pi

Run from the Commonplace source checkout with Python 3 (stdlib only):

```bash
python3 scripts/scan_tools/scan_pi_tool_failures.py --format pi-session /path/to/session.jsonl
python3 scripts/scan_tools/scan_pi_tool_failures.py --format pi-json /path/to/stdout.log
```

Each command accepts multiple files of the selected format. The wrapper imports
`commonplace.lib.agentic_analysis.tool_failures` from this checkout; it does not
implement a separate parser. It discovers no sessions, follows no embedded
paths, launches no workers and modifies no inputs.

Use [Review recent logs for hidden failures](../../kb/instructions/review-recent-logs-for-hidden-failures.md)
for discovery, incident assessment and the handoff to diagnosis. That procedure
limits each agent to reviewing logs from its own harness; the operator invokes
a separate agent per harness for broader coverage. The scanner
alone detects explicit tool failures, not recovery, provider retries or final
output quality. Native sessions include all stored branches. Expected search
no-matches can be findings; masked shell failures can be missed.

Exit 0 means no detected input issues, not no tool failures. Exit 2 means
malformed, unreadable or unsupported input or incomplete correlation; partial
findings remain available. Review commands and diagnostic excerpts for secrets
before sharing. Use `--help` for the current interface.

## Codex

```bash
python3 scripts/scan_tools/scan_codex_tool_failures.py /path/to/rollout.jsonl
```

Accepts one or more explicit native Codex rollout JSONL files (the optional
`--format codex-session` makes the format explicit). This source-checkout script uses
only Python's standard library and the shared result constructor. It does not accept `codex exec --json` streams,
discover sessions, follow worker references, execute trace contents or modify
inputs. Select project sessions and a bounded review window before scanning.
Use the universal review instruction above; select this parser for Codex
rollouts rather than importing Pi's parser or branch model.

Correlates `response_item` function/custom calls with outputs by `call_id`.
Detects nonzero structured `exit_code`, `isError`, native shell status envelopes
and selected tool-error prefixes. Recognizes `Script failed` exec envelopes,
including envelopes split across text blocks, and inspects JSON values printed
by `functions.exec`. Supports `Promise.allSettled` fulfilled/rejected records,
arrays of results and indexed `{i, result: ...}` wrappers. A fulfilled promise
can still contain a nonzero command exit; promise rejection is a separate signal.
Command stdout remains data: error examples printed by a successful command do
not become failures. Counts a failed outer call
once, retaining its individual evidence signals. Repeated outputs and mirrored
`event_msg` items are not counted again. Identical file paths are deduplicated;
copied files and shared histories across files are not deduplicated.

Reports session ID and working directory; `coverage` holds first/last observed
timestamps, last inspected line and scan cutoff. The initial file size bounds live-file reads.
Missing calls, missing outputs, conflicting duplicates and malformed records
produce input issues and exit 2 while retaining partial findings. A pending call
may be live or interrupted; it is not automatically a failed operation.

The scanner does not infer retries, recovery, process completion after a yielded
call, provider errors, masked shell failures, or output quality. Event-only tool
results and unrecognized tool-result encodings are not covered. A successful
wrapper may conceal failures it did not print. Arguments and diagnostic excerpts
can contain secrets. Use findings as leads for bounded inspection of the original
trace, including a declared sample of apparently successful sequences.

## Claude Code

Run from the Commonplace source checkout with Python 3 (stdlib only):

```bash
python3 scripts/scan_tools/scan_claude_code_tool_failures.py ~/.claude/projects/<cwd-slug>/<session>.jsonl
python3 scripts/scan_tools/scan_claude_code_tool_failures.py ~/.claude/projects/<cwd-slug>/<session>/subagents/agent-<id>.jsonl
python3 scripts/scan_tools/scan_claude_code_tool_failures.py /path/to/stdout.log
```

Like the Pi wrapper, it imports
`commonplace.lib.agentic_analysis.claude_code_tool_failures`, the parser the
analysis audit uses. It accepts both persisted session JSONL and the stdout of
`claude --print --output-format stream-json --verbose`; streams report `format`
`claude-stream-json`, permission-denial observations and their final
`details.result`.

Claude Code persists sessions under `~/.claude/projects/<cwd-slug>/`, one JSONL
per session, with worker transcripts in `<session>/subagents/`. Pass every file
explicitly: the scanner discovers no sessions and follows no paths or worker IDs
found in a trace. It reports per file the session ID, the worker `agent_id` for
subagent files, and the `details.worker_ids` the file launched, so missing or
out-of-scope children can be listed. Failures are matched to calls by tool-use
ID, so all stored branches are scanned, including rewound ones, and tool calls
are matched across split assistant records and attachments.

Findings use the common fields, with `evidence[].signals` for harness
outcomes recorded as tool errors: `user_rejected`, `permission_denied` and
`tool_use_error` (hook blocks, invalid input, unknown tools). Shell exit codes
come from the `Exit code N` prefix Claude Code adds to failed Bash output;
successful output is not inspected. Typed `observations` give API error messages,
user interruptions and compaction boundaries as leads for provider retries and
overflow recovery. `coverage.last_line` and `coverage.last_timestamp` record
the inspected cutoff for live files. Exit codes and limits are as for the Pi scanner.
Pass files directly, not through `xargs`: xargs replaces the scanner's exit 2
with its own 123 and hides the input issue.
