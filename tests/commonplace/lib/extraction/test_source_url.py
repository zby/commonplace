from __future__ import annotations

import sys
from pathlib import Path

import pytest


SRC_ROOT = Path(__file__).resolve().parents[5] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.lib.extraction import source_url  # noqa: E402


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


@pytest.mark.parametrize(
    ("content", "expected"),
    [
        (
            "---\nsource: https://example.com/article\ncaptured: 2026-01-01\n---\n# Snap\n",
            "https://example.com/article",
        ),
        ("# Title\n\nSource: https://example.com/post\n", "https://example.com/post"),
        (
            "# Title\n\nSource: [@user on X](https://x.com/user/status/123) (2026-01-01)\n",
            "https://x.com/user/status/123",
        ),
        ("# Title\n\nFrom: https://example.com/from-line\n", "https://example.com/from-line"),
        (
            "# Title\n\nNo source label, just text. Visit https://example.com/article for more.\n",
            "https://example.com/article",
        ),
        ("# Title\n\nSee https://example.com/path.\n", "https://example.com/path"),
        ("# Title\n\nJust some text.\n", None),
        (
            "---\nsource: https://example.com/canonical\n---\n# T\n\nAlso: https://example.com/other\n",
            "https://example.com/canonical",
        ),
    ],
)
def test_extract_url_from_supported_single_file_shapes(
    tmp_path: Path,
    content: str,
    expected: str | None,
) -> None:
    snap = write(tmp_path / "snap.md", content)

    assert source_url.extract_url(snap) == expected


def test_extracts_durable_source_directly_from_ingest(tmp_path: Path) -> None:
    ingest = write(
        tmp_path / "snap.ingest.md",
        "---\ndescription: Ingest\nsource: https://example.com/x\n---\n# Ingest\n",
    )

    assert source_url.extract_url(ingest) == "https://example.com/x"


def test_does_not_follow_retired_source_snapshot_pointer(tmp_path: Path) -> None:
    write(tmp_path / "snap.md", "---\nsource: https://example.com/y\n---\n# Y\n")
    ingest = write(
        tmp_path / "snap.ingest.md",
        "---\nsource_snapshot: snap.md\n---\n# Ingest without a URL\n",
    )

    assert source_url.extract_url(ingest) is None


def test_returns_none_for_missing_file(tmp_path: Path) -> None:
    assert source_url.extract_url(tmp_path / "nonexistent.md") is None
