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
        record("token_usage_record", {"usage": {"input_tokens": 10}}),
        record("inter_agent_communication_metadata", {"trigger_turn": "worker"}),
    ])
    assert code == 0
    assert report["finding_count"] == trace["tool_results_seen"] == 1
    failure = trace["findings"][0]
    assert failure["call_line"] == 2 and failure["line"] == 4
    assert failure["evidence"][0]["exit_code"] == 1
    assert failure["recovery"] == "not_assessed"
    assert trace["session_id"] == "s1" and trace["coverage"]["last_line"] == 7


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
    assert code == 0 and report["finding_count"] == 2
    assert trace["tool_results_seen"] == 3
    assert trace["findings"][0]["command"] == "test"
    assert [f["tool_call_id"] for f in trace["findings"]] == ["bad", "patch"]


def test_partial_input_retains_failures_and_correlation_gaps(tmp_path):
    code, report, trace = run_scan(tmp_path, [
        record("response_item", {"type": "function_call_output", "call_id": "orphan",
                                 "output": {"isError": True, "output": "x" * 900}}),
        record("response_item", {"type": "function_call", "call_id": "pending",
                                 "name": "exec_command", "arguments": "{}"}),
    ], suffix='{"type":')
    assert code == 2 and report["finding_count"] == 1
    messages = [i["message"] for i in trace["input_issues"]]
    assert any("no preceding call" in m for m in messages)
    assert any("no output" in m for m in messages)
    assert any("invalid JSON" in m for m in messages)
    evidence = trace["findings"][0]["evidence"][0]
    assert evidence["diagnostic_truncated"]
    assert len(evidence["diagnostic_excerpt"]) == 600


def test_other_harness_is_not_a_clean_scan(tmp_path):
    code, _, trace = run_scan(tmp_path, [{"type": "session", "id": "pi"}])
    assert code == 2 and trace["input_issues"]


def test_exec_envelopes_keep_script_failures_and_nested_results(tmp_path):
    failed_header = "Script failed\nWall time 0.1 seconds\nOutput:\n"
    completed_header = "Script completed\nWall time 0.1 seconds\nOutput:\n"
    command = {"exit_code": 2, "output": "missing required file"}
    settled = {"status": "fulfilled", "value": command}
    inputs = {
        "split_script_error": [
            {"type": "input_text", "text": failed_header},
            {"type": "input_text", "text": "Script error:\napply_patch verification failed: missing file"},
        ],
        "string_script_error": failed_header + "\nScript error:\nSyntaxError: Unexpected token",
        "settled": [{"type": "input_text", "text": json.dumps(settled)}],
        "indexed": {"i": 0, "result": settled},
        "array": [settled, {"status": "fulfilled", "value": {"exit_code": 0}}],
        "printed_values": completed_header + json.dumps({"exit_code": 0}) + "\n" + json.dumps(settled),
        "prose_then_result": [
            {"type": "input_text", "text": completed_header},
            {"type": "input_text", "text": "Progress message"},
            {"type": "input_text", "text": json.dumps(settled)},
        ],
        "rejected": {"status": "rejected", "reason": "tool unavailable"},
    }
    records = []
    for cid, output in inputs.items():
        records.extend([
            record("response_item", {"type": "custom_tool_call", "call_id": cid,
                                     "name": "exec", "input": "text(result)"}),
            record("response_item", {"type": "custom_tool_call_output", "call_id": cid,
                                     "output": output}),
        ])
    # A repeated envelope must not inflate the number of failed operations.
    records.append(records[-1])
    code, report, trace = run_scan(tmp_path, records)
    assert code == 0
    assert report["finding_count"] == trace["tool_results_seen"] == len(inputs)
    failures = {f["tool_call_id"]: f for f in trace["findings"]}
    for cid in ("split_script_error", "string_script_error"):
        evidence = failures[cid]["evidence"]
        assert len(evidence) == 1
        assert evidence[0]["signals"] == ["script_failed"]
        assert "Script error:" in evidence[0]["diagnostic_excerpt"]
    for cid in ("settled", "indexed", "array", "printed_values", "prose_then_result"):
        assert failures[cid]["evidence"][0]["exit_code"] == 2
    assert failures["rejected"]["evidence"][0]["signals"] == ["promise_rejected"]


def test_successful_command_output_is_not_parsed_as_exec_status(tmp_path):
    # Documentation and fixtures printed by a successful command are data,
    # even if they look exactly like harness failures or Promise results.
    examples = 'Script failed\nWall time 0 seconds\nOutput:\nScript error: example\n'
    examples += json.dumps({"status": "fulfilled", "value": {"exit_code": 9}})
    result = {"status": "fulfilled", "value": {"exit_code": 0, "output": examples}}
    code, report, trace = run_scan(tmp_path, [
        record("response_item", {"type": "custom_tool_call", "call_id": "ok",
                                 "name": "exec", "input": "text(result)"}),
        record("response_item", {"type": "custom_tool_call_output", "call_id": "ok",
                                 "output": [
                                     {"type": "input_text", "text": "Script completed\nWall time 0 seconds\nOutput:\n"},
                                     {"type": "input_text", "text": json.dumps(result)},
                                 ]}),
    ])
    assert code == 0 and report["finding_count"] == 0
    assert trace["tool_results_seen"] == 1
