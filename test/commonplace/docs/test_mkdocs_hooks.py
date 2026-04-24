from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

from commonplace.docs import mkdocs_hooks


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def tag_index(collection: Path, tag: str) -> Path:
    return write(
        collection / f"{tag}-index.md",
        f"""---
description: Index for {tag}
type: kb/types/index.md
index_source: tag
index_key: {tag}
---

# {tag}
""",
    )


def test_on_page_markdown_links_every_tag_with_declared_index(tmp_path: Path) -> None:
    notes = tmp_path / "kb" / "notes"
    for tag in ("agent-memory", "context-engineering", "learning-theory"):
        tag_index(notes, tag)
    note = write(notes / "example.md", "# Example\n")
    page = SimpleNamespace(
        meta={
            "type": "kb/types/note.md",
            "tags": ["agent-memory", "context-engineering", "learning-theory"],
        },
        file=SimpleNamespace(abs_src_path=str(note)),
    )

    result = mkdocs_hooks.on_page_markdown("# Example\n\nBody\n", page)

    assert (
        "**Tags:** [agent-memory](agent-memory-index.md), "
        "[context-engineering](context-engineering-index.md), "
        "[learning-theory](learning-theory-index.md)"
    ) in result


def test_on_page_markdown_keeps_unindexed_tags_as_text(tmp_path: Path) -> None:
    notes = tmp_path / "kb" / "notes"
    tag_index(notes, "learning-theory")
    note = write(notes / "example.md", "# Example\n")
    page = SimpleNamespace(
        meta={
            "type": "kb/types/note.md",
            "tags": ["context-engineering", "learning-theory"],
        },
        file=SimpleNamespace(abs_src_path=str(note)),
    )

    result = mkdocs_hooks.on_page_markdown("# Example\n\nBody\n", page)

    assert "**Tags:** context-engineering, [learning-theory](learning-theory-index.md)" in result
