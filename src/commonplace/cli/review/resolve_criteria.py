#!/usr/bin/env python3
"""Resolve criterion requests to concatenated instruction text.

Usage:
    commonplace-resolve-criteria prose/source-residue semantic/grounding-alignment
    commonplace-resolve-criteria prose                # all prose gates
    commonplace-resolve-criteria prose semantic       # all prose + all semantic gates
    commonplace-resolve-criteria critique             # report-kind critique criterion

For each resolved criterion, prints:

    === criterion: {criterion-id} ===
    <criterion file contents without frontmatter>
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review.paths import criterion_path_for_id, review_gates_dir
from commonplace.review.resolve_criteria import resolve_criterion_requests


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Resolve gate, bundle, concrete conformance, or critique criterion requests.",
    )
    parser.add_argument(
        "criteria",
        nargs="+",
        help="Criterion requests: gate IDs/bundles, concrete type/name or collection/path, or critique.",
    )
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    gates_dir = review_gates_dir(repo_root)
    try:
        criterion_ids = resolve_criterion_requests(args.criteria, gates_dir)
    except (FileNotFoundError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if not criterion_ids:
        print("error: no criteria resolved", file=sys.stderr)
        return 1

    for criterion_id in criterion_ids:
        criterion_file = repo_root / criterion_path_for_id(repo_root, criterion_id)
        criterion_text = frontmatter.strip(criterion_file.read_text(encoding="utf-8")).lstrip("\n")
        print(f"=== criterion: {criterion_id} ===")
        print(criterion_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
