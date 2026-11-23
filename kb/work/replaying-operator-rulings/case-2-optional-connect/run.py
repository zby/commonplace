"""Single-use replay: run from the checkout; existing run directory blocks reruns."""
import concurrent.futures
import hashlib
import json
import random
import subprocess
import tempfile
from pathlib import Path

out = Path(__file__).resolve().parent / 'run'
out.mkdir()
paths = ['kb/reference/scenario-architecture.md', 'tests/scenarios/write-a-note.md',
         'kb/instructions/cp-skill-write/SKILL.md']
packet = ''.join('\n\nDOCUMENT: '+p+'\n'+subprocess.check_output(
    ['git', 'show', '8db5c7666:'+p], text=True) for p in paths)
frame = 'Review these three historical project documents together. What single correction is most important for a maintainer relying on them? State the correction and its practical consequence in at most three sentences.'
hint = 'Follow one ordinary use. Who needs this information, at what step, and what do they actually read or do next?'
arms = ['C','U']*3
random.SystemRandom().shuffle(arms)
key = dict(zip([f'a{i}' for i in range(1,7)], arms))
(out/'key.json').write_text(json.dumps(key, indent=2)+'\n')

def call(name, system, prompt):
    cmd = ['claude','-p','--model','opus','--tools','','--strict-mcp-config',
           '--disable-slash-commands','--no-session-persistence','--output-format','json',
           '--system-prompt',system]
    with tempfile.TemporaryDirectory() as cwd:
        r = subprocess.run(cmd,input=prompt,cwd=cwd,text=True,capture_output=True,timeout=900)
    if r.returncode:
        (out/(name+'.error')).write_text(r.stderr+'\n'+r.stdout)
        raise RuntimeError(f'{name} exited {r.returncode}')
    j=json.loads(r.stdout)
    (out/(name+'.meta.json')).write_text(json.dumps({k:j.get(k) for k in ('is_error','modelUsage','duration_ms','num_turns','total_cost_usd','stop_reason')},indent=2)+'\n')
    if j.get('is_error') or not j.get('result'): raise RuntimeError(name+' did not return a completion')
    (out/(name+'.txt')).write_text(j['result'].strip()+'\n')
    return j['result']

system='You are a careful reviewer of technical writing.'
def propose(item):
    name,arm=item
    return call(name,system,frame+ ('\n'+hint if arm=='U' else '')+packet)
(out/'packet.sha256').write_text(hashlib.sha256(packet.encode()).hexdigest()+'\n')
with concurrent.futures.ThreadPoolExecutor(3) as pool: list(pool.map(propose,key.items()))
rubric="Grade each anonymous answer H, P or M. H: distinguishes suggesting connect from executing it AND assigns connect’s invocation/context cost only to the optional follow-up, not the ordinary write. P: detects optionality or wrong cost but not their connection. M: neither. Extra observations don't exclude a hit. Return all six IDs with grade and a short justification. Do not infer conditions."
def score(i):
    ids=list(key); random.SystemRandom().shuffle(ids)
    return call('scorer'+str(i),'You independently score anonymous answers against a fixed rubric.',rubric+'\n\n'+'\n\n'.join(n+': '+(out/(n+'.txt')).read_text() for n in ids))
with concurrent.futures.ThreadPoolExecutor(2) as pool: list(pool.map(score,[1,2]))
