#!/usr/bin/env python3
"""Create, execute, and finalize note-local review bundle runs."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from commonplace.review.review_db import resolve_db_path
from commonplace.review.run_review_bundles import run_bundles
from commonplace.review.runners import runner_names


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run note-local review bundles and persist them into the review DB.")
    parser.add_argument("note_path", help="Repository-relative note path.")
    parser.add_argument("gate_or_bundle", nargs="+", help="Gate IDs and/or bundle names.")
    parser.add_argument("--runner", required=True, choices=runner_names())
    parser.add_argument("--model", required=True, help="Requested runner model and initial review model partition.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument("--dry-run", action="store_true", help="Print the prompt and staging plan without invoking the runner.")
    args = parser.parse_args(argv)

    repo_root = (cwd if cwd is not None else Path.cwd()).resolve()
    note_abs = repo_root / args.note_path
    if not note_abs.is_file():
        parser.error(f"note not found: {args.note_path}")

    review_model = args.model.strip()
    if not review_model:
        parser.error("--model must not be empty")

    db_path = resolve_db_path(repo_root, args.db)

    try:
        outcome = run_bundles(
            repo_root=repo_root,
            db_path=db_path,
            note_path=args.note_path,
            gate_or_bundle=list(args.gate_or_bundle),
            runner=args.runner,
            model=review_model,
            dry_run=args.dry_run,
        )
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))
    if outcome.stdout:
        print(outcome.stdout, end="")
    if outcome.stderr:
        print(outcome.stderr, end="", file=sys.stderr)
    return outcome.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
