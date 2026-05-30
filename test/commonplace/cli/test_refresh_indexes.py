from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from commonplace.cli import refresh_indexes


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


def test_refresh_indexes_rebuilds_directory_and_tag_indexes(
    tmp_path: Path,
    monkeypatch,
) -> None:
    init_git_repo(tmp_path)
    notes_root = tmp_path / "kb" / "notes"
    sources_root = tmp_path / "kb" / "sources"
    write(tmp_path / ".gitignore", "kb/notes/scratch/\nkb/ignored-collection/\n")
    write(notes_root / "COLLECTION.md", "# Notes collection\n")
    write(sources_root / "COLLECTION.md", "# Sources collection\n")
    write(
        tmp_path / "kb" / "ignored-collection" / "COLLECTION.md",
        "# Ignored collection\n",
    )
    write(
        tmp_path / "kb" / "ignored-collection" / "ignored.md",
        "# Ignored collection note\n",
    )
    kb_design_index = write(
        notes_root / "kb-design-index.md",
        """---
description: KB design tag index
type: kb/types/curated-index.md
index_source: tag
index_key: kb-design
status: current
---

# KB design

## Other tagged notes <!-- generated -->
""",
    )
    write(
        notes_root / "example-note.md",
        """---
description: Example note
type: kb/types/note.md
status: current
tags: [kb-design]
---

# Example note
""",
    )
    write(
        notes_root / "scratch" / "ignored-note.md",
        """---
description: Ignored note
type: kb/types/note.md
status: current
tags: [kb-design]
---

# Ignored note
""",
    )
    write(
        notes_root / "dir-index.md",
        """---
description: stale
type: kb/types/dir-index.md
index_source: directory
---

# Old notes directory
""",
    )
    write(
        sources_root / "example-source.md",
        """---
description: Example source
type: source
status: current
---

# Example source
""",
    )
    write(
        sources_root / "dir-index.md",
        """---
description: stale
type: kb/types/dir-index.md
index_source: directory
---

# Old sources directory
""",
    )
    write(
        notes_root / "tags-index.md",
        """---
description: Tags directory
type: kb/types/curated-index.md
index_source: tag-indexes
status: current
---

# Tags

## Other tag indexes <!-- generated -->
""",
    )

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", ["refresh_indexes.py"])

    assert refresh_indexes.main() == 0

    notes_index = (notes_root / "dir-index.md").read_text(encoding="utf-8")
    sources_index = (sources_root / "dir-index.md").read_text(encoding="utf-8")
    tag_index = kb_design_index.read_text(encoding="utf-8")
    tags_directory = (notes_root / "tags-index.md").read_text(encoding="utf-8")

    assert "# Notes Directory" in notes_index
    assert "- [Example note](./example-note.md) *(note)* - Example note" in notes_index
    assert "scratch/" not in notes_index
    assert "Ignored note" not in notes_index
    assert not (notes_root / "scratch" / "dir-index.md").exists()
    assert not (tmp_path / "kb" / "ignored-collection" / "dir-index.md").exists()
    assert "# Sources Directory" in sources_index
    assert (
        "- [Example source](./example-source.md) *(source)* - Example source"
        in sources_index
    )
    assert "- [Example note](./example-note.md) - Example note" in tag_index
    assert "ignored-note.md" not in tag_index
    assert "- [KB design](./kb-design-index.md) - KB design tag index" in tags_directory
