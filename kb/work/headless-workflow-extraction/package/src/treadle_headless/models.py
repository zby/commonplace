"""Immutable, plain request and result values."""

from __future__ import annotations

import math
import re
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path
from types import MappingProxyType

FAILURE_STATUSES = frozenset(
    {
        "incomplete",
        "worker_problem",
        "usage_limit",
        "process_error",
        "timeout",
        "launch_error",
        "interrupted",
        "protocol_error",
    }
)
RETRYABLE_STATUSES = FAILURE_STATUSES - {"usage_limit", "protocol_error"}
_SAFE_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")
_RESERVED_NAMES = frozenset(
    {"prompt.txt", "problem.json", "evidence.json", "stdout.log", "stderr.log", "inputs", "outputs"}
)
_PATH_TOKENS = (
    {"prompt", "input_dir", "output_dir", "problem_file", "evidence_file", "launch_dir", "workdir"}
)
_PATH_TOKEN_RE = re.compile(r"\{(" + "|".join(_PATH_TOKENS) + r")\}")


def _safe_name(value: str) -> str:
    if not isinstance(value, str) or not _SAFE_NAME.fullmatch(value) or value in {".", ".."}:
        raise ValueError(f"unsafe file name: {value!r}")
    if value in _RESERVED_NAMES:
        raise ValueError(f"reserved file name: {value!r}")
    return value


def _freeze_json(value: object) -> object:
    if isinstance(value, Mapping):
        return MappingProxyType({key: _freeze_json(item) for key, item in value.items()})
    if isinstance(value, (list, tuple)):
        return tuple(_freeze_json(item) for item in value)
    return value


def _positive_number(value: float | int, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a positive finite number")
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be a positive finite number")
    return value


@dataclass(frozen=True)
class RetryPolicy:
    """Execution outcomes eligible for automatic relaunch, with fixed delay."""

    on: tuple[str, ...] = ()
    backoff_seconds: float = 0.0

    def __post_init__(self) -> None:
        statuses = tuple(self.on)
        if len(statuses) != len(set(statuses)) or not set(statuses) <= RETRYABLE_STATUSES:
            raise ValueError("retry statuses must be unique eligible execution failures")
        if isinstance(self.backoff_seconds, bool) or not isinstance(
            self.backoff_seconds, (int, float)
        ):
            raise ValueError("backoff_seconds must be a nonnegative finite number")
        if not math.isfinite(self.backoff_seconds) or self.backoff_seconds < 0:
            raise ValueError("backoff_seconds must be a nonnegative finite number")
        object.__setattr__(self, "on", statuses)
        object.__setattr__(self, "backoff_seconds", float(self.backoff_seconds))


@dataclass(frozen=True)
class CommandWorker:
    """A command template with path placeholders substituted per launch.

    Supported placeholders are prompt, input_dir, output_dir, problem_file,
    evidence_file, launch_dir, and workdir. The process runs in workdir.
    """

    argv: tuple[str, ...]
    name: str = "command"
    env: Mapping[str, str] = field(default_factory=dict)
    evidence_file: str | None = None

    def __post_init__(self) -> None:
        argv = tuple(self.argv)
        if not argv or not all(isinstance(x, str) and x for x in argv):
            raise ValueError("argv must contain nonempty strings")
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("worker name must be nonempty")
        env = dict(self.env)
        if not all(isinstance(k, str) and isinstance(v, str) for k, v in env.items()):
            raise ValueError("environment overrides must be strings")
        if self.evidence_file is not None:
            if (
                not isinstance(self.evidence_file, str)
                or not _SAFE_NAME.fullmatch(self.evidence_file)
                or self.evidence_file
                in {"inputs", "outputs", "prompt.txt", "problem.json", "stdout.log", "stderr.log"}
            ):
                raise ValueError("unsafe evidence file name")
        object.__setattr__(self, "argv", argv)
        object.__setattr__(self, "env", MappingProxyType(env))

    def command(self, paths: Mapping[str, Path]) -> tuple[str, ...]:
        """Render a subprocess command without invoking it."""
        return tuple(_replace_tokens(arg, paths) for arg in self.argv)


def _replace_tokens(arg: str, paths: Mapping[str, Path]) -> str:
    # Only these exact tokens are special. Literal JSON and shell/code braces survive.
    return _PATH_TOKEN_RE.sub(lambda match: str(paths[match.group(1)]), arg)


@dataclass(frozen=True)
class Request:
    call_id: str
    task: str
    inputs: Mapping[str, str]
    required_outputs: tuple[str, ...]
    worker: CommandWorker
    optional_outputs: tuple[str, ...] = ()
    timeout_seconds: float = 300.0
    max_launches: int = 1
    retry: RetryPolicy = field(default_factory=RetryPolicy)

    def __post_init__(self) -> None:
        if not isinstance(self.call_id, str) or not self.call_id or "\x00" in self.call_id:
            raise ValueError("call_id must be a nonempty string")
        if not isinstance(self.task, str) or not self.task:
            raise ValueError("task must be nonempty text")
        inputs = dict(self.inputs)
        if not all(isinstance(v, str) for v in inputs.values()):
            raise ValueError("input contents must be text")
        for name in inputs:
            _safe_name(name)
        required = tuple(self.required_outputs)
        optional = tuple(self.optional_outputs)
        for name in required + optional:
            _safe_name(name)
        if not required or len(set(required + optional)) != len(required + optional):
            raise ValueError("outputs must include a required name and have no duplicates")
        if not isinstance(self.worker, CommandWorker):
            raise ValueError("worker must be a CommandWorker")
        if (
            isinstance(self.max_launches, bool)
            or not isinstance(self.max_launches, int)
            or self.max_launches < 1
        ):
            raise ValueError("max_launches must be a positive integer")
        if not isinstance(self.retry, RetryPolicy):
            raise ValueError("retry must be a RetryPolicy")
        object.__setattr__(
            self, "timeout_seconds", _positive_number(self.timeout_seconds, "timeout_seconds")
        )
        object.__setattr__(self, "inputs", MappingProxyType(inputs))
        object.__setattr__(self, "required_outputs", required)
        object.__setattr__(self, "optional_outputs", optional)


@dataclass(frozen=True)
class Attempt:
    launch_id: str
    status: str
    launch_dir: str
    argv: tuple[str, ...] | None = None
    pid: int | None = None
    returncode: int | None = None
    started_at: str | None = None
    finished_at: str | None = None
    problem: Mapping[str, str] | None = None
    evidence: Mapping[str, object] | None = None
    missing_outputs: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.argv is not None:
            object.__setattr__(self, "argv", tuple(self.argv))
        if self.problem is not None:
            object.__setattr__(self, "problem", _freeze_json(self.problem))
        if self.evidence is not None:
            object.__setattr__(self, "evidence", _freeze_json(self.evidence))
        object.__setattr__(self, "missing_outputs", tuple(self.missing_outputs))


@dataclass(frozen=True)
class CallResult:
    call_id: str
    request_hash: str
    status: str
    outputs: Mapping[str, str]
    attempts: tuple[Attempt, ...]
    exhausted: bool
    reused: bool = False

    def __post_init__(self) -> None:
        object.__setattr__(self, "outputs", MappingProxyType(dict(self.outputs)))
        object.__setattr__(self, "attempts", tuple(self.attempts))
