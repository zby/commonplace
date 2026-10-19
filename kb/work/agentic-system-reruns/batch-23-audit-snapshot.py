"""Commission-specific read-only evidence capture; output path must be new."""
import hashlib,json,pathlib,re,subprocess,sys
root=pathlib.Path('/home/zby/llm/commonplace'); out=root/'kb/work/agentic-system-reruns'; base=pathlib.Path('/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs')
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def tree(p): return {str(f.relative_to(p)):h(f) for f in sorted(p.rglob('*')) if f.is_file() and '.git' not in f.relative_to(p).parts}
def git(*args): return subprocess.check_output(['git',*args],text=True).strip()
rec={'origin':str(root),'head':git('-C',str(root),'rev-parse','HEAD'),'status':git('-C',str(root),'status','--short'),'diagnostic':'COMMONPLACE_WORKER_OK; depth/nesting unknown','canonical':tree(root/'kb/agentic-system-analyses/retained'),'archives':tree(root/'kb/agentic-system-analyses/retained-archive'),'gitignore':h(root/'.gitignore'),'unrelated':{str(p.relative_to(root)):h(p) for p in [root/'kb/work/README.md',*(root/'kb/work/headless-workflow-extraction').rglob('*')] if p.is_file()},'cases':{}}
for k in ['jaz','autogenesis','arex-skill','contextpilot','openrsi','supermemory']:
 w=base/'commonplace-worktrees'/('batch-23-'+k); prep=w.with_name(w.name+'.preparation.json'); p=json.loads(prep.read_text()); runs=[x for x in (w/'kb/agentic-system-analyses/state').iterdir() if x.is_dir()]; assert len(runs)==1; r=runs[0]; e=r/'effects/publish.json'; effect=json.loads(e.read_text()); dest=pathlib.Path(effect['destination']); actual=tree(dest); assert actual==effect['new'] and len(actual)==13
 boundary=(dest/'boundary.md').read_text(); sourcepath=re.search(r'^  path: (.+)$',boundary,re.M).group(1); revision=re.search(r'^  revision: "?([a-f0-9]{40})',boundary,re.M).group(1); assert git('-C',sourcepath,'rev-parse','HEAD')==revision
 rec['cases'][k]={'run-id':r.name,'method-commit':p['commit'],'preparation':str(prep),'preparation-sha256':h(prep),'worktree':str(w),'path-prefix':p['path-prefix'],'run':str(r),'source-identity':effect['source-identity'],'source-revision':revision,'source-path':sourcepath,'source-files':tree(pathlib.Path(sourcepath)),'publication':str(dest),'publication-files':actual,'effect':str(e),'effect-sha256':h(e),'run-files':tree(r),'log':str(base/'batch-23'/(k+'.output')),'log-sha256':h(base/'batch-23'/(k+'.output')),'historical-audits-leads-only':[str(x.relative_to(root)) for x in (out/'audits').rglob('*.md') if k in x.name.lower()],'report':str(out/'audits'/('batch-23-'+k+'.md')),'incumbent':tree(root/dest.relative_to(w)) if (root/dest.relative_to(w)).exists() else None}
 assert p['commit']=='3e2491c83a4613d410511af8c3cfde30f4b67689' and p['status']=='ready'
rec['canonical-set-count']=len(list((root/'kb/agentic-system-analyses/retained').glob('*/ARTIFACT.yaml')))
rec['canonical-member-count']=sum('/' in name for name in rec['canonical'])
with pathlib.Path(sys.argv[1]).open('x') as f: json.dump(rec,f,indent=2); f.write('\n')
print(rec['canonical-set-count'],rec['canonical-member-count'],len(rec['cases']))
