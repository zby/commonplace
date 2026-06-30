#!/usr/bin/env python3
"""Run queued review jobs through a subprocess runner."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from commonplace.review.review_db import prepare_review_db
from commonplace.review.review_model import REASONING_EFFORT_VALUES
from commonplace.review.run_review_jobs import DEFAULT_LIMIT, run_review_jobs
from commonplace.review.runners import runner_names


def _print_json(payload: dict[str, object]) -> None:
    print(json.dumps(payload, ensure_ascii=True, sort_keys=True))


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run queued review jobs through a subprocess runner.")
    parser.add_argument("--runner", required=True, choices=runner_names(), help="Runner adapter to invoke.")
    parser.add_argument("--model", required=True, help="Concrete runner model.")
    parser.add_argument("--effort", choices=REASONING_EFFORT_VALUES, help="Concrete reasoning effort, if supported.")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help="Maximum queued jobs to run.")
    parser.add_argument("--review-job-id", type=int, help="Narrow execution to one queued review job.")
    parser.add_argument("--stop-on-usage-exhausted", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args(argv)

    if args.limit < 1:
        parser.error("--limit must be a positive integer")
    model = args.model.strip()
    if not model:
        parser.error("--model must not be empty")

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)
    payload, exit_code = run_review_jobs(
        repo_root=repo_root,
        db_path=db_path,
        runner=args.runner,
        model=model,
        effort=args.effort,
        limit=args.limit,
        review_job_id=args.review_job_id,
    )
    _print_json(payload)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
