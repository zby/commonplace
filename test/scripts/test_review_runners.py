from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


review_runners = load_module("review_runners_test", SCRIPTS_DIR / "review_runners.py")


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
