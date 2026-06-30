"""Runner adapters: each supported harness CLI behind one interface.

Adding a harness means writing one adapter module (build_command, optional
stream decoding, telemetry collection) and registering its class here; the
CLIs derive their --runner choices from this registry.
"""

from __future__ import annotations

import subprocess
import sys
import threading
from pathlib import Path

from commonplace.review.runners.base import RunnerAdapter, RunnerResult, stream_pipe
from commonplace.review.runners.claude_code import ClaudeCodeRunner
from commonplace.review.runners.codex import CodexRunner


RUNNER_ADAPTERS: dict[str, type[RunnerAdapter]] = {
    adapter.name: adapter for adapter in (ClaudeCodeRunner, CodexRunner)
}


def runner_names() -> list[str]:
    return sorted(RUNNER_ADAPTERS)


def get_runner(name: str) -> RunnerAdapter:
    """Instantiate a fresh adapter for one invocation."""
    adapter_cls = RUNNER_ADAPTERS.get(name)
    if adapter_cls is None:
        raise ValueError(f"unsupported runner: {name}")
    return adapter_cls()


def run_prompt(
    *,
    runner: str,
    prompt: str,
    repo_root: Path,
    model: str | None = None,
    effort: str | None = None,
) -> RunnerResult:
    adapter = get_runner(runner)
    if effort is not None and not adapter.supports_effort:
        raise ValueError(f"runner {runner!r} does not support reasoning effort")
    session_log_snapshot = adapter.snapshot_session_logs(repo_root)
    cmd, sent_prompt = adapter.build_command(prompt=prompt, repo_root=repo_root, model=model, effort=effort)

    process = subprocess.Popen(
        cmd,
        cwd=repo_root,
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
        target=adapter.stream_stdout,
        args=(process.stdout, sys.stdout, stdout_chunks),
        daemon=True,
    )
    stderr_thread = threading.Thread(
        target=stream_pipe,
        args=(process.stderr, sys.stderr, stderr_chunks),
        daemon=True,
    )
    stdout_thread.start()
    stderr_thread.start()
    returncode = process.wait()
    stdout_thread.join()
    stderr_thread.join()

    stdout = "".join(stdout_chunks)
    return RunnerResult(
        stdout=stdout,
        stderr="".join(stderr_chunks),
        returncode=returncode,
        telemetry=adapter.collect_telemetry(
            repo_root=repo_root,
            sent_prompt=sent_prompt,
            stdout=stdout,
            session_log_snapshot=session_log_snapshot,
        ),
    )
