"""`commonplace-run` drives the toy job set from the command line."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from commonplace.cli.run import main
from tests.commonplace.workflow.conftest import COMPLETE_BRIEF, toy_library
from tests.commonplace.workflow.handlers import LOG_ENV

pytestmark = pytest.mark.usefixtures("tmp_library")


@pytest.fixture
def run(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> tuple[Path, Path]:
    declaration, _ = toy_library(tmp_path)
    monkeypatch.setenv(LOG_ENV, str(tmp_path / "handlers.log"))
    run_dir = tmp_path / "runs" / "toy-1"
    assert main(["start", str(run_dir), str(declaration), "--param", "subject=toy"]) == 0
    return run_dir, declaration


def advance_json(run_dir: Path, capsys: pytest.CaptureFixture[str], *args: str) -> dict:
    assert main(["advance", str(run_dir), "--json", *args]) == 0
    return json.loads(capsys.readouterr().out)


def test_start_refuses_a_second_start(run: tuple[Path, Path], capsys: pytest.CaptureFixture[str]) -> None:
    run_dir, declaration = run
    assert main(["start", str(run_dir), str(declaration)]) == 1
    assert "already holds a run" in capsys.readouterr().err


def test_advance_hands_out_and_takes_results(run: tuple[Path, Path], capsys: pytest.CaptureFixture[str]) -> None:
    run_dir, _ = run
    status = advance_json(run_dir, capsys)
    (handout,) = status["handouts"]
    assert handout["job"] == "brief"
    Path(handout["outputs"]["brief"]).write_text(COMPLETE_BRIEF, encoding="utf-8")

    assert main(["advance", str(run_dir), "--completed", handout["attempt"], "--model", "m", "--effort", "e"]) == 0
    text = capsys.readouterr().out
    assert "hand-out" in text and " report" in text and " other" in text
    assert text.rstrip().endswith("publishable: no")


def test_failed_result_stops_and_keeps_the_job_ready(run: tuple[Path, Path], capsys: pytest.CaptureFixture[str]) -> None:
    run_dir, _ = run
    (handout,) = advance_json(run_dir, capsys)["handouts"]
    Path(handout["problem"]).write_text("no source at that revision\n", encoding="utf-8")
    status = advance_json(run_dir, capsys, "--failed", f"{handout['attempt']}=worker gave up")
    (stop,) = status["stops"]
    assert stop["job"] == "brief" and "no source at that revision" in stop["reason"]
    assert [h["job"] for h in advance_json(run_dir, capsys)["handouts"]] == ["brief"]


def test_status_and_judge(run: tuple[Path, Path], capsys: pytest.CaptureFixture[str]) -> None:
    run_dir, _ = run
    (handout,) = advance_json(run_dir, capsys)["handouts"]
    Path(handout["outputs"]["brief"]).write_text(COMPLETE_BRIEF, encoding="utf-8")
    advance_json(run_dir, capsys, "--completed", handout["attempt"])

    assert main(["judge", str(run_dir), "--role", "brief", "--outcome", "refused", "--findings", "wrong system"]) == 0
    assert capsys.readouterr().out.startswith("recorded ")
    assert main(["status", str(run_dir), "--json"]) == 0
    view = json.loads(capsys.readouterr().out)
    assert "brief" in view["members"]
    assert [r["job"] for r in view["refusals"]] == ["brief"]
    assert view["refusals"][0]["findings"] == "wrong system"
    assert main(["status", str(run_dir)]) == 0
    assert "refusal " in capsys.readouterr().out

    assert main(["judge", str(run_dir), "--role", "nowhere", "--outcome", "accepted"]) == 1
    assert "no role nowhere" in capsys.readouterr().err
