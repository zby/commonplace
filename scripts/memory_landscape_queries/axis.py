"""Print one set's memory-profile units and findings for the named axes: axis.py <set-dir> <axis>..."""
import yaml,sys
from pathlib import Path
d,axes=sys.argv[1],sys.argv[2:]
t=open(Path(__file__).resolve().parents[2] / 'kb/agentic-system-analyses/retained' / d / 'memory-profile.md').read().split('\n---\n')[0]
m=yaml.safe_load(t.lstrip('-\n'))['memory-comparison']
for a in axes:
    x=m['axes'][a]; print('##',d,a,x['assessment'],'|',x['note'])
    for u in x['units']:
        print('  U[%s] %s | %s'%(u['assessment'],u['scope'],u['note'][:250]))
        for f in u['findings']: print('     -',f['value'],f['basis'],f['records'],'|',f['note'][:300])
