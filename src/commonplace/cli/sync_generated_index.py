#!/usr/bin/env python3
"""Rebuild the generated section of index pages with generated tails.

For each managed index page, uses frontmatter to determine the source of
the generated section and replaces everything from the <!-- generated -->
marker to EOF. Links already present in the curated section above the
marker are excluded from the generated listing.

Usage:
    commonplace-sync-generated-index                    # all indexes
    commonplace-sync-generated-index kb/notes/kb-design-index.md
    commonplace-sync-generated-index --dry-run
"""

import argparse
import os
import re
import sys
from pathlib import Path

from commonplace.lib import frontmatter

KB_ROOT = Path.cwd().resolve() / "kb"
FIELD_NAME = "tags"
MARKER = "<!-- generated -->"
GENERATED_HEADING_BY_SOURCE = {
    "tag": "## Other tagged notes",
    "tag-indexes": "## Other tag indexes",
}


def find_all_collections() -> list[Path]:
    """Find all collection directories under KB_ROOT."""
    return sorted(
        p for p in KB_ROOT.iterdir()
        if p.is_dir() and not p.name.startswith(".")
    )


def collection_for_path(path: Path) -> Path:
    """Return the collection root for a file path.

    The collection is the first directory under KB_ROOT.
    E.g., kb/notes/foo/bar.md -> kb/notes/
    """
    try:
        rel = path.resolve().relative_to(KB_ROOT)
    except ValueError:
        return path.parent
    parts = rel.parts
    if parts:
        return KB_ROOT / parts[0]
    return KB_ROOT


def get_title(content: str) -> str:
    """Extract first H1 heading from markdown."""
    body = frontmatter.strip(content)
    match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    return match.group(1) if match else "Untitled"


def collect_notes_by_tag(collection_dir: Path) -> dict[str, list[tuple[Path, str, str]]]:
    """Scan a collection and group notes by tag.

    Returns {tag: [(path, title, description), ...]}.
    """
    by_tag: dict[str, list[tuple[Path, str, str]]] = {}

    for path in sorted(collection_dir.rglob("*.md")):
        content = path.read_text()
        fm = frontmatter.parse(content).data

        # Skip index pages and type/config directories
        if fm.get("type") == "index":
            continue
        rel_parts = path.relative_to(collection_dir).parts
        if "types" in rel_parts or ".collection" in rel_parts:
            continue

        tags = fm.get(FIELD_NAME, [])
        if not tags:
            continue

        title = get_title(content)
        desc = fm.get("description", "")

        for tag in tags:
            by_tag.setdefault(tag, []).append((path, title, desc))

    return by_tag


def index_frontmatter(path: Path, content: str | None = None) -> dict:
    """Parse frontmatter for an index candidate."""
    if content is None:
        content = path.read_text()
    return frontmatter.parse(content).data


def index_source(path: Path, content: str | None = None) -> str | None:
    """Return the declared generated-section source for a managed index."""
    collection = collection_for_path(path)
    try:
        rel_parts = path.relative_to(collection).parts
    except ValueError:
        rel_parts = path.parts

    if "types" in rel_parts or ".collection" in rel_parts:
        return None
    if path.name.endswith(".template.md"):
        return None

    fm = index_frontmatter(path, content)
    if fm.get("type") != "index":
        return None
    source = fm.get("index_source")
    if source in GENERATED_HEADING_BY_SOURCE:
        return source
    return None


def collect_tag_index_entries(collection_dir: Path) -> list[tuple[Path, str, str]]:
    """Return all tag indexes within a collection."""
    entries: list[tuple[Path, str, str]] = []
    for path in sorted(collection_dir.rglob("*.md")):
        content = path.read_text()
        if index_source(path, content) != "tag":
            continue
        fm = index_frontmatter(path, content)
        title = get_title(content)
        desc = fm.get("description", "")
        entries.append((path, title, desc))
    return entries


def extract_curated_links(curated_section: str) -> set[str]:
    """Extract link targets from the curated section above the marker."""
    return set(re.findall(r'\]\(([^)]+)\)', curated_section))


def build_generated_section(
    entries: list[tuple[Path, str, str]],
    index_dir: Path,
    heading: str,
    curated_links: set[str] | None = None,
) -> str:
    """Build the generated listing section, excluding already-curated notes."""
    lines = [f"{heading} {MARKER}", ""]

    for path, title, desc in sorted(entries, key=lambda x: x[1].lower()):
        relpath = os.path.relpath(path, index_dir)
        if not relpath.startswith(".."):
            relpath = f"./{relpath}"
        if curated_links and relpath in curated_links:
            continue
        entry = f"- [{title}]({relpath})"
        if desc:
            entry += f" — {desc}"
        lines.append(entry)

    lines.append("")
    return "\n".join(lines)


def sync_index(index_path: Path, notes_by_tag: dict, dry_run: bool = False) -> str | None:
    """Sync generated section of a single index. Returns change description or None."""
    content = index_path.read_text()
    fm = index_frontmatter(index_path, content)
    source = str(fm.get("index_source", ""))
    if source not in GENERATED_HEADING_BY_SOURCE:
        return None

    # Extract links from the curated section (above the marker)
    marker_pos_for_curated = content.find(MARKER)
    if marker_pos_for_curated != -1:
        curated_section = content[:marker_pos_for_curated]
    else:
        curated_section = content
    curated_links = extract_curated_links(curated_section)

    if source == "tag":
        key = str(fm.get("index_key", ""))
        entries = notes_by_tag.get(key, [])
        change_target = f"{len(entries)} notes for tag '{key}'"
    else:
        collection = collection_for_path(index_path)
        entries = collect_tag_index_entries(collection)
        change_target = f"{len(entries)} tag indexes"

    generated = build_generated_section(
        entries,
        index_path.parent,
        GENERATED_HEADING_BY_SOURCE[source],
        curated_links,
    )

    marker_pos = content.find(MARKER)
    if marker_pos == -1:
        # No marker yet — append
        heading_pos = -1
        for heading in GENERATED_HEADING_BY_SOURCE.values():
            heading_pos = max(heading_pos, content.rfind(f"\n{heading}"))
        if heading_pos == -1:
            heading_pos = content.rfind("\n## All notes")
        if heading_pos != -1:
            # Has the heading but no marker — replace from heading
            new_content = content[:heading_pos].rstrip("\n") + "\n\n" + generated
        else:
            # No section at all — append
            new_content = content.rstrip("\n") + "\n\n" + generated
    else:
        # Find the start of the line containing the marker
        line_start = content.rfind("\n", 0, marker_pos)
        if line_start == -1:
            line_start = 0
        else:
            line_start += 1
        new_content = content[:line_start].rstrip("\n") + "\n\n" + generated

    if new_content == content:
        return None

    if not dry_run:
        index_path.write_text(new_content)
    return f"  {'Would update' if dry_run else 'Updated'} {index_path.name}: {change_target}"


def find_index_files(args: list[str]) -> list[Path]:
    """Find index files to process."""
    if args:
        indexes = []
        for arg in args:
            path = Path(arg)
            if not path.is_file():
                continue
            content = path.read_text()
            if index_source(path, content):
                indexes.append(path)
        return indexes

    # Find all indexes with generated tails across all collections.
    indexes = []
    for collection in find_all_collections():
        for path in sorted(collection.rglob("*.md")):
            content = path.read_text()
            if index_source(path, content):
                indexes.append(path)
    return indexes


def main():
    parser = argparse.ArgumentParser(
        description="Rebuild generated sections of index pages with generated tails.",
    )
    parser.add_argument("index_paths", nargs="*", help="Optional index files to process.")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing files.")
    args = parser.parse_args()

    if args.dry_run:
        print("DRY RUN — no files will be modified\n")

    # Collect tags per collection (tags are collection-scoped)
    tags_by_collection: dict[Path, dict[str, list[tuple[Path, str, str]]]] = {}
    for collection in find_all_collections():
        tags = collect_notes_by_tag(collection)
        if tags:
            tags_by_collection[collection] = tags
            total = sum(len(v) for v in tags.values())
            print(f"  {collection.name}: {total} tag assignments across {len(tags)} tags")

    total_assignments = sum(sum(len(v) for v in tags.values()) for tags in tags_by_collection.values())
    total_tags = sum(len(tags) for tags in tags_by_collection.values())
    print(f"Total: {total_assignments} tag assignments across {total_tags} tags\n")

    indexes = find_index_files(args.index_paths)
    if not indexes:
        print("No index files found.", file=sys.stderr)
        sys.exit(1)

    changes = []
    for index_path in indexes:
        collection = collection_for_path(index_path)
        notes_by_tag = tags_by_collection.get(collection, {})
        result = sync_index(index_path, notes_by_tag, args.dry_run)
        if result:
            changes.append(result)

    if changes:
        print(f"\n{'Would change' if args.dry_run else 'Changed'} {len(changes)} index(es):")
        for c in changes:
            print(c)
    else:
        print("All generated sections are in sync.")


if __name__ == "__main__":
    main()
