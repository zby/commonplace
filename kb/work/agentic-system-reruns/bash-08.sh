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

run prime-agent https://github.com/PrimeIntellect-ai/prime-agent
run opensage https://github.com/opensage-agent/OpenSage
run openviking https://github.com/volcengine/OpenViking
run openwiki https://github.com/langchain-ai/openwiki
run operational-ontology-framework https://github.com/fstech-digital/operational-ontology-framework
run origin https://github.com/7xuanlu/origin
run pageindex https://github.com/VectifyAI/PageIndex
run pal https://github.com/agno-agi/pal
run phantom https://github.com/ghostwright/phantom
run pi-self-learning https://github.com/mcollina/pi-self-learning
