from __future__ import annotations

import json
import os
import re
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
    telemetry: dict[str, object] | None = None


CLAUDE_TOKEN_FIELDS = (
    "input_tokens",
    "cache_creation_input_tokens",
    "cache_read_input_tokens",
    "output_tokens",
)

CODEX_TOKEN_FIELDS = (
    "input_tokens",
    "cached_input_tokens",
    "output_tokens",
    "reasoning_output_tokens",
    "total_tokens",
)

CODEX_SESSION_ID_RE = re.compile(r"(?m)^session id:\s*(\S+)\s*$")


REVIEW_RUNNER_SYSTEM_PROMPT = (
    "Your goal is to write a series of review artifacts for the requested gates. "
    "The task prompt provides the exact note, gate definitions, and output contract for the run. "
    "Stay within the target note, the provided gate definitions, and only the linked neighborhood that the active gates require. "
    "Do not do broad repository exploration or search for alternate gate definitions. "
    "Treat helper scripts as command interfaces; inspect workflow files or script source only if a command fails and you need to debug it."
)


def _stream_pipe(pipe, sink, chunks: list[str]) -> None:
    try:
        for line in iter(pipe.readline, ""):
            chunks.append(line)
            sink.write(line)
            sink.flush()
    finally:
        pipe.close()


def _coerce_usage_int(value: object) -> int:
    return value if isinstance(value, int) and not isinstance(value, bool) else 0


def _usage_totals_from_requests(requests: list[dict[str, object]]) -> dict[str, int]:
    totals = {
        field: sum(
            _coerce_usage_int((request.get("usage") or {}).get(field))
            for request in requests
            if isinstance(request.get("usage"), dict)
        )
        for field in CLAUDE_TOKEN_FIELDS
    }
    totals["total_tokens"] = sum(totals[field] for field in CLAUDE_TOKEN_FIELDS)
    return totals


def _first_request_summary(request: dict[str, object]) -> dict[str, object]:
    summary: dict[str, object] = {
        "request_id": request.get("request_id"),
        "message_id": request.get("message_id"),
        "timestamp": request.get("timestamp"),
        "model": request.get("model"),
    }
    summary.update(_usage_totals_from_requests([request]))
    return summary


def _build_claude_telemetry(
    requests: list[dict[str, object]],
) -> dict[str, object] | None:
    if not requests:
        return None

    totals = _usage_totals_from_requests(requests)
    totals["request_count"] = len(requests)
    first_request = _first_request_summary(requests[0])
    followup_requests = requests[1:]
    followup_totals = _usage_totals_from_requests(followup_requests)
    followup_totals["request_count"] = len(followup_requests)
    return {
        "provider": "claude-code",
        "requests": requests,
        "totals": totals,
        "first_request": first_request,
        "followup_totals": followup_totals,
    }


def _usage_entry_ids(entry: dict[str, object]) -> tuple[str, ...]:
    ids: list[str] = []
    request_id = entry.get("request_id")
    if isinstance(request_id, str) and request_id:
        ids.append(f"request:{request_id}")
    message_id = entry.get("message_id")
    if isinstance(message_id, str) and message_id:
        ids.append(f"message:{message_id}")
    event_uuid = entry.get("event_uuid")
    if isinstance(event_uuid, str) and event_uuid:
        ids.append(f"uuid:{event_uuid}")
    return tuple(ids)


def _usage_entry_from_event(event: object, *, source: str) -> dict[str, object] | None:
    if not isinstance(event, dict):
        return None

    message = event.get("message")
    if not isinstance(message, dict):
        return None

    usage = message.get("usage")
    if not isinstance(usage, dict):
        return None

    entry: dict[str, object] = {
        "request_id": event.get("requestId"),
        "message_id": message.get("id"),
        "event_uuid": event.get("uuid"),
        "session_id": event.get("sessionId"),
        "timestamp": event.get("timestamp"),
        "model": message.get("model"),
        "usage": usage,
        "source": source,
    }
    if not _usage_entry_ids(entry):
        return None
    return entry


def _merge_usage_entry(target: dict[str, object], incoming: dict[str, object]) -> None:
    for key in ("request_id", "message_id", "event_uuid", "session_id", "timestamp", "model"):
        if target.get(key) in (None, "") and incoming.get(key) not in (None, ""):
            target[key] = incoming[key]
    if isinstance(incoming.get("usage"), dict):
        target["usage"] = incoming["usage"]
    source = incoming.get("source")
    if target.get("source") == source or source in (None, ""):
        return
    if isinstance(target.get("source"), list):
        if source not in target["source"]:
            target["source"].append(source)
        return
    existing = target.get("source")
    if existing in (None, ""):
        target["source"] = source
        return
    if existing == source:
        return
    target["source"] = [existing, source]


def _record_claude_usage_entry(
    request_usage_entries: list[dict[str, object]],
    request_usage_index: dict[str, int],
    event: object,
    *,
    source: str,
) -> None:
    entry = _usage_entry_from_event(event, source=source)
    if entry is None:
        return

    existing_index: int | None = None
    for entry_id in _usage_entry_ids(entry):
        if entry_id in request_usage_index:
            existing_index = request_usage_index[entry_id]
            break

    if existing_index is None:
        request_usage_entries.append(entry)
        existing_index = len(request_usage_entries) - 1
    else:
        _merge_usage_entry(request_usage_entries[existing_index], entry)

    for entry_id in _usage_entry_ids(request_usage_entries[existing_index]):
        request_usage_index[entry_id] = existing_index


def _claude_project_session_dir(repo_root: Path) -> Path:
    home = Path(os.path.expanduser("~"))
    project_key = str(repo_root.resolve()).replace(os.sep, "-")
    return home / ".claude" / "projects" / project_key


def _snapshot_claude_session_logs(repo_root: Path) -> dict[Path, int]:
    session_dir = _claude_project_session_dir(repo_root)
    if not session_dir.is_dir():
        return {}
    snapshot: dict[Path, int] = {}
    for path in session_dir.glob("*.jsonl"):
        try:
            snapshot[path] = path.stat().st_mtime_ns
        except FileNotFoundError:
            continue
    return snapshot


def _session_log_matches_prompt(session_log: Path, prompt: str) -> bool:
    try:
        with session_log.open(encoding="utf-8") as handle:
            for _ in range(8):
                line = handle.readline()
                if not line:
                    return False
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if not isinstance(event, dict):
                    continue
                content = event.get("content")
                if isinstance(content, str) and content == prompt:
                    return True
                message = event.get("message")
                if not isinstance(message, dict):
                    continue
                message_content = message.get("content")
                if isinstance(message_content, str) and message_content == prompt:
                    return True
    except OSError:
        return False
    return False


def _find_matching_claude_session_log(
    *,
    repo_root: Path,
    prompt: str,
    session_log_snapshot: dict[Path, int],
) -> Path | None:
    session_dir = _claude_project_session_dir(repo_root)
    if not session_dir.is_dir():
        return None

    candidates: list[tuple[int, Path]] = []
    for path in session_dir.glob("*.jsonl"):
        try:
            mtime_ns = path.stat().st_mtime_ns
        except FileNotFoundError:
            continue
        previous_mtime_ns = session_log_snapshot.get(path)
        if previous_mtime_ns is None or mtime_ns > previous_mtime_ns:
            candidates.append((mtime_ns, path))

    for _, path in sorted(candidates, reverse=True):
        if _session_log_matches_prompt(path, prompt):
            return path
    return None


def _load_claude_session_log_usage(
    session_log: Path,
    request_usage_entries: list[dict[str, object]],
    request_usage_index: dict[str, int],
) -> None:
    paths = [session_log]
    sidechain_dir = session_log.with_suffix("")
    if sidechain_dir.is_dir():
        paths.extend(sorted(sidechain_dir.rglob("*.jsonl")))

    for path in paths:
        try:
            with path.open(encoding="utf-8") as handle:
                for line in handle:
                    try:
                        event = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    _record_claude_usage_entry(
                        request_usage_entries,
                        request_usage_index,
                        event,
                        source="session-log",
                    )
        except OSError:
            continue


def _codex_sessions_root() -> Path:
    return Path(os.path.expanduser("~")) / ".codex" / "sessions"


def _snapshot_codex_session_logs() -> dict[Path, int]:
    sessions_root = _codex_sessions_root()
    if not sessions_root.is_dir():
        return {}
    snapshot: dict[Path, int] = {}
    for path in sessions_root.rglob("*.jsonl"):
        try:
            snapshot[path] = path.stat().st_mtime_ns
        except FileNotFoundError:
            continue
    return snapshot


def _extract_codex_session_id(output: str) -> str | None:
    match = CODEX_SESSION_ID_RE.search(output)
    if match is None:
        return None
    return match.group(1)


def _find_codex_session_log_by_id(session_id: str) -> Path | None:
    sessions_root = _codex_sessions_root()
    if not sessions_root.is_dir():
        return None
    for path in sessions_root.rglob(f"*{session_id}.jsonl"):
        return path
    return None


def _codex_session_log_matches_prompt(session_log: Path, prompt: str) -> bool:
    try:
        with session_log.open(encoding="utf-8") as handle:
            for _ in range(16):
                line = handle.readline()
                if not line:
                    return False
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if not isinstance(event, dict):
                    continue
                event_type = event.get("type")
                payload = event.get("payload")
                if not isinstance(payload, dict):
                    continue

                if event_type == "event_msg" and payload.get("type") == "user_message":
                    if payload.get("message") == prompt:
                        return True

                if event_type != "response_item":
                    continue
                if payload.get("type") != "message" or payload.get("role") != "user":
                    continue
                content = payload.get("content")
                if not isinstance(content, list):
                    continue
                for item in content:
                    if not isinstance(item, dict):
                        continue
                    if item.get("type") == "input_text" and item.get("text") == prompt:
                        return True
    except OSError:
        return False
    return False


def _find_matching_codex_session_log(
    *,
    prompt: str,
    session_log_snapshot: dict[Path, int],
    session_id: str | None,
) -> Path | None:
    if isinstance(session_id, str) and session_id:
        session_log = _find_codex_session_log_by_id(session_id)
        if session_log is not None:
            return session_log

    sessions_root = _codex_sessions_root()
    if not sessions_root.is_dir():
        return None

    candidates: list[tuple[int, Path]] = []
    for path in sessions_root.rglob("*.jsonl"):
        try:
            mtime_ns = path.stat().st_mtime_ns
        except FileNotFoundError:
            continue
        previous_mtime_ns = session_log_snapshot.get(path)
        if previous_mtime_ns is None or mtime_ns > previous_mtime_ns:
            candidates.append((mtime_ns, path))

    for _, path in sorted(candidates, reverse=True):
        if _codex_session_log_matches_prompt(path, prompt):
            return path
    return None


def _normalize_codex_usage(usage: object) -> dict[str, int] | None:
    if not isinstance(usage, dict):
        return None
    return {
        field: _coerce_usage_int(usage.get(field))
        for field in CODEX_TOKEN_FIELDS
    }


def _codex_reasoning_effort(turn_context: dict[str, object] | None) -> str | None:
    if not isinstance(turn_context, dict):
        return None

    effort = turn_context.get("effort")
    if isinstance(effort, str) and effort.strip():
        return effort.strip().lower()

    collaboration_mode = turn_context.get("collaboration_mode")
    if not isinstance(collaboration_mode, dict):
        return None
    settings = collaboration_mode.get("settings")
    if not isinstance(settings, dict):
        return None
    effort = settings.get("reasoning_effort")
    if isinstance(effort, str) and effort.strip():
        return effort.strip().lower()
    return None


def load_codex_session_log_telemetry(session_log: Path) -> dict[str, object] | None:
    session_meta: dict[str, object] | None = None
    turn_context: dict[str, object] | None = None
    task_started: dict[str, object] | None = None
    task_complete: dict[str, object] | None = None
    last_token_payload: dict[str, object] | None = None
    token_count_events = 0

    try:
        with session_log.open(encoding="utf-8") as handle:
            for line in handle:
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if not isinstance(event, dict):
                    continue

                event_type = event.get("type")
                payload = event.get("payload")
                if event_type == "session_meta" and isinstance(payload, dict):
                    session_meta = payload
                    continue
                if event_type == "turn_context" and isinstance(payload, dict):
                    turn_context = payload
                    continue
                if event_type != "event_msg" or not isinstance(payload, dict):
                    continue

                payload_type = payload.get("type")
                if payload_type == "task_started":
                    task_started = payload
                    continue
                if payload_type == "task_complete":
                    task_complete = payload
                    continue
                if payload_type != "token_count":
                    continue
                info = payload.get("info")
                if not isinstance(info, dict):
                    continue
                last_token_payload = payload
                token_count_events += 1
    except OSError:
        return None

    if last_token_payload is None:
        return None

    info = last_token_payload.get("info")
    assert isinstance(info, dict)
    totals = _normalize_codex_usage(info.get("total_token_usage"))
    last_usage = _normalize_codex_usage(info.get("last_token_usage"))
    if totals is None:
        return None

    return {
        "provider": "codex",
        "source": "session-log",
        "session_id": session_meta.get("id") if isinstance(session_meta, dict) else None,
        "session_path": str(session_log),
        "timestamp": session_meta.get("timestamp") if isinstance(session_meta, dict) else None,
        "cwd": session_meta.get("cwd") if isinstance(session_meta, dict) else None,
        "originator": session_meta.get("originator") if isinstance(session_meta, dict) else None,
        "cli_version": session_meta.get("cli_version") if isinstance(session_meta, dict) else None,
        "model_provider": session_meta.get("model_provider") if isinstance(session_meta, dict) else None,
        "model": turn_context.get("model") if isinstance(turn_context, dict) else None,
        "reasoning_effort": _codex_reasoning_effort(turn_context),
        "turn_id": (
            task_complete.get("turn_id")
            if isinstance(task_complete, dict) and isinstance(task_complete.get("turn_id"), str)
            else task_started.get("turn_id")
            if isinstance(task_started, dict)
            else None
        ),
        "task_complete_message": task_complete.get("last_agent_message") if isinstance(task_complete, dict) else None,
        "model_context_window": info.get("model_context_window"),
        "totals": totals,
        "last_usage": last_usage,
        "token_count_events": token_count_events,
        "rate_limits": last_token_payload.get("rate_limits"),
    }


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


def _stream_claude_json_pipe(
    pipe,
    sink,
    chunks: list[str],
    request_usage_entries: list[dict[str, object]],
    request_usage_index: dict[str, int],
) -> None:
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
            message = event.get("message")
            _record_claude_usage_entry(
                request_usage_entries,
                request_usage_index,
                event,
                source="stream-json",
            )

            emitted = ""
            if event_type in {"assistant", "user"}:
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
    runner_prompt = prompt
    claude_request_usage_entries: list[dict[str, object]] = []
    claude_request_usage_index: dict[str, int] = {}
    claude_session_log_snapshot = _snapshot_claude_session_logs(repo_root) if runner == "claude-code" else {}
    codex_session_log_snapshot = _snapshot_codex_session_logs() if runner == "codex" else {}

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
        runner_prompt = f"{REVIEW_RUNNER_SYSTEM_PROMPT}\n\n{prompt}"
        cmd.append(runner_prompt)
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
        args=(
            (process.stdout, sys.stdout, stdout_chunks, claude_request_usage_entries, claude_request_usage_index)
            if runner == "claude-code"
            else (process.stdout, sys.stdout, stdout_chunks)
        ),
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

    if runner == "claude-code":
        session_log = _find_matching_claude_session_log(
            repo_root=repo_root,
            prompt=prompt,
            session_log_snapshot=claude_session_log_snapshot,
        )
        if session_log is not None:
            _load_claude_session_log_usage(
                session_log,
                claude_request_usage_entries,
                claude_request_usage_index,
            )

    codex_telemetry = None
    if runner == "codex":
        session_log = _find_matching_codex_session_log(
            prompt=runner_prompt,
            session_log_snapshot=codex_session_log_snapshot,
            session_id=_extract_codex_session_id("".join(stdout_chunks)),
        )
        if session_log is not None:
            codex_telemetry = load_codex_session_log_telemetry(session_log)

    return RunnerResult(
        stdout="".join(stdout_chunks),
        stderr="".join(stderr_chunks),
        returncode=returncode,
        telemetry=(
            _build_claude_telemetry(claude_request_usage_entries)
            if runner == "claude-code"
            else codex_telemetry
        ),
    )
