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
from typing import Any

from commonplace.lib import frontmatter
from commonplace.review.review_db import GATES_ROOT


def strip_frontmatter(text: str) -> str:
    return frontmatter.strip(text).lstrip("\n")


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


def _load_frontmatter(path: Path) -> dict[str, Any]:
    try:
        parsed = frontmatter.parse(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError):
        return {}
    if not parsed.ok:
        return {}
    return parsed.data


def applicable_gate_ids_for_note(note_path: Path, gate_ids: list[str], gates_dir: Path) -> list[str]:
    note_traits_raw = _load_frontmatter(note_path).get("traits", [])
    note_traits = set(note_traits_raw) if isinstance(note_traits_raw, list) else set()

    applicable: list[str] = []
    for gate_id in gate_ids:
        gate_abs = gates_dir / f"{gate_id}.md"
        gate_meta = _load_frontmatter(gate_abs)
        requires_trait = gate_meta.get("requires_trait")
        if requires_trait and requires_trait not in note_traits:
            continue
        applicable.append(gate_id)
    return applicable


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
