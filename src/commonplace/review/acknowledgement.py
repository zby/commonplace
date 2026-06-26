"""Acknowledge review pairs by advancing their accepted snapshot baseline."""

from __future__ import annotations

from pathlib import Path

from commonplace.review.clock import iso_now
from commonplace.review.paths import gate_id_from_stored_path, normalize_gate_path
from commonplace.review.review_db import (
    append_acceptance_event,
    connect,
    ensure_db,
    resolve_db_path,
    snapshot_file,
)
from commonplace.review.review_model import normalize_model_partition


def ack_pairs(
    repo_root: Path,
    pairs: list[str],
    model: str,
    *,
    db_path: Path | None = None,
) -> list[tuple[str, str]]:
    model = normalize_model_partition(model)
    if db_path is None:
        db_path = resolve_db_path(repo_root)
    ensure_db(db_path)
    acked: list[tuple[str, str]] = []
    with connect(db_path) as conn:
        for pair in pairs:
            if ":" not in pair:
                raise ValueError(f"invalid pair (expected note:gate): {pair}")
            note_path, raw_gate = pair.split(":", 1)
            gate_path = normalize_gate_path(repo_root, raw_gate)
            note_abs = repo_root / note_path
            gate_abs = repo_root / gate_path
            if not note_abs.is_file():
                raise FileNotFoundError(f"note not found: {note_path}")
            if not gate_abs.is_file():
                raise FileNotFoundError(f"gate not found: {gate_path}")

            note_snapshot = snapshot_file(conn, repo_root=repo_root, path=note_path)
            gate_snapshot = snapshot_file(conn, repo_root=repo_root, path=gate_path)
            append_acceptance_event(
                conn,
                note_path=note_path,
                gate_path=gate_path,
                model_partition=model,
                accepted_review_pair_id=None,
                accepted_note_snapshot_id=note_snapshot.snapshot_id,
                accepted_gate_snapshot_id=gate_snapshot.snapshot_id,
                accepted_at=iso_now(),
            )
            acked.append((note_path, gate_id_from_stored_path(gate_path)))
        conn.commit()
    return acked
