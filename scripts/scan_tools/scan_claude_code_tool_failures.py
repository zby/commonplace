"""Report explicit tool failures in supplied Claude Code session JSONL; never judge recovery.

Input is the persisted session file written under ~/.claude/projects/<cwd-slug>/,
either a top-level <session>.jsonl or a worker file under
<session>/subagents/agent-<id>.jsonl. Pass every file explicitly; the scanner
discovers no sessions and follows no paths or worker IDs found in a trace.
All stored branches are scanned, including rewound ones, not just active context.
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

EXCERPT_LIMIT = 600
# Record types written by other harnesses' scanners' inputs; never silently clean.
FOREIGN_RECORD_TYPES = {
    "session", "message", "tool_execution_start", "tool_execution_end", "message_end",
    "response_item", "session_meta", "event_msg",
}
EXIT_CODE = re.compile(r"\AExit code (-?\d+)(?:\n|\Z)")
INTERRUPTION = re.compile(r"\A\[Request interrupted by user(?: for tool use)?\]")
# Harness-side outcomes recorded as tool errors; they are not command failures.
USER_REJECTED = "The user doesn't want to proceed with this tool use"
PERMISSION_DENIED = "Permission for this action was denied"


def block_text(content: Any) -> str:
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    return "\n".join(
        block["text"]
        for block in content
        if isinstance(block, dict)
        and block.get("type") == "text"
        and isinstance(block.get("text"), str)
    )


def scan(path: Path) -> dict[str, Any]:
    """Scan one explicit file. Never follow paths or worker IDs embedded in a trace."""
    report: dict[str, Any] = {
        "trace": str(path),
        "format": "claude-code-session",
        "session_id": None,
        "agent_id": None,
        "cwd": None,
        "first_timestamp": None,
        "completed_tools": 0,
        "failures": [],
        "api_errors": [],
        "interruptions": [],
        "compactions": [],
        "worker_ids": [],
        "last_line": None,
        "last_timestamp": None,
        "scan_issues": [],
    }
    # Only parent links and tool calls are retained, not the full conversation.
    entries: dict[str, tuple[str | None, dict[str, tuple[str | None, Any]], int]] = {}
    worker_ids: dict[str, None] = {}
    recognized = False

    def issue(line: int | None, message: str) -> None:
        report["scan_issues"].append({"line": line, "message": message})

    def find_call(parent: Any, call_id: Any) -> tuple[int, str | None, Any] | None:
        seen: set[str] = set()
        while isinstance(parent, str) and parent in entries and parent not in seen:
            seen.add(parent)
            parent, calls, call_line = entries[parent]
            if isinstance(call_id, str) and call_id in calls:
                name, arguments = calls[call_id]
                return call_line, name, arguments
        return None

    def complete(event: dict[str, Any], block: dict[str, Any], index: int, line: int) -> None:
        report["completed_tools"] += 1
        call_id = block.get("tool_use_id")
        call = find_call(event.get("parentUuid"), call_id)
        error = block.get("is_error", False)
        if not isinstance(error, bool):
            issue(line, "tool_result has a non-boolean is_error flag")
            error = False
        output = block_text(block.get("content"))
        name = call[1] if call else None
        code = None
        # Claude Code prefixes failed shell output with its exit code; successful
        # output is not inspected, so unrelated "Exit code" text is never read.
        if error and name in ("Bash", None):
            match = EXIT_CODE.match(output)
            if match:
                code = int(match[1])
        signals = []
        if error:
            signals.append("is_error")
        if code is not None and code != 0:
            signals.append("nonzero_exit")
        if USER_REJECTED in output:
            signals.append("user_rejected")
        if PERMISSION_DENIED in output:
            signals.append("permission_denied")
        if "<tool_use_error>" in output:
            signals.append("tool_use_error")
        if not signals:
            return
        if call is None:
            issue(line, "failed tool has no matching tool_use; arguments unavailable")
        arguments = call[2] if call else None
        report["failures"].append({
            "line": line,
            "block_index": index,
            "entry_id": event.get("uuid"),
            "timestamp": event.get("timestamp"),
            "tool_call_id": call_id,
            "tool_name": name,
            "call_line": call[0] if call else None,
            "arguments": arguments,
            "command": arguments.get("command") if isinstance(arguments, dict) else None,
            "exit_code": code,
            "signals": signals,
            "diagnostic_excerpt": output[-EXCERPT_LIMIT:],
            "diagnostic_truncated": len(output) > EXCERPT_LIMIT,
            "recovery": "not_assessed",
        })

    try:
        with path.open(encoding="utf-8") as stream:
            # File iteration splits on LF, not Unicode separators within JSON strings.
            for line, raw in enumerate(stream, 1):
                if not raw.strip():
                    continue
                report["last_line"] = line
                try:
                    event = json.loads(raw)
                except ValueError as exc:
                    issue(line, f"invalid JSON: {exc}")
                    continue
                if not isinstance(event, dict):
                    issue(line, "JSON record is not an object")
                    continue
                kind = event.get("type")
                if kind in FOREIGN_RECORD_TYPES:
                    issue(line, f"record type {kind!r} belongs to another harness format")
                    continue
                if report["session_id"] is None and isinstance(event.get("sessionId"), str):
                    report["session_id"] = event["sessionId"]
                if report["agent_id"] is None and isinstance(event.get("agentId"), str):
                    report["agent_id"] = event["agentId"]
                if report["cwd"] is None and isinstance(event.get("cwd"), str):
                    report["cwd"] = event["cwd"]
                if isinstance(event.get("timestamp"), str):
                    if report["first_timestamp"] is None:
                        report["first_timestamp"] = event["timestamp"]
                    report["last_timestamp"] = event["timestamp"]
                uuid, parent = event.get("uuid"), event.get("parentUuid")
                calls: dict[str, tuple[str | None, Any]] = {}
                message = event.get("message")
                content = message.get("content") if isinstance(message, dict) else None
                if kind == "assistant":
                    recognized = True
                    if not isinstance(message, dict):
                        issue(line, "assistant record lacks message object")
                    elif event.get("isApiErrorMessage") is True:
                        report["api_errors"].append({
                            "line": line, "entry_id": uuid, "timestamp": event.get("timestamp"),
                            "error": event.get("error"), "text": block_text(content)[:EXCERPT_LIMIT],
                        })
                    if isinstance(content, list):
                        for block in content:
                            if isinstance(block, dict) and block.get("type") == "tool_use":
                                cid = block.get("id")
                                if isinstance(cid, str):
                                    calls[cid] = (block.get("name"), block.get("input"))
                                else:
                                    issue(line, "tool_use block lacks string id")
                elif kind == "user":
                    recognized = True
                    if not isinstance(message, dict):
                        issue(line, "user record lacks message object")
                    elif isinstance(content, str):
                        if INTERRUPTION.match(content):
                            report["interruptions"].append({
                                "line": line, "entry_id": uuid, "timestamp": event.get("timestamp"),
                                "text": content[:EXCERPT_LIMIT],
                            })
                    elif isinstance(content, list):
                        for index, block in enumerate(content):
                            if not isinstance(block, dict):
                                continue
                            if block.get("type") == "tool_result":
                                complete(event, block, index, line)
                            elif block.get("type") == "text" and INTERRUPTION.match(
                                block.get("text", "")
                            ):
                                report["interruptions"].append({
                                    "line": line, "entry_id": uuid,
                                    "timestamp": event.get("timestamp"),
                                    "text": block["text"][:EXCERPT_LIMIT],
                                })
                    result = event.get("toolUseResult")
                    if isinstance(result, dict) and isinstance(result.get("agentId"), str):
                        worker_ids[result["agentId"]] = None
                elif kind == "system" and event.get("subtype") == "compact_boundary":
                    metadata = event.get("compactMetadata")
                    metadata = metadata if isinstance(metadata, dict) else {}
                    report["compactions"].append({
                        "line": line, "entry_id": uuid, "timestamp": event.get("timestamp"),
                        "trigger": metadata.get("trigger"), "pre_tokens": metadata.get("preTokens"),
                        "logical_parent": event.get("logicalParentUuid"),
                    })
                if isinstance(uuid, str):
                    entries[uuid] = (parent if isinstance(parent, str) else None, calls, line)
    except (OSError, UnicodeError) as exc:
        issue(None, str(exc))
    if not recognized:
        issue(None, "no recognized Claude Code records; empty or unsupported trace")
    report["worker_ids"] = list(worker_ids)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "traces", type=Path, nargs="+",
        help="explicit Claude Code session or subagent JSONL files; no recursive discovery",
    )
    args = parser.parse_args()
    paths = dict.fromkeys(path.resolve() for path in args.traces)
    reports = [scan(path) for path in paths]
    print(json.dumps({
        "schema_version": 1,
        "scope": (
            "explicit tool failures, API error messages, user interruptions and "
            "compaction boundaries only; recovery and semantic correctness not assessed"
        ),
        "failure_count": sum(len(report["failures"]) for report in reports),
        "traces": reports,
    }, indent=2, ensure_ascii=False))
    return 2 if any(report["scan_issues"] for report in reports) else 0


if __name__ == "__main__":
    raise SystemExit(main())
