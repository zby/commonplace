#!/usr/bin/env python3
"""Relocate a KB note by renaming it, moving it, or both.

Usage:
    commonplace-relocate-note kb/notes/my-note.md "New note title"
    commonplace-relocate-note kb/notes/my-note.md --to kb/notes/definitions
    commonplace-relocate-note kb/notes/my-note.md --to kb/notes/definitions/new-note.md --apply
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from commonplace.lib.relocation import relocate_note


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("note", help="Note path or unique note name under kb/notes/")
    parser.add_argument("new_name", nargs="?", help="New title or filename stem; omit to keep the current filename")
    parser.add_argument("--to", dest="dest_path", help="Destination directory or .md path under kb/notes/")
    parser.add_argument("--apply", action="store_true", help="Write changes instead of dry-running")
    args = parser.parse_args()

    repo_root = Path.cwd().resolve()

    try:
        sys.exit(
            relocate_note(
                repo_root=repo_root,
                note_arg=args.note,
                new_name=args.new_name,
                dest_path=args.dest_path,
                apply=args.apply,
            )
        )
    except (FileNotFoundError, ValueError) as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
