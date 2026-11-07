"""CLI regressions: Codex envelopes, duplicate accounting and partial evidence."""

import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[3] / "scripts/scan_tools/scan_codex_tool_failures.py"


def record(kind, payload):
    return {"timestamp": "2026-11-07T10:00:00Z", "type": kind, "payload": payload}


def run_scan(tmp_path, records, suffix=""):
    trace = tmp_path / "rollout.jsonl"
    trace.write_text("".join(json.dumps(r) + "\n" for r in records) + suffix)
    before = trace.read_bytes()
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(trace), str(trace)],
        capture_output=True, text=True, check=False,
    )
    assert trace.read_bytes() == before
    report = json.loads(result.stdout)
    assert len(report["traces"]) == 1
    return result.returncode, report, report["traces"][0]


def test_native_wrapped_results_and_duplicate_events(tmp_path):
    call = record("response_item", {
        "type": "custom_tool_call", "call_id": "c1", "name": "functions.exec",
        "input": "text(await tools.exec_command({cmd: 'rg absent file'}))",
    })
    output = record("response_item", {
        "type": "custom_tool_call_output", "call_id": "c1",
        "output": [{"type": "input_text", "text": json.dumps({
            "exit_code": 1, "output": "missing\u2028match",
        })}],
    })
    code, report, trace = run_scan(tmp_path, [
        record("session_meta", {"id": "s1", "cwd": "/project"}), call,
        record("event_msg", {"type": "item_completed", "item": {"exit_code": 1}}),
        output, output,
    ])
    assert code == 0
    assert report["failure_count"] == trace["completed_tools"] == 1
    failure = trace["failures"][0]
    assert failure["call_line"] == 2 and failure["line"] == 4
    assert failure["evidence"][0]["exit_code"] == 1
    assert failure["recovery"] == "not_assessed"
    assert trace["session_id"] == "s1" and trace["last_line"] == 5


def test_shell_envelope_and_successful_stdout_are_distinct(tmp_path):
    records = []
    for cid, output in [
        ("bad", "Chunk ID: abc\nWall time: 0.2 seconds\nProcess exited with code 2\nFinal output:\nfailed"),
        ("good", "Wall time: 0.2 seconds\nProcess exited with code 0\nFinal output:\nError: example\nProcess exited with code 2"),
        ("patch", "apply_patch verification failed: missing file"),
    ]:
        records.extend([
            record("response_item", {"type": "function_call", "call_id": cid,
                                     "name": "exec_command", "arguments": '{"cmd":"test"}'}),
            record("response_item", {"type": "function_call_output", "call_id": cid,
                                     "output": output}),
        ])
    code, report, trace = run_scan(tmp_path, records)
    assert code == 0 and report["failure_count"] == 2
    assert trace["completed_tools"] == 3
    assert trace["failures"][0]["command"] == "test"
    assert [f["tool_call_id"] for f in trace["failures"]] == ["bad", "patch"]


def test_partial_input_retains_failures_and_correlation_gaps(tmp_path):
    code, report, trace = run_scan(tmp_path, [
        record("response_item", {"type": "function_call_output", "call_id": "orphan",
                                 "output": {"isError": True, "output": "x" * 900}}),
        record("response_item", {"type": "function_call", "call_id": "pending",
                                 "name": "exec_command", "arguments": "{}"}),
    ], suffix='{"type":')
    assert code == 2 and report["failure_count"] == 1
    messages = [i["message"] for i in trace["scan_issues"]]
    assert any("no preceding call" in m for m in messages)
    assert any("no output" in m for m in messages)
    assert any("invalid JSON" in m for m in messages)
    evidence = trace["failures"][0]["evidence"][0]
    assert evidence["diagnostic_truncated"]
    assert len(evidence["diagnostic_excerpt"]) == 600


def test_other_harness_is_not_a_clean_scan(tmp_path):
    code, _, trace = run_scan(tmp_path, [{"type": "session", "id": "pi"}])
    assert code == 2 and trace["scan_issues"]
