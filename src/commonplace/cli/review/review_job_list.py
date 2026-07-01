#!/usr/bin/env python3
"""List review jobs from the canonical review DB."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from commonplace.cli.review.create_review_jobs import _job_payload
from commonplace.review.review_db import JOB_STATUS_VALUES, connect, list_review_job_plans, prepare_review_db
from commonplace.review.review_model import normalize_model_partition


def _print_table(jobs: list[dict[str, object]]) -> None:
    if not jobs:
        print("review_job_id\tstatus\tmodel_partition\tpacking\trunner\tpairs\tprompt_path\tbundle_output_path\tfailure_reason")
        return
    print("review_job_id\tstatus\tmodel_partition\tpacking\trunner\tpairs\tprompt_path\tbundle_output_path\tfailure_reason")
    for job in jobs:
        print(
            "\t".join(
                [
                    str(job["review_job_id"]),
                    str(job["status"]),
                    str(job["model_partition"]),
                    str(job["packing"]),
                    str(job["runner"] or ""),
                    str(job["pair_count"]),
                    str(job["prompt_path"] or ""),
                    str(job["bundle_output_path"] or ""),
                    str(job.get("failure_reason") or ""),
                ]
            )
        )


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description="List queued, completed, or failed review jobs.")
    parser.add_argument("--status", choices=sorted(JOB_STATUS_VALUES), help="Filter by job status.")
    parser.add_argument("--model", help="Filter by review model partition.")
    parser.add_argument("--json", action="store_true", help="Print JSON.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    model_partition = None
    if args.model is not None:
        if not args.model.strip():
            parser.error("--model must not be empty")
        model_partition = normalize_model_partition(args.model)

    db_path = prepare_review_db(repo_root, args.db)
    with connect(db_path) as conn:
        plans = list_review_job_plans(
            conn,
            status=args.status,
            model_partition=model_partition,
            require_paths=False,
        )

    jobs = [_job_payload(plan, include_timestamps=True) for plan in plans]
    if args.json:
        payload = {
            "filters": {
                "status": args.status,
                "model_partition": model_partition,
            },
            "count": len(jobs),
            "jobs": jobs,
        }
        print(json.dumps(payload, ensure_ascii=True, sort_keys=True))
        return 0

    _print_table(jobs)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
