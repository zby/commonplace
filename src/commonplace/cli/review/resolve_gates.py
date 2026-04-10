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
from commonplace.review.paths import GATES_ROOT
from commonplace.review.resolve_gates import resolve_to_gate_ids


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Resolve gate IDs and bundle names to concatenated gate text.",
    )
    parser.add_argument(
        "gates",
        nargs="+",
        help="Gate IDs (e.g. prose/source-residue) or bundle names (e.g. prose).",
    )
    args = parser.parse_args()

    repo_root = Path.cwd()
    gates_dir = repo_root / GATES_ROOT
    try:
        gate_ids = resolve_to_gate_ids(args.gates, gates_dir)
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)

    if not gate_ids:
        print("error: no gates resolved", file=sys.stderr)
        sys.exit(1)

    for gate_id in gate_ids:
        gate_file = gates_dir / f"{gate_id}.md"
        gate_text = frontmatter.strip(gate_file.read_text(encoding="utf-8")).lstrip("\n")
        print(f"=== gate: {gate_id} ===")
        print(gate_text)


if __name__ == "__main__":
    main()
