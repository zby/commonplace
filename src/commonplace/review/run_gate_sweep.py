#!/usr/bin/env python3
"""Run one gate across multiple notes in batched runner calls."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from commonplace.review.review_db import DB_ENV_VAR, prepare_review_db
from commonplace.review.run_gate_sweep_lib import run_gate_sweep


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one gate across many notes using batched prompts.")
    parser.add_argument("gate_id", help="Single gate id, e.g. accessibility/undefined-terms.")
    parser.add_argument("--runner", required=True, choices=["claude-code", "codex"])
    parser.add_argument("--model", required=True, help="Requested runner model and initial review model partition.")
    parser.add_argument("--current", action="store_true", help="Limit to notes whose frontmatter status is current.")
    parser.add_argument("--note", nargs="+", dest="note_paths", help="Filter to specific note paths.")
    parser.add_argument("--batch-size", type=int, default=5, help="Notes per runner invocation.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument("--dry-run", action="store_true", help="Print prompts without invoking the runner.")
    args = parser.parse_args()

    if args.batch_size < 1:
        parser.error("--batch-size must be a positive integer")
    if args.current and args.note_paths:
        parser.error("--current and --note are mutually exclusive")

    repo_root = Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)
    if args.db:
        # Threading the override into select_stale_gates and friends, which
        # still read the env var rather than taking an explicit db parameter.
        os.environ[DB_ENV_VAR] = str(db_path)

    try:
        return run_gate_sweep(
            repo_root=repo_root,
            db_path=db_path,
            gate_id=args.gate_id,
            runner=args.runner,
            model=args.model,
            note_paths=args.note_paths,
            current_only=args.current,
            batch_size=args.batch_size,
            dry_run=args.dry_run,
        )
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    raise SystemExit(main())
