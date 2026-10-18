#!/usr/bin/env bash
# Thirteen fresh analyses, one Pi session per target. No old-run recovery or integration.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 1

output_disk="/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372"
output_dir="$output_disk/outputs/batch-22"
worktree_dir="$output_disk/outputs/commonplace-worktrees"
mountpoint -q "$output_disk" || { printf 'Output disk is not mounted: %s\n' "$output_disk" >&2; exit 1; }
mkdir -p "$output_dir" "$worktree_dir" || exit 1
method_revision=$(git rev-parse --verify HEAD) || exit 1

run() {
  local system=$1 source=$2
  local output="$output_dir/$system.output"
  local worktree="$worktree_dir/batch-22-$system"
  local prompt code=0
  if [[ -e "$output" || -L "$output" || -e "$worktree" || -L "$worktree" || -e "$worktree.preparation.json" || -L "$worktree.preparation.json" ]]; then
    printf 'Skip %s: output or workspace already exists.\n' "$system"
    return
  fi
  printf -v prompt '/analyse-agentic-system %s\n\nUse worker profile pi-sol for all analytical and verification jobs. Prepare a fresh isolated run from this checkout with:\ncommonplace-analysis prepare --name %s --worktree %s --revision %s\nContinue in the returned worktree using its returned command prefix. Acquire the source fresh. Preserve the supplied source identity; if it is not a suitable analysis target, report the limitation rather than substituting another source. Do not read or reuse old analyses, reset or resume old runs, integrate, commit or push. Stop on preparation or acquisition failure.' "$source" "$system" "$worktree" "$method_revision"
  printf 'Start %s -> %s\n' "$system" "$output"
  (set -C; pi --approve --model openai/gpt-6.1-sol --thinking medium \
    --tools read,bash,edit,write,subagent --mode json \
    "$prompt" >"$output" 2>&1) || code=$?
  (set -C; printf '%s\n' "$code" >"$output_dir/$system.exit") || exit 1
  printf 'Finished %s: process exit %s (not an analysis verdict).\n' "$system" "$code"
}

run awesome-agent-memory https://github.com/TeleAI-UAGI/Awesome-Agent-Memory
run letta https://github.com/letta-ai/letta
run operational-ontology-framework https://github.com/fstech-digital/operational-ontology-framework
run ai-context-os https://github.com/alexdcd/AI-Context-OS
run nams https://neo4j.com/blog/genai/from-agent-memory-to-portable-skills
run llm-wiki-v3 https://github.com/vvvvvivekkk/LLM-Wiki-v3
run llmwiki-marimo https://github.com/Clod/llmwiki-marimo
run siftly https://github.com/ViperrCrypto/Siftly
run sift-kg https://github.com/juanceresa/sift-kg
run fragility-grid https://github.com/NikolaTesla-007/fragility-grid
run ace https://github.com/ace-agent/ace
run agent-skills-for-context-engineering https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering
run secure-llm-wiki https://github.com/nicobleh/secure-llm-wiki
