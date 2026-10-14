#!/usr/bin/env bash
# 18 targets with empty original logs and no recorded run; see disk-recovery-batches.md.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 1
output_disk="/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372"
output_dir="$output_disk/outputs/batch-14"
mountpoint -q "$output_disk" || { printf 'Output disk is not mounted: %s\n' "$output_disk" >&2; exit 1; }
mkdir -p "$output_dir" || exit 1
[[ -w "$output_dir" ]] || { printf 'Output directory is not writable: %s\n' "$output_dir" >&2; exit 1; }

run() {
  local system=$1 source=$2 source_kind=${3:-repository}
  mountpoint -q "$output_disk" || { printf 'Output disk is not mounted: %s\n' "$output_disk" >&2; exit 1; }
  local output="$output_dir/$system.output"
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

run meta-n https://github.com/MinnesotaNLP/Meta-n
run modularrsi https://github.com/IQuestLab/ModularRSI
run nams https://neo4j.com/blog/genai/from-agent-memory-to-portable-skills/ document
run oh-my-pi https://github.com/can1357/oh-my-pi
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
