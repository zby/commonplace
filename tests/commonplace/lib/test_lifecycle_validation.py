from __future__ import annotations

from pathlib import Path

from commonplace.lib.lifecycle_validation import validate_lifecycle


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_lifecycle_validation_reports_bounded_contradictions(tmp_path: Path) -> None:
    write(
        tmp_path / "kb/work/README.md",
        "- [registered](./registered/README.md) — active\n",
    )
    write(tmp_path / "kb/work/registered/README.md", "# Registered\n")
    write(tmp_path / "kb/work/unregistered/README.md", "# Unregistered\n")
    write(tmp_path / "kb/work/unframed/scratch.md", "Scratch\n")
    write(
        tmp_path / "kb/tasks/backlog/done.md",
        "# Done\n\n## Tasks\n\n- [x] First\n- [X] Second\n",
    )
    write(
        tmp_path / "kb/tasks/recurring/review.md",
        (
            "# Review\n\n## Output\n\nRecord findings in "
            "`kb/tasks/recurring/review-log.md`.\n"
        ),
    )

    results = validate_lifecycle(repo_root=tmp_path)

    assert results.subjects_inspected == 5
    assert [item.diagnostic_id for item in results.diagnostics] == [
        "lifecycle.workshop.unregistered",
        "lifecycle.workshop.missing-framing",
        "lifecycle.workshop.unregistered",
        "lifecycle.task.backlog-complete",
        "lifecycle.task.recurring-output-missing",
    ]
    assert [item.severity for item in results.diagnostics] == [
        "warning",
        "failure",
        "warning",
        "warning",
        "warning",
    ]
    assert results.diagnostics[-1].reason.endswith(
        "create it on the first run or revise the destination"
    )


def test_lifecycle_validation_accepts_registered_framed_and_open_work(
    tmp_path: Path,
) -> None:
    write(
        tmp_path / "kb/work/README.md",
        "- [active](./active/README.md) — active\n",
    )
    write(tmp_path / "kb/work/active/framing.md", "# Framing\n")
    write(
        tmp_path / "kb/tasks/backlog/open.md",
        "# Open\n\n## Tasks\n\n- [x] First\n- [ ] Second\n",
    )
    write(
        tmp_path / "kb/tasks/recurring/review.md",
        (
            "# Review\n\n## Output\n\nRecord findings in "
            "`kb/tasks/recurring/review-log.md`.\n"
        ),
    )
    write(tmp_path / "kb/tasks/recurring/review-log.md", "# Log\n")

    results = validate_lifecycle(repo_root=tmp_path)

    assert results.subjects_inspected == 4
    assert results.diagnostics == ()
