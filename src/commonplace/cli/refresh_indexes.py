#!/usr/bin/env python3
"""Refresh generated directory indexes and generated-tail indexes for the KB."""

import sys
from pathlib import Path

from commonplace.cli import generate_notes_index, sync_generated_index

DIRECTORY_INDEX_DIRS = ("kb/notes", "kb/sources")


def main() -> int:
    repo_root = Path.cwd().resolve()

    for relative_dir in DIRECTORY_INDEX_DIRS:
        notes_dir = repo_root / relative_dir
        if not notes_dir.is_dir():
            print(f"Not a directory: {notes_dir}", file=sys.stderr)
            return 1

        output, count = generate_notes_index.write_index(notes_dir)
        print(f"Generated {output} with {count} entries")

    notes_by_tag = sync_generated_index.collect_notes_by_tag()
    print(
        f"Found {sum(len(v) for v in notes_by_tag.values())} tag assignments "
        f"across {len(notes_by_tag)} tags\n",
    )

    indexes = sync_generated_index.find_index_files([])
    if not indexes:
        print("No generated-tail index files found.", file=sys.stderr)
        return 1

    changes = []
    for index_path in indexes:
        result = sync_generated_index.sync_index(index_path, notes_by_tag)
        if result:
            changes.append(result)

    if changes:
        print(f"\nChanged {len(changes)} index(es):")
        for change in changes:
            print(change)
    else:
        print("All generated sections are in sync.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
