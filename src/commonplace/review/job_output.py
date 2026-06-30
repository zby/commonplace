"""Finalize job-owned review output into DB rows and result artifacts."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from commonplace.review.artifacts import (
    bundle_artifact_dir,
    write_manifest,
    write_pair_result_files_to_persisted_paths,
)
from commonplace.review.clock import iso_now
from commonplace.review.finalization import record_and_finalize_job
from commonplace.review.protocol.parser import ParsedPairBundle, parse_pair_bundle
from commonplace.review.review_db import (
    ReviewPairCompletion,
    attach_execution_data,
    connect,
    fail_review_job,
    load_review_job_plan,
    mark_missing_pairs,
)


ACTIVE_REVIEW_JOB_STATUSES = frozenset({"queued", "running"})


def fail_active_review_jobs(
    *,
    db_path: Path,
    review_job_ids: list[int],
    failure_reason: str,
    telemetry_json: str | None = None,
) -> None:
    if not review_job_ids:
        return
    completed_at = iso_now()
    with connect(db_path) as conn:
        rows = conn.execute(
            f"""
            SELECT review_job_id, status
            FROM review_jobs
            WHERE review_job_id IN ({", ".join("?" for _ in review_job_ids)})
            """,
            review_job_ids,
        ).fetchall()
        for row in rows:
            if row["status"] not in ACTIVE_REVIEW_JOB_STATUSES:
                continue
            attach_execution_data(
                conn,
                review_job_id=int(row["review_job_id"]),
                telemetry_json=telemetry_json,
            )
            mark_missing_pairs(conn, review_job_id=int(row["review_job_id"]))
            fail_review_job(
                conn,
                review_job_id=int(row["review_job_id"]),
                failure_reason=failure_reason,
                completed_at=completed_at,
            )
        conn.commit()


def finalize_job_from_pairs(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    pairs: tuple[tuple[str, str], ...],
    parsed: ParsedPairBundle,
    telemetry_json: str | None = None,
) -> int:
    review_pairs = [
        ReviewPairCompletion(
            note_path=note_path,
            gate_path=gate_path,
            decision=parsed.reviews[(note_path, gate_path)].decision,
        )
        for note_path, gate_path in pairs
    ]
    return record_and_finalize_job(
        conn,
        review_job_id=review_job_id,
        review_pairs=review_pairs,
        telemetry_json=telemetry_json,
    )


def write_job_manifest_from_db(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    review_job_id: int,
) -> None:
    plan = load_review_job_plan(conn, review_job_id=review_job_id, require_paths=True)
    if plan is None:
        return
    artifact_dir = bundle_artifact_dir(repo_root, review_job_id)
    assert plan.prompt_path is not None
    assert plan.bundle_output_path is not None
    write_manifest(
        repo_root=repo_root,
        artifact_dir=artifact_dir,
        review_job_id=review_job_id,
        packing=plan.packing,
        prompt_path=plan.prompt_path,
        bundle_output_path=plan.bundle_output_path,
        pairs=plan.pairs,
        failure_reason=plan.failure_reason,
    )


def write_finalized_job_artifacts(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    review_job_id: int,
    parsed: ParsedPairBundle,
) -> None:
    plan = load_review_job_plan(conn, review_job_id=review_job_id, require_paths=True)
    if plan is None:
        return
    write_pair_result_files_to_persisted_paths(
        repo_root=repo_root,
        job=plan,
        pairs=plan.pairs,
        canonical_texts=parsed.canonical_texts,
    )
    write_job_manifest_from_db(conn, repo_root=repo_root, review_job_id=review_job_id)


def fail_job_for_bundle_parse_error(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    failure_reason: str,
    telemetry_json: str | None = None,
) -> None:
    mark_missing_pairs(conn, review_job_id=review_job_id)
    fail_review_job(
        conn,
        review_job_id=review_job_id,
        failure_reason=failure_reason,
        completed_at=iso_now(),
        telemetry_json=telemetry_json,
    )


def finalize_job_from_parsed(
    *,
    repo_root: Path,
    db_path: Path,
    review_job_id: int,
    expected_pairs: tuple[tuple[str, str], ...],
    parsed: ParsedPairBundle,
    telemetry_json: str | None = None,
) -> tuple[bool, str | None]:
    completed_pairs = tuple(pair for pair in expected_pairs if pair not in set(parsed.missing))
    with connect(db_path) as conn:
        try:
            finalize_job_from_pairs(
                conn,
                review_job_id=review_job_id,
                pairs=completed_pairs,
                parsed=parsed,
                telemetry_json=telemetry_json,
            )
        except ValueError as exc:
            failure_reason = str(exc)
            try:
                # Coverage failures still salvage completed pairs; write
                # those artifacts before committing the failed job state.
                write_finalized_job_artifacts(
                    conn,
                    repo_root=repo_root,
                    review_job_id=review_job_id,
                    parsed=parsed,
                )
            except (OSError, ValueError) as artifact_exc:
                conn.rollback()
                mark_missing_pairs(conn, review_job_id=review_job_id)
                fail_review_job(
                    conn,
                    review_job_id=review_job_id,
                    failure_reason=str(artifact_exc),
                    completed_at=iso_now(),
                    telemetry_json=telemetry_json,
                )
                conn.commit()
                return False, str(artifact_exc)
            conn.commit()
            return False, failure_reason

        try:
            # Keep DB completion/acceptance uncommitted until the derived
            # result artifacts are safely written.
            write_finalized_job_artifacts(
                conn,
                repo_root=repo_root,
                review_job_id=review_job_id,
                parsed=parsed,
            )
        except (OSError, ValueError) as exc:
            conn.rollback()
            mark_missing_pairs(conn, review_job_id=review_job_id)
            fail_review_job(
                conn,
                review_job_id=review_job_id,
                failure_reason=str(exc),
                completed_at=iso_now(),
                telemetry_json=telemetry_json,
            )
            conn.commit()
            return False, str(exc)
        conn.commit()
    return True, None


def finalize_job_bundle_markdown(
    *,
    repo_root: Path,
    db_path: Path,
    review_job_id: int,
    expected_pairs: tuple[tuple[str, str], ...],
    bundle_markdown: str,
    telemetry_json: str | None = None,
) -> tuple[bool, str | None]:
    try:
        parsed = parse_pair_bundle(bundle_markdown, expected_pairs=expected_pairs)
    except ValueError as exc:
        reason = str(exc)
        with connect(db_path) as conn:
            fail_job_for_bundle_parse_error(
                conn,
                review_job_id=review_job_id,
                failure_reason=reason,
                telemetry_json=telemetry_json,
            )
            write_job_manifest_from_db(conn, repo_root=repo_root, review_job_id=review_job_id)
            conn.commit()
        return False, reason

    return finalize_job_from_parsed(
        repo_root=repo_root,
        db_path=db_path,
        review_job_id=review_job_id,
        expected_pairs=expected_pairs,
        parsed=parsed,
        telemetry_json=telemetry_json,
    )
