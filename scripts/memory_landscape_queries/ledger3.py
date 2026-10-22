"""Named systems behind the write-agency, read-back and trace-source counts; doc-tier checks."""
from common import *  # noqa: F403
print('manual strong:', sorted(r['system_name'] for r in code if 'manual' in sv(r,'write_agency')))
print('manual weak-only:', sorted(r['system_name'] for r in code if 'manual' in wv(r,'write_agency') and 'manual' not in sv(r,'write_agency')))
for s in ['inferred-judgment','inferred-embedding','inferred-lexical']:
    print(s, sorted(r['system_name'] for r in code if s in sv(r,'read_back_signal')))
print('trace sources trajectories:', sorted(r['system_name'] for r in code if 'trajectories' in sv(r,'trace_source')))
print('known trace_learning union none & not-determinable:', sorted(r['system_name'] for r in code if r['trace_learning_assessment']=='not-determinable'))
print('Q14 doc-tier trace_learning yes basis per system:', {r['system_name']:sorted({f['basis'] for u,f in findings(r,'trace_learning') if f['value']=='yes'}) for r in doc if 'yes' in wv(r,'trace_learning')})
print('Q14b doc-tier model-weights any basis:', [r['system_name'] for r in doc if 'model-weights' in wv(r,'storage_substrate')])
