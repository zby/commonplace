#!/usr/bin/env bash
# Batch review sweep using claude -p for each note.
#
# Usage:
#   scripts/review_sweep.sh prose                          # one bundle
#   scripts/review_sweep.sh prose kb/notes/backlinks.md    # filtered to one note
#
# Requires: COMMONPLACE_REVIEW_MODEL set in environment.
#
# Optional: run review-triage.md first to ack insignificant note-changed pairs:
#   claude -p "Run kb/instructions/review-triage.md with: prose"
#
# See scripts/REVIEW-SYSTEM.md for the full design.

set -euo pipefail

if [[ -z "${COMMONPLACE_REVIEW_MODEL:-}" ]]; then
  echo "error: COMMONPLACE_REVIEW_MODEL is not set" >&2
  exit 1
fi

if [[ $# -lt 1 ]]; then
  echo "usage: review_sweep.sh {bundle} [note-paths...]" >&2
  exit 1
fi

bundle="$1"
if [[ "$bundle" == --* ]]; then
  echo "error: pass a bundle name (e.g. prose), not a flag" >&2
  exit 1
fi

# --- 1. Run selector and group stale pairs by note ---

selector_output=$(uv run scripts/gate_selector.py "$@" --json)

# Parse JSON into note->gates mapping using python
# Output: one line per note, tab-separated: note_path\tgate1 gate2 gate3
grouped=$(echo "$selector_output" | python3 -c "
import json, sys
data = json.load(sys.stdin)
if not data:
    sys.exit(0)
groups = {}
for entry in data:
    note = entry['note_path']
    gate = entry['gate_id']
    groups.setdefault(note, []).append(gate)
for note in sorted(groups):
    gates = ' '.join(sorted(groups[note]))
    print(f'{note}\t{gates}')
")

if [[ -z "$grouped" ]]; then
  echo "All reviews are fresh. Nothing to do."
  exit 0
fi

note_count=$(echo "$grouped" | wc -l)
pair_count=$(echo "$selector_output" | python3 -c "import json,sys; print(len(json.load(sys.stdin)))")
echo "Sweep: $pair_count stale pairs across $note_count notes"
echo ""

# --- 2. Review each note in a separate claude -p call ---

failed=0
reviewed=0

while IFS=$'\t' read -r note_path gates; do
  echo "--- Reviewing: $note_path ($gates)"

  prompt="Run kb/instructions/run-review-bundle-on-note.md on $note_path for gates: $gates"

  if claude -p "$prompt"; then
    reviewed=$((reviewed + 1))
  else
    echo "  FAILED: $note_path" >&2
    failed=$((failed + 1))
  fi

  echo ""
done <<< "$grouped"

# --- 3. Report ---

echo "=== Sweep complete ==="
echo "Reviewed: $reviewed notes"
if [[ $failed -gt 0 ]]; then
  echo "Failed:   $failed notes"
  exit 1
fi
