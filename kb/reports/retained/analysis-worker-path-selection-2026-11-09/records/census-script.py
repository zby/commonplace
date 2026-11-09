import json, re, shlex, subprocess, tempfile
from pathlib import Path
from collections import Counter, defaultdict

OLD=Path('/tmp/commonplace-hidden-failures-16-p9m83wvc')
OUT=Path(tempfile.mkdtemp(prefix='commonplace-path-base-rates-'))
selected=json.loads((OLD/'selection.json').read_text())['selected']
rows=[]; excluded=[]; catalogs={}; snapshots=[]

def textcontent(result):
    if isinstance(result,str): return result
    if not isinstance(result,dict): return ''
    return '\n'.join(c.get('text','') for c in result.get('content',[]) if c.get('type')=='text')

def expand_braces(s):
    match=re.search(r'\{([^{}]*,[^{}]*)\}',s)
    if not match:return [s]
    return [y for choice in match[1].split(',') for y in expand_braces(s[:match.start()]+choice+s[match.end():])]

def shell_operands(command, root, meta, line):
    # Deliberately only literal absolute path operands of simple inspection commands.
    # No shell execution or substitution, no glob expansion, and no Python/JS evaluation.
    try:
        lex=shlex.shlex(command,posix=True,punctuation_chars=';&|()<>');lex.whitespace_split=True;lex.commenters='';tokens=list(lex)
    except ValueError:
        excluded.append({**meta,'line':line,'reason':'unparsed-shell','command':command});return []
    result=[];program=None
    for token in tokens:
        if token in (';','&&','||','|','\n'):
            program=None;continue
        if program is None:
            program=Path(token).name;continue
        if not token.startswith(str(root)+'/'):continue
        if program not in ('rg','grep','cat','nl','head','tail','wc','ls','find'):
            excluded.append({**meta,'line':line,'reason':'non-simple-program-path','program':program,'operand':token});continue
        for path in expand_braces(token):
            if any(c in path for c in '*?[') and not Path(path).is_file():
                excluded.append({**meta,'line':line,'reason':'glob-or-pattern','operand':path});continue
            result.append((path,program))
    return list(dict.fromkeys(result))

for meta in selected:
    cwd=Path(meta['session-metadata']['cwd']); roots=list((cwd/'related-systems').iterdir())
    if len(roots)!=1:raise RuntimeError(roots)
    root=roots[0]
    if str(root) not in catalogs:
        paths=subprocess.check_output(['git','-C',str(root),'ls-tree','-r','--name-only','HEAD'],text=True).splitlines()
        head=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
        catalogs[str(root)]={'head':head,'files':set(paths)}
    catalog=catalogs[str(root)]['files']
    # The launch prompt and completed top-level tool results are the visible-evidence proxy.
    prompt=Path(meta['path']).parent/'prompt.txt';history=prompt.read_text() if prompt.exists() else ''
    first_access=set();starts={};pending=defaultdict(list);root_starts={};complete=[]
    def add_attempt(path, tool, line, cid, parent, program=None):
        absolute=Path(path)
        try:rel=str(absolute.relative_to(root))
        except ValueError:return
        if absolute.is_dir():return
        # The MDCP --files operand is explicitly a directory-discovery root,
        # not a file guess. Existing directory operands are also outside this file census.
        if rel == 'skills/mdcp/scripts' and program == 'rg' and not absolute.exists():
            excluded.append({**meta,'line':line,'reason':'missing-directory-discovery-root','operand':path});return
        exists=rel in catalog
        if exists!=absolute.is_file():
            excluded.append({**meta,'line':line,'reason':'catalog-filesystem-disagreement','operand':path});return
        outer=parent or cid
        if parent:
            while starts.get(outer,{}).get('parentToolCallId'):outer=starts[outer]['parentToolCallId']
        # A single shell invocation can name a file more than once; count that target once.
        if any(x['absolute']==path and x['tool-call']==cid for x in pending[outer]):return
        named=any(re.search(r'(?<![\w./-])'+re.escape(spelling)+r'(?![\w./-])',history) for spelling in (rel,path))
        row={**{k:meta[k] for k in ('system','kind','role','launch','path')},'line':line,'tool-call':cid,'outer-call':outer,'tool':tool,'program':program,'relative':rel,'absolute':path,'exists':exists,'first-access':rel not in first_access,'previously-named':named,'root-call-line':root_starts.get(outer,line),'tool-is-error':None}
        row['previous-basename-cue']=bool(re.search(r'(?<![\w.-])'+re.escape(absolute.name)+r'(?![\w.-])',history))
        first_access.add(rel);rows.append(row);pending[outer].append(row)
    for n,line in enumerate(Path(meta['path']).open(),1):
        e=json.loads(line);kind=e.get('type')
        if kind=='tool_execution_start':
            cid=e['toolCallId'];starts[cid]=e;parent=e.get('parentToolCallId')
            if not parent:root_starts[cid]=n
            tool=e['toolName'];args=e['args']
            if tool=='read' and isinstance(args.get('path'),str):add_attempt(args['path'],'read',n,cid,parent)
            elif tool=='bash':
                for operand,program in shell_operands(args['command'],root,meta,n):add_attempt(operand,'shell',n,cid,parent,program)
        elif kind=='tool_execution_end':
            cid=e['toolCallId']
            for row in rows[-100:]:
                if row['launch']==meta['launch'] and row['tool-call']==cid:row['tool-is-error']=e.get('isError');row['end-line']=n
            if not e.get('parentToolCallId'):
                # Missing-path diagnostics are evidence of absence, not earlier positive naming.
                result=textcontent(e.get('result',{}));result='\n'.join(l for l in result.splitlines() if not any(s in l for s in ('No such file or directory','no such file or directory','ENOENT','FileNotFoundError')))
                history+='\n'+result
    snapshots.append({**meta,'source-root':str(root),'head':catalogs[str(root)]['head'],'last-line':n})

def stats(data):
    total=len(data);missing=sum(not x['exists'] for x in data)
    return {'attempts':total,'existing':total-missing,'missing':missing,'missing-percent':round(100*missing/total,3) if total else None,'sessions':len({x['path'] for x in data}),'systems':len({x['system'] for x in data})}
summary={'all':stats(rows),'by-tool':{},'first-access':{},'by-system':{},'exclusion-reasons':dict(Counter(x['reason'] for x in excluded))}
for tool in ('read','shell'):
    subset=[x for x in rows if x['tool']==tool];summary['by-tool'][tool]=stats(subset)
    for named in (False,True):
        data=[x for x in subset if x['first-access'] and x['previously-named']==named]
        summary['first-access'][tool+('-previously-named' if named else '-not-previously-named')]=stats(data)
for system in sorted({x['system'] for x in rows}):
    data=[x for x in rows if x['system']==system];summary['by-system'][system]={'all':stats(data),'first-unmentioned':stats([x for x in data if x['first-access'] and not x['previously-named']])}
summary['first-all']=stats([x for x in rows if x['first-access']]);summary['first-unmentioned']=stats([x for x in rows if x['first-access'] and not x['previously-named']]);summary['first-mentioned']=stats([x for x in rows if x['first-access'] and x['previously-named']])
summary['unmentioned-with-basename-cue']=stats([x for x in rows if x['first-access'] and not x['previously-named'] and x['previous-basename-cue']])
summary['unmentioned-without-basename-cue']=stats([x for x in rows if x['first-access'] and not x['previously-named'] and not x['previous-basename-cue']])
for name,data in [('attempts.json',rows),('excluded.json',excluded),('selection.json',snapshots),('summary.json',summary)]:
    (OUT/name).write_text(json.dumps(data,indent=2)+'\n')
print('OUT',OUT);print(json.dumps(summary,indent=2))
print('MISSING TARGETS')
for row in rows:
    if not row['exists']:print(row['system'],row['role'],row['tool'],row['launch'],row['line'],row['relative'],'FIRST',row['first-access'],'NAMED',row['previously-named'])
Path('/tmp/commonplace-path-base-rates-latest-path.txt').write_text(str(OUT)+'\n')
