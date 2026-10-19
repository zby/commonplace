"""Durability and process ownership cases at the local subprocess boundary."""

from __future__ import annotations

import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

import pytest

from treadle_headless import (
    CommandWorker,
    RecordError,
    Request,
    RetryPolicy,
    Run,
    RunBusyError,
    UncertainLaunchError,
)

SRC = Path(__file__).resolve().parents[1] / "src"


def _worker(script: Path, *args: str) -> CommandWorker:
    return CommandWorker(
        (
            sys.executable,
            str(script),
            "{prompt}",
            "{input_dir}",
            "{output_dir}",
            "{problem_file}",
            *args,
        )
    )


def _request(
    worker: CommandWorker,
    *,
    timeout: float = 2,
    max_launches: int = 1,
    retry: RetryPolicy | None = None,
) -> Request:
    return Request(
        "job",
        "Read input and write output.",
        {"input.txt": "payload"},
        ("result.txt",),
        worker,
        timeout_seconds=timeout,
        max_launches=max_launches,
        retry=retry or RetryPolicy(),
    )


def test_worker_argv_preserves_literal_braces(tmp_path: Path) -> None:
    worker = CommandWorker((sys.executable, "-c", 'print({"x": 1})', "{prompt}"))
    prompt = tmp_path / "{input_dir}" / "prompt.txt"
    command = worker.command({"prompt": prompt})
    assert command[2] == 'print({"x": 1})'
    assert command[3] == str(prompt)


@pytest.mark.parametrize("leader_exits", [False, True])
def test_process_group_children_are_stopped(tmp_path: Path, leader_exits: bool) -> None:
    script = tmp_path / "worker.py"
    script.write_text(
        """\
import subprocess
import sys
import time
from pathlib import Path

_, inputs, outputs, problem, marker, mode = sys.argv[1:7]
subprocess.Popen([sys.executable, '-c',
    'import sys,time; from pathlib import Path; '
    'time.sleep(0.6); Path(sys.argv[1]).write_text("escaped")',
    marker])
(Path(outputs) / 'result.txt').write_text('premature')
if mode == 'wait':
    time.sleep(10)
""",
        encoding="utf-8",
    )
    marker = tmp_path / "escaped.txt"
    worker = _worker(script, str(marker), "exit" if leader_exits else "wait")
    with Run(tmp_path / "records", tmp_path) as run:
        result = run.call(_request(worker, timeout=0.1))
    assert result.status == ("process_error" if leader_exits else "timeout")
    assert result.outputs == {}
    time.sleep(0.7)
    assert not marker.exists(), "a child survived the leader's completion/timeout"


def test_lock_workdir_binding_and_closed_controller(tmp_path: Path) -> None:
    records = tmp_path / "records"
    other = tmp_path / "other"
    other.mkdir()
    worker = CommandWorker((sys.executable, "-c", "pass"))
    with Run(records, tmp_path) as run:
        with pytest.raises(RunBusyError):
            with Run(records, tmp_path):
                pass
    with pytest.raises(RuntimeError, match="not open"):
        run.call(_request(worker))
    with pytest.raises(RecordError, match="workdir"):
        with Run(records, other):
            pass


def test_cleanup_error_leaves_reservation_unresolved(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    records = tmp_path / "records"
    script = tmp_path / "sleep.py"
    script.write_text("import time\ntime.sleep(5)\n", encoding="utf-8")
    call = _request(_worker(script), timeout=0.05)

    def fail_cleanup(_: int) -> bool:
        raise PermissionError("injected cleanup failure")

    monkeypatch.setattr("treadle_headless.harness._cleanup_group", fail_cleanup)
    try:
        with Run(records, tmp_path) as run:
            with pytest.raises(PermissionError, match="injected cleanup failure"):
                run.call(call)
            with pytest.raises(RecordError, match="controller state is uncertain"):
                run.call(call)
    finally:
        # The injected failure deliberately leaves a real subprocess alive.
        if (records / "run.json").exists():
            state = json.loads((records / "run.json").read_text(encoding="utf-8"))
            attempts = state["calls"].get("job", {}).values()
            pids = [attempt["pid"] for entry in attempts for attempt in entry["attempts"]]
            for pid in pids:
                if pid is not None:
                    try:
                        os.killpg(pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass

    with Run(records, tmp_path) as run:
        unresolved = run.unresolved_launches()
        assert len(unresolved) == 1
        assert unresolved[0].status == "running"
        run.acknowledge_stopped(unresolved[0].launch_id)


def test_acknowledgment_spends_prelaunch_reservation_and_blocks_other_ids(tmp_path: Path) -> None:
    records = tmp_path / "records"
    script = tmp_path / "worker.py"
    script.write_text(
        "from pathlib import Path\nimport sys\n"
        "Path(sys.argv[3], 'result.txt').write_text('done')\n",
        encoding="utf-8",
    )
    worker = _worker(script)
    call = _request(worker, max_launches=2, retry=RetryPolicy(on=("interrupted",)))
    controller = tmp_path / "controller.py"
    controller.write_text(
        "import os\n"
        "import treadle_headless.run as module\n"
        "from treadle_headless import CommandWorker, Request, RetryPolicy, Run\n"
        "module.launch = lambda *a, **kw: os._exit(17)\n"
        f"worker = CommandWorker({worker.argv!r})\n"
        "call = Request('job', 'Read input and write output.', {'input.txt': 'payload'}, "
        "('result.txt',), worker, timeout_seconds=2, max_launches=2, "
        "retry=RetryPolicy(on=('interrupted',)))\n"
        f"with Run({str(records)!r}, {str(tmp_path)!r}) as run: run.call(call)\n",
        encoding="utf-8",
    )
    env = dict(os.environ, PYTHONPATH=str(SRC))
    ended = subprocess.run([sys.executable, str(controller)], cwd=tmp_path, env=env, check=False)
    assert ended.returncode == 17
    with Run(records, tmp_path) as run:
        unresolved = run.unresolved_launches()
        assert len(unresolved) == 1
        other = Request("other", call.task, call.inputs, call.required_outputs, worker)
        with pytest.raises(UncertainLaunchError):
            run.call(other)
        run.acknowledge_stopped(unresolved[0].launch_id)
        delivered = run.call(call)
    assert delivered.status == "delivered"
    assert len(delivered.attempts) == 2
    assert delivered.attempts[0].status == "interrupted"


def test_completed_record_survives_exit_after_atomic_commit(tmp_path: Path) -> None:
    records = tmp_path / "records"
    marker = tmp_path / "launches.txt"
    script = tmp_path / "worker.py"
    script.write_text(
        "from pathlib import Path\nimport sys\n"
        "with Path(sys.argv[5]).open('a') as f: f.write('launch\\n')\n"
        "Path(sys.argv[3], 'result.txt').write_text('done')\n",
        encoding="utf-8",
    )
    worker = _worker(script, str(marker))
    call = _request(worker)
    controller = tmp_path / "controller.py"
    controller.write_text(
        "import os\n"
        "from treadle_headless import CommandWorker, Request, Run\n"
        "original = Run._write_state\n"
        "def after_commit(self):\n"
        "    original(self)\n"
        "    state = self._state\n"
        "    if any(e['result'] is not None for v in state['calls'].values() "
        "for e in v.values()):\n"
        "        os._exit(23)\n"
        "Run._write_state = after_commit\n"
        f"worker = CommandWorker({worker.argv!r})\n"
        "call = Request('job', 'Read input and write output.', {'input.txt': 'payload'}, "
        "('result.txt',), worker, timeout_seconds=2)\n"
        f"with Run({str(records)!r}, {str(tmp_path)!r}) as run: run.call(call)\n",
        encoding="utf-8",
    )
    ended = subprocess.run(
        [sys.executable, str(controller)],
        cwd=tmp_path,
        env=dict(os.environ, PYTHONPATH=str(SRC)),
        check=False,
    )
    assert ended.returncode == 23
    with Run(records, tmp_path) as run:
        result = run.call(call)
    assert result.status == "delivered"
    assert result.reused
    assert marker.read_text(encoding="utf-8").splitlines() == ["launch"]


@pytest.mark.parametrize("value", [0, -1, True, float("nan"), float("inf")])
def test_invalid_timeout_rejected(value: object) -> None:
    with pytest.raises(ValueError):
        _request(CommandWorker(("echo",)), timeout=value)


@pytest.mark.parametrize("value", [0, -1, True, 1.5])
def test_invalid_launch_limit_rejected(value: object) -> None:
    with pytest.raises(ValueError):
        _request(CommandWorker(("echo",)), max_launches=value)
