#!/usr/bin/env bash
# Batch review sweep using the direct-write review runner.
#
# Usage:
#   scripts/review_sweep.sh prose                          # one bundle
#   scripts/review_sweep.sh prose kb/notes/backlinks.md    # filtered to one note
#   scripts/review_sweep.sh --all-gates                    # all bundles, one at a time
#   scripts/review_sweep.sh --all-gates kb/notes/backlinks.md
#
# Requires: COMMONPLACE_REVIEW_MODEL set in environment.
#
# See scripts/REVIEW-SYSTEM.md for the full design.

set -euo pipefail

if [[ -z "${COMMONPLACE_REVIEW_MODEL:-}" ]]; then
  cat >&2 <<'EOF'
error: COMMONPLACE_REVIEW_MODEL is not set.
This variable determines the review model partition and freshness key.
Set it to the model producing reviews in this run, for example:
  COMMONPLACE_REVIEW_MODEL=gpt-5-4-high
  COMMONPLACE_REVIEW_MODEL=opus-4-6
EOF
  exit 1
fi

if [[ $# -lt 1 ]]; then
  echo "usage: review_sweep.sh {bundle|--all-gates} [note-paths...]" >&2
  exit 1
fi

GATES_DIR="kb/instructions/review-gates"
RUNNER="claude-code"
usage_exhausted_exit_code=99

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

is_usage_exhausted_output() {
  local output_file="$1"
  grep -Fqi "out of extra usage" "$output_file"
}

group_selector_output() {
  python3 -c '
import json
import sys

data = json.load(sys.stdin)
if not data:
    raise SystemExit(0)
groups = {}
for entry in data:
    note = entry["note_path"]
    gate = entry["gate_id"]
    groups.setdefault(note, []).append(gate)
for note in sorted(groups):
    gates = " ".join(sorted(groups[note]))
    print(f"{note}\t{gates}")
'
}

run_bundle_review() {
  local note_path="$1"
  shift
  local gates=("$@")
  local output_file
  local status

  output_file=$(mktemp)
  if uv run scripts/run_review_bundle.py --runner "$RUNNER" "$note_path" "${gates[@]}" >"$output_file" 2>&1; then
    status=0
  else
    status=$?
  fi

  cat "$output_file"

  if is_usage_exhausted_output "$output_file"; then
    rm -f "$output_file"
    echo "error: claude reported extra usage exhaustion; aborting sweep immediately." >&2
    return "$usage_exhausted_exit_code"
  fi

  rm -f "$output_file"
  return "$status"
}

sweep_bundle() {
  local bundle="$1"
  shift
  local notes=("$@")

  local selector_args=("$bundle")
  selector_args+=("${notes[@]}")

  local selector_output
  selector_output=$(uv run scripts/gate_selector.py "${selector_args[@]}" --json)

  local grouped
  grouped=$(printf '%s' "$selector_output" | group_selector_output)

  if [[ -z "$grouped" ]]; then
    return 0
  fi

  local count
  count=$(printf '%s\n' "$grouped" | wc -l)
  echo "Bundle '$bundle': $count notes to review"

  while IFS=$'\t' read -r note_path gates; do
    [[ -n "$note_path" ]] || continue
    echo "--- Reviewing: $note_path ($gates)"

    # shellcheck disable=SC2206
    local gate_args=($gates)
    if run_bundle_review "$note_path" "${gate_args[@]}"; then
      reviewed=$((reviewed + 1))
    else
      local status=$?
      if [[ $status -eq $usage_exhausted_exit_code ]]; then
        return "$usage_exhausted_exit_code"
      fi
      echo "  FAILED: $note_path" >&2
      failed=$((failed + 1))
    fi

    echo ""
  done <<< "$grouped"
}

failed=0
reviewed=0

for bundle in "${bundles[@]}"; do
  echo "=== Bundle: $bundle ==="
  if sweep_bundle "$bundle" "${note_args[@]}"; then
    :
  else
    status=$?
    if [[ $status -eq $usage_exhausted_exit_code ]]; then
      exit 1
    fi
    exit "$status"
  fi
  echo ""
done

echo "=== Sweep complete ==="
echo "Reviewed: $reviewed notes"
if [[ $failed -gt 0 ]]; then
  echo "Failed:   $failed notes"
  exit 1
fi
