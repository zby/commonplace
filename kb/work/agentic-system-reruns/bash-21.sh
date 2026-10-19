#!/usr/bin/env bash
# Eight unfinished targets remain; existing outputs/workspaces are skipped.
# One Pi session per target. No old-run recovery or integration.
# Post-restart check (2026-10-18): Supermemory published all 13 members;
# hashes match effects/publish.json in batch-21-fresh-supermemory, run
# AAS-2026-10-18-supermemory-75d21b14316b-01. Removed from launch list only;
# independent audit and integration remain separate.
# ContextPilot stopped at failed 000009-workflow (runtime input defect).
# OpenRSI was interrupted with 000019-reconciliation open, without publication.
# Preserve both runs; the existing-path guard below skips them, not retries them.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 1

output_disk="/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372"
output_dir="$output_disk/outputs/batch-21"
worktree_dir="$output_disk/outputs/commonplace-worktrees"
mountpoint -q "$output_disk" || { printf 'Output disk is not mounted: %s\n' "$output_disk" >&2; exit 1; }
mkdir -p "$output_dir" "$worktree_dir" || exit 1
method_revision=$(git rev-parse --verify HEAD) || exit 1

run() {
  local system=$1 source=$2
  local output="$output_dir/$system.output"
  local worktree="$worktree_dir/batch-21-fresh-$system"
  local prompt code=0
  if [[ -e "$output" || -L "$output" || -e "$worktree" || -L "$worktree" || -e "$worktree.preparation.json" || -L "$worktree.preparation.json" ]]; then
    printf 'Skip %s: output or workspace already exists.\n' "$system"
    return
  fi
  printf -v prompt '/analyse-agentic-system %s\n\nUse worker profile pi-sol for all analytical and verification jobs. Prepare a fresh isolated run from this checkout with:\ncommonplace-analysis prepare --name %s --worktree %s --revision %s\nContinue in the returned worktree using its returned command prefix. Acquire the source fresh. Do not read or reuse old analyses, reset or resume old runs, integrate, commit or push. Stop on preparation or acquisition failure.' "$source" "$system" "$worktree" "$method_revision"
  printf 'Start %s -> %s\n' "$system" "$output"
  (set -C; pi --approve --model openai/gpt-6.1-sol --thinking medium \
    --tools read,bash,edit,write,subagent --mode json \
    "$prompt" >"$output" 2>&1) || code=$?
  (set -C; printf '%s\n' "$code" >"$output_dir/$system.exit") || exit 1
  printf 'Finished %s: process exit %s (not an analysis verdict).\n' "$system" "$code"
}

run contextpilot https://github.com/Tencent/ContextPilot
run openrsi https://github.com/FrontisAI/OpenRSI
run modularrsi https://github.com/IQuestLab/ModularRSI
run jaz https://github.com/jaz-lang/JAZ
run autogenesis https://github.com/DVampire/Autogenesis
run mehmetgoekce--llm-wiki https://github.com/MehmetGoekce/llm-wiki
run clawvault https://github.com/Versatly/clawvault
run arex-skill https://github.com/VectorSpaceLab/AREX-Skill
