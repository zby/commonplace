"""Parse/finalize tail for a single run's pair-delimited review bundle.

Used by the live-agent path: the agent writes bundle-output.md, this module
parses it and finalizes the run. Missing requested pairs fail the invocation,
while parsed pair blocks are still recorded.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Sequence

from commonplace.review.executor import (
    bundle_artifact_dir,
    finalize_run_from_pairs,
    write_artifacts_for_run,
    write_run_artifacts,
)
from commonplace.review.protocol.parser import parse_pair_bundle
from commonplace.review.review_db import fail_review_run, mark_missing_pairs
from commonplace.review.review_metadata import iso_now


def parse_and_finalize_bundle_output(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    review_run_id: int,
    raw_bundle_markdown: str,
    expected_pairs: Sequence[tuple[str, str]],
    telemetry_json: str | None = None,
    debug_log: str | None = None,
    actual_model_id: str | None = None,
) -> int:
    artifact_dir = bundle_artifact_dir(repo_root, review_run_id)
    write_run_artifacts(artifact_dir=artifact_dir, bundle_markdown=raw_bundle_markdown)

    pairs = tuple(expected_pairs)
    try:
        parsed = parse_pair_bundle(raw_bundle_markdown, expected_pairs=pairs)
    except ValueError as exc:
        mark_missing_pairs(conn, review_run_id=review_run_id)
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

    completed_pairs = tuple(pair for pair in pairs if pair not in set(parsed.missing))
    write_artifacts_for_run(
        repo_root=repo_root,
        review_run_id=review_run_id,
        pairs=completed_pairs,
        parsed=parsed,
    )

    return finalize_run_from_pairs(
        conn,
        review_run_id=review_run_id,
        pairs=completed_pairs,
        parsed=parsed,
        raw_bundle_markdown=raw_bundle_markdown if parsed.missing else None,
        telemetry_json=telemetry_json,
        debug_log=debug_log,
        actual_model_id=actual_model_id,
    )
