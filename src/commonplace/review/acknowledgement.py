"""Acknowledge review pairs by advancing their accepted snapshot baseline."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

from commonplace.review.artifacts import bundle_artifact_dir
from commonplace.review.clock import iso_now
from commonplace.review.paths import gate_id_from_stored_path, normalize_gate_path
from commonplace.review.review_db import (
    connect,
    ensure_db,
    load_latest_completed_review_pair,
    prune_superseded_acceptances,
    resolve_db_path,
    snapshot_file,
    upsert_acceptance,
)
from commonplace.review.review_model import normalize_model_partition


@dataclass(frozen=True)
class AckPair:
    note_path: str
    gate_path: str
    accepted_review_pair_id: int


def _normalize_note_path(repo_root: Path, raw: str) -> str:
    note_path = raw.strip()
    if not note_path:
        raise ValueError("note path must not be empty")
    normalized = Path(note_path).as_posix()
    path_parts = Path(normalized).parts
    if (
        Path(normalized).is_absolute()
        or normalized == "."
        or normalized.startswith("../")
        or ".." in path_parts
    ):
        raise ValueError(f"note path must be repo-relative: {raw}")
    if not (repo_root / normalized).is_file():
        raise FileNotFoundError(f"note not found: {normalized}")
    return normalized


def _normalize_requested_pairs(repo_root: Path, pairs: list[str]) -> list[tuple[str, str]]:
    normalized_pairs: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for pair in pairs:
        if ":" not in pair:
            raise ValueError(f"invalid pair (expected note:gate): {pair}")
        raw_note, raw_gate = pair.split(":", 1)
        if not raw_note.strip() or not raw_gate.strip():
            raise ValueError(f"invalid pair (expected note:gate): {pair}")
        note_path = _normalize_note_path(repo_root, raw_note)
        gate_path = normalize_gate_path(repo_root, raw_gate)
        if not (repo_root / gate_path).is_file():
            raise FileNotFoundError(f"gate not found: {gate_path}")
        key = (note_path, gate_path)
        if key in seen:
            continue
        seen.add(key)
        normalized_pairs.append(key)
    return normalized_pairs


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
    normalized_pairs = _normalize_requested_pairs(repo_root, pairs)
    pruned_review_job_ids: set[int] = set()
    with connect(db_path) as conn:
        ack_pairs_to_write: list[AckPair] = []
        for note_path, gate_path in normalized_pairs:
            review_pair = load_latest_completed_review_pair(
                conn,
                note_path=note_path,
                gate_path=gate_path,
                model_partition=model,
            )
            if review_pair is None:
                raise ValueError(
                    "no completed review pair to acknowledge: "
                    f"{note_path}:{gate_id_from_stored_path(gate_path)} for {model}"
                )
            ack_pairs_to_write.append(
                AckPair(
                    note_path=note_path,
                    gate_path=gate_path,
                    accepted_review_pair_id=review_pair.review_pair_id,
                )
            )

        superseded_acceptances = []
        for pair in ack_pairs_to_write:
            note_snapshot = snapshot_file(conn, repo_root=repo_root, path=pair.note_path)
            gate_snapshot = snapshot_file(conn, repo_root=repo_root, path=pair.gate_path)
            superseded_acceptances.append(
                upsert_acceptance(
                    conn,
                    note_path=pair.note_path,
                    gate_path=pair.gate_path,
                    model_partition=model,
                    accepted_review_pair_id=pair.accepted_review_pair_id,
                    accepted_note_snapshot_id=note_snapshot.snapshot_id,
                    accepted_gate_snapshot_id=gate_snapshot.snapshot_id,
                    accepted_at=iso_now(),
                )
            )
            acked.append((pair.note_path, gate_id_from_stored_path(pair.gate_path)))
        pruned_review_job_ids = prune_superseded_acceptances(conn, superseded_acceptances)
        conn.commit()
    for review_job_id in sorted(pruned_review_job_ids):
        artifact_dir = bundle_artifact_dir(repo_root, review_job_id)
        if artifact_dir.exists():
            shutil.rmtree(artifact_dir, ignore_errors=True)
    return acked
