#!/usr/bin/env bash
# Batch review sweep using claude -p for each note.
#
# Usage:
#   scripts/review_sweep.sh prose                          # one bundle
#   scripts/review_sweep.sh prose kb/notes/backlinks.md    # filtered to one note
#   scripts/review_sweep.sh --all-gates                    # all bundles, one at a time
#   scripts/review_sweep.sh --all-gates kb/notes/backlinks.md
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
  echo "usage: review_sweep.sh {bundle|--all-gates} [note-paths...]" >&2
  exit 1
fi

# --- Determine bundles to sweep ---

GATES_DIR="kb/instructions/review-gates"

if [[ "$1" == "--all-gates" ]]; then
  shift
  bundles=()
  for dir in "$GATES_DIR"/*/; do
    bundles+=("$(basename "$dir")")
  done
else
  bundles=("$1")
  shift
fi

note_args=("$@")

# --- Sweep function for one bundle ---

sweep_bundle() {
  local bundle="$1"
  shift
  local notes=("$@")

  local selector_args=("$bundle")
  selector_args+=("${notes[@]}")

  local selector_output
  selector_output=$(uv run scripts/gate_selector.py "${selector_args[@]}" --json)

  local grouped
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
    return 0
  fi

  local count
  count=$(echo "$grouped" | wc -l)
  echo "Bundle '$bundle': $count notes to review"

  while IFS=$'\t' read -r note_path gates; do
    echo "--- Reviewing: $note_path ($gates)"

    local prompt="Run kb/instructions/run-review-bundle-on-note.md on $note_path for gates: $gates"

    if claude -p "$prompt"; then
      reviewed=$((reviewed + 1))
    else
      echo "  FAILED: $note_path" >&2
      failed=$((failed + 1))
    fi

    echo ""
  done <<< "$grouped"
}

# --- Run each bundle ---

failed=0
reviewed=0

for bundle in "${bundles[@]}"; do
  echo "=== Bundle: $bundle ==="
  sweep_bundle "$bundle" "${note_args[@]}"
  echo ""
done

# --- Report ---

echo "=== Sweep complete ==="
echo "Reviewed: $reviewed notes"
if [[ $failed -gt 0 ]]; then
  echo "Failed:   $failed notes"
  exit 1
fi
