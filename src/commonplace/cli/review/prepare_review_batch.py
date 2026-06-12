#!/usr/bin/env python3
"""Create review runs for an arbitrary set of (note, gate) pairs and render
one batch prompt for an external executor (live agent or orchestrator)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from commonplace.review.batch import parse_pair_args, prepare_review_batch
from commonplace.review.review_db import prepare_review_db
from commonplace.review.review_model import normalize_model_id


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Prepare a review batch: create runs for the given pairs and write the canonical prompt.",
    )
    parser.add_argument(
        "pairs",
        nargs="+",
        help="Pairs in note-path::gate-id form, e.g. kb/notes/foo.md::prose/source-residue",
    )
    parser.add_argument("--runner", required=True, help="Runner label recorded on the runs, e.g. live-agent.")
    parser.add_argument("--model", required=True, help="Review model partition for these runs.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args(argv)

    model_id = args.model.strip()
    if not model_id:
        parser.error("--model must not be empty")
    model_id = normalize_model_id(model_id)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)

    try:
        pairs = parse_pair_args(args.pairs)
        prepared = prepare_review_batch(
            repo_root=repo_root,
            db_path=db_path,
            pairs=pairs,
            runner=args.runner,
            model_id=model_id,
        )
    except ValueError as exc:
        parser.error(str(exc))

    payload = {
        "review_runs": [
            {
                "review_run_id": target.review_run_id,
                "note_path": target.note_path,
                "gate_ids": list(target.gate_ids),
            }
            for target in prepared.targets
        ],
        "skipped_pairs": [
            {"note_path": pair.note_path, "gate_id": pair.gate_id, "reason": pair.reason}
            for pair in prepared.skipped
        ],
        "prompt_path": prepared.prompt_path,
        "bundle_output_path": prepared.bundle_output_path,
        "model_id": model_id,
        "runner": args.runner,
    }
    print(json.dumps(payload, ensure_ascii=True, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
