"""The command shell parses arguments and prints; the objects do the work."""

from __future__ import annotations

import ast
from pathlib import Path

import commonplace.workflow_legacy
from commonplace.workflow_legacy import Blocked, Orchestrator
from commonplace.workflow_legacy.shell import main, render
from tests.commonplace.workflow_legacy.definitions import (
    OneJob,
    ScriptedAgent,
    new_run,
    write_invalid,
)

DEFINITION = "tests.commonplace.workflow_legacy.definitions:TwoLenses"


def started(tmp_path: Path) -> Path:
    run_dir = new_run(tmp_path)
    assert main(["start", DEFINITION, "--run", str(run_dir)]) == 0
    return run_dir


def test_step_prints_one_launch_line_per_job(tmp_path, capsys):
    run_dir = started(tmp_path)
    capsys.readouterr()

    assert main(["step", str(run_dir)]) == 0

    lines = capsys.readouterr().out.splitlines()
    assert lines[0] == "launch"
    prompts = [line for line in lines if "prompt.md" in line]
    assert len(prompts) == 2
    assert all(Path(line.split("`")[1]).is_file() for line in prompts)


def test_start_refuses_a_run_that_already_started(tmp_path, capsys):
    run_dir = started(tmp_path)

    assert main(["start", DEFINITION, "--run", str(run_dir)]) == 1
    assert "already" in capsys.readouterr().err


def test_start_names_the_run_where_the_definition_says(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    located = "tests.commonplace.workflow_legacy.definitions:Located"

    assert main(["start", located, "--param", "name=example"]) == 0
    first = Path(capsys.readouterr().out.strip())
    assert main(["start", located, "--param", "name=example"]) == 0
    second = Path(capsys.readouterr().out.strip())

    assert first == tmp_path / "runs" / "example-01"
    assert second == tmp_path / "runs" / "example-02"
    assert Orchestrator.open(second).workflow.params == {"name": "example"}


def test_start_without_a_location_needs_the_run_directory(
    tmp_path, monkeypatch, capsys
):
    monkeypatch.chdir(tmp_path)

    assert main(["start", DEFINITION]) == 1
    assert "give the run directory" in capsys.readouterr().err


def test_step_refuses_a_directory_that_is_not_a_run(tmp_path, capsys):
    assert main(["step", str(tmp_path)]) == 1
    assert "not a run" in capsys.readouterr().err


def test_step_refuses_a_run_whose_state_cannot_be_read(tmp_path, capsys):
    run_dir = started(tmp_path)
    for path in (run_dir / "workflow-state").rglob("*"):
        if path.is_file():
            path.write_text("not a record\n", encoding="utf-8")
    capsys.readouterr()

    assert main(["step", str(run_dir)]) == 1
    assert "state" in capsys.readouterr().err


def test_start_refuses_a_name_that_is_not_a_workflow(tmp_path, capsys):
    run_dir = new_run(tmp_path)

    assert (
        main(
            [
                "start",
                "tests.commonplace.workflow_legacy.definitions:new_run",
                "--run",
                str(run_dir),
            ]
        )
        == 1
    )
    assert "workflow" in capsys.readouterr().err


def test_report_records_one_observation(tmp_path):
    run_dir = started(tmp_path)

    code = main(
        [
            "report",
            str(run_dir),
            "launch-failed",
            "--job",
            "lens-a",
            "--text",
            "rate limit",
        ]
    )

    assert code == 0
    (report,) = Orchestrator.open(run_dir).reports()
    assert (report.event, report.job, report.text) == (
        "launch-failed",
        "lens-a",
        "rate limit",
    )


def test_report_refuses_an_unlisted_event(tmp_path, capsys):
    run_dir = started(tmp_path)

    assert main(["report", str(run_dir), "finished"]) == 1
    assert "finished" in capsys.readouterr().err


def test_a_blocked_outcome_points_to_its_record_and_states_what_is_permitted(tmp_path):
    run_dir = new_run(tmp_path)
    result = ScriptedAgent(
        Orchestrator(run_dir, OneJob()), default=write_invalid
    ).run()[-1]
    assert isinstance(result, Blocked)

    lines = render(result).splitlines()

    assert lines[0] == "blocked"
    text = "\n".join(lines)
    assert str(result.blocks[0].record_path) in text
    assert OneJob.repair_scope in text
    assert "output must start with a level-one heading" not in text


def test_the_package_imports_nothing_from_the_rest_of_commonplace():
    package = Path(commonplace.workflow_legacy.__file__).parent
    foreign = []
    for path in sorted(package.glob("*.py")):
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            if isinstance(node, ast.ImportFrom):
                imported = [node.module or ""] if node.level == 0 else []
            elif isinstance(node, ast.Import):
                imported = [alias.name for alias in node.names]
            else:
                continue
            foreign += [
                f"{path.name}: {name}"
                for name in imported
                if name.startswith("commonplace")
                and not name.startswith("commonplace.workflow_legacy")
            ]

    assert foreign == []
