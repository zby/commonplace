#!/usr/bin/env python3
"""Helpers for review metadata blocks and git-backed review provenance."""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


METADATA_HEADER = "<!-- REVIEW-METADATA"
_METADATA_BLOCK_RE = re.compile(
    r"\A<!-- REVIEW-METADATA\n(?P<body>.*?)\n-->\n?",
    re.DOTALL,
)


@dataclass(frozen=True)
class ReviewMetadata:
    note_path: str | None = None
    last_full_review_note_sha: str | None = None
    last_full_review_note_commit: str | None = None
    last_full_review_at: str | None = None
    last_accepted_note_sha: str | None = None
    last_accepted_note_commit: str | None = None
    last_accepted_at: str | None = None
    last_acceptance_kind: str | None = None
    review_type: str | None = None
    gate_id: str | None = None
    gate_fingerprint: str | None = None


def iso_now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def _normalize_metadata_value(value: str | None) -> str | None:
    if value is None:
        return None
    normalized = value.strip()
    return normalized or None


def parse_review_metadata(review_text: str) -> ReviewMetadata | None:
    match = _METADATA_BLOCK_RE.match(review_text)
    if match is None:
        return None

    fields: dict[str, str | None] = {}
    for raw_line in match.group("body").splitlines():
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        fields[key.strip()] = _normalize_metadata_value(value)

    return ReviewMetadata(
        note_path=fields.get("note-path"),
        last_full_review_note_sha=fields.get("last-full-review-note-sha"),
        last_full_review_note_commit=fields.get("last-full-review-note-commit"),
        last_full_review_at=fields.get("last-full-review-at"),
        last_accepted_note_sha=fields.get("last-accepted-note-sha"),
        last_accepted_note_commit=fields.get("last-accepted-note-commit"),
        last_accepted_at=fields.get("last-accepted-at"),
        last_acceptance_kind=fields.get("last-acceptance-kind"),
        review_type=fields.get("review-type"),
        gate_id=fields.get("gate-id"),
        gate_fingerprint=fields.get("gate-fingerprint"),
    )


def render_review_metadata(metadata: ReviewMetadata) -> str:
    lines = [METADATA_HEADER]
    fields = [
        ("note-path", metadata.note_path),
        ("gate-id", metadata.gate_id),
        ("gate-fingerprint", metadata.gate_fingerprint),
        ("last-full-review-note-sha", metadata.last_full_review_note_sha),
        ("last-full-review-note-commit", metadata.last_full_review_note_commit),
        ("last-full-review-at", metadata.last_full_review_at),
        ("last-accepted-note-sha", metadata.last_accepted_note_sha),
        ("last-accepted-note-commit", metadata.last_accepted_note_commit),
        ("last-accepted-at", metadata.last_accepted_at),
        ("last-acceptance-kind", metadata.last_acceptance_kind),
        ("review-type", metadata.review_type),
    ]
    for key, value in fields:
        if value is None:
            lines.append(f"{key}:")
        else:
            lines.append(f"{key}: {value}")
    lines.append("-->")
    return "\n".join(lines)


def inject_review_metadata(review_text: str, metadata: ReviewMetadata) -> str:
    metadata_block = render_review_metadata(metadata)
    match = _METADATA_BLOCK_RE.match(review_text)
    if match is not None:
        remainder = review_text[match.end() :].lstrip("\n")
        return f"{metadata_block}\n{remainder}" if remainder else f"{metadata_block}\n"

    remainder = review_text.lstrip("\n")
    return f"{metadata_block}\n{remainder}" if remainder else f"{metadata_block}\n"


def detect_review_type(review_path: Path) -> str:
    parts = review_path.name.split(".")
    if len(parts) >= 3:
        return parts[-2]
    return review_path.stem


def _run_git(repo_root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )


def git_blob_sha(path: Path) -> str:
    cmd = ["git", "hash-object", str(path)]
    result = subprocess.run(
        cmd,
        cwd=path.parent,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def review_note_provenance(repo_root: Path, path: Path) -> tuple[str, str | None]:
    if path.is_absolute():
        file_abs = path.resolve()
    else:
        file_abs = (repo_root / path).resolve()

    # Outside a git checkout we still need a SHA to record the acceptance against;
    # fall back to the worktree blob SHA with no commit (same shape as a dirty file).
    if not (repo_root / ".git").exists():
        return git_blob_sha(file_abs), None

    file_path = file_abs.relative_to(repo_root.resolve())

    status = _run_git(repo_root, ["status", "--porcelain", "--", file_path.as_posix()])
    if status.returncode != 0:
        message = status.stderr.strip() or f"failed to inspect git status for {file_path.as_posix()}"
        raise ValueError(message)

    if status.stdout.strip():
        return git_blob_sha(file_abs), None

    file_commit = last_commit_for_path(repo_root, file_path)
    if file_commit is None:
        return git_blob_sha(file_abs), None

    file_sha = blob_sha_at_commit(repo_root, file_commit, file_path)
    if file_sha is None:
        return git_blob_sha(file_abs), None
    return file_sha, file_commit


def committed_file_provenance(repo_root: Path, path: Path, *, kind: str) -> tuple[str, str]:
    if path.is_absolute():
        file_abs = path.resolve()
    else:
        file_abs = (repo_root / path).resolve()
    file_path = file_abs.relative_to(repo_root.resolve())

    status = _run_git(repo_root, ["status", "--porcelain", "--", file_path.as_posix()])
    if status.returncode != 0:
        message = status.stderr.strip() or f"failed to inspect git status for {file_path.as_posix()}"
        raise ValueError(message)
    if status.stdout.strip():
        raise ValueError(
            f"{kind} has uncommitted changes: {file_path.as_posix()} "
            f"(review baselines must come from committed {kind} content)"
        )

    file_commit = last_commit_for_path(repo_root, file_path)
    if file_commit is None:
        raise ValueError(
            f"{kind} is not committed: {file_path.as_posix()} "
            f"(review baselines must come from committed {kind} content)"
        )

    file_sha = blob_sha_at_commit(repo_root, file_commit, file_path)
    if file_sha is None:
        raise ValueError(f"failed to resolve committed blob for {file_path.as_posix()} at {file_commit}")
    return file_sha, file_commit


def committed_note_provenance(repo_root: Path, path: Path) -> tuple[str, str]:
    return committed_file_provenance(repo_root, path, kind="note")


def last_commit_for_path(repo_root: Path, path: Path) -> str | None:
    result = _run_git(repo_root, ["log", "-1", "--format=%H", "--", path.as_posix()])
    commit = result.stdout.strip()
    return commit or None


def last_commit_timestamp_for_path(repo_root: Path, path: Path) -> str | None:
    result = _run_git(repo_root, ["log", "-1", "--format=%cI", "--", path.as_posix()])
    timestamp = result.stdout.strip()
    return timestamp or None


def blob_sha_at_commit(repo_root: Path, commit: str, path: Path) -> str | None:
    result = _run_git(repo_root, ["rev-parse", f"{commit}:{path.as_posix()}"])
    blob_sha = result.stdout.strip()
    return blob_sha or None


def blob_text_at_sha(repo_root: Path, blob_sha: str) -> str | None:
    result = _run_git(repo_root, ["cat-file", "-p", blob_sha])
    if result.returncode != 0:
        return None
    return result.stdout


def file_text_at_commit(repo_root: Path, commit: str, path: Path) -> str | None:
    result = _run_git(repo_root, ["show", f"{commit}:{path.as_posix()}"])
    if result.returncode != 0:
        return None
    return result.stdout


def resolve_review_target(
    repo_root: Path,
    note_path: str,
    gate_or_bundle: list[str],
) -> tuple[str, str | None, str, list[tuple[str, str, int]], dict[str, str]]:
    """Resolve gates and capture provenance for a review target.

    Returns (note_sha, note_commit, started_at, run_gates, gate_texts) where:
    - run_gates: list of (gate_path, gate_sha, ordinal) tuples for review-pair requests
    - gate_texts: dict of gate_path -> gate body text (frontmatter stripped)

    Raises ValueError if note provenance or gate provenance cannot be resolved,
    or if no applicable gates are found.
    """
    from commonplace.lib import frontmatter
    from commonplace.review.paths import gate_path_for_id, review_gates_dir
    from commonplace.review.resolve_gates import applicable_gate_ids_for_note, resolve_to_gate_ids

    note_abs = repo_root / note_path
    gates_dir = review_gates_dir(repo_root)
    requested_gate_ids = resolve_to_gate_ids(gate_or_bundle, gates_dir)
    gate_ids = applicable_gate_ids_for_note(note_abs, requested_gate_ids, gates_dir)
    if not gate_ids:
        raise ValueError(f"no applicable gates resolved for note: {note_path}")

    note_sha, note_commit = review_note_provenance(repo_root, Path(note_path))
    started_at = iso_now()

    run_gates: list[tuple[str, str, int]] = []
    gate_texts: dict[str, str] = {}
    for ordinal, gate_id in enumerate(gate_ids):
        gate_abs = gates_dir / f"{gate_id}.md"
        if not gate_abs.is_file():
            raise ValueError(f"gate not found: {gate_id}")
        gate_path = gate_path_for_id(repo_root, gate_id)
        gate_sha = git_blob_sha(gate_abs)
        run_gates.append((gate_path, gate_sha, ordinal))
        gate_texts[gate_path] = frontmatter.strip(gate_abs.read_text(encoding="utf-8")).lstrip("\n")

    return note_sha, note_commit, started_at, run_gates, gate_texts


def file_text_at_provenance(
    repo_root: Path,
    *,
    path: Path,
    commit: str | None = None,
    blob_sha: str | None = None,
) -> str | None:
    if commit:
        text = file_text_at_commit(repo_root, commit, path)
        if text is not None:
            return text
    if blob_sha:
        return blob_text_at_sha(repo_root, blob_sha)
    return None
