from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from commonplace.lib.snapshot import (
    DuplicateSnapshotError,
    dedup_existing_snapshot,
    find_snapshot_by_sha256,
    ingest_metadata_from_snapshot,
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


def test_find_snapshot_by_sha256_returns_only_exact_match(tmp_path: Path) -> None:
    match = write(tmp_path / "match.md", "exact bytes\n")
    write(tmp_path / "other.md", "different bytes\n")

    assert find_snapshot_by_sha256(tmp_path, snapshot_sha256(match)) == match.resolve()


def test_find_snapshot_by_sha256_reports_duplicate_paths(tmp_path: Path) -> None:
    first = write(tmp_path / "first.md", "same bytes\n")
    second = write(tmp_path / "second.md", "same bytes\n")

    with pytest.raises(DuplicateSnapshotError) as exc_info:
        find_snapshot_by_sha256(tmp_path, snapshot_sha256(first))

    assert exc_info.value.paths == (first.resolve(), second.resolve())


def test_find_snapshot_by_sha256_rejects_noncanonical_digest(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="64 lowercase hexadecimal"):
        find_snapshot_by_sha256(tmp_path, "A" * 64)


def test_ingest_metadata_projects_capture_fields_and_excludes_snapshot_fields(
    tmp_path: Path,
) -> None:
    snapshot = write(
        tmp_path / "source.md",
        """---
source: https://example.com/source
description: Local retrieval description
captured: "2026-08-22"
capture: gh-api
capture_scope: partial-source
doi: 10.5555/example
genre: github-issue
type: kb/sources/types/snapshot.md
tags: [github-issue]
api_url: https://api.github.com/repos/example/repo/issues/1
issue_number: 1
---

# Source
""",
    )

    assert ingest_metadata_from_snapshot(snapshot) == {
        "source": "https://example.com/source",
        "captured": "2026-08-22",
        "capture": "gh-api",
        "capture_scope": "partial-source",
        "doi": "10.5555/example",
        "api_url": "https://api.github.com/repos/example/repo/issues/1",
        "issue_number": 1,
    }


def test_ingest_metadata_rejects_collision_with_ingest_fields(tmp_path: Path) -> None:
    snapshot = write(
        tmp_path / "source.md",
        """---
source: https://example.com/source
captured: "2026-08-22"
capture: web-fetch
domains: [unexpected]
---
""",
    )

    with pytest.raises(ValueError, match="collides with ingest fields: domains"):
        ingest_metadata_from_snapshot(snapshot)


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
