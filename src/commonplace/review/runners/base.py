"""Runner adapter interface and shared streaming helpers.

A runner adapter wraps one harness CLI (claude, codex, ...) behind a uniform
surface: build the command, decode its stdout stream, and collect best-effort
telemetry afterwards. Adapters are instantiated per invocation so streaming
state collected during the run is available to telemetry collection.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar


@dataclass(frozen=True)
class RunnerResult:
    stdout: str
    stderr: str
    returncode: int
    telemetry: dict[str, object] | None = None


def stream_pipe(pipe, sink, chunks: list[str]) -> None:
    try:
        for line in iter(pipe.readline, ""):
            chunks.append(line)
            sink.write(line)
            sink.flush()
    finally:
        pipe.close()


def coerce_usage_int(value: object) -> int:
    return value if isinstance(value, int) and not isinstance(value, bool) else 0


class RunnerAdapter(ABC):
    """One harness CLI behind the generic run_prompt driver.

    Telemetry is best-effort by design: it is scraped from vendor session
    logs whose formats are undocumented, so collect_telemetry returning None
    must never fail a review run.
    """

    name: ClassVar[str]

    @abstractmethod
    def snapshot_session_logs(self, repo_root: Path) -> dict[Path, int]:
        """Snapshot session-log mtimes before the run, to find the new log after."""

    @abstractmethod
    def build_command(self, *, prompt: str, repo_root: Path, model: str | None) -> tuple[list[str], str]:
        """Return (argv, sent_prompt) — sent_prompt is the prompt text the
        harness actually receives (some adapters prepend the system prompt)."""

    def stream_stdout(self, pipe, sink, chunks: list[str]) -> None:
        """Decode the process stdout stream; default is raw passthrough."""
        stream_pipe(pipe, sink, chunks)

    @abstractmethod
    def collect_telemetry(
        self,
        *,
        repo_root: Path,
        sent_prompt: str,
        stdout: str,
        session_log_snapshot: dict[Path, int],
    ) -> dict[str, object] | None:
        """Assemble telemetry after the run completes; None when unavailable."""
