"""State survives the process: every step below runs in its own interpreter."""

from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

import pytest

from commonplace.workflow import Orchestrator, RunBusy
from commonplace.workflow.shell import main
from tests.commonplace.workflow.definitions import new_run, publications

REPOSITORY = Path(__file__).resolve().parents[3]
DEFINITION = "tests.commonplace.workflow.definitions:Publishes"


def shell(*arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "commonplace.workflow.shell", *arguments],
        cwd=REPOSITORY,
        capture_output=True,
        text=True,
        check=False,
    )


def started(tmp_path: Path, marker: Path) -> Path:
    run_dir = new_run(tmp_path)
    result = shell(
        "start",
        str(run_dir),
        DEFINITION,
        "--param",
        f"target={tmp_path / 'published'}",
        "--param",
        f"marker={marker}",
    )
    assert result.returncode == 0, result.stderr
    return run_dir


def test_a_run_advances_across_separate_processes(tmp_path):
    run_dir = started(tmp_path, tmp_path / "marker")

    assert shell("step", str(run_dir)).stdout.splitlines()[0] == "launch"
    (run_dir / "only.md").write_text("# only\n", encoding="utf-8")

    assert shell("step", str(run_dir)).stdout.splitlines() == ["done"]
    assert shell("step", str(run_dir)).stdout.splitlines() == ["done"]
    assert publications(tmp_path / "published") == 1


def test_a_process_that_ends_after_publishing_does_not_publish_again(tmp_path):
    marker = tmp_path / "marker"
    run_dir = started(tmp_path, marker)
    shell("step", str(run_dir))
    (run_dir / "only.md").write_text("# only\n", encoding="utf-8")

    marker.write_text("exit after", encoding="utf-8")
    ended = shell("step", str(run_dir))

    assert ended.returncode == 9
    assert ended.stdout == ""
    assert shell("step", str(run_dir)).stdout.splitlines() == ["done"]
    assert publications(tmp_path / "published") == 1


def test_a_process_that_ends_part_way_through_publishing_leaves_it_uncertain(tmp_path):
    marker = tmp_path / "marker"
    run_dir = started(tmp_path, marker)
    shell("step", str(run_dir))
    (run_dir / "only.md").write_text("# only\n", encoding="utf-8")

    marker.write_text("exit between", encoding="utf-8")
    assert shell("step", str(run_dir)).returncode == 9

    assert shell("step", str(run_dir)).stdout.splitlines()[0] == "uncertain"
    assert shell("step", str(run_dir)).stdout.splitlines()[0] == "uncertain"
    assert publications(tmp_path / "published") == 1


def test_the_operator_resolves_an_uncertain_effect_from_the_shell(tmp_path):
    marker = tmp_path / "marker"
    run_dir = started(tmp_path, marker)
    shell("step", str(run_dir))
    (run_dir / "only.md").write_text("# only\n", encoding="utf-8")
    marker.write_text("exit between", encoding="utf-8")
    shell("step", str(run_dir))
    assert shell("step", str(run_dir)).stdout.splitlines()[0] == "uncertain"

    (tmp_path / "published" / "index.md").write_text("- only.md\n", encoding="utf-8")
    assert shell("resolve", str(run_dir), "publish", "completed").returncode == 0

    assert shell("step", str(run_dir)).stdout.splitlines() == ["done"]
    assert publications(tmp_path / "published") == 1


def test_the_operator_releases_a_stopped_job_from_the_shell(tmp_path):
    run_dir = started(tmp_path, tmp_path / "marker")
    # No worker ever writes: two attempts, a block, two more attempts, a stop.
    outcomes = [shell("step", str(run_dir)).stdout.splitlines()[0] for _ in range(6)]
    assert outcomes == ["launch", "launch", "blocked", "launch", "launch", "blocked"]
    assert "stop and report" in shell("step", str(run_dir)).stdout

    assert shell("release", str(run_dir), "only").returncode == 0

    assert shell("step", str(run_dir)).stdout.splitlines()[0] == "launch"
    (run_dir / "only.md").write_text("# only\n", encoding="utf-8")
    assert shell("step", str(run_dir)).stdout.splitlines() == ["done"]


def test_a_step_is_refused_while_another_process_runs_one(tmp_path, capsys):
    run_dir = new_run(tmp_path)
    holding, finish = tmp_path / "holding", tmp_path / "finish"
    result = shell(
        "start",
        str(run_dir),
        "tests.commonplace.workflow.definitions:HoldsTheStep",
        "--param",
        f"holding={holding}",
        "--param",
        f"finish={finish}",
    )
    assert result.returncode == 0, result.stderr
    running = subprocess.Popen(
        [sys.executable, "-m", "commonplace.workflow.shell", "step", str(run_dir)],
        cwd=REPOSITORY,
        stdout=subprocess.PIPE,
        text=True,
    )
    try:
        deadline = time.monotonic() + 30
        while not holding.exists() and time.monotonic() < deadline:
            time.sleep(0.05)
        assert holding.exists()

        with pytest.raises(RunBusy):
            Orchestrator.open(run_dir).step()
        assert main(["step", str(run_dir)]) == 1
        assert "busy" in capsys.readouterr().err
    finally:
        finish.write_text("", encoding="utf-8")
        output, _ = running.communicate(timeout=30)

    assert output.splitlines()[0] == "launch"
