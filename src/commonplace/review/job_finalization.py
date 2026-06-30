"""Job-owned review finalization shared by CLIs and queue runners."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from commonplace.review.executor import finalize_job_bundle_markdown
from commonplace.review.review_db import connect, load_review_job_plan


@dataclass(frozen=True)
class FinalizeReviewJobOutcome:
    completed: bool
    state_changed: bool
    review_job_id: int
    completed_pair_count: int = 0
    failed: tuple[tuple[int, str], ...] = ()
    job_status: str | None = None
    reason: str | None = None

    @property
    def exit_code(self) -> int:
        return 0 if self.completed else 1

    def to_payload(self) -> dict[str, object]:
        if not self.state_changed:
            return {
                "completed": False,
                "state_changed": False,
                "review_job_id": self.review_job_id,
                "reason": self.reason,
            }
        return {
            "completed": self.completed,
            "state_changed": True,
            "review_job_id": self.review_job_id,
            "completed_pair_count": self.completed_pair_count,
            "failed": [
                {"review_job_id": review_job_id, "reason": reason}
                for review_job_id, reason in self.failed
            ],
            "job": {
                "review_job_id": self.review_job_id,
                "status": self.job_status,
            },
        }


def _repo_relative_input_path(repo_root: Path, stored_path: str) -> Path:
    path = Path(stored_path)
    if path.is_absolute():
        raise ValueError(f"bundle output path must be repo-relative: {stored_path}")
    resolved = (repo_root / path).resolve()
    repo_root_resolved = repo_root.resolve()
    if not resolved.is_relative_to(repo_root_resolved):
        raise ValueError(f"bundle output path escapes repo root: {stored_path}")
    return resolved


def _completed_pair_count(db_path: Path, review_job_id: int) -> int:
    with connect(db_path) as conn:
        plan = load_review_job_plan(conn, review_job_id=review_job_id, require_paths=False)
        if plan is None:
            return 0
        return sum(1 for pair in plan.pairs if pair.pair_status == "completed")


def _job_status(db_path: Path, review_job_id: int) -> str | None:
    with connect(db_path) as conn:
        plan = load_review_job_plan(conn, review_job_id=review_job_id, require_paths=False)
        if plan is None:
            return None
        return plan.status


def _precondition_failure(review_job_id: int, reason: str) -> FinalizeReviewJobOutcome:
    return FinalizeReviewJobOutcome(
        completed=False,
        state_changed=False,
        review_job_id=review_job_id,
        reason=reason,
    )


def finalize_review_job_from_owned_output(
    *,
    repo_root: Path,
    db_path: Path,
    review_job_id: int,
    telemetry_json: str | None = None,
) -> FinalizeReviewJobOutcome:
    """Finalize one review job from its persisted bundle output path."""
    with connect(db_path) as conn:
        try:
            plan = load_review_job_plan(conn, review_job_id=review_job_id, require_paths=True)
        except ValueError as exc:
            return _precondition_failure(review_job_id, str(exc))
    if plan is None:
        return _precondition_failure(review_job_id, f"review job not found: {review_job_id}")
    if plan.status not in {"queued", "running"}:
        return _precondition_failure(review_job_id, f"review job is not finalizable: {plan.status}")
    assert plan.bundle_output_path is not None

    try:
        bundle_output_path = _repo_relative_input_path(repo_root, plan.bundle_output_path)
    except ValueError as exc:
        return _precondition_failure(review_job_id, str(exc))
    if not bundle_output_path.is_file():
        return _precondition_failure(
            review_job_id,
            f"bundle output file not found: {plan.bundle_output_path}",
        )

    bundle_markdown = bundle_output_path.read_text(encoding="utf-8")
    expected_pairs = tuple((pair.note_path, pair.gate_path) for pair in plan.pairs)
    completed, failure_reason = finalize_job_bundle_markdown(
        repo_root=repo_root,
        db_path=db_path,
        review_job_id=review_job_id,
        expected_pairs=expected_pairs,
        bundle_markdown=bundle_markdown,
        telemetry_json=telemetry_json,
    )

    completed_pair_count = _completed_pair_count(db_path, review_job_id)
    job_status = _job_status(db_path, review_job_id)
    failed_tuple = () if failure_reason is None else ((review_job_id, failure_reason),)
    return FinalizeReviewJobOutcome(
        completed=completed,
        state_changed=True,
        review_job_id=review_job_id,
        completed_pair_count=completed_pair_count,
        failed=failed_tuple,
        job_status=job_status,
    )
