#!/usr/bin/env bash
# Nine ordinary fresh analyses. No reset, old-run resume or integration.
# Run only after batch 18 and other same-target coordinators have stopped.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0

# Opening validates the entire inherited corpus. Check what preparation will
# inherit, not only whether the new target's publication name is well formed.
method_revision=$(git rev-parse --verify HEAD) || exit 1
git diff --quiet "$method_revision" -- src/commonplace kb/agentic-system-analyses/retained || {
  printf 'Batch 20 blocked: commit code/canonical publication changes first.\n' >&2
  exit 1
}
untracked=$(git ls-files --others --exclude-standard -- kb/agentic-system-analyses/retained) || exit 1
[[ -z "$untracked" ]] || {
  printf 'Batch 20 blocked: reconcile untracked canonical publications first.\n' >&2
  exit 1
}
canonical_sources=$(uv run --no-sync python3 - <<'PY'
from pathlib import Path
from commonplace.lib.agentic_analysis.analyses import current_analyses
from commonplace.lib.source_identity import normalize_source_identity

for analysis in current_analyses(Path.cwd()):
    print(normalize_source_identity(analysis.memory.frontmatter['source-identity']))
PY
) || exit 1
# Refuse an origin change during validation. Every preparation below uses this
# same validated commit, even if unrelated integrations advance main later.
git diff --quiet "$method_revision" -- src/commonplace kb/agentic-system-analyses/retained || {
  printf 'Batch 20 blocked: origin changed during namespace validation.\n' >&2
  exit 1
}
printf 'Batch 20 method and inherited corpus: %s\n' "$method_revision"

output_disk="/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372"
output_dir="$output_disk/outputs/batch-20"
worktree_dir="$output_disk/outputs/commonplace-worktrees"
mountpoint -q "$output_disk" || { printf 'Output disk is not mounted: %s\n' "$output_disk" >&2; exit 1; }
mkdir -p "$output_dir" "$worktree_dir" || exit 1
[[ -w "$output_dir" && -w "$worktree_dir" ]] || { printf 'External output/worktree directories are not writable.\n' >&2; exit 1; }

run() {
  local system=$1 source=$2 revision=${3-} local_source=${4-}
  mountpoint -q "$output_disk" || { printf 'Output disk is not mounted: %s\n' "$output_disk" >&2; exit 1; }
  local output="$output_dir/$system.output"
  local worktree="$worktree_dir/batch-20-$system"
  local prompt
  if grep -Fxiq -- "$source" <<<"$canonical_sources"; then
    printf 'Skip %s: source already has a current origin publication; reconcile before scheduling again.\n' "$system"
    return
  fi
  if [[ -e "$output" || -L "$output" ]]; then
    printf 'Skip %s: output already exists; preserve and review it.\n' "$system"
    return
  fi
  if [[ -e "$worktree" || -L "$worktree" || -e "$worktree.preparation.json" || -L "$worktree.preparation.json" ]]; then
    printf 'Skip %s: worktree/preparation already exists; preserve and review it.\n' "$system"
    return
  fi
  printf -v prompt '/analyse-agentic-system %s\n\nOperator preparation instruction: from the origin checkout, use commonplace-analysis prepare --name %s --worktree %s --revision %s for isolated run setup. This batch explicitly selects that validated committed revision; do not replace it with a later HEAD. Continue this session in the returned worktree with its returned command prefix. Do not use the default primary-disk worktree location, launch a replacement harness, reset or resume an old run. Stop on any preparation/acquisition failure. Preserve the exact repository owner and source identity; do not substitute similarly named repositories or replace another source publication. The required writable locations are %s and %s; the mount root itself need not be writable. Check the actual destination parent, not write permission on the mount root.' "$source" "$system" "$worktree" "$method_revision" "$output_dir" "$worktree_dir"
  if [[ -n "$revision" ]]; then
    if [[ ! -d "$local_source" ]] || ! git -C "$local_source" cat-file -e "$revision^{commit}"; then
      printf 'Stop %s: pinned local source is unavailable; do not substitute upstream.\n' "$system" >&2
      exit 1
    fi
    local source_name=${source#https://github.com/}
    local source_destination="$worktree/related-systems/${source_name/\//--}"
    local source_setup
    printf -v source_setup '\n\nOperator-authorized historical source setup: analyse exactly commit %s, not a current upstream tip. After isolated preparation and before opening the new run, seed its source checkout from the supplied local Git repository. This is planned source preparation, not repair of an acquisition failure. The existing repository is read-only input; never fetch, checkout, change its origin or modify it. Require the new source destination to be absent; stop otherwise. Run these commands in order, stopping on any failure:\n\nmkdir -p %q\ngit clone --no-hardlinks --no-checkout -- %q %q\ngit -C %q remote set-url origin %q\ngit -C %q checkout --detach %q\n\nOpen the new run with the original source identity %s and source input %s, explicitly passing --source-revision %s. Normal acquisition can verify the already-present pinned commit without fetching. Record the historical revision and local-copy acquisition limit in the boundary; do not claim a current-upstream analysis. Use no old analysis outputs or historical findings. Do not fetch another revision, use a public fork as a new identity, or repair the source after an acquisition stop.' "$revision" "$worktree/related-systems" "$local_source" "$source_destination" "$source_destination" "$source" "$source_destination" "$revision" "$source" "$source" "$revision"
    prompt+="$source_setup"
  fi
  printf 'Start %s -> %s; worktree %s\n' "$system" "$output" "$worktree"
  local code=0
  (set -C; pi --approve --model openai/gpt-6.1-sol --thinking medium \
    --tools read,bash,edit,write,subagent --mode json \
    "$prompt" >"$output" 2>&1) || code=$?
  (set -C; printf '%s\n' "$code" >"$output_dir/$system.exit") || exit 1
  printf 'Finished %s: process exit %s (not an analysis verdict).\n' "$system" "$code"
  # As in ordinary fresh-start batches, preserve a failed coordinator and move
  # to the next independent target. Never retry that coordinator or old run.
}

run academic-research-skills https://github.com/Imbad0202/academic-research-skills
run kenhuangus--llm-wiki https://github.com/kenhuangus/llm-wiki
run nvk--llm-wiki https://github.com/nvk/llm-wiki
run mehmetgoekce--llm-wiki https://github.com/MehmetGoekce/llm-wiki
run clawvault https://github.com/Versatly/clawvault bd702e9cce436bc3065827714cd576e8be20c375 "$PWD/related-systems/clawvault"
run cortex https://github.com/abbacusgroup/cortex a51c2209eb6d26812c19c97aaade3cb64ccfc23c "$PWD/related-systems/abbacusgroup--cortex"
run pal https://github.com/agno-agi/pal 6516b8ede0c085e48f39f3bd04cb85b475a855dc "$PWD/related-systems/agno-agi--pal"
run semantic-engine https://github.com/Open-Research-Institute/semantic-engine 7e2481671cad01f0b4c89f2a1877d6733d7e552c "$PWD/related-systems/Open-Research-Institute--semantic-engine"
run memori https://github.com/MemoriLabs/Memori
