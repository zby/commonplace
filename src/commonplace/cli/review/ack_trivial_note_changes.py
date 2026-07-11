#!/usr/bin/env python3
"""Bulk-ack stale verdict pairs whose watched note parts did not change.

Conformance pairs may be selected (via explicit requests or `--all-gates`) but
never qualify: their criterion documents declare no `watches:`, which means
they watch the whole note, so no note change is trivial against them.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.review.acknowledgement import ack_pairs
from commonplace.review.ack_trivial_note_changes import qualifying_pairs
from commonplace.review.resolve_gates import all_gate_requests, resolve_gate_requests
from commonplace.review.paths import review_gates_dir


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Acknowledge note-changed stale verdict pairs when the criterion's watched "
            "note parts did not change. Conformance pairs never qualify because their "
            "criterion documents declare no watches."
        ),
        allow_abbrev=False,
    )
    parser.add_argument(
        "gate_or_bundle",
        nargs="*",
        help=(
            "Gate IDs (e.g. prose/source-residue), bundle names (e.g. prose), "
            "and/or conformance requests (type/type-name, collection/path)."
        ),
    )
    parser.add_argument(
        "--all-gates",
        action="store_true",
        help="Check all verdict criteria: catalog gates plus type- and collection-conformance pairs.",
    )
    parser.add_argument("--note", nargs="+", dest="note_paths", help="Filter to specific note paths or directories.")
    parser.add_argument("--current", action="store_true", help="Filter to notes with frontmatter status: current.")
    parser.add_argument(
        "--model-partition",
        required=True,
        help="Review model partition to acknowledge against (a partition name, not a concrete model).",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print qualifying pairs without acknowledging them.")
    return parser


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    gates_dir = review_gates_dir(repo_root)
    model = args.model_partition.strip()
    if not model:
        parser.error("--model-partition must not be empty")

    if args.all_gates:
        if args.gate_or_bundle:
            parser.error("gate/bundle names and --all-gates are mutually exclusive")
        try:
            gate_ids = all_gate_requests(gates_dir)
        except (FileNotFoundError, ValueError) as exc:
            parser.error(str(exc))
    elif args.gate_or_bundle:
        try:
            gate_ids = resolve_gate_requests(args.gate_or_bundle, gates_dir)
        except (FileNotFoundError, ValueError) as exc:
            parser.error(str(exc))
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
        return 0

    if args.dry_run:
        for pair in pairs:
            print(pair)
        print(f"\nWould ack {len(pairs)} stale pair(s).")
        return 0

    try:
        acked = ack_pairs(repo_root, pairs, model)
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))
    for note_path, gate_id in acked:
        print(f"acked: {note_path} {gate_id}")
    print(f"acked {len(pairs)} stale pair(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
