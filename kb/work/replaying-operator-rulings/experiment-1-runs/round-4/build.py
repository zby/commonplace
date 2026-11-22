import pathlib, random, json, sys
S=pathlib.Path(sys.argv[1]); M=S/"materials"
def f(n,file): return f"\n\n===== FILE: {n} =====\n\n{(M/file).read_text()}"
note=f("on-balance-judgments-can-guide-improvement-without-a-global-measure.md","on-balance-note.md"); checks=f("definition-checks.md","definition-checks.md"); draft=f("draft-definition.md","draft-definition.md")
W_head="You are reviewing a draft definition written for a knowledge base about agent-operated knowledge systems. The draft names the learning process the project works on. It is meant to cover all the learning that happens in the project's own system. Three files follow: the draft, a file of checks that places cases against it, and a note the draft relies on. All three are working drafts by the same authors and none is settled: the expected placements in the checks and the text of the note may be changed along with the definition. Links to other files will not resolve."
W_task="Propose the three changes that you consider most important, most important first. A change may alter the definition, the checks, the note, or several of them together. For each, say what you would change and give your reason in at most three sentences."
hints={"W0":"","WG2":"Prefer the most general definition that still does its job. A feature that separates some systems from others can be a named kind or a reported property instead of a condition of membership.","WG3":"A good definition is continuous: a small change to a system should not move it across the boundary, unless that difference is what the term exists to mark.","WD4":"The term should be the general one. What distinguishes this project can be stated as a claim about a kind within the term, not as a condition of membership.","WP2":"Consider whether a learner that keeps or drops changes by one fixed measure should be outside the definition."}
runs=[]
for c,h in hints.items():
    for i in range(3): runs.append((c,i,W_head+("\n\n"+h if h else "")+"\n\n"+W_task+draft+checks+note,{}))
C_head="You are advising on a definition written for a knowledge base about agent-operated knowledge systems. The definition names the learning process the project works on. Two versions of the draft follow, and a note both rely on. A file of checks written for the earlier version also follows. The checks file and the note are working drafts and can be changed to fit whichever version is adopted. Links to other files will not resolve."
C_task="Say which version the project should adopt, and give your reasons in at most five sentences. Then name the one thing in the other version that you would keep."
for i in range(4):
    fb=(i%2==0); v1,v2=("draft-definition.md","draft-after.md") if fb else ("draft-after.md","draft-definition.md")
    runs.append(("CW",i,C_head+"\n\n"+C_task+f("Version 1",v1)+f("Version 2",v2)+note+checks,{"version1":"before" if fb else "after"}))
random.seed(2026112201); random.shuffle(runs)
(S/"prompts4").mkdir(exist_ok=True); (S/"out4").mkdir(exist_ok=True); key={}
for k,(c,i,body,meta) in enumerate(runs,1):
    rid=f"u{k:02d}"; key[rid]={"condition":c,"rep":i,**meta}; (S/"prompts4"/f"{rid}.txt").write_text(body)
(S/"key4.json").write_text(json.dumps(key,indent=1)); print(len(runs))
