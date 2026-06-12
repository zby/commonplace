"""claude-code runner adapter: stream-json decoding and session-log telemetry."""

from __future__ import annotations

import json
import os
from pathlib import Path

from commonplace.review.protocol.prompt import REVIEW_RUNNER_SYSTEM_PROMPT
from commonplace.review.runners.base import RunnerAdapter, coerce_usage_int


CLAUDE_TOKEN_FIELDS = (
    "input_tokens",
    "cache_creation_input_tokens",
    "cache_read_input_tokens",
    "output_tokens",
)


def _usage_totals_from_requests(requests: list[dict[str, object]]) -> dict[str, int]:
    totals = {
        field: sum(
            coerce_usage_int((request.get("usage") or {}).get(field))
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


def _is_usable_claude_model(value: object) -> bool:
    return isinstance(value, str) and bool(value) and not value.startswith("<")


def build_claude_telemetry(
    requests: list[dict[str, object]],
    *,
    init_model: str | None = None,
) -> dict[str, object] | None:
    usable_init_model = init_model if _is_usable_claude_model(init_model) else None
    if not requests and usable_init_model is None:
        return None

    totals = _usage_totals_from_requests(requests)
    totals["request_count"] = len(requests)
    first_request = _first_request_summary(requests[0]) if requests else None
    followup_requests = requests[1:]
    followup_totals = _usage_totals_from_requests(followup_requests)
    followup_totals["request_count"] = len(followup_requests)
    models = [
        model
        for model in dict.fromkeys(
            request.get("model")
            for request in requests
            if _is_usable_claude_model(request.get("model"))
        )
    ]
    if not models and usable_init_model is not None:
        models = [usable_init_model]
    return {
        "provider": "claude-code",
        "model": models[0] if len(models) == 1 else None,
        "models": models,
        "init_model": usable_init_model,
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


def record_claude_usage_entry(
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


def snapshot_claude_session_logs(repo_root: Path) -> dict[Path, int]:
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


def find_matching_claude_session_log(
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


def load_claude_session_log_usage(
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
                    record_claude_usage_entry(
                        request_usage_entries,
                        request_usage_index,
                        event,
                        source="session-log",
                    )
        except OSError:
            continue


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


def stream_claude_json_pipe(
    pipe,
    sink,
    chunks: list[str],
    request_usage_entries: list[dict[str, object]],
    request_usage_index: dict[str, int],
    init_state: dict[str, str],
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
            record_claude_usage_entry(
                request_usage_entries,
                request_usage_index,
                event,
                source="stream-json",
            )

            emitted = ""
            if event_type == "system" and event.get("subtype") == "init":
                model = event.get("model")
                if _is_usable_claude_model(model):
                    init_state["model"] = model
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


class ClaudeCodeRunner(RunnerAdapter):
    name = "claude-code"

    def __init__(self) -> None:
        self._usage_entries: list[dict[str, object]] = []
        self._usage_index: dict[str, int] = {}
        self._init_state: dict[str, str] = {}

    def snapshot_session_logs(self, repo_root: Path) -> dict[Path, int]:
        return snapshot_claude_session_logs(repo_root)

    def build_command(self, *, prompt: str, repo_root: Path, model: str | None) -> tuple[list[str], str]:
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
        return cmd, prompt

    def stream_stdout(self, pipe, sink, chunks: list[str]) -> None:
        stream_claude_json_pipe(
            pipe,
            sink,
            chunks,
            self._usage_entries,
            self._usage_index,
            self._init_state,
        )

    def collect_telemetry(
        self,
        *,
        repo_root: Path,
        sent_prompt: str,
        stdout: str,
        session_log_snapshot: dict[Path, int],
    ) -> dict[str, object] | None:
        session_log = find_matching_claude_session_log(
            repo_root=repo_root,
            prompt=sent_prompt,
            session_log_snapshot=session_log_snapshot,
        )
        if session_log is not None:
            load_claude_session_log_usage(session_log, self._usage_entries, self._usage_index)
        return build_claude_telemetry(self._usage_entries, init_model=self._init_state.get("model"))
