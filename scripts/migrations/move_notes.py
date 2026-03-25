#!/usr/bin/env python3
"""Move notes to a new directory and update all markdown links.

Usage:
    uv run scripts/move_notes.py TARGET_DIR NOTE [NOTE ...]

Example:
    uv run scripts/move_notes.py kb/notes/definitions kb/notes/constraining.md kb/notes/distillation.md

The script:
1. Creates TARGET_DIR if it doesn't exist.
2. Moves each NOTE into TARGET_DIR.
3. Finds all .md files under kb/ that link to the moved notes.
4. Rewrites relative links to point to the new location.
5. Prints a summary of changes.

Dry-run by default. Pass --apply to actually write changes.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
KB_DIR = REPO_ROOT / "kb"


def compute_relative(from_file: Path, to_file: Path) -> str:
    """Compute the relative path from from_file's directory to to_file."""
    return os.path.relpath(to_file, from_file.parent)


def find_md_files(root: Path) -> list[Path]:
    """Find all .md files under root."""
    return sorted(root.rglob("*.md"))


def rewrite_links(
    content: str,
    source_file: Path,
    old_paths: dict[str, Path],
    new_paths: dict[str, Path],
) -> tuple[str, list[str]]:
    """Rewrite markdown links from old paths to new paths.

    old_paths and new_paths are keyed by the note stem (e.g. 'constraining').
    Returns (new_content, list_of_changes).
    """
    changes = []

    # Match markdown links: [text](path)
    def replace_link(m: re.Match) -> str:
        text = m.group(1)
        link_target = m.group(2)

        # Strip any anchor
        anchor = ""
        if "#" in link_target:
            link_target, anchor = link_target.rsplit("#", 1)
            anchor = "#" + anchor

        # Resolve the link to an absolute path
        if link_target.startswith("http") or link_target.startswith("#"):
            return m.group(0)

        resolved = (source_file.parent / link_target).resolve()

        # Check if this resolved path matches any of our old paths
        for stem, old_abs in old_paths.items():
            if resolved == old_abs:
                new_rel = compute_relative(source_file, new_paths[stem])
                # Normalize: use ./ prefix for same-dir or child paths
                if not new_rel.startswith(".."):
                    new_rel = "./" + new_rel
                changes.append(f"  {link_target} -> {new_rel}")
                return f"[{text}]({new_rel}{anchor})"

        return m.group(0)

    new_content = re.sub(r"\[([^\]]*)\]\(([^)]+)\)", replace_link, content)
    return new_content, changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target_dir", help="Directory to move notes into")
    parser.add_argument("notes", nargs="+", help="Note files to move")
    parser.add_argument(
        "--apply", action="store_true", help="Actually apply changes (default is dry-run)"
    )
    args = parser.parse_args()

    target_dir = Path(args.target_dir)
    notes = [Path(n) for n in args.notes]

    # Validate
    for note in notes:
        if not note.exists():
            print(f"ERROR: {note} does not exist", file=sys.stderr)
            sys.exit(1)

    # Build path maps
    old_paths: dict[str, Path] = {}
    new_paths: dict[str, Path] = {}
    for note in notes:
        stem = note.stem
        old_paths[stem] = note.resolve()
        new_paths[stem] = (target_dir / note.name).resolve()

    # Find all md files to check
    md_files = find_md_files(KB_DIR)

    # Also check CLAUDE.md at repo root
    claude_md = REPO_ROOT / "CLAUDE.md"
    if claude_md.exists():
        md_files.append(claude_md)

    mode = "APPLYING" if args.apply else "DRY RUN"
    print(f"=== {mode} ===\n")

    if args.apply:
        target_dir.mkdir(parents=True, exist_ok=True)

    # Track stats
    files_changed = 0
    total_links = 0

    for md_file in md_files:
        # Skip the notes being moved (they'll be handled after move)
        if md_file.resolve() in old_paths.values():
            continue

        content = md_file.read_text()
        new_content, changes = rewrite_links(content, md_file, old_paths, new_paths)

        if changes:
            files_changed += 1
            total_links += len(changes)
            rel_path = md_file.relative_to(REPO_ROOT)
            print(f"{rel_path}: {len(changes)} link(s)")
            for c in changes:
                print(c)
            print()

            if args.apply:
                md_file.write_text(new_content)

    # Rewrite links within the moved notes themselves
    for note in notes:
        content = note.read_text()
        new_note_path = target_dir / note.name
        # For self-links, the source file will be in the new location
        new_content, changes = rewrite_links(
            content, new_note_path, old_paths, new_paths
        )

        if changes:
            files_changed += 1
            total_links += len(changes)
            print(f"{note.relative_to(REPO_ROOT)} (self-links): {len(changes)} link(s)")
            for c in changes:
                print(c)
            print()

        if args.apply:
            # Move the file and write updated content
            shutil.move(str(note), str(new_note_path))
            new_note_path.write_text(new_content)
        else:
            # In dry-run, just report the move
            pass

    print(f"--- Summary ---")
    print(f"Notes to move: {len(notes)}")
    print(f"Files with link updates: {files_changed}")
    print(f"Total links rewritten: {total_links}")

    if not args.apply:
        print(f"\nThis was a dry run. Pass --apply to execute.")


if __name__ == "__main__":
    main()
