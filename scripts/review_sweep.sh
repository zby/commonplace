#!/usr/bin/env bash
# Batch review sweep using the direct-write review runner.
#
# Usage:
#   scripts/review_sweep.sh --model gpt-5-4-xhigh prose                              # one bundle
#   scripts/review_sweep.sh --model gpt-5-4-xhigh prose kb/notes/backlinks.md        # filtered to one note
#   scripts/review_sweep.sh --model gpt-5-4-xhigh --current prose                    # current notes only
#   scripts/review_sweep.sh --model gpt-5-4-xhigh --runner codex --current prose     # current notes only in Codex
#   scripts/review_sweep.sh --model gpt-5-4-xhigh --all-gates                        # all bundles, one at a time
#   scripts/review_sweep.sh --model gpt-5-4-xhigh --current --all-gates
#
# Default concurrency: 4 note-local review runs at a time.
# Override with REVIEW_SWEEP_JOBS=<n>.
#
# See kb/instructions/REVIEW-SYSTEM.md for the full design.

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: review_sweep.sh --model <model-id> [--runner {claude-code|codex}] [--current] {bundle|--all-gates} [note-paths...]" >&2
  exit 1
fi

GATES_DIR="kb/instructions/review-gates"
RUNNER="claude-code"
MODEL=""
usage_exhausted_exit_code=99
current_only=0
parallelism="${REVIEW_SWEEP_JOBS:-4}"

if ! [[ "$parallelism" =~ ^[1-9][0-9]*$ ]]; then
  echo "error: REVIEW_SWEEP_JOBS must be a positive integer" >&2
  exit 1
fi

while [[ $# -gt 0 ]]; do
  case "$1" in
    --current)
      current_only=1
      shift
      ;;
    --runner)
      if [[ $# -lt 2 ]]; then
        echo "error: --runner requires a value" >&2
        exit 1
      fi
      case "$2" in
        claude-code|codex)
          RUNNER="$2"
          ;;
        *)
          echo "error: --runner must be one of: claude-code, codex" >&2
          exit 1
          ;;
      esac
      shift 2
      ;;
    --model)
      if [[ $# -lt 2 ]]; then
        echo "error: --model requires a value" >&2
        exit 1
      fi
      MODEL="$2"
      shift 2
      ;;
    --all-gates)
      select_all_gates=1
      shift
      break
      ;;
    -*)
      echo "error: unknown option: $1" >&2
      exit 1
      ;;
    *)
      break
      ;;
  esac
done

if [[ -z "$MODEL" ]]; then
  echo "error: --model is required" >&2
  exit 1
fi

if [[ $# -lt 1 && "${select_all_gates:-0}" -ne 1 ]]; then
  echo "usage: review_sweep.sh --model <model-id> [--runner {claude-code|codex}] [--current] {bundle|--all-gates} [note-paths...]" >&2
  exit 1
fi

if [[ "${select_all_gates:-0}" -eq 1 ]]; then
  bundles=()
  for dir in "$GATES_DIR"/*/; do
    bundles+=("$(basename "$dir")")
  done
else
  bundles=("$1")
  shift
fi

note_args=("$@")

if [[ $current_only -eq 1 && ${#note_args[@]} -gt 0 ]]; then
  echo "error: --current and explicit note paths are mutually exclusive" >&2
  exit 1
fi

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
  if uv run scripts/run_review_bundle.py --runner "$RUNNER" --model "$MODEL" "$note_path" "${gates[@]}" >"$output_file" 2>&1; then
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

remove_active_pid() {
  local target_pid="$1"
  local next=()
  local pid
  for pid in "${active_pids[@]}"; do
    if [[ "$pid" != "$target_pid" ]]; then
      next+=("$pid")
    fi
  done
  active_pids=("${next[@]}")
}

collect_one_job() {
  local finished_pid
  local status
  local note_path

  if wait -n -p finished_pid; then
    status=0
  else
    status=$?
  fi

  note_path="${job_note[$finished_pid]}"
  unset "job_note[$finished_pid]"
  remove_active_pid "$finished_pid"

  if [[ $status -eq 0 ]]; then
    reviewed=$((reviewed + 1))
    return 0
  fi

  if [[ $status -eq $usage_exhausted_exit_code ]]; then
    return "$usage_exhausted_exit_code"
  fi

  echo "  FAILED: $note_path" >&2
  failed=$((failed + 1))
  return 0
}

abort_active_jobs() {
  local pid
  for pid in "${active_pids[@]}"; do
    kill "$pid" 2>/dev/null || true
  done
  for pid in "${active_pids[@]}"; do
    wait "$pid" 2>/dev/null || true
  done
  active_pids=()
  job_note=()
}

sweep_bundle() {
  local bundle="$1"
  shift
  local notes=("$@")

  local selector_args=("$bundle" --json)
  if [[ $current_only -eq 1 ]]; then
    selector_args+=(--current)
  elif [[ ${#notes[@]} -gt 0 ]]; then
    selector_args+=(--note "${notes[@]}")
  fi

  local selector_output
  selector_output=$(uv run scripts/review_target_selector.py --model "$MODEL" "${selector_args[@]}")

  local grouped
  grouped=$(printf '%s' "$selector_output" | group_selector_output)

  if [[ -z "$grouped" ]]; then
    return 0
  fi

  local count
  count=$(printf '%s\n' "$grouped" | wc -l)
  echo "Bundle '$bundle': $count notes to review"

  local -a active_pids=()
  declare -A job_note=()

  while IFS=$'\t' read -r note_path gates; do
    [[ -n "$note_path" ]] || continue
    echo "--- Reviewing: $note_path ($gates)"

    # shellcheck disable=SC2206
    local gate_args=($gates)
    run_bundle_review "$note_path" "${gate_args[@]}" &
    local pid=$!
    active_pids+=("$pid")
    job_note["$pid"]="$note_path"

    if [[ ${#active_pids[@]} -ge $parallelism ]]; then
      if collect_one_job; then
        :
      else
        local status=$?
        if [[ $status -eq $usage_exhausted_exit_code ]]; then
          abort_active_jobs
          return "$usage_exhausted_exit_code"
        fi
        return "$status"
      fi
    fi

    echo ""
  done <<< "$grouped"

  while [[ ${#active_pids[@]} -gt 0 ]]; do
    if collect_one_job; then
      :
    else
      local status=$?
      if [[ $status -eq $usage_exhausted_exit_code ]]; then
        abort_active_jobs
        return "$usage_exhausted_exit_code"
      fi
      return "$status"
    fi
  done
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
