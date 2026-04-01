from __future__ import annotations

import json
import os
import subprocess
import sys
import threading
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RunnerResult:
    stdout: str
    stderr: str
    returncode: int


REVIEW_RUNNER_SYSTEM_PROMPT = (
    "Your goal is to write a series of review artifacts for the requested gates. "
    "The task prompt is self-contained; do not open workflow instruction files unless a command errors and you need to debug the failure. "
    "Trust the review helper scripts and use them as command interfaces. "
    "Do not inspect helper script source unless a command errors and you need to debug the failure. "
    "Do not do broad repository exploration; stay within the target note, the requested gate definitions, "
    "and links explicitly reachable from the target note when the gate requires it."
)


def _stream_pipe(pipe, sink, chunks: list[str]) -> None:
    try:
        for line in iter(pipe.readline, ""):
            chunks.append(line)
            sink.write(line)
            sink.flush()
    finally:
        pipe.close()


def _extract_claude_text_content(payload: object) -> str:
    if not isinstance(payload, list):
        return ""
    parts: list[str] = []
    for block in payload:
        if not isinstance(block, dict):
            continue
        if block.get("type") != "text":
            continue
        text = block.get("text")
        if isinstance(text, str):
            parts.append(text)
    return "".join(parts)


def _summarize_claude_block(block: object) -> str:
    if not isinstance(block, dict):
        return ""
    block_type = block.get("type")
    if block_type == "tool_use":
        name = block.get("name")
        tool_input = block.get("input")
        suffix = ""
        if tool_input is not None:
            rendered = json.dumps(tool_input, ensure_ascii=True, sort_keys=True)
            if len(rendered) > 240:
                rendered = rendered[:237] + "..."
            suffix = f" {rendered}"
        if isinstance(name, str):
            return f"\n[tool] {name}{suffix}\n"
        return f"\n[tool]{suffix}\n"
    if block_type == "tool_result":
        tool_use_id = block.get("tool_use_id")
        if isinstance(tool_use_id, str):
            return f"\n[tool-result] {tool_use_id}\n"
        return "\n[tool-result]\n"
    return ""


def _stream_claude_json_pipe(pipe, sink, chunks: list[str]) -> None:
    current_message_id: str | None = None
    current_message_text = ""
    current_nontext_blocks: set[tuple[int, str]] = set()
    saw_assistant_text = False

    try:
        for line in iter(pipe.readline, ""):
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                chunks.append(line)
                sink.write(line)
                sink.flush()
                continue

            if not isinstance(event, dict):
                continue

            event_type = event.get("type")
            emitted = ""
            if event_type in {"assistant", "user"}:
                message = event.get("message")
                if isinstance(message, dict):
                    message_id = message.get("id")
                    if isinstance(message_id, str) and message_id != current_message_id:
                        current_message_id = message_id
                        current_message_text = ""
                        current_nontext_blocks = set()
                    content = message.get("content")
                    text = _extract_claude_text_content(content)
                    if text.startswith(current_message_text):
                        emitted = text[len(current_message_text) :]
                    elif text != current_message_text:
                        emitted = text
                    current_message_text = text
                    if emitted:
                        saw_assistant_text = True
                    if isinstance(content, list):
                        for index, block in enumerate(content):
                            if not isinstance(block, dict):
                                continue
                            block_type = block.get("type")
                            if block_type == "text" or not isinstance(block_type, str):
                                continue
                            key = (index, block_type)
                            if key in current_nontext_blocks:
                                continue
                            summary = _summarize_claude_block(block)
                            if summary:
                                emitted += summary
                                current_nontext_blocks.add(key)
            elif event_type == "result" and not saw_assistant_text:
                result_text = event.get("result")
                if isinstance(result_text, str):
                    emitted = result_text

            if emitted:
                chunks.append(emitted)
                sink.write(emitted)
                sink.flush()
    finally:
        pipe.close()


def run_prompt(
    *,
    runner: str,
    prompt: str,
    repo_root: Path,
    model: str | None = None,
) -> RunnerResult:
    env = os.environ.copy()

    if runner == "claude-code":
        cmd = [
            "claude",
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
        cmd.extend(["--append-system-prompt", REVIEW_RUNNER_SYSTEM_PROMPT])
        if model:
            cmd.extend(["--model", model])
        cmd.append(prompt)
    elif runner == "codex":
        cmd = ["codex", "exec", "--full-auto", "-C", str(repo_root)]
        if model:
            cmd.extend(["--model", model])
        cmd.append(f"{REVIEW_RUNNER_SYSTEM_PROMPT}\n\n{prompt}")
    else:
        raise ValueError(f"unsupported runner: {runner}")

    process = subprocess.Popen(
        cmd,
        cwd=repo_root,
        env=env,
        text=True,
        bufsize=1,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert process.stdout is not None
    assert process.stderr is not None

    stdout_chunks: list[str] = []
    stderr_chunks: list[str] = []
    stdout_thread = threading.Thread(
        target=_stream_claude_json_pipe if runner == "claude-code" else _stream_pipe,
        args=(process.stdout, sys.stdout, stdout_chunks),
        daemon=True,
    )
    stderr_thread = threading.Thread(
        target=_stream_pipe,
        args=(process.stderr, sys.stderr, stderr_chunks),
        daemon=True,
    )
    stdout_thread.start()
    stderr_thread.start()
    returncode = process.wait()
    stdout_thread.join()
    stderr_thread.join()

    return RunnerResult(
        stdout="".join(stdout_chunks),
        stderr="".join(stderr_chunks),
        returncode=returncode,
    )
