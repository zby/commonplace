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

run compound-engineering-plugin https://github.com/EveryInc/compound-engineering-plugin
run context-constitution https://github.com/letta-ai/context-constitution
run contextpilot https://github.com/Tencent/ContextPilot
run continuity https://github.com/uziiuzair/continuity
run coral https://github.com/Human-Agent-Society/CORAL
run cortex https://github.com/abbacusgroup/cortex
run cq https://github.com/mozilla-ai/cq
run crewai-memory https://github.com/crewAIInc/crewAI
run decapod https://github.com/DecapodLabs/decapod
run deja-vu https://github.com/vshulcz/deja-vu
