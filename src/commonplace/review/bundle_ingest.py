"""Shared parse/finalize tail for sentinel-delimited review bundles."""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Sequence

from commonplace.review.finalization import record_and_finalize_run
from commonplace.review.review_db import fail_review_run
from commonplace.review.review_metadata import iso_now
from commonplace.review.run_review_bundle import (
    bundle_artifact_dir,
    parse_bundle_gate_reviews,
    write_bundle_artifacts,
)


def parse_and_finalize_bundle_output(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    review_run_id: int,
    raw_bundle_markdown: str,
    expected_gate_ids: Sequence[str],
    telemetry_json: str | None = None,
    debug_log: str | None = None,
    actual_model_id: str | None = None,
) -> int:
    artifact_dir = bundle_artifact_dir(repo_root, review_run_id)
    write_bundle_artifacts(artifact_dir=artifact_dir, raw_bundle_markdown=raw_bundle_markdown)

    try:
        canonical_bundle_markdown, gate_reviews, canonical_reviews = parse_bundle_gate_reviews(
            raw_bundle_markdown,
            expected_gate_ids=list(expected_gate_ids),
        )
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

    write_bundle_artifacts(
        artifact_dir=artifact_dir,
        raw_bundle_markdown=canonical_bundle_markdown,
        parsed_reviews=canonical_reviews,
    )

    return record_and_finalize_run(
        conn,
        review_run_id=review_run_id,
        gate_reviews=gate_reviews,
        actual_model_id=actual_model_id,
        telemetry_json=telemetry_json,
        raw_bundle_markdown=canonical_bundle_markdown,
        debug_log=debug_log,
    )
