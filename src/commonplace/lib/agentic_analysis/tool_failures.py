"""Report explicit tool failures in supplied Pi JSONL traces; never judge recovery.

Use --format pi-json for `pi --mode json` stdout, or pi-session for persisted
session files. All stored session branches are scanned, not just active context.
Exit 0 means the scan encountered no input issues, not that tools succeeded.
Exit 2 means some input could not be interpreted; partial findings remain useful.
Commands/output may contain secrets. Review before retaining or sharing output.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from commonplace.lib.trace_scan import scan_report, trace_result

EXCERPT_LIMIT = 600


def text_content(result: dict[str, Any]) -> str:
    content = result.get("content", [])
    if not isinstance(content, list):
        return ""
    return "\n".join(
        block["text"]
        for block in content
        if isinstance(block, dict)
        and block.get("type") == "text"
        and isinstance(block.get("text"), str)
    )


def scan(path: Path, trace_format: str) -> dict[str, Any]:
    """Scan one explicit file. Never follow paths embedded in a trace."""
    report: dict[str, Any] = {
        "trace": str(path),
        "format": trace_format,
        "session_id": None,
        "tool_results_seen": 0,
        "last_line": 0, "first_timestamp": None, "last_timestamp": None,
        "findings": [],
        "input_issues": [],
    }
    pending: dict[str, tuple[int, dict[str, Any]]] = {}
    # Only parent links and tool calls are retained, not the full conversation.
    entries: dict[str, tuple[str | None, dict[str, dict[str, Any]], int]] = {}
    recognized = False

    def issue(line: int | None, message: str) -> None:
        report["input_issues"].append({"line": line, "message": message})

    def complete(
        event: dict[str, Any], result: dict[str, Any], line: int,
        call: tuple[int, dict[str, Any]] | None,
    ) -> None:
        report["tool_results_seen"] += 1
        error = event.get("isError")
        if not isinstance(error, bool):
            issue(line, "completed tool has no boolean isError flag")
        output = text_content(result)
        structured = result.get("structuredContent")
        code = structured.get("exit_code") if isinstance(structured, dict) else None
        if type(code) is not int:
            code = None
        # Older Pi bash results expose the exit code only in their final status line.
        # Do not interpret arbitrary occurrences in output or successful tool text.
        if code is None and error is True and event.get("toolName") == "bash":
            match = re.search(r"(?:^|\n)Command exited with code (-?\d+)\s*\Z", output)
            if match:
                code = int(match[1])
        signals = []
        if error is True:
            signals.append("isError")
        if code is not None and code != 0:
            signals.append("nonzero_exit")
        if not signals:
            return
        if call is None:
            issue(line, "failed tool has no matching call; arguments unavailable")
        args = call[1] if call else None
        report["findings"].append({
            "line": line,
            "entry_id": event.get("id"),
            "tool_call_id": event.get("toolCallId"),
            "tool_name": event.get("toolName"),
            "call_line": call[0] if call else None,
            "arguments": args,
            "command": args.get("command") if isinstance(args, dict) else None,
            "evidence": [{
                "exit_code": code,
                "signals": signals,
                "diagnostic_excerpt": output[-EXCERPT_LIMIT:],
                "diagnostic_truncated": len(output) > EXCERPT_LIMIT,
            }],
            "recovery": "not_assessed",
        })

    try:
        with path.open(encoding="utf-8") as stream:
            # File iteration splits on LF, not Unicode separators within JSON strings.
            for line, raw in enumerate(stream, 1):
                report["last_line"] = line
                if not raw.strip():
                    continue
                try:
                    event = json.loads(raw)
                except ValueError as exc:
                    issue(line, f"invalid JSON: {exc}")
                    continue
                if not isinstance(event, dict):
                    issue(line, "JSON record is not an object")
                    continue
                stamp = event.get("timestamp")
                if isinstance(stamp, str):
                    if report["first_timestamp"] is None:
                        report["first_timestamp"] = stamp
                    report["last_timestamp"] = stamp
                kind = event.get("type")
                if kind == "session":
                    recognized = True
                    report["session_id"] = event.get("id")
                if trace_format == "pi-json":
                    if kind == "message":
                        issue(line, "persisted message entry in pi-json input; use pi-session")
                    if kind == "tool_execution_start":
                        recognized = True
                        call_id, args = event.get("toolCallId"), event.get("args")
                        if isinstance(call_id, str) and isinstance(args, dict):
                            pending[call_id] = (line, args)
                        else:
                            issue(line, "tool start lacks call ID or argument object")
                    elif kind == "tool_execution_end":
                        recognized = True
                        call_id, result = event.get("toolCallId"), event.get("result")
                        call = pending.pop(call_id, None) if isinstance(call_id, str) else None
                        if not isinstance(result, dict):
                            issue(line, "tool end lacks result object")
                            continue
                        complete(event, result, line, call)
                    # message_end/turn_end/agent_end repeat results: do not count them.
                elif kind == "message":
                    recognized = True
                    message = event.get("message")
                    if not isinstance(message, dict):
                        issue(line, "session message lacks message object")
                        continue
                    entry_id, parent = event.get("id"), event.get("parentId")
                    calls = {}
                    content = message.get("content")
                    if message.get("role") == "assistant" and isinstance(content, list):
                        for block in content:
                            if isinstance(block, dict) and block.get("type") == "toolCall":
                                cid, args = block.get("id"), block.get("arguments")
                                if isinstance(cid, str) and isinstance(args, dict):
                                    calls[cid] = args
                    if isinstance(entry_id, str):
                        entries[entry_id] = (parent, calls, line)
                    if message.get("role") != "toolResult":
                        continue
                    call = None
                    seen = set()
                    while isinstance(parent, str) and parent in entries and parent not in seen:
                        seen.add(parent)
                        parent, ancestor_calls, call_line = entries[parent]
                        cid = message.get("toolCallId")
                        if isinstance(cid, str) and cid in ancestor_calls:
                            call = (call_line, ancestor_calls[cid])
                            break
                    complete({**message, "id": entry_id}, message, line, call)
                elif trace_format == "pi-session":
                    if kind in ("tool_execution_start", "tool_execution_end", "message_end"):
                        issue(line, "stream event in pi-session input; use pi-json")
                    elif isinstance(event.get("id"), str):
                        entries[event["id"]] = (event.get("parentId"), {}, line)
    except (OSError, UnicodeError) as exc:
        issue(None, str(exc))
    if not recognized:
        issue(None, "no recognized Pi records; empty or unsupported trace")
    for call_id, (line, _) in pending.items():
        issue(line, f"tool start has no completion: {call_id}")
    return trace_result(report, harness="pi", checks=("tool_failures",),
                        branch_scope=("all_stored_branches" if trace_format == "pi-session" else "stream"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=("pi-json", "pi-session"), required=True)
    parser.add_argument("traces", type=Path, nargs="+", help="explicit trace files; no recursive discovery")
    args = parser.parse_args()
    paths = dict.fromkeys(path.resolve() for path in args.traces)
    reports = [scan(path, args.format) for path in paths]
    print(json.dumps(scan_report(
        reports, scope="explicit failure candidates and supported observations; recovery not assessed",
    ), indent=2, ensure_ascii=False))
    return 2 if any(report["input_issues"] for report in reports) else 0


if __name__ == "__main__":
    raise SystemExit(main())
