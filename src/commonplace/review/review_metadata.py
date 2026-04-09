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
_LEGACY_NOTE_HEADER_RE = re.compile(
    r"^===\s+[A-Z0-9 _-]+ REVIEW:\s+(?P<filename>.+?\.md)\s+===\s*$",
    re.MULTILINE,
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


def extract_note_filename(review_text: str) -> str | None:
    match = _LEGACY_NOTE_HEADER_RE.search(review_text)
    if match is None:
        return None
    return match.group("filename")


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
