from __future__ import annotations

import sys
from pathlib import Path

from commonplace.cli import sync_generated_index
from commonplace.lib import index_generated


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_sync_generated_index_main_dry_run_reports_changes(
    tmp_path: Path,
    monkeypatch,
    capsys,
) -> None:
    notes_root = tmp_path / "kb" / "notes"
    index_path = write(
        notes_root / "kb-design-index.md",
        """---
description: Index page for kb-design notes with a generated section maintained by the sync script
type: index
index_source: tag
index_key: kb-design
traits: []
status: current
---

# KB design index

Curated introduction.
""",
    )
    original = index_path.read_text(encoding="utf-8")
    write(
        notes_root / "example-note.md",
        """---
description: Example note tagged for kb-design so the generated section should report one pending update
type: note
traits: []
status: current
tags: [kb-design]
---

# Example note
""",
    )

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", ["sync_generated_index.py", "--dry-run", str(index_path)])

    sync_generated_index.main()

    captured = capsys.readouterr()
    assert "Would change 1 index(es):" in captured.out
    assert "Would update kb-design-index.md: 1 notes for tag 'kb-design'" in captured.out
    assert index_path.read_text(encoding="utf-8") == original


def test_find_index_files_only_returns_tag_indexes(
    tmp_path: Path,
    monkeypatch,
) -> None:
    notes_root = tmp_path / "kb" / "notes"
    write(
        notes_root / "index.md",
        """---
description: Directory index
type: index
index_source: directory
---

# Notes Directory
""",
    )
    kb_design_index = write(
        notes_root / "kb-design-index.md",
        """---
description: KB design tag index
type: index
index_source: tag
index_key: kb-design
---

# KB design

## Other tagged notes <!-- generated -->
""",
    )
    tags_index = write(
        notes_root / "tags-index.md",
        """---
description: Tags index
type: index
index_source: tag-indexes
---

# Tags

## Other tag indexes <!-- generated -->
""",
    )
    write(
        notes_root / "types" / "index.template.md",
        """---
description: Template
type: index
index_source: tag
index_key: template
---

# Template
""",
    )

    indexes = index_generated.find_index_files([], tmp_path)

    assert indexes == [kb_design_index, tags_index]


def test_sync_generated_index_supports_tag_index_directory(
    tmp_path: Path,
    monkeypatch,
) -> None:
    notes_root = tmp_path / "kb" / "notes"
    tags_index = write(
        notes_root / "tags-index.md",
        """---
description: Tag directory
type: index
index_source: tag-indexes
---

# Tags

## Tag Indexes
- [KB design](./kb-design-index.md) — curated

## Other tag indexes <!-- generated -->
""",
    )
    write(
        notes_root / "kb-design-index.md",
        """---
description: KB design
type: index
index_source: tag
index_key: kb-design
---

# KB design
""",
    )
    write(
        notes_root / "tool-loop-index.md",
        """---
description: Tool loop
type: index
index_source: tag
index_key: tool-loop
---

# Tool loop
""",
    )

    result = index_generated.sync_index(tags_index, {}, tmp_path)
    updated = tags_index.read_text(encoding="utf-8")

    assert result == "  Updated tags-index.md: 2 tag indexes"
    assert "- [KB design](./kb-design-index.md) — curated" in updated
    assert "- [Tool loop](./tool-loop-index.md) - Tool loop" in updated
    assert updated.count("./kb-design-index.md") == 1
