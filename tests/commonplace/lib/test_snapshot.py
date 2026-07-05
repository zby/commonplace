from __future__ import annotations

from pathlib import Path

from commonplace.lib.snapshot import dedup_existing_snapshot


def test_dedup_existing_snapshot_returns_matching_markdown_snapshot(tmp_path: Path) -> None:
    source_url = "https://example.com/source"
    match = tmp_path / "source.md"
    match.write_text(
        f"---\nsource: {source_url}\n---\n\n# Source\n",
        encoding="utf-8",
    )
    (tmp_path / "other.md").write_text("---\nsource: https://example.com/other\n---\n", encoding="utf-8")

    assert dedup_existing_snapshot(tmp_path, source_url) == match


def test_dedup_existing_snapshot_ignores_non_matching_snapshots(tmp_path: Path) -> None:
    (tmp_path / "other.md").write_text("---\nsource: https://example.com/other\n---\n", encoding="utf-8")

    assert dedup_existing_snapshot(tmp_path, "https://example.com/source") is None


def test_dedup_existing_snapshot_does_not_match_url_prefixes(tmp_path: Path) -> None:
    (tmp_path / "issue-123.md").write_text(
        "---\nsource: https://github.com/o/r/issues/123\n---\n",
        encoding="utf-8",
    )

    assert dedup_existing_snapshot(tmp_path, "https://github.com/o/r/issues/12") is None
