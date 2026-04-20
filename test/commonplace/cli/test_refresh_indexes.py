from __future__ import annotations

import sys
from pathlib import Path

from commonplace.cli import refresh_indexes


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_refresh_indexes_rebuilds_directory_and_tag_indexes(
    tmp_path: Path,
    monkeypatch,
) -> None:
    notes_root = tmp_path / "kb" / "notes"
    sources_root = tmp_path / "kb" / "sources"
    kb_design_index = write(
        notes_root / "kb-design-index.md",
        """---
description: KB design tag index
type: kb/types/index.md
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
        notes_root / "dir-index.md",
        """---
description: stale
type: kb/types/index.md
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
type: kb/types/index.md
index_source: directory
---

# Old sources directory
""",
    )
    write(
        notes_root / "tags-index.md",
        """---
description: Tags directory
type: kb/types/index.md
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
    assert "# Sources Directory" in sources_index
    assert "- [Example source](./example-source.md) *(source)* - Example source" in sources_index
    assert "- [Example note](./example-note.md) - Example note" in tag_index
    assert "- [KB design](./kb-design-index.md) - KB design tag index" in tags_directory
