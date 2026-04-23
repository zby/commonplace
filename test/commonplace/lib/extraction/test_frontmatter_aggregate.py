from __future__ import annotations

import sys
from pathlib import Path


SRC_ROOT = Path(__file__).resolve().parents[5] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.lib.extraction import frontmatter_aggregate  # noqa: E402


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_groups_files_by_field_value(tmp_path: Path) -> None:
    write(tmp_path / "a.md", "---\ntype: kb/types/note.md\n---\n# A\n")
    write(tmp_path / "b.md", "---\ntype: kb/types/note.md\n---\n# B\n")
    write(tmp_path / "c.md", "---\ntype: kb/types/index.md\n---\n# C\n")

    result = frontmatter_aggregate.aggregate_field("type", roots=[tmp_path])

    assert set(result.keys()) == {"kb/types/note.md", "kb/types/index.md"}
    assert len(result["kb/types/note.md"]) == 2
    assert len(result["kb/types/index.md"]) == 1


def test_skips_files_without_frontmatter(tmp_path: Path) -> None:
    write(tmp_path / "no-fm.md", "# No frontmatter\n")
    write(tmp_path / "fm.md", "---\ntype: kb/types/note.md\n---\n# Has\n")

    result = frontmatter_aggregate.aggregate_field("type", roots=[tmp_path])

    assert result == {"kb/types/note.md": [tmp_path / "fm.md"]}


def test_skips_files_missing_field(tmp_path: Path) -> None:
    write(tmp_path / "no-type.md", "---\ndescription: just a desc\n---\n# X\n")

    result = frontmatter_aggregate.aggregate_field("type", roots=[tmp_path])

    assert result == {}


def test_recurses_subdirectories(tmp_path: Path) -> None:
    write(tmp_path / "a" / "b" / "deep.md", "---\nstatus: proposed\n---\n# D\n")
    write(tmp_path / "shallow.md", "---\nstatus: accepted\n---\n# S\n")

    result = frontmatter_aggregate.aggregate_field("status", roots=[tmp_path])

    assert set(result.keys()) == {"proposed", "accepted"}


def test_non_string_values_use_repr(tmp_path: Path) -> None:
    write(tmp_path / "a.md", "---\ntags:\n  - foo\n  - bar\n---\n# A\n")

    result = frontmatter_aggregate.aggregate_field("tags", roots=[tmp_path])

    assert "['foo', 'bar']" in result


def test_skips_symlinks(tmp_path: Path) -> None:
    real = write(tmp_path / "real.md", "---\nstatus: real\n---\n# R\n")
    link = tmp_path / "link.md"
    link.symlink_to(real)

    result = frontmatter_aggregate.aggregate_field("status", roots=[tmp_path])

    assert result == {"real": [real]}


def test_aggregates_across_multiple_roots(tmp_path: Path) -> None:
    root_a = tmp_path / "a"
    root_b = tmp_path / "b"
    write(root_a / "x.md", "---\nstatus: shared\n---\n")
    write(root_b / "y.md", "---\nstatus: shared\n---\n")

    result = frontmatter_aggregate.aggregate_field("status", roots=[root_a, root_b])

    assert len(result["shared"]) == 2
