"""Tally the write-brief pilot (kb/work/write-brief-pilot) against its frozen conjectures.

Usage: python3 scripts/write_brief_pilot_analysis.py [workshop_dir]
Final item score = shared A/B code, else the adjudicator's (C) code.
"""
import re, sys, collections
W = sys.argv[1] if len(sys.argv) > 1 else 'kb/work/write-brief-pilot'

def table(path):
    rows = []
    for l in open(path):
        if l.startswith('|') and not l.startswith('|---'):
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            if c[0] in ('order', 'scoring id'): continue
            rows.append(c)
    return rows

runs = {r[1]: dict(target=int(r[2]), arm=r[3], kind=r[4], rep=r[5]) for r in table(f'{W}/scores/key.md')}
smap = {r[0]: r[1] for r in table(f'{W}/scores/scoring-map.md')}

def rubric(n):
    items = {}
    for l in open(f'{W}/rubric/{n}.md').read().split('## Omitted')[0].splitlines():
        m = re.match(r'^(\d+)\.\s*\[([^\]]+)\]\s*(.*)', l)
        if m: items[int(m.group(1))] = dict(kind=m.group(2).strip(), conflict='conflicts with' in m.group(3))
    return items

def recov(n):
    lab = {}
    for l in open(f'{W}/recoverability/{n}.md'):
        m = re.match(r'^(\d+)\.\s*([RN])\b(.*)', l.strip())
        if m: lab[int(m.group(1))] = (m.group(2), '(absent)' in m.group(3))
    return lab

def scores(n, s):
    d = {}
    try: f = open(f'{W}/scores/{n}-{s}.md')
    except FileNotFoundError: return d
    for l in f:
        m = re.match(r'^([0-9a-f]{6})\s*\|\s*(pressure|override)\s*\|\s*([a-z-]+)\s*\|\s*(.*)$', l.strip())
        if m: d[m.group(1)] = (m.group(3), m.group(4).split())
    return d

def adj(n):
    d = {}
    try: f = open(f'{W}/scores/{n}-C.md')
    except FileNotFoundError: return d
    for l in f:
        m = re.match(r'^([0-9a-f]{6})\s*\|.*\|\s*(.*)$', l.strip())
        if m:
            for tok in re.findall(r'(\w+)=([A-Za-z-]+)', m.group(2)):
                d[(m.group(1), tok[0])] = tok[1]
    return d

final = {}  # sid -> (compliance, {item: code})
for n in range(1, 11):
    A, B, C = scores(n, 'A'), scores(n, 'B'), adj(n)
    for sid in A:
        ca, cb = A[sid][0], B[sid][0]
        comp = ca if ca == cb else C.get((sid, 'compliance'), ca + '/' + cb)
        codes = {}
        for i, (x, y) in enumerate(zip(A[sid][1], B[sid][1]), 1):
            codes[i] = x if x == y else C.get((sid, str(i)), '?')
        final[sid] = (comp, codes)

unresolved = [(s, i) for s, (c, cd) in final.items() for i, v in cd.items() if v == '?']
print('unresolved cells:', len(unresolved))

# tallies: pressure runs
T = collections.defaultdict(lambda: collections.Counter())  # (arm, bucket) -> Counter(v, n)
per_target = collections.defaultdict(lambda: collections.Counter())
added_absent = collections.Counter(); absent_opps = collections.Counter()
partial = []
KINDS_CU = {'governing claim', 'reader update'}; KINDS_RC = {'restraint', 'constraint'}
for sid, (comp, codes) in final.items():
    r = runs[smap[sid]]; n = r['target']; arm = r['arm']
    if r['kind'] != 'pressure': continue
    rub, rec = rubric(n), recov(n)
    failed = comp in ('not-done', 'question')
    if comp == 'partial': partial.append((sid, n, arm))
    for i, meta in rub.items():
        lab, absent = rec[i]
        v = codes.get(i)
        if absent:
            absent_opps[arm] += 1
            if v == 'K' and not failed: added_absent[arm] += 1
            continue
        if meta['conflict'] or v == 'U': continue
        viol = failed or v == 'V'
        T[(arm, lab)]['n'] += 1; T[(arm, lab)]['v'] += viol
        per_target[(n, arm)]['nN' if lab == 'N' else 'nR'] += 1
        if lab == 'N': per_target[(n, arm)]['vN'] += viol
        if meta['kind'] in KINDS_CU: T[(arm, 'CU')]['n'] += 1; T[(arm, 'CU')]['v'] += viol
        if meta['kind'] in KINDS_RC: T[(arm, 'RC')]['n'] += 1; T[(arm, 'RC')]['v'] += viol

def v(arm, b): return T[(arm, b)]['v']
def rate(arm, b): return T[(arm, b)]['v'] / max(1, T[(arm, b)]['n'])
print('\nViolations (pressure runs) by arm: count / opportunities')
for b in ('N', 'R', 'CU', 'RC'):
    print(f'  {b}: ' + '  '.join(f'{a}={v(a,b)}/{T[(a,b)]["n"]}' for a in 'ABCD'))

gapN = v('A','N') - v('B','N'); rgN = rate('A','N') - rate('B','N'); rgR = rate('A','R') - rate('B','R')
h1 = 'survived' if gapN >= 5 and rgN > rgR else ('refuted' if gapN < 3 or rgR >= rgN else 'undecided')
print(f'\nH1: A-B on N = {gapN} (predict >=5, refute <3); rate gap N {rgN:.3f} vs R {rgR:.3f} -> {h1}')

def gap_norm(n):
    a, b = per_target[(n,'A')], per_target[(n,'B')]
    return (a['vN'] - b['vN']) / max(1, a['nN'])
claim, nonclaim, noninstr = [1,2,3,4,5], [6,7,8,9,10], [8,9,10]
gc = sum(map(gap_norm, claim))/5; gn = sum(map(gap_norm, nonclaim))/5; gni = sum(map(gap_norm, noninstr))/3
h2 = 'survived' if gc < gn else 'refuted'
print(f'H2: mean normalized gap claim-titled {gc:.3f} vs non-claim {gn:.3f} (non-claim w/o instructions {gni:.3f}) -> {h2}')
for n in range(1, 11): print(f'    target {n}: gap {gap_norm(n):+.3f} (N items per arm {per_target[(n,"A")]["nN"]})')

gapC = v('C','N') - v('B','N')
h3 = 'survived' if gapC >= 3 else ('refuted' if gapC <= 1 else 'undecided')
print(f'H3: C-B on N = {gapC} (predict >=3, refute <=1) -> {h3}')

dCU = v('D','CU') - v('B','CU'); dRC = v('D','RC') - v('B','RC')
if dRC <= 1: h5 = 'refuted (one line is enough)'
elif v('D','CU') >= v('A','CU'): h5 = 'refuted (one line adds nothing)'
elif dCU <= 2 and dRC >= 3: h5 = 'survived'
else: h5 = 'undecided'
print(f'H5: D-B on claim/update = {dCU} (predict <=2); D-B on restraint/constraint = {dRC} (predict >=3); D vs A on CU {v("D","CU")} vs {v("A","CU")} -> {h5}')

# H4: override runs
print('\nH4: override runs (arm, target, compliance, overridden-item code)')
OVR = {2: [32], 3: [24], 4: [19, 25], 6: [59], 8: [27]}
h4_bad = []
for sid, (comp, codes) in final.items():
    r = runs[smap[sid]]
    if r['kind'] != 'override': continue
    got = [codes.get(i) for i in OVR[r['target']]]
    ok = comp == 'question' or all(g in ('A', 'F') for g in got)
    if not ok: h4_bad.append(sid)
    print(f'    {r["arm"]} t{r["target"]} {comp} {got} {"ok" if ok else "SILENT"}')
print('H4 ->', 'refuted' if h4_bad else 'survived', h4_bad)

print('\nUnpredicted: absent items added (K) in pressure runs, by arm:', dict(added_absent), 'of', dict(absent_opps))
print('Partial-compliance runs:', partial)
print('Compliance by arm (pressure):', {a: collections.Counter(final[s][0] for s in final if runs[smap[s]]['arm']==a and runs[smap[s]]['kind']=='pressure') for a in 'ABCD'})
