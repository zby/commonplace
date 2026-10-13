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

run agno-agentos https://github.com/agno-agi/agno
run awesome-agent-memory https://github.com/TeleAI-UAGI/Awesome-Agent-Memory
run claude-workstream-kit https://github.com/ChristopherA/claude-workstream-kit
run clawvault https://github.com/Versatly/clawvault
run closure-sdk https://github.com/faltz009/Closure-SDK
run cludebot https://github.com/sebbsssss/cludebot
run cobusgreyling--llm-wiki https://github.com/cobusgreyling/llm-wiki
run cocoindex https://github.com/cocoindex-io/cocoindex
run cognee https://github.com/topoteretes/cognee
run company-brain https://github.com/supermemoryai/company-brain
