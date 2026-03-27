"""Resolve gate IDs and bundle names to concatenated gate text with output paths.

Usage:
    uv run scripts/resolve_gates.py prose/source-residue semantic/grounding-alignment
    uv run scripts/resolve_gates.py prose                # all prose gates
    uv run scripts/resolve_gates.py prose semantic        # all prose + all semantic gates
    uv run scripts/resolve_gates.py --note kb/notes/backlinks.md prose

For each resolved gate, prints:

    === gate: {gate-id} | path: {review-output-path} ===
    <gate file contents without frontmatter>

The path line is only included when --note is provided.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

GATES_ROOT = Path("kb/instructions/review-gates")
REVIEWS_ROOT = Path("kb/reports/reviews")
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n*", re.DOTALL)
MODEL_ENV_VAR = "COMMONPLACE_REVIEW_MODEL"


def encode_note_path(note_path: str) -> str:
    return str(Path(note_path).with_suffix("")).replace("/", "__")


def encode_gate_id(gate_id: str) -> str:
    return gate_id.replace("/", "__")


def encode_model(model: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "-", model).strip("-").lower()


def require_review_model() -> str:
    model = os.environ.get(MODEL_ENV_VAR, "").strip()
    if not model:
        print(f"error: {MODEL_ENV_VAR} is not set", file=sys.stderr)
        sys.exit(1)
    return model


def review_path_for(note_path: str, gate_id: str, model: str) -> str:
    return (REVIEWS_ROOT / encode_note_path(note_path) / f"{encode_gate_id(gate_id)}.{encode_model(model)}.md").as_posix()


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
    parser.add_argument(
        "--note",
        dest="note_path",
        default=None,
        help="Note path — includes the canonical review output path for each gate.",
    )
    args = parser.parse_args()

    repo_root = Path.cwd()
    gates_dir = repo_root / GATES_ROOT
    gate_ids = resolve_to_gate_ids(args.gates, gates_dir)

    if not gate_ids:
        print("error: no gates resolved", file=sys.stderr)
        sys.exit(1)

    model = require_review_model() if args.note_path else None

    for gate_id in gate_ids:
        gate_file = gates_dir / f"{gate_id}.md"
        gate_text = strip_frontmatter(gate_file.read_text(encoding="utf-8"))

        header_parts = [f"gate: {gate_id}"]
        if args.note_path and model:
            header_parts.append(f"path: {review_path_for(args.note_path, gate_id, model)}")

        print(f"=== {' | '.join(header_parts)} ===")
        print(gate_text)


if __name__ == "__main__":
    main()
