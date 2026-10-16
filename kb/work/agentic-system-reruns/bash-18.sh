#!/usr/bin/env bash
# Four deferred wikis, four pinned local sources, and nine other fresh starts.
# Requires the committed owner-qualified namespace migration. See batch-18.md.
# Fresh starts only; never resume preserved runs.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 1

# Fail before creating logs/worktrees while the known namespace collision persists.
# This inspects naming only; it does not prepare, acquire or open an analysis.
git diff --quiet HEAD -- src/commonplace/lib/agentic_analysis/analyses.py || {
  printf 'Batch 18 blocked: commit the namespace implementation before preparing runs.\n' >&2
  exit 1
}
uv run --no-sync python - <<'PY' || exit 1
from commonplace.lib.agentic_analysis.analyses import source_slug

for owner in ("Pratiyush", "kenhuangus", "nvk", "MehmetGoekce"):
    expected = owner.lower() + "--llm-wiki"
    actual = source_slug(f"https://github.com/{owner}/llm-wiki", "llm-wiki")
    if actual != expected:
        raise SystemExit(
            "Batch 18 blocked: the committed owner-qualified publication namespace "
            f"migration is required (expected {expected}, got {actual}). "
            "Do not bypass this check or replace cobusgreyling's publication."
        )
PY

output_disk="/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372"
output_dir="$output_disk/outputs/batch-18"
worktree_dir="$output_disk/outputs/commonplace-worktrees"
mountpoint -q "$output_disk" || { printf 'Output disk is not mounted: %s\n' "$output_disk" >&2; exit 1; }
mkdir -p "$output_dir" "$worktree_dir" || exit 1
[[ -w "$output_dir" && -w "$worktree_dir" ]] || { printf 'External output/worktree directories are not writable.\n' >&2; exit 1; }

run() {
  local system=$1 source=$2 revision=${3-} local_source=${4-}
  mountpoint -q "$output_disk" || { printf 'Output disk is not mounted: %s\n' "$output_disk" >&2; exit 1; }
  local output="$output_dir/$system.output"
  local worktree="$worktree_dir/batch-18-$system"
  local prompt
  printf -v prompt '/analyse-agentic-system %s\n\nOperator preparation instruction: from the origin checkout, use commonplace-analysis prepare --name %s --worktree %s for isolated run setup. Continue this session in the returned worktree with its returned command prefix. Do not use the default primary-disk worktree location, launch a replacement harness, or resume an old run. Stop if external storage or this new destination is unavailable. Preserve the exact repository owner and source identity; do not substitute a similarly named repository or replace another source publication.' "$source" "$system" "$worktree"
  if [[ -e "$output" || -L "$output" ]]; then
    printf 'Skip %s: output already exists; review it before scheduling again.\n' "$system"
    return
  fi
  if [[ -e "$worktree" || -L "$worktree" || -e "$worktree.preparation.json" || -L "$worktree.preparation.json" ]]; then
    printf 'Skip %s: external worktree/preparation already exists; preserve and review it.\n' "$system"
    return
  fi
  if [[ -n "$revision" ]]; then
    if [[ ! -d "$local_source" ]] || ! git -C "$local_source" cat-file -e "$revision^{commit}"; then
      printf 'Stop %s: pinned local source is unavailable; preserve evidence, do not substitute upstream.\n' "$system" >&2
      exit 1
    fi
    local source_name=${source#https://github.com/}
    local source_destination="$worktree/related-systems/${source_name/\//--}"
    local source_setup
    printf -v source_setup '\n\nOperator-authorized historical source setup: the original upstream is unavailable. Analyse exactly commit %s, not a current upstream tip. After isolated preparation and before opening the new run, seed its source checkout from the supplied local Git repository. This is planned source preparation, not repair of an acquisition failure. The existing repository is read-only input; never fetch, checkout, change its origin, or modify it. Require the new source destination to be absent; stop otherwise. Run these commands in order, stopping on any failure:\n\nmkdir -p %q\ngit clone --no-hardlinks --no-checkout -- %q %q\ngit -C %q remote set-url origin %q\ngit -C %q checkout --detach %q\n\nOpen the new run with the original source identity %s and source input %s, and explicitly pass --source-revision %s. Normal acquisition can verify the already-present pinned commit without fetching. Record the historical revision and local-copy acquisition limit in the boundary; do not claim a current-upstream analysis. Use no old analysis outputs or historical findings. Do not fetch a different revision, use a public fork as a new identity, or repair the source after an acquisition stop.' "$revision" "$worktree/related-systems" "$local_source" "$source_destination" "$source_destination" "$source" "$source_destination" "$revision" "$source" "$source" "$revision"
    prompt+="$source_setup"
  fi
  printf 'Start %s -> %s; worktree %s\n' "$system" "$output" "$worktree"
  (set -C; pi --approve --model openai/gpt-6.1-sol --thinking medium \
    --tools read,bash,edit,write,subagent --mode json \
    "$prompt" >"$output" 2>&1)
  printf 'Finished %s: process exit %s (not an analysis verdict).\n' "$system" "$?"
}

run pratiyush--llm-wiki https://github.com/Pratiyush/llm-wiki
run kenhuangus--llm-wiki https://github.com/kenhuangus/llm-wiki
run nvk--llm-wiki https://github.com/nvk/llm-wiki
run mehmetgoekce--llm-wiki https://github.com/MehmetGoekce/llm-wiki
run clawvault https://github.com/Versatly/clawvault bd702e9cce436bc3065827714cd576e8be20c375 "$PWD/related-systems/clawvault"
run cortex https://github.com/abbacusgroup/cortex a51c2209eb6d26812c19c97aaade3cb64ccfc23c "$PWD/related-systems/abbacusgroup--cortex"
run pal https://github.com/agno-agi/pal 6516b8ede0c085e48f39f3bd04cb85b475a855dc "$PWD/related-systems/agno-agi--pal"
run semantic-engine https://github.com/Open-Research-Institute/semantic-engine 7e2481671cad01f0b4c89f2a1877d6733d7e552c "$PWD/related-systems/Open-Research-Institute--semantic-engine"
run memori https://github.com/MemoriLabs/Memori
run openclerk https://github.com/yazanabuashour/openclerk
run beads-rust https://github.com/Dicklesworthstone/beads_rust
run agent-s https://github.com/simular-ai/Agent-S
run memoryos https://github.com/BAI-LAB/MemoryOS
run basic-memory https://github.com/basicmachines-co/basic-memory
run os-copilot https://github.com/OS-Copilot/OS-Copilot
run a-mem https://github.com/WujiangXu/A-mem-sys
run hipporag https://github.com/OSU-NLP-Group/HippoRAG
