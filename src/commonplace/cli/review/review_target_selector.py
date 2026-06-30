#!/usr/bin/env python3
"""Select stale review targets from the canonical review DB."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.review.acknowledgement import ack_pairs
from commonplace.review.paths import review_gates_dir
from commonplace.review.resolve_gates import resolve_to_gate_ids
from commonplace.review.review_target_selector import (
    print_grouped,
    render_json,
    select_stale_gates,
)
from commonplace.review.review_model import normalize_model_partition


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description="List stale (note, gate) review pairs.")
    parser.add_argument(
        "gate_or_bundle",
        nargs="*",
        help="Gate IDs (e.g. prose/source-residue) and/or bundle names (e.g. prose).",
    )
    parser.add_argument("--all-gates", action="store_true", help="Check all gates.")
    parser.add_argument("--note", nargs="+", dest="note_paths", help="Filter to specific note paths or directories.")
    parser.add_argument("--current", action="store_true", help="Filter to notes with frontmatter status: current.")
    parser.add_argument("--json", action="store_true", help="JSON output (includes diffs for note-changed).")
    parser.add_argument(
        "--model",
        help=(
            "Review model partition to query or acknowledge. "
            "Omit only for model-agnostic missing-review coverage."
        ),
    )
    parser.add_argument(
        "--reason",
        choices=["missing-review", "gate-changed", "note-changed"],
        help="Filter output to a single staleness reason.",
    )
    parser.add_argument(
        "--ack",
        nargs="+",
        metavar="NOTE:GATE",
        help="Ack (note, gate) pairs. Format: note_path:gate_id",
    )
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    model = args.model.strip() if args.model is not None else None
    if args.model is not None and not model:
        parser.error("--model must not be empty")

    if args.ack:
        if model is None:
            parser.error("--model is required with --ack")
        try:
            acked = ack_pairs(repo_root, args.ack, model)
        except (FileNotFoundError, ValueError) as exc:
            parser.error(str(exc))
        for note_path, gate_id in acked:
            print(f"acked: {note_path} {gate_id}")
        return 0

    gates_dir = review_gates_dir(repo_root)

    if args.all_gates:
        if args.gate_or_bundle:
            parser.error("gate/bundle names and --all-gates are mutually exclusive")
        bundles = sorted(d.name for d in gates_dir.iterdir() if d.is_dir())
        try:
            gate_ids = resolve_to_gate_ids(bundles, gates_dir)
        except FileNotFoundError as exc:
            parser.error(str(exc))
    elif args.gate_or_bundle:
        try:
            gate_ids = resolve_to_gate_ids(args.gate_or_bundle, gates_dir)
        except FileNotFoundError as exc:
            parser.error(str(exc))
    else:
        parser.error("provide gate/bundle names or --all-gates")

    if model is None and args.reason not in (None, "missing-review"):
        parser.error("--model is required unless selecting missing-review coverage")

    try:
        records = select_stale_gates(
            repo_root,
            model=model,
            gate_ids=gate_ids,
            note_filter=args.note_paths,
            current_only=args.current,
            include_diff=args.json,
        )
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))

    if args.reason:
        records = [record for record in records if record.reason == args.reason]

    if args.json:
        print(render_json(records, model_partition=normalize_model_partition(model) if model is not None else None))
    else:
        print_grouped(records)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
