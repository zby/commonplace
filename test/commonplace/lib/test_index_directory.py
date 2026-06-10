from __future__ import annotations

import subprocess
from pathlib import Path

from commonplace.lib.index_directory import collect_index_pages, generate


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def init_git_repo(path: Path) -> None:
    subprocess.run(
        ["git", "init"],
        cwd=path,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


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

    assert (
        "- [Current](./current.md) *(agent-memory-system-review)* - Current review"
        in content
    )
    assert "current.replaced.2026-04-25.md" not in content
    assert "Replaced review" not in content


def as_dict(pages: list[tuple[Path, str]]) -> dict[Path, str]:
    return dict(pages)


def test_collect_index_pages_recurses_and_lists_subdirs(tmp_path: Path) -> None:
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

    pages = as_dict(collect_index_pages(collection))

    root_index = pages[collection / "dir-index.md"]
    adr_index = pages[collection / "adr" / "dir-index.md"]

    # Root lists the subdir entry, not the file inside it
    assert "- [adr/](./adr/dir-index.md)" in root_index
    assert "001-some-decision.md" not in root_index
    assert "- [Top](./top.md) *(note)* - Top-level note" in root_index
    assert "← [Parent](../index.md)" in root_index

    # Subdir index lists its file and points its parent at ../dir-index.md
    assert (
        "- [001 Some decision](./001-some-decision.md) *(adr)* - First decision"
        in adr_index
    )
    assert "← [Parent](../dir-index.md)" in adr_index

    # Empty and types directories are not indexed, and nothing touched disk
    assert collection / "empty" / "dir-index.md" not in pages
    assert collection / "types" / "dir-index.md" not in pages
    assert not (collection / "dir-index.md").exists()


def test_collect_index_pages_max_depth_skips_nested_indexes(tmp_path: Path) -> None:
    collection = tmp_path / "kb" / "instructions"
    write(collection / "top.md", "# Top\n")
    write(collection / "skill-foo" / "SKILL.md", "# Foo skill\n")

    pages = as_dict(collect_index_pages(collection, max_depth=1))

    root_index = pages[collection / "dir-index.md"]

    # Root dir-index lists the subdir, but no nested dir-index is generated
    assert collection / "skill-foo" / "dir-index.md" not in pages
    # Subdir entry falls back to a sensible link target (SKILL.md exists; no
    # README, no dir-index → the sole markdown file)
    assert "- [skill-foo/](./skill-foo/SKILL.md)" in root_index


def test_collect_index_pages_prunes_gitignored_directories(tmp_path: Path) -> None:
    init_git_repo(tmp_path)
    write(tmp_path / ".gitignore", "kb/reference/generated/\n")
    collection = tmp_path / "kb" / "reference"
    write(
        collection / "kept.md",
        """---
description: Kept note
type: kb/types/note.md
---

# Kept
""",
    )
    write(
        collection / "generated" / "ignored.md",
        """---
description: Ignored note
type: kb/types/note.md
---

# Ignored
""",
    )
    pages = as_dict(collect_index_pages(collection, ignore_root=tmp_path))

    root_index = pages[collection / "dir-index.md"]

    assert "- [Kept](./kept.md) *(note)* - Kept note" in root_index
    assert "generated/" not in root_index
    assert "Ignored note" not in root_index
    assert collection / "generated" / "dir-index.md" not in pages
