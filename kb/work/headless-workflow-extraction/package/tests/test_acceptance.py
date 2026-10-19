"""Independent acceptance probes through the public API and real subprocesses."""

from __future__ import annotations

import json
import os
import signal
import subprocess
import sys
import time
from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest

from treadle_headless import (
    CommandWorker,
    RecordError,
    Request,
    RetryPolicy,
    Run,
    UncertainLaunchError,
)

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
PACKAGE_SRC = Path(__file__).resolve().parents[1] / "src"


@pytest.fixture
def command_script(tmp_path: Path) -> Path:
    script = tmp_path / "command.py"
    script.write_text(
        """\
import json
import os
from pathlib import Path
import sys
import time

prompt, inputs, outputs, problem, mode, marker = sys.argv[1:7]
inputs, outputs, problem = Path(inputs), Path(outputs), Path(problem)
if not Path(prompt).read_text(encoding="utf-8").strip():
    raise RuntimeError("prompt was not rendered")
log = Path(os.environ["ACCEPTANCE_LOG"])
def event(name):
    with log.open("a", encoding="utf-8") as handle:
        payload = {"event": name, "mode": mode, "marker": marker, "pid": os.getpid()}
        handle.write(json.dumps(payload) + "\\n")

event("start")
value = (inputs / "value.txt").read_text(encoding="utf-8")
outputs.mkdir(parents=True, exist_ok=True)
if mode == "first_partial":
    flag = Path(os.environ["ACCEPTANCE_FLAG"])
    try:
        fd = os.open(flag, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        pass
    else:
        os.close(fd)
        (outputs / "result.txt").write_text("STALE", encoding="utf-8")
        problem.write_text(
            json.dumps({"kind": "unable", "message": "first launch failed"}),
            encoding="utf-8",
        )
        event("partial")
        sys.exit(7)
if mode == "always_fail":
    (outputs / "result.txt").write_text("STALE", encoding="utf-8")
    event("failed")
    sys.exit(7)
if mode == "missing":
    event("missing")
    sys.exit(0)
if mode == "usage_limit":
    problem.write_text(json.dumps({"kind": "usage_limit", "message": "quota"}), encoding="utf-8")
    event("limited")
    sys.exit(0)
if mode == "sleep_success":
    time.sleep(0.45)
if mode == "sleep_fail":
    time.sleep(0.12)
    event("failed")
    sys.exit(7)
(outputs / "result.txt").write_text(value + marker, encoding="utf-8")
event("done")
""",
        encoding="utf-8",
    )
    return script


def events(log: Path) -> list[dict[str, object]]:
    if not log.exists():
        return []
    return [json.loads(line) for line in log.read_text(encoding="utf-8").splitlines()]


def request(
    call_id: str,
    worker: CommandWorker,
    *,
    value: str = "value",
    max_launches: int = 1,
    retry: RetryPolicy | None = None,
) -> Request:
    return Request(
        call_id=call_id,
        task="Read value.txt and write result.txt.",
        inputs={"value.txt": value},
        required_outputs=("result.txt",),
        worker=worker,
        max_launches=max_launches,
        retry=retry or RetryPolicy(),
    )


def command(script: Path, log: Path, mode: str = "echo", marker: str = "") -> CommandWorker:
    return CommandWorker(
        argv=(
            sys.executable,
            str(script),
            "{prompt}",
            "{input_dir}",
            "{output_dir}",
            "{problem_file}",
            mode,
            marker or "-",
        ),
        env={"ACCEPTANCE_LOG": str(log), "ACCEPTANCE_FLAG": str(log.with_suffix(".flag"))},
    )


def test_same_material_different_call_ids_launch_independently(
    command_script: Path, tmp_path: Path
) -> None:
    log = tmp_path / "events.jsonl"
    worker = command(command_script, log)
    with Run(tmp_path / "records", tmp_path) as run:
        first = run.call(request("first", worker))
        second = run.call(request("second", worker))
        again = run.call(request("first", worker))
    assert first.status == second.status == again.status == "delivered"
    assert first.attempts[0].launch_id != second.attempts[0].launch_id
    assert not first.reused and not second.reused and again.reused
    assert len([e for e in events(log) if e["event"] == "start"]) == 2


def test_changed_declared_inputs_miss_reuse(command_script: Path, tmp_path: Path) -> None:
    log = tmp_path / "events.jsonl"
    worker = command(command_script, log)
    with Run(tmp_path / "records", tmp_path) as run:
        first = run.call(request("same", worker, value="old"))
        changed = run.call(request("same", worker, value="new"))
    assert first.outputs["result.txt"] == "old-"
    assert changed.outputs["result.txt"] == "new-"
    assert not changed.reused
    assert len([e for e in events(log) if e["event"] == "start"]) == 2


def test_failed_partial_output_and_problem_do_not_leak(
    command_script: Path, tmp_path: Path
) -> None:
    log = tmp_path / "events.jsonl"
    worker = command(command_script, log, "first_partial")
    call = request(
        "partial",
        worker,
        max_launches=2,
        retry=RetryPolicy(on=("worker_problem", "process_error")),
    )
    with Run(tmp_path / "records", tmp_path) as run:
        result = run.call(call)
    assert result.status == "delivered"
    assert result.outputs == {"result.txt": "value-"}
    assert len(result.attempts) == 2
    assert result.attempts[0].status != "delivered"
    assert result.attempts[0].launch_dir != result.attempts[1].launch_dir
    assert len([e for e in events(log) if e["event"] == "start"]) == 2


def test_request_and_result_are_immutable_snapshots(command_script: Path, tmp_path: Path) -> None:
    log = tmp_path / "events.jsonl"
    input_contents = {"value.txt": "original"}
    worker_env = {"ACCEPTANCE_LOG": str(log), "ACCEPTANCE_FLAG": str(log.with_suffix(".flag"))}
    worker = CommandWorker(
        argv=(
            sys.executable,
            str(command_script),
            "{prompt}",
            "{input_dir}",
            "{output_dir}",
            "{problem_file}",
            "echo",
            "-",
        ),
        env=worker_env,
    )
    call = Request("immutable", "Read value.txt.", input_contents, ("result.txt",), worker)
    input_contents["value.txt"] = "mutated"
    worker_env["ACCEPTANCE_LOG"] = str(tmp_path / "other.jsonl")
    with Run(tmp_path / "records", tmp_path) as run:
        result = run.call(call)
    assert result.outputs["result.txt"] == "original-"
    with pytest.raises(TypeError):
        result.outputs["result.txt"] = "tampered"
    with pytest.raises(FrozenInstanceError):
        result.status = "tampered"
    assert len(events(log)) == 2


def test_parallel_group_waits_for_all_calls_before_reporting_failure(
    command_script: Path, tmp_path: Path
) -> None:
    log = tmp_path / "events.jsonl"
    with Run(tmp_path / "records", tmp_path) as run:
        try:
            results = run.parallel(
                (
                    request("fail", command(command_script, log, "sleep_fail")),
                    request("finish", command(command_script, log, "sleep_success")),
                ),
                max_workers=2,
            )
        finally:
            observed = events(log)
    assert any(e["event"] == "done" and e["mode"] == "sleep_success" for e in observed)
    assert results[0].status != "delivered"
    assert results[1].status == "delivered"


@pytest.mark.parametrize("delays", [(0.0, 0.2), (0.2, 0.0)])
def test_ordinary_workflow_resumes_and_checks_frozen_siblings(
    tmp_path: Path, delays: tuple[float, float]
) -> None:
    workdir = tmp_path / "ordinary"
    workdir.mkdir()
    (workdir / "left-source.txt").write_text("alpha\n", encoding="utf-8")
    (workdir / "right-source.txt").write_text("beta\n", encoding="utf-8")
    records = tmp_path / "records"
    base = [
        sys.executable,
        str(EXAMPLES / "ordinary_files.py"),
        str(records),
        str(workdir),
        "--left-delay",
        str(delays[0]),
        "--right-delay",
        str(delays[1]),
    ]
    env = dict(
        os.environ, PYTHONPATH=str(PACKAGE_SRC) + os.pathsep + os.environ.get("PYTHONPATH", "")
    )

    def invoke(*extra: str) -> dict[str, object]:
        completed = subprocess.run(
            base + list(extra),
            env=env,
            cwd=workdir,
            text=True,
            capture_output=True,
            check=True,
            timeout=10,
        )
        return json.loads(completed.stdout)

    stopped = invoke("--stop-after-producers")
    assert stopped["status"] == "stopped"
    assert len((workdir / "invocations.log").read_text(encoding="utf-8").splitlines()) == 2
    accepted = invoke()
    assert accepted["status"] == "accepted"
    assert accepted["candidate"] == "LEFT:alpha\nRIGHT:beta\n"
    assert accepted["corrections_used"] == 1
    assert accepted["producer_reused"] == {"left": True, "right": True}
    assert len((workdir / "invocations.log").read_text(encoding="utf-8").splitlines()) == 4
    repeated = invoke()
    assert repeated["status"] == "accepted"
    assert repeated["combine_reused"] is True
    assert len((workdir / "invocations.log").read_text(encoding="utf-8").splitlines()) == 4


def test_workflow_correction_budget_is_bounded(tmp_path: Path) -> None:
    workdir = tmp_path / "ordinary"
    workdir.mkdir()
    (workdir / "left-source.txt").write_text("alpha", encoding="utf-8")
    (workdir / "right-source.txt").write_text("beta", encoding="utf-8")
    env = dict(
        os.environ, PYTHONPATH=str(PACKAGE_SRC) + os.pathsep + os.environ.get("PYTHONPATH", "")
    )
    base = [
        sys.executable,
        str(EXAMPLES / "ordinary_files.py"),
        str(tmp_path / "records"),
        str(workdir),
    ]
    rejected = subprocess.run(
        base + ["--max-corrections", "0"],
        env=env,
        cwd=workdir,
        text=True,
        capture_output=True,
        check=True,
        timeout=10,
    )
    assert json.loads(rejected.stdout)["status"] == "rejected"
    assert len((workdir / "invocations.log").read_text(encoding="utf-8").splitlines()) == 3
    accepted = subprocess.run(
        base, env=env, cwd=workdir, text=True, capture_output=True, check=True, timeout=10
    )
    assert json.loads(accepted.stdout)["status"] == "accepted"
    assert len((workdir / "invocations.log").read_text(encoding="utf-8").splitlines()) == 4


def test_launch_allowance_remains_spent_after_restart(command_script: Path, tmp_path: Path) -> None:
    log = tmp_path / "events.jsonl"
    call = request(
        "fail-twice",
        command(command_script, log, "always_fail"),
        max_launches=2,
        retry=RetryPolicy(on=("process_error",)),
    )
    with Run(tmp_path / "records", tmp_path) as run:
        first = run.call(call)
    assert first.status == "process_error"
    assert first.exhausted
    assert len(first.attempts) == 2
    with Run(tmp_path / "records", tmp_path) as run:
        resumed = run.call(call)
    assert resumed.exhausted
    assert len([e for e in events(log) if e["event"] == "start"]) == 2


def test_missing_output_and_usage_limit_are_explicit(command_script: Path, tmp_path: Path) -> None:
    log = tmp_path / "events.jsonl"
    with Run(tmp_path / "records", tmp_path) as run:
        missing = run.call(request("missing", command(command_script, log, "missing")))
        limited = run.call(
            request(
                "limited",
                command(command_script, log, "usage_limit"),
                max_launches=3,
                retry=RetryPolicy(on=("process_error", "worker_problem")),
            )
        )
    assert missing.status == "incomplete"
    assert missing.outputs == {}
    assert limited.status == "usage_limit"
    assert len(limited.attempts) == 1
    assert len([e for e in events(log) if e["event"] == "start"]) == 2


@pytest.mark.parametrize(
    "unsafe_name", ("../escape.txt", "/tmp/escape.txt", "nested/name.txt", "..")
)
def test_runtime_managed_names_reject_escape(
    command_script: Path, tmp_path: Path, unsafe_name: str
) -> None:
    worker = command(command_script, tmp_path / "events.jsonl")
    with pytest.raises(ValueError):
        Request("escape", "Write the result.", {"value.txt": "value"}, (unsafe_name,), worker)


def test_unresolved_reservation_blocks_resume_until_old_worker_stops(
    command_script: Path, tmp_path: Path
) -> None:
    log = tmp_path / "events.jsonl"
    records = tmp_path / "records"
    worker = command(command_script, log, "sleep_success")
    call = request("interrupted", worker, max_launches=2, retry=RetryPolicy(on=("interrupted",)))
    controller = tmp_path / "controller.py"
    controller.write_text(
        "from treadle_headless import Run, Request, RetryPolicy, CommandWorker\n"
        f"worker = CommandWorker(argv={worker.argv!r}, env={dict(worker.env)!r})\n"
        "call = Request('interrupted', 'Read value.txt and write result.txt.', "
        "{'value.txt': 'value'}, ('result.txt',), worker, "
        "max_launches=2, retry=RetryPolicy(on=('interrupted',)))\n"
        f"with Run({str(records)!r}, {str(tmp_path)!r}) as run:\n"
        "    run.call(call)\n",
        encoding="utf-8",
    )
    env = dict(
        os.environ, PYTHONPATH=str(PACKAGE_SRC) + os.pathsep + os.environ.get("PYTHONPATH", "")
    )
    controller_process = subprocess.Popen([sys.executable, str(controller)], cwd=tmp_path, env=env)
    deadline = time.monotonic() + 5
    while not any(e["event"] == "start" for e in events(log)) and time.monotonic() < deadline:
        time.sleep(0.01)
    assert any(e["event"] == "start" for e in events(log)), "worker did not start"
    os.kill(controller_process.pid, signal.SIGKILL)
    controller_process.wait(timeout=5)
    deadline = time.monotonic() + 5
    while not any(e["event"] == "done" for e in events(log)) and time.monotonic() < deadline:
        time.sleep(0.01)
    assert any(e["event"] == "done" for e in events(log)), "old worker did not finish"

    with Run(records, tmp_path) as run:
        unresolved = run.unresolved_launches()
        assert len(unresolved) == 1
        with pytest.raises(UncertainLaunchError):
            run.call(call)
        run.acknowledge_stopped(unresolved[0].launch_id)
        resumed = run.call(call)
    assert resumed.status == "delivered"
    assert len(resumed.attempts) == 2
    assert resumed.attempts[0].launch_dir != resumed.attempts[1].launch_dir
    assert len([e for e in events(log) if e["event"] == "start"]) == 2


@pytest.mark.parametrize(
    "damage",
    (
        "missing",
        "broken_json",
        "invalid_result",
        "missing_required",
        "forged_name",
        "changed_content",
    ),
)
def test_missing_or_corrupt_result_record_fails_visibly(
    command_script: Path, tmp_path: Path, damage: str
) -> None:
    records = tmp_path / "records"
    worker = command(command_script, tmp_path / "events.jsonl")
    with Run(records, tmp_path) as run:
        delivered = run.call(request("stored", worker))
    assert delivered.status == "delivered"
    record = records / "run.json"
    if damage == "missing":
        record.unlink()
    elif damage == "broken_json":
        record.write_text("{unparseable", encoding="utf-8")
    else:
        state = json.loads(record.read_text(encoding="utf-8"))
        entry = next(iter(state["calls"]["stored"].values()))
        if damage == "invalid_result":
            entry["result"]["outputs"] = {"result.txt": ["invalid content"]}
        elif damage == "missing_required":
            entry["result"]["outputs"] = {}
        elif damage == "changed_content":
            entry["result"]["outputs"]["result.txt"] = "plausible but altered"
        else:
            entry["result"]["outputs"]["forged.txt"] = "not requested"
        record.write_text(json.dumps(state), encoding="utf-8")
    with pytest.raises(RecordError):
        with Run(records, tmp_path) as run:
            run.call(request("stored", worker))


def test_failed_result_commit_poisoned_controller_until_reopen(
    command_script: Path, tmp_path: Path
) -> None:
    log = tmp_path / "events.jsonl"
    records = tmp_path / "records"
    worker = command(command_script, log)
    call = request("commit", worker, max_launches=2, retry=RetryPolicy(on=("interrupted",)))
    with Run(records, tmp_path) as run:
        original_write = run._write_state
        injected = False

        def fail_delivered_commit() -> None:
            nonlocal injected
            state = run._state
            entries = state["calls"].get("commit", {}) if state is not None else {}
            if not injected and any(entry["result"] is not None for entry in entries.values()):
                injected = True
                raise OSError("injected failure before atomic result commit")
            original_write()

        run._write_state = fail_delivered_commit
        with pytest.raises(OSError, match="injected failure"):
            run.call(call)
        assert injected
        run._write_state = original_write
        with pytest.raises((RecordError, UncertainLaunchError)):
            run.call(call)

    with Run(records, tmp_path) as run:
        unresolved = run.unresolved_launches()
        assert len(unresolved) == 1
        with pytest.raises(UncertainLaunchError):
            run.call(call)
        run.acknowledge_stopped(unresolved[0].launch_id)
        resumed = run.call(call)
    assert resumed.status == "delivered"
    assert len(resumed.attempts) == 2
    assert len([e for e in events(log) if e["event"] == "start"]) == 2
