#!/usr/bin/env python3
"""Resolve gate IDs and bundle names to concatenated gate text.

Usage:
    commonplace-resolve-gates prose/source-residue semantic/grounding-alignment
    commonplace-resolve-gates prose                # all prose gates
    commonplace-resolve-gates prose semantic       # all prose + all semantic gates

For each resolved gate, prints:

    === gate: {gate-id} ===
    <gate file contents without frontmatter>
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review.paths import gate_path_for_id, review_gates_dir
from commonplace.review.resolve_gates import resolve_gate_requests


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Resolve gate IDs and bundle names to concatenated gate text.",
    )
    parser.add_argument(
        "gates",
        nargs="+",
        help="Gate IDs (e.g. prose/source-residue) or bundle names (e.g. prose).",
    )
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    gates_dir = review_gates_dir(repo_root)
    try:
        gate_ids = resolve_gate_requests(args.gates, gates_dir)
    except (FileNotFoundError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if not gate_ids:
        print("error: no gates resolved", file=sys.stderr)
        return 1

    for gate_id in gate_ids:
        gate_file = repo_root / gate_path_for_id(repo_root, gate_id)
        gate_text = frontmatter.strip(gate_file.read_text(encoding="utf-8")).lstrip("\n")
        print(f"=== gate: {gate_id} ===")
        print(gate_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
