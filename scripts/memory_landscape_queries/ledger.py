"""Q0-Q4: population, per-axis assessments, existence counts and complete-set eligibility."""
from common import *  # noqa: F403

print('Q0 population', len(R), 'code', len(code), 'doc', len(doc), 'versions', C(r['comparison_version'] for r in R))
for a in AX:
    print('\n==', a)
    print(' Q1 axis assessment (code):', dict(C(r[a+'_assessment'] for r in code)))
    print(' Q1 axis assessment (doc):', dict(C(r[a+'_assessment'] for r in doc)))
    ex=C(); weak=C(); basisc=C()
    for r in code:
        sv=set(); wv=set()
        for u,f in findings(r,a):
            basisc[f['basis']]+=1
            (sv if f['basis'] in STRONG else wv).add(f['value'])
        for v in sv: ex[v]+=1
        for v in wv-sv: weak[v]+=1
    print(' Q2 existence (code, strong basis, systems):', dict(ex.most_common()))
    print(' Q3 weak-only values (code, claimed/afforded only):', dict(weak.most_common()))
    print(' Q3b finding basis counts (code):', dict(basisc))
    # complete set
    comp=[r for r in code if r[a+'_assessment']=='known' and all(f['basis'] in STRONG for u,f in findings(r,a))]
    print(' Q4 complete-set eligible (code, known axis, all strong):', len(comp))
    print('   distribution:', dict(C(tuple(sorted(json.loads(r[a]))) for r in comp).most_common(12)))
    known_weak=[r['system_name'] for r in code if r[a+'_assessment']=='known' and not all(f['basis'] in STRONG for u,f in findings(r,a))]
    print('   known but weak finding excluded:', len(known_weak))
