#!/usr/bin/env python3
"""List reviewable notes in kb/notes/.

With `--all`, prints one path per line for all top-level notes that have YAML
frontmatter, excluding indexes.

With a review type, prints only notes whose review target is missing or older
than the note itself. This behaves like a simple make-style stale-target check:
if `kb/notes/foo.md` is newer than `reviews/foo.prose-review.md`, `foo.md` is
listed for re-review.

Usage:
    uv run scripts/list_notes.py prose-review
    uv run scripts/list_notes.py semantic-review
    uv run scripts/list_notes.py --all
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


NOTES_DIR = Path("kb/notes")
REVIEWS_DIR = Path("reviews")


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


def list_reviewable_notes(notes_dir: Path) -> list[Path]:
    """Return top-level kb notes that should be eligible for review."""
    return sorted(
        path
        for path in notes_dir.glob("*.md")
        if not is_index(path) and has_frontmatter(path)
    )


def review_path_for(note: Path, review_type: str, reviews_dir: Path) -> Path:
    """Return the review file path for a note/review-type pair."""
    return reviews_dir / f"{note.stem}.{review_type}.md"


def needs_review(note: Path, review_type: str, reviews_dir: Path) -> bool:
    """Return whether the note should be re-reviewed for the given review type."""
    review_path = review_path_for(note, review_type, reviews_dir)
    if not review_path.exists():
        return True

    return note.stat().st_mtime_ns > review_path.stat().st_mtime_ns


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "List top-level kb notes, or only notes whose review files are "
            "missing/stale for a given review type."
        )
    )
    parser.add_argument(
        "review_type",
        nargs="?",
        help="Review target suffix such as prose-review or semantic-review.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="List all reviewable notes without checking review timestamps.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if not NOTES_DIR.is_dir():
        print(f"Directory not found: {NOTES_DIR}", file=sys.stderr)
        sys.exit(1)

    if not args.all and not args.review_type:
        parser.error("provide a review type or pass --all")

    notes = list_reviewable_notes(NOTES_DIR)
    if args.review_type:
        notes = [
            note
            for note in notes
            if needs_review(note, args.review_type, REVIEWS_DIR)
        ]

    for note in notes:
        print(note)


if __name__ == "__main__":
    main()
