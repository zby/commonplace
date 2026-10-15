#!/usr/bin/env bash
# Six disk-full interruptions, rerun fresh; see failed-batch-reruns.md. Preserve open old attempts.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 1
output_disk="/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372"
output_dir="$output_disk/outputs/batch-16"
worktree_dir="$output_disk/outputs/commonplace-worktrees"
mountpoint -q "$output_disk" || { printf 'Output disk is not mounted: %s\n' "$output_disk" >&2; exit 1; }
mkdir -p "$output_dir" "$worktree_dir" || exit 1
[[ -w "$output_dir" && -w "$worktree_dir" ]] || { printf 'External output/worktree directories are not writable.\n' >&2; exit 1; }

run() {
  local system=$1 source=$2
  mountpoint -q "$output_disk" || { printf 'Output disk is not mounted: %s\n' "$output_disk" >&2; exit 1; }
  local output="$output_dir/$system.output"
  local worktree="$worktree_dir/batch-16-$system"
  local prompt
  printf -v prompt '/analyse-agentic-system %s\n\nOperator preparation instruction: from the origin checkout, use commonplace-analysis prepare --name %s --worktree %s for isolated run setup. Continue this session in the returned worktree with its returned command prefix. Do not use the default primary-disk worktree location, launch a replacement harness, or resume an old run. Stop if external storage or this new destination is unavailable.' "$source" "$system" "$worktree"
  if [[ -e "$output" ]]; then
    printf 'Skip %s: output already exists; review it before scheduling again.\n' "$system"
    return
  fi
  if [[ -e "$worktree" || -e "$worktree.preparation.json" ]]; then
    printf 'Skip %s: external worktree/preparation already exists; preserve and review it.\n' "$system"
    return
  fi
  printf 'Start %s -> %s; worktree %s\n' "$system" "$output" "$worktree"
  (set -C; pi --approve --model openai/gpt-6.1-sol --thinking medium \
    --tools read,bash,edit,write,subagent --mode json \
    "$prompt" >"$output" 2>&1)
  printf 'Finished %s: process exit %s (not an analysis verdict).\n' "$system" "$?"
}

run kblam https://github.com/microsoft/KBLaM
run llm-wiki-mcp https://github.com/Electro-resonance/LLM-WIKI-MCP
run miroshark https://github.com/aaronjmars/MiroShark
run origin https://github.com/7xuanlu/origin
run isaacclupus-mnemosyn-spec https://github.com/noirblue/IsaacCLupus_mnemosyn_spec
run quicky-wiki https://github.com/anzal1/quicky-wiki
