"""Q15-Q17: complete-set distributions, known-axis counts, runs and cutoffs."""
from common import *  # noqa: F403
for a in ['storage_substrate','representational_form','read_back_direction','read_back_signal']:
    comp=[r for r in code if r[a+'_assessment']=='known' and all(f['basis'] in STRONG for u,f in findings(r,a))]
    vals=C(v for r in comp for v in json.loads(r[a]))
    print('Q15',a,'eligible',len(comp),'value membership',dict(vals),'names',sorted(r['system_name'] for r in comp) if len(comp)<12 else '')
print('Q16 known-axis counts all tiers:', {a:sum(1 for r in R if r[a+'_assessment']=='known') for a in AX})
print('Q17 runs:', len({r['analysis_run'] for r in R}), 'cutoff dist', sorted(C(r['analysis_cutoff'] for r in R).items()))
