"""Prevent operative instructions from bypassing harness delegation."""

from __future__ import annotations

import re
import shlex
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]

SHELL_FENCE = re.compile(
    r"(?ms)^```(?:bash|sh|shell|zsh|fish|powershell|pwsh)\s*\n(?P<body>.*?)^```\s*$"
)
COMMAND_SEPARATORS = {";", "&", "&&", "|", "||"}
SIMPLE_WRAPPERS = {"command", "env", "exec", "nohup", "sudo"}
AGENT_CLIS = {"claude", "codex"}


def _command_segments(line: str) -> list[list[str]]:
    lexer = shlex.shlex(line, posix=True, punctuation_chars=";&|")
    lexer.commenters = "#"
    lexer.whitespace_split = True
    segments: list[list[str]] = [[]]
    try:
        for token in lexer:
            if token in COMMAND_SEPARATORS:
                segments.append([])
            else:
                segments[-1].append(token)
    except ValueError:
        # Shell fences may contain multiline awk or heredoc bodies whose quote
        # state is not meaningful one logical shell line at a time. A simple
        # fallback still catches a command-position agent CLI on that line.
        return [
            segment.split()
            for segment in re.split(r"&&|\|\||[;|]", line)
            if segment.strip()
        ]
    return [segment for segment in segments if segment]


def _logical_shell_lines(body: str) -> list[tuple[int, str]]:
    logical_lines: list[tuple[int, str]] = []
    parts: list[str] = []
    start_offset = 0
    for offset, line in enumerate(body.splitlines()):
        if not parts:
            start_offset = offset
        stripped = line.rstrip()
        if stripped.endswith("\\"):
            parts.append(stripped[:-1])
            continue
        parts.append(line)
        logical_lines.append((start_offset, " ".join(parts)))
        parts = []
    if parts:
        logical_lines.append((start_offset, " ".join(parts)))
    return logical_lines


def _launched_agent_cli(segment: list[str]) -> str | None:
    tokens = list(segment)
    if tokens and tokens[0] == "$":
        tokens.pop(0)

    while tokens and (
        tokens[0] in SIMPLE_WRAPPERS
        or re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*=.*", tokens[0])
    ):
        tokens.pop(0)

    if len(tokens) >= 2 and tokens[:2] == ["uv", "run"]:
        tokens = tokens[2:]
    elif tokens and tokens[0] == "uvx":
        tokens = tokens[1:]

    if not tokens:
        return None
    command = Path(tokens[0].replace("\\", "/")).name.lower()
    return command if command in AGENT_CLIS else None


def _agent_cli_launches(markdown: str) -> list[tuple[int, str]]:
    launches: list[tuple[int, str]] = []
    for fence in SHELL_FENCE.finditer(markdown):
        first_line = markdown.count("\n", 0, fence.start("body")) + 1
        for offset, line in _logical_shell_lines(fence.group("body")):
            for segment in _command_segments(line):
                command = _launched_agent_cli(segment)
                if command is not None:
                    launches.append((first_line + offset, command))
    return launches


def _operative_instruction_paths() -> tuple[Path, ...]:
    relative_paths = [Path("AGENTS.md"), Path("AGENTS.md.template")]
    relative_paths.extend(
        path.relative_to(REPO_ROOT)
        for path in (REPO_ROOT / "kb/instructions").rglob("*.md")
    )
    return tuple(sorted(relative_paths))


def test_agent_cli_launch_detection_covers_common_shell_forms() -> None:
    markdown = """```bash
claude -p task
env MODE=test codex exec task
build && /usr/local/bin/codex exec task
$ uv run claude -p task
```
"""

    assert _agent_cli_launches(markdown) == [
        (2, "claude"),
        (3, "codex"),
        (4, "codex"),
        (5, "claude"),
    ]


def test_operative_instructions_do_not_launch_agent_clis() -> None:
    violations = []
    for relative_path in _operative_instruction_paths():
        text = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
        violations.extend(
            f"{relative_path}:{line}: {command}"
            for line, command in _agent_cli_launches(text)
        )

    assert violations == []
