"""Freshness baseline transitions for registered targets."""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from commonplace.freshness import baselines as freshness_baselines
from commonplace.freshness.keys import canonical_json, review_pair_target_key
from commonplace.freshness.revisions import allocate_initial_revision, allocate_successor_revision
from commonplace.freshness.snapshots import insert_or_get_snapshot
from commonplace.freshness.versioning import FILE_TEXT, resolve_file_text
from commonplace.review.clock import iso_now
from commonplace.review.review_db import SupersededFreshnessBaseline, snapshot_file
from commonplace.review.review_model import normalize_model_partition

REVIEW_PAIR_KIND = freshness_baselines.REVIEW_PAIR_KIND
V1_ACCEPT_TARGET_KINDS: frozenset[str] = frozenset()


@dataclass(frozen=True)
class InputObservation:
    input_role: str
    artifact_path: str
    version_kind: str
    content_sha256: str


def _target_key_json(target_kind: str, target_key: dict[str, str]) -> str:
    if target_kind == REVIEW_PAIR_KIND:
        required = {"note_path", "criterion_path", "model_partition"}
        if set(target_key) != required:
            raise ValueError(f"review-pair target_key must contain exactly {sorted(required)}")
        return review_pair_target_key(
            note_path=target_key["note_path"],
            criterion_path=target_key["criterion_path"],
            model_partition=normalize_model_partition(target_key["model_partition"]),
        )
    return canonical_json(target_key)


def _load_target_id(
    conn: sqlite3.Connection,
    *,
    target_kind: str,
    target_key: dict[str, str],
) -> int | None:
    row = conn.execute(
        """
        SELECT target_id
        FROM freshness_baselines
        WHERE target_kind = ? AND target_key_json = ?
        """,
        (target_kind, _target_key_json(target_kind, target_key)),
    ).fetchone()
    if row is None:
        return None
    return int(row["target_id"])


def retire_target(
    conn: sqlite3.Connection,
    *,
    target_kind: str,
    target_key: dict[str, str],
) -> bool:
    """Delete one registered baseline. Returns False when already absent."""
    target_id = _load_target_id(conn, target_kind=target_kind, target_key=target_key)
    if target_id is None:
        return False
    conn.execute("DELETE FROM freshness_baselines WHERE target_id = ?", (target_id,))
    return True


def accept_target_observations(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    target_kind: str,
    target_key: dict[str, str],
    inputs: dict[str, InputObservation],
    expected_baseline_revision: int | None,
    accepted_at: str | None = None,
) -> None:
    """Observation refresh or initial acceptance. Rejects review-pair in v1."""
    if target_kind == REVIEW_PAIR_KIND:
        raise ValueError("review-pair targets must use review capture finalization, not generic accept")
    if target_kind not in V1_ACCEPT_TARGET_KINDS:
        raise ValueError(f"target kind {target_kind!r} is not supported for generic accept in v1")
    if not inputs:
        raise ValueError("accept manifest must include at least one input role")
    target_key_json = _target_key_json(target_kind, target_key)
    current = conn.execute(
        """
        SELECT target_id, revision
        FROM freshness_baselines
        WHERE target_kind = ? AND target_key_json = ?
        """,
        (target_kind, target_key_json),
    ).fetchone()
    if expected_baseline_revision is None:
        if current is not None:
            raise ValueError("stale-baseline-revision: baseline already exists")
    else:
        if current is None:
            raise ValueError("stale-baseline-revision: expected baseline but none registered")
        if int(current["revision"]) != expected_baseline_revision:
            raise ValueError(
                f"stale-baseline-revision: expected {expected_baseline_revision}, "
                f"current {current['revision']}"
            )

    accepted = accepted_at or iso_now()
    snapshot_ids: dict[str, int] = {}
    for role, observation in inputs.items():
        if observation.version_kind != FILE_TEXT:
            raise ValueError(f"unsupported version kind: {observation.version_kind}")
        resolved = resolve_file_text(repo_root=repo_root, path=observation.artifact_path)
        if resolved.content_sha256 != observation.content_sha256:
            raise ValueError(
                f"live hash mismatch for {observation.artifact_path}: "
                f"expected {observation.content_sha256}, current {resolved.content_sha256}"
            )
        snapshot = insert_or_get_snapshot(conn, resolved=resolved, captured_at=accepted)
        snapshot_ids[role] = snapshot.snapshot_id

    if current is None:
        revision = allocate_initial_revision(
            conn,
            target_kind=target_kind,
            target_key_json=target_key_json,
        )
        cursor = conn.execute(
            """
            INSERT INTO freshness_baselines (target_kind, target_key_json, revision, accepted_at)
            VALUES (?, ?, ?, ?)
            """,
            (target_kind, target_key_json, revision, accepted),
        )
        target_id = int(cursor.lastrowid)
    else:
        target_id = int(current["target_id"])
        revision = allocate_successor_revision(
            conn,
            target_kind=target_kind,
            target_key_json=target_key_json,
            current_revision=int(current["revision"]),
        )
        conn.execute(
            """
            UPDATE freshness_baselines
            SET revision = ?, accepted_at = ?
            WHERE target_id = ?
            """,
            (revision, accepted, target_id),
        )
        conn.execute("DELETE FROM freshness_inputs WHERE target_id = ?", (target_id,))

    for role, observation in inputs.items():
        conn.execute(
            """
            INSERT INTO freshness_inputs (
                target_id, input_role, artifact_path, version_kind, accepted_snapshot_id
            ) VALUES (?, ?, ?, ?, ?)
            """,
            (target_id, role, observation.artifact_path, observation.version_kind, snapshot_ids[role]),
        )


def ack_target_inputs(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    target_kind: str,
    target_key: dict[str, str],
    expected_baseline_revision: int,
    selected_inputs: tuple[InputObservation, ...] | None = None,
    accepted_at: str | None = None,
) -> SupersededFreshnessBaseline | None:
    """Observation ack with CAS. Review-pair preserves evidence automatically."""
    if target_kind != REVIEW_PAIR_KIND:
        raise ValueError(f"ack for {target_kind!r} is not implemented in v1")
    note_path = target_key["note_path"]
    criterion_path = target_key["criterion_path"]
    model_partition = normalize_model_partition(target_key["model_partition"])
    current = freshness_baselines.load_review_target(
        conn,
        note_path=note_path,
        criterion_path=criterion_path,
        model_partition=model_partition,
    )
    if current is None:
        raise ValueError("no freshness baseline to acknowledge")
    if current.revision != expected_baseline_revision:
        raise ValueError(
            f"stale-baseline-revision: expected {expected_baseline_revision}, "
            f"current {current.revision}"
        )

    evidence_row = conn.execute(
        """
        SELECT evidence_review_pair_id
        FROM review_freshness_evidence
        WHERE target_id = ?
        """,
        (current.target_id,),
    ).fetchone()
    if evidence_row is None:
        raise RuntimeError(f"review evidence missing for target_id={current.target_id}")
    evidence_review_pair_id = int(evidence_row["evidence_review_pair_id"])

    input_rows = conn.execute(
        """
        SELECT input_role, artifact_path, version_kind, accepted_snapshot_id
        FROM freshness_inputs
        WHERE target_id = ?
        """,
        (current.target_id,),
    ).fetchall()
    registered_inputs = {row["input_role"]: row for row in input_rows}

    roles_to_ack: set[str]
    if selected_inputs is None:
        roles_to_ack = {"note", "criterion"}
    else:
        roles_to_ack = {observation.input_role for observation in selected_inputs}
        for observation in selected_inputs:
            registered = registered_inputs.get(observation.input_role)
            if registered is None:
                raise ValueError(f"unknown input role for target: {observation.input_role}")
            if observation.artifact_path != registered["artifact_path"]:
                raise ValueError(
                    f"artifact_path for {observation.input_role} must be {registered['artifact_path']}"
                )
            if observation.version_kind != registered["version_kind"]:
                raise ValueError(
                    f"version_kind for {observation.input_role} must be {registered['version_kind']}"
                )
            if observation.version_kind != FILE_TEXT:
                raise ValueError(f"unsupported version kind: {observation.version_kind}")
            resolved = resolve_file_text(
                repo_root=repo_root,
                path=registered["artifact_path"],
            )
            if resolved.content_sha256 != observation.content_sha256:
                raise ValueError(
                    f"live hash mismatch for {registered['artifact_path']}: "
                    f"expected {observation.content_sha256}, current {resolved.content_sha256}"
                )

    note_snapshot_id = int(registered_inputs["note"]["accepted_snapshot_id"])
    criterion_snapshot_id = int(registered_inputs["criterion"]["accepted_snapshot_id"])
    if "note" in roles_to_ack:
        note_snapshot = snapshot_file(conn, repo_root=repo_root, path=note_path)
        note_snapshot_id = note_snapshot.snapshot_id
    if "criterion" in roles_to_ack:
        criterion_snapshot = snapshot_file(conn, repo_root=repo_root, path=criterion_path)
        criterion_snapshot_id = criterion_snapshot.snapshot_id

    accepted = accepted_at or iso_now()
    superseded_evidence_pair_id = freshness_baselines.refresh_review_baseline_from_observation(
        conn,
        note_path=note_path,
        criterion_path=criterion_path,
        model_partition=model_partition,
        evidence_review_pair_id=evidence_review_pair_id,
        baseline_note_snapshot_id=note_snapshot_id,
        baseline_criterion_snapshot_id=criterion_snapshot_id,
        accepted_at=accepted,
    )
    if superseded_evidence_pair_id is None:
        return None
    return SupersededFreshnessBaseline(
        note_path=note_path,
        criterion_path=criterion_path,
        model_partition=model_partition,
        evidence_review_pair_id=superseded_evidence_pair_id,
        baseline_note_snapshot_id=registered_inputs["note"]["accepted_snapshot_id"],
        baseline_criterion_snapshot_id=registered_inputs["criterion"]["accepted_snapshot_id"],
    )


def refresh_target_from_captures(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    criterion_path: str,
    model_partition: str,
    evidence_review_pair_id: int,
    baseline_note_snapshot_id: int,
    baseline_criterion_snapshot_id: int,
    expected_baseline_revision: int | None,
    accepted_at: str,
) -> tuple[int | None, int | None]:
    """Review-owned capture refresh. Returns superseded evidence pair and target ids."""
    return freshness_baselines.refresh_review_baseline_from_captures(
        conn,
        note_path=note_path,
        criterion_path=criterion_path,
        model_partition=model_partition,
        evidence_review_pair_id=evidence_review_pair_id,
        baseline_note_snapshot_id=baseline_note_snapshot_id,
        baseline_criterion_snapshot_id=baseline_criterion_snapshot_id,
        expected_baseline_revision=expected_baseline_revision,
        accepted_at=accepted_at,
    )


def parse_target_key(raw: object) -> dict[str, str]:
    if not isinstance(raw, dict):
        raise ValueError("target_key must be an object")
    result: dict[str, str] = {}
    for key, value in raw.items():
        if not isinstance(key, str) or not isinstance(value, str) or not value.strip():
            raise ValueError("target_key values must be non-empty strings")
        result[key] = value.strip()
    return result


def parse_input_observation(raw: object) -> InputObservation:
    if not isinstance(raw, dict):
        raise ValueError("input observation must be an object")
    role = raw.get("input_role")
    path = raw.get("artifact_path")
    version_kind = raw.get("version_kind")
    content_sha256 = raw.get("content_sha256")
    if not isinstance(role, str) or not role.strip():
        raise ValueError("input_role is required")
    if not isinstance(path, str) or not path.strip():
        raise ValueError("artifact_path is required")
    if not isinstance(version_kind, str) or not version_kind.strip():
        raise ValueError("version_kind is required")
    if not isinstance(content_sha256, str) or len(content_sha256) != 64:
        raise ValueError("content_sha256 must be 64 lowercase hex")
    return InputObservation(
        input_role=role.strip(),
        artifact_path=path.strip(),
        version_kind=version_kind.strip(),
        content_sha256=content_sha256.lower(),
    )


def load_json_input(raw: str) -> dict[str, object]:
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON input: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError("JSON input must be an object")
    return payload