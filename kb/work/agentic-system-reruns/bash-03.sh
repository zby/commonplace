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

run dense-mem https://github.com/markhuangai/dense-mem
run docmason https://github.com/JetXu-LLM/DocMason
run eal-bench https://github.com/tommasocerruti/eal-bench
run ecdysis https://github.com/cuiyu-ai/Ecdysis
run echel https://github.com/alirezabbasi/echel
run echoes-vault-opencode https://github.com/psinetron/echoes-vault-opencode
run echowiki https://github.com/mohammadmaso/echowiki
run eidetic https://github.com/LARIkoz/eidetic
run eigenius https://github.com/eigenius/eigenius
run engraph https://github.com/devwhodevs/engraph
