import pathlib, random, json, sys
S=pathlib.Path(sys.argv[1]); M=S/"materials"
def f(n,file): return f"\n\n===== FILE: {n} =====\n\n{(M/file).read_text()}"
mat=f("draft-definition.md","draft-definition.md")+f("definition-checks.md","definition-checks.md")+f("on-balance-judgments-can-guide-improvement-without-a-global-measure.md","on-balance-note.md")
conds={"D1":("1","Legible store"),"D2":("2","Judgment in the loop"),"D3":("3","Open to criticism")}
def cand(c):
    n,name=conds[c]
    return f'Remove condition {n}, "{name}", from the conditions of membership. Report it instead as a property that a learner may or may not have. Place again the cases that this condition alone put outside the term.'
head="You are advising on a draft definition written for a knowledge base about agent-operated knowledge systems. The draft names the learning process the project works on. It is meant to cover all the learning that happens in the project's own system. Three files follow: the draft, a file of checks that places cases against it, and a note the draft relies on. All three are working drafts by the same authors and none is settled: the expected placements in the checks and the text of the note may be changed along with the definition. Links to other files will not resolve."
runs=[]
for c in conds:
    for i in range(3):
        runs.append(("S1",c,i,head+"\n\nOne change to the definition has been proposed:\n\n"+cand(c)+"\n\nSay whether the project should adopt or reject this change. Begin with the single word Adopt or Reject, then give your reasons in at most five sentences."+mat,{}))
order=["D1","D2","D3"]
for i in range(4):
    o=order[i%3:]+order[:i%3]
    body="\n\n".join(f"Change {l}: {cand(c)}" for l,c in zip("ABC",o))
    runs.append(("S3","all",i,head+"\n\nThree changes to the definition have been proposed. They are independent: adopting one does not require adopting another.\n\n"+body+"\n\nGive a separate verdict on each change. For each, write the letter, then the single word Adopt or Reject, then your reasons in at most three sentences."+mat,{"order":o}))
for i in range(3):
    runs.append(("G","proc",i,head+"\n\nApply this procedure to the draft. List every condition of membership. For each one, write the change that removes it from the conditions of membership and reports it instead as a property that a learner may or may not have. Give no verdict on any of the changes."+mat,{}))
random.seed(2026112204); random.shuffle(runs)
(S/"prompts").mkdir(exist_ok=True); (S/"out").mkdir(exist_ok=True); key={}
for k,(c,cd,i,body,meta) in enumerate(runs,1):
    rid=f"x{k:02d}"; key[rid]={"condition":c,"candidate":cd,"rep":i,**meta}; (S/"prompts"/f"{rid}.txt").write_text(body)
(S/"key.json").write_text(json.dumps(key,indent=1)); print(len(runs))
