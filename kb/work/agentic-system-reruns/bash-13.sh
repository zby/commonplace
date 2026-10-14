#!/usr/bin/env bash
# 20 targets with empty original logs and no recorded run; see disk-recovery-batches.md.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 1
output_disk="/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372"
output_dir="$output_disk/outputs/batch-13"
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

run kgai https://github.com/kgaidev/kgai
run kompl https://github.com/tuirk/Kompl
run lacp https://github.com/0xNyk/lacp
run llm-wiki-v3 https://github.com/vvvvvivekkk/LLM-Wiki-v3
run llmwiki-marimo https://github.com/Clod/llmwiki-marimo
run mem0 https://github.com/mem0ai/mem0
run memex https://github.com/wastedcode/memex
run nao https://github.com/getnao/nao
run nuggets https://github.com/NeoVertex1/nuggets
run o-o https://github.com/jahala/o-o
run okf-harness https://github.com/pumblus/okf-harness
run pageindex https://github.com/VectifyAI/PageIndex
run pal https://github.com/agno-agi/pal
run phantom https://github.com/ghostwright/phantom
run pi-self-learning https://github.com/mcollina/pi-self-learning
run jaz https://github.com/jaz-lang/JAZ
run jaz-evals https://github.com/jaz-lang/jaz-evals
run jepa-anything https://github.com/Gen-Verse/JEPA-Anything
run lhtb https://github.com/zli12321/lhtb
run merchantbench https://github.com/khancold/MerchantBench
