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

run pond https://github.com/tenequm/pond
run mempalace https://github.com/milla-jovovich/mempalace
run memwiki https://github.com/hereisSwapnil/memwiki
run mentisdb https://github.com/cloudllm-ai/mentisdb
run meta-harness https://github.com/stanford-iris-lab/meta-harness
run miroshark https://github.com/aaronjmars/MiroShark
run nao https://github.com/getnao/nao
run nuggets https://github.com/NeoVertex1/nuggets
run o-o https://github.com/jahala/o-o
run okf-harness https://github.com/pumblus/okf-harness
