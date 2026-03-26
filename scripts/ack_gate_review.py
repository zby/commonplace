#!/usr/bin/env python3
"""Advance recorded gate-review baselines without rewriting review prose."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from gate_reviews import (
    build_current_gate_review_record,
    gate_review_csv_path,
    gate_review_path_for,
    parse_gate_review_metadata,
    require_review_model,
    rebuild_gate_review_index,
    render_gate_review_metadata,
    strip_gate_review_metadata,
)


class AckGateReviewError(Exception):
    """Raised when a gate review acknowledgement target cannot be processed."""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Advance the recorded baseline for one note and one or more gates "
            "without rewriting the stored review prose."
        )
    )
    parser.add_argument(
        "note_path",
        help="Repository-relative note path, for example kb/notes/backlinks.md.",
    )
    parser.add_argument(
        "gate_ids",
        nargs="+",
        help="One or more gate ids, for example prose/source-residue.",
    )
    return parser


def acknowledge_gate(repo_root: Path, note_path: str, gate_id: str) -> str:
    reviews_root = repo_root / "kb" / "reports" / "reviews"
    model = require_review_model()
    review_path = gate_review_path_for(note_path, gate_id, model, reviews_root)
    if not review_path.is_file():
        raise AckGateReviewError(f"Recorded gate review not found: {review_path.relative_to(repo_root)}")

    review_text = review_path.read_text(encoding="utf-8")
    metadata = parse_gate_review_metadata(review_text)
    if metadata is None:
        raise AckGateReviewError(
            f"Gate review metadata missing or invalid in {review_path.relative_to(repo_root)}"
        )

    current_record = build_current_gate_review_record(
        repo_root,
        note_path=note_path,
        gate_id=gate_id,
    )
    review_body = strip_gate_review_metadata(review_text).lstrip("\n")
    review_path.write_text(
        render_gate_review_metadata(current_record) + review_body,
        encoding="utf-8",
    )

    rebuild_gate_review_index(
        reviews_root,
        gate_review_csv_path(repo_root),
    )
    return (
        f"Updated {review_path.relative_to(repo_root)} "
        f"to record {note_path} for {gate_id} with model {current_record.model} at {current_record.recorded_at}"
    )


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    repo_root = Path.cwd()

    failures = 0
    for gate_id in args.gate_ids:
        try:
            print(acknowledge_gate(repo_root, args.note_path, gate_id))
        except AckGateReviewError as exc:
            failures += 1
            print(str(exc), file=sys.stderr)

    if failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
