"""Sequential subprocess consumer for queued review jobs."""

from __future__ import annotations

import contextlib
import io
from pathlib import Path

from commonplace.review import executor
from commonplace.review.clock import iso_now
from commonplace.review.job_finalization import finalize_review_job_from_owned_output
from commonplace.review.review_db import (
    ReviewJobClaimError,
    ReviewJobPlan,
    attach_execution_data,
    claim_review_job,
    connect,
    fail_review_job,
    list_review_job_plans,
    load_review_job_plan,
    mark_missing_pairs,
)
from commonplace.review.review_model import build_model_partition, normalize_reasoning_effort
from commonplace.review.runners import get_runner


DEFAULT_LIMIT = 1


def _repo_relative_path(repo_root: Path, stored_path: str, *, field_name: str) -> Path:
    path = Path(stored_path)
    if path.is_absolute():
        raise ValueError(f"{field_name} must be repo-relative: {stored_path}")
    resolved = (repo_root / path).resolve()
    repo_root_resolved = repo_root.resolve()
    if not resolved.is_relative_to(repo_root_resolved):
        raise ValueError(f"{field_name} escapes repo root: {stored_path}")
    return resolved


def _missing_path_reason(plan: ReviewJobPlan) -> str | None:
    missing: list[str] = []
    if plan.prompt_path is None:
        missing.append("prompt_path")
    if plan.bundle_output_path is None:
        missing.append("bundle_output_path")
    missing_pair_ids = [str(pair.review_pair_id) for pair in plan.pairs if pair.result_path is None]
    if missing_pair_ids:
        missing.append(f"result_path for review_pair_id(s): {', '.join(missing_pair_ids)}")
    if not missing:
        return None
    return f"review job {plan.review_job_id} is missing load-bearing path(s): {', '.join(missing)}"


def _debug_log_path(bundle_output_path: Path) -> Path:
    return bundle_output_path.parent / "debug.log"


def _rel(repo_root: Path, path: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def _job_payload(
    *,
    plan: ReviewJobPlan | None,
    review_job_id: int,
    status: str,
    runner_returncode: int | None,
    completed_pair_count: int,
    failure_reason: str | None,
    bundle_output_path: str | None = None,
    debug_log_path: str | None = None,
) -> dict[str, object]:
    return {
        "review_job_id": review_job_id,
        "status": status,
        "runner_returncode": runner_returncode,
        "completed_pair_count": completed_pair_count,
        "failure_reason": failure_reason,
        "bundle_output_path": bundle_output_path if bundle_output_path is not None else plan.bundle_output_path if plan else None,
        "debug_log_path": debug_log_path,
    }


def _requested_payload(
    *,
    runner: str,
    model: str,
    effort: str | None,
    model_partition: str,
    limit: int,
    review_job_id: int | None,
) -> dict[str, object]:
    return {
        "runner": runner,
        "model": model,
        "effort": effort,
        "model_partition": model_partition,
        "limit": limit,
        "review_job_id": review_job_id,
    }


def _result_payload(
    *,
    requested: dict[str, object],
    selected_count: int,
    jobs: list[dict[str, object]],
    skipped: list[dict[str, object]],
    usage_exhausted: bool = False,
) -> dict[str, object]:
    completed_count = sum(1 for job in jobs if job.get("status") == "completed")
    failed_count = sum(1 for job in jobs if job.get("status") == "failed")
    return {
        "requested": requested,
        "selected_count": selected_count,
        "completed_count": completed_count,
        "failed_count": failed_count,
        "skipped_count": len(skipped),
        "usage_exhausted": usage_exhausted,
        "jobs": jobs,
        "skipped": skipped,
    }


def _preflight_explicit_job(
    *,
    db_path: Path,
    review_job_id: int,
    requested_partition: str,
) -> tuple[ReviewJobPlan | None, str | None]:
    with connect(db_path) as conn:
        plan = load_review_job_plan(conn, review_job_id=review_job_id, require_paths=False)
    if plan is None:
        return None, f"review job not found: {review_job_id}"
    if plan.status != "queued":
        return plan, f"review job is not claimable: {plan.status}"
    if plan.model_partition != requested_partition:
        return (
            plan,
            f"review job model_partition {plan.model_partition!r} does not match requested partition {requested_partition!r}",
        )
    missing_path_reason = _missing_path_reason(plan)
    if missing_path_reason is not None:
        return plan, missing_path_reason
    return plan, None


def _claim_plan(
    *,
    db_path: Path,
    review_job_id: int,
    runner: str,
    model: str,
    effort: str | None,
    requested_partition: str,
) -> ReviewJobPlan:
    with connect(db_path) as conn:
        plan = claim_review_job(
            conn,
            review_job_id=review_job_id,
            runner=runner,
            runner_model=model,
            runner_effort=effort,
            model_partition=requested_partition,
        )
        conn.commit()
        return plan


def _fail_claimed_job(
    *,
    db_path: Path,
    review_job_id: int,
    failure_reason: str,
    telemetry_json: str | None = None,
) -> None:
    with connect(db_path) as conn:
        mark_missing_pairs(conn, review_job_id=review_job_id)
        fail_review_job(
            conn,
            review_job_id=review_job_id,
            failure_reason=failure_reason,
            completed_at=iso_now(),
            telemetry_json=telemetry_json,
        )
        conn.commit()


def _run_prompt_quietly(
    *,
    runner: str,
    prompt: str,
    repo_root: Path,
    model: str,
    effort: str | None,
):
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        return executor.run_prompt(
            runner=runner,
            prompt=prompt,
            repo_root=repo_root,
            model=model,
            effort=effort,
        )


def _execute_claimed_job(
    *,
    repo_root: Path,
    db_path: Path,
    plan: ReviewJobPlan,
    runner: str,
    model: str,
    effort: str | None,
) -> tuple[dict[str, object], bool, int]:
    assert plan.prompt_path is not None
    assert plan.bundle_output_path is not None
    prompt_path = _repo_relative_path(repo_root, plan.prompt_path, field_name="prompt_path")
    bundle_output_path = _repo_relative_path(repo_root, plan.bundle_output_path, field_name="bundle_output_path")
    prompt_text = prompt_path.read_text(encoding="utf-8")

    try:
        result = _run_prompt_quietly(
            runner=runner,
            prompt=prompt_text,
            repo_root=repo_root,
            model=model,
            effort=effort,
        )
    except KeyboardInterrupt:
        reason = "review job interrupted"
        _fail_claimed_job(db_path=db_path, review_job_id=plan.review_job_id, failure_reason=reason)
        return (
            _job_payload(
                plan=plan,
                review_job_id=plan.review_job_id,
                status="failed",
                runner_returncode=None,
                completed_pair_count=0,
                failure_reason=reason,
            ),
            False,
            130,
        )

    bundle_output_path.parent.mkdir(parents=True, exist_ok=True)
    bundle_output_path.write_text(result.stdout, encoding="utf-8")

    debug_log = executor.combine_logs(result.stdout, result.stderr)
    debug_log_rel: str | None = None
    if debug_log:
        debug_log_path = _debug_log_path(bundle_output_path)
        debug_log_path.write_text(debug_log, encoding="utf-8")
        debug_log_rel = _rel(repo_root, debug_log_path)

    telemetry_json = executor.serialize_telemetry(result.telemetry)
    concrete_runner_model = executor.runner_model_from_telemetry(result.telemetry) or model
    concrete_runner_effort = executor.runner_effort_from_telemetry(result.telemetry)
    with connect(db_path) as conn:
        attach_execution_data(
            conn,
            review_job_id=plan.review_job_id,
            telemetry_json=telemetry_json,
            runner_model=concrete_runner_model,
            runner_effort=concrete_runner_effort,
        )
        conn.commit()

    if executor.USAGE_EXHAUSTION_TEXT in (result.stdout + result.stderr).lower():
        reason = "runner reported usage exhausted"
        _fail_claimed_job(
            db_path=db_path,
            review_job_id=plan.review_job_id,
            failure_reason=reason,
            telemetry_json=telemetry_json,
        )
        return (
            _job_payload(
                plan=plan,
                review_job_id=plan.review_job_id,
                status="failed",
                runner_returncode=result.returncode,
                completed_pair_count=0,
                failure_reason=reason,
                debug_log_path=debug_log_rel,
            ),
            True,
            1,
        )

    if result.returncode != 0:
        reason = f"{runner} exited {result.returncode}"
        _fail_claimed_job(
            db_path=db_path,
            review_job_id=plan.review_job_id,
            failure_reason=reason,
            telemetry_json=telemetry_json,
        )
        return (
            _job_payload(
                plan=plan,
                review_job_id=plan.review_job_id,
                status="failed",
                runner_returncode=result.returncode,
                completed_pair_count=0,
                failure_reason=reason,
                debug_log_path=debug_log_rel,
            ),
            False,
            1,
        )

    finalization = finalize_review_job_from_owned_output(
        repo_root=repo_root,
        db_path=db_path,
        review_job_id=plan.review_job_id,
        telemetry_json=telemetry_json,
    )
    if not finalization.completed and not finalization.state_changed:
        reason = finalization.reason or "review job finalization failed"
        _fail_claimed_job(
            db_path=db_path,
            review_job_id=plan.review_job_id,
            failure_reason=reason,
            telemetry_json=telemetry_json,
        )
        return (
            _job_payload(
                plan=plan,
                review_job_id=plan.review_job_id,
                status="failed",
                runner_returncode=result.returncode,
                completed_pair_count=0,
                failure_reason=reason,
                debug_log_path=debug_log_rel,
            ),
            False,
            1,
        )
    failure_reason = None
    if not finalization.completed:
        failure_reason = "; ".join(reason for _, reason in finalization.failed) or "review job finalization failed"
    return (
        _job_payload(
            plan=plan,
            review_job_id=plan.review_job_id,
            status="completed" if finalization.completed else "failed",
            runner_returncode=result.returncode,
            completed_pair_count=finalization.completed_pair_count,
            failure_reason=failure_reason,
            debug_log_path=debug_log_rel,
        ),
        False,
        finalization.exit_code,
    )


def run_review_jobs(
    *,
    repo_root: Path,
    db_path: Path,
    runner: str,
    model: str,
    effort: str | None = None,
    limit: int | None = None,
    review_job_id: int | None = None,
) -> tuple[dict[str, object], int]:
    run_limit = limit or DEFAULT_LIMIT
    normalized_effort = normalize_reasoning_effort(effort)
    requested_partition = build_model_partition(model, normalized_effort)
    requested = _requested_payload(
        runner=runner,
        model=model,
        effort=normalized_effort,
        model_partition=requested_partition,
        limit=run_limit,
        review_job_id=review_job_id,
    )

    try:
        adapter = get_runner(runner)
    except ValueError as exc:
        payload = _result_payload(requested=requested, selected_count=0, jobs=[], skipped=[])
        payload["error"] = str(exc)
        return payload, 1
    if normalized_effort is not None and not adapter.supports_effort:
        payload = _result_payload(requested=requested, selected_count=0, jobs=[], skipped=[])
        payload["error"] = f"runner {runner!r} does not support reasoning effort"
        return payload, 1

    selected_plans: list[ReviewJobPlan] = []
    if review_job_id is not None:
        explicit_plan, preflight_reason = _preflight_explicit_job(
            db_path=db_path,
            review_job_id=review_job_id,
            requested_partition=requested_partition,
        )
        if preflight_reason is not None:
            job_payload = _job_payload(
                plan=explicit_plan,
                review_job_id=review_job_id,
                status="failed",
                runner_returncode=None,
                completed_pair_count=0,
                failure_reason=preflight_reason,
            )
            return _result_payload(requested=requested, selected_count=1, jobs=[job_payload], skipped=[]), 1
        assert explicit_plan is not None
        selected_plans = [explicit_plan]
    else:
        with connect(db_path) as conn:
            selected_plans = list_review_job_plans(
                conn,
                status="queued",
                model_partition=requested_partition,
                require_paths=False,
            )[:run_limit]

    if not selected_plans:
        return _result_payload(requested=requested, selected_count=0, jobs=[], skipped=[]), 0

    jobs: list[dict[str, object]] = []
    skipped: list[dict[str, object]] = []
    for candidate in selected_plans:
        try:
            plan = _claim_plan(
                db_path=db_path,
                review_job_id=candidate.review_job_id,
                runner=runner,
                model=model,
                effort=normalized_effort,
                requested_partition=requested_partition,
            )
        except ReviewJobClaimError as exc:
            if review_job_id is not None:
                jobs.append(
                    _job_payload(
                        plan=candidate,
                        review_job_id=candidate.review_job_id,
                        status="failed",
                        runner_returncode=None,
                        completed_pair_count=0,
                        failure_reason=str(exc),
                    )
                )
                return _result_payload(requested=requested, selected_count=len(selected_plans), jobs=jobs, skipped=skipped), 1
            skipped.append({"review_job_id": candidate.review_job_id, "reason": str(exc)})
            continue

        job_payload, usage_exhausted, exit_code = _execute_claimed_job(
            repo_root=repo_root,
            db_path=db_path,
            plan=plan,
            runner=runner,
            model=model,
            effort=normalized_effort,
        )
        jobs.append(job_payload)
        if exit_code != 0:
            return (
                _result_payload(
                    requested=requested,
                    selected_count=len(selected_plans),
                    jobs=jobs,
                    skipped=skipped,
                    usage_exhausted=usage_exhausted,
                ),
                exit_code,
            )

    return _result_payload(requested=requested, selected_count=len(selected_plans), jobs=jobs, skipped=skipped), 0
