#!/usr/bin/env python3
"""Bulk-ack stale gate pairs whose watched note parts did not change."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.review.ack_trivial_note_changes_lib import qualifying_pairs
from commonplace.review.resolve_gates import resolve_to_gate_ids
from commonplace.review.paths import GATES_ROOT
from commonplace.review.review_target_selector import ack_pairs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Acknowledge note-changed stale pairs when the gate's watched note parts "
            "did not change."
        )
    )
    parser.add_argument(
        "gate_or_bundle",
        nargs="*",
        help="Gate IDs (e.g. prose/source-residue) and/or bundle names (e.g. prose).",
    )
    parser.add_argument("--all-gates", action="store_true", help="Check all gates.")
    parser.add_argument("--note", nargs="+", dest="note_paths", help="Filter to specific note paths.")
    parser.add_argument("--current", action="store_true", help="Filter to notes with frontmatter status: current.")
    parser.add_argument("--model", required=True, help="Review model partition to acknowledge against.")
    parser.add_argument("--dry-run", action="store_true", help="Print qualifying pairs without acknowledging them.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    repo_root = Path.cwd()
    gates_dir = repo_root / GATES_ROOT
    model = args.model.strip()
    if not model:
        parser.error("--model must not be empty")

    if args.all_gates:
        if args.gate_or_bundle:
            parser.error("gate/bundle names and --all-gates are mutually exclusive")
        bundles = sorted(d.name for d in gates_dir.iterdir() if d.is_dir())
        gate_ids = resolve_to_gate_ids(bundles, gates_dir)
    elif args.gate_or_bundle:
        gate_ids = resolve_to_gate_ids(args.gate_or_bundle, gates_dir)
    else:
        parser.error("provide gate/bundle names or --all-gates")

    if args.note_paths and args.current:
        parser.error("--note and --current are mutually exclusive")

    pairs = qualifying_pairs(
        repo_root,
        model=model,
        gate_ids=gate_ids,
        note_filter=args.note_paths,
        current_only=args.current,
    )

    if not pairs:
        print("No qualifying stale pairs found.")
        return

    if args.dry_run:
        for pair in pairs:
            print(pair)
        print(f"\nWould ack {len(pairs)} stale pair(s).")
        return

    ack_pairs(repo_root, pairs, model)
    print(f"acked {len(pairs)} stale pair(s)")


if __name__ == "__main__":
    main()
