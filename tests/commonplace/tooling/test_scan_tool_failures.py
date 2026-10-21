"""Failure observations must not become recovery or whole-run verdicts."""

import json
import subprocess
import sys
from pathlib import Path

import pytest

from commonplace.lib.agentic_analysis.tool_failures import scan

SCRIPT = Path(__file__).resolve().parents[3] / "scripts/scan_tool_failures.py"


def trace(tmp_path, records):
    path = tmp_path / "trace.jsonl"
    path.write_text("\n".join(json.dumps(record, ensure_ascii=False) for record in records) + "\n")
    return path


def start(cid="call", command="false"):
    return {"type": "tool_execution_start", "toolCallId": cid, "toolName": "bash",
            "args": {"command": command}}


def end(cid="call", error=True, text="Command exited with code 1", **extra):
    return {"type": "tool_execution_end", "toolCallId": cid, "toolName": "bash",
            "isError": error, "result": {"content": [{"type": "text", "text": text}], **extra}}


def test_stream_failure_then_success_is_not_a_recovery_verdict(tmp_path):
    path = trace(tmp_path, [start(command="rg absent file"), end(), start("retry", "true"),
                            end("retry", error=False, text="")])
    result = scan(path, "pi-json")
    assert result["completed_tools"] == 2
    assert result["scan_issues"] == []
    assert len(result["failures"]) == 1
    failure = result["failures"][0]
    assert (failure["line"], failure["call_line"], failure["exit_code"]) == (2, 1, 1)
    assert failure["command"] == "rg absent file"
    assert failure["recovery"] == "not_assessed"


def test_ignore_repeated_messages_partial_output_and_failure_prose(tmp_path):
    result_message = {"role": "toolResult", "isError": True, "toolCallId": "call"}
    path = trace(tmp_path, [start(), {"type": "tool_execution_update", "isError": True},
                            end(), {"type": "message_end", "message": result_message},
                            {"type": "turn_end", "toolResults": [result_message]},
                            {"type": "agent_end", "messages": [result_message]}])
    assert len(scan(path, "pi-json")["failures"]) == 1
    path = trace(tmp_path, [start(), end(error=False, text="Error: example\nCommand exited with code 1")])
    assert scan(path, "pi-json")["failures"] == []


def test_structured_nonzero_code_and_bounded_diagnostic(tmp_path):
    path = trace(tmp_path, [start(), end(error=False, text="x" * 700,
                                        structuredContent={"exit_code": 2})])
    failure = scan(path, "pi-json")["failures"][0]
    assert failure["signals"] == ["nonzero_exit"]
    assert failure["exit_code"] == 2
    assert failure["diagnostic_truncated"] is True
    assert len(failure["diagnostic_excerpt"]) == 600


def test_non_shell_error_without_exit_code(tmp_path):
    first, last = start(), end(text="ENOENT")
    first["toolName"], first["args"] = "read", {"path": "missing"}
    last["toolName"] = "read"
    failure = scan(trace(tmp_path, [first, last]), "pi-json")["failures"][0]
    assert failure["exit_code"] is None
    assert failure["arguments"] == {"path": "missing"}


def message(eid, parent, body):
    return {"type": "message", "id": eid, "parentId": parent, "message": body}


def call(command):
    return {"role": "assistant", "content": [
        {"type": "toolCall", "id": "same-id", "name": "bash", "arguments": {"command": command}}]}


def result():
    return {"role": "toolResult", "toolCallId": "same-id", "toolName": "bash",
            "isError": True, "content": [{"type": "text", "text": "Command exited with code 7"}]}


def test_session_correlates_ancestors_not_latest_branch_and_survives_compaction(tmp_path):
    path = trace(tmp_path, [
        {"type": "session", "version": 3, "id": "session-1"},
        message("a", None, call("original")),
        message("b", None, call("other branch")),
        {"type": "compaction", "id": "c", "parentId": "a", "summary": "compacted"},
        message("d", "c", result()), message("e", "b", result()),
    ])
    report = scan(path, "pi-session")
    assert report["session_id"] == "session-1"
    assert report["scan_issues"] == []
    assert [failure["command"] for failure in report["failures"]] == ["original", "other branch"]
    assert [failure["entry_id"] for failure in report["failures"]] == ["d", "e"]


def test_malformed_line_preserves_later_findings(tmp_path):
    path = tmp_path / "trace.jsonl"
    path.write_text(json.dumps(start()) + "\nnot-json\n" + json.dumps(end()) + "\n")
    report = scan(path, "pi-json")
    assert report["scan_issues"][0]["line"] == 2
    assert report["failures"][0]["line"] == 3


@pytest.mark.parametrize("records", [[], [42], [{"type": "unrelated"}]])
def test_empty_or_unsupported_is_not_a_clean_scan(tmp_path, records):
    assert scan(trace(tmp_path, records), "pi-json")["scan_issues"]


def test_missing_start_and_unfinished_call_are_visible(tmp_path):
    report = scan(trace(tmp_path, [end(), start("unfinished")]), "pi-json")
    assert report["failures"][0]["arguments"] is None
    assert len(report["scan_issues"]) == 2


def test_unicode_separators_are_not_record_boundaries(tmp_path):
    report = scan(trace(tmp_path, [start(), end(text="a\u2028b\u2029c")]), "pi-json")
    assert report["scan_issues"] == []
    assert report["failures"][0]["diagnostic_excerpt"] == "a\u2028b\u2029c"


@pytest.mark.parametrize("trace_format,record", [
    ("pi-session", start()),
    ("pi-json", message("a", None, call("false"))),
])
def test_wrong_format_does_not_silently_report_no_failures(tmp_path, trace_format, record):
    path = trace(tmp_path, [{"type": "session", "version": 3, "id": "s"}, record])
    assert scan(path, trace_format)["scan_issues"]


def test_absent_error_flag_is_an_input_issue(tmp_path):
    event = end()
    del event["isError"]
    report = scan(trace(tmp_path, [start(), event]), "pi-json")
    assert report["scan_issues"]
    assert report["failures"] == []


def test_missing_file_is_reported(tmp_path):
    report = scan(tmp_path / "absent", "pi-json")
    assert report["scan_issues"]


def test_cli_exit_zero_with_failures_and_two_with_input_issues(tmp_path):
    path = trace(tmp_path, [start(), end()])
    run = subprocess.run([sys.executable, str(SCRIPT), "--format", "pi-json", str(path), str(path)],
                         capture_output=True, text=True, check=False)
    assert run.returncode == 0
    output = json.loads(run.stdout)
    assert output["failure_count"] == 1
    assert len(output["traces"]) == 1
    path.write_text("{truncated")
    run = subprocess.run([sys.executable, str(SCRIPT), "--format", "pi-json", str(path)],
                         capture_output=True, text=True, check=False)
    assert run.returncode == 2
    assert json.loads(run.stdout)["traces"][0]["scan_issues"]
