#!/usr/bin/env python3
"""Select actionable findings from effective warn reviews in the DB."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.review.review_db import prepare_review_db
from commonplace.review.warn_selector import render_grouped, render_json, scan_reviews


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description="Select notes with actionable findings from effective warn reviews.")
    parser.add_argument("note_paths", nargs="*", help="Optional note path filter.")
    parser.add_argument("--json", action="store_true", help="JSON output with full WARN text.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    note_filter = set(args.note_paths) if args.note_paths else None

    db_path = prepare_review_db(repo_root, args.db)
    notes, stale_gates = scan_reviews(repo_root, note_filter, db_path=db_path)
    if not notes and not stale_gates:
        print("[]" if args.json else "No warn findings found.")
        return 0

    if args.json:
        print(render_json(notes, stale_gates))
    else:
        print(render_grouped(notes, stale_gates))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
