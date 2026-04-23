from __future__ import annotations

import sys
from pathlib import Path


SRC_ROOT = Path(__file__).resolve().parents[5] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.lib.extraction import source_url  # noqa: E402


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_extract_from_frontmatter_source_field(tmp_path: Path) -> None:
    snap = write(
        tmp_path / "snap.md",
        "---\nsource: https://example.com/article\ncaptured: 2026-01-01\n---\n# Snap\n",
    )
    assert source_url.extract_url(snap) == "https://example.com/article"


def test_follow_source_snapshot_pointer_relative(tmp_path: Path) -> None:
    write(tmp_path / "snap.md", "---\nsource: https://example.com/x\n---\n# X\n")
    ingest = write(
        tmp_path / "snap.ingest.md",
        "---\ndescription: Ingest\nsource_snapshot: snap.md\n---\n# Ingest\n",
    )

    assert source_url.extract_url(ingest) == "https://example.com/x"


def test_follow_source_snapshot_pointer_kb_absolute(tmp_path: Path) -> None:
    write(
        tmp_path / "kb" / "sources" / "snap.md",
        "---\nsource: https://example.com/y\n---\n# Y\n",
    )
    ingest = write(
        tmp_path / "kb" / "sources" / "snap.ingest.md",
        "---\nsource_snapshot: kb/sources/snap.md\n---\n# Ingest\n",
    )

    assert source_url.extract_url(ingest, repo_root=tmp_path) == "https://example.com/y"


def test_extract_from_body_source_line(tmp_path: Path) -> None:
    snap = write(tmp_path / "snap.md", "# Title\n\nSource: https://example.com/post\n")

    assert source_url.extract_url(snap) == "https://example.com/post"


def test_extract_from_body_source_markdown_link(tmp_path: Path) -> None:
    snap = write(
        tmp_path / "snap.md",
        "# Title\n\nSource: [@user on X](https://x.com/user/status/123) (2026-01-01)\n",
    )

    assert source_url.extract_url(snap) == "https://x.com/user/status/123"


def test_extract_from_body_from_line(tmp_path: Path) -> None:
    snap = write(tmp_path / "snap.md", "# Title\n\nFrom: https://example.com/from-line\n")

    assert source_url.extract_url(snap) == "https://example.com/from-line"


def test_extract_from_body_first_url_fallback(tmp_path: Path) -> None:
    snap = write(
        tmp_path / "snap.md",
        "# Title\n\nNo source label, just text. Visit https://example.com/article for more.\n",
    )

    assert source_url.extract_url(snap) == "https://example.com/article"


def test_returns_none_when_no_url_anywhere(tmp_path: Path) -> None:
    snap = write(tmp_path / "snap.md", "# Title\n\nJust some text.\n")

    assert source_url.extract_url(snap) is None


def test_returns_none_for_missing_file(tmp_path: Path) -> None:
    assert source_url.extract_url(tmp_path / "nonexistent.md") is None


def test_handles_cycle_in_source_snapshot_pointers(tmp_path: Path) -> None:
    write(tmp_path / "a.md", "---\nsource_snapshot: b.md\n---\n# A no url\n")
    write(tmp_path / "b.md", "---\nsource_snapshot: a.md\n---\n# B no url\n")

    assert source_url.extract_url(tmp_path / "a.md") is None


def test_strips_trailing_punctuation(tmp_path: Path) -> None:
    snap = write(
        tmp_path / "snap.md",
        "# Title\n\nSee https://example.com/path.\n",
    )
    assert source_url.extract_url(snap) == "https://example.com/path"


def test_prefers_frontmatter_source_over_body_url(tmp_path: Path) -> None:
    snap = write(
        tmp_path / "snap.md",
        "---\nsource: https://example.com/canonical\n---\n# T\n\nAlso: https://example.com/other\n",
    )
    assert source_url.extract_url(snap) == "https://example.com/canonical"
