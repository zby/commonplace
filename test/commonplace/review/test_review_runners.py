from __future__ import annotations

import os
from pathlib import Path

from commonplace.review import review_runners


def install_fake_codex(fake_codex: Path, *, emit_session_id: bool, reasoning_effort: str = "xhigh") -> None:
    session_id = "019d54ab-17a2-73b0-b341-3f36434aa48b"
    emit_session_id_line = 'print(f"session id: {session_id}", flush=True)' if emit_session_id else ""
    fake_codex.write_text(
        f"""#!/usr/bin/env python3
import json
import os
import sys
from pathlib import Path

args = sys.argv[1:]
required = ["exec", "--full-auto", "-C"]
for item in required:
    if item not in args:
        raise SystemExit(f"missing arg: {{item}}")

prompt = sys.argv[-1]
home = Path(os.environ["HOME"])
session_id = "{session_id}"
session_dir = home / ".codex" / "sessions" / "2026" / "04" / "03"
session_dir.mkdir(parents=True, exist_ok=True)
session_log = session_dir / f"rollout-2026-04-03T20-46-32-{{session_id}}.jsonl"
events = [
    {{
        "type": "session_meta",
        "payload": {{
            "id": session_id,
            "timestamp": "2026-04-03T20:46:32.019Z",
            "cwd": os.getcwd(),
            "originator": "codex_cli_rs",
            "cli_version": "0.0.0",
            "model_provider": "openai",
        }},
    }},
    {{
        "type": "turn_context",
        "payload": {{
            "cwd": os.getcwd(),
            "approval_policy": "never",
            "sandbox_policy": {{
                "mode": "workspace-write",
                "writable_roots": [os.getcwd()],
            }},
            "model": "gpt-5.4",
            "collaboration_mode": {{
                "mode": "default",
                "settings": {{
                    "model": "gpt-5.4",
                    "reasoning_effort": "{reasoning_effort}",
                }},
            }},
            "effort": "{reasoning_effort}",
        }},
    }},
    {{
        "type": "response_item",
        "payload": {{
            "type": "message",
            "role": "user",
            "content": [{{"type": "input_text", "text": prompt}}],
        }},
    }},
    {{
        "type": "event_msg",
        "payload": {{
            "type": "task_started",
            "turn_id": "turn-1",
        }},
    }},
    {{
        "type": "event_msg",
        "payload": {{
            "type": "token_count",
            "info": {{
                "model_context_window": 272000,
                "last_token_usage": {{
                    "input_tokens": 100,
                    "cached_input_tokens": 50,
                    "output_tokens": 25,
                    "reasoning_output_tokens": 10,
                    "total_tokens": 175,
                }},
                "total_token_usage": {{
                    "input_tokens": 100,
                    "cached_input_tokens": 50,
                    "output_tokens": 25,
                    "reasoning_output_tokens": 10,
                    "total_tokens": 175,
                }},
            }},
            "rate_limits": {{"primary": {{"used_percent": 7}}}},
        }},
    }},
    {{
        "type": "event_msg",
        "payload": {{
            "type": "token_count",
            "info": {{
                "model_context_window": 272000,
                "last_token_usage": {{
                    "input_tokens": 34414,
                    "cached_input_tokens": 34304,
                    "output_tokens": 267,
                    "reasoning_output_tokens": 154,
                    "total_tokens": 34681,
                }},
                "total_token_usage": {{
                    "input_tokens": 387914,
                    "cached_input_tokens": 375168,
                    "output_tokens": 8994,
                    "reasoning_output_tokens": 6144,
                    "total_tokens": 396908,
                }},
            }},
            "rate_limits": {{"primary": {{"used_percent": 12}}}},
        }},
    }},
    {{
        "type": "event_msg",
        "payload": {{
            "type": "task_complete",
            "turn_id": "turn-1",
            "last_agent_message": "Finished review bundle",
        }},
    }},
]
with session_log.open("w", encoding="utf-8") as handle:
    for event in events:
        handle.write(json.dumps(event) + "\\n")

{emit_session_id_line}
print("=== GATE REVIEW START: frontmatter ===", flush=True)
print("Looks good.", flush=True)
print("", flush=True)
print("## Result: pass", flush=True)
print("=== GATE REVIEW END: frontmatter ===", flush=True)
""",
        encoding="utf-8",
    )
    fake_codex.chmod(0o755)


def test_run_prompt_streams_claude_json(monkeypatch, tmp_path: Path, capsys) -> None:
    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    fake_claude = fake_bin / "claude"
    fake_claude.write_text(
        """#!/usr/bin/env python3
import json
import sys

args = sys.argv[1:]
required = [
    "-p",
    "--verbose",
    "--output-format",
    "stream-json",
    "--include-partial-messages",
    "--permission-mode",
    "acceptEdits",
    "--tools",
    "Bash,Read,Edit,Write,Glob,Grep",
    "--allowedTools",
    "Bash,Read,Edit,Write,Glob,Grep",
]
for item in required:
    if item not in args:
        raise SystemExit(f"missing arg: {item}")

for event in [
    {"type": "system", "subtype": "init"},
    {
        "type": "assistant",
        "message": {
            "id": "msg-1",
            "content": [
                {"type": "text", "text": "Hel"},
                {"type": "tool_use", "name": "Bash", "input": {"command": "pwd"}},
            ],
        },
    },
    {
        "type": "assistant",
        "message": {
            "id": "msg-1",
            "content": [
                {"type": "text", "text": "Hello"},
                {"type": "tool_use", "name": "Bash", "input": {"command": "pwd"}},
            ],
        },
    },
    {
        "type": "result",
        "subtype": "success",
        "is_error": False,
        "result": "Hello",
    },
]:
    print(json.dumps(event), flush=True)
""",
        encoding="utf-8",
    )
    fake_claude.chmod(0o755)

    monkeypatch.setenv("PATH", f"{fake_bin}:{os.environ['PATH']}")

    result = review_runners.run_prompt(
        runner="claude-code",
        prompt="test prompt",
        repo_root=tmp_path,
    )

    assert result.returncode == 0
    assert result.stdout == 'Hel\n[tool] Bash {"command": "pwd"}\nlo'
    captured = capsys.readouterr()
    assert captured.out == 'Hel\n[tool] Bash {"command": "pwd"}\nlo'
    assert captured.err == ""


def test_run_prompt_collects_usage_without_request_id(monkeypatch, tmp_path: Path) -> None:
    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    fake_claude = fake_bin / "claude"
    fake_claude.write_text(
        """#!/usr/bin/env python3
import json
import sys

for event in [
    {"type": "system", "subtype": "init"},
    {
        "type": "assistant",
        "message": {
            "id": "msg-1",
            "model": "claude-test",
            "usage": {
                "input_tokens": 10,
                "cache_creation_input_tokens": 2,
                "cache_read_input_tokens": 3,
                "output_tokens": 5,
            },
            "content": [{"type": "text", "text": "Hel"}],
        },
    },
    {
        "type": "assistant",
        "message": {
            "id": "msg-1",
            "model": "claude-test",
            "usage": {
                "input_tokens": 10,
                "cache_creation_input_tokens": 2,
                "cache_read_input_tokens": 3,
                "output_tokens": 5,
            },
            "content": [{"type": "text", "text": "Hello"}],
        },
    },
    {"type": "result", "subtype": "success", "is_error": False, "result": "Hello"},
]:
    print(json.dumps(event), flush=True)
""",
        encoding="utf-8",
    )
    fake_claude.chmod(0o755)

    monkeypatch.setenv("PATH", f"{fake_bin}:{os.environ['PATH']}")

    result = review_runners.run_prompt(
        runner="claude-code",
        prompt="test prompt",
        repo_root=tmp_path,
    )

    assert result.returncode == 0
    assert result.telemetry is not None
    assert result.telemetry["model"] == "claude-test"
    assert result.telemetry["models"] == ["claude-test"]
    assert result.telemetry["totals"] == {
        "input_tokens": 10,
        "cache_creation_input_tokens": 2,
        "cache_read_input_tokens": 3,
        "output_tokens": 5,
        "total_tokens": 20,
        "request_count": 1,
    }
    assert result.telemetry["first_request"]["request_id"] is None
    assert result.telemetry["first_request"]["message_id"] == "msg-1"


def test_run_prompt_uses_claude_init_model_when_usage_model_is_synthetic(monkeypatch, tmp_path: Path) -> None:
    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    fake_claude = fake_bin / "claude"
    fake_claude.write_text(
        """#!/usr/bin/env python3
import json

for event in [
    {"type": "system", "subtype": "init", "model": "claude-opus-4-6"},
    {
        "type": "assistant",
        "message": {
            "id": "msg-1",
            "model": "<synthetic>",
            "usage": {
                "input_tokens": 0,
                "cache_creation_input_tokens": 0,
                "cache_read_input_tokens": 0,
                "output_tokens": 0,
            },
            "content": [{"type": "text", "text": "You're out of extra usage"}],
        },
    },
    {"type": "result", "subtype": "success", "is_error": True, "result": "You're out of extra usage"},
]:
    print(json.dumps(event), flush=True)
""",
        encoding="utf-8",
    )
    fake_claude.chmod(0o755)

    monkeypatch.setenv("PATH", f"{fake_bin}:{os.environ['PATH']}")

    result = review_runners.run_prompt(
        runner="claude-code",
        prompt="test prompt",
        repo_root=tmp_path,
    )

    assert result.telemetry is not None
    assert result.telemetry["model"] == "claude-opus-4-6"
    assert result.telemetry["models"] == ["claude-opus-4-6"]
    assert result.telemetry["init_model"] == "claude-opus-4-6"
    assert result.telemetry["requests"][0]["model"] == "<synthetic>"


def test_run_prompt_falls_back_to_claude_session_log_usage(monkeypatch, tmp_path: Path) -> None:
    fake_home = tmp_path / "home"
    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    fake_claude = fake_bin / "claude"
    fake_claude.write_text(
        """#!/usr/bin/env python3
import json
import os
import sys
from pathlib import Path

prompt = sys.argv[-1]
home = Path(os.environ["HOME"])
project_key = os.getcwd().replace(os.sep, "-")
project_dir = home / ".claude" / "projects" / project_key
project_dir.mkdir(parents=True, exist_ok=True)
session_id = "session-123"
session_log = project_dir / f"{session_id}.jsonl"
session_events = [
    {
        "type": "queue-operation",
        "operation": "enqueue",
        "timestamp": "2026-04-03T15:17:37.974Z",
        "sessionId": session_id,
        "content": prompt,
    },
    {
        "parentUuid": None,
        "isSidechain": False,
        "promptId": "prompt-1",
        "type": "user",
        "message": {"role": "user", "content": prompt},
        "uuid": "user-1",
        "timestamp": "2026-04-03T15:17:37.992Z",
        "cwd": os.getcwd(),
        "sessionId": session_id,
    },
    {
        "type": "assistant",
        "uuid": "assistant-1",
        "timestamp": "2026-04-03T15:17:39.632Z",
        "sessionId": session_id,
        "message": {
            "id": "msg-session-1",
            "model": "claude-test",
            "role": "assistant",
            "type": "message",
            "usage": {
                "input_tokens": 11,
                "cache_creation_input_tokens": 7,
                "cache_read_input_tokens": 13,
                "output_tokens": 17,
            },
            "content": [{"type": "text", "text": "Hello"}],
        },
    },
]
with session_log.open("w", encoding="utf-8") as handle:
    for event in session_events:
        handle.write(json.dumps(event) + "\\n")

for event in [
    {"type": "system", "subtype": "init"},
    {
        "type": "assistant",
        "message": {
            "id": "msg-session-1",
            "content": [{"type": "text", "text": "Hello"}],
        },
    },
    {"type": "result", "subtype": "success", "is_error": False, "result": "Hello"},
]:
    print(json.dumps(event), flush=True)
""",
        encoding="utf-8",
    )
    fake_claude.chmod(0o755)

    monkeypatch.setenv("HOME", str(fake_home))
    monkeypatch.setenv("PATH", f"{fake_bin}:{os.environ['PATH']}")

    result = review_runners.run_prompt(
        runner="claude-code",
        prompt="test prompt",
        repo_root=tmp_path,
    )

    assert result.returncode == 0
    assert result.telemetry is not None
    assert result.telemetry["model"] == "claude-test"
    assert result.telemetry["models"] == ["claude-test"]
    assert result.telemetry["totals"] == {
        "input_tokens": 11,
        "cache_creation_input_tokens": 7,
        "cache_read_input_tokens": 13,
        "output_tokens": 17,
        "total_tokens": 48,
        "request_count": 1,
    }
    assert result.telemetry["requests"][0]["source"] == "session-log"


def test_run_prompt_collects_codex_telemetry_from_session_id(monkeypatch, tmp_path: Path) -> None:
    fake_home = tmp_path / "home"
    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    fake_codex = fake_bin / "codex"
    install_fake_codex(fake_codex, emit_session_id=True)

    monkeypatch.setenv("HOME", str(fake_home))
    monkeypatch.setenv("PATH", f"{fake_bin}:{os.environ['PATH']}")

    result = review_runners.run_prompt(
        runner="codex",
        prompt="test prompt",
        repo_root=tmp_path,
        model="gpt-5.4",
    )

    assert result.returncode == 0
    assert result.telemetry is not None
    assert result.telemetry["provider"] == "codex"
    assert result.telemetry["source"] == "session-log"
    assert result.telemetry["session_id"] == "019d54ab-17a2-73b0-b341-3f36434aa48b"
    assert result.telemetry["model"] == "gpt-5.4"
    assert result.telemetry["reasoning_effort"] == "xhigh"
    assert result.telemetry["token_count_events"] == 2
    assert result.telemetry["totals"] == {
        "input_tokens": 387914,
        "cached_input_tokens": 375168,
        "output_tokens": 8994,
        "reasoning_output_tokens": 6144,
        "total_tokens": 396908,
    }
    assert result.telemetry["last_usage"] == {
        "input_tokens": 34414,
        "cached_input_tokens": 34304,
        "output_tokens": 267,
        "reasoning_output_tokens": 154,
        "total_tokens": 34681,
    }


def test_run_prompt_falls_back_to_codex_prompt_match(monkeypatch, tmp_path: Path) -> None:
    fake_home = tmp_path / "home"
    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    fake_codex = fake_bin / "codex"
    install_fake_codex(fake_codex, emit_session_id=False)

    monkeypatch.setenv("HOME", str(fake_home))
    monkeypatch.setenv("PATH", f"{fake_bin}:{os.environ['PATH']}")

    result = review_runners.run_prompt(
        runner="codex",
        prompt="test prompt",
        repo_root=tmp_path,
        model="gpt-5.4",
    )

    assert result.returncode == 0
    assert result.telemetry is not None
    assert result.telemetry["session_id"] == "019d54ab-17a2-73b0-b341-3f36434aa48b"
    assert result.telemetry["task_complete_message"] == "Finished review bundle"
    assert result.telemetry["reasoning_effort"] == "xhigh"
    assert result.telemetry["rate_limits"] == {"primary": {"used_percent": 12}}
