#!/usr/bin/env python3
"""Sync Topics footer links from frontmatter areas: field.

Usage:
    uv run scripts/sync_topic_links.py kb/notes/my-note.md
    uv run scripts/sync_topic_links.py kb/notes/ kb/claw-design/
    uv run scripts/sync_topic_links.py --dry-run kb/notes/my-note.md

Accepts files and directories. Directories are expanded to *.md files
(non-recursive). At least one path is required.
"""

import os
import re
import sys
from pathlib import Path


def parse_areas(content: str) -> list[str]:
    """Extract areas from YAML frontmatter.

    Handles:
      - areas: [val1, val2]
      - areas:
          - val1
          - val2
      - areas:          (empty — returns [])
    """
    # Match frontmatter block
    fm_match = re.match(r"^---\n(.*?\n)---\n", content, re.DOTALL)
    if not fm_match:
        return []
    frontmatter = fm_match.group(1)

    # Try inline format: areas: [val1, val2]
    inline = re.search(r"^areas:\s*\[([^\]]*)\]\s*$", frontmatter, re.MULTILINE)
    if inline:
        raw = inline.group(1).strip()
        if not raw:
            return []
        return [a.strip() for a in raw.split(",") if a.strip()]

    # Try multi-line format: areas:\n  - val1\n  - val2
    ml = re.search(r"^areas:\s*\n((?:\s+-\s+.*\n)*)", frontmatter, re.MULTILINE)
    if ml:
        items = re.findall(r"^\s+-\s+(.+)$", ml.group(1), re.MULTILINE)
        return [a.strip() for a in items if a.strip()]

    return []


def find_index_relpath(area: str, note_dir: Path) -> str:
    """Find the relative path from note_dir to the area's index file.

    At each level (note_dir, parent, grandparent, up to 4 levels), checks:
      1. Flat file: {search_dir}/{area}.md
      2. Subdirectories: {search_dir}/*/{area}.md

    This handles indexes in the same directory (approvals-index.md next to notes),
    in a sibling subdirectory (claw-design/claw-design.md from notes/), or in a sibling
    subdirectory with a different name (claw-design/links.md from notes/).

    Returns a relative path like './area.md' or '../claw-design/area.md'.
    Falls back to './area.md' if not found (will trigger a warning elsewhere).
    """
    filenames = [f"{area}.md", f"{area}-index.md"]
    search_dir = note_dir.resolve()
    note_dir_resolved = note_dir.resolve()

    for _ in range(4):
        for filename in filenames:
            # Check flat file in search_dir
            candidate = search_dir / filename
            if candidate.exists():
                rel = os.path.relpath(candidate, note_dir_resolved)
                return f"./{rel}" if not rel.startswith("..") else rel

            # Check one level of subdirectories
            try:
                if search_dir.is_dir():
                    for subdir in sorted(search_dir.iterdir()):
                        if subdir.is_dir() and not subdir.name.startswith("."):
                            candidate = subdir / filename
                            if candidate.exists():
                                rel = os.path.relpath(candidate, note_dir_resolved)
                                return f"./{rel}" if not rel.startswith("..") else rel
            except PermissionError:
                pass

        search_dir = search_dir.parent

    return f"./{filenames[0]}"


def build_topics_section(areas: list[str], note_dir: Path | None = None) -> str:
    """Build the Topics: footer section from a list of area names."""
    lines = ["Topics:"]
    for area in sorted(areas):
        if note_dir:
            relpath = find_index_relpath(area, note_dir)
        else:
            relpath = f"./{area}.md"
        lines.append(f"- [{area}]({relpath})")
    return "\n".join(lines) + "\n"


def remove_topics_section(content: str) -> str:
    """Remove existing Topics: section from content."""
    # Topics section: starts with "Topics:" line, followed by list items, until EOF or next section
    return re.sub(r"\nTopics:\n(?:- \[.*\]\(.*\)\n)*$", "\n", content)


def sync_note(filepath: Path, dry_run: bool = False) -> str | None:
    """Sync a single note's Topics section. Returns description of change, or None."""
    content = filepath.read_text()
    areas = parse_areas(content)

    # Remove existing Topics section (if any) to work with clean content
    cleaned = remove_topics_section(content)

    if not areas:
        if cleaned != content:
            # Had a Topics section that was removed
            # Also clean up trailing separator if it's now dangling
            cleaned = cleaned.rstrip("\n") + "\n"
            if not dry_run:
                filepath.write_text(cleaned)
            return f"  REMOVED Topics (no areas): {filepath.name}"
        return None

    # Build new Topics section
    topics = build_topics_section(areas, filepath.parent)

    # Ensure content ends cleanly before appending
    cleaned = cleaned.rstrip("\n") + "\n"

    # Check if there's already a footer separator (--- at end area)
    # Look for --- followed by optional Relevant Notes section at end
    has_footer_sep = bool(re.search(r"\n---\n", cleaned))

    if not has_footer_sep:
        cleaned += "\n---\n"

    # Append Topics after a blank line
    cleaned += "\n" + topics

    if cleaned == content:
        return None

    if not dry_run:
        filepath.write_text(cleaned)
    return f"  UPDATED: {filepath.name} -> areas={areas}"


def resolve_paths(args: list[str]) -> list[Path]:
    """Resolve arguments to a list of .md file paths."""
    files = []
    for arg in args:
        p = Path(arg)
        if p.is_dir():
            files.extend(sorted(p.glob("*.md")))
        elif p.is_file() and p.suffix == ".md":
            files.append(p)
        else:
            print(f"Warning: skipping {arg} (not a .md file or directory)", file=sys.stderr)
    return files


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry_run = "--dry-run" in sys.argv

    if not args:
        print("Usage: sync_topic_links.py [--dry-run] <file-or-dir> [...]", file=sys.stderr)
        print("  Accepts .md files and directories (expanded to *.md).", file=sys.stderr)
        sys.exit(1)

    if dry_run:
        print("DRY RUN — no files will be modified\n")

    notes = resolve_paths(args)
    if not notes:
        print("No .md files found in the given paths.", file=sys.stderr)
        sys.exit(1)

    # Check which index files are referenced
    all_areas: set[str] = set()
    for note in notes:
        areas = parse_areas(note.read_text())
        all_areas.update(areas)

    if all_areas:
        print("Areas referenced in frontmatter:")
        for area in sorted(all_areas):
            # Check whether the area's index file can be found from any note
            found = any(
                (note.parent / find_index_relpath(area, note.parent)).resolve().exists()
                for note in notes
            )
            status = "OK" if found else "WARNING: index file not found"
            print(f"  {area} — {status}")
        print()

    # Sync
    changes = []
    for note in notes:
        result = sync_note(note, dry_run=dry_run)
        if result:
            changes.append(result)

    if changes:
        print(f"{'Would change' if dry_run else 'Changed'} {len(changes)} file(s):")
        for c in changes:
            print(c)
    else:
        print("All Topics sections are in sync.")


if __name__ == "__main__":
    main()
