import pathlib, random, json, sys
S=pathlib.Path(sys.argv[1]); M=S/"materials"
def f(n,file): return f"\n\n===== FILE: {n} =====\n\n{(M/file).read_text()}"
note=f("on-balance-judgments-can-guide-improvement-without-a-global-measure.md","on-balance-note.md")
checks=f("definition-checks.md","definition-checks.md")
runs=[]
C_head="You are advising on a definition written for a knowledge base about agent-operated knowledge systems. The definition names the learning process the project works on. Two versions of the draft follow, and a note both rely on.{cs} Links to other files will not resolve."
C_task="Say which version the project should adopt, and give your reasons in at most five sentences. Then name the one thing in the other version that you would keep."
for code,cs,extra in (("C0","",""),("C1"," A file of checks written for the earlier version also follows.",checks)):
    for i in range(4):
        first_before = (i%2==0)
        v1,v2=("draft-definition.md","draft-after.md") if first_before else ("draft-after.md","draft-definition.md")
        body=C_head.format(cs=cs)+"\n\n"+C_task+f("Version 1",v1)+f("Version 2",v2)+note+extra
        runs.append((code,i,body,{"version1":"before" if first_before else "after"}))
A_head="You are reviewing a draft definition written for a knowledge base about agent-operated knowledge systems. The draft names the learning process the project works on. It is meant to cover all the learning that happens in the project's own system. Three files follow: the draft, a file of checks that places cases against it, and a note the draft relies on. Links to other files will not resolve."
L_task="List ten candidate changes to the definition, including ones you would reject. For each, state the change in one sentence and give a verdict, adopt or reject, with a one-sentence reason. Then name the three you would make."
for i in range(4):
    runs.append(("L",i,A_head+"\n\n"+L_task+f("draft-definition.md","draft-definition.md")+checks+note,{}))
M_head=A_head.replace("Three files follow: the draft, a file of checks that places cases against it, and a note the draft relies on.","Two files follow: the draft and a note the draft relies on.")
M_pairs='''Under the draft, the first system in each pair below is outside the definition and the second is inside.

1. A link repairer that keeps a patch exactly when its fixed validator passes. The same repairer together with a team that can change the validator after bad repairs.
2. A program that keeps a learned rule while one fixed formula estimates that the rule saves time, and drops it when the estimate turns negative. The same program together with the researcher who chose and can revise the formula.
3. A prompt search that keeps the variant scoring highest on a fixed benchmark. The same search with a step that can reject the score winner for a stated reason about future work.
4. A service that appends every interaction to a searchable log. The same service with a step that judges which entries to keep.
5. A team that weighs each change and never revisits a decision. The same team when later failures can lead it to revise a decision.

For each pair, say whether the difference between the two systems is one the term should mark, in one or two sentences. Then propose the three changes to the definition that you consider most important.'''
for i in range(4):
    runs.append(("M",i,M_head+"\n\n"+M_pairs+f("draft-definition.md","draft-definition.md")+note,{}))
random.seed(2026112103); random.shuffle(runs)
(S/"prompts3").mkdir(exist_ok=True); (S/"out3").mkdir(exist_ok=True); key={}
for k,(c,i,body,meta) in enumerate(runs,1):
    rid=f"t{k:02d}"; key[rid]={"condition":c,"rep":i,**meta}; (S/"prompts3"/f"{rid}.txt").write_text(body)
(S/"key3.json").write_text(json.dumps(key,indent=1)); print(len(runs))
