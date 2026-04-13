#!/usr/bin/env python3
"""Generate dir-index.md from frontmatter of all markdown files in a directory."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from commonplace.lib.index_directory import write_index


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate dir-index.md from frontmatter of markdown files in a directory.",
    )
    parser.add_argument("directory", help="Directory to scan recursively for notes.")
    args = parser.parse_args()

    notes_dir = Path(args.directory).resolve()
    if not notes_dir.is_dir():
        print(f"Not a directory: {notes_dir}", file=sys.stderr)
        return 1

    output, count = write_index(notes_dir)
    print(f"Generated {output} with {count} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
