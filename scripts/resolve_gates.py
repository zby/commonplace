"""Resolve gate IDs and bundle names to concatenated gate text.

Usage:
    python3 scripts/resolve_gates.py prose/source-residue semantic/grounding-alignment
    python3 scripts/resolve_gates.py prose                # all prose gates
    python3 scripts/resolve_gates.py prose semantic       # all prose + all semantic gates

For each resolved gate, prints:

    === gate: {gate-id} ===
    <gate file contents without frontmatter>
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from review_db import GATES_ROOT

FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n*", re.DOTALL)


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1).lstrip("\n")


def resolve_to_gate_ids(args: list[str], gates_dir: Path) -> list[str]:
    gate_ids: list[str] = []
    for arg in args:
        bundle_dir = gates_dir / arg
        if bundle_dir.is_dir():
            for gate_file in sorted(bundle_dir.glob("*.md")):
                gate_ids.append(f"{arg}/{gate_file.stem}")
        else:
            gate_file = gates_dir / f"{arg}.md"
            if not gate_file.is_file():
                print(f"error: gate not found: {arg}", file=sys.stderr)
                sys.exit(1)
            gate_ids.append(arg)
    return gate_ids


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
    gate_ids = resolve_to_gate_ids(args.gates, gates_dir)

    if not gate_ids:
        print("error: no gates resolved", file=sys.stderr)
        sys.exit(1)

    for gate_id in gate_ids:
        gate_file = gates_dir / f"{gate_id}.md"
        gate_text = strip_frontmatter(gate_file.read_text(encoding="utf-8"))
        print(f"=== gate: {gate_id} ===")
        print(gate_text)


if __name__ == "__main__":
    main()
