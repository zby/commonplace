"""Freshness helpers for snapshot-backed assay inputs.

Freshness hashes exactly the two evaluated inputs: note text and criterion
text. The persisted `criterion_path` side may be a catalog gate, a type spec, a
COLLECTION.md contract, or the critique instruction; the same two hashes
decide staleness. The prompt scaffolding around them (protocol/prompt.py,
including the conformance wrappers) and
the assembling code itself are deliberately outside the hash — changing them
leaves freshness_baselines fresh. Keep judgment-bearing review criteria in note/criterion
files; widening beyond two inputs should stay compatible with this boundary
(see kb/reference/review-architecture.md, freshness mechanism). The default
answer to a new review dependency is a new factored (note, dependency) pair
with the dependency on the criterion side, not a wider per-pair input set.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import sqlite3

from commonplace.lib import frontmatter
from commonplace.review.review_db import ReviewPairRequest, snapshot_file


@dataclass(frozen=True)
class CapturedReviewInputs:
    pair_requests: list[ReviewPairRequest]
    note_texts: dict[str, str]
    criterion_texts: dict[str, str]


def capture_review_inputs(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    pairs: Sequence[tuple[str, str, str]],
) -> CapturedReviewInputs:
    """Snapshot note/criterion files and build assay-pair requests from them."""
    note_paths = sorted({note_path for note_path, _, _ in pairs})
    criterion_paths = sorted({criterion_path for _, criterion_path, _ in pairs})

    note_snapshots = {
        note_path: snapshot_file(conn, repo_root=repo_root, path=note_path)
        for note_path in note_paths
    }
    criterion_snapshots = {
        criterion_path: snapshot_file(conn, repo_root=repo_root, path=criterion_path)
        for criterion_path in criterion_paths
    }

    return CapturedReviewInputs(
        pair_requests=[
            ReviewPairRequest(
                note_path=note_path,
                criterion_path=criterion_path,
                pair_ordinal=ordinal,
                result_kind=result_kind,
                reviewed_note_snapshot_id=note_snapshots[note_path].snapshot_id,
                reviewed_criterion_snapshot_id=criterion_snapshots[criterion_path].snapshot_id,
            )
            for ordinal, (note_path, criterion_path, result_kind) in enumerate(pairs, start=1)
        ],
        note_texts={
            note_path: snapshot.content_text
            for note_path, snapshot in note_snapshots.items()
        },
        criterion_texts={
            criterion_path: frontmatter.strip(snapshot.content_text).lstrip("\n")
            for criterion_path, snapshot in criterion_snapshots.items()
        },
    )
