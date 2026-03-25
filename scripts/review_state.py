from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

from frontmatter import extract_raw as extract_frontmatter_raw
from frontmatter import strip as strip_frontmatter
from review_metadata import (
    ReviewMetadata,
    git_blob_sha,
    parse_review_metadata,
    read_blob,
    resolve_last_accepted_note_sha,
)


@dataclass
class NoteCandidate:
    path: Path
    rel_path: str


@dataclass
class NoteSnapshot:
    path: Path
    rel_path: str
    text: str
    blob_sha: str
    frontmatter_raw: str | None
    body_text: str
    body_lines: list[str]


@dataclass
class ReviewState:
    review_type: str
    review_path: Path | None
    metadata: ReviewMetadata | None
    accepted_blob_sha: str | None
    accepted_snapshot: NoteSnapshot | None
    load_error: str | None


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


def note_rel_path(note_path: Path, repo_root: Path) -> str:
    """Return a repository-relative note path."""
    return note_path.relative_to(repo_root).as_posix()


def review_name_for(
    note_path: Path,
    review_type: str,
    notes_root: Path,
) -> str:
    """Build the review filename for a note/review-type pair."""
    rel_path = note_path.relative_to(notes_root)
    stem_parts = list(rel_path.with_suffix("").parts)
    stem = stem_parts[0] if len(stem_parts) == 1 else "__".join(stem_parts)
    return f"{stem}.{review_type}.md"


def review_path_for(
    note_path: Path,
    review_type: str,
    notes_root: Path,
    reviews_root: Path,
) -> Path:
    """Return the review file path for a note/review-type pair."""
    return reviews_root / review_name_for(note_path, review_type, notes_root)


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


def build_note_snapshot(
    note_path: Path,
    repo_root: Path,
    *,
    text: str | None = None,
    blob_sha: str | None = None,
) -> NoteSnapshot:
    """Build a snapshot for a note from disk or provided text."""
    note_text = text if text is not None else note_path.read_text(encoding="utf-8")
    return NoteSnapshot(
        path=note_path,
        rel_path=note_rel_path(note_path, repo_root),
        text=note_text,
        blob_sha=blob_sha or git_blob_sha(note_path),
        frontmatter_raw=extract_frontmatter_raw(note_text),
        body_text=strip_frontmatter(note_text),
        body_lines=extract_body_lines(note_text),
    )


def load_review_state(
    note_path: Path,
    review_type: str,
    repo_root: Path,
    notes_root: Path,
    reviews_root: Path,
) -> ReviewState:
    """Load review metadata and accepted snapshot for one note/review type."""
    review_path = review_path_for(note_path, review_type, notes_root, reviews_root)
    if not review_path.exists():
        return ReviewState(
            review_type=review_type,
            review_path=None,
            metadata=None,
            accepted_blob_sha=None,
            accepted_snapshot=None,
            load_error="missing-review",
        )

    try:
        review_text = review_path.read_text(encoding="utf-8")
    except OSError:
        return ReviewState(
            review_type=review_type,
            review_path=review_path,
            metadata=None,
            accepted_blob_sha=None,
            accepted_snapshot=None,
            load_error="unreadable-review",
        )

    metadata = parse_review_metadata(review_text)
    if metadata is None:
        return ReviewState(
            review_type=review_type,
            review_path=review_path,
            metadata=None,
            accepted_blob_sha=None,
            accepted_snapshot=None,
            load_error="missing-metadata",
        )

    accepted_blob_sha = resolve_last_accepted_note_sha(repo_root, metadata)
    if accepted_blob_sha is None:
        return ReviewState(
            review_type=review_type,
            review_path=review_path,
            metadata=metadata,
            accepted_blob_sha=None,
            accepted_snapshot=None,
            load_error="invalid-accepted-note-sha",
        )

    return ReviewState(
        review_type=review_type,
        review_path=review_path,
        metadata=metadata,
        accepted_blob_sha=accepted_blob_sha,
        accepted_snapshot=None,
        load_error=None,
    )


def ensure_accepted_snapshot(
    review_state: ReviewState,
    note_path: Path,
    repo_root: Path,
) -> ReviewState:
    """Load the accepted note snapshot into review_state when needed."""
    if (
        review_state.load_error is not None
        or review_state.accepted_blob_sha is None
        or review_state.accepted_snapshot is not None
    ):
        return review_state

    try:
        accepted_text = read_blob(repo_root, review_state.accepted_blob_sha)
    except subprocess.CalledProcessError:
        review_state.accepted_blob_sha = None
        review_state.accepted_snapshot = None
        review_state.load_error = "invalid-accepted-note-sha"
        return review_state

    review_state.accepted_snapshot = build_note_snapshot(
        note_path,
        repo_root,
        text=accepted_text,
        blob_sha=review_state.accepted_blob_sha,
    )
    return review_state
