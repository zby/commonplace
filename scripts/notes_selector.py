#!/usr/bin/env python3
"""List reviewable notes in kb/notes/."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from review_state import list_reviewable_notes
from selector_engine import (
    collect_review_changes,
    get_selector_policy,
    render_change_record,
)


REPO_ROOT = Path.cwd()
NOTES_DIR = REPO_ROOT / "kb" / "notes"
REVIEWS_DIR = REPO_ROOT / "kb" / "reports" / "reviews"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "List top-level kb notes, or only notes whose content differs from "
            "the revision recorded in their review files."
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
        help="Emit structured change records instead of plain note paths.",
    )
    parser.add_argument(
        "--include-unchanged",
        action="store_true",
        help="Include unchanged notes in JSON output when a review type is provided.",
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

    if args.include_unchanged and not args.json:
        parser.error("--include-unchanged requires --json")

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
        get_selector_policy(args.review_type)
    except ValueError as exc:
        parser.error(str(exc))

    changes = collect_review_changes(
        notes,
        args.review_type,
        REVIEWS_DIR,
        REPO_ROOT,
        include_unchanged=args.include_unchanged,
        include_diff=args.json,
        notes_root=NOTES_DIR,
    )

    if args.json:
        print(
            json.dumps(
                [
                    render_change_record(
                        change,
                        include_status=args.include_unchanged,
                    )
                    for change in changes
                ],
                indent=2,
            )
        )
        return

    for change in changes:
        print(change.note_path)


if __name__ == "__main__":
    main()
