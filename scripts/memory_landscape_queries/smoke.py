"""Check retained query-ledger consistency without rereading/recounting the matrix."""
import json
from pathlib import Path

path = Path(__file__).resolve().parent / 'outputs-2026-11-09/snapshot.json'
ledger = json.loads(path.read_text())
assert ledger['inputs_commit'] == 'bf2da04db03fb4cb60be52d1bb04e638a79eda79'
expected = {'revision-2/code-grounded': 225, 'revision-2/doc-grounded': 18}
assert set(ledger['strata']) == set(expected)
checks = 0
for name, count in expected.items():
    stratum = ledger['strata'][name]
    assert stratum['population'] == count
    runs = {r['analysis_run'] for r in stratum['identities']}
    assert len(runs) == count
    assert sum(stratum['boundary_kinds'].values()) == count
    assert sum(stratum['cutoffs'].values()) == count
    queries = list(stratum['queries'].values())
    for axis in stratum['axes'].values():
        assert sum(axis['assessments'].values()) == count
        queries += [axis['complete'], *axis['strong'].values(),
                    *axis['weak_only'].values()]
    for query in queries:
        included, excluded = map(set, (query['included_runs'], query['excluded_runs']))
        assert not included & excluded
        assert included | excluded == runs
        assert len(included) == query['numerator']
        assert query['denominator'] == count
        assert query['fields'] and query['test'] and query['basis_filter']
        checks += 1
print(f'Ledger smoke passed: {checks} query memberships; 243 identities; two revision/tier strata.')
print('No matrix rebuild, checksum sweep or quantitative recomputation performed.')
