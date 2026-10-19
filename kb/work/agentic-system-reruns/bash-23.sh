#!/usr/bin/env bash
# Eight source-first fresh starts. Never resume or overwrite predecessor evidence.
# Run one instance at a time; do not run other batches for these targets concurrently.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 1

output_disk="/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372"
output_dir="$output_disk/outputs/batch-23"
worktree_dir="$output_disk/outputs/commonplace-worktrees"
mountpoint -q "$output_disk" || { printf 'Output disk is not mounted: %s\n' "$output_disk" >&2; exit 1; }
mkdir -p "$output_dir" "$worktree_dir" || exit 1
method_revision=$(git rev-parse --verify HEAD) || exit 1

run() {
  local system=$1 source=$2
  local key=$system retry=0
  local output="$output_dir/$key.output"
  local worktree="$worktree_dir/batch-23-$key"
  local prompt code=0
  while [[ -e "$output" || -L "$output" || -e "$output_dir/$key.exit" || -L "$output_dir/$key.exit" || -e "$worktree" || -L "$worktree" || -e "$worktree.preparation.json" || -L "$worktree.preparation.json" ]]; do
    retry=$((retry + 1))
    key="$system-retry-$retry"
    output="$output_dir/$key.output"
    worktree="$worktree_dir/batch-23-$key"
  done
  printf -v prompt '/analyse-agentic-system %s\n\nUse worker profile pi-sol for all analytical and verification jobs. Prepare a fresh isolated run from this checkout with:\ncommonplace-analysis prepare --name %s --worktree %s --revision %s\nContinue in the returned worktree using its returned command prefix. Acquire the source fresh at its default-branch tip. Preserve the supplied source identity; if it is not a suitable analysis target, report the limitation rather than substituting another source. Do not read or reuse old analyses, audits, correction packets, source checkouts or snapshots. Do not reset or resume old runs, integrate, commit or push. Stop on preparation or acquisition failure.' "$source" "$system" "$worktree" "$method_revision"
  printf 'Start %s -> %s (method %s)\n' "$system" "$output" "$method_revision"
  (set -C; pi --approve --model openai/gpt-6.1-sol --thinking medium \
    --tools read,bash,edit,write,subagent --mode json \
    "$prompt" >"$output" 2>&1) || code=$?
  (set -C; printf '%s\n' "$code" >"$output_dir/$key.exit") || exit 1
  printf 'Finished %s: process exit %s (not an analysis verdict).\n' "$system" "$code"
}

run jaz https://github.com/jaz-lang/JAZ
run autogenesis https://github.com/DVampire/Autogenesis
run mehmetgoekce--llm-wiki https://github.com/MehmetGoekce/llm-wiki
run clawvault https://github.com/Versatly/clawvault
run arex-skill https://github.com/VectorSpaceLab/AREX-Skill
run contextpilot https://github.com/Tencent/ContextPilot
run openrsi https://github.com/FrontisAI/OpenRSI
run supermemory https://github.com/supermemoryai/supermemory
