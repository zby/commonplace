#!/usr/bin/env python3
"""Backfill review metadata into existing review files from git history.

For each individual review file in `reviews/`, this script finds the commit that
last touched the review, resolves the corresponding note blob at that commit,
and prepends a metadata block. Existing metadata is preserved unless
`--rewrite` is passed.

Usage:
    uv run scripts/migrate_review_metadata.py
    uv run scripts/migrate_review_metadata.py --rewrite
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from review_metadata import (
    ReviewMetadata,
    blob_sha_at_commit,
    detect_review_type,
    extract_note_filename,
    git_blob_sha,
    inject_review_metadata,
    last_commit_for_path,
    last_commit_timestamp_for_path,
    parse_review_metadata,
)


REPO_ROOT = Path.cwd()
NOTES_DIR = REPO_ROOT / "kb" / "notes"
REVIEWS_DIR = REPO_ROOT / "reviews"


@dataclass
class MigrationResult:
    updated: int = 0
    skipped: int = 0
    warned: int = 0
    failed: int = 0


def iter_review_files(reviews_dir: Path) -> list[Path]:
    """Return individual review files, excluding summaries."""
    return sorted(
        path
        for path in reviews_dir.glob("*.*-review.md")
        if not path.name.startswith("SUMMARY.")
    )


def iso_now() -> str:
    """Return the current local timestamp in ISO 8601 format."""
    return datetime.now().astimezone().isoformat(timespec="seconds")


def migrate_review_file(
    review_path: Path,
    notes_dir: Path,
    repo_root: Path,
    rewrite: bool = False,
) -> tuple[bool, str]:
    """Add revision metadata to a single review file."""
    review_text = review_path.read_text(encoding="utf-8")
    if not rewrite and parse_review_metadata(review_text) is not None:
        return False, "metadata-present"

    note_filename = extract_note_filename(review_text)
    if note_filename is None:
        return False, "missing-note-header"

    note_path = notes_dir / note_filename
    review_rel = review_path.relative_to(repo_root)
    note_rel = note_path.relative_to(repo_root)
    review_commit = last_commit_for_path(repo_root, review_rel)
    if review_commit is None:
        if not note_path.exists():
            return False, "missing-review-commit"

        note_commit = last_commit_for_path(repo_root, note_rel)
        migrated_at = iso_now()
        metadata = ReviewMetadata(
            note_path=note_rel.as_posix(),
            last_full_review_note_sha=git_blob_sha(note_path),
            last_full_review_note_commit=note_commit,
            last_full_review_at=migrated_at,
            last_accepted_note_sha=git_blob_sha(note_path),
            last_accepted_note_commit=note_commit,
            last_accepted_at=migrated_at,
            last_acceptance_kind="full-review",
            review_type=detect_review_type(review_path),
        )
        updated = inject_review_metadata(review_text, metadata)
        review_path.write_text(updated, encoding="utf-8")
        return True, "updated-untracked-review"

    reviewed_blob_sha = blob_sha_at_commit(repo_root, review_commit, note_rel)
    if reviewed_blob_sha is None:
        return False, "missing-note-blob"

    reviewed_at = last_commit_timestamp_for_path(repo_root, review_rel)
    metadata = ReviewMetadata(
        note_path=note_rel.as_posix(),
        last_full_review_note_sha=reviewed_blob_sha,
        last_full_review_note_commit=review_commit,
        last_full_review_at=reviewed_at,
        last_accepted_note_sha=reviewed_blob_sha,
        last_accepted_note_commit=review_commit,
        last_accepted_at=reviewed_at,
        last_acceptance_kind="full-review",
        review_type=detect_review_type(review_path),
    )
    updated = inject_review_metadata(review_text, metadata)
    review_path.write_text(updated, encoding="utf-8")
    return True, "updated"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Backfill review revision metadata from git history."
    )
    parser.add_argument(
        "--rewrite",
        action="store_true",
        help="Replace existing metadata blocks instead of skipping them.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if not REVIEWS_DIR.is_dir():
        print(f"Directory not found: {REVIEWS_DIR}", file=sys.stderr)
        sys.exit(1)

    results = MigrationResult()
    for review_path in iter_review_files(REVIEWS_DIR):
        updated, reason = migrate_review_file(
            review_path,
            NOTES_DIR,
            REPO_ROOT,
            rewrite=args.rewrite,
        )
        if updated:
            results.updated += 1
            continue

        if reason == "metadata-present":
            results.skipped += 1
        elif reason == "missing-note-blob":
            results.warned += 1
            print(
                f"Warning: could not reconstruct reviewed blob for "
                f"{review_path.relative_to(REPO_ROOT)}; leaving existing metadata in place",
                file=sys.stderr,
            )
        else:
            results.failed += 1
            print(
                f"Failed to migrate {review_path.relative_to(REPO_ROOT)}: {reason}",
                file=sys.stderr,
            )

    print(
        f"Updated {results.updated} review files; "
        f"skipped {results.skipped}; "
        f"warned {results.warned}; failed {results.failed}"
    )

    if results.failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
