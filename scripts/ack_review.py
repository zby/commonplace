#!/usr/bin/env python3
"""Acknowledge a trivial note change without rewriting the review body.

This advances the accepted note revision in an existing review file while
preserving the last full-review revision.

Usage:
    uv run scripts/ack_review.py prose-review kb/notes/backlinks.md
    uv run scripts/ack_review.py semantic-review kb/notes/backlinks.md
    uv run scripts/ack_review.py semantic-review kb/notes/foo.md kb/notes/bar.md
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

from review_metadata import (
    ReviewMetadata,
    git_blob_sha,
    inject_review_metadata,
    last_commit_for_path,
    parse_review_metadata,
)


class AckReviewError(Exception):
    """Raised when a review acknowledgement target cannot be processed."""


def iso_now() -> str:
    """Return the current local timestamp in ISO 8601 format."""
    return datetime.now().astimezone().isoformat(timespec="seconds")


def review_path_for(repo_root: Path, note_path: Path, review_type: str) -> Path:
    """Return the review file path for a note/review pair."""
    return repo_root / "kb" / "reports" / "reviews" / f"{note_path.stem}.{review_type}.md"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Advance the accepted note revision in an existing review file "
            "after deciding the diff is trivial."
        )
    )
    parser.add_argument(
        "review_type",
        help="Review suffix such as prose-review or semantic-review.",
    )
    parser.add_argument(
        "note_paths",
        nargs="+",
        help="One or more reviewed note paths, for example kb/notes/backlinks.md.",
    )
    return parser


def acknowledge_note(repo_root: Path, review_type: str, raw_note_path: str) -> str:
    """Advance the accepted revision for one reviewed note."""
    note_path = (repo_root / raw_note_path).resolve()
    if not note_path.is_file():
        raise AckReviewError(f"Note not found: {raw_note_path}")

    try:
        note_rel = note_path.relative_to(repo_root)
    except ValueError:
        raise AckReviewError(
            f"Note must be inside the repository: {note_path}"
        )

    review_path = review_path_for(repo_root, note_path, review_type)
    if not review_path.is_file():
        raise AckReviewError(
            f"Review file not found: {review_path.relative_to(repo_root)}",
        )

    review_text = review_path.read_text(encoding="utf-8")
    metadata = parse_review_metadata(review_text)
    if metadata is None:
        raise AckReviewError(
            f"Review metadata missing or invalid in {review_path.relative_to(repo_root)}",
        )

    note_commit = last_commit_for_path(repo_root, note_rel)
    accepted_at = iso_now()
    updated_metadata = ReviewMetadata(
        note_path=note_rel.as_posix(),
        last_full_review_note_sha=metadata.last_full_review_note_sha,
        last_full_review_note_commit=metadata.last_full_review_note_commit,
        last_full_review_at=metadata.last_full_review_at,
        last_accepted_note_sha=git_blob_sha(note_path),
        last_accepted_note_commit=note_commit,
        last_accepted_at=accepted_at,
        last_acceptance_kind="trivial-change-ack",
        review_type=metadata.review_type or review_type,
    )
    review_path.write_text(
        inject_review_metadata(review_text, updated_metadata),
        encoding="utf-8",
    )
    return (
        f"Updated {review_path.relative_to(repo_root)} "
        f"to accept {note_rel.as_posix()} at {accepted_at}"
    )


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    repo_root = Path.cwd()

    failures = 0
    for raw_note_path in args.note_paths:
        try:
            print(acknowledge_note(repo_root, args.review_type, raw_note_path))
        except AckReviewError as exc:
            failures += 1
            print(str(exc), file=sys.stderr)

    if failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
