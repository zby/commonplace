#!/usr/bin/env bash
# Active batch 21: nine fresh lineages. Read-only; no launch or old-run recovery.
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0
if [[ $# -gt 1 ]]; then printf 'Usage: bash %s [--check|--help]\n' "$0" >&2; exit 2; fi
case "${1:---check}" in
  --help|-h) printf 'Batch 21: nine full fresh analyses, not old-run corrections.\nDefault/--check verifies preparation only. No launch mode.\n'; exit 0 ;;
  --check) ;;
  *) printf 'No launch mode. Use --check or --help; no acquisition/reset/analysis was started.\n' >&2; exit 2 ;;
esac
cd "$(dirname "${BASH_SOURCE[0]}")/../../.."
exec python3 - <<'PY'
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

root = Path.cwd()
base = root / 'kb/work/agentic-system-reruns'
expected = {'supermemory', 'contextpilot', 'openrsi', 'modularrsi', 'jaz', 'autogenesis',
            'mehmetgoekce--llm-wiki', 'clawvault', 'arex-skill'}
# Exact independently reviewed commissions, not substring presence or a hash
# supplied alongside editable task text. Re-review before changing these seals.
expected_tasks = {
    'supermemory': 'ffffc65ffd4120b09d6a7f15b02e35b9ea1e15b2a1f086035db058e7186863f2',
    'contextpilot': '4d18102ad4405782412bf5f84ea575ccd80e2798a078bb56236389f7c53fdedc',
    'openrsi': '7b0b42a0266c530ed83397f5ef9c2389f724d6b9c6912bb05aea66269c646f32',
    'modularrsi': '140b2f3d4a116f2d0ebe68637e9f98890f0797fd514394373f6ba16da71e4457',
    'jaz': '6b7e71205e7716d4931eb1e9ea96a03fbd75c3739ff5e5f69d623e141226085b',
    'autogenesis': '1eb21ad49f4ae15333b5e52dd71f21783a2c22cb09b50f2d00e3181cdd104316',
    'mehmetgoekce--llm-wiki': '10761a5bb098c9e5c4f850bf1ffa06203271fc78f91bdbe2a1f375f42efc3723',
    'clawvault': '530949a57b20b1b56b90b9867a6b61b773373a8a50d9217b24a51e6252a556e5',
    'arex-skill': 'bdbedef1e47fcfbaab22a75ad59c10cb73894956135bc4b798bdb876856810b5',
}


def need(value, message):
    if not value:
        raise SystemExit(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def bound(record):
    path = Path(record['path'])
    need(path.is_file() and path.resolve() == path and sha(path) == record['sha256'],
         f'Changed/redirected binding: {path}')


def maps(directory):
    directory = Path(directory)
    need(directory.is_dir() and directory.resolve() == directory, f'Missing/redirected tree: {directory}')
    files = list(directory.rglob('*'))
    need(not any(path.is_symlink() for path in files), f'Symlink in {directory}')
    return {path.relative_to(directory).as_posix(): sha(path) for path in files if path.is_file()}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


plan = json.loads((base / 'batch-21-fresh.json').read_text())
need(plan['status'] == 'prepared-fresh-not-launched' and not plan['execution-authorized'], 'Unexpected authority')
for record in plan['bindings']:
    bound(record)
original = json.loads((base / 'batch-21.json').read_text())
originals = {r['key']: r for r in original['rows']}
other = json.loads((base / 'batch-22.json').read_text())
rows = plan['rows']
need(len(rows) == 9 and {r['key'] for r in rows} == expected, 'Expected nine exact fresh cases')
need(not expected.intersection(r['key'] for r in other['rows']), 'Batch overlap')
need(plan['worker-profile'] == 'pi-sol', 'Worker profile changed')
method = plan['method-revision']
need(re.fullmatch(r'[0-9a-f]{40}', method), 'Method must be a full committed revision')
actual = subprocess.check_output(['git', 'rev-parse', '--verify', method + '^{commit}'], text=True).strip()
need(actual == method, 'Unresolved method')
method_paths = ['src/commonplace', 'kb/agentic-system-analyses/instructions',
                'kb/agentic-system-analyses/types', 'pyproject.toml', 'uv.lock',
                'AGENTS.md', 'CLAUDE.md', '.pi', '.agents', '.claude']
for index in [[], ['--cached']]:
    changes = subprocess.check_output(['git', 'diff', *index, '--name-only', method, '--', *method_paths], text=True)
    need(not changes, 'Selected code/method/startup/dependencies changed; review release')
need(not subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard', '--', 'src/commonplace'],
                                text=True), 'Untracked package code')
ledger = Path(plan['runtime-ledger'])
need(ledger.is_absolute() and ledger.resolve() == ledger, 'Redirected ledger')
need(not ledger.exists() and not ledger.is_symlink(), 'Existing runtime ledger: reconcile without reuse')
need(ledger.parent.is_dir() and os.access(ledger.parent, os.W_OK | os.X_OK), 'Ledger parent not writable')
old_roots = [Path(r['worktree']) for r in original['rows']]
other_roots = [Path(r['proposed-worktree']) for r in other['rows']]
new_roots = []
for row in rows:
    key = row['key']
    old = originals[key]
    need(row['source'] == old['source-identity'] and row['source-kind'] == 'git', 'Source route changed')
    need(re.fullmatch(r'https://github\.com/[^/?#]+/[^/?#]+/?', row['source']), 'Not an exact GitHub root')
    need(row['predecessor'] == {k: old[k] for k in ['run-id', 'worktree', 'run', 'method-revision']},
         'Historical lineage identity changed')
    need(row['route'] == 'full-fresh-analysis' and row['fresh-acquisition-required']
         and not row['execution-authorized'] and row['new-run-id'] is None
         and row['new-source-commit'] is None, 'Not an unreleased full fresh commission')
    need(row['agent'] == 'commonplace-coordinator' and row['agentScope'] == 'project'
         and row['cwd'] == str(root) and row['model'] == 'openai/gpt-6.1-sol'
         and row['thinkingLevel'] == 'medium', 'Wrong dispatch binding')
    worktree = Path(row['proposed-worktree'])
    preparation = Path(row['proposed-preparation-record'])
    need(worktree.is_absolute() and preparation == Path(str(worktree) + '.preparation.json'), 'Bad destination')
    need(worktree.name == 'batch-21-fresh-' + key, 'Wrong fresh destination label')
    for path in [worktree, preparation]:
        need(path.resolve() == path and not path.exists() and not path.is_symlink(),
             f'Existing/redirected destination: {path}')
    need(worktree.parent.is_dir() and os.access(worktree.parent, os.W_OK | os.X_OK), 'Worktree parent not writable')
    need(not any(worktree == p or worktree.is_relative_to(p) or p.is_relative_to(worktree)
                 for p in [root] + old_roots + other_roots + new_roots), 'Overlapping origin/old/new/batch-22 ownership')
    new_roots.append(worktree)
    need(isinstance(row['task'], str)
         and hashlib.sha256(row['task'].encode()).hexdigest() == expected_tasks[key], 'Reviewed packet text changed')
    need(row['source'] in row['task'] and str(worktree) in row['task'] and method in row['task'], 'Incomplete packet')
    owner, project = row['source'].rstrip('/').split('/')[-2:]
    publication = root / 'kb/agentic-system-analyses/retained' / f'{owner}--{project}'.lower()
    need(not publication.exists() and not publication.is_symlink(), 'Canonical target incumbent: explicit decision required')
    print(f'{key}: full fresh analysis; old run untouched; new destination absent')
retained = root / 'kb/agentic-system-analyses/retained'
canonical = {p.name: maps(p) for p in retained.iterdir() if p.is_dir()}
need(len(canonical) == plan['canonical']['sets'] == 182
     and sum(map(len, canonical.values())) == plan['canonical']['members'] == 2366
     and digest(canonical) == plan['canonical']['map-digest'], 'Canonical baseline changed')
need({p.name: sha(p) for p in retained.iterdir() if p.is_file()} == plan['canonical']['root-files'], 'Root files changed')
print('CHECKED: nine fresh analyses; no reset/refusal/old-writer gate; thirteen batch-22 cases remain separate.')
print('PREPARATION ONLY. No launch mode; metadata/path checks do not prove writer exclusivity or source availability.')
PY
