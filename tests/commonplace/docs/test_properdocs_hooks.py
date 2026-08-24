from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

from properdocs.structure.files import File, Files, InclusionLevel

from commonplace.docs import properdocs_hooks


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def tag_index(collection: Path, tag: str) -> Path:
    return write(
        collection / f"{tag}-index.md",
        f"""---
description: Index for {tag}
type: kb/types/generated-index.md
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

    result = properdocs_hooks.on_page_markdown("# Example\n\nBody\n", page)

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

    result = properdocs_hooks.on_page_markdown("# Example\n\nBody\n", page)

    assert (
        "**Tags:** [agent-memory](agent-memory-index.md), "
        "[context-engineering](context-engineering-index.md), "
        "[learning-theory](learning-theory-index.md)"
    ) in result


def test_on_page_markdown_appends_generated_tail_to_tag_index(tmp_path: Path) -> None:
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
            "type": "kb/types/generated-index.md",
            "index_source": "tag",
            "index_key": "kb-design",
        },
        file=SimpleNamespace(abs_src_path=str(index)),
    )
    curated_body = "# kb-design\n\n## Notes\n\n- [Curated](curated.md) — placed\n"
    properdocs_hooks.on_config({"docs_dir": str(tmp_path / "kb")})

    result = properdocs_hooks.on_page_markdown(
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
    properdocs_hooks.on_config({"docs_dir": str(tmp_path / "kb")})

    result = properdocs_hooks.on_page_markdown(
        "# kb-design\n\nOrientation.\n",
        page,
        config={"docs_dir": str(tmp_path / "kb")},
    )

    assert "## Other tagged notes <!-- generated -->" in result
    assert "- [Tagged note](./tagged.md) - Tagged note" in result


def test_on_page_markdown_skips_empty_tail_for_complete_readme(tmp_path: Path) -> None:
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
    properdocs_hooks.on_config({"docs_dir": str(tmp_path / "kb")})

    result = properdocs_hooks.on_page_markdown(
        curated_body,
        page,
        config={"docs_dir": str(tmp_path / "kb")},
    )

    # Every member is curated, so no generated section is appended at all
    assert "Other tagged notes" not in result


def test_on_files_publishes_source_index_with_only_published_pages(tmp_path: Path) -> None:
    class Config(dict):
        def __init__(self, docs_dir: Path, site_dir: Path) -> None:
            super().__init__(docs_dir=str(docs_dir))
            self.site_dir = str(site_dir)
            self.use_directory_urls = True
            self.plugins = SimpleNamespace(_current_plugin="test")

    docs_dir = tmp_path / "kb"
    sources = docs_dir / "sources"
    readme = write(sources / "README.md", "# Sources\n")
    collection = write(sources / "COLLECTION.md", "# Sources collection\n")
    ingest = write(sources / "published.ingest.md", "# Published ingest\n")
    snapshot = write(sources / "excluded.md", "# Excluded snapshot\n")
    config = Config(docs_dir, tmp_path / "site")

    def source_file(path: Path, inclusion: InclusionLevel) -> File:
        return File(
            path.relative_to(docs_dir).as_posix(),
            str(docs_dir),
            config.site_dir,
            config.use_directory_urls,
            inclusion=inclusion,
        )

    files = Files(
        [
            source_file(readme, InclusionLevel.INCLUDED),
            source_file(collection, InclusionLevel.INCLUDED),
            source_file(ingest, InclusionLevel.INCLUDED),
            source_file(snapshot, InclusionLevel.EXCLUDED),
        ]
    )

    properdocs_hooks.on_files(files, config)
    generated = files.get_file_from_path("sources/dir-index.md")
    readme_page = SimpleNamespace(
        meta={},
        file=SimpleNamespace(abs_src_path=str(readme)),
    )
    rendered_readme = properdocs_hooks.on_page_markdown(
        "# Sources\n\nBody\n",
        readme_page,
    )

    assert generated is not None
    assert generated.inclusion is InclusionLevel.INCLUDED
    assert "Published ingest" in generated.content_string
    assert "Excluded snapshot" not in generated.content_string
    assert "[Complete file listing](./dir-index.md)" in rendered_readme


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

    result = properdocs_hooks.on_page_markdown("# Example\n\nBody\n", page)

    assert "**Tags:** context-engineering, [learning-theory](learning-theory-index.md)" in result
