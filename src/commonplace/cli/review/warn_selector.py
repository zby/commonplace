#!/usr/bin/env python3
"""Select actionable findings from effective warn reviews in the DB."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.review.warn_selector import render_grouped, render_json, scan_reviews


def main() -> None:
    parser = argparse.ArgumentParser(description="Select notes with actionable findings from effective warn reviews.")
    parser.add_argument("note_paths", nargs="*", help="Optional note path filter.")
    parser.add_argument("--json", action="store_true", help="JSON output with full WARN text.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    note_filter = set(args.note_paths) if args.note_paths else None

    notes, stale_gates = scan_reviews(repo_root, note_filter)
    if not notes and not stale_gates:
        print("[]" if args.json else "No warn findings found.")
        return

    if args.json:
        print(render_json(notes, stale_gates))
    else:
        print(render_grouped(notes, stale_gates))


if __name__ == "__main__":
    main()
