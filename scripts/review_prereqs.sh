#!/usr/bin/env bash
# Emit review prerequisite metadata for a note.
# Usage: scripts/review_prereqs.sh <note-path>
set -euo pipefail

if [ $# -ne 1 ] || [ ! -f "$1" ]; then
  echo "Usage: $0 <note-path>" >&2
  exit 1
fi

note_path="$1"
note_sha=$(git hash-object "$note_path")
note_commit=$(git log -1 --format=%H -- "$note_path" 2>/dev/null || echo "")
now=$(date -Iseconds)

echo "note-path: $note_path"
echo "last-full-review-note-sha: $note_sha"
echo "last-full-review-note-commit: $note_commit"
echo "last-full-review-at: $now"
echo "last-accepted-note-sha: $note_sha"
echo "last-accepted-note-commit: $note_commit"
echo "last-accepted-at: $now"
echo "last-acceptance-kind: full-review"
