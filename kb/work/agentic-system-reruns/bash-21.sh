#!/usr/bin/env bash
# Batch 21 is a gated decision/repair queue, NOT an analysis launcher.
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0
if [[ $# -gt 1 ]]; then
  printf 'Usage: bash bash-21.sh [--check|--help]\n' >&2
  exit 2
fi
case "${1:---check}" in
  --help|-h)
    printf 'Batch 21 covers all 25 remaining inventory targets.\nRead-only check: bash bash-21.sh --check\nNo launch mode: repair/source/refusal/ownership decisions remain.\n'
    exit 0 ;;
  --check) ;;
  *) printf 'Batch 21 is not launchable: use --check and resolve batch-21.md gates. No reset, acquisition or coordinator was started.\n' >&2; exit 2 ;;
esac
cd "$(dirname "${BASH_SOURCE[0]}")/../../.."
exec python3 - <<'PY'
from pathlib import Path
import collections
import hashlib
import json
import re
import sys

root = Path.cwd()
base = root / 'kb/work/agentic-system-reruns'
retained = root / 'kb/agentic-system-analyses/retained'


def need(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def bound(record):
    path = Path(record['path'])
    need(digest(path) == record['sha256'], f'Changed input: {path}')
    return path


def file_map(directory):
    directory = Path(directory)
    need(directory.is_dir() and not directory.is_symlink(), f'Invalid directory: {directory}')
    paths = list(directory.rglob('*'))
    need(not any(path.is_symlink() for path in paths), f'Symlink in bound tree: {directory}')
    return {path.relative_to(directory).as_posix(): digest(path)
            for path in paths if path.is_file()}


def map_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


try:
    plan = json.loads((base / 'batch-21.json').read_text())
    need(plan['status'] == 'prepared-gated-not-launched', 'Reconcile changed batch status')
    cases = plan['rows']
    need(len(cases) == 25 and len({case['key'] for case in cases}) == 25, 'Expected 25 distinct targets')
    need(not any(case['execution-authorized'] for case in cases), 'This checker cannot release execution')
    groups = collections.Counter(case['gate'] for case in cases)
    need(groups == {'repair': 9, 'source-boundary-refusal': 8, 'ownership-operational': 8}, 'Reconcile changed scheduling gates')
    inventory = bound(plan['inventory']).read_text()
    rows = [re.match(r'- \[([ x])\] \*\*.*?\*\* \(`([^`]+)`\)', line)
            for line in inventory.splitlines()]
    rows = [row for row in rows if row]
    need(len(rows) == 206 and sum(row[1] == 'x' for row in rows) == 181, 'Reconcile inventory counts')
    need({row[2] for row in rows if row[1] == ' '} == {case['key'] for case in cases}, 'Remainder does not match checklist')
    need(sum(case['inventory-status'] == 'older-target-hold' for case in cases) == 4, 'Reconcile older target holds')
    proof = json.loads(bound(plan['integration-proof']).read_text())
    need(proof['state'] == 'complete', 'Integration proof is incomplete')
    canonical = {path.name: file_map(path) for path in retained.iterdir() if path.is_dir()}
    need(len(canonical) == 182 and sum(map(len, canonical.values())) == 2366, 'Reconcile canonical counts')
    need(map_digest(canonical) == proof['canonical-after']['map-digest'], 'Canonical bytes changed')
    need({path.name: digest(path) for path in retained.iterdir() if path.is_file()}
         == proof['retained-root-files'], 'Retained-root files changed')
    raw = json.loads(bound(proof['raw-results']).read_text())
    need(raw['state'] == 'complete' and raw['final'] == canonical, 'Canonical transfer proof mismatch')
    for case in cases:
        definition = json.loads(bound(case['run-definition']).read_text())
        bound(case['preparation'])
        need(definition['parameters']['source-identity'].lower().rstrip('/')
             == case['source-identity'].lower().rstrip('/'), f"Source mismatch: {case['key']}")
        attempts = Path(case['run']) / 'state/attempts'
        need({path.name: digest(path) for path in attempts.glob('*.json')} == case['attempts-map'],
             f"Attempts changed; reconcile ownership: {case['key']}")
        for evidence in case['evidence']:
            bound(evidence)
        publication = case['own-publication']
        if publication is not None:
            need(file_map(publication['directory']) == publication['members'], f"Own publication changed: {case['key']}")
            bound(publication['effect'])
            bound(publication['manifest'])
    for case in cases:
        print(f"{case['key']}: {case['gate']} — {case['next-decision']}")
    print('CHECKED: all 25 remaining targets; 9 repair / 8 source-boundary-refusal / 8 ownership-operational.')
    print('Prepared only; no launch mode. Metadata bindings are not a writer-idle or ownership clearance.')
except (OSError, ValueError, TypeError, KeyError) as error:
    print(f'Batch 21 check blocked: {error}', file=sys.stderr)
    sys.exit(2)
PY
