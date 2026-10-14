#!/usr/bin/env bash
# Clean residue: 20 untouched targets, sequential; no retries of batches 01–08.
# Selection boundary and exclusions: residue-09.md. This script does not launch itself.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 1
mkdir -p kb/work/agentic-system-reruns/outputs || exit 1

run() {
  local system=$1 source=$2 source_kind=${3:-repository}
  local output="kb/work/agentic-system-reruns/outputs/$system.output"
  local prompt="/analyse-agentic-system $source"
  if [[ "$source_kind" == document ]]; then
    prompt="/analyse-agentic-system Analyse $system from this document source, not a repository: $source. Use a document-grounded boundary; do not use historical reviews or infer an implementation repository."
  fi
  if [[ -e "$output" ]]; then
    printf 'Skip %s: output already exists; review it before scheduling again.\n' "$system"
    return
  fi
  printf 'Start %s -> %s\n' "$system" "$output"
  (set -C; pi --approve --model openai/gpt-6.1-sol --thinking medium \
    --tools read,bash,edit,write,subagent --mode json \
    "$prompt" >"$output" 2>&1)
  printf 'Finished %s: process exit %s (not an analysis verdict).\n' "$system" "$?"
}

run aide2 https://arxiv.org/abs/2609.26457 document
run claude-code-dynamic-workflows https://code.claude.com/docs/en/workflows document
run dualgraph https://github.com/microsoft/DKI_LLM
run fintool https://x.com/nicbstme/status/2015174818497437834 document
run fractal https://github.com/trampoline-ai/fractal
run fragility-grid https://github.com/NikolaTesla-007/fragility-grid
run incremental-self-improvement https://people.idsia.ch/~juergen/fki198-94.pdf document
run isaacclupus-mnemosyn-spec https://github.com/noirblue/IsaacCLupus_mnemosyn_spec
run jaz https://github.com/jaz-lang/JAZ
run jaz-evals https://github.com/jaz-lang/jaz-evals
run jepa-anything https://github.com/Gen-Verse/JEPA-Anything
run kenhuangus--llm-wiki https://github.com/kenhuangus/llm-wiki
run lhtb https://github.com/zli12321/lhtb
run nvk--llm-wiki https://github.com/nvk/llm-wiki
run mehmetgoekce--llm-wiki https://github.com/MehmetGoekce/llm-wiki
run merchantbench https://github.com/khancold/MerchantBench
run meta-n https://github.com/MinnesotaNLP/Meta-n
run modularrsi https://github.com/IQuestLab/ModularRSI
run nams https://neo4j.com/blog/genai/from-agent-memory-to-portable-skills/ document
run oh-my-pi https://github.com/can1357/oh-my-pi
