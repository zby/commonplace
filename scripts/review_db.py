#!/usr/bin/env python3
"""Helpers for the canonical review-store SQLite database."""

from __future__ import annotations

import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from review_metadata import git_blob_sha, iso_now, last_commit_for_path, parse_review_metadata


@dataclass(frozen=True)
class AcceptanceState:
    note_path: str
    gate_id: str
    model_id: str
    accepted_review_id: int | None
    accepted_note_sha: str
    accepted_note_commit: str | None
    accepted_gate_sha: str
    accepted_at: str
    acceptance_kind: str


@dataclass(frozen=True)
class GateReviewRow:
    id: int
    note_path: str
    gate_id: str
    model_id: str
    decision: str
    rationale_markdown: str
    evidence_json: str | None
    gate_sha: str
    reviewed_note_sha: str
    reviewed_note_commit: str | None
    reviewed_at: str
    review_kind: str


_DECISION_RE = re.compile(r"^\*\*(pass|fail|concern|error)\*\*", re.IGNORECASE)


def connect(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def apply_schema(conn: sqlite3.Connection, schema_path: Path) -> None:
    conn.executescript(schema_path.read_text(encoding="utf-8"))


def init_db(db_path: Path, schema_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with connect(db_path) as conn:
        apply_schema(conn, schema_path)
        conn.commit()


def load_current_acceptances(conn: sqlite3.Connection) -> dict[tuple[str, str, str], AcceptanceState]:
    rows = conn.execute(
        """
        SELECT
            note_path,
            gate_id,
            model_id,
            accepted_review_id,
            accepted_note_sha,
            accepted_note_commit,
            accepted_gate_sha,
            accepted_at,
            acceptance_kind
        FROM current_gate_acceptances
        """
    ).fetchall()
    return {
        (row["note_path"], row["gate_id"], row["model_id"]): AcceptanceState(
            note_path=row["note_path"],
            gate_id=row["gate_id"],
            model_id=row["model_id"],
            accepted_review_id=row["accepted_review_id"],
            accepted_note_sha=row["accepted_note_sha"],
            accepted_note_commit=row["accepted_note_commit"],
            accepted_gate_sha=row["accepted_gate_sha"],
            accepted_at=row["accepted_at"],
            acceptance_kind=row["acceptance_kind"],
        )
        for row in rows
    }


def insert_gate_review(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    gate_id: str,
    model_id: str,
    decision: str,
    rationale_markdown: str,
    evidence_json: str | None,
    gate_sha: str,
    reviewed_note_sha: str,
    reviewed_note_commit: str | None,
    reviewed_at: str,
    review_kind: str = "full-review",
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO gate_reviews (
            note_path,
            gate_id,
            model_id,
            decision,
            rationale_markdown,
            evidence_json,
            gate_sha,
            reviewed_note_sha,
            reviewed_note_commit,
            reviewed_at,
            review_kind
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            note_path,
            gate_id,
            model_id,
            decision,
            rationale_markdown,
            evidence_json,
            gate_sha,
            reviewed_note_sha,
            reviewed_note_commit,
            reviewed_at,
            review_kind,
        ),
    )
    return int(cursor.lastrowid)


def append_acceptance_event(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    gate_id: str,
    model_id: str,
    accepted_review_id: int | None,
    accepted_note_sha: str,
    accepted_note_commit: str | None,
    accepted_gate_sha: str,
    accepted_at: str,
    acceptance_kind: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO acceptance_events (
            note_path,
            gate_id,
            model_id,
            accepted_review_id,
            accepted_note_sha,
            accepted_note_commit,
            accepted_gate_sha,
            accepted_at,
            acceptance_kind
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            note_path,
            gate_id,
            model_id,
            accepted_review_id,
            accepted_note_sha,
            accepted_note_commit,
            accepted_gate_sha,
            accepted_at,
            acceptance_kind,
        ),
    )
    return int(cursor.lastrowid)


def parse_review_decision(review_text: str) -> str:
    stripped = review_text.lstrip()
    match = _DECISION_RE.match(stripped)
    if match is not None:
        return match.group(1).lower()
    return "concern"


def model_id_from_review_filename(review_path: Path) -> str:
    parts = review_path.name.split(".")
    if len(parts) >= 3:
        return parts[-2]
    raise ValueError(f"Could not infer model_id from review filename: {review_path}")


def infer_note_path_from_review_path(review_path: Path, reviews_root: Path) -> str:
    try:
        encoded = review_path.relative_to(reviews_root).parent.as_posix()
    except ValueError as exc:
        raise ValueError(f"Review path is not under reviews root: {review_path}") from exc
    if not encoded or encoded == ".":
        raise ValueError(f"Could not infer note_path from review path: {review_path}")
    return encoded.replace("__", "/") + ".md"


def infer_gate_id_from_review_path(review_path: Path) -> str:
    parts = review_path.name.split(".")
    if len(parts) < 3:
        raise ValueError(f"Could not infer gate_id from review filename: {review_path}")
    return parts[0].replace("__", "/")


def import_review_text(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    review_text: str,
    review_path: Path,
    reviews_root: Path,
) -> tuple[int, int]:
    metadata = parse_review_metadata(review_text)
    model_id = model_id_from_review_filename(review_path)

    if metadata is None:
        note_path = infer_note_path_from_review_path(review_path, reviews_root)
        gate_id = infer_gate_id_from_review_path(review_path)
        note_abs = repo_root / note_path
        gate_abs = repo_root / "kb" / "instructions" / "review-gates" / f"{gate_id}.md"
        if not note_abs.is_file():
            raise ValueError(f"Legacy review note not found: {note_path}")
        if not gate_abs.is_file():
            raise ValueError(f"Legacy review gate not found: {gate_id}")
        now = iso_now()
        note_sha = git_blob_sha(note_abs)
        gate_sha = git_blob_sha(gate_abs)
        note_commit = last_commit_for_path(repo_root, Path(note_path))
        metadata_note_path = note_path
        metadata_gate_id = gate_id
        metadata_full_note_sha = note_sha
        metadata_full_note_commit = note_commit
        metadata_full_review_at = now
        metadata_accepted_note_sha = note_sha
        metadata_accepted_note_commit = note_commit
        metadata_accepted_at = now
        metadata_acceptance_kind = "migration-import"
        metadata_gate_sha = gate_sha
    else:
        if metadata.note_path is None or metadata.gate_id is None:
            raise ValueError(f"Review metadata missing note_path or gate_id: {review_path.name}")
        if metadata.last_full_review_note_sha is None or metadata.gate_fingerprint is None:
            raise ValueError(f"Review metadata missing full-review provenance: {review_path.name}")
        if metadata.last_full_review_at is None:
            raise ValueError(f"Review metadata missing last_full_review_at: {review_path.name}")
        if metadata.last_accepted_note_sha is None or metadata.last_accepted_at is None:
            raise ValueError(f"Review metadata missing accepted provenance: {review_path.name}")
        if metadata.last_acceptance_kind is None:
            raise ValueError(f"Review metadata missing acceptance kind: {review_path.name}")
        metadata_note_path = metadata.note_path
        metadata_gate_id = metadata.gate_id
        metadata_full_note_sha = metadata.last_full_review_note_sha
        metadata_full_note_commit = metadata.last_full_review_note_commit
        metadata_full_review_at = metadata.last_full_review_at
        metadata_accepted_note_sha = metadata.last_accepted_note_sha
        metadata_accepted_note_commit = metadata.last_accepted_note_commit
        metadata_accepted_at = metadata.last_accepted_at
        metadata_acceptance_kind = metadata.last_acceptance_kind
        metadata_gate_sha = metadata.gate_fingerprint

    existing_review = conn.execute(
        """
        SELECT id
        FROM gate_reviews
        WHERE note_path = ?
          AND gate_id = ?
          AND model_id = ?
          AND gate_sha = ?
          AND reviewed_note_sha = ?
          AND reviewed_at = ?
          AND review_kind = 'manual-import'
          AND rationale_markdown = ?
        """,
        (
            metadata_note_path,
            metadata_gate_id,
            model_id,
            metadata_gate_sha,
            metadata_full_note_sha,
            metadata_full_review_at,
            review_text,
        ),
    ).fetchone()
    if existing_review is None:
        review_id = insert_gate_review(
            conn,
            note_path=metadata_note_path,
            gate_id=metadata_gate_id,
            model_id=model_id,
            decision=parse_review_decision(review_text),
            rationale_markdown=review_text,
            evidence_json=None,
            gate_sha=metadata_gate_sha,
            reviewed_note_sha=metadata_full_note_sha,
            reviewed_note_commit=metadata_full_note_commit,
            reviewed_at=metadata_full_review_at,
            review_kind="manual-import",
        )
    else:
        review_id = int(existing_review["id"])

    existing_acceptance = conn.execute(
        """
        SELECT id
        FROM acceptance_events
        WHERE note_path = ?
          AND gate_id = ?
          AND model_id = ?
          AND accepted_review_id IS ?
          AND accepted_note_sha = ?
          AND accepted_gate_sha = ?
          AND accepted_at = ?
          AND acceptance_kind = ?
        """,
        (
            metadata_note_path,
            metadata_gate_id,
            model_id,
            review_id,
            metadata_accepted_note_sha,
            metadata_gate_sha,
            metadata_accepted_at,
            metadata_acceptance_kind,
        ),
    ).fetchone()
    if existing_acceptance is None:
        acceptance_id = append_acceptance_event(
            conn,
            note_path=metadata_note_path,
            gate_id=metadata_gate_id,
            model_id=model_id,
            accepted_review_id=review_id,
            accepted_note_sha=metadata_accepted_note_sha,
            accepted_note_commit=metadata_accepted_note_commit,
            accepted_gate_sha=metadata_gate_sha,
            accepted_at=metadata_accepted_at,
            acceptance_kind=metadata_acceptance_kind,
        )
    else:
        acceptance_id = int(existing_acceptance["id"])
    return review_id, acceptance_id


def load_gate_reviews_for_note(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    model_id: str,
) -> list[GateReviewRow]:
    rows = conn.execute(
        """
        SELECT
            id,
            note_path,
            gate_id,
            model_id,
            decision,
            rationale_markdown,
            evidence_json,
            gate_sha,
            reviewed_note_sha,
            reviewed_note_commit,
            reviewed_at,
            review_kind
        FROM gate_reviews
        WHERE note_path = ? AND model_id = ?
        ORDER BY gate_id, reviewed_at, id
        """,
        (note_path, model_id),
    ).fetchall()
    return [
        GateReviewRow(
            id=row["id"],
            note_path=row["note_path"],
            gate_id=row["gate_id"],
            model_id=row["model_id"],
            decision=row["decision"],
            rationale_markdown=row["rationale_markdown"],
            evidence_json=row["evidence_json"],
            gate_sha=row["gate_sha"],
            reviewed_note_sha=row["reviewed_note_sha"],
            reviewed_note_commit=row["reviewed_note_commit"],
            reviewed_at=row["reviewed_at"],
            review_kind=row["review_kind"],
        )
        for row in rows
    ]
