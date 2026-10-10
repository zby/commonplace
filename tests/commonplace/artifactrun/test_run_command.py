"""`commonplace-run` drives the toy plan from the command line."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from commonplace.artifactrun import CodeJob, UncertainEffectError
from commonplace.artifactrun.store import RunStore
from commonplace.cli.run import main
from tests.commonplace.artifactrun.handlers import LOG_ENV
from tests.commonplace.artifactrun.support import COMPLETE_BRIEF, as_member, toy_library

pytestmark = pytest.mark.usefixtures("tmp_library")


@pytest.fixture
def run(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> tuple[Path, Path]:
    declaration, _ = toy_library(tmp_path)
    monkeypatch.setenv(LOG_ENV, str(tmp_path / "handlers.log"))
    run_dir = tmp_path / "runs" / "toy-1"
    assert main(["start", str(run_dir), str(declaration), "--param", "subject=toy"]) == 0
    return run_dir, declaration


def advance_json(run_dir: Path, capsys: pytest.CaptureFixture[str], *args: str, exit_code: int = 0) -> dict:
    assert main(["advance", str(run_dir), "--json", *args]) == exit_code
    return json.loads(capsys.readouterr().out)


def test_start_refuses_a_second_start(run: tuple[Path, Path], capsys: pytest.CaptureFixture[str]) -> None:
    run_dir, declaration = run
    assert main(["start", str(run_dir), str(declaration)]) == 1
    assert "already holds a run" in capsys.readouterr().err


def test_advance_hands_out_and_takes_results(run: tuple[Path, Path], capsys: pytest.CaptureFixture[str]) -> None:
    run_dir, _ = run
    (handout,) = advance_json(run_dir, capsys)["handouts"]
    assert handout["job"] == "brief"
    Path(handout["problem"]).write_text("no source at that revision\n", encoding="utf-8")
    status = advance_json(run_dir, capsys, "--failed", f"{handout['attempt']}=worker gave up", exit_code=2)
    (stop,) = status["stops"]
    assert stop["job"] == "brief" and "no source at that revision" in stop["reason"]
    (handout,) = advance_json(run_dir, capsys)["handouts"]
    assert handout["job"] == "brief", "a failed attempt leaves the job ready"
    Path(handout["outputs"]["brief"]).write_text(as_member("brief", COMPLETE_BRIEF), encoding="utf-8")
    Path(handout["worker_identity"]).write_text('{"model": "test-model", "effort": "medium"}\n', encoding="utf-8")

    assert main(["advance", str(run_dir), "--completed", handout["attempt"], "--model", "m", "--effort", "e"]) == 0
    text = capsys.readouterr().out
    assert "hand-out" in text and " report" in text and " other" in text
    assert text.rstrip().endswith("publishable: no")




@pytest.mark.parametrize("uncertain", (False, True))
def test_code_failures_keep_their_effect_distinction_on_status(run, capsys, monkeypatch, uncertain):
    run_dir, _ = run
    (handout,) = advance_json(run_dir, capsys)["handouts"]
    Path(handout["outputs"]["brief"]).write_text(as_member("brief", COMPLETE_BRIEF), encoding="utf-8")
    Path(handout["worker_identity"]).write_text('{"model": "test-model", "effort": "medium"}\n', encoding="utf-8")
    original = CodeJob.resolve_handler

    def fail(attempt):
        error = UncertainEffectError if uncertain else ValueError
        raise error("scripted external condition")

    monkeypatch.setattr(CodeJob, "resolve_handler", lambda job: fail if job.name == "check-brief" else original(job))
    status = advance_json(run_dir, capsys, "--completed", handout["attempt"], exit_code=2)
    (stop,) = status["stops"]
    assert stop["uncertain"] is uncertain
    (record,) = [r for r in RunStore(run_dir).attempt_records() if r["job"] == "check-brief"]
    assert record["state"] == "failed" and record["uncertain"] is uncertain and record["pins"] == {}
    assert main(["status", str(run_dir), "--json"]) == 0
    view = json.loads(capsys.readouterr().out)
    assert view["failed_attempts"] == [stop]
    assert main(["status", str(run_dir)]) == 0
    label = "uncertain effect" if uncertain else "stop"
    assert f"{label} check-brief" in capsys.readouterr().out
    monkeypatch.setattr(CodeJob, "resolve_handler", original)
    advance_json(run_dir, capsys)
    assert main(["status", str(run_dir), "--json"]) == 0
    assert json.loads(capsys.readouterr().out)["failed_attempts"] == []
    # The earlier failure remains evidence after recovery.
    assert [r for r in RunStore(run_dir).attempt_records() if r["state"] == "failed"] == [record]


def test_status_and_judge(run: tuple[Path, Path], capsys: pytest.CaptureFixture[str]) -> None:
    run_dir, _ = run
    (handout,) = advance_json(run_dir, capsys)["handouts"]
    Path(handout["outputs"]["brief"]).write_text(as_member("brief", COMPLETE_BRIEF), encoding="utf-8")
    Path(handout["worker_identity"]).write_text('{"model": "test-model", "effort": "medium"}\n', encoding="utf-8")
    advance_json(run_dir, capsys, "--completed", handout["attempt"])

    assert main(["judge", str(run_dir), "--role", "brief", "--outcome", "refused", "--findings", "wrong system"]) == 0
    assert capsys.readouterr().out.startswith("recorded ")
    assert main(["status", str(run_dir), "--json"]) == 0
    view = json.loads(capsys.readouterr().out)
    assert "brief" in view["members"]
    assert [r["job"] for r in view["refusals"]] == ["brief"]
    assert view["refusals"][0]["findings"] == "wrong system"
    assert main(["status", str(run_dir)]) == 0
    text = capsys.readouterr().out
    assert "refusal " in text and "open hand-out" in text

    assert main(["judge", str(run_dir), "--role", "nowhere", "--outcome", "accepted"]) == 1
    assert "no role nowhere" in capsys.readouterr().err
