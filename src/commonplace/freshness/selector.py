"""Repository-wide freshness selection."""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path

from commonplace.freshness.keys import review_pair_target_key
from commonplace.freshness.versioning import resolve_file_text
from commonplace.review.review_db import FreshnessBaseline, load_current_freshness_baselines


@dataclass(frozen=True)
class ChangedInput:
    input_role: str
    artifact_path: str
    version_kind: str
    status: str
    accepted_snapshot_id: int | None
    accepted_content_sha256: str | None
    current_content_sha256: str | None
    diff: str | None = None


@dataclass(frozen=True)
class StaleTarget:
    target_kind: str
    target_key: dict[str, str]
    baseline_revision: int
    accepted_at: str
    changed_inputs: tuple[ChangedInput, ...]


def select_stale_review_targets(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    include_fresh: bool = False,
    model_partition: str | None = None,
) -> list[StaleTarget]:
    baselines = load_current_freshness_baselines(conn)
    stale: list[StaleTarget] = []
    for key, baseline in baselines.items():
        note_path, criterion_path, partition = key
        if model_partition is not None and partition != model_partition:
            continue
        changed = _changed_inputs_for_baseline(conn, repo_root=repo_root, baseline=baseline)
        if changed or include_fresh:
            stale.append(
                StaleTarget(
                    target_kind="review-pair",
                    target_key={
                        "note_path": note_path,
                        "criterion_path": criterion_path,
                        "model_partition": partition,
                    },
                    baseline_revision=_baseline_revision(conn, baseline=baseline),
                    accepted_at=baseline.baseline_updated_at,
                    changed_inputs=changed,
                )
            )
    return stale


def _baseline_revision(conn: sqlite3.Connection, *, baseline: FreshnessBaseline) -> int:
    target_key_json = review_pair_target_key(
        note_path=baseline.note_path,
        criterion_path=baseline.criterion_path,
        model_partition=baseline.model_partition,
    )
    row = conn.execute(
        """
        SELECT revision FROM freshness_baselines
        WHERE target_kind = 'review-pair' AND target_key_json = ?
        """,
        (target_key_json,),
    ).fetchone()
    if row is None:
        raise RuntimeError("baseline row missing for current view entry")
    return int(row["revision"])


def _changed_inputs_for_baseline(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    baseline: FreshnessBaseline,
) -> tuple[ChangedInput, ...]:
    changed: list[ChangedInput] = []
    for role, path, accepted_hash, accepted_snapshot_id in (
        ("note", baseline.note_path, baseline.baseline_note_hash, baseline.baseline_note_snapshot_id),
        (
            "criterion",
            baseline.criterion_path,
            baseline.baseline_criterion_hash,
            baseline.baseline_criterion_snapshot_id,
        ),
    ):
        try:
            resolved = resolve_file_text(repo_root=repo_root, path=path)
        except FileNotFoundError:
            changed.append(
                ChangedInput(
                    input_role=role,
                    artifact_path=path,
                    version_kind="file-text",
                    status="input-missing",
                    accepted_snapshot_id=accepted_snapshot_id,
                    accepted_content_sha256=accepted_hash,
                    current_content_sha256=None,
                )
            )
            continue
        if resolved.content_sha256 != accepted_hash:
            changed.append(
                ChangedInput(
                    input_role=role,
                    artifact_path=path,
                    version_kind="file-text",
                    status="input-changed",
                    accepted_snapshot_id=accepted_snapshot_id,
                    accepted_content_sha256=accepted_hash,
                    current_content_sha256=resolved.content_sha256,
                )
            )
    return tuple(changed)