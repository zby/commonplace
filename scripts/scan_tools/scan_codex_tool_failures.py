"""Scan explicit Codex native rollout JSONL files for tool failure candidates.

Read-only and stdlib-only. Does not discover sessions or assess recovery.
Exit 2 indicates input/correlation gaps; exit 0 does not mean no failures.
Arguments and excerpts may contain secrets: review before sharing.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from commonplace.lib.trace_scan import scan_report, trace_result

EXCERPT_LIMIT = 600
CALL_TYPES = {"function_call", "custom_tool_call"}
OUTPUT_TYPES = {"function_call_output", "custom_tool_call_output"}
# Match the shell tool's status envelope, never arbitrary lines in stdout.
SHELL_STATUS = re.compile(
    r"\A(?:Chunk ID: [^\n]+\n)?Wall time: [^\n]+\n"
    r"Process exited with code (-?\d+)\n(?:Final output:|Output:)"
)


EXEC_STATUS = re.compile(r"\AScript (completed|failed)\nWall time [^\n]+\nOutput:\n")


def signals(value: Any) -> list[dict[str, Any]]:
    """Inspect result containers and envelopes without searching command stdout."""
    found = []
    if isinstance(value, list):
        # Codex can split the exec envelope and its printed values across blocks.
        # Join only text blocks when the first block establishes that envelope.
        texts = [block.get("text", "") for block in value
                 if isinstance(block, dict) and block.get("type") in ("text", "input_text")
                 and isinstance(block.get("text"), str)]
        if texts and EXEC_STATUS.match(texts[0]):
            found.extend(signals(texts[0]))
            for evidence in found:
                if "script_failed" in evidence["signals"]:
                    evidence["diagnostic"] = "\n".join(texts)
            for text in texts[1:]:
                found.extend(printed_signals(text))
            return found
        for block in value:
            found.extend(signals(block))
    elif isinstance(value, dict):
        if value.get("type") in ("text", "input_text"):
            return signals(value.get("text"))
        # Promise.allSettled records may be printed directly, in arrays, or
        # inside the indexed {i, result: ...} wrapper used by local sessions.
        if value.get("status") == "fulfilled" and "value" in value:
            return signals(value["value"])
        if value.get("status") == "rejected" and "reason" in value:
            return [{"signals": ["promise_rejected"], "exit_code": None,
                     "diagnostic": str(value["reason"])}]
        if isinstance(value.get("result"), dict) and value["result"].get("status") in (
            "fulfilled", "rejected"
        ):
            return signals(value["result"])
        code = value.get("exit_code")
        reasons = []
        if type(code) is int and code != 0:
            reasons.append("nonzero_exit")
        if value.get("isError") is True:
            reasons.append("isError")
        if reasons:
            found.append({"signals": reasons, "exit_code": code,
                          "diagnostic": str(value.get("output", value))})
        # Never recurse into output: a successful command may print error
        # examples or JSON containing nonzero exit codes as ordinary data.
        for key in ("content", "structuredContent"):
            if key in value:
                found.extend(signals(value[key]))
    elif isinstance(value, str):
        envelope = EXEC_STATUS.match(value)
        if envelope:
            if envelope[1] == "failed":
                found.append({"signals": ["script_failed"], "exit_code": None,
                              "diagnostic": value})
            # exec prints a sequence of values, not necessarily one JSON value.
            # Decode only its leading JSON stream, never arbitrary stdout lines.
            found.extend(printed_signals(value[envelope.end():]))
            return found
        try:
            structured = json.loads(value)
        except ValueError:
            structured = None
        if isinstance(structured, (dict, list)):
            return signals(structured)
        match = SHELL_STATUS.match(value)
        if match and int(match[1]) != 0:
            found.append({"signals": ["nonzero_exit"], "exit_code": int(match[1]),
                          "diagnostic": value})
        elif value.startswith(("Error:", "Error parsing function call:",
                               "failed to parse function arguments:", "exec_command failed:",
                               "write_stdin failed:", "apply_patch verification failed:")):
            found.append({"signals": ["tool_error_prefix"], "exit_code": None,
                          "diagnostic": value})
    return found


def printed_signals(text: str) -> list[dict[str, Any]]:
    """Decode JSON values printed by exec, stopping when non-JSON text begins."""
    found = []
    body = text.lstrip()
    decoder = json.JSONDecoder()
    while body:
        try:
            structured, end = decoder.raw_decode(body)
        except ValueError:
            break
        if isinstance(structured, (dict, list)):
            found.extend(signals(structured))
        body = body[end:].lstrip()
    return found


def scan(path: Path) -> dict[str, Any]:
    report: dict[str, Any] = {
        "trace": str(path), "format": "codex-session", "session_id": None,
        "cwd": None, "first_timestamp": None, "last_timestamp": None,
        "last_line": 0, "cutoff_utc": None, "tool_results_seen": 0,
        "findings": [], "input_issues": [],
    }
    calls: dict[str, tuple[int, dict[str, Any]]] = {}
    outputs: dict[str, dict[str, Any]] = {}
    recognized = False

    def issue(line: int | None, message: str) -> None:
        report["input_issues"].append({"line": line, "message": message})

    try:
        with path.open("rb") as stream:
            # Freeze the byte boundary so a live file cannot extend this scan.
            remaining = os.fstat(stream.fileno()).st_size
            line = 0
            while remaining > 0:
                raw = stream.readline(remaining + 1)
                if not raw:
                    break
                remaining -= len(raw)
                if remaining < 0:
                    issue(line + 1, "record crosses initial file boundary; not inspected")
                    break
                line += 1
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
                kind = event.get("type")
                if not isinstance(kind, str):
                    issue(line, "record type is not a string")
                    continue
                payload = event.get("payload")
                if kind not in {"session_meta", "response_item", "event_msg",
                                "turn_context", "compacted", "world_state",
                                "token_usage_record", "inter_agent_communication_metadata"}:
                    issue(line, f"unsupported rollout record type: {kind!r}")
                    continue
                if not isinstance(payload, dict):
                    issue(line, "rollout record lacks payload object")
                    continue
                recognized = True
                stamp = event.get("timestamp")
                if isinstance(stamp, str):
                    if report["first_timestamp"] is None:
                        report["first_timestamp"] = stamp
                    report["last_timestamp"] = stamp
                if kind == "session_meta":
                    report["session_id"] = payload.get("id") or payload.get("session_id")
                    report["cwd"] = payload.get("cwd")
                # event_msg can duplicate response items. Only response_item is
                # authoritative for tool accounting in native rollouts.
                if kind != "response_item":
                    continue
                item_type = payload.get("type")
                if not isinstance(item_type, str):
                    issue(line, "response item type is not a string")
                    continue
                if item_type not in CALL_TYPES | OUTPUT_TYPES:
                    continue
                cid = payload.get("call_id")
                if not isinstance(cid, str) or not cid:
                    issue(line, "tool record lacks call_id")
                    continue
                if item_type in CALL_TYPES:
                    if cid in calls:
                        if calls[cid][1] != payload:
                            issue(line, f"conflicting duplicate call: {cid}")
                        continue
                    calls[cid] = (line, payload)
                    continue
                if cid in outputs:
                    if outputs[cid] != payload:
                        issue(line, f"conflicting duplicate output: {cid}")
                    continue
                outputs[cid] = payload
                report["tool_results_seen"] += 1
                call = calls.get(cid)
                if call is None:
                    issue(line, f"output has no preceding call: {cid}")
                output = payload.get("output")
                if not isinstance(output, (str, list, dict)):
                    issue(line, "tool output is absent or unsupported")
                    continue
                evidence = signals(output)
                if not evidence:
                    continue
                source = call[1] if call else {}
                args = source.get("arguments", source.get("input"))
                if source.get("type") == "function_call" and isinstance(args, str):
                    try:
                        args = json.loads(args)
                    except ValueError:
                        pass  # Invalid arguments can themselves explain a failure.
                for item in evidence:
                    diagnostic = item.pop("diagnostic")
                    item["diagnostic_excerpt"] = diagnostic[-EXCERPT_LIMIT:]
                    item["diagnostic_truncated"] = len(diagnostic) > EXCERPT_LIMIT
                report["findings"].append({
                    "line": line, "timestamp": stamp, "tool_call_id": cid,
                    "tool_name": source.get("name"), "call_line": call[0] if call else None,
                    "arguments": args,
                    "command": args.get("cmd", args.get("command")) if isinstance(args, dict) else None,
                    "evidence": evidence, "recovery": "not_assessed",
                })
    except (OSError, UnicodeError) as exc:
        issue(None, str(exc))
    if not recognized:
        issue(None, "no recognized Codex rollout records; empty or unsupported trace")
    for cid, (line, _) in calls.items():
        if cid not in outputs:
            issue(line, f"call has no output at scan cutoff: {cid}")
    report["cutoff_utc"] = datetime.now(UTC).isoformat()
    return trace_result(report, harness="codex", checks=("tool_failures",),
                        branch_scope="stored_records")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=["codex-session"], default="codex-session")
    parser.add_argument("traces", type=Path, nargs="+", help="explicit native rollout JSONL paths")
    args = parser.parse_args()
    reports = [scan(path) for path in dict.fromkeys(p.resolve() for p in args.traces)]
    print(json.dumps(scan_report(
        reports, scope="explicit failure candidates and supported observations; recovery not assessed",
    ), indent=2, ensure_ascii=False))
    return 2 if any(r["input_issues"] for r in reports) else 0


if __name__ == "__main__":
    raise SystemExit(main())
