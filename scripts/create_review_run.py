#!/usr/bin/env python3
"""Create a review run and capture its requested gate set."""

from __future__ import annotations

import argparse
from pathlib import Path

from gate_selector import GATES_ROOT, ensure_db, resolve_db_path
from resolve_gates import resolve_to_gate_ids
from review_db import connect, init_db, insert_review_run, insert_review_run_gates
from review_metadata import git_blob_sha, iso_now, last_commit_for_path
from review_model import resolve_model

SCHEMA_PATH = Path("scripts/review-schema.sql")
SCRIPT_REPO_ROOT = Path(__file__).resolve().parents[1]


def ensure_review_db(repo_root: Path, db_path: Path) -> None:
    if db_path.exists():
        ensure_db(repo_root, db_path)
        return
    schema_path = repo_root / SCHEMA_PATH
    if not schema_path.is_file():
        schema_path = SCRIPT_REPO_ROOT / SCHEMA_PATH
    init_db(db_path, schema_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a review run for one note and gate set.")
    parser.add_argument("note_path", help="Repository-relative note path.")
    parser.add_argument("gate_or_bundle", nargs="+", help="Gate IDs and/or bundle names.")
    parser.add_argument("--runner", required=True, help="Runner name, e.g. claude-code or codex.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument("--model", help="Override COMMONPLACE_REVIEW_MODEL.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    note_abs = repo_root / args.note_path
    if not note_abs.is_file():
        parser.error(f"note not found: {args.note_path}")

    gates_dir = repo_root / GATES_ROOT
    gate_ids = resolve_to_gate_ids(args.gate_or_bundle, gates_dir)
    model_id = args.model or resolve_model()

    db_path = Path(args.db).resolve() if args.db else resolve_db_path(repo_root)
    ensure_review_db(repo_root, db_path)

    note_sha = git_blob_sha(note_abs, write_object=True)
    note_commit = last_commit_for_path(repo_root, Path(args.note_path))
    started_at = iso_now()

    run_gates: list[tuple[str, str, int]] = []
    for ordinal, gate_id in enumerate(gate_ids):
        gate_abs = gates_dir / f"{gate_id}.md"
        if not gate_abs.is_file():
            parser.error(f"gate not found: {gate_id}")
        run_gates.append((gate_id, git_blob_sha(gate_abs), ordinal))

    with connect(db_path) as conn:
        review_run_id = insert_review_run(
            conn,
            note_path=args.note_path,
            model_id=model_id,
            runner=args.runner,
            reviewed_note_sha=note_sha,
            reviewed_note_commit=note_commit,
            started_at=started_at,
            status="running",
        )
        insert_review_run_gates(conn, review_run_id=review_run_id, gates=run_gates)
        conn.commit()

    print(review_run_id)


if __name__ == "__main__":
    main()
