"""Shared review execution helpers.

The live execution path is queued jobs: create a prompt, claim the job, run a
runner, then finalize the job-owned output. This module keeps the lower-level
pieces shared by those paths: note-target preparation, telemetry helpers,
active-job failure, and parsing/finalizing one job-owned bundle output.
"""

from __future__ import annotations

import json
import re
import sqlite3
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.lib.note_parser import find_markdown_links_with_text
from commonplace.review.artifacts import (
    write_manifest,
    write_pair_result_files_to_persisted_paths,
)
from commonplace.review.finalization import record_and_finalize_job
from commonplace.review.protocol.parser import ParsedPairBundle, parse_pair_bundle
from commonplace.review.protocol.prompt import NoteReviewTarget
from commonplace.review.review_db import (
    ReviewPairCompletion,
    attach_execution_data,
    connect,
    fail_review_job,
    load_review_job_plan,
    mark_missing_pairs,
    review_job_artifact_dir_rel,
)
from commonplace.review.clock import iso_now

URL_SCHEME_RE = re.compile(r"^[a-z]+://", re.IGNORECASE)
USAGE_EXHAUSTION_TEXT = "out of extra usage"
ACTIVE_REVIEW_JOB_STATUSES = frozenset({"queued", "running"})


class UsageExhausted(Exception):
    """Raised when the runner reports that paid usage is exhausted.

    Callers running multiple batches (e.g. review_sweep) should catch this
    and abort the whole sweep rather than continuing.
    """


def bundle_artifact_dir(repo_root: Path, review_job_id: int) -> Path:
    return repo_root / review_job_artifact_dir_rel(review_job_id)


def combine_logs(stdout: str, stderr: str) -> str | None:
    return (stdout + ("\n" if stdout and stderr else "") + stderr).strip() or None


def serialize_telemetry(telemetry: dict[str, object] | None) -> str | None:
    if telemetry is None:
        return None
    return json.dumps(telemetry, ensure_ascii=True, sort_keys=True)


def runner_model_from_telemetry(telemetry: dict[str, object] | None) -> str | None:
    if not isinstance(telemetry, dict):
        return None
    model = telemetry.get("model")
    if not isinstance(model, str) or not model.strip():
        return None
    return model.strip()


def runner_effort_from_telemetry(telemetry: dict[str, object] | None) -> str | None:
    if not isinstance(telemetry, dict):
        return None
    reasoning_effort = telemetry.get("reasoning_effort")
    if not isinstance(reasoning_effort, str) or not reasoning_effort.strip():
        return None
    return reasoning_effort.strip().lower()


def resolve_note_markdown_links(
    *,
    repo_root: Path,
    note_abs: Path,
    note_body: str,
) -> tuple[list[tuple[str, str, str]], list[tuple[str, str]]]:
    resolved: list[tuple[str, str, str]] = []
    unresolved: list[tuple[str, str]] = []
    seen_resolved: set[tuple[str, str, str]] = set()
    seen_unresolved: set[tuple[str, str]] = set()

    repo_root_resolved = repo_root.resolve()
    for link_text, raw_target in find_markdown_links_with_text(note_body):
        if URL_SCHEME_RE.match(raw_target) or raw_target.startswith("#"):
            continue

        bare_target = raw_target.split("#", 1)[0]
        if not bare_target or not bare_target.endswith(".md"):
            continue

        candidate = (note_abs.parent / bare_target).resolve()
        try:
            repo_rel = candidate.relative_to(repo_root_resolved).as_posix()
        except ValueError:
            repo_rel = None

        if candidate.exists() and repo_rel is not None:
            entry = (link_text, raw_target, repo_rel)
            if entry not in seen_resolved:
                seen_resolved.add(entry)
                resolved.append(entry)
            continue

        missing = (link_text, raw_target)
        if missing not in seen_unresolved:
            seen_unresolved.add(missing)
            unresolved.append(missing)

    return resolved, unresolved


def prepare_note_target(
    *,
    repo_root: Path,
    note_path: str,
    review_job_id: int,
    gate_paths: tuple[str, ...],
    note_text: str | None = None,
) -> NoteReviewTarget:
    note_abs = repo_root / note_path
    if note_text is None:
        note_text = note_abs.read_text(encoding="utf-8")
    note_body = frontmatter.strip(note_text).lstrip("\n")
    resolved_links, unresolved_links = resolve_note_markdown_links(
        repo_root=repo_root,
        note_abs=note_abs,
        note_body=note_body,
    )
    return NoteReviewTarget(
        note_path=note_path,
        review_job_id=review_job_id,
        gate_paths=gate_paths,
        note_text=note_text,
        resolved_links=resolved_links,
        unresolved_links=unresolved_links,
    )


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
    """Finalize one job from a parsed pair bundle. Raises ValueError on failure
    (the job is failed in the DB before raising)."""
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
    """Finalize one parsed review job and write its canonical artifacts."""
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
