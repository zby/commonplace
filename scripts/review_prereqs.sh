#!/usr/bin/env bash
# Emit review prerequisite metadata for a review.
# Usage: scripts/review_prereqs.sh <note-path> [gate-id]
set -euo pipefail

if [ $# -lt 1 ] || [ $# -gt 2 ] || [ ! -f "$1" ]; then
  echo "Usage: $0 <note-path> [gate-id]" >&2
  exit 1
fi

note_path="$1"
note_sha=$(git hash-object -w "$note_path")
note_commit=$(git log -1 --format=%H -- "$note_path" 2>/dev/null || echo "")
now=$(date -Iseconds)

echo "note-path: $note_path"
if [ $# -eq 2 ]; then
  gate_id="$2"
  gate_path="kb/instructions/review-gates/${gate_id}.md"
  if [ ! -f "$gate_path" ]; then
    echo "Gate not found: $gate_id" >&2
    exit 1
  fi
  gate_fingerprint=$(git hash-object -w "$gate_path")
  echo "gate-id: $gate_id"
  echo "gate-fingerprint: $gate_fingerprint"
  echo "review-type: gate-review"
fi
echo "last-full-review-note-sha: $note_sha"
echo "last-full-review-note-commit: $note_commit"
echo "last-full-review-at: $now"
echo "last-accepted-note-sha: $note_sha"
echo "last-accepted-note-commit: $note_commit"
echo "last-accepted-at: $now"
echo "last-acceptance-kind: full-review"
