from __future__ import annotations

import hashlib
from pathlib import Path

from commonplace.lib.snapshot import (
    dedup_existing_snapshot,
    snapshot_sha256,
)


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_snapshot_sha256_hashes_exact_file_bytes(tmp_path: Path) -> None:
    snapshot = tmp_path / "source.md"
    snapshot.write_bytes(b"line one\r\nline two")

    assert snapshot_sha256(snapshot) == hashlib.sha256(
        b"line one\r\nline two"
    ).hexdigest()

    snapshot.write_bytes(b"line one\r\nline two\n")
    assert snapshot_sha256(snapshot) == hashlib.sha256(
        b"line one\r\nline two\n"
    ).hexdigest()


def test_dedup_existing_snapshot_returns_matching_markdown_snapshot(tmp_path: Path) -> None:
    source_url = "https://example.com/source"
    match = write(
        tmp_path / "source.md",
        f"---\nsource: {source_url}\n---\n\n# Source\n",
    )
    write(
        tmp_path / "other.md",
        "---\nsource: https://example.com/other\n---\n",
    )

    assert dedup_existing_snapshot(tmp_path, source_url) == match


def test_dedup_existing_snapshot_ignores_non_matching_snapshots(tmp_path: Path) -> None:
    write(
        tmp_path / "other.md",
        "---\nsource: https://example.com/other\n---\n",
    )

    assert dedup_existing_snapshot(tmp_path, "https://example.com/source") is None


def test_dedup_existing_snapshot_does_not_match_url_prefixes(tmp_path: Path) -> None:
    write(
        tmp_path / "issue-123.md",
        "---\nsource: https://github.com/o/r/issues/123\n---\n",
    )

    assert dedup_existing_snapshot(tmp_path, "https://github.com/o/r/issues/12") is None


def test_reobservation_slug_appends_the_capture_date_within_the_limit() -> None:
    from datetime import date

    from commonplace.lib.snapshot import reobservation_slug

    assert reobservation_slug("paper-x", date(2026, 9, 25), 40) == "paper-x-20260925"
    long = reobservation_slug("a" * 50, date(2026, 9, 25), 40)
    assert len(long) == 40 and long.endswith("-20260925")
