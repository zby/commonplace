#!/usr/bin/env bash
# Operator-run, one-shot recovery of six existing runs. Not a fresh-run batch.
# --check is read-only. --confirm-idle confirms no prior same-run writer is live.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/../../.."
root=$PWD
mode=${1:---check}
if [[ $# -gt 1 || ( "$mode" != --check && "$mode" != --confirm-idle ) ]]; then
  printf 'Usage: bash %s [--check | --confirm-idle]\n' "$0" >&2
  exit 2
fi
export PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0
output_disk=/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372
output_dir="$output_disk/outputs/batch-19"
for executable in uv pi mountpoint flock; do command -v "$executable" >/dev/null; done
mountpoint -q "$output_disk" || { printf 'Output disk is not mounted.\n' >&2; exit 1; }

# Batch glue only: use the current reset_run(run, job) API externally, then the
# unchanged prepared commands and driver. No new engine resume command/loop.
batch19() {
  uv run --no-sync python3 - "$root" "$@" <<'PY'
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

import commonplace
import yaml
from commonplace.artifactrun.reset import affected_jobs, reset_run
from commonplace.artifactrun.run import Run
from commonplace.artifactrun.store import RunStore
from commonplace.artifactrun.worktree import preparation_for, require_clean_worktree
from commonplace.lib.agentic_analysis.guards import OUTPUT_LOCATIONS
from commonplace.lib.source_identity import normalize_source_identity

root, action = Path(sys.argv[1]), sys.argv[2]
base = root / 'kb/work/agentic-system-reruns'
intake_path = base / 'publication-audit-current-intake.json'
# Keep reset code fixed even if unrelated workshop bookkeeping advances main.
reset_code_commit = 'ce0715a086a9957d2fca20b3fdc5ac05b938792a'
expected = [
    ('AAS-2026-10-15-supermemory-ae21530d128d-01', 'runtime'),
    ('AAS-2026-10-13-contextpilot-30d0d09e6cdc-01', 'boundary'),
    ('AAS-2026-10-14-openrsi-c72dec9967a3-01', 'runtime'),
    ('AAS-2026-10-14-modularrsi-96b89989168e-01', 'runtime'),
    ('AAS-2026-10-15-jaz-a94bea79c61a-01', 'runtime'),
    ('AAS-2026-10-15-autogenesis-9bcfa57fd7c1-01', 'boundary'),
]

def require(condition, message):
    if not condition:
        raise SystemExit(message)

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def git(*args, cwd=root):
    result = subprocess.run(['git', '--no-optional-locks', *args], cwd=cwd,
                            text=True, capture_output=True)
    require(result.returncode == 0, result.stderr or str(args))
    return result.stdout.strip()

def file_map(directory):
    directory = Path(directory)
    require(directory.is_dir() and directory.resolve() == directory,
            f'Absent or redirected directory: {directory}')
    paths = list(directory.rglob('*'))
    require(not any(p.is_symlink() for p in paths), f'Symlink in {directory}')
    return {p.relative_to(directory).as_posix(): sha(p) for p in paths if p.is_file()}

require(Path(commonplace.__file__).resolve().parents[2] == root,
        'Current reset API is not bound to the origin checkout')
require(not git('diff', '--name-only', reset_code_commit, '--',
                'src/commonplace', 'pyproject.toml', 'uv.lock'),
        'Reset implementation/dependencies changed; require a new reviewed launcher')
require(not git('ls-files', '--others', '--exclude-standard', '--', 'src/commonplace'),
        'Untracked package code; require review before reset')
require(sha(intake_path) == '29c5a94a2c926f9c8b895cf5a5f50b0157461fa2a8aff39779131d14ab6d530e',
        'Fixed intake bytes changed')
selected = json.loads((base / 'batch-19.json').read_text())['selected']
require([(r['run-id'], r['from-job']) for r in selected] == expected,
        'Batch selection changed; do not silently expand or reorder this launcher')
rows = {r['run-id']: r for r in json.loads(intake_path.read_text())['publications']}

def preflight(index):
    run_id, job = expected[index]
    row = rows[run_id]
    worktree = Path(row['worktree'])
    prefix = Path(row['command-prefix'])
    run_dir = Path(row['run-definition']['path']).parent
    for key in ('preparation', 'run-definition', 'publication-effect'):
        require(sha(row[key]['path']) == row[key]['sha256'], f'{run_id}: changed {key}')
    prep = preparation_for(worktree)
    require(Path(prep['origin']).resolve() == root, f'{run_id}: foreign origin')
    require(prep['commit'] == git('rev-parse', 'HEAD', cwd=worktree) == row['method-revision'],
            f'{run_id}: frozen method changed')
    require_clean_worktree(worktree, OUTPUT_LOCATIONS)
    for name in ('commonplace-run', 'commonplace-analysis'):
        require(os.access(prefix / name, os.X_OK), f'{run_id}: unavailable {name}')
    driver = worktree / 'kb/agentic-system-analyses/instructions/analyse-agentic-system/drive-a-code-scheduled-run.md'
    require(driver.is_file(), f'{run_id}: missing frozen driver')
    require(not (run_dir / '.reset-pending.json').exists(),
            f'{run_id}: pending reset needs explicit reconciliation, not a batch rerun')
    run = Run(RunStore(run_dir))
    require(not any(a['state'] == 'open' for a in run.attempts.values()), f'{run_id}: open attempts')
    latest = {}
    for attempt in sorted(run.attempts.values(), key=lambda a: a['seq']):
        latest[attempt['job']] = attempt
    require(not any(a.get('uncertain') for a in latest.values()), f'{run_id}: uncertain effects')
    for journal in (run_dir / 'effects').glob('*.json'):
        require(json.loads(journal.read_text())['state'] == 'completed', f'{run_id}: incomplete {journal}')
    opening = run.latest_completed('opening')
    require(opening is not None, f'{run_id}: no completed opening')
    metadata = json.loads(run.store.get(opening['outputs']['metadata']))
    require(metadata['inputs-commit'] == row['method-revision'] and metadata['run-id'] == run_id,
            f'{run_id}: opening identity changed')
    require(metadata['expected-incumbent-sha256'] == 'absent', f'{run_id}: opening incumbent needs disposition')
    require(metadata['worker'] == {'profile': 'pi-sol', 'harness': 'pi',
                                  'launch-model': 'gpt-6.1-sol', 'effort': 'medium'},
            f'{run_id}: unexpected frozen worker profile')
    source = row['source']
    require(source['kind'] == 'git', f'{run_id}: unexpected source kind')
    require(git('rev-parse', 'HEAD', cwd=source['path']) == source['revision'], f'{run_id}: source revision changed')
    require(not git('status', '--porcelain', '--untracked-files=all', cwd=source['path']), f'{run_id}: dirty source')
    identity = normalize_source_identity(source['identity'])
    require(normalize_source_identity(git('remote', 'get-url', 'origin', cwd=source['path'])) == identity,
            f'{run_id}: foreign source origin')
    for overview in (root / 'kb/agentic-system-analyses/retained').glob('*/overview.md'):
        boundary = overview.parent / 'boundary.md'
        front = yaml.safe_load(boundary.read_text().split('---', 2)[1])
        require(normalize_source_identity(front['source']['identity']) != identity,
                f'{run_id}: canonical incumbent appeared; no replacement authority')
    effect = json.loads(Path(row['publication-effect']['path']).read_text())
    require(effect['state'] == 'completed' and effect['run-id'] == run_id,
            f'{run_id}: publication effect identity changed')
    require(file_map(row['publication']) == row['published-sha256'] == effect['new'],
            f'{run_id}: publication map changed')
    jobs = affected_jobs(run, job)
    require(not jobs & {'opening', 'acquire'}, f'{run_id}: would discard frozen acquisition')
    require(sum(a['job'] in jobs for a in run.attempts.values()) == selected[index]['current-attempts-in-reset-closure'],
            f'{run_id}: reset closure changed; require renewed depth review')
    return {'run-id': run_id, 'from-job': job, 'worktree': str(worktree),
            'command-prefix': str(prefix), 'run': str(run_dir), 'driver': str(driver),
            'method': row['method-revision'], 'source': source, 'reset-jobs': sorted(jobs)}

if action == 'check':
    print(json.dumps([preflight(index) for index in range(len(expected))], indent=2))
elif action == 'paths':
    index = int(sys.argv[3])
    row = rows[expected[index][0]]
    values = [expected[index][0], row['worktree'], row['command-prefix'],
              str(Path(row['run-definition']['path']).parent)]
    require(not any('\n' in v or '\t' in v for v in values), 'Unsafe shell field')
    print('\t'.join(values))
elif action == 'reset':
    checked = preflight(int(sys.argv[3]))
    # The only recovery inputs: existing run and selected job. No findings.
    print(json.dumps(reset_run(Path(checked['run']), checked['from-job']), indent=2))
elif action == 'verify':
    index = int(sys.argv[3])
    report = json.loads(Path(sys.argv[4]).read_text())
    require(report['state'] == 'completed' and report.get('completion') == 'publication-job-completed',
            f'{expected[index][0]}: coordinator did not complete a publication; preserve logs and stop')
    row = rows[expected[index][0]]
    run_dir = Path(row['run-definition']['path']).parent
    run = Run(RunStore(run_dir))
    require(not (run_dir / '.reset-pending.json').exists() and
            not any(a['state'] == 'open' for a in run.attempts.values()), 'Run is not idle after coordinator return')
    effect = json.loads((run_dir / 'effects/publish.json').read_text())
    require(effect['state'] == 'completed' and effect['run-id'] == expected[index][0] and
            file_map(row['publication']) == effect['new'], 'Renewed publication/effect mismatch')
    print('Internal publication complete; still held for independent comparison, not cleared for integration.')
else:
    raise SystemExit('Unknown batch action')
PY
}

if [[ "$mode" == --check ]]; then
  batch19 check
  exit
fi
# A fresh directory is the one-shot fence, including after interruption. Never
# overwrite logs or automatically repeat a reset / restart a failed coordinator.
mkdir "$output_dir"
exec 9>"$output_dir/batch.lock"
flock -n 9
printf '%s\n' "$BASHPID" >"$output_dir/batch.pid"
batch19 check >"$output_dir/preflight.json" 2>"$output_dir/preflight.stderr"
for index in 0 1 2 3 4 5; do
  mountpoint -q "$output_disk"
  fields=$(batch19 paths "$index")
  IFS=$'\t' read -r run_id worktree prefix run_dir <<<"$fields"
  printf 'Reset and start %s; logs: %s\n' "$run_id" "$output_dir"
  batch19 reset "$index" >"$output_dir/$run_id.reset.json" 2>"$output_dir/$run_id.reset.stderr"
  printf -v prompt 'Existing run: `%s`.\nPrepared command directory: `%s`.\nRead the complete `kb/agentic-system-analyses/instructions/analyse-agentic-system/drive-a-code-scheduled-run.md` and follow it for this run.' "$run_dir" "$prefix"
  if (cd "$worktree"; set -C; exec pi --approve --model openai/gpt-6.1-sol --thinking medium \
      --tools read,bash,edit,write,subagent --mode json "$prompt" >"$output_dir/$run_id.output" 2>&1); then
    printf '0\n' >"$output_dir/$run_id.exit"
  else
    code=$?
    printf '%s\n' "$code" >"$output_dir/$run_id.exit"
    printf 'Coordinator exit %s; stop and preserve %s. No automatic retry.\n' "$code" "$run_id" >&2
    exit "$code"
  fi
  (cd "$worktree"; "$prefix/commonplace-analysis" inspect "$run_dir") \
    >"$output_dir/$run_id.inspect.json" 2>"$output_dir/$run_id.inspect.stderr"
  batch19 verify "$index" "$output_dir/$run_id.inspect.json"
done
printf 'Batch 19 finished internally. All six results remain held for independent audit; no integration performed.\n'
