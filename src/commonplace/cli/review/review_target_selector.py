#!/usr/bin/env python3
"""Select stale review targets from the canonical review DB."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.review.paths import review_gates_dir
from commonplace.review.resolve_criteria import all_gate_requests, resolve_criterion_requests
from commonplace.review.review_target_selector import (
    render_grouped,
    render_json,
    select_requested_criteria,
    select_stale_criteria,
)
from commonplace.review.review_model import normalize_model_partition


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="List assay target (note, criterion) pairs (schema fields use criterion names).",
        allow_abbrev=False,
    )
    parser.add_argument(
        "--mode",
        choices=["stale", "requested"],
        default="stale",
        help="Select stale pairs or emit the explicitly requested applicable pairs.",
    )
    parser.add_argument(
        "criterion_or_bundle",
        nargs="*",
        help=(
            "Gate IDs (e.g. prose/source-residue), bundle names (e.g. prose), "
            "type-conformance requests (type, type/definition), and/or "
            "collection-conformance requests (collection, collection/notes), and/or "
            "the opt-in report-kind critique assay."
        ),
    )
    parser.add_argument(
        "--all-gates",
        action="store_true",
        help="Check every applicable review criterion: all catalog gates plus type- and collection-conformance pairs.",
    )
    parser.add_argument("--note", nargs="+", dest="note_paths", help="Filter to specific note paths or directories.")
    parser.add_argument(
        "--user-verified",
        action="store_true",
        help="Filter to notes with frontmatter user-verified: true.",
    )
    parser.add_argument("--json", action="store_true", help="JSON output (includes diffs for note-changed).")
    parser.add_argument(
        "--model-partition",
        help=(
            "Review model partition to query or acknowledge (a partition name such as "
            "'claude-opus-4.8', not the concrete model that will run). "
            "Omit only for model-agnostic missing-baseline coverage."
        ),
    )
    parser.add_argument(
        "--reason",
        choices=["missing-baseline", "criterion-changed", "note-changed"],
        help="Filter output to a single staleness reason.",
    )
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    model = args.model_partition.strip() if args.model_partition is not None else None
    if args.model_partition is not None and not model:
        parser.error("--model-partition must not be empty")

    gates_dir = review_gates_dir(repo_root)

    if args.all_gates:
        if args.criterion_or_bundle:
            parser.error("criterion/bundle names and --all-gates are mutually exclusive")
        try:
            criterion_ids = all_gate_requests(gates_dir)
        except (FileNotFoundError, ValueError) as exc:
            parser.error(str(exc))
    elif args.criterion_or_bundle:
        try:
            criterion_ids = resolve_criterion_requests(args.criterion_or_bundle, gates_dir)
        except (FileNotFoundError, ValueError) as exc:
            parser.error(str(exc))
    else:
        parser.error("provide criterion/bundle names or --all-gates")

    if args.mode == "requested" and args.reason is not None:
        parser.error("--reason is only valid with --mode stale")
    if args.mode == "requested" and model is None:
        parser.error("--model-partition is required with --mode requested")
    if args.mode == "stale" and model is None and args.reason not in (None, "missing-baseline"):
        parser.error("--model-partition is required unless selecting missing-baseline coverage")

    try:
        if args.mode == "requested":
            records = select_requested_criteria(
                repo_root,
                criterion_ids=criterion_ids,
                note_filter=args.note_paths,
                user_verified_only=args.user_verified,
            )
        else:
            records = select_stale_criteria(
                repo_root,
                model=model,
                criterion_ids=criterion_ids,
                note_filter=args.note_paths,
                user_verified_only=args.user_verified,
                include_diff=args.json,
            )
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))

    if args.reason:
        records = [record for record in records if record.reason == args.reason]

    if args.json:
        print(render_json(records, model_partition=normalize_model_partition(model) if model is not None else None))
    else:
        output = render_grouped(records)
        if output:
            print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
