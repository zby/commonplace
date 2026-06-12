"""Parse/finalize tail for a single run's pair-delimited review bundle.

Used by the live-agent path: the agent writes bundle-output.md, this module
parses it and finalizes the run. One run is all-or-nothing — a missing pair
fails the whole run (salvage across runs only applies to batched execution
in the executor).
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Sequence

from commonplace.review.executor import bundle_artifact_dir, finalize_run_from_pairs, write_run_artifacts
from commonplace.review.protocol.parser import parse_pair_bundle
from commonplace.review.review_db import fail_review_run
from commonplace.review.review_metadata import iso_now


def parse_and_finalize_bundle_output(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    review_run_id: int,
    note_path: str,
    raw_bundle_markdown: str,
    expected_gate_ids: Sequence[str],
    telemetry_json: str | None = None,
    debug_log: str | None = None,
    actual_model_id: str | None = None,
) -> int:
    artifact_dir = bundle_artifact_dir(repo_root, review_run_id)
    write_run_artifacts(artifact_dir=artifact_dir, bundle_markdown=raw_bundle_markdown)

    gate_ids = tuple(expected_gate_ids)
    expected_pairs = [(note_path, gate_id) for gate_id in gate_ids]
    try:
        parsed = parse_pair_bundle(raw_bundle_markdown, expected_pairs=expected_pairs)
        if parsed.missing:
            missing_gates = ", ".join(sorted(gate_id for _, gate_id in parsed.missing))
            raise ValueError(f"missing pair reviews: {missing_gates}")
    except ValueError as exc:
        fail_review_run(
            conn,
            review_run_id=review_run_id,
            failure_reason=str(exc),
            completed_at=iso_now(),
            raw_bundle_markdown=raw_bundle_markdown,
            debug_log=debug_log,
            telemetry_json=telemetry_json,
        )
        raise

    return finalize_run_from_pairs(
        conn,
        repo_root=repo_root,
        note_path=note_path,
        review_run_id=review_run_id,
        gate_ids=gate_ids,
        parsed=parsed,
        telemetry_json=telemetry_json,
        debug_log=debug_log,
        actual_model_id=actual_model_id,
    )
