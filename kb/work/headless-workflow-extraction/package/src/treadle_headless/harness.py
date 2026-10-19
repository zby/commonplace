"""Per-launch file protocol and local process ownership."""

from __future__ import annotations

import json
import os
import signal
import subprocess
import time
from collections.abc import Callable, Mapping
from contextlib import ExitStack
from dataclasses import replace
from datetime import UTC, datetime
from pathlib import Path

from .models import Attempt, Request


def _now() -> str:
    return datetime.now(UTC).isoformat()


def prepare(
    request: Request, launch_dir: Path, workdir: Path
) -> tuple[Mapping[str, Path], tuple[str, ...]]:
    """Write fresh inputs and a human-readable task frame before reservation."""
    input_dir = launch_dir / "inputs"
    output_dir = launch_dir / "outputs"
    input_dir.mkdir()
    output_dir.mkdir()
    for name, content in request.inputs.items():
        (input_dir / name).write_text(content, encoding="utf-8")
    prompt = launch_dir / "prompt.txt"
    lines = ["Task:", request.task, "", "Inputs (read these exact files):"]
    lines.extend(f"- {name}: {input_dir / name}" for name in sorted(request.inputs))
    lines.extend(["", "Required outputs (write these exact files):"])
    lines.extend(f"- {name}: {output_dir / name}" for name in request.required_outputs)
    if request.optional_outputs:
        lines.extend(["", "Optional outputs:"])
        lines.extend(f"- {name}: {output_dir / name}" for name in request.optional_outputs)
    lines.extend(
        [
            "",
            "If unable to finish, write a JSON object to this problem file:",
            str(launch_dir / "problem.json"),
            'Use {"kind":"unable","message":"..."} or {"kind":"usage_limit","message":"..."}.',
        ]
    )
    prompt.write_text("\n".join(lines) + "\n", encoding="utf-8")
    paths = {
        "prompt": prompt,
        "input_dir": input_dir,
        "output_dir": output_dir,
        "problem_file": launch_dir / "problem.json",
        "evidence_file": launch_dir / (request.worker.evidence_file or "evidence.json"),
        "launch_dir": launch_dir,
        "workdir": workdir,
    }
    return paths, request.worker.command(paths)


def _group_exists(pgid: int) -> bool:
    try:
        os.killpg(pgid, 0)
    except ProcessLookupError:
        return False
    return True


def _cleanup_group(pgid: int) -> bool:
    """Terminate descendants even if the leader has already exited."""
    if not _group_exists(pgid):
        return False
    try:
        os.killpg(pgid, signal.SIGTERM)
    except ProcessLookupError:
        return False
    deadline = time.monotonic() + 0.25
    while time.monotonic() < deadline:
        if not _group_exists(pgid):
            return True
        time.sleep(0.01)
    try:
        os.killpg(pgid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    return True


def _read_problem(path: Path) -> tuple[dict[str, str] | None, bool]:
    if path.is_symlink():
        return None, True
    if not path.exists():
        return None, False
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return None, True
    if (
        not isinstance(value, dict)
        or value.get("kind") not in {"unable", "usage_limit"}
        or not isinstance(value.get("message"), str)
    ):
        return None, True
    return {"kind": value["kind"], "message": value["message"]}, False


def _read_evidence(path: Path) -> Mapping[str, object] | None:
    if not path.exists() or path.is_symlink():
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def launch(
    request: Request,
    workdir: Path,
    paths: Mapping[str, Path],
    argv: tuple[str, ...],
    reserved: Attempt,
    on_started: Callable[[int, tuple[str, ...], str], None],
) -> tuple[Attempt, dict[str, str]]:
    """Invoke once, terminate its process group, then collect only its outputs."""
    started_at = _now()
    stdout_path = Path(reserved.launch_dir) / "stdout.log"
    stderr_path = Path(reserved.launch_dir) / "stderr.log"
    env = os.environ.copy()
    env.update(request.worker.env)

    def launch_error(error: OSError) -> tuple[Attempt, dict[str, str]]:
        return (
            replace(
                reserved,
                status="launch_error",
                argv=argv,
                started_at=started_at,
                finished_at=_now(),
                problem={"kind": "launch_error", "message": str(error)},
            ),
            {},
        )

    files = ExitStack()
    try:
        stdout = files.enter_context(stdout_path.open("wb"))
        stderr = files.enter_context(stderr_path.open("wb"))
    except OSError as error:
        files.close()
        return launch_error(error)
    try:
        try:
            process = subprocess.Popen(
                argv,
                cwd=workdir,
                env=env,
                stdin=subprocess.DEVNULL,
                stdout=stdout,
                stderr=stderr,
                start_new_session=True,
            )
        except OSError as error:
            return launch_error(error)
        timed_out = False
        group_lingered = False
        try:
            on_started(process.pid, argv, started_at)
            process.wait(timeout=request.timeout_seconds)
        except subprocess.TimeoutExpired:
            timed_out = True
        finally:
            group_lingered = _cleanup_group(process.pid)
            if process.poll() is None:
                process.wait(timeout=1)
    finally:
        files.close()

    status = "delivered"
    problem, invalid_problem = _read_problem(paths["problem_file"])
    evidence = _read_evidence(paths["evidence_file"])
    outputs: dict[str, str] = {}
    missing: list[str] = []
    if timed_out:
        status = "timeout"
    elif group_lingered:
        status = "process_error"
    elif invalid_problem:
        status = "protocol_error"
    elif problem is not None:
        status = "usage_limit" if problem["kind"] == "usage_limit" else "worker_problem"
    elif process.returncode != 0:
        status = "process_error"
    else:
        if paths["output_dir"].is_symlink():
            status = "protocol_error"
        for name in request.required_outputs + request.optional_outputs:
            if status != "delivered":
                break
            path = paths["output_dir"] / name
            if path.is_symlink():
                status = "protocol_error"
                break
            if not path.is_file():
                if name in request.required_outputs:
                    missing.append(name)
                continue
            try:
                outputs[name] = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                status = "protocol_error"
                break
        if status == "delivered" and missing:
            status = "incomplete"
    if status != "delivered":
        outputs = {}
    return (
        replace(
            reserved,
            status=status,
            argv=argv,
            pid=process.pid,
            returncode=process.returncode,
            started_at=started_at,
            finished_at=_now(),
            problem=problem,
            evidence=evidence,
            missing_outputs=tuple(missing),
        ),
        outputs,
    )
