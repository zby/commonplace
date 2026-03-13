#!/usr/bin/env python3
"""Rebuild the generated 'All notes' section of tag index pages.

For each index page, derives the tag from the filename (strip -index.md),
finds all notes with that tag in their areas: field, and replaces
everything from the <!-- generated --> marker to EOF.

Usage:
    uv run scripts/sync_generated_index.py                    # all indexes
    uv run scripts/sync_generated_index.py kb/notes/kb-design-index.md
    uv run scripts/sync_generated_index.py --dry-run
"""

import os
import re
import sys
from pathlib import Path

import yaml

KB_ROOT = Path(__file__).parent.parent / "kb"
NOTES_DIR = KB_ROOT / "notes"
FIELD_NAME = "tags"
MARKER = "<!-- generated -->"


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def get_title(content: str) -> str:
    """Extract first H1 heading from markdown."""
    content_no_fm = re.sub(r"^---\n.*?\n---\n", "", content, flags=re.DOTALL)
    match = re.search(r"^#\s+(.+)$", content_no_fm, re.MULTILINE)
    return match.group(1) if match else "Untitled"


def collect_notes_by_tag() -> dict[str, list[tuple[Path, str, str]]]:
    """Scan all notes and group by tag.

    Returns {tag: [(path, title, description), ...]}.
    """
    by_tag: dict[str, list[tuple[Path, str, str]]] = {}

    for path in sorted(NOTES_DIR.rglob("*.md")):
        content = path.read_text()
        fm = parse_frontmatter(content)

        # Skip index pages themselves
        if fm.get("type") == "index":
            continue

        tags = fm.get(FIELD_NAME, [])
        if not tags:
            continue

        title = get_title(content)
        desc = fm.get("description", "")

        for tag in tags:
            by_tag.setdefault(tag, []).append((path, title, desc))

    return by_tag


def tag_from_filename(index_path: Path) -> str:
    """Derive tag name from index filename.

    kb-design-index.md -> kb-design
    related-systems-index.md -> related-systems
    """
    stem = index_path.stem
    if stem.endswith("-index"):
        return stem[: -len("-index")]
    return stem


def build_generated_section(
    notes: list[tuple[Path, str, str]], index_dir: Path
) -> str:
    """Build the generated listing section."""
    lines = [f"## All notes {MARKER}", ""]

    for path, title, desc in sorted(notes, key=lambda x: x[1].lower()):
        relpath = os.path.relpath(path, index_dir)
        if not relpath.startswith(".."):
            relpath = f"./{relpath}"
        entry = f"- [{title}]({relpath})"
        if desc:
            entry += f" — {desc}"
        lines.append(entry)

    lines.append("")
    return "\n".join(lines)


def sync_index(index_path: Path, notes_by_tag: dict, dry_run: bool = False) -> str | None:
    """Sync generated section of a single index. Returns change description or None."""
    content = index_path.read_text()
    tag = tag_from_filename(index_path)

    notes = notes_by_tag.get(tag, [])
    generated = build_generated_section(notes, index_path.parent)

    marker_pos = content.find(MARKER)
    if marker_pos == -1:
        # No marker yet — append
        heading_pos = content.rfind(f"\n## All notes")
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
    return f"  {'Would update' if dry_run else 'Updated'} {index_path.name}: {len(notes)} notes for tag '{tag}'"


def find_index_files(args: list[str]) -> list[Path]:
    """Find index files to process."""
    if args:
        return [Path(a) for a in args if Path(a).is_file()]

    # Find all type: index files
    indexes = []
    for path in sorted(NOTES_DIR.rglob("*.md")):
        content = path.read_text()
        fm = parse_frontmatter(content)
        if fm.get("type") == "index":
            indexes.append(path)
    return indexes


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("DRY RUN — no files will be modified\n")

    notes_by_tag = collect_notes_by_tag()
    print(f"Found {sum(len(v) for v in notes_by_tag.values())} tag assignments across {len(notes_by_tag)} tags\n")

    indexes = find_index_files(args)
    if not indexes:
        print("No index files found.", file=sys.stderr)
        sys.exit(1)

    changes = []
    for index_path in indexes:
        result = sync_index(index_path, notes_by_tag, dry_run)
        if result:
            changes.append(result)

    if changes:
        print(f"\n{'Would change' if dry_run else 'Changed'} {len(changes)} index(es):")
        for c in changes:
            print(c)
    else:
        print("All generated sections are in sync.")


if __name__ == "__main__":
    main()
