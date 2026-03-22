#!/usr/bin/env python3
"""List reviewable notes in kb/notes/.

Prints one path per line for notes that have YAML frontmatter.
Excludes index files and subdirectories.

Usage: uv run scripts/list_notes.py
"""

import re
import sys
from pathlib import Path


def has_frontmatter(path: Path) -> bool:
    """Check if a file starts with YAML frontmatter."""
    try:
        content = path.read_text(encoding="utf-8")
        return bool(re.match(r"^---\n", content))
    except (OSError, UnicodeDecodeError):
        return False


def is_index(path: Path) -> bool:
    """Check if a file is an index."""
    return path.name == "index.md" or path.name.endswith("-index.md")


def main() -> None:
    notes_dir = Path("kb/notes")
    if not notes_dir.is_dir():
        print(f"Directory not found: {notes_dir}", file=sys.stderr)
        sys.exit(1)

    notes = sorted(
        p
        for p in notes_dir.glob("*.md")
        if not is_index(p) and has_frontmatter(p)
    )

    for note in notes:
        print(note)


if __name__ == "__main__":
    main()
