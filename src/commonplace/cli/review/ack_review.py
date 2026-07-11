#!/usr/bin/env python3
"""Carry assay evidence across a note change without rewriting its prose."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.review.acknowledgement import ack_pairs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Advance the freshness baseline for one note and one or more criteria "
            "without rewriting the assay body (the command uses criterion vocabulary)."
        ),
        allow_abbrev=False,
    )
    parser.add_argument(
        "note_path",
        help="Repository-relative note path, for example kb/notes/backlinks.md.",
    )
    parser.add_argument(
        "--model-partition",
        required=True,
        help="Review model partition to acknowledge against (a partition name, not a concrete model).",
    )
    parser.add_argument(
        "criterion_ids",
        nargs="+",
        help="One or more criterion ids, for example prose/source-residue or critique.",
    )
    return parser


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    model = args.model_partition.strip()
    if not model:
        parser.error("--model-partition must not be empty")
    pairs = [f"{args.note_path}:{criterion_id}" for criterion_id in args.criterion_ids]
    repo_root = cwd if cwd is not None else Path.cwd()
    try:
        acked = ack_pairs(repo_root, pairs, model)
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))
    for note_path, criterion_id in acked:
        print(f"acked: {note_path} {criterion_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
