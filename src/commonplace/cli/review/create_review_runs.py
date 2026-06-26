#!/usr/bin/env python3
"""Create one or more review runs and capture their requested gate sets."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from commonplace.review.batch import PreparedBatch, prepare_review_batch
from commonplace.review.gate_packing import group_requested_gates_by_bundle
from commonplace.review.review_db import prepare_review_db
from commonplace.review.review_model import normalize_model_partition


def _prepared_run_payload(
    *,
    bundle: str,
    gate_ids: list[str],
    prepared: PreparedBatch,
) -> dict[str, object]:
    gate_paths = [pair.gate_path for pair in prepared.pairs]
    artifact_dir = Path(prepared.prompt_path).parent.as_posix()
    return {
        "review_run_id": prepared.review_run_id,
        "bundle": bundle,
        "gate_ids": gate_ids,
        "gate_paths": gate_paths,
        "pairs": [
            {
                "review_pair_id": pair.review_pair_id,
                "note_path": pair.note_path,
                "gate_path": pair.gate_path,
                "status": pair.pair_status,
                "result_path": prepared.result_paths[pair.review_pair_id],
            }
            for pair in prepared.pairs
        ],
        "skipped_pairs": [
            {"note_path": pair.note_path, "gate_path": pair.gate_path, "reason": pair.reason}
            for pair in prepared.skipped
        ],
        "artifact_dir": artifact_dir,
        "prompt_path": prepared.prompt_path,
        "bundle_output_path": prepared.bundle_output_path,
        "manifest_path": prepared.manifest_path,
    }


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Create one or more note-local review runs, grouped by gate bundle.",
    )
    parser.add_argument("note_path", help="Repository-relative note path.")
    parser.add_argument("gate_or_bundle", nargs="+", help="Gate IDs and/or bundle names.")
    parser.add_argument("--runner", required=True, help="Runner label, e.g. claude-code, codex, or live-agent.")
    parser.add_argument("--model", required=True, help="Review model partition for these runs.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
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
        groups = group_requested_gates_by_bundle(
            repo_root=repo_root,
            note_path=args.note_path,
            gate_or_bundle=args.gate_or_bundle,
        )
        runs = []
        for group in groups:
            prepared = prepare_review_batch(
                repo_root=repo_root,
                db_path=db_path,
                pairs=[(args.note_path, gate_path) for gate_path in group.gate_paths],
                runner=args.runner,
                model_partition=model_partition,
            )
            runs.append(
                _prepared_run_payload(
                    bundle=group.bundle,
                    gate_ids=group.gate_ids,
                    prepared=prepared,
                )
            )
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))

    payload = {
        "note_path": args.note_path,
        "model_partition": model_partition,
        "runner": args.runner,
        "runs": runs,
    }
    print(json.dumps(payload, ensure_ascii=True, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
