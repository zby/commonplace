#!/usr/bin/env python3
"""Relocate a KB collection directory: move all contents, update links, add one redirect.

Usage:
    commonplace-relocate-directory kb/notes/related-systems kb/agent-memory-systems
    commonplace-relocate-directory kb/notes/related-systems kb/agent-memory-systems \\
        --redirect notes/related-systems/related-systems-index.md:agent-memory-systems/index.md \\
        --apply
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from commonplace.lib.relocation import relocate_directory
from commonplace.review.relocation_hook import ReviewRelocationHook


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="Source directory under kb/")
    parser.add_argument("destination", help="Destination directory under kb/")
    parser.add_argument(
        "--redirect",
        dest="redirect",
        help="Single mkdocs redirect to add, formatted as OLD:NEW (e.g. notes/old/index.md:new/index.md)",
    )
    parser.add_argument("--apply", action="store_true", help="Write changes instead of dry-running")
    args = parser.parse_args()

    redirect_from = redirect_to = None
    if args.redirect:
        if ":" not in args.redirect:
            print("--redirect must be OLD:NEW", file=sys.stderr)
            sys.exit(1)
        redirect_from, redirect_to = args.redirect.split(":", 1)

    repo_root = Path.cwd().resolve()
    try:
        sys.exit(
            relocate_directory(
                root=repo_root,
                source_arg=args.source,
                dest_path=args.destination,
                redirect_from=redirect_from,
                redirect_to=redirect_to,
                apply=args.apply,
                hooks=[ReviewRelocationHook()],
            )
        )
    except (FileNotFoundError, ValueError) as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
