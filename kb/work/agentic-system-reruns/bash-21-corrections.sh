#!/usr/bin/env bash
# Prepared feedback-assisted recovery. Default is READ ONLY; never launch implicitly.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/../../.."
root=$PWD
export PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0
mode=${1:---check}
if [[ $# -gt 1 || ( "$mode" != --check && "$mode" != --confirm-idle ) ]]; then
  printf 'Usage: bash %s [--check | --confirm-idle]\nPreparation is not launch authority. --confirm-idle is for a separately authorized operator launch.\n' "$0" >&2
  exit 2
fi
output_disk=/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372
output_dir="$output_disk/outputs/batch-21-corrections"

batch21() {
  uv run --no-sync python3 - "$root" "$@" <<'PY'
import hashlib
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys

import commonplace
from commonplace.artifactrun.plan import ModelJob
from commonplace.artifactrun.reset import affected_jobs, reset_run
from commonplace.artifactrun.run import Run
from commonplace.artifactrun.store import RunStore
from commonplace.artifactrun.worktree import require_clean_worktree
from commonplace.lib.agentic_analysis.guards import OUTPUT_LOCATIONS
from commonplace.lib.source_identity import normalize_source_identity

root, action = Path(sys.argv[1]), sys.argv[2]
base = root / 'kb/work/agentic-system-reruns'
plan_path = base / 'batch-21-corrections/plan.json'
plan = json.loads(plan_path.read_text())
rows = plan['rows']


def need(condition, message):
    if not condition:
        raise SystemExit(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def maps(path):
    path = Path(path)
    need(path.is_dir() and path.resolve() == path, f'Absent/redirected directory: {path}')
    children = list(path.rglob('*'))
    need(not any(p.is_symlink() for p in children), f'Symlink: {path}')
    return {p.relative_to(path).as_posix(): sha(p) for p in children if p.is_file()}


def mdig(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def bound(record):
    need(sha(record['path']) == record['sha256'], f"Changed input: {record['path']}")


def git(*args, cwd=root):
    r = subprocess.run(['git', '--no-optional-locks', *args], cwd=cwd, capture_output=True, text=True)
    need(r.returncode == 0, r.stderr or str(args))
    return r.stdout.strip()


need(Path(commonplace.__file__).resolve().parents[2] == root, 'External reset must load origin package')
need(Path(importlib.import_module('commonplace.lib.agentic_analysis.publication').__file__).resolve()
     == root / 'src/commonplace/lib/agentic_analysis/publication.py', 'Foreign publication hook')
need(not git('diff', '--name-only', plan['reset-code-commit'], '--', 'src/commonplace', 'pyproject.toml', 'uv.lock'), 'Reset code/dependencies changed')
need(not git('ls-files', '--others', '--exclude-standard', '--', 'src/commonplace'), 'Untracked package code')
need(len(rows) == 9 and len({r['case']['run-id'] for r in rows}) == 9, 'Expected nine exact cases')
for record in plan['runtime-files'] + [plan['base-inventory'], plan['integration-proof'], plan['launcher']]:
    bound(record)
originals = {c['key']: c for c in json.loads(Path(plan['base-inventory']['path']).read_text())['rows'] if c['gate'] == 'repair'}
need({e['case']['key'] for e in rows} == set(originals), 'Repair inventory changed')
for entry in rows:
    c = entry['case']
    need(c == originals[c['key']], 'Case bindings differ from original batch inventory')
    expected_reset = 'synthesis-verification' if c['key'] == 'arex-skill' else c['verification-barriers'][0]
    expected_roles = ['synthesis'] if c['key'] == 'arex-skill' else c['candidate-author-jobs'] + (['workflow'] if c['key'] == 'modularrsi' else [])
    need(entry['reset-job'] == expected_reset and [f['role'] for f in entry['feedback']] == expected_roles, 'Unsupported correction route')


def global_guards():
    retained = root / 'kb/agentic-system-analyses/retained'
    canonical = {p.name: maps(p) for p in retained.iterdir() if p.is_dir()}
    need(mdig(canonical) == plan['canonical-map-digest'] and len(canonical) == 182, 'Canonical baseline changed')
    need({p.name: sha(p) for p in retained.iterdir() if p.is_file()} == plan['retained-root-files'], 'Retained-root files changed')
    for old in plan['protected-publications']:
        need(maps(old['directory']) == old['members'], f"Unselected held publication changed: {old['directory']}")


def preflight(index):
    entry = rows[index]
    case = entry['case']
    run_dir, worktree = Path(case['run']), Path(case['worktree'])
    for record in [case['preparation'], case['run-definition'], *case['evidence'], *entry['native-files']]:
        bound(record)
    for feedback in entry['feedback']:
        bound(feedback['payload'])
    need(git('rev-parse', 'HEAD', cwd=worktree) == case['method-revision'], 'Frozen method changed')
    require_clean_worktree(worktree, OUTPUT_LOCATIONS)
    need(not (run_dir / '.reset-pending.json').exists(), 'Pending reset requires separate reconciliation')
    need(maps(run_dir / 'state/attempts') == case['attempts-map'], 'Attempt snapshot changed')
    need(maps(run_dir / 'state/judgments') == entry['judgments-map'], 'Judgment snapshot changed')
    need(mdig(maps(run_dir / 'state/versions')) == entry['versions-map-digest'], 'Version store changed')
    bound(entry['sequence'])
    budget = run_dir / 'state/attempt-budget.json'
    if entry['budget'] is None:
        need(not budget.exists(), 'Unexpected budget record')
    else:
        bound(entry['budget'])
    run = Run(RunStore(run_dir))
    need(not any(a['state'] == 'open' for a in run.attempts.values()), 'Open attempt; not idle')
    latest = {}
    for attempt in sorted(run.attempts.values(), key=lambda a: a['seq']):
        latest[attempt['job']] = attempt
    need(not any(a.get('uncertain') for a in latest.values()), 'Uncertain effect')
    need(not any(j['job'] == 'operator' for j in run.judgments), 'Existing operator decisions need reconciliation')
    for journal in (run_dir / 'effects').glob('*.json'):
        need(json.loads(journal.read_text())['state'] == 'completed', f'Incomplete journal: {journal}')
    need(sorted(affected_jobs(run, entry['reset-job'])) == entry['reset-jobs'], 'Reset closure changed')
    opening = run.latest_completed('opening')
    acquire = run.latest_completed('acquire')
    need(opening['outputs']['metadata'] == entry['opening-version'] and acquire['outputs']['source'] == entry['source-version'], 'Opening/acquisition changed')
    metadata = json.loads(run.store.get(entry['opening-version']))
    need(metadata['expected-incumbent-sha256'] == 'absent' and metadata['inputs-commit'] == case['method-revision'], 'Incumbent/method stop')
    need(metadata['worker'] == {'profile': 'pi-sol', 'harness': 'pi', 'launch-model': 'gpt-6.1-sol', 'effort': 'medium'}, 'Frozen worker profile changed')
    source = entry['source']
    need(git('rev-parse', 'HEAD', cwd=source['path']) == source['revision'], 'Source revision changed')
    need(not git('status', '--porcelain', '--untracked-files=all', cwd=source['path']), 'Dirty source')
    need(normalize_source_identity(git('remote', 'get-url', 'origin', cwd=source['path'])) == normalize_source_identity(case['source-identity']), 'Foreign source origin')
    publication = case['own-publication']
    bound(publication['effect'])
    bound(publication['manifest'])
    effect = json.loads(Path(publication['effect']['path']).read_text())
    need(effect['state'] == 'completed' and effect['run-id'] == case['run-id'] and effect['old'] is None, 'Publication identity/incumbent changed')
    need(maps(publication['directory']) == publication['members'] == effect['new'], 'Own publication changed')
    for feedback in entry['feedback']:
        role, version = feedback['role'], feedback['version']
        filler = run.jobs.filler(role)
        need(isinstance(filler, ModelJob) and run.members().get(role) == version == run.latest_output(filler), 'Feedback witness changed')
        need(sha(run.store.versions / version) == version, 'Corrupt feedback witness')
        if not entry['consumes-budget-floor']:
            used = sum(a['job'] == filler.name for a in run.attempts.values())
            need(filler.max_attempts is None or used < filler.max_attempts, f'No old-method headroom for {role}')
    if not entry['consumes-budget-floor']:
        for job in run.jobs.jobs:
            if isinstance(job, ModelJob) and job.name not in entry['reset-jobs']:
                used = sum(a['job'] == job.name for a in run.attempts.values())
                need(job.max_attempts is None or used < job.max_attempts, f'No retained dependency headroom: {job.name}')
    for name in ('commonplace-run', 'commonplace-analysis'):
        need(os.access(Path(case['command-prefix']) / name, os.X_OK), f'Unavailable {name}')
    global_guards()
    return entry


if action == 'check':
    for i in range(9):
        e = preflight(i)
        print(e['case']['key'], 'reset', e['reset-job'], 'then refused roles', ', '.join(f['role'] for f in e['feedback']))
    print('PREPARATION CHECK ONLY: nine bindings; no native reset/judge/advance or model launch. Old retained attempt budgets remain limits.')
elif action == 'paths':
    c = rows[int(sys.argv[3])]['case']
    values = [c['run-id'], c['worktree'], c['command-prefix'], c['run']]
    need(not any('\n' in v or '\t' in v for v in values), 'Unsafe shell field')
    print('\t'.join(values))
elif action == 'release-check':
    need(git('branch', '--show-current') == 'main' and not git('status', '--porcelain'), 'Commit complete preparation; origin must be clean main')
    for p in [plan_path, Path(plan['launcher']['path']), *[Path(f['payload']['path']) for e in rows for f in e['feedback']]]:
        relative = p.relative_to(root)
        need(sha(p) == hashlib.sha256(subprocess.check_output(['git', 'show', f'HEAD:{relative}'], cwd=root)).hexdigest(), f'Uncommitted launch input: {relative}')
    # Bounded process evidence supplements, never replaces, --confirm-idle.
    processes = subprocess.check_output(['ps', '-eo', 'pid=,ppid=,args='], text=True)
    matches = [line for line in processes.splitlines() if any(e['case']['run-id'] in line or e['case']['worktree'] in line for e in rows)]
    need(not matches, 'Possible same-run process; reconcile before launch:\n' + '\n'.join(matches))
elif action == 'reset-feedback':
    entry = preflight(int(sys.argv[3]))
    c = entry['case']
    out = Path(sys.argv[4])
    events = {'run-id': c['run-id'], 'state': 'before-reset', 'commands': []}
    destination = out / (c['run-id'] + '.events.json')
    need(not destination.exists(), 'Existing case events require reconciliation')
    def save():
        temp = destination.with_suffix('.tmp')
        temp.write_text(json.dumps(events, indent=2) + '\n')
        temp.replace(destination)
    save()
    try:
        report = reset_run(Path(c['run']), entry['reset-job'])
        events.update(state='reset-completed', reset=report)
        save()
        need(report['state'] == 'completed' and report['jobs'] == entry['reset-jobs'], 'Reset result mismatch')
        archive = Path(report['archive'])
        old = c['own-publication']
        positions = [i for i, p in enumerate(report['effects']) if Path(p) == Path(old['directory'])]
        need(len(positions) == 1 and maps(archive / 'effects' / str(positions[0]) / 'before') == old['members'], 'Predecessor publication archive mismatch')
        need(not Path(old['directory']).exists() and not (Path(c['run']) / '.reset-pending.json').exists(), 'Publication/reset not withdrawn')
        after = Run(RunStore(Path(c['run'])))
        need(all(after.members().get(k) == v for k, v in entry['preserved-members'].items()), 'Upstream member loss')
        need(after.latest_completed('opening')['outputs']['metadata'] == entry['opening-version'] and after.latest_completed('acquire')['outputs']['source'] == entry['source-version'], 'Frozen upstream identity changed')
        for feedback in entry['feedback']:
            bound(feedback['payload'])
            role, version = feedback['role'], feedback['version']
            current = Run(RunStore(Path(c['run'])))
            need(current.members().get(role) == version == current.latest_output(current.jobs.filler(role)), 'Feedback target not preserved')
            text = Path(feedback['payload']['path']).read_text()
            argv = [str(Path(c['command-prefix']) / 'commonplace-run'), 'judge', c['run'], '--role', role, '--version', version, '--outcome', 'refused', '--findings', text]
            result = subprocess.run(argv, cwd=c['worktree'], text=True, capture_output=True)
            events['commands'].append({'argv': argv, 'cwd': c['worktree'], 'exit': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr})
            save()
            need(result.returncode == 0, f'Native judge failed: {result.stderr}')
            current = Run(RunStore(Path(c['run'])))
            refusal = current.refusal_in_force(current.jobs.filler(role))
            need(refusal is not None and refusal['subject']['version'] == version and refusal['findings'] == text and refusal['id'] == result.stdout.strip(), 'Feedback not in force')
        current = Run(RunStore(Path(c['run'])))
        for feedback in entry['feedback']:
            job = current.jobs.filler(feedback['role'])
            need(current.refusal_in_force(job) is not None and current.ready(job, current.permitted()), 'Feedback producer not ready')
        global_guards()
        events['state'] = 'feedback-ready-not-yet-advanced'
        save()
    except BaseException as error:
        events.update(state='stopped-preserve-evidence', error=repr(error))
        save()
        raise
elif action == 'verify':
    entry = rows[int(sys.argv[3])]
    c = entry['case']
    for record in [c['preparation'], c['run-definition'], *entry['native-files']]:
        bound(record)
    for feedback in entry['feedback']:
        bound(feedback['payload'])
    need(git('rev-parse', 'HEAD', cwd=c['worktree']) == c['method-revision'], 'Method changed during correction')
    require_clean_worktree(Path(c['worktree']), OUTPUT_LOCATIONS)
    need(git('rev-parse', 'HEAD', cwd=entry['source']['path']) == entry['source']['revision'] and not git('status', '--porcelain', '--untracked-files=all', cwd=entry['source']['path']), 'Source changed during correction')
    report = json.loads(Path(sys.argv[4]).read_text())
    need(report['state'] == 'completed' and report.get('completion') == 'publication-job-completed', 'Coordinator did not complete current publication')
    run_dir = Path(c['run'])
    need(not (run_dir / '.reset-pending.json').exists(), 'Pending reset after coordinator')
    run = Run(RunStore(run_dir))
    need(not any(a['state'] == 'open' for a in run.attempts.values()), 'Open attempt after coordinator')
    effect = json.loads((run_dir / 'effects/publish.json').read_text())
    need(effect['state'] == 'completed' and effect['run-id'] == c['run-id'] and maps(c['own-publication']['directory']) == effect['new'], 'Renewed publication mismatch')
    global_guards()
    print('Internal completion only. Remains held for fresh independent exact-byte audit; no integration authorized.')
else:
    raise SystemExit('Unknown internal batch action')
PY
}

if [[ "$mode" == --check ]]; then
  batch21 check
  exit
fi
printf 'Separately authorized operator launch only: --confirm-idle asserts no prior same-run writer can continue.\n'
for executable in uv pi mountpoint flock; do command -v "$executable" >/dev/null; done
mountpoint -q "$output_disk"
batch21 release-check
# Fresh directory is a permanent one-shot fence, including preflight failure.
mkdir "$output_dir"
exec 9>"$output_dir/batch.lock"
flock -n 9
printf '%s\n' "$BASHPID" >"$output_dir/batch.pid"
batch21 check >"$output_dir/preflight.txt" 2>"$output_dir/preflight.stderr"
for index in 0 1 2 3 4 5 6 7 8; do
  mountpoint -q "$output_disk"
  batch21 release-check
  fields=$(batch21 paths "$index")
  IFS=$'\t' read -r run_id worktree prefix run_dir <<<"$fields"
  batch21 reset-feedback "$index" "$output_dir" >"$output_dir/$run_id.preparation.txt" 2>"$output_dir/$run_id.preparation.stderr"
  printf -v prompt 'Existing run: `%s`.\nPrepared command directory: `%s`.\nRead the complete `kb/agentic-system-analyses/instructions/analyse-agentic-system/drive-a-code-scheduled-run.md` and follow it for this run.' "$run_dir" "$prefix"
  if (cd "$worktree"; set -C; exec pi --approve --model openai/gpt-6.1-sol --thinking medium \
      --tools read,bash,edit,write,subagent --mode json "$prompt" >"$output_dir/$run_id.output" 2>&1); then
    printf '0\n' >"$output_dir/$run_id.exit"
  else
    code=$?
    printf '%s\n' "$code" >"$output_dir/$run_id.exit"
    printf 'Coordinator failure; stop without retry or cleanup.\n' >&2
    exit "$code"
  fi
  (cd "$worktree"; "$prefix/commonplace-analysis" inspect "$run_dir") >"$output_dir/$run_id.inspect.json" 2>"$output_dir/$run_id.inspect.stderr"
  batch21 verify "$index" "$output_dir/$run_id.inspect.json"
done
printf 'Nine correction coordinators completed internally. All results still require independent audit; no integration.\n'
