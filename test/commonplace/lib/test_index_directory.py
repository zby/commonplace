from __future__ import annotations

from pathlib import Path

from commonplace.lib.index_directory import generate


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
type: note
---

# Real
""",
    )
    write(collection / "README.md", "# Readme\n")
    write(collection / "index.md", "# Old index\n")
    write(collection / "types" / "note.template.md", "# Template\n")

    content = generate(collection)

    assert "- [Real](./real.md) *(note)* - Real note" in content
    assert "README.md" not in content
    assert "note.template.md" not in content
