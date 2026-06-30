"""Execute batched pair reviews: one runner call, per-job salvage and finalize.

The executor owns the lifecycle shared by every packing shape: render one
prompt for a set of note targets, invoke the runner once, parse pair blocks,
then finalize each review job whose pairs all came back and fail the rest.
Failure policy lives here once: usage exhaustion, interrupts, runner errors,
structural parse errors, and per-job missing pairs.
"""

from __future__ import annotations

import json
import re
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.lib.note_parser import find_markdown_links_with_text
from commonplace.review.artifacts import (
    result_paths_by_pair_id,
    write_manifest,
    write_pair_result_files_to_persisted_paths,
)
from commonplace.review.finalization import record_and_finalize_job
from commonplace.review.protocol.parser import ParsedPairBundle, parse_pair_bundle
from commonplace.review.protocol.prompt import NoteReviewTarget, render_pairs_prompt
from commonplace.review.review_db import (
    ReviewPairCompletion,
    attach_execution_data,
    connect,
    fail_review_job,
    load_review_pairs_for_job,
    load_review_job,
    load_review_job_plan,
    mark_missing_pairs,
    review_job_artifact_dir_rel,
    set_job_artifact_paths,
)
from commonplace.review.clock import iso_now
from commonplace.review.review_model import build_model_partition
from commonplace.review.runners import run_prompt


URL_SCHEME_RE = re.compile(r"^[a-z]+://", re.IGNORECASE)
USAGE_EXHAUSTION_TEXT = "out of extra usage"
ACTIVE_REVIEW_JOB_STATUSES = frozenset({"queued", "running"})


class UsageExhausted(Exception):
    """Raised when the runner reports that paid usage is exhausted.

    Callers running multiple batches (e.g. review_sweep) should catch this
    and abort the whole sweep rather than continuing.
    """


@dataclass(frozen=True)
class BatchOutcome:
    completed: list[int]
    failed: list[tuple[int, str]]
    runner_returncode: int

    @property
    def ok(self) -> bool:
        return self.runner_returncode == 0 and not self.failed


@dataclass(frozen=True)
class JobPairs:
    """One review job's identity and expected pair set, for finalization."""

    review_job_id: int
    pairs: tuple[tuple[str, str], ...]


def bundle_artifact_dir(repo_root: Path, review_job_id: int) -> Path:
    return repo_root / review_job_artifact_dir_rel(review_job_id)


def bundle_output_path_for_job(repo_root: Path, review_job_id: int) -> str:
    artifact_dir = bundle_artifact_dir(repo_root, review_job_id)
    return f"{artifact_dir.relative_to(repo_root).as_posix()}/bundle-output.md"


def prompt_path_for_job(repo_root: Path, review_job_id: int) -> str:
    artifact_dir = bundle_artifact_dir(repo_root, review_job_id)
    return f"{artifact_dir.relative_to(repo_root).as_posix()}/prompt.md"


def write_job_artifacts(
    *,
    artifact_dir: Path,
    bundle_markdown: str,
) -> None:
    artifact_dir.mkdir(parents=True, exist_ok=True)
    (artifact_dir / "bundle-output.md").write_text(bundle_markdown, encoding="utf-8")


def write_debug_log_artifact(
    *,
    artifact_dir: Path,
    debug_log: str | None,
) -> None:
    if not debug_log:
        return
    artifact_dir.mkdir(parents=True, exist_ok=True)
    (artifact_dir / "debug.log").write_text(debug_log, encoding="utf-8")


def persist_bundle_artifacts(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    review_job_ids: list[int],
    bundle_markdown: str,
    debug_log: str | None = None,
) -> None:
    for review_job_id in review_job_ids:
        artifact_dir = bundle_artifact_dir(repo_root, review_job_id)
        write_job_artifacts(artifact_dir=artifact_dir, bundle_markdown=bundle_markdown)
        write_debug_log_artifact(artifact_dir=artifact_dir, debug_log=debug_log)
        set_job_artifact_paths(
            conn,
            review_job_id=review_job_id,
            bundle_output_path=bundle_output_path_for_job(repo_root, review_job_id),
        )


def persist_prompt_artifacts(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    review_job_ids: list[int],
    prompt: str,
) -> None:
    for review_job_id in review_job_ids:
        artifact_dir = bundle_artifact_dir(repo_root, review_job_id)
        artifact_dir.mkdir(parents=True, exist_ok=True)
        (artifact_dir / "prompt.md").write_text(prompt, encoding="utf-8")
        artifact_dir_rel = artifact_dir.relative_to(repo_root).as_posix()
        review_job = load_review_job(conn, review_job_id=review_job_id)
        if review_job is None:
            continue
        pairs = load_review_pairs_for_job(conn, review_job_id=review_job_id)
        set_job_artifact_paths(
            conn,
            review_job_id=review_job_id,
            prompt_path=prompt_path_for_job(repo_root, review_job_id),
            bundle_output_path=bundle_output_path_for_job(repo_root, review_job_id),
            result_paths=result_paths_by_pair_id(
                artifact_dir_rel=artifact_dir_rel,
                packing=review_job.packing,
                pairs=pairs,
            ),
        )


def combine_logs(stdout: str, stderr: str) -> str | None:
    return (stdout + ("\n" if stdout and stderr else "") + stderr).strip() or None


def serialize_telemetry(telemetry: dict[str, object] | None) -> str | None:
    if telemetry is None:
        return None
    return json.dumps(telemetry, ensure_ascii=True, sort_keys=True)


def model_partition_from_telemetry(telemetry: dict[str, object] | None) -> str | None:
    if not isinstance(telemetry, dict):
        return None
    model = telemetry.get("model")
    if not isinstance(model, str) or not model.strip():
        return None
    reasoning_effort = telemetry.get("reasoning_effort")
    if reasoning_effort is not None and not isinstance(reasoning_effort, str):
        reasoning_effort = None
    return build_model_partition(model, reasoning_effort)


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


def fail_jobs_for_bundle_parse_error(
    conn: sqlite3.Connection,
    *,
    review_job_ids: list[int],
    failure_reason: str,
    telemetry_json: str | None = None,
) -> None:
    completed_at = iso_now()
    for review_job_id in review_job_ids:
        mark_missing_pairs(conn, review_job_id=review_job_id)
        fail_review_job(
            conn,
            review_job_id=review_job_id,
            failure_reason=failure_reason,
            completed_at=completed_at,
            telemetry_json=telemetry_json,
        )


def finalize_bundle_markdown(
    *,
    repo_root: Path,
    db_path: Path,
    job_pairs: list[JobPairs],
    bundle_markdown: str,
    telemetry_json: str | None = None,
    debug_log: str | None = None,
    raise_parse_errors: bool = False,
    persist_output: bool = True,
) -> tuple[list[int], list[tuple[int, str]]]:
    review_job_ids = [job.review_job_id for job in job_pairs]
    if persist_output:
        with connect(db_path) as conn:
            persist_bundle_artifacts(
                conn,
                repo_root=repo_root,
                review_job_ids=review_job_ids,
                bundle_markdown=bundle_markdown,
                debug_log=debug_log,
            )
            conn.commit()

    expected_pairs = [pair for job in job_pairs for pair in job.pairs]
    try:
        parsed = parse_pair_bundle(bundle_markdown, expected_pairs=expected_pairs)
    except ValueError as exc:
        reason = str(exc)
        with connect(db_path) as conn:
            fail_jobs_for_bundle_parse_error(
                conn,
                review_job_ids=review_job_ids,
                failure_reason=reason,
                telemetry_json=telemetry_json,
            )
            for review_job_id in review_job_ids:
                write_job_manifest_from_db(
                    conn,
                    repo_root=repo_root,
                    review_job_id=review_job_id,
                )
            conn.commit()
        if raise_parse_errors:
            raise
        return [], [(review_job_id, reason) for review_job_id in review_job_ids]

    return finalize_jobs_from_parsed(
        repo_root=repo_root,
        db_path=db_path,
        job_pairs=job_pairs,
        parsed=parsed,
        telemetry_json=telemetry_json,
    )


def execute_batch(
    *,
    repo_root: Path,
    db_path: Path,
    targets: list[NoteReviewTarget],
    gate_texts: dict[str, str],
    runner: str,
    runner_model: str,
    model_partition: str,
) -> BatchOutcome:
    """Run one batched runner call over the given prepared targets.

    Every target must already have its review job created (status running).
    Returns a BatchOutcome; raises UsageExhausted after failing all jobs if
    the runner reports exhausted usage, and re-raises KeyboardInterrupt after
    failing all jobs.
    """
    job_ids = sorted({target.review_job_id for target in targets})
    if len(job_ids) != 1:
        raise ValueError("execute_batch expects one review_job_id per prompt")

    try:
        prompt = render_pairs_prompt(notes=targets, gate_texts=gate_texts)
    except ValueError as exc:
        fail_active_review_jobs(db_path=db_path, review_job_ids=job_ids, failure_reason=str(exc))
        return BatchOutcome(completed=[], failed=[(rid, str(exc)) for rid in job_ids], runner_returncode=0)

    with connect(db_path) as conn:
        persist_prompt_artifacts(
            conn,
            repo_root=repo_root,
            review_job_ids=job_ids,
            prompt=prompt,
        )
        conn.commit()

    try:
        result = run_prompt(runner=runner, prompt=prompt, repo_root=repo_root, model=runner_model)
    except KeyboardInterrupt:
        fail_active_review_jobs(
            db_path=db_path,
            review_job_ids=job_ids,
            failure_reason="review batch interrupted",
        )
        raise

    raw_output = result.stdout
    telemetry_json = serialize_telemetry(result.telemetry)
    concrete_runner_model = runner_model_from_telemetry(result.telemetry) or runner_model
    concrete_runner_effort = runner_effort_from_telemetry(result.telemetry)
    debug_log = combine_logs(result.stdout, result.stderr)
    with connect(db_path) as conn:
        persist_bundle_artifacts(
            conn,
            repo_root=repo_root,
            review_job_ids=job_ids,
            bundle_markdown=raw_output,
            debug_log=debug_log,
        )
        for review_job_id in job_ids:
            attach_execution_data(
                conn,
                review_job_id=review_job_id,
                telemetry_json=telemetry_json,
                runner_model=concrete_runner_model,
                runner_effort=concrete_runner_effort,
            )
        conn.commit()
    actual_model_partition = model_partition_from_telemetry(result.telemetry)
    if actual_model_partition is not None and actual_model_partition != model_partition:
        print(
            (
                f"warning: requested model partition {model_partition} "
                f"does not match runner telemetry {actual_model_partition}; "
                "keeping the declared partition"
            ),
            file=sys.stderr,
        )

    if USAGE_EXHAUSTION_TEXT in (result.stdout + result.stderr).lower():
        fail_active_review_jobs(
            db_path=db_path,
            review_job_ids=job_ids,
            failure_reason="runner reported usage exhausted",
            telemetry_json=telemetry_json,
        )
        raise UsageExhausted()

    if result.returncode != 0:
        reason = f"{runner} exited {result.returncode}"
        fail_active_review_jobs(
            db_path=db_path,
            review_job_ids=job_ids,
            failure_reason=reason,
            telemetry_json=telemetry_json,
        )
        return BatchOutcome(
            completed=[],
            failed=[(rid, reason) for rid in job_ids],
            runner_returncode=result.returncode,
        )

    expected_pairs = [(target.note_path, gate_path) for target in targets for gate_path in target.gate_paths]
    job_pairs = [JobPairs(review_job_id=job_ids[0], pairs=tuple(expected_pairs))]
    completed, failed = finalize_bundle_markdown(
        repo_root=repo_root,
        db_path=db_path,
        job_pairs=job_pairs,
        bundle_markdown=raw_output,
        telemetry_json=telemetry_json,
        debug_log=debug_log,
        persist_output=False,
    )
    return BatchOutcome(completed=completed, failed=failed, runner_returncode=0)


def finalize_jobs_from_parsed(
    *,
    repo_root: Path,
    db_path: Path,
    job_pairs: list[JobPairs],
    parsed: ParsedPairBundle,
    telemetry_json: str | None = None,
) -> tuple[list[int], list[tuple[int, str]]]:
    """Finalize parsed jobs and write each job's canonical artifacts."""
    completed: list[int] = []
    failed: list[tuple[int, str]] = []
    for job in job_pairs:
        completed_pairs = tuple(pair for pair in job.pairs if pair not in set(parsed.missing))
        with connect(db_path) as conn:
            try:
                finalize_job_from_pairs(
                    conn,
                    review_job_id=job.review_job_id,
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
                        review_job_id=job.review_job_id,
                        parsed=parsed,
                    )
                except (OSError, ValueError) as artifact_exc:
                    conn.rollback()
                    mark_missing_pairs(conn, review_job_id=job.review_job_id)
                    fail_review_job(
                        conn,
                        review_job_id=job.review_job_id,
                        failure_reason=str(artifact_exc),
                        completed_at=iso_now(),
                        telemetry_json=telemetry_json,
                    )
                    conn.commit()
                    failed.append((job.review_job_id, str(artifact_exc)))
                    continue
                conn.commit()
                failed.append((job.review_job_id, failure_reason))
                continue

            try:
                # Keep DB completion/acceptance uncommitted until the derived
                # result artifacts are safely written.
                write_finalized_job_artifacts(
                    conn,
                    repo_root=repo_root,
                    review_job_id=job.review_job_id,
                    parsed=parsed,
                )
            except (OSError, ValueError) as exc:
                conn.rollback()
                mark_missing_pairs(conn, review_job_id=job.review_job_id)
                fail_review_job(
                    conn,
                    review_job_id=job.review_job_id,
                    failure_reason=str(exc),
                    completed_at=iso_now(),
                    telemetry_json=telemetry_json,
                )
                conn.commit()
                failed.append((job.review_job_id, str(exc)))
                continue
            conn.commit()
        completed.append(job.review_job_id)
    return completed, failed


def finalize_job_records_from_parsed(
    *,
    db_path: Path,
    job_pairs: list[JobPairs],
    parsed: ParsedPairBundle,
    telemetry_json: str | None = None,
) -> tuple[list[int], list[tuple[int, str]]]:
    """Finalize parsed job records without writing filesystem artifacts."""
    completed: list[int] = []
    failed: list[tuple[int, str]] = []
    for job in job_pairs:
        completed_pairs = tuple(pair for pair in job.pairs if pair not in set(parsed.missing))
        with connect(db_path) as conn:
            try:
                finalize_job_from_pairs(
                    conn,
                    review_job_id=job.review_job_id,
                    pairs=completed_pairs,
                    parsed=parsed,
                    telemetry_json=telemetry_json,
                )
            except ValueError as exc:
                conn.commit()
                failed.append((job.review_job_id, str(exc)))
                continue
            conn.commit()
        completed.append(job.review_job_id)

    return completed, failed
