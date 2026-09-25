"""ProperDocs hooks: metadata badge, collection nav, build-time generated listings.

Complete generated listings (per-collection dir-index pages and per-tag
generated tails) are materialized here at build time for the published site;
they are never committed (ADR 025). Agents use curated heads plus scoped rg.
Tag pages are the heads in kb/tags/ (ADR 089); a tail lists every member
across the participating collections.
"""

import os
import re
from functools import cache
from pathlib import Path

from properdocs.structure.files import File, InclusionLevel

from commonplace.lib import index_directory, index_generated
from commonplace.lib.project_paths import collection_dirs

# Recursion caps for per-collection dir-index generation. instructions stops
# at one level because each cp-skill-* subdir is essentially a single SKILL.md
# and the review-gates/ tree is a deep but flat catalog of gate definitions.
COLLECTION_MAX_DEPTH = {"instructions": 1}

# Operational collections can require a local contract and landing without
# becoming part of the public documentation surface.
UNPUBLISHED_COLLECTIONS = frozenset({"reports"})

# Directories that received a virtual dir-index page in on_files, so
# on_page_markdown can link each collection README to its full listing.
_generated_index_dirs: set[Path] = set()


def on_config(config):
    """Generate top-level nav from kb/<collection>/README.md files.

    Any directory directly under docs_dir containing a README.md becomes a
    top-nav entry pointing at that README. Discovery is alphabetical;
    fixed Home and external entries bracket the auto-discovered list.
    """
    _tag_space.cache_clear()
    docs_dir = Path(config["docs_dir"])
    collection_entries = []
    for child in sorted(docs_dir.iterdir()):
        if not child.is_dir() or child.name.startswith("."):
            continue
        if child.name in UNPUBLISHED_COLLECTIONS:
            continue
        readme = child / "README.md"
        if not readme.exists():
            continue
        label = child.name.replace("-", " ").title()
        collection_entries.append({label: str(readme.relative_to(docs_dir))})

    # TODO: read external links (Recent Changes, GitHub, etc.) from properdocs.yml
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
    published_paths = {
        Path(file.abs_src_path).resolve()
        for file in files.documentation_pages()
        if file.abs_src_path is not None
    }

    for collection in collection_dirs(root):
        if collection.name in UNPUBLISHED_COLLECTIONS:
            continue
        pages = index_directory.collect_index_pages(
            collection,
            max_depth=COLLECTION_MAX_DEPTH.get(collection.name),
            include=lambda path: path.resolve() in published_paths,
        )
        for output_path, content in pages:
            src_uri = output_path.relative_to(docs_dir).as_posix()
            stale = files.get_file_from_path(src_uri)
            if stale is not None:
                files.remove(stale)
            files.append(
                File.generated(
                    config,
                    src_uri,
                    content=content,
                    inclusion=InclusionLevel.INCLUDED,
                )
            )
            _generated_index_dirs.add(output_path.parent)

    return files


@cache
def _tag_space(root: Path) -> index_generated.TagSpace:
    """Per-build cache of one tag-space scan."""
    return index_generated.collect_tag_space(root)


def _root_for(config) -> Path | None:
    if config is None:
        return None
    return Path(config["docs_dir"]).resolve().parent


def _is_head(page_path: Path, meta: dict, root: Path) -> bool:
    return (
        meta.get("type") == index_generated.TAG_README_TYPE
        and page_path.resolve().parent == index_generated.tags_collection(root).resolve()
        and index_generated.tag_for_head(page_path) is not None
    )


def _append_generated_tail(markdown: str, page, config) -> str:
    """Append the generated member listing to a tag head at build time."""
    meta = page.meta or {}
    root = _root_for(config)
    if root is None or page.file.abs_src_path is None:
        return markdown
    page_path = Path(page.file.abs_src_path)
    if not _is_head(page_path, meta, root):
        return markdown

    section = index_generated.generated_section_for_head(
        page_path, curated_text=markdown, tag_space=_tag_space(root)
    )
    # A complete-marked head curates every member, leaving the generated
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


def _tag_link(tag: str, note_dir: Path, root: Path | None) -> str:
    """Link a tag to its head when the head exists; otherwise plain text."""
    if root is not None:
        head = _tag_space(root).heads.get(tag)
        if head is not None:
            return f"[{tag}]({os.path.relpath(head, note_dir.resolve())})"
    return tag


def on_page_markdown(markdown: str, page, config=None, **kwargs) -> str:
    meta = page.meta or {}

    if meta:
        markdown = _append_generated_tail(markdown, page, config)
    markdown = _append_full_listing_link(markdown, page)

    status = meta.get("status")
    user_verified = meta.get("user-verified") is True
    note_type = meta.get("type")
    tags = meta.get("tags", [])
    if not status and not user_verified and not note_type and not tags:
        return markdown

    parts = []
    if note_type:
        parts.append(f"**Type:** {note_type}")
    if status:
        parts.append(f"**Status:** {status}")
    if user_verified:
        parts.append("**User verified:** yes")

    if tags:
        note_dir = Path(page.file.abs_src_path).parent
        root = _root_for(config)
        parts.append(
            "**Tags:** " + ", ".join(_tag_link(tag, note_dir, root) for tag in tags)
        )

    badge_line = " · ".join(parts)

    # Insert after the first heading
    return re.sub(
        r"(^# .+\n)",
        rf"\1\n{badge_line}\n",
        markdown,
        count=1,
        flags=re.MULTILINE,
    )
