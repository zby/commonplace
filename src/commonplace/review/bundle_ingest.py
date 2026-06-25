"""Parse/finalize tail for a single run's pair-delimited review bundle.

Used by the live-agent path: the agent writes bundle-output.md, this module
parses it and finalizes the run. Missing requested pairs fail the invocation,
while parsed pair blocks are still recorded.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Sequence

from commonplace.review.artifacts import write_manifest
from commonplace.review.executor import (
    bundle_artifact_dir,
    finalize_run_from_pairs,
    write_artifacts_for_run,
    write_run_artifacts,
)
from commonplace.review.protocol.parser import parse_pair_bundle
from commonplace.review.review_db import fail_review_run, load_review_pairs_for_run, load_review_run, mark_missing_pairs
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
    completed_count = finalize_run_from_pairs(
        conn,
        review_run_id=review_run_id,
        pairs=completed_pairs,
        parsed=parsed,
        raw_bundle_markdown=raw_bundle_markdown if parsed.missing else None,
        telemetry_json=telemetry_json,
        debug_log=debug_log,
    )
    review_run = load_review_run(conn, review_run_id=review_run_id)
    updated_pairs = load_review_pairs_for_run(conn, review_run_id=review_run_id)
    if review_run is not None:
        write_artifacts_for_run(
            repo_root=repo_root,
            review_run_id=review_run_id,
            pairs=completed_pairs,
            parsed=parsed,
            packing=review_run.packing,
        )
        artifact_dir_rel = artifact_dir.relative_to(repo_root).as_posix()
        write_manifest(
            repo_root=repo_root,
            artifact_dir=artifact_dir,
            review_run_id=review_run_id,
            packing=review_run.packing,
            prompt_path=f"{artifact_dir_rel}/prompt.md",
            bundle_output_path=f"{artifact_dir_rel}/bundle-output.md",
            pairs=updated_pairs,
            failure_reason=review_run.failure_reason,
        )
    return completed_count
