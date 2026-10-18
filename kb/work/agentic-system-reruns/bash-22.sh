#!/usr/bin/env bash
# Read-only batch preparation checker. Intentionally has no launch mode.
set -euo pipefail
if [[ $# -gt 1 ]]; then printf 'Usage: bash %s [--check | --help]\n' "$0" >&2; exit 2; fi
case "${1:---check}" in
  --help) printf 'Batch 22: thirteen fresh-start targets, including three source-selection gates.\nDefault/--check only verify preparation. No launch, acquisition, reset or ownership release.\n'; exit 0 ;;
  --check) ;;
  *) printf 'Batch 22 has no launch mode; use --check or --help.\n' >&2; exit 2 ;;
esac
cd "$(dirname "${BASH_SOURCE[0]}")/../../.."
export PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0
python3 - "$PWD" <<'PY'
import hashlib
import json
import os
from pathlib import Path
import sys

root = Path(sys.argv[1])
base = root / 'kb/work/agentic-system-reruns'
plan = json.loads((base / 'batch-22.json').read_text())
expected = {'awesome-agent-memory', 'letta', 'operational-ontology-framework',
            'ai-context-os', 'nams', 'llm-wiki-v3', 'llmwiki-marimo', 'siftly', 'sift-kg',
            'fragility-grid', 'ace', 'agent-skills-for-context-engineering', 'secure-llm-wiki'}
selection = {'awesome-agent-memory', 'letta', 'operational-ontology-framework'}


def need(value, message):
    if not value:
        raise SystemExit(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def bound(record):
    path = Path(record['path'])
    need(path.is_file() and path.resolve() == path and sha(path) == record['sha256'], f'Changed/redirected binding: {path}')


def maps(path):
    path = Path(path)
    need(path.is_dir() and path.resolve() == path, f'Missing/redirected directory: {path}')
    files = list(path.rglob('*'))
    need(not any(p.is_symlink() for p in files), f'Symlink in {path}')
    return {p.relative_to(path).as_posix(): sha(p) for p in files if p.is_file()}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


need(plan['status'] == 'prepared-not-launched' and not plan['execution-authorized'], 'Unexpected execution authority')
need(plan['method-revision'] is None, 'Method selection requires a later release record')
for record in plan['bindings']:
    bound(record)
original = json.loads(Path(plan['base-inventory']['path']).read_text())
bound(plan['base-inventory'])
by_key = {c['key']: c for c in original['rows']}
rows = plan['rows']
need(len(rows) == 13 and {r['key'] for r in rows} == expected, 'Wrong or duplicate batch membership')
independent_restarts = {'ace', 'agent-skills-for-context-engineering'}
need(set(plan['old-reconciliation-not-required']) == independent_restarts, 'Changed operator restart policy')
old_roots = [Path(c['worktree']) for c in original['rows']]
proposed = []
for row in rows:
    c = by_key[row['key']]
    need(row['predecessor'] == c, f"Predecessor identity/snapshot changed: {row['key']}")
    need(row['initial-source'] == c['source-identity'] and row['selected-source'] is None
         and row['new-run-id'] is None, 'Unreleased source/run selection')
    need(row['route'] == ('source-selection-first' if row['key'] in selection else 'fresh-isolated-analysis'), 'Wrong route')
    if row['key'] == 'secure-llm-wiki':
        need(row.get('release-gate') == 'profile-contract-validator-alignment', 'Missing method-alignment gate')
    kind = 'implementation-selection' if row['key'] in selection else ('document' if row['key'] == 'nams' else 'git')
    need(row['new-source-kind'] == kind, 'Wrong source route; NAMS must remain a document input')
    need(row['fresh-acquisition-required'] and row['old-hold-remains']
         and not row['execution-authorized'], 'Preservation/acquisition policy changed')
    for record in [c['run-definition'], c['preparation'], *c['evidence']]:
        bound(record)
    run = Path(c['run'])
    if row['key'] not in independent_restarts:
        need(maps(run / 'state/attempts') == c['attempts-map'], 'Old evidence changed; review preservation bindings, do not refresh mechanically')
        for path in (run / 'state/attempts').glob('*.json'):
            need(json.loads(path.read_text()).get('state') != 'open', 'Unexpected old writer; preserve and review isolation')
        need(not (run / '.reset-pending.json').exists(), 'Old reset is pending')
    # ACE/Agent Skills may remain unfinished: do not interpret or repair their
    # mutable state as an admission condition for a separately owned new run.
    if row['previous-acquisition-record'] is not None:
        bound(row['previous-acquisition-record'])
    own = c['own-publication']
    if own and row['key'] not in independent_restarts:
        need(maps(own['directory']) == own['members'], 'Old publication changed')
        bound(own['effect'])
        bound(own['manifest'])
    worktree = Path(row['proposed-worktree'])
    preparation = Path(row['proposed-preparation-record'])
    need(worktree.is_absolute() and preparation == Path(str(worktree) + '.preparation.json'), 'Bad proposed destination')
    need(worktree.resolve() == worktree and preparation.resolve() == preparation, 'Redirected proposed destination')
    need(not worktree.exists() and not worktree.is_symlink()
         and not preparation.exists() and not preparation.is_symlink(), 'Existing destination: stop without reuse/cleanup')
    need(worktree.parent.is_dir() and os.access(worktree.parent, os.W_OK | os.X_OK), 'Destination parent is not writable')
    need(not any(worktree == old or worktree.is_relative_to(old) or old.is_relative_to(worktree) for old in old_roots + proposed), 'Overlapping worktree ownership')
    proposed.append(worktree)
    print(f"{row['key']}: {row['route']} — fresh {row['new-source-kind']}; old hold unchanged")
retained = root / 'kb/agentic-system-analyses/retained'
canonical = {p.name: maps(p) for p in retained.iterdir() if p.is_dir()}
need(len(canonical) == plan['canonical']['sets'] and digest(canonical) == plan['canonical']['map-digest'], 'Canonical baseline changed; reconcile before release')
need({p.name: sha(p) for p in retained.iterdir() if p.is_file()} == plan['canonical']['root-files'], 'Retained root files changed')
print('CHECKED: thirteen targets; three source-selection gates, nine fresh Git acquisitions, one fresh document capture.')
print('Method release pending: align validator/tests with clarified profile coverage before new runs.')
print('PREPARATION ONLY. No launch mode; no acquisition/installation/run mutation, source suitability or writer-idle clearance.')
PY
