#!/usr/bin/env python3
"""Finalize a review run and advance acceptance for all requested gates."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.review.review_db import (
    connect,
    prepare_review_db,
    record_and_finalize_run,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Finalize a review run after all gate reviews are written.")
    parser.add_argument("--review-run-id", type=int, required=True, help="Review run id to finalize.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)

    with connect(db_path) as conn:
        try:
            gate_count = record_and_finalize_run(conn, review_run_id=args.review_run_id)
        except ValueError as exc:
            conn.commit()
            parser.error(str(exc))
        conn.commit()

    print(f"completed {args.review_run_id} {gate_count}")


if __name__ == "__main__":
    main()
