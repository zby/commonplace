from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib.validation import validate_note
from tests.commonplace.validation_helpers import (
    NOTE_TYPE_SPECS,
    copy_repo_files,
    write_packet,
)


def install_types(repo: Path) -> None:
    copy_repo_files(
        repo,
        *NOTE_TYPE_SPECS,
        "kb/types/full-pass-report.md",
        "kb/types/full-pass-report.schema.yaml",
    )


def edit(report: Path, old: str, new: str) -> None:
    text = report.read_text(encoding="utf-8")
    assert old in text, f"fixture text not found: {old!r}"
    report.write_text(text.replace(old, new, 1), encoding="utf-8")


def has_fail(result, *fragments: str) -> bool:
    return any(all(f in item for f in fragments) for item in result.fails)


def test_full_pass_type_rule_verifies_capture_and_resolution(tmp_path: Path) -> None:
    install_types(tmp_path)
    report = write_packet(tmp_path)

    result = validate_note(report, repo_root=tmp_path)

    assert not result.fails
    assert any("packet captures: all 1" in item for item in result.passes)
    assert any("resolution projection" in item for item in result.passes)


def test_full_pass_type_rule_rejects_corrupt_capture(tmp_path: Path) -> None:
    install_types(tmp_path)
    report = write_packet(tmp_path)
    (report.parent / "source.txt").write_text("corrupted\n", encoding="utf-8")

    result = validate_note(report, repo_root=tmp_path)

    assert has_fail(result, "does not match its recorded hash")


def test_full_pass_type_rule_rejects_resolution_projection_drift(
    tmp_path: Path,
) -> None:
    install_types(tmp_path)
    report = write_packet(tmp_path)
    edit(report, "**Status:** not-required", "**Status:** pending")

    result = validate_note(report, repo_root=tmp_path)

    assert has_fail(result, "resolution projection")


def test_full_pass_type_rule_rejects_duplicate_resolution_sections(
    tmp_path: Path,
) -> None:
    install_types(tmp_path)
    report = write_packet(tmp_path)
    report.write_text(
        report.read_text(encoding="utf-8")
        + "\n\n## Other\n\nContext.\n\n## Resolution\n\nDuplicate.\n",
        encoding="utf-8",
    )

    result = validate_note(report, repo_root=tmp_path)

    assert has_fail(result, "headings")


@pytest.mark.parametrize(
    ("disposition", "capture_count"),
    [
        ("merge", 2),  # the merge target is captured alongside the source
        ("rehome", 1),
        ("revise", 1),  # revise hands back from the packet phase
    ],
)
def test_pending_disposition_validates_its_packet_captures(
    tmp_path: Path, disposition: str, capture_count: int
) -> None:
    install_types(tmp_path)
    report = write_packet(tmp_path, disposition=disposition)

    result = validate_note(report, repo_root=tmp_path)

    assert not result.fails
    assert any(f"packet captures: all {capture_count}" in item for item in result.passes)


def test_terminal_resolution_requires_complete_metadata(tmp_path: Path) -> None:
    install_types(tmp_path)
    report = write_packet(tmp_path, disposition="delete")
    edit(report, "resolution: pending", "resolution: accepted")

    result = validate_note(report, repo_root=tmp_path)

    assert has_fail(result, "resolved_at")
    assert has_fail(result, "resolution_authority")


def test_keep_report_may_be_superseded_by_version_guard(tmp_path: Path) -> None:
    install_types(tmp_path)
    report = write_packet(tmp_path)
    edit(
        report,
        """resolution: not-required
resolved_at: null
resolution_authority: null
resolution_summary: null
resolution_rationale: null
resulting_paths: []""",
        """resolution: superseded
resolved_at: "2026-07-13T17:00:00Z"
resolution_authority: version-guard
resolution_summary: Source changed before packet application
resolution_rationale: The packet no longer describes the live source
resulting_paths: [kb/notes/source.md]""",
    )
    edit(
        report,
        """**Status:** not-required
**Resolved at:** —
**Authority:** —
**Outcome:** —
**Rationale:** —
**Resulting paths:** —""",
        """**Status:** superseded
**Resolved at:** 2026-07-13T17:00:00Z
**Authority:** version-guard
**Outcome:** Source changed before packet application
**Rationale:** The packet no longer describes the live source
**Resulting paths:** `kb/notes/source.md`""",
    )

    result = validate_note(report, repo_root=tmp_path)

    assert not result.fails


def test_completed_recovery_requires_ready_closing_status(tmp_path: Path) -> None:
    install_types(tmp_path)
    report = write_packet(
        tmp_path,
        phase="complete",
        final_text="edited text\n",
        live_source_text="edited text\n",
        closing_repair_attempted=True,
    )

    assert not validate_note(report, repo_root=tmp_path).fails

    edit(report, "closing_status: ready", "closing_status: null")

    result = validate_note(report, repo_root=tmp_path)

    assert has_fail(result, "complete phase requires ready status")


def test_closing_phase_allows_only_one_pending_bounded_repair(tmp_path: Path) -> None:
    install_types(tmp_path)
    report = write_packet(
        tmp_path,
        phase="closing",
        final_text="edited text\n",
        live_source_text="edited text\n",
        closing_status="repair-needed",
    )

    assert not validate_note(report, repo_root=tmp_path).fails

    edit(report, "closing_repair_attempted: false", "closing_repair_attempted: true")

    result = validate_note(report, repo_root=tmp_path)

    assert has_fail(result, "repair-needed is unavailable after the bounded repair")


def test_closing_hand_back_is_valid_but_cannot_be_complete(tmp_path: Path) -> None:
    install_types(tmp_path)
    report = write_packet(
        tmp_path,
        phase="closing",
        final_text="edited text\n",
        closing_status="hand-back",
    )

    assert not validate_note(report, repo_root=tmp_path).fails

    edit(report, "phase: closing", "phase: complete")

    result = validate_note(report, repo_root=tmp_path)

    assert has_fail(result, "complete phase requires ready status")


def test_completed_keep_pass_rejects_a_corrupt_final_capture(tmp_path: Path) -> None:
    install_types(tmp_path)
    report = write_packet(
        tmp_path,
        phase="complete",
        final_text="edited text\n",
        live_source_text="edited text\n",
    )
    (report.parent / "final.txt").write_text("corrupted\n", encoding="utf-8")

    result = validate_note(report, repo_root=tmp_path)

    assert has_fail(result, "final capture")


def test_closing_phase_requires_a_final_capture(tmp_path: Path) -> None:
    install_types(tmp_path)
    report = write_packet(tmp_path, phase="closing")

    result = validate_note(report, repo_root=tmp_path)

    assert has_fail(result, "frontmatter.final_capture")


def test_pending_disposition_must_stay_in_packet_phase(tmp_path: Path) -> None:
    install_types(tmp_path)
    report = write_packet(tmp_path, disposition="delete")
    edit(report, "phase: packet", "phase: editing")

    result = validate_note(report, repo_root=tmp_path)

    assert has_fail(result, "frontmatter.phase", "'packet' was expected")
