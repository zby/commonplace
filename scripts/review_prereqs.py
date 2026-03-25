#!/usr/bin/env python3
"""Emit review prerequisite metadata for a note.

Usage:
    uv run scripts/review_prereqs.py <note-path>

Outputs YAML-formatted metadata ready to paste into a review header:
    note-path, note-sha, note-commit, timestamp
"""
from __future__ import annotations

import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def git_hash_object(path: Path) -> str:
    result = subprocess.run(
        ["git", "hash-object", str(path)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def git_last_commit(path: Path) -> str:
    result = subprocess.run(
        ["git", "log", "-1", "--format=%H", "--", str(path)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <note-path>", file=sys.stderr)
        sys.exit(1)

    note_path = Path(sys.argv[1])
    if not note_path.exists():
        print(f"File not found: {note_path}", file=sys.stderr)
        sys.exit(1)

    note_sha = git_hash_object(note_path)
    note_commit = git_last_commit(note_path)
    now = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")

    print(f"note-path: {note_path}")
    print(f"last-full-review-note-sha: {note_sha}")
    print(f"last-full-review-note-commit: {note_commit}")
    print(f"last-full-review-at: {now}")
    print(f"last-accepted-note-sha: {note_sha}")
    print(f"last-accepted-note-commit: {note_commit}")
    print(f"last-accepted-at: {now}")
    print(f"last-acceptance-kind: full-review")


if __name__ == "__main__":
    main()
