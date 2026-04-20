#!/usr/bin/env python3
"""Acknowledge trivial gate-review changes without rewriting review prose."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.review.review_target_selector import ack_pairs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Advance the accepted baseline for one note and one or more gates "
            "without rewriting the review body."
        )
    )
    parser.add_argument(
        "note_path",
        help="Repository-relative note path, for example kb/notes/backlinks.md.",
    )
    parser.add_argument(
        "--model",
        required=True,
        help="Review model partition to acknowledge against.",
    )
    parser.add_argument(
        "gate_ids",
        nargs="+",
        help="One or more gate ids, for example prose/source-residue.",
    )
    return parser


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    model = args.model.strip()
    if not model:
        parser.error("--model must not be empty")
    pairs = [f"{args.note_path}:{gate_id}" for gate_id in args.gate_ids]
    repo_root = cwd if cwd is not None else Path.cwd()
    ack_pairs(repo_root, pairs, model)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
