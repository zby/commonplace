"""Command construction and synthetic harness-event parsing.

These tests do not invoke a model or establish live adapter support.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from treadle_headless.adapters import (
    claude_worker,
    codex_worker,
    parse_evidence,
    pi_worker,
)
from treadle_headless.models import CommandWorker


def _render(worker):
    paths = {
        "prompt": Path("/tmp/launch-1/prompt.txt"),
        "input_dir": Path("/tmp/launch-1/inputs"),
        "output_dir": Path("/tmp/launch-1/outputs"),
        "problem_file": Path("/tmp/launch-1/problem.json"),
        "evidence_file": Path("/tmp/launch-1/evidence.json"),
        "launch_dir": Path("/tmp/launch-1"),
        "workdir": Path("/tmp/project"),
    }
    return worker.command(paths)


def test_codex_command_has_explicit_model_sandbox_and_unattended_policy():
    command = _render(codex_worker("gpt-6.1-sol", sandbox="workspace-write", effort="medium"))
    assert command[:2] == ("codex", "exec")
    assert ("-m", "gpt-6.1-sol") == command[command.index("-m") : command.index("-m") + 2]
    assert ("-s", "workspace-write") == command[command.index("-s") : command.index("-s") + 2]
    assert "approval_policy=never" in command
    assert "model_reasoning_effort=medium" in command
    assert "--skip-git-repo-check" in command
    assert "/tmp/launch-1/prompt.txt" in command[-1]
    assert "--dangerously-bypass-approvals-and-sandbox" not in command
    assert "--ignore-rules" not in command


def test_claude_command_requires_tool_choice_and_denies_unanswered_prompts():
    command = _render(claude_worker("sonnet", allowed_tools=("Read", "Write")))
    assert command[:2] == ("claude", "-p")
    assert command[command.index("--model") + 1] == "sonnet"
    assert command[command.index("--permission-mode") + 1] == "dontAsk"
    assert command[command.index("--permission-prompts") + 1] == "none"
    assert "--allowedTools=Read,Write" in command
    assert "--verbose" in command
    assert "/tmp/launch-1/prompt.txt" in command[-1]
    assert "--dangerously-skip-permissions" not in command
    assert "--bare" not in command


def test_pi_command_requires_provider_tools_and_trust_choice():
    command = _render(
        pi_worker(
            "gpt-6.1-sol", provider="openai", tools=("read", "write"), project_trust="no-approve"
        )
    )
    assert command[:3] == ("pi", "--mode", "json")
    assert command[command.index("--provider") + 1] == "openai"
    assert command[command.index("--model") + 1] == "gpt-6.1-sol"
    assert command[command.index("--tools") + 1] == "read,write"
    assert "--no-approve" in command
    assert command[command.index("--session-dir") + 1] == "/tmp/launch-1"
    assert "/tmp/launch-1/prompt.txt" in command[-1]


def test_command_rendering_keeps_literal_braces_while_replacing_path_tokens():
    command = _render(CommandWorker(argv=("worker", '{"literal": 1}', "{prompt}")))
    assert command == ("worker", '{"literal": 1}', "/tmp/launch-1/prompt.txt")


@pytest.mark.parametrize(
    "build",
    [
        lambda: codex_worker("", sandbox="workspace-write"),
        lambda: codex_worker("m", sandbox="invalid"),
        lambda: codex_worker("{prompt}", sandbox="workspace-write"),
        lambda: claude_worker("m", allowed_tools=()),
        lambda: claude_worker("m", allowed_tools=("Read,Bash",)),
        lambda: pi_worker("m", provider="p", tools=("read",), project_trust="unknown"),
    ],
)
def test_invalid_adapter_configuration_is_rejected(build):
    with pytest.raises(ValueError):
        build()


def _jsonl(*records):
    return "\n".join(json.dumps(record) for record in records)


def test_codex_evidence_keeps_session_and_terminal_failure_without_model_guess():
    evidence = parse_evidence(
        "codex",
        _jsonl(
            {"type": "thread.started", "thread_id": "thread-1"},
            {"type": "turn.started"},
            {"type": "turn.failed", "error": {"message": "failure"}},
        ),
    )
    assert evidence["session_id"] == "thread-1"
    assert evidence["turn_outcome"] == "turn.failed"
    assert "served_model" not in evidence


def test_claude_retry_rate_limit_is_not_a_final_usage_limit_claim():
    evidence = parse_evidence(
        "claude",
        _jsonl(
            {"type": "system", "subtype": "api_retry", "error": "rate_limit"},
            {"type": "assistant", "message": {"model": "claude-sonnet-example"}},
            {"type": "result", "subtype": "success", "session_id": "session-1", "is_error": False},
        ),
    )
    assert evidence["retry_error_categories"] == ["rate_limit"]
    assert evidence["is_error"] is False
    assert evidence["session_id"] == "session-1"
    assert evidence["reported_model"] == "claude-sonnet-example"
    assert "served_model" not in evidence


def test_pi_evidence_distinguishes_requested_and_concrete_response_model():
    evidence = parse_evidence(
        "pi",
        _jsonl(
            {"type": "session", "id": "pi-1", "cwd": "/tmp/project"},
            {
                "type": "message_end",
                "message": {
                    "role": "assistant",
                    "provider": "openai",
                    "model": "model-alias",
                    "responseModel": "concrete-model",
                    "responseId": "resp-1",
                    "stopReason": "stop",
                },
            },
            {"type": "agent_settled", "aborted": False},
        ),
    )
    assert evidence["session_id"] == "pi-1"
    assert evidence["reported_model"] == "model-alias"
    assert evidence["served_model"] == "concrete-model"
    assert evidence["response_id"] == "resp-1"
    assert evidence["settled_aborted"] is False


def test_partial_and_malformed_stream_does_not_invent_completion():
    evidence = parse_evidence("pi", '{"type":"session","id":"pi-2"}\nnot json\n')
    assert evidence["session_id"] == "pi-2"
    assert evidence["parse_errors"] == 1
    assert "settled_aborted" not in evidence
    assert "served_model" not in evidence


def test_jsonl_parser_does_not_split_unicode_line_separator_inside_text():
    raw = json.dumps(
        {"type": "message_end", "message": {"role": "assistant", "model": "m\u2028v"}},
        ensure_ascii=False,
    )
    evidence = parse_evidence("pi", raw + "\n")
    assert evidence["records"] == 1
    assert evidence["parse_errors"] == 0
    assert evidence["reported_model"] == "m\u2028v"
