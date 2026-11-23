import pathlib, random, json, sys, re
S=pathlib.Path(sys.argv[1]); M=S/"materials"
REASON=re.compile(r"\s+The (operator's )?reason:\s+the definition should be general and continuous, so that a small change\s+to how a system judges does not move it out of the term\.")
before=(M/"draft-definition.md").read_text()
after=(M/"draft-after-raw.md").read_text()
# the later draft: two phrases that name the operator made neutral, as in experiment 2
a2=after.replace("The operator's reason:","The reason:",1)
a3=re.sub(r"The operator ruled that\s+being open to criticism","Being open to criticism",a2,count=1)
assert a2!=after and a3!=a2
after=a3
drafts={"R+":{"before":before,"after":after}}
bm,n1=REASON.subn("",before); am,n2=REASON.subn("",after)
assert n1==1 and n2==1,(n1,n2)
drafts["R-"]={"before":bm,"after":am}
for arm,d in drafts.items():
    for k,v in d.items(): (M/f"draft-{k}-{'plus' if arm=='R+' else 'minus'}.md").write_text(v)
def f(n,text): return f"\n\n===== FILE: {n} =====\n\n{text}"
note=f("on-balance-judgments-can-guide-improvement-without-a-global-measure.md",(M/"on-balance-note.md").read_text()); checks=f("definition-checks.md",(M/"definition-checks.md").read_text())
assert not REASON.search(note) and not REASON.search(checks)
W_head="You are reviewing a draft definition written for a knowledge base about agent-operated knowledge systems. The draft names the learning process the project works on. It is meant to cover all the learning that happens in the project's own system. Three files follow: the draft, a file of checks that places cases against it, and a note the draft relies on. All three are working drafts by the same authors and none is settled: the expected placements in the checks and the text of the note may be changed along with the definition. Links to other files will not resolve."
W_task="Propose the three changes that you consider most important, most important first. A change may alter the definition, the checks, the note, or several of them together. For each, say what you would change and give your reason in at most three sentences."
WG2="Prefer the most general definition that still does its job. A feature that separates some systems from others can be a named kind or a reported property instead of a condition of membership."
C_head="You are advising on a definition written for a knowledge base about agent-operated knowledge systems. The definition names the learning process the project works on. Two versions of the draft follow, and a note both rely on. A file of checks written for one of the versions also follows. The checks file and the note are working drafts and can be changed to fit whichever version is adopted. Links to other files will not resolve."
C_task="Say which version the project should adopt, and give your reasons in at most five sentences. Then name the one thing in the other version that you would keep."
runs=[]
for arm,d in drafts.items():
    for i in range(6):
        runs.append(("WG2",arm,i,W_head+"\n\n"+WG2+"\n\n"+W_task+f("draft-definition.md",d["before"])+checks+note,{}))
    for i in range(6):
        fb=(i%2==0); v1,v2=(d["before"],d["after"]) if fb else (d["after"],d["before"])
        runs.append(("CW",arm,i,C_head+"\n\n"+C_task+f("Version 1",v1)+f("Version 2",v2)+note+checks,{"version1":"before" if fb else "after"}))
random.seed(2026112203); random.shuffle(runs)
(S/"prompts").mkdir(exist_ok=True); (S/"out").mkdir(exist_ok=True); key={}
for k,(c,arm,i,body,meta) in enumerate(runs,1):
    rid=f"w{k:02d}"; key[rid]={"condition":c,"arm":arm,"rep":i,**meta}; (S/"prompts"/f"{rid}.txt").write_text(body)
(S/"key.json").write_text(json.dumps(key,indent=1)); print(len(runs))
