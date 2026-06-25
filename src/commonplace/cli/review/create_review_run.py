#!/usr/bin/env python3
"""Create a review run and capture its requested gate set."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from commonplace.review.artifacts import result_paths_by_pair_id, write_manifest
from commonplace.review.freshness import capture_review_inputs
from commonplace.review.review_db import (
    connect,
    create_run_with_pairs,
    load_review_pairs_for_run,
    prepare_review_db,
    set_run_artifact_paths,
)
from commonplace.review.review_metadata import resolve_review_target
from commonplace.review.review_model import normalize_model_partition
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
    model_partition = args.model.strip()
    if not model_partition:
        parser.error("--model must not be empty")
    model_partition = normalize_model_partition(model_partition)

    db_path = prepare_review_db(repo_root, args.db)

    try:
        _note_sha, _note_commit, started_at, run_gates, _gate_texts = resolve_review_target(
            repo_root, args.note_path, args.gate_or_bundle,
        )
    except ValueError as exc:
        parser.error(str(exc))
    gate_paths = [g[0] for g in run_gates]

    with connect(db_path) as conn:
        captured_inputs = capture_review_inputs(
            conn,
            repo_root=repo_root,
            pairs=[(args.note_path, gate_path) for gate_path in gate_paths],
        )
        review_run_id = create_run_with_pairs(
            conn,
            model_partition=model_partition,
            runner=args.runner,
            started_at=started_at,
            packing="note",
            pairs=captured_inputs.pair_requests,
        )
        stored_pairs = load_review_pairs_for_run(conn, review_run_id=review_run_id)
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
            gate_paths=gate_paths,
            gate_texts=captured_inputs.gate_texts,
            review_run_id=review_run_id,
            output_mode="file",
            bundle_output_path=bundle_output_path_rel,
            note_text=captured_inputs.note_texts[args.note_path],
        )
        prompt_path.write_text(prompt, encoding="utf-8")
        manifest_path = write_manifest(
            repo_root=repo_root,
            artifact_dir=artifact_dir,
            review_run_id=review_run_id,
            packing="note",
            prompt_path=prompt_path_rel,
            bundle_output_path=bundle_output_path_rel,
            pairs=stored_pairs,
        )
    else:
        manifest_path = None

    with connect(db_path) as conn:
        set_run_artifact_paths(
            conn,
            review_run_id=review_run_id,
            bundle_output_path=bundle_output_path_rel,
            result_paths=result_paths_by_pair_id(
                artifact_dir_rel=artifact_dir_rel,
                packing="note",
                pairs=stored_pairs,
            ),
        )
        conn.commit()

    if args.json or args.with_prompt:
        payload = {
            "review_run_id": review_run_id,
            "note_path": args.note_path,
            "gate_paths": gate_paths,
            "gates": [
                {"gate_path": gate_path, "text": captured_inputs.gate_texts[gate_path]}
                for gate_path in gate_paths
            ],
            "model_partition": model_partition,
            "runner": args.runner,
            "artifact_dir": artifact_dir_rel,
            "bundle_output_path": bundle_output_path_rel,
        }
        if args.with_prompt:
            payload["prompt_path"] = prompt_path_rel
            payload["manifest_path"] = manifest_path
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
