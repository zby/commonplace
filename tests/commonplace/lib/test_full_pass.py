from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib.full_pass import (
    guard_full_pass_report,
    load_full_pass_report,
    render_resolution_section,
)
from commonplace.lib.hashing import content_sha256_for_text
from tests.commonplace.validation_helpers import write_packet


def test_matching_report_returns_one_matching_result(tmp_path: Path) -> None:
    report_path = write_packet(tmp_path)

    report = load_full_pass_report(report_path, repo_root=tmp_path)
    results = guard_full_pass_report(report)

    assert [result.status for result in results] == ["matching"]
    assert results[0].capture_sha256 == results[0].current_sha256
    assert results[0].diff is None


def test_changed_report_returns_capture_to_current_diff(tmp_path: Path) -> None:
    report_path = write_packet(tmp_path, live_source_text="edited text\n")

    results = guard_full_pass_report(
        load_full_pass_report(report_path, repo_root=tmp_path)
    )

    assert results[0].status == "changed"
    assert "--- source.txt" in (results[0].diff or "")
    assert "+++ kb/notes/source.md" in (results[0].diff or "")
    assert "-source text" in (results[0].diff or "")
    assert "+edited text" in (results[0].diff or "")


def test_merge_guard_returns_every_result_without_short_circuiting(
    tmp_path: Path,
) -> None:
    report_path = write_packet(
        tmp_path,
        disposition="merge",
        live_target_text="changed target\n",
    )
    (report_path.parent / "source.txt").write_text("corrupt\n", encoding="utf-8")

    results = guard_full_pass_report(
        load_full_pass_report(report_path, repo_root=tmp_path)
    )

    assert [result.role for result in results] == ["source", "merge-target"]
    assert [result.status for result in results] == ["corrupt-capture", "changed"]


def test_missing_live_artifact_is_not_capture_corruption(tmp_path: Path) -> None:
    report_path = write_packet(tmp_path, disposition="delete")
    (tmp_path / "kb/notes/source.md").unlink()

    results = guard_full_pass_report(
        load_full_pass_report(report_path, repo_root=tmp_path)
    )

    assert results[0].status == "missing"
    assert results[0].capture_sha256 == results[0].expected_sha256


def test_rehome_report_parses_as_pending_with_only_the_source_guarded(
    tmp_path: Path,
) -> None:
    report_path = write_packet(tmp_path, disposition="rehome")

    report = load_full_pass_report(report_path, repo_root=tmp_path)

    assert report.disposition == "rehome"
    assert [guarded.role for guarded in report.guarded_inputs] == ["source"]

    results = guard_full_pass_report(report)
    assert [result.status for result in results] == ["matching"]


def test_capture_symlink_is_corrupt_even_when_it_points_inside_packet(
    tmp_path: Path,
) -> None:
    report_path = write_packet(tmp_path)
    capture = report_path.parent / "source.txt"
    real_capture = report_path.parent / "real-source.txt"
    capture.rename(real_capture)
    try:
        capture.symlink_to(real_capture.name)
    except OSError:
        pytest.skip("symlinks unavailable")

    result = guard_full_pass_report(
        load_full_pass_report(report_path, repo_root=tmp_path)
    )[0]

    assert result.status == "corrupt-capture"
    assert result.detail == "capture path contains a symlink"


def test_escaping_capture_path_is_rejected_before_any_read(tmp_path: Path) -> None:
    report_path = write_packet(tmp_path)
    text = report_path.read_text(encoding="utf-8").replace(
        "source_capture: source.txt", "source_capture: ../source.txt"
    )
    report_path.write_text(text, encoding="utf-8")

    with pytest.raises(ValueError, match="packet-relative"):
        load_full_pass_report(report_path, repo_root=tmp_path)


def test_resolution_section_renderer_is_deterministic() -> None:
    rendered = render_resolution_section(
        {
            "resolution": "accepted",
            "resolved_at": "2026-07-13T17:00:00Z",
            "resolution_authority": "user",
            "resolution_summary": "Merged source into target",
            "resolution_rationale": "The target carries the stronger claim",
            "resulting_paths": ["kb/notes/target.md"],
        }
    )

    assert rendered.endswith("**Resulting paths:** `kb/notes/target.md`")
    assert "**Status:** accepted" in rendered


def test_revise_report_parses_as_pending_with_only_the_source_guarded(
    tmp_path: Path,
) -> None:
    report_path = write_packet(tmp_path, disposition="revise")

    report = load_full_pass_report(report_path, repo_root=tmp_path)

    assert report.disposition == "revise"
    assert report.frontmatter["resolution"] == "pending"
    assert [item.role for item in report.guarded_inputs] == ["source"]


def test_final_capture_guards_the_live_source_against_the_text_the_pass_left(
    tmp_path: Path,
) -> None:
    report_path = write_packet(
        tmp_path,
        phase="complete",
        final_text="edited text\n",
        live_source_text="edited text\n",
    )

    report = load_full_pass_report(report_path, repo_root=tmp_path)
    results = guard_full_pass_report(report)

    assert [item.role for item in report.captures] == ["source", "final"]
    assert [item.role for item in report.guarded_inputs] == ["final"]
    assert [result.status for result in results] == ["matching"]


def test_final_capture_refuses_a_source_edited_after_the_pass(
    tmp_path: Path,
) -> None:
    report_path = write_packet(
        tmp_path,
        phase="complete",
        final_text="edited text\n",
        live_source_text="edited again\n",
    )

    report = load_full_pass_report(report_path, repo_root=tmp_path)
    results = guard_full_pass_report(report)

    assert [result.status for result in results] == ["changed"]
    assert results[0].capture_path == "final.txt"


def test_closing_hand_back_guards_the_restored_pass_start_text(
    tmp_path: Path,
) -> None:
    report_path = write_packet(
        tmp_path,
        phase="closing",
        final_text="failed edit\n",
        closing_status="hand-back",
    )

    report = load_full_pass_report(report_path, repo_root=tmp_path)
    results = guard_full_pass_report(report)

    assert report.closing_status == "hand-back"
    assert report.frontmatter["final_capture"] == "source.txt"
    assert [result.status for result in results] == ["matching"]


def test_closing_hand_back_rejects_a_non_source_final_capture(
    tmp_path: Path,
) -> None:
    report_path = write_packet(
        tmp_path,
        phase="closing",
        final_text="failed edit\n",
        closing_status="hand-back",
    )
    text = report_path.read_text(encoding="utf-8").replace(
        "final_capture: source.txt\nfinal_sha256: "
        + content_sha256_for_text("source text\n"),
        "final_capture: final.txt\nfinal_sha256: "
        + content_sha256_for_text("failed edit\n"),
    )
    report_path.write_text(text, encoding="utf-8")

    with pytest.raises(ValueError, match="must point to the pass-start capture"):
        load_full_pass_report(report_path, repo_root=tmp_path)


def test_final_capture_is_rejected_on_a_pending_disposition(tmp_path: Path) -> None:
    report_path = write_packet(tmp_path, disposition="revise")
    text = report_path.read_text(encoding="utf-8").replace(
        "final_capture: null\nfinal_sha256: null",
        "final_capture: final.txt\nfinal_sha256: "
        + content_sha256_for_text("x\n"),
    )
    report_path.write_text(text, encoding="utf-8")

    with pytest.raises(ValueError, match="final capture: expected null"):
        load_full_pass_report(report_path, repo_root=tmp_path)
