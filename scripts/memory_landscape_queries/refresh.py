"""Frozen snapshot queries; pass the builder-produced matrix explicitly.

Reuses common.py's unit decoder and strong-basis rule. Outputs one JSON ledger
with membership/exclusions, not just counts. No matrix generation or hashing.
Revision-1 write semantics are never pooled with revision 2.
"""
from common import AX, STRONG, C, R, findings, json, sv, units, wv


def query(rows, fields, test, predicate, *, basis_filter=None):
    included = [r['analysis_run'] for r in rows if predicate(r)]
    return {
        'fields': fields, 'test': test,
        'basis_filter': sorted(STRONG) if basis_filter is None else basis_filter,
        'numerator': len(included), 'denominator': len(rows),
        'included_runs': included,
        'excluded_runs': [r['analysis_run'] for r in rows
                          if r['analysis_run'] not in included],
    }


def snapshot(rows):
    result = {
        'population': len(rows),
        'identities': [{k: r[k] for k in (
            'system_name', 'analysis_run', 'source_identity', 'review_file',
            'artifact_file', 'artifact_sha256', 'reviewed_revision',
            'analysis_cutoff', 'boundary_kind')} for r in rows],
        'boundary_kinds': dict(C(r['boundary_kind'] for r in rows)),
        'cutoffs': dict(sorted(C(r['analysis_cutoff'] for r in rows).items())),
        'basis_census': dict(C(f['basis'] for r in rows for a in AX
                               for _, f in findings(r, a))),
        'axes': {}, 'queries': {},
    }
    for a in AX:
        values = sorted(set().union(*(wv(r, a) for r in rows)))
        result['axes'][a] = {
            'assessments': dict(C(r[a + '_assessment'] for r in rows)),
            'unit_assessments': dict(C(u['assessment'] for r in rows
                                      for u in units(r, a))),
            'strong': {v: query(rows, [a + '_units'], f'any strong {v}',
                                lambda r, v=v, a=a: v in sv(r, a)) for v in values},
            'weak_only': {v: query(rows, [a + '_units'],
                                   f'{v} present but no strong witness',
                                   lambda r, v=v, a=a: v in wv(r, a) - sv(r, a),
                                   basis_filter=['claimed', 'afforded'])
                          for v in values},
            'complete': query(rows, [a + '_assessment', a + '_units'],
                              'known axis; every positive unit finding strong',
                              lambda r, a=a: r[a + '_assessment'] == 'known'
                              and all(f['basis'] in STRONG
                                      for _, f in findings(r, a))),
        }
    tests = {
        'push_with_inferred': (
            ['read_back_direction_units', 'read_back_signal_units'],
            lambda r: 'push' in sv(r, 'read_back_direction') and bool(
                sv(r, 'read_back_signal') & {
                    'inferred-embedding', 'inferred-lexical', 'inferred-judgment'})),
        'push_without_strong_inferred': (
            ['read_back_direction_units', 'read_back_signal_units'],
            lambda r: 'push' in sv(r, 'read_back_direction') and bool(
                sv(r, 'read_back_signal')) and not sv(r, 'read_back_signal') & {
                    'inferred-embedding', 'inferred-lexical', 'inferred-judgment'}),
        'complete_pull_only': (
            ['read_back_direction_assessment', 'read_back_direction_units'],
            lambda r: r['read_back_direction_assessment'] == 'known'
            and sv(r, 'read_back_direction') == {'pull'}
            and all(f['basis'] in STRONG for _, f in
                    findings(r, 'read_back_direction'))),
        'manual_any': (['write_agency_units'],
                       lambda r: 'manual' in wv(r, 'write_agency')),
        'files_only_strong': (['storage_substrate_units'],
                              lambda r: sv(r, 'storage_substrate') == {'files'}),
        'any_db': (['storage_substrate_units'], lambda r: bool(
            sv(r, 'storage_substrate') & {'sqlite', 'rdbms', 'vector', 'graph', 'kv'})),
        'curation_3_to_7': (['curation_operations_units'],
                            lambda r: 3 <= len(sv(r, 'curation_operations')) <= 7),
        'trace_yes_weights': (['trace_learning_units', 'storage_substrate_units'],
                              lambda r: 'yes' in sv(r, 'trace_learning')
                              and 'model-weights' in sv(r, 'storage_substrate')),
        'trace_local_no': (['trace_learning_units'],
                           lambda r: 'no' in sv(r, 'trace_learning')),
    }
    for name, (fields, predicate) in tests.items():
        result['queries'][name] = query(
            rows, fields, name, predicate,
            basis_filter=['claimed', 'afforded', *sorted(STRONG)]
            if name == 'manual_any' else None)
    # A local no is retained above, never interpreted as a system-wide negative.
    result['trace_unions'] = dict(C(r['trace_learning'] for r in rows))
    return result


output = {
    'selection': 'all current accepted sets; no review filter',
    'inputs_commit': 'bf2da04db03fb4cb60be52d1bb04e638a79eda79',
    'matrix_sha256_recorded_by_builder':
        '19da70a6ca54b9c659dd9d1bf734e5f46885325d48f58b40685eccea083ce0bc',
    'strata': {},
}
for version in sorted({r['comparison_version'] for r in R}):
    for tier in sorted({r['source_tier'] for r in R}):
        selected = [r for r in R if r['comparison_version'] == version
                    and r['source_tier'] == tier]
        output['strata'][f'revision-{version}/{tier}'] = snapshot(selected)
print(json.dumps(output, indent=2, sort_keys=True))
