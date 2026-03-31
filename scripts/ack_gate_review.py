#!/usr/bin/env python3
"""Acknowledge trivial gate-review changes without rewriting review prose."""

from __future__ import annotations

import argparse
from pathlib import Path

from gate_selector import ack_pairs
from review_model import resolve_model


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
        "gate_ids",
        nargs="+",
        help="One or more gate ids, for example prose/source-residue.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    model = resolve_model()
    pairs = [f"{args.note_path}:{gate_id}" for gate_id in args.gate_ids]
    ack_pairs(Path.cwd(), pairs, model)


if __name__ == "__main__":
    main()
