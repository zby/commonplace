"""Every scanner CLI must feed one consumer without harness-specific field reads."""

import json
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker

from tests.commonplace.tooling.test_scan_claude_code_tool_failures import result, use
from tests.commonplace.tooling.test_scan_codex_tool_failures import record
from tests.commonplace.tooling.test_scan_tool_failures import call, end, message, start
from tests.commonplace.tooling.test_scan_tool_failures import result as pi_result

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = json.loads((ROOT / "scripts/scan_tools/result.schema.json").read_text())
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())
CASES = [
    ("pi", "pi-json", [start(), end()]),
    ("pi", "pi-session", [
        {"type": "session", "id": "s"}, message("a", None, call("false")),
        message("b", "a", pi_result()),
    ]),
    ("codex", "codex-session", [
        record("session_meta", {"id": "s", "cwd": "/project"}),
        record("response_item", {"type": "function_call", "call_id": "call",
                                 "name": "exec_command", "arguments": '{"cmd":"false"}'}),
        record("response_item", {"type": "function_call_output", "call_id": "call",
                                 "output": {"exit_code": 1, "output": "failed"}}),
    ]),
    ("claude_code", "claude-code-session", [use("a", None), result("b", "a")]),
    ("claude_code", "claude-stream-json", [
        {"type": "system", "subtype": "init", "session_id": "s"},
        use("a", None), result("b", "a"),
        {"type": "result", "subtype": "success", "is_error": False},
    ]),
]


@pytest.mark.parametrize("harness,trace_format,records", CASES, ids=[c[1] for c in CASES])
def test_cli_contract_preserves_evidence_and_distinguishes_coverage(tmp_path, harness, trace_format, records):
    path = tmp_path / "trace.jsonl"
    original = "".join(json.dumps(r) + "\n" for r in records)
    argv = [sys.executable, str(ROOT / f"scripts/scan_tools/scan_{harness}_tool_failures.py")]
    if harness != "claude_code":
        argv += ["--format", trace_format]
    suffixes = ["", '{"incomplete":', '{"type": [], "payload": {}}']
    if harness == "codex":
        suffixes.append(json.dumps(record("response_item", {"type": []})))
    elif harness == "claude_code":
        suffixes.append(json.dumps({"type": "user", "message": {
            "content": [{"type": "text", "text": None}],
        }}))
    for suffix in suffixes:
        broken = bool(suffix)
        path.write_text(original + suffix)
        before = path.read_bytes()
        proc = subprocess.run([*argv, str(path)], capture_output=True, text=True, check=False)
        assert path.read_bytes() == before
        assert proc.returncode == (2 if broken else 0)
        output = json.loads(proc.stdout)
        VALIDATOR.validate(output)
        assert output["schema_version"] == 2
        assert output["finding_count"] == 1
        [trace] = output["traces"]
        assert trace["format"] == trace_format
        assert trace["tool_results_seen"] == 1
        coverage = trace["coverage"]
        assert coverage["input_status"] == ("partial" if broken else "read")
        assert coverage["last_line"] == len(records) + broken
        assert coverage["checks"]["tool_failures"] == "supported"
        assert coverage["checks"]["recovery"] == "unsupported"
        assert coverage["checks"]["provider_errors"] == ("supported" if harness == "claude_code" else "unsupported")
        [finding] = trace["findings"]
        assert finding["line"] > finding["call_line"]
        assert finding["tool_call_id"]
        assert finding["command"] == "false"
        assert finding["evidence"][0]["exit_code"] != 0
        assert "nonzero_exit" in finding["evidence"][0]["signals"]
        assert finding["recovery"] == "not_assessed"


def test_schema_rejects_old_shape_and_missing_coverage():
    Draft202012Validator.check_schema(SCHEMA)
    assert not VALIDATOR.is_valid({"schema_version": 1, "failure_count": 0, "traces": []})
    from commonplace.lib.trace_scan import scan_report

    assert VALIDATOR.is_valid(scan_report([], scope="no inputs selected"))
    assert not VALIDATOR.is_valid(scan_report([{"findings": []}], scope="missing coverage"))


def test_malformed_native_fields_still_emit_valid_partial_evidence(tmp_path):
    # A schema must also hold on bad inputs; retain the original value rather
    # than making the consumer guess whether a boolean exit code means success.
    from commonplace.lib.trace_scan import scan_report
    from tests.commonplace.tooling.test_scan_codex_tool_failures import run_scan

    code, output, trace = run_scan(tmp_path, [
        record("session_meta", {"id": 42}),
        record("response_item", {"type": "function_call", "call_id": "c", "name": "exec",
                                 "arguments": '{"cmd":false}'}),
        record("response_item", {"type": "function_call_output", "call_id": "c",
                                 "output": {"isError": True, "exit_code": False}}),
    ])
    VALIDATOR.validate(output)
    assert code == 2
    assert trace["coverage"]["input_status"] == "partial"
    assert trace["session_id"] is None
    assert trace["details"]["invalid_fields"]["session_id"] == 42
    [finding] = trace["findings"]
    assert finding["command"] is None
    assert finding["details"]["invalid_fields"]["command"] is False
    assert finding["evidence"][0]["exit_code"] is None
    assert finding["evidence"][0]["details"]["native_exit_code"] is False
    assert scan_report([trace], scope="partial input")["finding_count"] == 1
