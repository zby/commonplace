"""State survives the process: every step below runs in its own interpreter."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from tests.commonplace.workflow.definitions import new_run, on_request, publications

pytestmark = on_request

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
