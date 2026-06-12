"""codex runner adapter: session-id matching and session-log telemetry."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path

from commonplace.review.protocol.prompt import REVIEW_RUNNER_SYSTEM_PROMPT
from commonplace.review.runners.base import RunnerAdapter, coerce_usage_int


CODEX_TOKEN_FIELDS = (
    "input_tokens",
    "cached_input_tokens",
    "output_tokens",
    "reasoning_output_tokens",
    "total_tokens",
)

CODEX_SESSION_ID_RE = re.compile(r"(?m)^session id:\s*(\S+)\s*$")


def _codex_sessions_root() -> Path:
    return Path(os.path.expanduser("~")) / ".codex" / "sessions"


def snapshot_codex_session_logs() -> dict[Path, int]:
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


def extract_codex_session_id(output: str) -> str | None:
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


def find_matching_codex_session_log(
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
        field: coerce_usage_int(usage.get(field))
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


class CodexRunner(RunnerAdapter):
    name = "codex"

    def snapshot_session_logs(self, repo_root: Path) -> dict[Path, int]:
        return snapshot_codex_session_logs()

    def build_command(self, *, prompt: str, repo_root: Path, model: str | None) -> tuple[list[str], str]:
        cmd = ["codex", "exec", "--full-auto", "-C", str(repo_root)]
        if model:
            cmd.extend(["--model", model])
        sent_prompt = f"{REVIEW_RUNNER_SYSTEM_PROMPT}\n\n{prompt}"
        cmd.append(sent_prompt)
        return cmd, sent_prompt

    def collect_telemetry(
        self,
        *,
        repo_root: Path,
        sent_prompt: str,
        stdout: str,
        session_log_snapshot: dict[Path, int],
    ) -> dict[str, object] | None:
        session_log = find_matching_codex_session_log(
            prompt=sent_prompt,
            session_log_snapshot=session_log_snapshot,
            session_id=extract_codex_session_id(stdout),
        )
        if session_log is None:
            return None
        return load_codex_session_log_telemetry(session_log)
