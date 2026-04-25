from __future__ import annotations

from pathlib import Path

from commonplace.lib.index_directory import generate, write_index


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_generate_directory_index_skips_readme_index_and_types(tmp_path: Path) -> None:
    collection = tmp_path / "kb" / "notes"
    write(
        collection / "real.md",
        """---
description: Real note
type: kb/types/note.md
---

# Real
""",
    )
    write(collection / "README.md", "# Readme\n")
    write(collection / "dir-index.md", "# Old dir-index\n")
    write(collection / "types" / "note.template.md", "# Template\n")

    content = generate(collection, parent_link="../index.md")

    assert "- [Real](./real.md) *(note)* - Real note" in content
    assert "README.md" not in content
    assert "dir-index.md" not in content
    assert "note.template.md" not in content
    assert "← [Parent](../index.md)" in content


def test_generate_directory_index_skips_replaced_archives(tmp_path: Path) -> None:
    collection = tmp_path / "kb" / "agent-memory-systems" / "reviews"
    write(
        collection / "current.md",
        """---
description: Current review
type: ../types/agent-memory-system-review.md
---

# Current
""",
    )
    write(
        collection / "current.replaced.2026-04-25.md",
        """---
description: Replaced review
type: ../types/agent-memory-system-review.md
---

# Current
""",
    )

    content = generate(collection, parent_link="../dir-index.md")

    assert "- [Current](./current.md) *(agent-memory-system-review)* - Current review" in content
    assert "current.replaced.2026-04-25.md" not in content
    assert "Replaced review" not in content


def test_write_index_recurses_and_lists_subdirs(tmp_path: Path) -> None:
    collection = tmp_path / "kb" / "reference"
    write(
        collection / "top.md",
        """---
description: Top-level note
type: kb/types/note.md
---

# Top
""",
    )
    write(
        collection / "adr" / "001-some-decision.md",
        """---
description: First decision
type: kb/reference/types/adr.md
---

# 001 Some decision
""",
    )
    # Empty subdir should not get a dir-index
    (collection / "empty").mkdir()
    # types/ subdir should not get a dir-index
    write(collection / "types" / "adr.template.md", "# Template\n")

    output, count = write_index(collection)

    root_index = (collection / "dir-index.md").read_text(encoding="utf-8")
    adr_index = (collection / "adr" / "dir-index.md").read_text(encoding="utf-8")

    # Root lists the subdir entry, not the file inside it
    assert "- [adr/](./adr/dir-index.md)" in root_index
    assert "001-some-decision.md" not in root_index
    assert "- [Top](./top.md) *(note)* - Top-level note" in root_index
    assert "← [Parent](../index.md)" in root_index

    # Subdir index lists its file and points its parent at ../dir-index.md
    assert "- [001 Some decision](./001-some-decision.md) *(adr)* - First decision" in adr_index
    assert "← [Parent](../dir-index.md)" in adr_index

    # Empty and types directories are not indexed
    assert not (collection / "empty" / "dir-index.md").exists()
    assert not (collection / "types" / "dir-index.md").exists()


def test_write_index_max_depth_cleans_stale_subdir_indexes(tmp_path: Path) -> None:
    collection = tmp_path / "kb" / "instructions"
    write(collection / "top.md", "# Top\n")
    write(collection / "skill-foo" / "SKILL.md", "# Foo skill\n")
    # Pre-existing stale dir-index from an earlier unlimited run
    write(collection / "skill-foo" / "dir-index.md", "# Stale\n")

    write_index(collection, max_depth=1)

    root_index = (collection / "dir-index.md").read_text(encoding="utf-8")

    # Root dir-index lists the subdir, but the stale nested dir-index is gone
    assert "- [skill-foo/](" in root_index
    assert not (collection / "skill-foo" / "dir-index.md").exists()
    # Subdir entry falls back to a sensible link target (SKILL.md exists; no
    # README, no dir-index → bare directory URL is acceptable too)
    assert "skill-foo/" in root_index
