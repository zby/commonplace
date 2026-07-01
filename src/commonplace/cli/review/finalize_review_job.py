#!/usr/bin/env python3
"""Finalize a review job from its derived bundle output path."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from commonplace.review.finalization import ExecutionMetadata, finalize_review_job_from_owned_output
from commonplace.review.review_db import prepare_review_db
from commonplace.review.review_model import REASONING_EFFORT_VALUES, normalize_reasoning_effort


def _print_json(payload: dict[str, object]) -> None:
    print(json.dumps(payload, ensure_ascii=True, sort_keys=True))


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description="Finalize a review job from its job-owned bundle output.")
    parser.add_argument("--review-job-id", type=int, required=True, help="Review job id to finalize.")
    parser.add_argument("--runner", help="Worker or execution medium that produced the output.")
    parser.add_argument("--model", help="Concrete worker model that produced the output.")
    parser.add_argument("--effort", choices=REASONING_EFFORT_VALUES, help="Concrete worker reasoning effort.")
    parser.add_argument(
        "--telemetry-json",
        help="Opaque per-harness execution telemetry blob, stored verbatim and never interpreted.",
    )
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args(argv)

    runner = args.runner.strip() if args.runner is not None else None
    runner_model = args.model.strip() if args.model is not None else None
    if runner is not None and not runner:
        parser.error("--runner must not be empty")
    if runner_model is not None and not runner_model:
        parser.error("--model must not be empty")
    if args.effort is not None and runner_model is None:
        parser.error("--effort requires --model")
    runner_effort = normalize_reasoning_effort(args.effort)
    telemetry_json = args.telemetry_json if args.telemetry_json else None

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)
    outcome = finalize_review_job_from_owned_output(
        repo_root=repo_root,
        db_path=db_path,
        review_job_id=args.review_job_id,
        execution=ExecutionMetadata(
            runner=runner,
            runner_model=runner_model,
            runner_effort=runner_effort,
            telemetry_json=telemetry_json,
        ),
    )
    _print_json(outcome.to_payload())
    return outcome.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
