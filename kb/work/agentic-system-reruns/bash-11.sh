#!/usr/bin/env bash
# Clean residue: 20 untouched targets, sequential; no retries of batches 01–08.
# Selection boundary and exclusions: residue-09.md. This script does not launch itself.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 1
output_disk="/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372"
output_dir="$output_disk/outputs"
mountpoint -q "$output_disk" || { printf 'Output disk is not mounted: %s\n' "$output_disk" >&2; exit 1; }
mkdir -p "$output_dir" || exit 1
[[ -w "$output_dir" ]] || { printf 'Output directory is not writable: %s\n' "$output_dir" >&2; exit 1; }

run() {
  local system=$1 source=$2 source_kind=${3:-repository}
  mountpoint -q "$output_disk" || { printf 'Output disk is not mounted: %s\n' "$output_disk" >&2; exit 1; }
  local output="$output_dir/$system.output"
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
