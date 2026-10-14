#!/usr/bin/env bash
# Clean residue: 16 untouched targets, sequential; no retries of batches 01–08.
# Selection boundary and exclusions: residue-09.md. This script does not launch itself.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 1
output_disk="/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372"
output_dir="$output_disk/outputs"
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

run thalo https://github.com/rejot-dev/thalo
run theafh--ai-modules https://github.com/TheAFH/ai-modules
run theknowledge https://github.com/BadWally/TheKnowledge
run tolaria https://github.com/refactoringhq/tolaria
run tracecraft https://github.com/arrmlet/tracecraft
run trajectory-informed-memory-generation https://arxiv.org/html/2603.10600v1 document
run virtual-context https://github.com/virtual-context/virtual-context
run vlm-wiki https://github.com/veniVeci/VLM-wiki
run voiden https://github.com/voidenhq/voiden
run voyager https://github.com/MineDojo/Voyager
run weknora https://github.com/Tencent/WeKnora
run wikiskill https://arxiv.org/abs/2608.27454 document
run wikiskill-stahl-g https://github.com/Stahl-G/WikiSkill
run wuphf https://github.com/nex-crm/wuphf
run xmemory https://github.com/hu-xiaobai/xMemory
run zikkaron https://github.com/amanhij/zikkaron
