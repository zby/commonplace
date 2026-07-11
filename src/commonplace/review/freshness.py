"""Review freshness helpers for snapshot-backed review inputs.

Freshness hashes exactly the two reviewed inputs: note text and gate text.
The gate side may be a catalog gate or a type spec (type-conformance pairs);
either way the same two hashes decide staleness. The prompt scaffolding
around them (protocol/prompt.py, including the type-conformance wrapper) and
the assembling code itself are deliberately outside the hash — changing them
leaves acceptances fresh. Keep judgment-bearing review criteria in note/gate
files; widening beyond two inputs should stay compatible with this boundary
(see kb/reference/review-architecture.md, freshness mechanism). The default
answer to a new review dependency is a new factored (note, dependency) pair
with the dependency on the gate side, not a wider per-pair input set.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Sequence

import sqlite3

from commonplace.lib import frontmatter
from commonplace.review.review_db import ReviewPairRequest, snapshot_file


@dataclass(frozen=True)
class NoteSnapshot:
    path: str
    content_hash: str


@dataclass(frozen=True)
class GateSnapshot:
    id: str
    content_hash: str


@dataclass(frozen=True)
class AcceptanceSnapshot:
    accepted_note_hash: str
    accepted_gate_hash: str


@dataclass(frozen=True)
class Staleness:
    reason: str


@dataclass(frozen=True)
class CapturedReviewInputs:
    pair_requests: list[ReviewPairRequest]
    note_texts: dict[str, str]
    gate_texts: dict[str, str]


def content_sha256_for_text(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()


def file_content_sha256(path: Path) -> str:
    return content_sha256_for_text(path.read_text(encoding="utf-8"))


def classify_staleness(
    note: NoteSnapshot,
    gate: GateSnapshot,
    acceptance: AcceptanceSnapshot | None,
) -> Staleness | None:
    if acceptance is None:
        return Staleness("missing-review")
    if acceptance.accepted_gate_hash != gate.content_hash:
        return Staleness("gate-changed")
    if acceptance.accepted_note_hash != note.content_hash:
        return Staleness("note-changed")
    return None


def capture_review_inputs(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    pairs: Sequence[tuple[str, str, str]],
) -> CapturedReviewInputs:
    """Snapshot note/gate files and build review-pair requests from those snapshots."""
    note_paths = sorted({note_path for note_path, _, _ in pairs})
    gate_paths = sorted({gate_path for _, gate_path, _ in pairs})

    note_snapshots = {
        note_path: snapshot_file(conn, repo_root=repo_root, path=note_path)
        for note_path in note_paths
    }
    gate_snapshots = {
        gate_path: snapshot_file(conn, repo_root=repo_root, path=gate_path)
        for gate_path in gate_paths
    }

    return CapturedReviewInputs(
        pair_requests=[
            ReviewPairRequest(
                note_path=note_path,
                gate_path=gate_path,
                pair_ordinal=ordinal,
                result_kind=result_kind,
                reviewed_note_snapshot_id=note_snapshots[note_path].snapshot_id,
                reviewed_gate_snapshot_id=gate_snapshots[gate_path].snapshot_id,
            )
            for ordinal, (note_path, gate_path, result_kind) in enumerate(pairs, start=1)
        ],
        note_texts={
            note_path: snapshot.content_text
            for note_path, snapshot in note_snapshots.items()
        },
        gate_texts={
            gate_path: frontmatter.strip(snapshot.content_text).lstrip("\n")
            for gate_path, snapshot in gate_snapshots.items()
        },
    )
