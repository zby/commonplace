from __future__ import annotations

import shutil
from pathlib import Path

from commonplace.lib.validation import validate_note
from tests.commonplace.lib.test_full_pass import write_packet


def install_types(repo: Path) -> None:
    project_root = Path(__file__).resolve().parents[2]
    shutil.copytree(project_root / "kb/types", repo / "kb/types")
    report_types = repo / "kb/reports/types"
    report_types.mkdir(parents=True)
    for name in ("full-pass-report.md", "full-pass-report.schema.yaml"):
        shutil.copy2(project_root / "kb/reports/types" / name, report_types / name)


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

    assert any("does not match its recorded hash" in item for item in result.fails)


def test_full_pass_type_rule_rejects_resolution_projection_drift(
    tmp_path: Path,
) -> None:
    install_types(tmp_path)
    report = write_packet(tmp_path)
    text = report.read_text(encoding="utf-8").replace(
        "**Status:** not-required", "**Status:** pending"
    )
    report.write_text(text, encoding="utf-8")

    result = validate_note(report, repo_root=tmp_path)

    assert any("resolution projection" in item for item in result.fails)


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

    assert any("headings" in item for item in result.fails)


def test_pending_merge_validates_both_packet_captures(tmp_path: Path) -> None:
    install_types(tmp_path)
    report = write_packet(tmp_path, disposition="merge")

    result = validate_note(report, repo_root=tmp_path)

    assert not result.fails
    assert any("packet captures: all 2" in item for item in result.passes)


def test_terminal_resolution_requires_complete_metadata(tmp_path: Path) -> None:
    install_types(tmp_path)
    report = write_packet(tmp_path, disposition="delete")
    text = report.read_text(encoding="utf-8").replace(
        "resolution: pending", "resolution: accepted", 1
    )
    report.write_text(text, encoding="utf-8")

    result = validate_note(report, repo_root=tmp_path)

    assert any("resolved_at" in item for item in result.fails)
    assert any("resolution_authority" in item for item in result.fails)


def test_keep_report_may_be_superseded_by_version_guard(tmp_path: Path) -> None:
    install_types(tmp_path)
    report = write_packet(tmp_path)
    text = report.read_text(encoding="utf-8")
    text = text.replace(
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
    text = text.replace(
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
    report.write_text(text, encoding="utf-8")

    result = validate_note(report, repo_root=tmp_path)

    assert not result.fails
