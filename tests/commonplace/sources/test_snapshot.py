from __future__ import annotations

from pathlib import Path

from commonplace.lib.snapshot import (
    dedup_existing_snapshot,
)


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_dedup_existing_snapshot_does_not_match_url_prefixes(tmp_path: Path) -> None:
    write(
        tmp_path / "issue-123.md",
        "---\nsource: https://github.com/o/r/issues/123\n---\n",
    )

    assert dedup_existing_snapshot(tmp_path, "https://github.com/o/r/issues/12") is None
