"""Freshness status projection and JSON rendering."""

from __future__ import annotations

import difflib
import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from commonplace.freshness.selector import ChangedInput, StaleTarget, select_stale_review_targets
from commonplace.freshness.snapshots import load_snapshot_by_id
from commonplace.review.clock import iso_now


@dataclass(frozen=True)
class FreshnessStatus:
    targets: tuple[StaleTarget, ...]
    exit_class: str


def load_target_status(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    include_fresh: bool = False,
    include_diff: bool = False,
    model_partition: str | None = None,
) -> FreshnessStatus:
    targets = select_stale_review_targets(
        conn,
        repo_root=repo_root,
        include_fresh=include_fresh,
        model_partition=model_partition,
    )
    if include_diff:
        targets = tuple(_attach_diffs(conn, repo_root=repo_root, target=target) for target in targets)
    exit_class = _exit_class(targets)
    return FreshnessStatus(targets=targets, exit_class=exit_class)


def _exit_class(targets: tuple[StaleTarget, ...] | list[StaleTarget]) -> str:
    for target in targets:
        for changed in target.changed_inputs:
            if changed.status == "version-error":
                return "error"
            if changed.status in {"input-changed", "input-missing"}:
                return "stale"
    return "fresh"


def _attach_diffs(conn: sqlite3.Connection, *, repo_root: Path, target: StaleTarget) -> StaleTarget:
    changed: list[ChangedInput] = []
    for item in target.changed_inputs:
        if item.status != "input-changed" or item.accepted_content_sha256 is None:
            changed.append(item)
            continue
        accepted_text = _accepted_text(conn, item=item)
        current_text = (repo_root / item.artifact_path).read_text(encoding="utf-8")
        diff = "".join(
            difflib.unified_diff(
                accepted_text.splitlines(keepends=True),
                current_text.splitlines(keepends=True),
                fromfile=f"a/{item.artifact_path}",
                tofile=f"b/{item.artifact_path}",
            )
        ).strip()
        changed.append(
            ChangedInput(
                input_role=item.input_role,
                artifact_path=item.artifact_path,
                version_kind=item.version_kind,
                status=item.status,
                accepted_snapshot_id=item.accepted_snapshot_id,
                accepted_content_sha256=item.accepted_content_sha256,
                current_content_sha256=item.current_content_sha256,
                diff=diff or None,
            )
        )
    return StaleTarget(
        target_kind=target.target_kind,
        target_key=target.target_key,
        baseline_revision=target.baseline_revision,
        accepted_at=target.accepted_at,
        changed_inputs=tuple(changed),
    )


def _accepted_text(conn: sqlite3.Connection, *, item: ChangedInput) -> str:
    if item.accepted_snapshot_id is not None:
        snapshot = load_snapshot_by_id(conn, item.accepted_snapshot_id)
        if snapshot is not None and snapshot.content_text is not None:
            return snapshot.content_text
    raise RuntimeError(f"cannot resolve accepted text for {item.artifact_path}")


def render_status_json(status: FreshnessStatus, *, include_all: bool = False) -> str:
    if include_all:
        rendered_targets = status.targets
    else:
        rendered_targets = tuple(target for target in status.targets if target.changed_inputs)
    payload = {
        "schema": "commonplace-freshness-status/1",
        "generated_at": iso_now(),
        "exit_class": status.exit_class,
        "targets": [_target_to_json(target) for target in rendered_targets],
    }
    return json.dumps(payload, indent=2, sort_keys=True)


def _target_to_json(target: StaleTarget) -> dict[str, object]:
    return {
        "target_kind": target.target_kind,
        "target_key": dict(sorted(target.target_key.items())),
        "baseline_revision": target.baseline_revision,
        "accepted_at": target.accepted_at,
        "changed_inputs": [_changed_input_to_json(item) for item in target.changed_inputs],
    }


def _changed_input_to_json(item: ChangedInput) -> dict[str, object]:
    payload: dict[str, object] = {
        "input_role": item.input_role,
        "artifact_path": item.artifact_path,
        "version_kind": item.version_kind,
        "status": item.status,
        "accepted_snapshot_id": item.accepted_snapshot_id,
        "accepted_content_sha256": item.accepted_content_sha256,
        "current_content_sha256": item.current_content_sha256,
    }
    if item.diff is not None:
        payload["diff"] = item.diff
    return payload


def status_exit_code(status: FreshnessStatus) -> int:
    if status.exit_class == "fresh":
        return 0
    if status.exit_class == "stale":
        return 1
    return 2