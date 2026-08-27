"""Acknowledge review pairs by advancing an existing freshness baseline."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from commonplace.freshness.baselines import REVIEW_PAIR_KIND
from commonplace.freshness.selector import ChangedInput
from commonplace.freshness.transitions import InputObservation, ack_target_inputs
from commonplace.review.paths import (
    criterion_id_from_stored_path,
    normalize_criterion_path,
    normalize_repo_relative_path,
)
from commonplace.review.review_db import (
    connect,
    ensure_db,
    load_current_freshness_baselines,
    prune_superseded_freshness_baselines,
    resolve_db_path,
)
from commonplace.review.review_model import normalize_model_partition
from commonplace.review.review_target_selector import SELECTOR_SCHEMA, StaleCriterion


def _normalize_note_path(repo_root: Path, raw: str) -> str:
    note_path = raw.strip()
    if not note_path:
        raise ValueError("note path must not be empty")
    normalized = normalize_repo_relative_path(note_path, label="note path")
    if not (repo_root / normalized).is_file():
        raise FileNotFoundError(f"note not found: {normalized}")
    return normalized


def _required_string(raw: object, *, label: str) -> str:
    if not isinstance(raw, str) or not raw.strip():
        raise ValueError(f"{label} is required")
    return raw.strip()


def _content_hash(raw: object, *, label: str) -> str:
    value = _required_string(raw, label=label).lower()
    if len(value) != 64 or any(character not in "0123456789abcdef" for character in value):
        raise ValueError(f"{label} must be 64 lowercase hex")
    return value


def _parse_changed_input(
    raw: object,
    *,
    index: int,
    note_path: str,
    criterion_path: str,
) -> ChangedInput:
    if not isinstance(raw, dict):
        raise TypeError(f"selector target changed_inputs[{index}] must be an object")
    input_role = _required_string(raw.get("input_role"), label="input_role")
    if input_role not in {"note", "criterion"}:
        raise ValueError(f"unsupported review input role: {input_role}")
    expected_path = note_path if input_role == "note" else criterion_path
    artifact_path = _required_string(raw.get("artifact_path"), label="artifact_path")
    if artifact_path != expected_path:
        raise ValueError(f"artifact_path for {input_role} must be {expected_path}")
    version_kind = _required_string(raw.get("version_kind"), label="version_kind")
    if version_kind != "file-text":
        raise ValueError(f"unsupported version kind: {version_kind}")
    status = _required_string(raw.get("status"), label="status")
    if status != "input-changed":
        raise ValueError(f"review acknowledgement requires input-changed observations, got {status}")
    accepted_snapshot_id = raw.get("accepted_snapshot_id")
    if not isinstance(accepted_snapshot_id, int) or accepted_snapshot_id < 1:
        raise ValueError("accepted_snapshot_id must be >= 1")
    accepted_hash = _content_hash(
        raw.get("accepted_content_sha256"),
        label="accepted_content_sha256",
    )
    current_hash = _content_hash(
        raw.get("current_content_sha256"),
        label="current_content_sha256",
    )
    diff = raw.get("diff")
    if diff is not None and not isinstance(diff, str):
        raise TypeError("diff must be a string")
    return ChangedInput(
        input_role=input_role,
        artifact_path=artifact_path,
        version_kind=version_kind,
        status=status,
        accepted_snapshot_id=accepted_snapshot_id,
        accepted_content_sha256=accepted_hash,
        current_content_sha256=current_hash,
        diff=diff,
    )


def records_from_selector_payload(
    repo_root: Path,
    payload: dict[str, object],
) -> tuple[str, list[StaleCriterion]]:
    if payload.get("schema") != SELECTOR_SCHEMA:
        raise ValueError(f"schema must be {SELECTOR_SCHEMA}")
    model = normalize_model_partition(
        _required_string(payload.get("model_partition"), label="model_partition")
    )
    raw_targets = payload.get("targets")
    if not isinstance(raw_targets, list):
        raise TypeError("selector targets must be an array")

    records: list[StaleCriterion] = []
    seen_pairs: set[tuple[str, str]] = set()
    for target_index, raw_target in enumerate(raw_targets, start=1):
        if not isinstance(raw_target, dict):
            raise TypeError(f"selector target {target_index} must be an object")
        note_path = _normalize_note_path(
            repo_root,
            _required_string(raw_target.get("note_path"), label="note_path"),
        )
        criterion_path = normalize_criterion_path(
            repo_root,
            _required_string(raw_target.get("criterion_path"), label="criterion_path"),
        )
        if not (repo_root / criterion_path).is_file():
            raise FileNotFoundError(f"criterion not found: {criterion_path}")
        criterion_id = _required_string(raw_target.get("criterion_id"), label="criterion_id")
        expected_criterion_id = criterion_id_from_stored_path(criterion_path)
        if criterion_id != expected_criterion_id:
            raise ValueError(
                f"criterion_id {criterion_id!r} does not match criterion_path {criterion_path!r}"
            )
        pair_key = (note_path, criterion_path)
        if pair_key in seen_pairs:
            raise ValueError(f"duplicate selector target: {note_path}:{criterion_path}")
        seen_pairs.add(pair_key)

        raw_revision = raw_target.get("baseline_revision")
        if not isinstance(raw_revision, int) or raw_revision < 1:
            raise ValueError(f"selector target {target_index} baseline_revision must be >= 1")
        raw_reasons = raw_target.get("reasons")
        if not isinstance(raw_reasons, list) or not raw_reasons:
            raise ValueError(f"selector target {target_index} reasons must be a non-empty array")
        reasons = tuple(_required_string(reason, label="reason") for reason in raw_reasons)
        raw_changed_inputs = raw_target.get("changed_inputs")
        if not isinstance(raw_changed_inputs, list) or not raw_changed_inputs:
            raise ValueError(f"selector target {target_index} changed_inputs must be a non-empty array")
        changed_inputs = tuple(
            _parse_changed_input(
                item,
                index=input_index,
                note_path=note_path,
                criterion_path=criterion_path,
            )
            for input_index, item in enumerate(raw_changed_inputs, start=1)
        )
        roles = tuple(item.input_role for item in changed_inputs)
        if len(set(roles)) != len(roles):
            raise ValueError(f"selector target {target_index} repeats an input role")
        expected_reasons = tuple(f"{role}-changed" for role in roles)
        if reasons != expected_reasons:
            raise ValueError(
                f"selector target {target_index} reasons {reasons!r} do not match changed inputs {expected_reasons!r}"
            )
        result_kind = _required_string(raw_target.get("result_kind"), label="result_kind")
        if result_kind not in {"verdict", "report"}:
            raise ValueError(f"invalid result_kind: {result_kind}")
        records.append(
            StaleCriterion(
                note_path=note_path,
                criterion_path=criterion_path,
                reasons=reasons,
                result_kind=result_kind,
                baseline_revision=raw_revision,
                changed_inputs=changed_inputs,
            )
        )
    return model, records


def _selected_inputs(record: StaleCriterion) -> tuple[InputObservation, ...]:
    if record.baseline_revision is None:
        raise ValueError(f"selector target has no baseline revision: {record.note_path}:{record.criterion_id}")
    if not record.changed_inputs:
        raise ValueError(f"selector target has no changed inputs: {record.note_path}:{record.criterion_id}")
    roles = tuple(item.input_role for item in record.changed_inputs)
    if len(set(roles)) != len(roles):
        raise ValueError(f"selector target repeats an input role: {record.note_path}:{record.criterion_id}")
    expected_reasons = tuple(f"{role}-changed" for role in roles)
    if record.reasons != expected_reasons:
        raise ValueError(
            f"selector target reasons {record.reasons!r} do not match changed inputs {expected_reasons!r}"
        )
    observations: list[InputObservation] = []
    for item in record.changed_inputs:
        if item.input_role not in {"note", "criterion"}:
            raise ValueError(f"unsupported review input role: {item.input_role}")
        if item.status != "input-changed" or item.current_content_sha256 is None:
            raise ValueError(
                f"selector target has no acknowledgeable observation for {item.input_role}: "
                f"{record.note_path}:{record.criterion_id}"
            )
        observations.append(
            InputObservation(
                input_role=item.input_role,
                artifact_path=item.artifact_path,
                version_kind=item.version_kind,
                content_sha256=item.current_content_sha256,
            )
        )
    return tuple(observations)


def ack_pairs(
    repo_root: Path,
    records: Sequence[StaleCriterion],
    model: str,
    *,
    db_path: Path | None = None,
) -> list[tuple[str, str]]:
    model = normalize_model_partition(model)
    if db_path is None:
        db_path = resolve_db_path(repo_root)
    ensure_db(db_path)
    acked: list[tuple[str, str]] = []
    candidates: list[tuple[StaleCriterion, tuple[InputObservation, ...]]] = []
    seen_pairs: set[tuple[str, str]] = set()
    for record in records:
        pair_key = (record.note_path, record.criterion_path)
        if pair_key in seen_pairs:
            raise ValueError(f"duplicate selector target: {record.note_path}:{record.criterion_path}")
        seen_pairs.add(pair_key)
        candidates.append((record, _selected_inputs(record)))

    with connect(db_path) as conn:
        baselines = load_current_freshness_baselines(conn)
        for record, _selected in candidates:
            baseline = baselines.get((record.note_path, record.criterion_path, model))
            if baseline is None:
                raise ValueError(
                    "no freshness baseline to acknowledge: "
                    f"{record.note_path}:{record.criterion_id} for {model}"
                )
            if baseline.baseline_revision != record.baseline_revision:
                raise ValueError(
                    f"stale-baseline-revision: expected {record.baseline_revision}, "
                    f"current {baseline.baseline_revision}"
                )
            accepted_by_role = {
                "note": (
                    baseline.baseline_note_snapshot_id,
                    baseline.baseline_note_hash,
                ),
                "criterion": (
                    baseline.baseline_criterion_snapshot_id,
                    baseline.baseline_criterion_hash,
                ),
            }
            for changed_input in record.changed_inputs:
                expected_snapshot_id, expected_hash = accepted_by_role[changed_input.input_role]
                if (
                    changed_input.accepted_snapshot_id != expected_snapshot_id
                    or changed_input.accepted_content_sha256 != expected_hash
                ):
                    raise ValueError(
                        f"accepted input mismatch for {changed_input.artifact_path}: "
                        f"expected snapshot {expected_snapshot_id} hash {expected_hash}"
                    )

        superseded_baselines = []
        for record, selected_inputs in candidates:
            superseded = ack_target_inputs(
                conn,
                repo_root=repo_root,
                target_kind=REVIEW_PAIR_KIND,
                target_key={
                    "note_path": record.note_path,
                    "criterion_path": record.criterion_path,
                    "model_partition": model,
                },
                expected_baseline_revision=record.baseline_revision,
                selected_inputs=selected_inputs,
            )
            superseded_baselines.append(superseded)
            acked.append((record.note_path, criterion_id_from_stored_path(record.criterion_path)))
        prune_superseded_freshness_baselines(conn, superseded_baselines)
        conn.commit()
    return acked
