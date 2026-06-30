#!/usr/bin/env python3
"""Finalize a review job from its persisted bundle output path."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from commonplace.review.executor import JobPairs, finalize_bundle_markdown
from commonplace.review.review_db import (
    connect,
    load_review_job_plan,
    prepare_review_db,
)


def _print_json(payload: dict[str, object]) -> None:
    print(json.dumps(payload, ensure_ascii=True, sort_keys=True))


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


def _precondition_failure(review_job_id: int, reason: str) -> int:
    _print_json(
        {
            "completed": False,
            "state_changed": False,
            "review_job_id": review_job_id,
            "reason": reason,
        }
    )
    return 1


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description="Finalize a review job from its job-owned bundle output.")
    parser.add_argument("--review-job-id", type=int, required=True, help="Review job id to finalize.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)

    with connect(db_path) as conn:
        try:
            plan = load_review_job_plan(conn, review_job_id=args.review_job_id, require_paths=True)
        except ValueError as exc:
            return _precondition_failure(args.review_job_id, str(exc))
    if plan is None:
        return _precondition_failure(args.review_job_id, f"review job not found: {args.review_job_id}")
    if plan.status not in {"queued", "running"}:
        return _precondition_failure(args.review_job_id, f"review job is not finalizable: {plan.status}")
    assert plan.bundle_output_path is not None

    try:
        bundle_output_path = _repo_relative_input_path(repo_root, plan.bundle_output_path)
    except ValueError as exc:
        return _precondition_failure(args.review_job_id, str(exc))
    if not bundle_output_path.is_file():
        return _precondition_failure(
            args.review_job_id,
            f"bundle output file not found: {plan.bundle_output_path}",
        )

    bundle_markdown = bundle_output_path.read_text(encoding="utf-8")
    expected_pairs = tuple((pair.note_path, pair.gate_path) for pair in plan.pairs)
    try:
        completed, failed = finalize_bundle_markdown(
            repo_root=repo_root,
            db_path=db_path,
            job_pairs=[JobPairs(review_job_id=args.review_job_id, pairs=expected_pairs)],
            bundle_markdown=bundle_markdown,
            persist_output=False,
        )
    except ValueError as exc:
        completed = []
        failed = [(args.review_job_id, str(exc))]

    status = _job_status(db_path, args.review_job_id)
    completed_pair_count = _completed_pair_count(db_path, args.review_job_id)
    failed_payload = [{"review_job_id": review_job_id, "reason": reason} for review_job_id, reason in failed]
    completed_ok = not failed and completed == [args.review_job_id]
    _print_json(
        {
            "completed": completed_ok,
            "state_changed": True,
            "review_job_id": args.review_job_id,
            "completed_pair_count": completed_pair_count,
            "failed": failed_payload,
            "job": {
                "review_job_id": args.review_job_id,
                "status": status,
            },
        }
    )
    return 0 if completed_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
