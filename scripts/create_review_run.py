#!/usr/bin/env python3
"""Create a review run and capture its requested gate set."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from review_db import GATES_ROOT, connect, ensure_db, insert_review_run, insert_review_run_gates, resolve_db_path
from resolve_gates import resolve_to_gate_ids, strip_frontmatter
from review_metadata import git_blob_sha, iso_now, last_commit_for_path
from review_model import resolve_model

def main() -> None:
    parser = argparse.ArgumentParser(description="Create a review run for one note and gate set.")
    parser.add_argument("note_path", help="Repository-relative note path.")
    parser.add_argument("gate_or_bundle", nargs="+", help="Gate IDs and/or bundle names.")
    parser.add_argument("--runner", required=True, help="Runner name, e.g. claude-code or codex.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument("--model", help="Override COMMONPLACE_REVIEW_MODEL.")
    parser.add_argument("--json", action="store_true", help="Print review run metadata as JSON.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    note_abs = repo_root / args.note_path
    if not note_abs.is_file():
        parser.error(f"note not found: {args.note_path}")

    gates_dir = repo_root / GATES_ROOT
    gate_ids = resolve_to_gate_ids(args.gate_or_bundle, gates_dir)
    model_id = args.model or resolve_model()

    db_path = Path(args.db).resolve() if args.db else resolve_db_path(repo_root)
    ensure_db(repo_root, db_path)

    note_sha = git_blob_sha(note_abs, write_object=True)
    note_commit = last_commit_for_path(repo_root, Path(args.note_path))
    started_at = iso_now()

    run_gates: list[tuple[str, str, int]] = []
    gate_definitions: list[dict[str, str]] = []
    for ordinal, gate_id in enumerate(gate_ids):
        gate_abs = gates_dir / f"{gate_id}.md"
        if not gate_abs.is_file():
            parser.error(f"gate not found: {gate_id}")
        run_gates.append((gate_id, git_blob_sha(gate_abs), ordinal))
        gate_definitions.append(
            {
                "gate_id": gate_id,
                "path": str(gate_abs.relative_to(repo_root)),
                "text": strip_frontmatter(gate_abs.read_text(encoding="utf-8")),
            }
        )

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

    if args.json:
        print(
            json.dumps(
                {
                    "review_run_id": review_run_id,
                    "note_path": args.note_path,
                    "gate_ids": gate_ids,
                    "gates": gate_definitions,
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
