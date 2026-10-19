"""Version-scoped command templates and evidence extraction for headless CLIs.

Factories only construct subprocess commands. They do not authenticate, launch
models, or claim that a requested model was the one served.
"""

from __future__ import annotations

import json
from typing import Literal

from .models import CommandWorker


def _required_text(value: str, name: str) -> str:
    if not isinstance(value, str) or not value or any(char in value for char in "\x00{}\r\n"):
        raise ValueError(f"{name} must be nonempty text without control or template characters")
    return value


def _tool_list(tools: tuple[str, ...]) -> str:
    if not tools or not all(
        isinstance(tool, str) and tool and not any(char in tool for char in ",\x00{}\r\n")
        for tool in tools
    ):
        raise ValueError("tools must be a nonempty tuple of names without commas")
    return ",".join(tools)


_PROMPT_POINTER = "Read the complete task and file paths in `{prompt}`, then perform that task."


def codex_worker(
    model: str,
    *,
    sandbox: Literal["read-only", "workspace-write", "danger-full-access"],
    effort: str | None = None,
) -> CommandWorker:
    """Construct a Codex 0.162.1 noninteractive worker.

    The caller chooses the sandbox. ``approval_policy=never`` denies requests
    that require interactive approval; it does not replace host isolation.
    """
    _required_text(model, "model")
    if sandbox not in {"read-only", "workspace-write", "danger-full-access"}:
        raise ValueError("unsupported Codex sandbox")
    argv = [
        "codex",
        "exec",
        "--json",
        "--skip-git-repo-check",
        "-C",
        "{workdir}",
        "-m",
        model,
        "-s",
        sandbox,
        "-c",
        "approval_policy=never",
    ]
    if effort is not None:
        _required_text(effort, "effort")
        argv.extend(("-c", f"model_reasoning_effort={effort}"))
    argv.append(_PROMPT_POINTER)
    return CommandWorker(argv=tuple(argv), name="codex")


def claude_worker(
    model: str,
    *,
    allowed_tools: tuple[str, ...],
    permission_mode: Literal["dontAsk", "acceptEdits"] = "dontAsk",
) -> CommandWorker:
    """Construct a Claude Code 2.1.303 one-shot worker.

    The caller selects an explicit tool allowlist. Unanswered permission
    requests are denied; normal settings and instruction loading remain active.
    """
    _required_text(model, "model")
    if permission_mode not in {"dontAsk", "acceptEdits"}:
        raise ValueError("unsupported Claude permission mode")
    tools = _tool_list(allowed_tools)
    return CommandWorker(
        argv=(
            "claude",
            "-p",
            "--output-format",
            "stream-json",
            "--verbose",
            "--model",
            model,
            "--permission-mode",
            permission_mode,
            "--permission-prompts",
            "none",
            f"--allowedTools={tools}",
            _PROMPT_POINTER,
        ),
        name="claude",
    )


def pi_worker(
    model: str,
    *,
    provider: str,
    tools: tuple[str, ...],
    project_trust: Literal["approve", "no-approve"],
) -> CommandWorker:
    """Construct a Pi 1.3.0 one-shot worker.

    Project trust only controls project resource loading. Pi has no built-in
    sandbox or per-tool approval; the caller supplies process isolation.
    """
    _required_text(model, "model")
    _required_text(provider, "provider")
    if project_trust not in {"approve", "no-approve"}:
        raise ValueError("project_trust must be approve or no-approve")
    return CommandWorker(
        argv=(
            "pi",
            "--mode",
            "json",
            "--provider",
            provider,
            "--model",
            model,
            "--tools",
            _tool_list(tools),
            f"--{project_trust}",
            "--session-dir",
            "{launch_dir}",
            _PROMPT_POINTER,
        ),
        name="pi",
    )


def parse_evidence(harness: Literal["codex", "claude", "pi"], stdout: str) -> dict[str, object]:
    """Extract documented fields from retained JSONL without guessing identity.

    Raw stdout remains authoritative evidence. Parsing a partial stream yields
    only fields actually present; callers retain parse_errors for diagnosis.
    """
    if harness not in {"codex", "claude", "pi"}:
        raise ValueError("unknown harness")
    records: list[dict[str, object]] = []
    parse_errors = 0
    # JSONL is LF-delimited. Unicode paragraph separators can occur in strings.
    for line in stdout.split("\n"):
        line = line.removesuffix("\r")
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError:
            parse_errors += 1
            continue
        if isinstance(value, dict):
            records.append(value)
        else:
            parse_errors += 1

    evidence: dict[str, object] = {
        "harness": harness,
        "records": len(records),
        "parse_errors": parse_errors,
    }
    if harness == "codex":
        error_events = 0
        for record in records:
            if record.get("type") == "thread.started" and isinstance(record.get("thread_id"), str):
                evidence["session_id"] = record["thread_id"]
            if record.get("type") in {"turn.completed", "turn.failed"}:
                evidence["turn_outcome"] = record["type"]
            if record.get("type") == "error":
                error_events += 1
        if error_events:
            evidence["error_event_count"] = error_events
        return evidence

    if harness == "claude":
        retry_errors: list[str] = []
        for record in records:
            if record.get("type") == "system" and record.get("subtype") == "api_retry":
                if isinstance(record.get("error"), str):
                    retry_errors.append(record["error"])
            if record.get("type") == "assistant":
                message = record.get("message")
                if isinstance(message, dict) and isinstance(message.get("model"), str):
                    evidence["reported_model"] = message["model"]
            if record.get("type") == "result":
                evidence["last_result_subtype"] = record.get("subtype")
                if isinstance(record.get("session_id"), str):
                    evidence["session_id"] = record["session_id"]
                if isinstance(record.get("is_error"), bool):
                    evidence["is_error"] = record["is_error"]
        if retry_errors:
            evidence["retry_error_categories"] = retry_errors
        return evidence

    for record in records:
        if record.get("type") == "session" and isinstance(record.get("id"), str):
            evidence["session_id"] = record["id"]
        if record.get("type") == "message_end":
            message = record.get("message")
            if isinstance(message, dict) and message.get("role") == "assistant":
                for source, target in (
                    ("provider", "provider"),
                    ("model", "reported_model"),
                    ("responseModel", "served_model"),
                    ("responseId", "response_id"),
                    ("stopReason", "stop_reason"),
                    ("errorMessage", "error_message"),
                ):
                    if isinstance(message.get(source), str):
                        evidence[target] = message[source]
        if record.get("type") == "agent_settled" and isinstance(record.get("aborted"), bool):
            evidence["settled_aborted"] = record["aborted"]
    return evidence
