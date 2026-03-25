#!/usr/bin/env python3
"""Fix outbound links in moved files that still use old relative paths.

After move_notes.py moves files to a subdirectory, links FROM those files
to non-moved files still use the old relative paths. This script resolves
each broken link by searching parent directories for the target.

Usage:
    uv run scripts/migrations/fix_outbound_links.py FILE [FILE ...]
    uv run scripts/migrations/fix_outbound_links.py --apply FILE [FILE ...]
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def find_target(filename: str, search_root: Path) -> Path | None:
    """Find a file by name under search_root."""
    for match in search_root.rglob(filename):
        return match
    return None


def fix_links(md_file: Path, apply: bool) -> list[str]:
    """Fix broken relative links in md_file. Returns list of changes."""
    content = md_file.read_text()
    changes = []

    def fix_link(m: re.Match) -> str:
        text, target = m.group(1), m.group(2)
        if target.startswith("http") or target.startswith("#"):
            return m.group(0)

        anchor = ""
        bare = target
        if "#" in bare:
            bare, anchor = bare.rsplit("#", 1)
            anchor = "#" + anchor

        resolved = (md_file.parent / bare).resolve()
        if resolved.exists():
            return m.group(0)

        # Try to find the file by name under kb/
        filename = Path(bare).name
        found = find_target(filename, REPO_ROOT / "kb")
        if found:
            new_rel = os.path.relpath(found, md_file.parent)
            if not new_rel.startswith(".."):
                new_rel = "./" + new_rel
            changes.append(f"  {target} -> {new_rel}")
            return f"[{text}]({new_rel}{anchor})"

        changes.append(f"  {target} -> NOT FOUND")
        return m.group(0)

    new_content = re.sub(r"\[([^\]]*)\]\(([^)]+)\)", fix_link, content)

    if changes and apply:
        md_file.write_text(new_content)

    return changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", help="Files to fix")
    parser.add_argument("--apply", action="store_true", help="Write changes")
    args = parser.parse_args()

    mode = "APPLYING" if args.apply else "DRY RUN"
    print(f"=== {mode} ===\n")

    for f in args.files:
        path = Path(f)
        changes = fix_links(path, args.apply)
        if changes:
            print(f"{path}: {len(changes)} fix(es)")
            for c in changes:
                print(c)
            print()

    if not args.apply:
        print("Pass --apply to write changes.")


if __name__ == "__main__":
    main()
