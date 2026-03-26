#!/usr/bin/env python3
"""Compatibility wrapper for listing reviewable notes or stale gate pairs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from gate_selector import render_stale_gate, select_stale_gates
from review_state import list_reviewable_notes


REPO_ROOT = Path.cwd()
NOTES_DIR = REPO_ROOT / "kb" / "notes"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "List top-level reviewable notes, or stale gate pairs for a review bundle."
        )
    )
    parser.add_argument(
        "review_type",
        nargs="?",
        help="Review target suffix such as prose-review or semantic-review.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="List all reviewable notes without checking review metadata.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit structured stale gate records instead of grouped plain text.",
    )
    parser.add_argument(
        "--include-unchanged",
        action="store_true",
        help="Legacy flag from the pre-gate selector. No longer supported.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if not NOTES_DIR.is_dir():
        print(f"Directory not found: {NOTES_DIR}", file=sys.stderr)
        sys.exit(1)

    if not args.all and not args.review_type:
        parser.error("provide a review type or pass --all")

    if args.include_unchanged:
        parser.error("--include-unchanged is not supported by the gate selector")

    notes = list_reviewable_notes(NOTES_DIR)
    if args.all:
        if args.json:
            payload = [
                {
                    "note_path": note.relative_to(REPO_ROOT).as_posix(),
                }
                for note in notes
            ]
            print(json.dumps(payload, indent=2))
            return

        for note in notes:
            print(note.relative_to(REPO_ROOT).as_posix())
        return

    assert args.review_type is not None
    try:
        stale_records = select_stale_gates(
            REPO_ROOT,
            bundle_id=args.review_type,
        )
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))

    if args.json:
        print(json.dumps([render_stale_gate(item) for item in stale_records], indent=2))
        return

    grouped: dict[str, list[object]] = {}
    for record in stale_records:
        grouped.setdefault(record.note_path, []).append(record)

    for note_path in sorted(grouped):
        print(note_path)
        for record in sorted(grouped[note_path], key=lambda item: item.gate_id):
            print(f"  - {record.gate_id} ({record.reason})")


if __name__ == "__main__":
    main()
