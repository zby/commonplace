#!/usr/bin/env python3
"""Create a review run and capture its requested gate set."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from commonplace.review.review_db import (
    GATES_ROOT,
    connect,
    ensure_db,
    insert_review_run,
    insert_review_run_gates,
    resolve_db_path,
)
from commonplace.review.resolve_gates import applicable_gate_ids_for_note, resolve_to_gate_ids, strip_frontmatter
from commonplace.review.review_metadata import committed_file_provenance, committed_note_provenance, iso_now


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

    gates_dir = repo_root / GATES_ROOT
    requested_gate_ids = resolve_to_gate_ids(args.gate_or_bundle, gates_dir)
    gate_ids = applicable_gate_ids_for_note(note_abs, requested_gate_ids, gates_dir)
    if not gate_ids:
        parser.error(f"no applicable gates resolved for note: {args.note_path}")
    model_id = args.model.strip()
    if not model_id:
        parser.error("--model must not be empty")

    db_path = Path(args.db).resolve() if args.db else resolve_db_path(repo_root)
    ensure_db(repo_root, db_path)

    try:
        note_sha, note_commit = committed_note_provenance(repo_root, Path(args.note_path))
    except ValueError as exc:
        parser.error(str(exc))
    started_at = iso_now()

    run_gates: list[tuple[str, str, int]] = []
    gate_definitions: list[dict[str, str]] = []
    for ordinal, gate_id in enumerate(gate_ids):
        gate_abs = gates_dir / f"{gate_id}.md"
        if not gate_abs.is_file():
            parser.error(f"gate not found: {gate_id}")
        try:
            gate_sha, _ = committed_file_provenance(repo_root, gate_abs, kind="gate")
        except ValueError as exc:
            parser.error(str(exc))
        run_gates.append((gate_id, gate_sha, ordinal))
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

    bundle_artifact_dir(repo_root, review_run_id).mkdir(parents=True, exist_ok=True)

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
