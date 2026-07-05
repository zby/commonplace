"""MkDocs hooks: metadata badge, collection nav, build-time generated listings.

Complete generated listings (per-collection dir-index pages and per-tag
generated tails) are materialized here at build time for the published site;
they are never committed (ADR 025). Agents use curated heads plus scoped rg.
"""

import os
import re
from functools import cache
from pathlib import Path

from mkdocs.structure.files import File

from commonplace.lib import frontmatter, index_directory, index_generated
from commonplace.lib.project_paths import collection_dirs, collection_for_path

INDEX_TYPE = "kb/types/index.md"
# Page types that act as a tag's landing: the committed tag-readme (ADR 026)
# and the index type (build-time virtual pages, unmigrated indexes).
TAG_PAGE_TYPES = {INDEX_TYPE, "kb/types/tag-readme.md"}

# Recursion caps for per-collection dir-index generation. instructions stops
# at one level because each cp-skill-* subdir is essentially a single SKILL.md
# and the review-gates/ tree is a deep but flat catalog of gate definitions.
COLLECTION_MAX_DEPTH = {"instructions": 1}

# Directories that received a virtual dir-index page in on_files, so
# on_page_markdown can link each collection README to its full listing.
_generated_index_dirs: set[Path] = set()


def on_config(config):
    """Generate top-level nav from kb/<collection>/README.md files.

    Any directory directly under docs_dir containing a README.md becomes a
    top-nav entry pointing at that README. Discovery is alphabetical;
    fixed Home and external entries bracket the auto-discovered list.
    """
    _index_metadata.cache_clear()
    _notes_by_tag.cache_clear()
    docs_dir = Path(config["docs_dir"])
    collection_entries = []
    for child in sorted(docs_dir.iterdir()):
        if not child.is_dir() or child.name.startswith("."):
            continue
        readme = child / "README.md"
        if not readme.exists():
            continue
        label = child.name.replace("-", " ").title()
        collection_entries.append({label: str(readme.relative_to(docs_dir))})

    # TODO: read external links (Recent Changes, GitHub, etc.) from mkdocs.yml
    # so consuming projects don't have to fork this hook to change them.
    config["nav"] = [
        {"Home": "index.md"},
        *collection_entries,
        {"Recent Changes": "https://github.com/zby/commonplace/commits/main/"},
        {"GitHub": "https://github.com/zby/commonplace"},
    ]
    return config


def on_files(files, config):
    """Add per-collection dir-index pages as build-time virtual files.

    Content comes from the same lib generation the retired
    commonplace-refresh-indexes command used, but stays in memory: the pages
    exist only in the built site. A stale on-disk dir-index.md (gitignored
    leftover) is replaced by the generated version.
    """
    _generated_index_dirs.clear()
    docs_dir = Path(config["docs_dir"]).resolve()
    root = docs_dir.parent

    for collection in collection_dirs(root):
        if collection.name == "reports":
            continue
        pages = index_directory.collect_index_pages(
            collection,
            max_depth=COLLECTION_MAX_DEPTH.get(collection.name),
        )
        for output_path, content in pages:
            src_uri = output_path.relative_to(docs_dir).as_posix()
            stale = files.get_file_from_path(src_uri)
            if stale is not None:
                files.remove(stale)
            files.append(File.generated(config, src_uri, content=content))
            _generated_index_dirs.add(output_path.parent)

    return files


@cache
def _notes_by_tag(collection: Path) -> dict[str, list[tuple[Path, str, str]]]:
    """Per-build cache of one tag scan per collection."""
    return index_generated.collect_notes_by_tag(collection)


@cache
def _index_metadata(candidate: Path) -> tuple[str | None, str | None, str | None]:
    """Return index-related frontmatter for a markdown page."""
    if not candidate.is_file() or candidate.suffix != ".md":
        return (None, None, None)
    content = candidate.read_text(encoding="utf-8")
    fm = frontmatter.parse(content).data
    return (fm.get("type"), fm.get("index_source"), fm.get("index_key"))


def _matches_tag_index(candidate: Path, tag: str) -> bool:
    """Return True when a page declares itself as the landing for a tag."""
    note_type, index_source, index_key = _index_metadata(candidate)
    return note_type in TAG_PAGE_TYPES and index_source == "tag" and index_key == tag


def _find_tag_index(tag: str, note_dir: Path) -> str | None:
    """Find relative path from note_dir to the declared index page for a tag."""
    search_dir = note_dir.resolve()
    note_dir_resolved = note_dir.resolve()

    for _ in range(4):
        if search_dir.is_dir():
            for candidate in sorted(search_dir.glob("*.md")):
                if _matches_tag_index(candidate, tag):
                    return os.path.relpath(candidate, note_dir_resolved)
            for subdir in sorted(search_dir.iterdir()):
                if not subdir.is_dir() or subdir.name.startswith("."):
                    continue
                for candidate in sorted(subdir.glob("*.md")):
                    if _matches_tag_index(candidate, tag):
                        return os.path.relpath(candidate, note_dir_resolved)

        search_dir = search_dir.parent

    return None


def _append_generated_tail(markdown: str, page, config) -> str:
    """Append the generated listing to tag / tag-indexes pages at build time."""
    meta = page.meta or {}
    source = meta.get("index_source")
    if (
        meta.get("type") not in TAG_PAGE_TYPES
        or source not in index_generated.GENERATED_HEADING_BY_SOURCE
        or config is None
        or page.file.abs_src_path is None
    ):
        return markdown

    docs_dir = Path(config["docs_dir"]).resolve()
    root = docs_dir.parent
    page_path = Path(page.file.abs_src_path)
    section = index_generated.generated_section_for_index(
        page_path,
        source=source,
        index_key=meta.get("index_key"),
        curated_text=markdown,
        root=root,
        notes_by_tag=_notes_by_tag(collection_for_path(page_path, root))
        if source == "tag"
        else None,
    )
    # A complete-marked README curates every member, leaving the generated
    # section as a bare heading — skip it rather than render an empty shell.
    if not section or "\n- " not in section:
        return markdown
    return markdown.rstrip("\n") + "\n\n" + section


def _append_full_listing_link(markdown: str, page) -> str:
    """Link a collection README to its build-time dir-index sibling."""
    abs_src_path = page.file.abs_src_path
    if abs_src_path is None:  # generated virtual file
        return markdown
    page_path = Path(abs_src_path)
    if page_path.name != "README.md" or page_path.parent not in _generated_index_dirs:
        return markdown
    return (
        markdown.rstrip("\n")
        + "\n\n---\n\n[Complete file listing](./dir-index.md) *(generated at build time)*\n"
    )


def on_page_markdown(markdown: str, page, config=None, **kwargs) -> str:
    meta = page.meta or {}

    if meta:
        markdown = _append_generated_tail(markdown, page, config)
    markdown = _append_full_listing_link(markdown, page)

    status = meta.get("status")
    note_type = meta.get("type")
    tags = meta.get("tags", [])
    if not status and not note_type and not tags:
        return markdown

    parts = []
    if note_type:
        parts.append(f"**Type:** {note_type}")
    if status:
        parts.append(f"**Status:** {status}")

    if tags:
        note_dir = Path(page.file.abs_src_path).parent
        tag_links = []
        for tag in tags:
            relpath = _find_tag_index(tag, note_dir)
            if relpath:
                tag_links.append(f"[{tag}]({relpath})")
            else:
                tag_links.append(tag)
        parts.append(f"**Tags:** {', '.join(tag_links)}")

    badge_line = " · ".join(parts)

    # Insert after the first heading
    return re.sub(
        r"(^# .+\n)",
        rf"\1\n{badge_line}\n",
        markdown,
        count=1,
        flags=re.MULTILINE,
    )
