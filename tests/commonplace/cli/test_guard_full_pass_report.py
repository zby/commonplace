from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from commonplace.cli.guard_full_pass_report import main
from tests.commonplace.lib.test_full_pass import write_packet


def test_guard_cli_emits_json_and_exits_zero_when_all_inputs_match(
    tmp_path: Path, capsys
) -> None:
    report = write_packet(tmp_path)

    exit_code = main([str(report.relative_to(tmp_path))], cwd=tmp_path)
    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["all_matching"] is True
    assert [item["status"] for item in payload["inputs"]] == ["matching"]
    assert captured.err == ""


def test_guard_cli_exits_one_with_complete_refusal_payload(
    tmp_path: Path, capsys
) -> None:
    report = write_packet(
        tmp_path,
        disposition="merge",
        live_source_text="changed source\n",
    )
    (tmp_path / "kb/notes/target.md").unlink()

    exit_code = main([str(report.relative_to(tmp_path))], cwd=tmp_path)
    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 1
    assert payload["all_matching"] is False
    assert [item["status"] for item in payload["inputs"]] == [
        "changed",
        "missing",
    ]
    assert "transition refused" in captured.err


def test_guard_cli_exits_two_for_invalid_report(tmp_path: Path, capsys) -> None:
    report = write_packet(tmp_path)
    report.write_text("not a report\n", encoding="utf-8")

    exit_code = main([str(report.relative_to(tmp_path))], cwd=tmp_path)
    payload = json.loads(capsys.readouterr().out)

    assert exit_code == 2
    assert "missing frontmatter" in payload["error"]


def test_guard_cli_exits_two_with_json_for_invalid_invocation(capsys) -> None:
    exit_code = main([])
    captured = capsys.readouterr()

    assert exit_code == 2
    assert "required" in json.loads(captured.out)["error"]
    assert captured.err == ""


def test_guard_persists_across_processes_in_one_working_copy(tmp_path: Path) -> None:
    report = write_packet(tmp_path)
    command = [
        sys.executable,
        "-m",
        "commonplace.cli.guard_full_pass_report",
        str(report.relative_to(tmp_path)),
    ]

    first = subprocess.run(
        command, cwd=tmp_path, check=False, capture_output=True, text=True
    )
    (tmp_path / "kb/notes/source.md").write_text("later edit\n", encoding="utf-8")
    second = subprocess.run(
        command, cwd=tmp_path, check=False, capture_output=True, text=True
    )

    assert first.returncode == 0
    assert json.loads(first.stdout)["inputs"][0]["status"] == "matching"
    assert second.returncode == 1
    assert json.loads(second.stdout)["inputs"][0]["status"] == "changed"
