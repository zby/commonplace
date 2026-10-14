#!/usr/bin/env bash
# Ten sequential analyses. Run from any directory; no queue/takeover bookkeeping.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 1
mkdir -p kb/work/agentic-system-reruns/outputs || exit 1

run() {
  local system=$1 source=$2
  local output="kb/work/agentic-system-reruns/outputs/$system.output"
  if [[ -e "$output" ]]; then
    printf 'Skip %s: output already exists; review it before scheduling again.\n' "$system"
    return
  fi
  printf 'Start %s -> %s\n' "$system" "$output"
  (set -C; pi --approve --model openai/gpt-6.1-sol --thinking medium \
    --tools read,bash,edit,write,subagent --mode json \
    "/analyse-agentic-system $source" >"$output" 2>&1)
  printf 'Finished %s: process exit %s (not an analysis verdict).\n' "$system" "$?"
}

run halo https://github.com/context-labs/halo
run hermes-agent https://github.com/nousresearch/hermes-agent
run hindsight https://github.com/vectorize-io/hindsight
run hyalo https://github.com/ractive/hyalo
run hyperagents https://github.com/facebookresearch/Hyperagents
run interview-doc-agent https://github.com/Shilren/interview-doc-agent
run kblam https://github.com/microsoft/KBLaM
run kgai https://github.com/kgaidev/kgai
run kompl https://github.com/tuirk/Kompl
run lacp https://github.com/0xNyk/lacp
