"""Acknowledge review pairs by advancing an existing freshness baseline."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from commonplace.review.clock import iso_now
from commonplace.review.paths import criterion_id_from_stored_path, normalize_criterion_path, normalize_repo_relative_path
from commonplace.review.review_db import (
    connect,
    ensure_db,
    load_current_freshness_baselines,
    prune_superseded_freshness_baselines,
    resolve_db_path,
    snapshot_file,
    upsert_freshness_baseline,
)
from commonplace.review.review_model import normalize_model_partition


@dataclass(frozen=True)
class AckPair:
    note_path: str
    criterion_path: str
    evidence_review_pair_id: int


def _normalize_note_path(repo_root: Path, raw: str) -> str:
    note_path = raw.strip()
    if not note_path:
        raise ValueError("note path must not be empty")
    normalized = normalize_repo_relative_path(note_path, label="note path")
    if not (repo_root / normalized).is_file():
        raise FileNotFoundError(f"note not found: {normalized}")
    return normalized


def _normalize_requested_pairs(repo_root: Path, pairs: list[str]) -> list[tuple[str, str]]:
    normalized_pairs: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for pair in pairs:
        if ":" not in pair:
            raise ValueError(f"invalid pair (expected note:criterion): {pair}")
        raw_note, raw_criterion = pair.split(":", 1)
        if not raw_note.strip() or not raw_criterion.strip():
            raise ValueError(f"invalid pair (expected note:criterion): {pair}")
        note_path = _normalize_note_path(repo_root, raw_note)
        criterion_path = normalize_criterion_path(repo_root, raw_criterion)
        if not (repo_root / criterion_path).is_file():
            raise FileNotFoundError(f"criterion not found: {criterion_path}")
        key = (note_path, criterion_path)
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
    with connect(db_path) as conn:
        baselines = load_current_freshness_baselines(conn)
        ack_pairs_to_write: list[AckPair] = []
        for note_path, criterion_path in normalized_pairs:
            baseline = baselines.get((note_path, criterion_path, model))
            if baseline is None:
                raise ValueError(
                    "no freshness baseline to acknowledge: "
                    f"{note_path}:{criterion_id_from_stored_path(criterion_path)} for {model}"
                )
            ack_pairs_to_write.append(
                AckPair(
                    note_path=note_path,
                    criterion_path=criterion_path,
                    evidence_review_pair_id=baseline.evidence_review_pair_id,
                )
            )

        superseded_baselines = []
        for pair in ack_pairs_to_write:
            note_snapshot = snapshot_file(conn, repo_root=repo_root, path=pair.note_path)
            criterion_snapshot = snapshot_file(conn, repo_root=repo_root, path=pair.criterion_path)
            superseded_baselines.append(
                upsert_freshness_baseline(
                    conn,
                    note_path=pair.note_path,
                    criterion_path=pair.criterion_path,
                    model_partition=model,
                    evidence_review_pair_id=pair.evidence_review_pair_id,
                    baseline_note_snapshot_id=note_snapshot.snapshot_id,
                    baseline_criterion_snapshot_id=criterion_snapshot.snapshot_id,
                    baseline_updated_at=iso_now(),
                )
            )
            acked.append((pair.note_path, criterion_id_from_stored_path(pair.criterion_path)))
        prune_superseded_freshness_baselines(conn, superseded_baselines)
        conn.commit()
    return acked
