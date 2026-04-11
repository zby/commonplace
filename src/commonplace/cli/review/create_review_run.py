#!/usr/bin/env python3
"""Create a review run and capture its requested gate set."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from commonplace.review.paths import GATES_ROOT
from commonplace.review.review_db import (
    connect,
    create_run,
    prepare_review_db,
)
from commonplace.review.review_metadata import resolve_review_target
from commonplace.review.review_model import normalize_model_id


BUNDLE_ARTIFACTS_ROOT = Path("kb/reports/bundle-reviews")


def bundle_artifact_dir(repo_root: Path, review_run_id: int) -> Path:
    return repo_root / BUNDLE_ARTIFACTS_ROOT / f"review-run-{review_run_id}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a review run for one note and gate set.")
    parser.add_argument("note_path", help="Repository-relative note path.")
    parser.add_argument("gate_or_bundle", nargs="+", help="Gate IDs and/or bundle names.")
    parser.add_argument("--runner", required=True, help="Runner name, e.g. claude-code or codex.")
    parser.add_argument("--model", required=True, help="Review model partition for this run.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument("--json", action="store_true", help="Print review run metadata as JSON.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    note_abs = repo_root / args.note_path
    if not note_abs.is_file():
        parser.error(f"note not found: {args.note_path}")
    model_id = args.model.strip()
    if not model_id:
        parser.error("--model must not be empty")
    model_id = normalize_model_id(model_id)

    db_path = prepare_review_db(repo_root, args.db)

    try:
        note_sha, note_commit, started_at, run_gates, gate_texts = resolve_review_target(
            repo_root, args.note_path, args.gate_or_bundle,
        )
    except ValueError as exc:
        parser.error(str(exc))
    gate_ids = [g[0] for g in run_gates]

    with connect(db_path) as conn:
        review_run_id = create_run(
            conn,
            note_path=args.note_path,
            model_id=model_id,
            runner=args.runner,
            reviewed_note_sha=note_sha,
            reviewed_note_commit=note_commit,
            started_at=started_at,
            gates=run_gates,
        )
        conn.commit()

    bundle_artifact_dir(repo_root, review_run_id).mkdir(parents=True, exist_ok=True)

    if args.json:
        print(
            json.dumps(
                {
                    "review_run_id": review_run_id,
                    "note_path": args.note_path,
                    "gate_ids": gate_ids,
                    "gates": [
                        {"gate_id": gid, "path": str(GATES_ROOT / f"{gid}.md"), "text": gate_texts[gid]}
                        for gid in gate_ids
                    ],
                    "model_id": model_id,
                    "runner": args.runner,
                },
                ensure_ascii=True,
                sort_keys=True,
            )
        )
    else:
        print(review_run_id)


if __name__ == "__main__":
    main()
