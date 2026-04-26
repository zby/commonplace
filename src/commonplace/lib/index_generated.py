"""Rebuild generated sections of index pages."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

from commonplace.lib import frontmatter
from commonplace.lib.note_parser import extract_title, strip_frontmatter
from commonplace.lib.project_paths import (
    collection_dirs,
    collection_for_path,
    is_replaced_archive,
    is_type_definition_content,
    iter_unignored_markdown_files,
)


FIELD_NAME = "tags"
MARKER = "<!-- generated -->"
INDEX_TYPE = "kb/types/index.md"
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

        if fm.get("type") == INDEX_TYPE:
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
    if fm.get("type") != INDEX_TYPE:
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


def sync_index(
    index_path: Path,
    notes_by_tag: dict[str, list[tuple[Path, str, str]]],
    root: Path,
    dry_run: bool = False,
) -> str | None:
    """Sync the generated section of one index."""
    content = index_path.read_text(encoding="utf-8")
    fm = index_frontmatter(index_path, content)
    source = str(fm.get("index_source", ""))
    if source not in GENERATED_HEADING_BY_SOURCE:
        return None

    marker_pos_for_curated = content.find(MARKER)
    curated_section = (
        content[:marker_pos_for_curated] if marker_pos_for_curated != -1 else content
    )
    curated_links = extract_curated_links(curated_section)

    if source == "tag":
        key = str(fm.get("index_key", ""))
        entries = notes_by_tag.get(key, [])
        change_target = f"{len(entries)} notes for tag '{key}'"
    else:
        collection = collection_for_path(index_path, root)
        entries = collect_tag_index_entries(collection, root)
        change_target = f"{len(entries)} tag indexes"

    generated = build_generated_section(
        entries,
        index_path.parent,
        GENERATED_HEADING_BY_SOURCE[source],
        curated_links,
    )

    marker_pos = content.find(MARKER)
    if marker_pos == -1:
        heading_pos = -1
        for heading in GENERATED_HEADING_BY_SOURCE.values():
            heading_pos = max(heading_pos, content.rfind(f"\n{heading}"))
        if heading_pos == -1:
            heading_pos = content.rfind("\n## All notes")
        if heading_pos != -1:
            new_content = content[:heading_pos].rstrip("\n") + "\n\n" + generated
        else:
            new_content = content.rstrip("\n") + "\n\n" + generated
    else:
        line_start = content.rfind("\n", 0, marker_pos)
        line_start = 0 if line_start == -1 else line_start + 1
        new_content = content[:line_start].rstrip("\n") + "\n\n" + generated

    if new_content == content:
        return None

    if not dry_run:
        index_path.write_text(new_content, encoding="utf-8")
    return f"  {'Would update' if dry_run else 'Updated'} {index_path.name}: {change_target}"


def find_index_files(args: list[str], root: Path) -> list[Path]:
    """Find generated-tail index files to process."""
    if args:
        indexes = []
        for arg in args:
            path = Path(arg)
            if not path.is_file():
                continue
            content = path.read_text(encoding="utf-8")
            if index_source(path, root, content):
                indexes.append(path)
        return indexes

    indexes = []
    for collection in collection_dirs(root):
        for path in sorted(iter_unignored_markdown_files(collection)):
            content = path.read_text(encoding="utf-8")
            if index_source(path, root, content):
                indexes.append(path)
    return indexes
