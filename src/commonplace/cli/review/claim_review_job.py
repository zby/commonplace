#!/usr/bin/env python3
"""Claim a queued review job for parent-dispatched worker execution."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from commonplace.cli.review.create_review_jobs import _job_payload
from commonplace.review.review_db import (
    ReviewJobClaimError,
    claim_review_job,
    connect,
    prepare_review_db,
)
from commonplace.review.review_model import (
    REASONING_EFFORT_VALUES,
    build_model_partition,
    normalize_reasoning_effort,
)


def _print_json(payload: dict[str, object]) -> None:
    print(json.dumps(payload, ensure_ascii=True, sort_keys=True))


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description="Claim a queued review job for worker dispatch.")
    parser.add_argument("--review-job-id", type=int, required=True, help="Review job id to claim.")
    parser.add_argument("--runner", required=True, help="Worker or execution medium being dispatched.")
    parser.add_argument("--model", required=True, help="Concrete worker model.")
    parser.add_argument("--effort", choices=REASONING_EFFORT_VALUES, help="Concrete worker reasoning effort.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args(argv)

    runner = args.runner.strip()
    runner_model = args.model.strip()
    if not runner:
        parser.error("--runner must not be empty")
    if not runner_model:
        parser.error("--model must not be empty")
    runner_effort = normalize_reasoning_effort(args.effort)
    model_partition = build_model_partition(runner_model, runner_effort)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)

    try:
        with connect(db_path) as conn:
            plan = claim_review_job(
                conn,
                review_job_id=args.review_job_id,
                runner=runner,
                runner_model=runner_model,
                runner_effort=runner_effort,
                model_partition=model_partition,
            )
            conn.commit()
    except ReviewJobClaimError as exc:
        _print_json(
            {
                "claimed": False,
                "review_job_id": args.review_job_id,
                "reason": str(exc),
            }
        )
        return 1

    _print_json(
        {
            "claimed": True,
            "review_job_id": args.review_job_id,
            "job": _job_payload(plan),
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
