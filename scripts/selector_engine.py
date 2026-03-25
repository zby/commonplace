from __future__ import annotations

import difflib
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from review_metadata import build_diff_summary
from review_state import (
    NoteSnapshot,
    ReviewState,
    build_note_snapshot,
    ensure_accepted_snapshot,
    extract_body_lines,
    load_review_state,
)


DIFF_OUTPUT_LIMIT = 1000
BODY_REWRITE_THRESHOLD = 0.5


@dataclass
class SelectionDecision:
    status: str
    reason: str
    diff_kind: str
    sort_key: object | None = None


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
    diff_kind: str = "none"
    diff_added_lines: int | None = None
    diff_removed_lines: int | None = None
    diff: str | None = None


@dataclass(frozen=True)
class SelectorPolicy:
    name: str
    evaluator: Callable[[NoteSnapshot, ReviewState], SelectionDecision]
    needs_accepted_snapshot: bool = False


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


def _common_decision(
    current_snapshot: NoteSnapshot,
    review_state: ReviewState,
) -> SelectionDecision | None:
    if review_state.load_error == "missing-review":
        return SelectionDecision("changed", "missing-review", "none")
    if review_state.load_error == "unreadable-review":
        return SelectionDecision("changed", "unreadable-review", "none")
    if review_state.load_error == "missing-metadata":
        return SelectionDecision("changed", "missing-metadata", "none")
    if review_state.load_error == "invalid-accepted-note-sha":
        return SelectionDecision("changed", "invalid-accepted-note-sha", "none")
    if review_state.accepted_blob_sha == current_snapshot.blob_sha:
        return SelectionDecision("unchanged", "blob-match", "none")
    return None


def _full_text_decision(
    current_snapshot: NoteSnapshot,
    review_state: ReviewState,
) -> SelectionDecision:
    common = _common_decision(current_snapshot, review_state)
    if common is not None:
        return common
    return SelectionDecision("changed", "content-changed", "full")


def _frontmatter_decision(
    current_snapshot: NoteSnapshot,
    review_state: ReviewState,
) -> SelectionDecision:
    common = _common_decision(current_snapshot, review_state)
    if common is not None:
        return common

    accepted_snapshot = review_state.accepted_snapshot
    assert accepted_snapshot is not None

    if accepted_snapshot.frontmatter_raw != current_snapshot.frontmatter_raw:
        return SelectionDecision("changed", "frontmatter-changed", "frontmatter")

    baseline = max(len(accepted_snapshot.body_lines), len(current_snapshot.body_lines), 1)
    matcher = difflib.SequenceMatcher(
        a=accepted_snapshot.body_lines,
        b=current_snapshot.body_lines,
    )
    matched_lines = sum(block.size for block in matcher.get_matching_blocks())
    rewrite_ratio = 1 - (matched_lines / baseline)
    if rewrite_ratio > BODY_REWRITE_THRESHOLD:
        return SelectionDecision("changed", "body-major-rewrite", "body")

    return SelectionDecision("unchanged", "frontmatter-unchanged", "none")


SELECTOR_POLICIES = {
    "prose-review": SelectorPolicy("prose-review", _full_text_decision),
    "semantic-review": SelectorPolicy("semantic-review", _full_text_decision),
    "frontmatter-review": SelectorPolicy(
        "frontmatter-review",
        _frontmatter_decision,
        needs_accepted_snapshot=True,
    ),
}


def get_selector_policy(review_type: str) -> SelectorPolicy:
    """Return the configured selector policy for review_type."""
    try:
        return SELECTOR_POLICIES[review_type]
    except KeyError as exc:
        supported = ", ".join(sorted(SELECTOR_POLICIES))
        raise ValueError(
            f"unknown review type: {review_type} (supported: {supported})"
        ) from exc


def _diff_texts(
    diff_kind: str,
    accepted_snapshot: NoteSnapshot,
    current_snapshot: NoteSnapshot,
) -> tuple[str, str]:
    if diff_kind == "frontmatter":
        return (
            (accepted_snapshot.frontmatter_raw or "") + "\n",
            (current_snapshot.frontmatter_raw or "") + "\n",
        )
    if diff_kind == "body":
        return accepted_snapshot.body_text, current_snapshot.body_text
    return accepted_snapshot.text, current_snapshot.text


def _materialize_diff(
    change: ReviewChange,
    current_snapshot: NoteSnapshot,
    accepted_snapshot: NoteSnapshot | None,
) -> ReviewChange:
    if change.diff_kind == "none" or accepted_snapshot is None:
        return change

    reviewed_text, current_text = _diff_texts(
        change.diff_kind,
        accepted_snapshot,
        current_snapshot,
    )
    accepted_sha = change.accepted_note_sha or "unknown"
    diff_summary = build_diff_summary(
        reviewed_text,
        current_text,
        f"{current_snapshot.path.name}@{accepted_sha[:12]}",
        f"{current_snapshot.path.name}@{current_snapshot.blob_sha[:12]}",
    )
    change.diff_added_lines = diff_summary.added_lines
    change.diff_removed_lines = diff_summary.removed_lines
    change.diff = diff_summary.diff
    return change


def build_change_record(
    note_path: Path,
    review_type: str,
    reviews_root: Path,
    repo_root: Path,
    *,
    include_diff: bool = True,
    notes_root: Path | None = None,
) -> ReviewChange:
    """Compare a note against its stored review revision metadata."""
    resolved_notes_root = notes_root or (repo_root / "kb" / "notes")
    current_snapshot = build_note_snapshot(note_path, repo_root)
    review_state = load_review_state(
        note_path,
        review_type,
        repo_root,
        resolved_notes_root,
        reviews_root,
    )
    policy = get_selector_policy(review_type)
    if (
        policy.needs_accepted_snapshot
        and review_state.load_error is None
        and review_state.accepted_blob_sha != current_snapshot.blob_sha
    ):
        ensure_accepted_snapshot(review_state, note_path, repo_root)
    decision = policy.evaluator(current_snapshot, review_state)

    metadata = review_state.metadata
    review_path = (
        review_state.review_path.relative_to(repo_root).as_posix()
        if review_state.review_path is not None
        else None
    )
    change = ReviewChange(
        note_path=current_snapshot.rel_path,
        review_path=review_path,
        review_type=review_type,
        status=decision.status,
        reason=decision.reason,
        current_blob_sha=current_snapshot.blob_sha,
        accepted_note_sha=(
            review_state.accepted_blob_sha
            or (metadata.last_accepted_note_sha if metadata is not None else None)
        ),
        accepted_note_commit=(
            metadata.last_accepted_note_commit if metadata is not None else None
        ),
        accepted_at=metadata.last_accepted_at if metadata is not None else None,
        diff_kind=decision.diff_kind,
    )
    if include_diff and change.diff_kind != "none" and review_state.accepted_snapshot is None:
        ensure_accepted_snapshot(review_state, note_path, repo_root)
        if review_state.load_error is not None:
            change.reason = review_state.load_error
            change.diff_kind = "none"
            change.accepted_note_sha = (
                metadata.last_accepted_note_sha if metadata is not None else None
            )
            return change
    if include_diff:
        return _materialize_diff(
            change,
            current_snapshot,
            review_state.accepted_snapshot,
        )
    return change


def collect_review_changes(
    notes: list[Path],
    review_type: str,
    reviews_root: Path,
    repo_root: Path,
    include_unchanged: bool = False,
    *,
    include_diff: bool = False,
    notes_root: Path | None = None,
) -> list[ReviewChange]:
    """Collect review records for a given review type."""
    changes = [
        build_change_record(
            note,
            review_type,
            reviews_root,
            repo_root,
            include_diff=include_diff,
            notes_root=notes_root,
        )
        for note in notes
    ]
    if include_unchanged:
        return changes
    return [change for change in changes if change.status != "unchanged"]


def needs_review(
    note_path: Path,
    review_type: str,
    reviews_root: Path,
    *,
    repo_root: Path | None = None,
    notes_root: Path | None = None,
) -> bool:
    """Return whether a note differs from its accepted review revision."""
    resolved_repo_root = repo_root or note_path.parents[2]
    change = build_change_record(
        note_path,
        review_type,
        reviews_root,
        resolved_repo_root,
        include_diff=False,
        notes_root=notes_root,
    )
    return change.status != "unchanged"
