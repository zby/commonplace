#!/usr/bin/env python3
"""List reviewable notes in kb/notes/.

With `--all`, prints one path per line for all top-level notes that have YAML
frontmatter, excluding indexes.

With a review type, compares the note's current git-style blob hash against the
blob hash stored in the corresponding review file metadata. Unchanged notes are
filtered out. Changed notes can be emitted either as paths or as JSON records
that include a compact diff for the sweep orchestrator.

Usage:
    uv run scripts/notes_selector.py prose-review
    uv run scripts/notes_selector.py prose-review --json
    uv run scripts/notes_selector.py semantic-review
    uv run scripts/notes_selector.py --all
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from frontmatter import extract_raw as extract_frontmatter_raw
from frontmatter import strip as strip_frontmatter
from review_metadata import (
    build_diff_summary,
    git_blob_sha,
    parse_review_metadata,
    read_blob,
    resolve_last_accepted_note_sha,
)


REPO_ROOT = Path.cwd()
NOTES_DIR = REPO_ROOT / "kb" / "notes"
REVIEWS_DIR = REPO_ROOT / "kb" / "reports" / "reviews"
DIFF_OUTPUT_LIMIT = 1000
BODY_REWRITE_THRESHOLD = 0.5


@dataclass
class ReviewChange:
    note_path: str
    review_path: str | None
    review_type: str
    status: str
    reason: str
    current_blob_sha: str
    accepted_note_sha: str | None
    accepted_note_commit: str | None
    accepted_at: str | None
    diff_added_lines: int | None = None
    diff_removed_lines: int | None = None
    diff: str | None = None


def truncate_diff(diff: str | None, limit: int = DIFF_OUTPUT_LIMIT) -> str | None:
    """Clip diff output for JSON emission."""
    if diff is None or len(diff) <= limit:
        return diff
    return diff[:limit]


def render_change_record(
    change: ReviewChange,
    include_status: bool = False,
) -> dict[str, object]:
    """Emit a compact JSON-friendly change record."""
    record: dict[str, object] = {
        "note_path": change.note_path,
        "review_path": change.review_path,
        "reason": change.reason,
    }
    if include_status:
        record["status"] = change.status
    if change.diff is not None:
        record["diff"] = truncate_diff(change.diff)
    return record


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


def extract_body_lines(content: str) -> list[str]:
    """Return body-content lines, excluding frontmatter and the H1 title."""
    lines = strip_frontmatter(content).splitlines()
    while lines and not lines[0].strip():
        lines = lines[1:]
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    return lines


def body_change_ratio(reviewed_text: str, current_text: str) -> float:
    """Measure how much of the body changed, ignoring frontmatter."""
    reviewed_lines = extract_body_lines(reviewed_text)
    current_lines = extract_body_lines(current_text)
    baseline = max(len(reviewed_lines), len(current_lines), 1)
    matcher = difflib.SequenceMatcher(a=reviewed_lines, b=current_lines)
    matched_lines = sum(block.size for block in matcher.get_matching_blocks())
    return 1 - (matched_lines / baseline)


def body_changed_substantially(
    reviewed_text: str,
    current_text: str,
    threshold: float = BODY_REWRITE_THRESHOLD,
) -> bool:
    """Return whether body-only churn exceeds the rewrite threshold."""
    return body_change_ratio(reviewed_text, current_text) > threshold


def build_frontmatter_review_change(
    note: Path,
    review_type: str,
    review_path: Path,
    repo_root: Path,
    current_blob_sha: str,
    accepted_note_sha: str,
    accepted_note_commit: str | None,
    accepted_at: str | None,
    reviewed_text: str,
    current_text: str,
) -> ReviewChange:
    """Compare frontmatter first, then fall back to major body rewrites."""
    reviewed_fm = extract_frontmatter_raw(reviewed_text) or ""
    current_fm = extract_frontmatter_raw(current_text) or ""

    if reviewed_fm != current_fm:
        diff_summary = build_diff_summary(
            reviewed_fm + "\n",
            current_fm + "\n",
            f"{note.name}@{accepted_note_sha[:12]}",
            f"{note.name}@{current_blob_sha[:12]}",
        )
        return ReviewChange(
            note_path=note.relative_to(repo_root).as_posix(),
            review_path=review_path.relative_to(repo_root).as_posix(),
            review_type=review_type,
            status="changed",
            reason="frontmatter-changed",
            current_blob_sha=current_blob_sha,
            accepted_note_sha=accepted_note_sha,
            accepted_note_commit=accepted_note_commit,
            accepted_at=accepted_at,
            diff_added_lines=diff_summary.added_lines,
            diff_removed_lines=diff_summary.removed_lines,
            diff=diff_summary.diff,
        )

    if body_changed_substantially(reviewed_text, current_text):
        diff_summary = build_diff_summary(
            strip_frontmatter(reviewed_text),
            strip_frontmatter(current_text),
            f"{note.name}@{accepted_note_sha[:12]}",
            f"{note.name}@{current_blob_sha[:12]}",
        )
        return ReviewChange(
            note_path=note.relative_to(repo_root).as_posix(),
            review_path=review_path.relative_to(repo_root).as_posix(),
            review_type=review_type,
            status="changed",
            reason="body-major-rewrite",
            current_blob_sha=current_blob_sha,
            accepted_note_sha=accepted_note_sha,
            accepted_note_commit=accepted_note_commit,
            accepted_at=accepted_at,
            diff_added_lines=diff_summary.added_lines,
            diff_removed_lines=diff_summary.removed_lines,
            diff=diff_summary.diff,
        )

    return ReviewChange(
        note_path=note.relative_to(repo_root).as_posix(),
        review_path=review_path.relative_to(repo_root).as_posix(),
        review_type=review_type,
        status="unchanged",
        reason="frontmatter-unchanged",
        current_blob_sha=current_blob_sha,
        accepted_note_sha=accepted_note_sha,
        accepted_note_commit=accepted_note_commit,
        accepted_at=accepted_at,
    )


def build_change_record(
    note: Path,
    review_type: str,
    reviews_dir: Path,
    repo_root: Path,
    *,
    frontmatter_only: bool = False,
) -> ReviewChange:
    """Compare a note against its stored review revision metadata."""
    review_path = review_path_for(note, review_type, reviews_dir)
    current_blob_sha = git_blob_sha(note)

    if not review_path.exists():
        return ReviewChange(
            note_path=note.relative_to(repo_root).as_posix(),
            review_path=None,
            review_type=review_type,
            status="changed",
            reason="missing-review",
            current_blob_sha=current_blob_sha,
            accepted_note_sha=None,
            accepted_note_commit=None,
            accepted_at=None,
        )

    review_text = review_path.read_text(encoding="utf-8")
    metadata = parse_review_metadata(review_text)
    if metadata is None:
        return ReviewChange(
            note_path=note.relative_to(repo_root).as_posix(),
            review_path=review_path.relative_to(repo_root).as_posix(),
            review_type=review_type,
            status="changed",
            reason="missing-metadata",
            current_blob_sha=current_blob_sha,
            accepted_note_sha=None,
            accepted_note_commit=None,
            accepted_at=None,
        )

    accepted_note_sha = resolve_last_accepted_note_sha(repo_root, metadata)
    if accepted_note_sha is None:
        return ReviewChange(
            note_path=note.relative_to(repo_root).as_posix(),
            review_path=review_path.relative_to(repo_root).as_posix(),
            review_type=review_type,
            status="changed",
            reason="invalid-accepted-note-sha",
            current_blob_sha=current_blob_sha,
            accepted_note_sha=metadata.last_accepted_note_sha,
            accepted_note_commit=metadata.last_accepted_note_commit,
            accepted_at=metadata.last_accepted_at,
        )

    if accepted_note_sha == current_blob_sha:
        return ReviewChange(
            note_path=note.relative_to(repo_root).as_posix(),
            review_path=review_path.relative_to(repo_root).as_posix(),
            review_type=review_type,
            status="unchanged",
            reason="blob-match",
            current_blob_sha=current_blob_sha,
            accepted_note_sha=accepted_note_sha,
            accepted_note_commit=metadata.last_accepted_note_commit,
            accepted_at=metadata.last_accepted_at,
        )

    reviewed_text = read_blob(repo_root, accepted_note_sha)
    current_text = note.read_text(encoding="utf-8")

    if frontmatter_only:
        return build_frontmatter_review_change(
            note=note,
            review_type=review_type,
            review_path=review_path,
            repo_root=repo_root,
            current_blob_sha=current_blob_sha,
            accepted_note_sha=accepted_note_sha,
            accepted_note_commit=metadata.last_accepted_note_commit,
            accepted_at=metadata.last_accepted_at,
            reviewed_text=reviewed_text,
            current_text=current_text,
        )

    diff_summary = build_diff_summary(
        reviewed_text,
        current_text,
        f"{note.name}@{accepted_note_sha[:12]}",
        f"{note.name}@{current_blob_sha[:12]}",
    )
    return ReviewChange(
        note_path=note.relative_to(repo_root).as_posix(),
        review_path=review_path.relative_to(repo_root).as_posix(),
        review_type=review_type,
        status="changed",
        reason="content-changed",
        current_blob_sha=current_blob_sha,
        accepted_note_sha=accepted_note_sha,
        accepted_note_commit=metadata.last_accepted_note_commit,
        accepted_at=metadata.last_accepted_at,
        diff_added_lines=diff_summary.added_lines,
        diff_removed_lines=diff_summary.removed_lines,
        diff=diff_summary.diff,
    )


def collect_review_changes(
    notes: list[Path],
    review_type: str,
    reviews_dir: Path,
    repo_root: Path,
    include_unchanged: bool = False,
    *,
    frontmatter_only: bool = False,
) -> list[ReviewChange]:
    """Collect changed-note records for a given review type."""
    changes = [
        build_change_record(
            note, review_type, reviews_dir, repo_root,
            frontmatter_only=frontmatter_only,
        )
        for note in notes
    ]
    if include_unchanged:
        return changes
    return [change for change in changes if change.status != "unchanged"]


def needs_review(note: Path, review_type: str, reviews_dir: Path) -> bool:
    """Compatibility helper: true when the note content differs from the review."""
    record = build_change_record(note, review_type, reviews_dir, note.parents[2])
    return record.status != "unchanged"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "List top-level kb notes, or only notes whose content differs from "
            "the revision recorded in their review files."
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
        help="List all reviewable notes without checking review metadata.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit structured change records instead of plain note paths.",
    )
    parser.add_argument(
        "--include-unchanged",
        action="store_true",
        help="Include unchanged notes in JSON output when a review type is provided.",
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

    if args.include_unchanged and not args.json:
        parser.error("--include-unchanged requires --json")

    notes = list_reviewable_notes(NOTES_DIR)
    if args.all:
        if args.json:
            payload = [
                {
                    "note_path": note.relative_to(REPO_ROOT).as_posix(),
                }
                for note in notes
            ]
            print(json.dumps(payload, indent=2))
            return

        for note in notes:
            print(note.relative_to(REPO_ROOT).as_posix())
        return

    changes = collect_review_changes(
        notes,
        args.review_type,
        REVIEWS_DIR,
        REPO_ROOT,
        include_unchanged=args.include_unchanged,
        frontmatter_only=args.review_type == "frontmatter-review",
    )

    if args.json:
        print(
            json.dumps(
                [
                    render_change_record(
                        change,
                        include_status=args.include_unchanged,
                    )
                    for change in changes
                ],
                indent=2,
            )
        )
        return

    for change in changes:
        print(change.note_path)


if __name__ == "__main__":
    main()
