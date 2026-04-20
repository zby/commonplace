#!/usr/bin/env python3
"""Finalize a review run and advance acceptance for all requested gates."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.review.finalization import record_and_finalize_run
from commonplace.review.review_db import (
    connect,
    prepare_review_db,
)


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description="Finalize a review run after all gate reviews are written.")
    parser.add_argument("--review-run-id", type=int, required=True, help="Review run id to finalize.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)

    with connect(db_path) as conn:
        try:
            gate_count = record_and_finalize_run(conn, review_run_id=args.review_run_id)
        except ValueError as exc:
            conn.commit()
            parser.error(str(exc))
        conn.commit()

    print(f"completed {args.review_run_id} {gate_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
