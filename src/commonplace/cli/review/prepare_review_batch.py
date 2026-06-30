#!/usr/bin/env python3
"""Create review jobs for an arbitrary set of (note, gate) pairs and render
one batch prompt for an external executor (live agent or orchestrator)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from commonplace.review.batch import parse_pair_args, prepare_review_batch
from commonplace.review.review_db import prepare_review_db
from commonplace.review.review_model import normalize_model_partition


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Prepare a review batch: create one job for the given pairs and write the canonical prompt.",
    )
    parser.add_argument(
        "pairs",
        nargs="+",
        help="Pairs in note-path::gate-id form, e.g. kb/notes/foo.md::prose/source-residue",
    )
    parser.add_argument("--runner", required=True, help="Runner label recorded on the jobs, e.g. live-agent.")
    parser.add_argument("--model", required=True, help="Review model partition for these jobs.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args(argv)

    model_partition = args.model.strip()
    if not model_partition:
        parser.error("--model must not be empty")
    model_partition = normalize_model_partition(model_partition)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)

    try:
        pairs = parse_pair_args(args.pairs)
        prepared = prepare_review_batch(
            repo_root=repo_root,
            db_path=db_path,
            pairs=pairs,
            runner=args.runner,
            model_partition=model_partition,
        )
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))

    payload = {
        "review_job_id": prepared.review_job_id,
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
        "prompt_path": prepared.prompt_path,
        "bundle_output_path": prepared.bundle_output_path,
        "manifest_path": prepared.manifest_path,
        "model_partition": model_partition,
        "runner": args.runner,
    }
    print(json.dumps(payload, ensure_ascii=True, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
