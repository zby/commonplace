#!/usr/bin/env bash
# Clean residue: 20 untouched targets, sequential; no retries of batches 01–08.
# Selection boundary and exclusions: residue-09.md. This script does not launch itself.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 1
mkdir -p kb/work/agentic-system-reruns/outputs || exit 1

run() {
  local system=$1 source=$2 source_kind=${3:-repository}
  local output="kb/work/agentic-system-reruns/outputs/$system.output"
  local prompt="/analyse-agentic-system $source"
  if [[ "$source_kind" == document ]]; then
    prompt="/analyse-agentic-system Analyse $system from this document source, not a repository: $source. Use a document-grounded boundary; do not use historical reviews or infer an implementation repository."
  fi
  if [[ -e "$output" ]]; then
    printf 'Skip %s: output already exists; review it before scheduling again.\n' "$system"
    return
  fi
  printf 'Start %s -> %s\n' "$system" "$output"
  (set -C; pi --approve --model openai/gpt-6.1-sol --thinking medium \
    --tools read,bash,edit,write,subagent --mode json \
    "$prompt" >"$output" 2>&1)
  printf 'Finished %s: process exit %s (not an analysis verdict).\n' "$system" "$?"
}

run openrsi https://github.com/FrontisAI/OpenRSI
run pi-posthorse https://github.com/fitchmultz/pi-posthorse
run pratiyush--llm-wiki https://github.com/Pratiyush/llm-wiki
run primescientist https://github.com/henri-xyu02/PrimeScientist
run prove2me https://github.com/prove2me/Prove2Me_workspace
run quicky-wiki https://github.com/anzal1/quicky-wiki
run reasoning-bank https://github.com/google-research/reasoning-bank
run reflexion https://github.com/noahshinn/reflexion
run reframeweb https://github.com/jubjub727/ReframeWeb
run rem https://github.com/satyammistari/REM
run rsiagent https://github.com/AetherLabsAI/RSIAgent
run sage https://github.com/l33tdawg/sage
run sage-wiki https://github.com/xoai/sage-wiki
run scroll https://github.com/niceirene/qwenpaw
run secure-llm-wiki https://github.com/nicobleh/secure-llm-wiki
run self-training-llm https://github.com/wj210/Self-Training-LLM
run semantic-engine https://github.com/Open-Research-Institute/semantic-engine
run semiont https://github.com/The-AI-Alliance/semiont
run sift-kg https://github.com/juanceresa/sift-kg
run siftly https://github.com/ViperrCrypto/Siftly
