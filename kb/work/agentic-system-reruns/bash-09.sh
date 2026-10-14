#!/usr/bin/env bash
# Clean residue: 76 untouched targets, sequential; no retries of batches 01–08.
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
run openrsi https://github.com/FrontisAI/OpenRSI
run pi-posthorse https://github.com/fitchmultz/pi-posthorse
run pratiyush--llm-wiki https://github.com/Pratiyush/llm-wiki
run primescientist https://github.com/henri-xyu02/PrimeScientist
run prove2me https://github.com/prove2me/Prove2Me_workspace
run quicky-wiki https://github.com/anzal1/quicky-wiki
run reasoning-bank https://github.com/google-research/reasoning-bank
run reflexion https://github.com/noahshinn/reflexion
run reframeweb https://github.com/jubjub727/ReframeWeb
run rem https://github.com/satyammistari/REM
run rsiagent https://github.com/AetherLabsAI/RSIAgent
run sage https://github.com/l33tdawg/sage
run sage-wiki https://github.com/xoai/sage-wiki
run scroll https://github.com/niceirene/qwenpaw
run secure-llm-wiki https://github.com/nicobleh/secure-llm-wiki
run self-training-llm https://github.com/wj210/Self-Training-LLM
run semantic-engine https://github.com/Open-Research-Institute/semantic-engine
run semiont https://github.com/The-AI-Alliance/semiont
run sift-kg https://github.com/juanceresa/sift-kg
run siftly https://github.com/ViperrCrypto/Siftly
run sig https://github.com/sig-ai-app/sig-releases
run signetai https://github.com/signet-ai/signetai
run skilllift https://github.com/walter-mitty-pro/SkillLift
run skillnote https://github.com/luna-prompts/SkillNote
run skillrl https://github.com/aiming-lab/SkillRL
run skillweaver https://github.com/OSU-NLP-Group/SkillWeaver
run skillx https://github.com/zjunlp/SkillX
run smriti-mcp https://github.com/Deepak-Bhardwaj-PS/smriti-mcp
run sol-pi https://github.com/NVlabs/SoL-Pi
run spacebot https://github.com/spacedriveapp/spacebot
run sparks https://github.com/YogiRK/sparks
run stash https://github.com/alash3al/stash
run supermemory https://github.com/supermemoryai/supermemory
run swamp https://github.com/swamp-club/swamp
run swarmworld https://github.com/lamm-mit/SwarmWorld
run synapptic https://github.com/appcuarium/synapptic
run synthadoc https://github.com/axoviq-ai/synthadoc
run synto https://github.com/kytmanov/synto
run tardigrade https://github.com/clavia-labs/tardigrade
run tendril https://github.com/serverless-dna/tendril
run thalo https://github.com/rejot-dev/thalo
run theafh--ai-modules https://github.com/TheAFH/ai-modules
run theknowledge https://github.com/BadWally/TheKnowledge
run tolaria https://github.com/refactoringhq/tolaria
run tracecraft https://github.com/arrmlet/tracecraft
run trajectory-informed-memory-generation https://arxiv.org/html/2603.10600v1 document
run virtual-context https://github.com/virtual-context/virtual-context
run vlm-wiki https://github.com/veniVeci/VLM-wiki
run voiden https://github.com/voidenhq/voiden
run voyager https://github.com/MineDojo/Voyager
run weknora https://github.com/Tencent/WeKnora
run wikiskill https://arxiv.org/abs/2608.27454 document
run wikiskill-stahl-g https://github.com/Stahl-G/WikiSkill
run wuphf https://github.com/nex-crm/wuphf
run xmemory https://github.com/hu-xiaobai/xMemory
run zikkaron https://github.com/amanhij/zikkaron
