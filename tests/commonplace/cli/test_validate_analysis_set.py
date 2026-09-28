from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.cli import validate_notes
from commonplace.lib import agentic_set, validation
from commonplace.lib.project_paths import (
    analysis_set_overview,
    list_collection_validation_paths,
)
from tests.commonplace.lib.test_agentic_analysis import RUN_ID, valid_run_state, write

pytestmark = pytest.mark.usefixtures("tmp_library")


def retained_dir(tmp_path: Path) -> Path:
    valid_run_state(tmp_path)
    return tmp_path / agentic_set.retained_overview_path(RUN_ID).parent


def diagnostics(tmp_path: Path, target: str) -> list[tuple[str, str]]:
    resolved = validate_notes.resolve_validation_target(target, repo_root=tmp_path)
    outcome = validation.run_validation(resolved.paths, repo_root=tmp_path, collection=resolved.collection)
    report = validate_notes.build_validation_report(
        target_arg=target, target=resolved, outcome=outcome, repo_root=tmp_path
    )
    return [(item.severity, item.reason) for item in report.diagnostics]


def test_a_run_directory_validates_as_its_overview(tmp_path: Path) -> None:
    directory = retained_dir(tmp_path)
    (directory / "runtime.md").write_text(
        (directory / "runtime.md").read_text() + "\nBroken: OBJ-1/O2.\n", encoding="utf-8"
    )

    resolved = validate_notes.resolve_validation_target(str(directory), repo_root=tmp_path)

    assert resolved.paths == (directory / "overview.md",)
    assert resolved.collection is None
    from_directory = diagnostics(tmp_path, str(directory))
    from_overview = diagnostics(tmp_path, str(directory / "overview.md"))
    assert from_directory == from_overview
    assert any("runtime.md bytes hash to" in reason for _, reason in from_directory)


def test_a_run_directory_with_a_missing_member_fails_at_the_set_level(tmp_path: Path) -> None:
    directory = retained_dir(tmp_path)
    (directory / "epistemic.md").unlink()

    failures = [reason for severity, reason in diagnostics(tmp_path, str(directory)) if severity == "failure"]

    assert len(failures) == 1
    assert "member set: cannot read epistemic.md" in failures[0]


def test_a_member_validated_alone_gets_only_its_own_checks(tmp_path: Path) -> None:
    directory = retained_dir(tmp_path)
    (directory / "epistemic.md").unlink()

    results = validation.validate_note(directory / "runtime.md", repo_root=tmp_path)

    assert results.fails == []
    assert results.note_type == "agentic-system-runtime-report"


def test_a_collection_sweep_treats_the_run_directory_as_one_unit(tmp_path: Path) -> None:
    directory = retained_dir(tmp_path)
    write(directory.parent / "README.md", "# Retained analyses\n")
    collection = tmp_path / "kb/reports"

    paths = list_collection_validation_paths(collection)

    assert directory / "overview.md" in paths
    assert not any(path.parent == directory and path.name != "overview.md" for path in paths)
    assert directory.parent / "README.md" in paths


def test_recognition_needs_an_overview_of_the_analysis_type(tmp_path: Path) -> None:
    directory = tmp_path / "kb/reports/retained/other"
    write(directory / "overview.md", "---\ntype: types/note.md\ndescription: Not a set\n---\n# Other\n")
    write(directory / "member.md", "# Member\n")

    assert analysis_set_overview(directory) is None
    assert analysis_set_overview(tmp_path / "kb/reports/retained/missing") is None
    assert analysis_set_overview(retained_dir(tmp_path)) is not None
