"""Rebuild generated sections of index pages."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

from commonplace.lib import frontmatter
from commonplace.lib.note_parser import extract_title, strip_frontmatter
from commonplace.lib.project_paths import (
    collection_for_path,
    is_replaced_archive,
    is_type_definition_content,
    iter_unignored_markdown_files,
)


FIELD_NAME = "tags"
MARKER = "<!-- generated -->"
INDEX_TYPE = "kb/types/index.md"
TAG_README_TYPE = "kb/types/tag-readme.md"
# Page types that carry index_source/index_key and receive a build-time
# generated listing. INDEX_TYPE remains for build-time virtual pages and
# unmigrated indexes; TAG_README_TYPE is the committed curated head (ADR 026).
TAG_PAGE_TYPES = {INDEX_TYPE, TAG_README_TYPE}
GENERATED_HEADING_BY_SOURCE = {
    "tag": "## Other tagged notes",
    "tag-indexes": "## Other tag indexes",
}


def collect_notes_by_tag(
    collection_dir: Path,
) -> dict[str, list[tuple[Path, str, str]]]:
    """Scan a collection and group notes by tag."""
    by_tag: dict[str, list[tuple[Path, str, str]]] = {}

    for path in sorted(iter_unignored_markdown_files(collection_dir)):
        if is_replaced_archive(path):
            continue
        content = path.read_text(encoding="utf-8")
        fm = frontmatter.parse(content).data

        if fm.get("type") in TAG_PAGE_TYPES:
            continue
        rel_parts = path.relative_to(collection_dir).parts
        if "types" in rel_parts or ".collection" in rel_parts:
            continue

        tags = fm.get(FIELD_NAME, [])
        if not tags:
            continue

        title = extract_title(strip_frontmatter(content))
        desc = fm.get("description", "")

        for tag in tags:
            by_tag.setdefault(tag, []).append((path, title, desc))

    return by_tag


def index_frontmatter(path: Path, content: str | None = None) -> dict[str, Any]:
    """Parse frontmatter for an index candidate."""
    if content is None:
        content = path.read_text(encoding="utf-8")
    return frontmatter.parse(content).data


def index_source(path: Path, root: Path, content: str | None = None) -> str | None:
    """Return the declared generated-section source for a managed index."""
    collection = collection_for_path(path, root)
    rel_parts = path.relative_to(collection).parts

    if is_replaced_archive(path):
        return None
    if is_type_definition_content(path, collection) or ".collection" in rel_parts:
        return None
    fm = index_frontmatter(path, content)
    if fm.get("type") not in TAG_PAGE_TYPES:
        return None
    source = fm.get("index_source")
    if source in GENERATED_HEADING_BY_SOURCE:
        return str(source)
    return None


def collect_tag_index_entries(
    collection_dir: Path, root: Path
) -> list[tuple[Path, str, str]]:
    """Return all tag indexes within a collection."""
    entries: list[tuple[Path, str, str]] = []
    for path in sorted(iter_unignored_markdown_files(collection_dir)):
        if is_replaced_archive(path):
            continue
        content = path.read_text(encoding="utf-8")
        if index_source(path, root, content) != "tag":
            continue
        fm = index_frontmatter(path, content)
        title = extract_title(strip_frontmatter(content))
        desc = fm.get("description", "")
        entries.append((path, title, desc))
    return entries


def extract_curated_links(curated_section: str) -> set[str]:
    """Extract link targets from the curated section above the marker."""
    return set(re.findall(r"\]\(([^)]+)\)", curated_section))


def build_generated_section(
    entries: list[tuple[Path, str, str]],
    index_dir: Path,
    heading: str,
    curated_links: set[str] | None = None,
) -> str:
    """Build a generated listing section, excluding already-curated notes."""
    lines = [f"{heading} {MARKER}", ""]

    for path, title, desc in sorted(entries, key=lambda x: x[1].lower()):
        relpath = os.path.relpath(path, index_dir)
        if not relpath.startswith(".."):
            relpath = f"./{relpath}"
        if curated_links and relpath in curated_links:
            continue
        entry = f"- [{title}]({relpath})"
        if desc:
            entry += f" - {desc}"
        lines.append(entry)

    lines.append("")
    return "\n".join(lines)


def generated_section_for_index(
    index_path: Path,
    *,
    source: str,
    index_key: str | None,
    curated_text: str,
    root: Path,
    notes_by_tag: dict[str, list[tuple[Path, str, str]]] | None = None,
) -> str | None:
    """Build the generated section for one tag/tag-indexes page, in memory.

    `curated_text` is the page's committed body; links already curated there
    are excluded from the generated listing. `notes_by_tag` lets the caller
    reuse one collection scan across pages. Returns None for unknown sources.
    Nothing is written — generated tails are build-time materializations for
    the published site, never committed artifacts (ADR 025).
    """
    if source not in GENERATED_HEADING_BY_SOURCE:
        return None

    collection = collection_for_path(index_path, root)
    if source == "tag":
        if notes_by_tag is None:
            notes_by_tag = collect_notes_by_tag(collection)
        entries = notes_by_tag.get(index_key or "", [])
    else:
        entries = collect_tag_index_entries(collection, root)

    return build_generated_section(
        entries,
        index_path.parent,
        GENERATED_HEADING_BY_SOURCE[source],
        extract_curated_links(curated_text),
    )
