from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib.full_pass import (
    guard_full_pass_report,
    load_full_pass_report,
    render_resolution_section,
)
from commonplace.lib.hashing import content_sha256_for_text


def write_packet(
    root: Path,
    *,
    source_text: str = "source text\n",
    live_source_text: str | None = None,
    disposition: str = "keep",
    target_text: str = "target text\n",
    live_target_text: str | None = None,
) -> Path:
    source = root / "kb/notes/source.md"
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text(
        source_text if live_source_text is None else live_source_text,
        encoding="utf-8",
    )

    packet = root / "kb/reports/full-pass/source/pass-1"
    packet.mkdir(parents=True)
    (packet / "source.txt").write_text(source_text, encoding="utf-8")

    if disposition == "merge":
        target = root / "kb/notes/target.md"
        target.write_text(
            target_text if live_target_text is None else live_target_text,
            encoding="utf-8",
        )
        (packet / "merge-target.txt").write_text(target_text, encoding="utf-8")
        merge_fields = f"""merge_target: kb/notes/target.md
merge_target_capture: merge-target.txt
merge_target_title: Target
merge_target_sha256: {content_sha256_for_text(target_text)}"""
        resolution = "pending"
    else:
        merge_fields = """merge_target: null
merge_target_capture: null
merge_target_title: null
merge_target_sha256: null"""
        resolution = "not-required" if disposition == "keep" else "pending"

    report = packet / "full-pass-report.md"
    report.write_text(
        f"""---
description: Full improvement pass fixture with packet-owned captures for testing
type: kb/reports/types/full-pass-report.md
source: kb/notes/source.md
source_capture: source.txt
source_sha256: {content_sha256_for_text(source_text)}
pass_id: pass-1
disposition: {disposition}
{merge_fields}
resolution: {resolution}
resolved_at: null
resolution_authority: null
resolution_summary: null
resolution_rationale: null
resulting_paths: []
---

# Full Improvement Pass: Source

## Resolution

**Status:** {resolution}
**Resolved at:** —
**Authority:** —
**Outcome:** —
**Rationale:** —
**Resulting paths:** —
""",
        encoding="utf-8",
    )
    return report


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
