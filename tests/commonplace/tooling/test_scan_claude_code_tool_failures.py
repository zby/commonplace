"""Claude Code session and stream scans: ID correlation across blocks and branches, no recovery verdicts."""

import json
import subprocess
import sys
from pathlib import Path

import pytest

from commonplace.lib.agentic_analysis.claude_code_tool_failures import scan

SCRIPT = Path(__file__).resolve().parents[3] / "scripts/scan_tools/scan_claude_code_tool_failures.py"


def observations(report, kind):
    return [o for o in report["observations"] if o["kind"] == kind]


def trace(tmp_path, records, name="session.jsonl"):
    path = tmp_path / name
    path.write_text(
        "\n".join(json.dumps(record, ensure_ascii=False) for record in records) + "\n", encoding="utf-8"
    )
    return path


def use(uuid, parent, cid="toolu_1", name="Bash", command="false", **extra):
    return {"type": "assistant", "uuid": uuid, "parentUuid": parent, "sessionId": "s1",
            "cwd": "/project", "timestamp": "2026-11-07T10:00:00.000Z",
            "message": {"role": "assistant", "content": [
                {"type": "tool_use", "id": cid, "name": name, "input": {"command": command}}]},
            **extra}


def result(uuid, parent, cid="toolu_1", text="Exit code 1\nboom", error=True, **extra):
    block = {"type": "tool_result", "tool_use_id": cid, "content": text}
    if error is not None:
        block["is_error"] = error
    return {"type": "user", "uuid": uuid, "parentUuid": parent, "sessionId": "s1",
            "timestamp": "2026-11-07T10:00:01.000Z",
            "message": {"role": "user", "content": [block]}, **extra}


def test_failure_then_success_is_not_a_recovery_verdict(tmp_path):
    path = trace(tmp_path, [
        use("a", None, command="rg absent file"), result("b", "a"),
        use("c", "b", cid="toolu_2", command="true"),
        result("d", "c", cid="toolu_2", text="", error=False),
    ])
    report = scan(path)
    assert report["session_id"] == "s1"
    assert report["tool_results_seen"] == 2
    assert report["input_issues"] == []
    assert len(report["findings"]) == 1
    failure = report["findings"][0]
    assert (failure["line"], failure["call_line"], failure["evidence"][0]["exit_code"]) == (2, 1, 1)
    assert failure["command"] == "rg absent file"
    assert failure["evidence"][0]["signals"] == ["tool_error", "nonzero_exit"]
    assert failure["recovery"] == "not_assessed"
    assert (report["coverage"]["last_line"], report["coverage"]["last_timestamp"]) == (4, "2026-11-07T10:00:01.000Z")
    assert report["coverage"]["first_timestamp"] == "2026-11-07T10:00:00.000Z"
    assert report["cwd"] == "/project"


def test_absent_error_flag_is_success_and_exit_text_in_success_is_ignored(tmp_path):
    path = trace(tmp_path, [
        use("a", None), result("b", "a", text="File created", error=None),
        use("c", "b", cid="toolu_2"), result("d", "c", cid="toolu_2", text="Exit code 1\nx", error=False),
    ])
    report = scan(path)
    assert report["findings"] == []
    assert report["input_issues"] == []
    assert report["tool_results_seen"] == 2


def test_tool_use_found_across_block_records_attachments_and_branches(tmp_path):
    # Claude Code writes one assistant record per content block and may interpose
    # attachment records; rewinds leave several children under one parent.
    path = trace(tmp_path, [
        use("a", None, command="first block"),
        {"type": "assistant", "uuid": "a2", "parentUuid": "a", "message": {
            "role": "assistant", "content": [{"type": "text", "text": "then"}]}},
        {"type": "attachment", "uuid": "att", "parentUuid": "a2", "attachment": {}},
        result("b", "att"),
        use("x", "a", cid="toolu_9", command="rewound branch"),
        result("y", "x", cid="toolu_9", text="Exit code 2\nno"),
    ])
    report = scan(path)
    assert report["input_issues"] == []
    assert [f["command"] for f in report["findings"]] == ["first block", "rewound branch"]
    assert [f["entry_id"] for f in report["findings"]] == ["b", "y"]


def test_harness_outcomes_get_distinct_signals(tmp_path):
    texts = {
        "toolu_1": "The user doesn't want to proceed with this tool use. The tool use was rejected",
        "toolu_2": "Permission for this action was denied by the Claude Code auto mode classifier.",
        "toolu_3": "<tool_use_error>Blocked: sleep 30 followed by: x</tool_use_error>",
        "toolu_4": "getaddrinfo ENOTFOUND example.invalid",
    }
    records, parent = [], None
    for index, (cid, text) in enumerate(texts.items()):
        records.append(use(f"u{index}", parent, cid=cid, name="WebFetch" if cid == "toolu_4" else "Bash"))
        records.append(result(f"r{index}", f"u{index}", cid=cid, text=text))
        parent = f"r{index}"
    report = scan(trace(tmp_path, records))
    assert [f["evidence"][0]["signals"] for f in report["findings"]] == [
        ["tool_error", "user_rejected"], ["tool_error", "permission_denied"],
        ["tool_error", "tool_use_error"], ["tool_error"],
    ]
    assert report["findings"][3]["evidence"][0]["exit_code"] is None
    assert report["findings"][3]["tool_name"] == "WebFetch"


def test_harness_strings_quoted_in_successful_output_are_not_failures(tmp_path):
    quoted = ("The user doesn't want to proceed with this tool use\n"
              "Permission for this action was denied\n<tool_use_error>x</tool_use_error>")
    path = trace(tmp_path, [
        use("a", None, command="cat log"), result("b", "a", text=quoted, error=False),
        use("c", "b", cid="toolu_2", command="cat log"), result("d", "c", cid="toolu_2", text=quoted, error=None),
        use("e", "d", cid="toolu_3", command="cat log"), result("f", "e", cid="toolu_3", text=quoted),
    ])
    report = scan(path)
    assert report["input_issues"] == []
    assert [f["entry_id"] for f in report["findings"]] == ["f"]
    assert report["findings"][0]["evidence"][0]["signals"] == [
        "tool_error", "user_rejected", "permission_denied", "tool_use_error",
    ]


def test_exit_code_only_parsed_for_shell_or_unknown_tool(tmp_path):
    path = trace(tmp_path, [
        use("a", None, name="Write"), result("b", "a", text="Exit code 3\nnot a shell"),
        result("orphan", "b", cid="toolu_missing", text="Exit code 4\nno call"),
    ])
    report = scan(path)
    assert [f["evidence"][0]["exit_code"] for f in report["findings"]] == [None, 4]
    assert report["findings"][1]["arguments"] is None
    assert len(report["input_issues"]) == 1
    assert "no matching tool_use" in report["input_issues"][0]["message"]


def test_api_errors_interruptions_compactions_and_workers_are_listed(tmp_path):
    path = trace(tmp_path, [
        {"type": "assistant", "uuid": "e", "parentUuid": None, "sessionId": "s1",
         "isApiErrorMessage": True, "error": "authentication_failed",
         "message": {"role": "assistant", "content": [{"type": "text", "text": "Login expired"}]}},
        {"type": "user", "uuid": "i", "parentUuid": "e", "message": {
            "role": "user", "content": [{"type": "text", "text": "[Request interrupted by user for tool use]"}]}},
        {"type": "user", "uuid": "i2", "parentUuid": "i", "message": {
            "role": "user", "content": "[Request interrupted by user]"}},
        {"type": "system", "subtype": "compact_boundary", "uuid": "c", "parentUuid": None,
         "logicalParentUuid": "i2", "compactMetadata": {"trigger": "auto", "preTokens": 254216}},
        use("a", "c", name="Agent"),
        {**result("b", "a", text="Async agent launched", error=None),
         "toolUseResult": {"agentId": "af86", "status": "forked"}},
    ])
    report = scan(path)
    assert report["findings"] == []
    assert report["input_issues"] == []
    assert observations(report, "provider_error") == [{
        "kind": "provider_error", "line": 1, "entry_id": "e", "block_index": None, "timestamp": None,
        "details": {"error": "authentication_failed", "text": "Login expired"},
    }]
    assert [i["line"] for i in observations(report, "interruption")] == [2, 3]
    assert observations(report, "compaction")[0]["details"]["pre_tokens"] == 254216
    assert observations(report, "compaction")[0]["details"]["logical_parent"] == "i2"
    assert report["details"]["worker_ids"] == ["af86"]


def test_subagent_file_reports_agent_id(tmp_path):
    records = [use("a", None, agentId="af86", isSidechain=True), result("b", "a", agentId="af86")]
    report = scan(trace(tmp_path, records, name="agent-af86.jsonl"))
    assert report["agent_id"] == "af86"
    assert len(report["findings"]) == 1


def test_bounded_diagnostic_and_unicode_separators(tmp_path):
    report = scan(trace(tmp_path, [use("a", None), result("b", "a", text="Exit code 1\n" + "x" * 700)]))
    failure = report["findings"][0]
    assert failure["evidence"][0]["diagnostic_truncated"] is True
    assert len(failure["evidence"][0]["diagnostic_excerpt"]) == 600
    report = scan(trace(tmp_path, [use("a", None), result("b", "a", text="a b c")]))
    assert report["input_issues"] == []
    assert report["findings"][0]["evidence"][0]["diagnostic_excerpt"] == "a b c"


def test_malformed_line_preserves_later_findings(tmp_path):
    path = tmp_path / "session.jsonl"
    path.write_text(json.dumps(use("a", None)) + "\nnot-json\n" + json.dumps(result("b", "a")) + "\n",
                    encoding="utf-8")
    report = scan(path)
    assert report["input_issues"][0]["line"] == 2
    assert report["findings"][0]["line"] == 3


@pytest.mark.parametrize("records", [
    [], [42], [{"type": "unrelated"}],
    [{"type": "session", "version": 3, "id": "pi"}],
    [{"type": "response_item", "payload": {}}],
])
def test_empty_or_foreign_input_is_not_a_clean_scan(tmp_path, records):
    assert scan(trace(tmp_path, records))["input_issues"]


def test_missing_file_is_reported(tmp_path):
    assert scan(tmp_path / "absent")["input_issues"]


def test_stream_json_correlates_by_id_and_records_denials_and_result(tmp_path):
    # `claude --print --output-format stream-json` records carry uuid and
    # session_id but no parentUuid; successful tool_results omit is_error.
    sid = "766c8fb8-1897-47da-9516-181f85c85201"

    def call(cid, command):
        return {"type": "assistant", "uuid": f"u-{cid}", "session_id": sid, "parent_tool_use_id": None,
                "message": {"role": "assistant", "content": [
                    {"type": "tool_use", "id": cid, "name": "Bash", "input": {"command": command}}]}}

    def answer(cid, text, **flag):
        return {"type": "user", "uuid": f"r-{cid}", "session_id": sid, "parent_tool_use_id": None,
                "message": {"role": "user", "content": [
                    {"type": "tool_result", "tool_use_id": cid, "content": text, **flag}]}}

    path = trace(tmp_path, [
        {"type": "system", "subtype": "init", "cwd": "/worktree", "session_id": sid, "uuid": "i"},
        call("toolu_1", "ls"), answer("toolu_1", "README.md"),
        call("toolu_2", "cd x && git status"),
        {"type": "system", "subtype": "permission_denied", "tool_name": "Bash", "tool_use_id": "toolu_2",
         "decision_reason_type": "other", "decision_reason": "changes directory", "session_id": sid},
        answer("toolu_2", "Permission for this action was denied", is_error=True),
        {"type": "result", "subtype": "success", "is_error": False, "num_turns": 3, "session_id": sid,
         "permission_denials": [{"tool_name": "Bash", "tool_use_id": "toolu_2"}]},
    ], name="stdout.log")
    report = scan(path)
    assert report["input_issues"] == []
    assert report["format"] == "claude-stream-json"
    assert (report["session_id"], report["cwd"]) == (sid, "/worktree")
    assert report["tool_results_seen"] == 2
    [failure] = report["findings"]
    assert (failure["tool_name"], failure["call_line"], failure["command"]) == ("Bash", 4, "cd x && git status")
    assert failure["evidence"][0]["signals"] == ["tool_error", "permission_denied"]
    assert observations(report, "permission_denial") == [{
        "kind": "permission_denial", "line": 5, "entry_id": None, "timestamp": None, "block_index": None,
        "details": {"tool_name": "Bash", "tool_use_id": "toolu_2", "decision_reason": "changes directory"},
    }]
    assert report["details"]["result"] == {"subtype": "success", "is_error": False, "num_turns": 3,
                                "permission_denials": 1}


def test_session_file_has_no_stream_fields(tmp_path):
    # Real session records may carry session_id beside sessionId; that is not a stream.
    report = scan(trace(tmp_path, [use("a", None, session_id="s1"), result("b", "a", session_id="s1")]))
    assert report["format"] == "claude-code-session"
    assert (observations(report, "permission_denial"), report["details"]["result"]) == ([], None)


def test_cli_exit_zero_with_failures_and_two_with_input_issues(tmp_path):
    path = trace(tmp_path, [use("a", None), result("b", "a")])
    before = path.read_bytes()
    run = subprocess.run([sys.executable, str(SCRIPT), str(path), str(path)],
                         capture_output=True, text=True, check=False)
    assert run.returncode == 0
    assert path.read_bytes() == before
    output = json.loads(run.stdout)
    assert output["finding_count"] == 1
    assert len(output["traces"]) == 1
    path.write_text("{truncated", encoding="utf-8")
    run = subprocess.run([sys.executable, str(SCRIPT), str(path)],
                         capture_output=True, text=True, check=False)
    assert run.returncode == 2
    assert json.loads(run.stdout)["traces"][0]["input_issues"]
