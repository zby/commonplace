# Execution-log scan tools

Harness-specific, read-only scanners supply leads for execution-health reviews.
Pi, Codex and Claude Code have separate parsers; do not pass other harness
formats to them: foreign records are reported as input issues, not clean scans.

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

Use [Review recent Pi logs for hidden failures](../../kb/instructions/review-recent-pi-logs-for-hidden-failures.md)
for discovery, incident assessment and the handoff to diagnosis. The scanner
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
`--format codex-session` makes the format explicit). This standalone script uses
only Python's standard library. It does not accept `codex exec --json` streams,
discover sessions, follow worker references, execute trace contents or modify
inputs. Select project sessions and a bounded review window before scanning.
The Pi procedure's review principles apply, but its parser and branch model do
not apply to Codex.

Correlates `response_item` function/custom calls with outputs by `call_id`.
Detects nonzero structured `exit_code`, `isError`, native shell status envelopes
and selected tool-error prefixes. Inspects JSON results in text blocks, including
nested command results printed by `functions.exec`. Counts a failed outer call
once, retaining its individual evidence signals. Repeated outputs and mirrored
`event_msg` items are not counted again. Identical file paths are deduplicated;
copied files and shared histories across files are not deduplicated.

Reports session ID, working directory, first/last observed timestamps, last
inspected line and scan cutoff. The initial file size bounds live-file reads.
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

Run from the Commonplace source checkout with Python 3 (stdlib only, no `src/`):

```bash
python3 scripts/scan_tools/scan_claude_code_tool_failures.py ~/.claude/projects/<cwd-slug>/<session>.jsonl
python3 scripts/scan_tools/scan_claude_code_tool_failures.py ~/.claude/projects/<cwd-slug>/<session>/subagents/agent-<id>.jsonl
```

Claude Code persists sessions under `~/.claude/projects/<cwd-slug>/`, one JSONL
per session, with worker transcripts in `<session>/subagents/`. Pass every file
explicitly: the scanner discovers no sessions and follows no paths or worker IDs
found in a trace. It reports per file the session ID, the worker `agent_id` for
subagent files, and the `worker_ids` the file launched, so missing or
out-of-scope children can be listed. The failure correlation walks `parentUuid`
links, so all stored branches are scanned, including rewound ones, and tool
calls are matched across split assistant records and attachments.

Findings carry the same fields as the Pi scanner plus `signals` for harness
outcomes recorded as tool errors: `user_rejected`, `permission_denied` and
`tool_use_error` (hook blocks, invalid input, unknown tools). Shell exit codes
come from the `Exit code N` prefix Claude Code adds to failed Bash output;
successful output is not inspected. Separate lists give API error messages,
user interruptions and compaction boundaries as leads for provider retries and
overflow recovery; `last_line` and `last_timestamp` record the inspected
cutoff for live files. Exit codes and limits are as for the Pi scanner.
Pass files directly, not through `xargs`: xargs replaces the scanner's exit 2
with its own 123 and hides the input issue.
