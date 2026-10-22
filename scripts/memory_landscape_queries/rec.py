"""Print canonical records from one set: rec.py <set-dir> <member.md>#<record-anchor>..."""
import sys,re
from pathlib import Path
base=Path(__file__).resolve().parents[2] / 'kb/agentic-system-analyses/retained'
d=sys.argv[1]
for ref in sys.argv[2:]:
    f,anc=ref.split('#')
    lines=open(base / d / f).read().split('\n')
    out=[];on=False
    for l in lines:
        if l.startswith('#### '):
            if on: break
            if l[5:].strip().lower()==anc: on=True
        if on: out.append(l)
    print('>>>',d,ref,'\n'+'\n'.join(out)[:1800] if out else 'NOT FOUND')
