"""Acknowledge review pairs by advancing an existing freshness baseline."""

from __future__ import annotations

from pathlib import Path

from commonplace.freshness.baselines import REVIEW_PAIR_KIND
from commonplace.freshness.transitions import ack_target_inputs
from commonplace.review.paths import criterion_id_from_stored_path, normalize_criterion_path, normalize_repo_relative_path
from commonplace.review.review_db import (
    connect,
    ensure_db,
    load_current_freshness_baselines,
    prune_superseded_freshness_baselines,
    resolve_db_path,
)
from commonplace.review.review_model import normalize_model_partition


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
        pairs_to_ack: list[tuple[str, str, int]] = []
        for note_path, criterion_path in normalized_pairs:
            baseline = baselines.get((note_path, criterion_path, model))
            if baseline is None:
                raise ValueError(
                    "no freshness baseline to acknowledge: "
                    f"{note_path}:{criterion_id_from_stored_path(criterion_path)} for {model}"
                )
            pairs_to_ack.append((note_path, criterion_path, baseline.baseline_revision))

        superseded_baselines = []
        for note_path, criterion_path, expected_revision in pairs_to_ack:
            superseded = ack_target_inputs(
                conn,
                repo_root=repo_root,
                target_kind=REVIEW_PAIR_KIND,
                target_key={
                    "note_path": note_path,
                    "criterion_path": criterion_path,
                    "model_partition": model,
                },
                expected_baseline_revision=expected_revision,
            )
            superseded_baselines.append(superseded)
            acked.append((note_path, criterion_id_from_stored_path(criterion_path)))
        prune_superseded_freshness_baselines(conn, superseded_baselines)
        conn.commit()
    return acked