import pathlib, random, json, sys
S=pathlib.Path(sys.argv[1]); M=S/"materials"
def f(n,text): return f"\n\n===== FILE: {n} =====\n\n{text}"
orig=(M/"draft-definition.md").read_text()
note=f("on-balance-judgments-can-guide-improvement-without-a-global-measure.md",(M/"on-balance-note.md").read_text()); checks=f("definition-checks.md",(M/"definition-checks.md").read_text())
C_head="You are advising on a definition written for a knowledge base about agent-operated knowledge systems. The definition names the learning process the project works on. Two versions of the draft follow, and a note both rely on. A file of checks written for one of the versions also follows. The checks file and the note are working drafts and can be changed to fit whichever version is adopted. Links to other files will not resolve."
C_task="Say which version the project should adopt, and give your reasons in at most five sentences. Then name the one thing in the other version that you would keep."
runs=[]
for d in ["D1-1","D1-2","D2-1","D2-2","D3-1","D3-2"]:
    rev=(S/"eout"/f"{d}.txt").read_text()
    for i in range(4):
        fb=(i%2==0); v1,v2=(orig,rev) if fb else (rev,orig)
        runs.append((d,i,C_head+"\n\n"+C_task+f("Version 1",v1)+f("Version 2",v2)+note+checks,{"version1":"original" if fb else "revised"}))
random.seed(2026112205); random.shuffle(runs)
(S/"prompts").mkdir(exist_ok=True); (S/"out").mkdir(exist_ok=True); key={}
for k,(d,i,body,meta) in enumerate(runs,1):
    rid=f"y{k:02d}"; key[rid]={"draft":d,"candidate":d[:2],"rep":i,**meta}; (S/"prompts"/f"{rid}.txt").write_text(body)
(S/"key.json").write_text(json.dumps(key,indent=1)); print(len(runs))
