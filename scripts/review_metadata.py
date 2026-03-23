from __future__ import annotations

import difflib
import hashlib
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


HEX_SHA_PATTERN = re.compile(r"^[0-9a-f]{40}$")
METADATA_PATTERN = re.compile(
    r"^<!-- REVIEW-METADATA\n(.*?)\n-->\n?",
    re.DOTALL,
)
REVIEW_HEADER_PATTERN = re.compile(r"===\s+\w[\w\s]+:\s+(\S+\.md)\s+===")


@dataclass
class ReviewMetadata:
    note_path: str
    last_full_review_note_sha: str
    last_accepted_note_sha: str
    last_full_review_at: str | None = None
    last_full_review_note_commit: str | None = None
    last_accepted_at: str | None = None
    last_accepted_note_commit: str | None = None
    last_acceptance_kind: str = "full-review"
    review_type: str | None = None


@dataclass
class DiffSummary:
    added_lines: int
    removed_lines: int
    diff: str


def detect_review_type(path: Path) -> str | None:
    """Extract the review type from a filename like foo.prose-review.md."""
    stem = path.stem
    parts = stem.rsplit(".", 1)
    if len(parts) == 2:
        return parts[1]
    return None


def extract_note_filename(review_text: str) -> str | None:
    """Extract the reviewed note filename from a review body."""
    match = REVIEW_HEADER_PATTERN.search(review_text)
    if not match:
        return None
    return match.group(1)


def parse_review_metadata(review_text: str) -> ReviewMetadata | None:
    """Parse the optional review metadata comment at the top of a review file."""
    match = METADATA_PATTERN.match(review_text)
    if not match:
        return None

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()

    note_path = fields.get("note-path") or fields.get("reviewed-path")
    last_full_review_note_sha = (
        fields.get("last-full-review-note-sha")
        or fields.get("reviewed-blob-sha")
    )
    last_accepted_note_sha = (
        fields.get("last-accepted-note-sha")
        or last_full_review_note_sha
    )
    if not note_path or not last_full_review_note_sha or not last_accepted_note_sha:
        return None

    return ReviewMetadata(
        note_path=note_path,
        last_full_review_note_sha=last_full_review_note_sha,
        last_accepted_note_sha=last_accepted_note_sha,
        last_full_review_at=(
            fields.get("last-full-review-at")
            or fields.get("reviewed-at")
        ),
        last_full_review_note_commit=(
            fields.get("last-full-review-note-commit")
            or fields.get("reviewed-commit")
        ),
        last_accepted_at=(
            fields.get("last-accepted-at")
            or fields.get("last-full-review-at")
            or fields.get("reviewed-at")
        ),
        last_accepted_note_commit=(
            fields.get("last-accepted-note-commit")
            or fields.get("last-full-review-note-commit")
            or fields.get("reviewed-commit")
        ),
        last_acceptance_kind=fields.get("last-acceptance-kind") or "full-review",
        review_type=fields.get("review-type"),
    )


def strip_review_metadata(review_text: str) -> str:
    """Remove the leading metadata comment if present."""
    return METADATA_PATTERN.sub("", review_text, count=1)


def render_review_metadata(metadata: ReviewMetadata) -> str:
    """Render review metadata as a leading HTML comment block."""
    lines = [
        "<!-- REVIEW-METADATA",
        f"note-path: {metadata.note_path}",
        f"last-full-review-note-sha: {metadata.last_full_review_note_sha}",
    ]
    if metadata.last_full_review_note_commit:
        lines.append(
            f"last-full-review-note-commit: {metadata.last_full_review_note_commit}"
        )
    if metadata.last_full_review_at:
        lines.append(f"last-full-review-at: {metadata.last_full_review_at}")
    lines.append(f"last-accepted-note-sha: {metadata.last_accepted_note_sha}")
    if metadata.last_accepted_note_commit:
        lines.append(
            f"last-accepted-note-commit: {metadata.last_accepted_note_commit}"
        )
    if metadata.last_accepted_at:
        lines.append(f"last-accepted-at: {metadata.last_accepted_at}")
    if metadata.last_acceptance_kind:
        lines.append(f"last-acceptance-kind: {metadata.last_acceptance_kind}")
    if metadata.review_type:
        lines.append(f"review-type: {metadata.review_type}")
    lines.append("-->")
    return "\n".join(lines) + "\n"


def inject_review_metadata(review_text: str, metadata: ReviewMetadata) -> str:
    """Add or replace the leading review metadata comment."""
    body = strip_review_metadata(review_text).lstrip("\n")
    return render_review_metadata(metadata) + body


def git_blob_sha(path: Path) -> str:
    """Compute the git-style blob hash for a file's current content."""
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("utf-8")
    return hashlib.sha1(header + data).hexdigest()


def read_blob(repo_root: Path, blob_sha: str) -> str:
    """Read blob content from git object storage."""
    result = subprocess.run(
        ["git", "show", blob_sha],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def is_hex_blob_sha(value: str) -> bool:
    """Return whether value looks like a raw git object SHA."""
    return bool(HEX_SHA_PATTERN.fullmatch(value))


def run_git(
    repo_root: Path,
    *args: str,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    """Run a git command in repo_root."""
    return subprocess.run(
        ["git", *args],
        cwd=repo_root,
        check=check,
        capture_output=True,
        text=True,
    )


def last_commit_for_path(repo_root: Path, path: Path) -> str | None:
    """Return the last commit touching path."""
    rel = path.as_posix()
    result = run_git(
        repo_root,
        "log",
        "-1",
        "--format=%H",
        "--",
        rel,
        check=False,
    )
    if result.returncode != 0:
        return None
    value = result.stdout.strip()
    return value or None


def last_commit_timestamp_for_path(repo_root: Path, path: Path) -> str | None:
    """Return the last commit timestamp touching path."""
    rel = path.as_posix()
    result = run_git(
        repo_root,
        "log",
        "-1",
        "--format=%cI",
        "--",
        rel,
        check=False,
    )
    if result.returncode != 0:
        return None
    value = result.stdout.strip()
    return value or None


def blob_sha_at_commit(repo_root: Path, commit: str, path: Path) -> str | None:
    """Return the blob SHA for path at commit, if available."""
    rel = path.as_posix()
    result = run_git(
        repo_root,
        "rev-parse",
        "--verify",
        f"{commit}:{rel}",
        check=False,
    )
    if result.returncode != 0:
        return None
    value = result.stdout.strip()
    if not value or not is_hex_blob_sha(value):
        return None
    return value


def resolve_blob_reference(repo_root: Path, blob_ref: str) -> str | None:
    """Resolve a raw blob SHA or blob-ish revspec to a raw blob SHA."""
    if is_hex_blob_sha(blob_ref):
        return blob_ref

    ref = blob_ref
    if ":" not in blob_ref:
        ref = f"{blob_ref}^{{blob}}"

    result = run_git(
        repo_root,
        "rev-parse",
        "--verify",
        ref,
        check=False,
    )
    if result.returncode != 0:
        return None

    value = result.stdout.strip()
    if not value or not is_hex_blob_sha(value):
        return None
    return value


def resolve_reviewed_blob_sha(
    repo_root: Path,
    metadata: ReviewMetadata,
) -> str | None:
    """Resolve the last accepted note SHA to a raw blob SHA."""
    resolved = resolve_blob_reference(repo_root, metadata.last_accepted_note_sha)
    if resolved is not None:
        return resolved

    if metadata.last_accepted_note_commit:
        return blob_sha_at_commit(
            repo_root,
            metadata.last_accepted_note_commit,
            Path(metadata.note_path),
        )
    return None


def resolve_last_accepted_note_sha(
    repo_root: Path,
    metadata: ReviewMetadata,
) -> str | None:
    """Resolve the accepted note revision to a raw blob SHA."""
    return resolve_reviewed_blob_sha(repo_root, metadata)


def build_diff_summary(
    reviewed_text: str,
    current_text: str,
    reviewed_label: str,
    current_label: str,
) -> DiffSummary:
    """Build a zero-context unified diff and added/removed line counts."""
    old_lines = reviewed_text.splitlines(keepends=True)
    new_lines = current_text.splitlines(keepends=True)
    matcher = difflib.SequenceMatcher(a=old_lines, b=new_lines)
    added_lines = 0
    removed_lines = 0

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag in ("replace", "delete"):
            removed_lines += i2 - i1
        if tag in ("replace", "insert"):
            added_lines += j2 - j1

    diff = "".join(
        difflib.unified_diff(
            old_lines,
            new_lines,
            fromfile=reviewed_label,
            tofile=current_label,
            n=0,
        )
    )

    return DiffSummary(
        added_lines=added_lines,
        removed_lines=removed_lines,
        diff=diff,
    )
