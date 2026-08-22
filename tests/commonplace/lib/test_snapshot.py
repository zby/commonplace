from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from commonplace.lib.snapshot import (
    DuplicateSnapshotError,
    SnapshotUnavailableError,
    dedup_existing_snapshot,
    find_snapshot_by_sha256,
    ingest_metadata_from_snapshot,
    resolve_ingest_snapshot,
    snapshot_sha256,
)


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def write_ingest(path: Path, checksum: str) -> Path:
    return write(
        path,
        f"""---
source: https://example.com/source
snapshot_sha256: "{checksum}"
---

# Ingest
""",
    )


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


def test_resolve_ingest_snapshot_uses_exact_local_match_first(tmp_path: Path) -> None:
    snapshot_dir = tmp_path / ".snapshots"
    snapshot = write(snapshot_dir / "source.md", "grounding bytes\n")
    ingest = write_ingest(tmp_path / "source.ingest.md", snapshot_sha256(snapshot))

    def recapture(_source: str) -> Path:
        raise AssertionError("exact cache hit must not recapture")

    result = resolve_ingest_snapshot(ingest, snapshot_dir, recapture=recapture)

    assert result.status == "exact"
    assert result.path == snapshot.resolve()
    assert result.actual_sha256 == result.expected_sha256


def test_resolve_ingest_snapshot_stops_on_duplicate_exact_copies(
    tmp_path: Path,
) -> None:
    snapshot_dir = tmp_path / ".snapshots"
    first = write(snapshot_dir / "first.md", "grounding bytes\n")
    write(snapshot_dir / "second.md", "grounding bytes\n")
    ingest = write_ingest(tmp_path / "source.ingest.md", snapshot_sha256(first))

    with pytest.raises(DuplicateSnapshotError):
        resolve_ingest_snapshot(
            ingest,
            snapshot_dir,
            recapture=lambda _source: (_ for _ in ()).throw(
                AssertionError("duplicates must stop before recapture")
            ),
        )


def test_resolve_ingest_snapshot_installs_exact_recapture(tmp_path: Path) -> None:
    snapshot_dir = tmp_path / ".snapshots"
    candidate = write(tmp_path / "download" / "source.md", "reconstructed\n")
    ingest = write_ingest(tmp_path / "source.ingest.md", snapshot_sha256(candidate))

    result = resolve_ingest_snapshot(
        ingest,
        snapshot_dir,
        recapture=lambda source: candidate
        if source == "https://example.com/source"
        else None,
    )

    assert result.status == "exact"
    assert result.path == (snapshot_dir / "source.md").resolve()
    assert result.path.read_bytes() == candidate.read_bytes()


def test_resolve_ingest_snapshot_exposes_mismatch_without_editing_ingest(
    tmp_path: Path,
) -> None:
    snapshot_dir = tmp_path / ".snapshots"
    expected_file = write(tmp_path / "expected.md", "original bytes\n")
    candidate = write(snapshot_dir / "source.md", "current bytes\n")
    ingest = write_ingest(
        tmp_path / "source.ingest.md", snapshot_sha256(expected_file)
    )
    ingest_before = ingest.read_bytes()

    result = resolve_ingest_snapshot(
        ingest,
        snapshot_dir,
        recapture=lambda _source: candidate,
    )

    assert result.status == "mismatch"
    assert result.actual_sha256 == snapshot_sha256(candidate)
    assert result.actual_sha256 != result.expected_sha256
    assert ingest.read_bytes() == ingest_before


def test_resolve_ingest_snapshot_reports_unavailable_without_adapter(
    tmp_path: Path,
) -> None:
    ingest = write_ingest(tmp_path / "source.ingest.md", "0" * 64)

    result = resolve_ingest_snapshot(ingest, tmp_path / ".snapshots")

    assert result.status == "unavailable"
    assert "no recapture adapter" in (result.detail or "")


def test_resolve_ingest_snapshot_preserves_adapter_unavailable_detail(
    tmp_path: Path,
) -> None:
    ingest = write_ingest(tmp_path / "source.ingest.md", "0" * 64)

    def unavailable(_source: str) -> Path:
        raise SnapshotUnavailableError("upstream returned 404")

    result = resolve_ingest_snapshot(
        ingest,
        tmp_path / ".snapshots",
        recapture=unavailable,
    )

    assert result.status == "unavailable"
    assert result.detail == "upstream returned 404"


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
