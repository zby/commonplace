#!/usr/bin/env python3
"""Finalize a review job from its persisted bundle output path."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from commonplace.review.finalization import finalize_review_job_from_owned_output
from commonplace.review.review_db import prepare_review_db


def _print_json(payload: dict[str, object]) -> None:
    print(json.dumps(payload, ensure_ascii=True, sort_keys=True))


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description="Finalize a review job from its job-owned bundle output.")
    parser.add_argument("--review-job-id", type=int, required=True, help="Review job id to finalize.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)
    outcome = finalize_review_job_from_owned_output(
        repo_root=repo_root,
        db_path=db_path,
        review_job_id=args.review_job_id,
    )
    _print_json(outcome.to_payload())
    return outcome.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
