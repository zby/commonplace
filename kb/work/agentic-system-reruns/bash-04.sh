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

run enoch https://github.com/our-ark/enoch
run equipa https://github.com/sbknana/equipa
run evoontology https://github.com/ruc-datalab/EvoOntology
run exo https://github.com/exoharness/exo
run exocomp https://github.com/cookiengineer/exocomp
run expel https://github.com/LeapLabTHU/ExpeL
run funes https://github.com/ulyssestenn/funes
run g-memory https://github.com/bingreeky/GMemory
run getsentry-skills https://github.com/getsentry/skills
run gnosis https://github.com/skorokithakis/gnosis
