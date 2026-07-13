#!/usr/bin/env python3
"""Report repository-wide freshness status for registered targets."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.freshness.status import load_target_status, render_status_json, status_exit_code
from commonplace.review.review_db import connect, ensure_db, resolve_db_path
from commonplace.review.review_model import normalize_model_partition


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Report freshness status for registered targets.",
        allow_abbrev=False,
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON status.")
    parser.add_argument("--diff", action="store_true", help="Include unified diffs for changed inputs.")
    parser.add_argument("--all", action="store_true", help="Include fresh targets in JSON output.")
    parser.add_argument(
        "--model-partition",
        help="Filter to one review model partition.",
    )
    parser.add_argument("--db", help="Override operational store path.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    model = args.model_partition.strip() if args.model_partition is not None else None
    if args.model_partition is not None and not model:
        parser.error("--model-partition must not be empty")
    if model is not None:
        model = normalize_model_partition(model)

    db_path = resolve_db_path(repo_root, args.db)
    try:
        ensure_db(db_path)
        with connect(db_path) as conn:
            status = load_target_status(
                conn,
                repo_root=repo_root,
                include_fresh=args.all,
                include_diff=args.diff,
                model_partition=model,
            )
    except (OSError, RuntimeError, ValueError) as exc:
        parser.error(str(exc))

    if args.json:
        print(render_status_json(status, include_all=args.all))
    else:
        if status.exit_class == "fresh":
            print("fresh")
        else:
            for target in status.targets:
                if not target.changed_inputs:
                    continue
                key = target.target_key
                print(
                    f"stale {target.target_kind}: "
                    f"{key['note_path']} :: {key['criterion_path']} ({key['model_partition']})"
                )
                for changed in target.changed_inputs:
                    print(f"  {changed.input_role}: {changed.status}")

    return status_exit_code(status)


if __name__ == "__main__":
    raise SystemExit(main())