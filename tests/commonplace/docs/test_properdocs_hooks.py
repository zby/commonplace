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


def test_on_page_markdown_renders_user_verification_and_specialized_status(tmp_path: Path) -> None:
    note = write(tmp_path / "kb" / "reference" / "adr" / "044-example.md", "# Example\n")
    page = SimpleNamespace(
        meta={
            "type": "kb/reference/types/adr.md",
            "status": "accepted",
            "user-verified": True,
        },
        file=SimpleNamespace(abs_src_path=str(note)),
    )

    result = mkdocs_hooks.on_page_markdown("# Example\n\nBody\n", page)

    assert "**Status:** accepted" in result
    assert "**User verified:** yes" in result


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


def test_on_page_markdown_appends_generated_tail_to_tag_index(tmp_path: Path) -> None:
    mkdocs_hooks._notes_by_tag.cache_clear()
    notes = tmp_path / "kb" / "notes"
    write(notes / "COLLECTION.md", "# Notes collection\n")
    index = tag_index(notes, "kb-design")
    write(
        notes / "tagged.md",
        """---
description: Tagged note
type: kb/types/note.md
tags: [kb-design]
---

# Tagged note
""",
    )
    write(
        notes / "curated.md",
        """---
description: Already curated note
type: kb/types/note.md
tags: [kb-design]
---

# Curated note
""",
    )
    page = SimpleNamespace(
        meta={
            "type": "kb/types/index.md",
            "index_source": "tag",
            "index_key": "kb-design",
        },
        file=SimpleNamespace(abs_src_path=str(index)),
    )
    curated_body = "# kb-design\n\n## Notes\n\n- [Curated](curated.md) — placed\n"

    result = mkdocs_hooks.on_page_markdown(
        curated_body,
        page,
        config={"docs_dir": str(tmp_path / "kb")},
    )

    assert "## Other tagged notes <!-- generated -->" in result
    assert "- [Tagged note](./tagged.md) - Tagged note" in result
    # Curated links are excluded from the generated tail
    assert result.count("curated.md") == 1
    assert "- [Curated note](./curated.md)" not in result


def test_on_page_markdown_appends_tail_to_tag_readme_type(tmp_path: Path) -> None:
    mkdocs_hooks._notes_by_tag.cache_clear()
    notes = tmp_path / "kb" / "notes"
    write(notes / "COLLECTION.md", "# Notes collection\n")
    readme = write(
        notes / "kb-design-README.md",
        """---
description: "Curated head for kb-design"
type: kb/types/tag-readme.md
index_source: tag
index_key: kb-design
---

# kb-design
""",
    )
    write(
        notes / "tagged.md",
        """---
description: Tagged note
type: kb/types/note.md
tags: [kb-design]
---

# Tagged note
""",
    )
    page = SimpleNamespace(
        meta={
            "type": "kb/types/tag-readme.md",
            "index_source": "tag",
            "index_key": "kb-design",
        },
        file=SimpleNamespace(abs_src_path=str(readme)),
    )

    result = mkdocs_hooks.on_page_markdown(
        "# kb-design\n\nOrientation.\n",
        page,
        config={"docs_dir": str(tmp_path / "kb")},
    )

    assert "## Other tagged notes <!-- generated -->" in result
    assert "- [Tagged note](./tagged.md) - Tagged note" in result


def test_on_page_markdown_skips_empty_tail_for_complete_readme(tmp_path: Path) -> None:
    mkdocs_hooks._notes_by_tag.cache_clear()
    notes = tmp_path / "kb" / "notes"
    write(notes / "COLLECTION.md", "# Notes collection\n")
    readme = write(
        notes / "kb-design-README.md",
        """---
description: "Curated head for kb-design"
type: kb/types/tag-readme.md
index_source: tag
index_key: kb-design
complete: true
---

# kb-design
""",
    )
    write(
        notes / "curated.md",
        """---
description: Curated note
type: kb/types/note.md
tags: [kb-design]
---

# Curated note
""",
    )
    page = SimpleNamespace(
        meta={
            "type": "kb/types/tag-readme.md",
            "index_source": "tag",
            "index_key": "kb-design",
            "complete": True,
        },
        file=SimpleNamespace(abs_src_path=str(readme)),
    )
    curated_body = "# kb-design\n\n- [Curated](./curated.md) — placed\n"

    result = mkdocs_hooks.on_page_markdown(
        curated_body,
        page,
        config={"docs_dir": str(tmp_path / "kb")},
    )

    # Every member is curated, so no generated section is appended at all
    assert "Other tagged notes" not in result


def test_on_page_markdown_links_collection_readme_to_dir_index(tmp_path: Path) -> None:
    notes = tmp_path / "kb" / "notes"
    readme = write(notes / "README.md", "# Notes\n")
    mkdocs_hooks._generated_index_dirs.add(notes)
    try:
        page = SimpleNamespace(
            meta={},
            file=SimpleNamespace(abs_src_path=str(readme)),
        )
        result = mkdocs_hooks.on_page_markdown("# Notes\n\nBody\n", page)
    finally:
        mkdocs_hooks._generated_index_dirs.discard(notes)

    assert "[Complete file listing](./dir-index.md)" in result


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
