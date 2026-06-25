"""Review freshness helpers for snapshot-backed review inputs."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Sequence

import sqlite3

from commonplace.lib import frontmatter
from commonplace.review.review_db import ReviewPairRequest, snapshot_file
from commonplace.review.review_metadata import git_blob_sha, review_note_provenance


@dataclass(frozen=True)
class CapturedReviewInputs:
    pair_requests: list[ReviewPairRequest]
    note_texts: dict[str, str]
    gate_texts: dict[str, str]


def content_sha256_for_text(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()


def file_content_sha256(path: Path) -> str:
    return content_sha256_for_text(path.read_text(encoding="utf-8"))


def capture_review_inputs(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    pairs: Sequence[tuple[str, str]],
) -> CapturedReviewInputs:
    """Snapshot note/gate files and build review-pair requests from those snapshots.

    The legacy SHA columns are still populated until the destructive migration
    drops them, but prompt text and accepted baselines can now refer to the
    captured snapshot IDs.
    """
    note_paths = sorted({note_path for note_path, _ in pairs})
    gate_paths = sorted({gate_path for _, gate_path in pairs})

    note_snapshots = {
        note_path: snapshot_file(conn, repo_root=repo_root, path=note_path)
        for note_path in note_paths
    }
    gate_snapshots = {
        gate_path: snapshot_file(conn, repo_root=repo_root, path=gate_path)
        for gate_path in gate_paths
    }
    note_provenance = {
        note_path: review_note_provenance(repo_root, Path(note_path))
        for note_path in note_paths
    }
    gate_shas = {
        gate_path: git_blob_sha(repo_root / gate_path)
        for gate_path in gate_paths
    }

    return CapturedReviewInputs(
        pair_requests=[
            ReviewPairRequest(
                note_path=note_path,
                gate_path=gate_path,
                gate_sha=gate_shas[gate_path],
                reviewed_note_sha=note_provenance[note_path][0],
                reviewed_note_commit=note_provenance[note_path][1],
                reviewed_note_snapshot_id=note_snapshots[note_path].snapshot_id,
                reviewed_gate_snapshot_id=gate_snapshots[gate_path].snapshot_id,
                pair_ordinal=ordinal,
            )
            for ordinal, (note_path, gate_path) in enumerate(pairs)
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
