"""Q5-Q13: trace learning, write agency, read-back, curation, storage and tiers."""
from common import *  # noqa: F403
print('Q5 basis set over all axes, all tiers:', C(f['basis'] for r in R for a in AX for u,f in findings(r,a)))
print('Q5b union trace_learning (code):', C(tuple(json.loads(r['trace_learning'])) for r in code))
print('Q5c union trace_learning (doc):', C(tuple(json.loads(r['trace_learning'])) for r in doc))
no=[(r['system_name'],r['trace_learning_assessment'],r['trace_learning']) for r in code if 'no' in sv(r,'trace_learning')]
print('Q5d systems with local strong no:', no)
ty=[r for r in code if 'yes' in sv(r,'trace_learning')]
print('Q6 strong yes trace learning:', len(ty))
print('  among these, strong trace_source values:', C(v for r in ty for v in sv(r,'trace_source')))
print('  among these, no strong trace_source value:', sum(1 for r in ty if not sv(r,'trace_source')))
print('  among these, number of distinct source values:', C(len(sv(r,'trace_source')) for r in ty))
print('  among these, learning authority strong:', sum(1 for r in ty if 'learning' in sv(r,'behavioral_authority')))
print('  among these, model-weights strong:', [r['system_name'] for r in ty if 'model-weights' in sv(r,'storage_substrate')])
print('  among these, trace-extracted lineage strong:', sum(1 for r in ty if 'trace-extracted' in sv(r,'lineage')))
nl=[r for r in code if 'learning' in sv(r,'behavioral_authority') and 'yes' not in sv(r,'trace_learning')]
print('Q6b learning authority strong but no strong trace yes:', len(nl), C(r['trace_learning_assessment'] for r in nl))
print('Q7 model-weights strong:', [r['system_name'] for r in code if 'model-weights' in sv(r,'storage_substrate')])
print('Q7b parametric strong & model-weights strong:', sum(1 for r in code if 'model-weights' in sv(r,'storage_substrate')))
# write agency
m_any=[r for r in code if 'manual' in wv(r,'write_agency')]
m_s=[r for r in code if 'manual' in sv(r,'write_agency')]
print('Q8 manual any basis:', len(m_any), 'strong', len(m_s), 'weak-only', len(m_any)-len(m_s))
print('  weak-only manual basis split:', C(f['basis'] for r in m_any if r not in m_s for u,f in findings(r,'write_agency') if f['value']=='manual'))
print('  automatic strong but no manual at any basis:', sum(1 for r in code if 'automatic' in sv(r,'write_agency') and 'manual' not in wv(r,'write_agency')))
print('  write_agency unit assessments (code):', C(u['assessment'] for r in code for u in units(r,'write_agency')))
# read back
push=[r for r in code if 'push' in sv(r,'read_back_direction')]
inf={'inferred-embedding','inferred-lexical','inferred-judgment'}
print('Q9 strong push:', len(push))
print('  push with strong inferred-* signal:', sum(1 for r in push if sv(r,'read_back_signal')&inf))
print('  push with only coarse/identifier strong signals:', sum(1 for r in push if sv(r,'read_back_signal') and not sv(r,'read_back_signal')&inf))
print('  push with no strong signal:', sum(1 for r in push if not sv(r,'read_back_signal')))
print('  any strong inferred-* (all code):', sum(1 for r in code if sv(r,'read_back_signal')&inf))
print('  pull-only strong (no push any basis):', sum(1 for r in code if 'pull' in sv(r,'read_back_direction') and 'push' not in wv(r,'read_back_direction')))
print('  inapplicable signal systems:', [(r['system_name'],r['read_back_direction'],r['read_back_direction_assessment']) for r in code if r['read_back_signal_assessment']=='inapplicable'])
# curation
print('Q10 synthesize strong:', [r['system_name'] for r in code if 'synthesize' in sv(r,'curation_operations')])
print('Q10b no strong curation value:', sum(1 for r in code if not sv(r,'curation_operations')))
print('  curation count of strong ops distribution:', sorted(C(len(sv(r,'curation_operations')) for r in code).items()))
print('Q11 storage files strong but not other:', sum(1 for r in code if sv(r,'storage_substrate')=={'files'}), 'files+in-memory only', sum(1 for r in code if sv(r,'storage_substrate')<= {'files','in-memory'} and 'files' in sv(r,'storage_substrate')))
print('  no files strong:', [r['system_name'] for r in code if 'files' not in sv(r,'storage_substrate')][:40], sum(1 for r in code if 'files' not in sv(r,'storage_substrate')))
print('  any db (sqlite/rdbms/vector/graph/kv) strong:', sum(1 for r in code if sv(r,'storage_substrate')&{'sqlite','rdbms','vector','graph','kv'}))
print('Q12 boundary kind code:', C(r['boundary_kind'] for r in code))
print('Q13 doc tier names:', [r['system_name'] for r in doc])
print('Q13b doc tier basis:', C(f['basis'] for r in doc for a in AX for u,f in findings(r,a)))
