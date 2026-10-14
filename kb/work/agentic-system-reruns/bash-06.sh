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

run playground https://github.com/triblespace/playground
run link https://github.com/gowtham0992/link
run llm-context-base https://github.com/asakin/llm-context-base
run llm-project-wiki https://github.com/akash-r34/llm-project-wiki
run llm-wiki-coordination https://github.com/AEVYRA/llm-wiki-coordination
run llm-wiki-mcp https://github.com/Electro-resonance/LLM-WIKI-MCP
run llm-wiki-v3 https://github.com/vvvvvivekkk/LLM-Wiki-v3
run llmwiki-marimo https://github.com/Clod/llmwiki-marimo
run mem0 https://github.com/mem0ai/mem0
run memex https://github.com/wastedcode/memex
