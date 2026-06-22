#!/usr/bin/env python3
"""Create a review run and capture its requested gate set."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from commonplace.review.paths import GATES_ROOT
from commonplace.review.review_db import (
    ReviewPairRequest,
    connect,
    create_run_with_pairs,
    prepare_review_db,
)
from commonplace.review.review_metadata import resolve_review_target
from commonplace.review.review_model import normalize_model_id
from commonplace.review.executor import bundle_artifact_dir
from commonplace.review.run_review_bundle import build_review_run_prompt


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description="Create a review run for one note and gate set.")
    parser.add_argument("note_path", help="Repository-relative note path.")
    parser.add_argument("gate_or_bundle", nargs="+", help="Gate IDs and/or bundle names.")
    parser.add_argument("--runner", required=True, help="Runner name, e.g. claude-code or codex.")
    parser.add_argument("--model", required=True, help="Review model partition for this run.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument("--json", action="store_true", help="Print review run metadata as JSON.")
    parser.add_argument(
        "--with-prompt",
        action="store_true",
        help="Print JSON metadata plus the canonical review prompt for a live-agent run.",
    )
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
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
        review_run_id = create_run_with_pairs(
            conn,
            model_id=model_id,
            runner=args.runner,
            started_at=started_at,
            packing="note",
            pairs=[
                ReviewPairRequest(
                    note_path=args.note_path,
                    gate_id=gate_id,
                    gate_sha=gate_sha,
                    reviewed_note_sha=note_sha,
                    reviewed_note_commit=note_commit,
                    pair_ordinal=ordinal,
                )
                for gate_id, gate_sha, ordinal in run_gates
            ],
        )
        conn.commit()

    artifact_dir = bundle_artifact_dir(repo_root, review_run_id)
    artifact_dir.mkdir(parents=True, exist_ok=True)
    artifact_dir_rel = artifact_dir.relative_to(repo_root).as_posix()
    prompt_path = artifact_dir / "prompt.md"
    prompt_path_rel = prompt_path.relative_to(repo_root).as_posix()
    bundle_output_path = artifact_dir / "bundle-output.md"
    bundle_output_path_rel = bundle_output_path.relative_to(repo_root).as_posix()

    if args.with_prompt:
        prompt = build_review_run_prompt(
            repo_root=repo_root,
            note_path=args.note_path,
            gate_ids=gate_ids,
            gate_texts=gate_texts,
            review_run_id=review_run_id,
            output_mode="file",
            bundle_output_path=bundle_output_path_rel,
        )
        prompt_path.write_text(prompt, encoding="utf-8")

    if args.json or args.with_prompt:
        payload = {
            "review_run_id": review_run_id,
            "note_path": args.note_path,
            "gate_ids": gate_ids,
            "gates": [
                {"gate_id": gid, "path": str(GATES_ROOT / f"{gid}.md"), "text": gate_texts[gid]}
                for gid in gate_ids
            ],
            "model_id": model_id,
            "runner": args.runner,
            "artifact_dir": artifact_dir_rel,
            "bundle_output_path": bundle_output_path_rel,
        }
        if args.with_prompt:
            payload["prompt_path"] = prompt_path_rel
        print(
            json.dumps(
                payload,
                ensure_ascii=True,
                sort_keys=True,
            )
        )
    else:
        print(review_run_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
