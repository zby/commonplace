import pathlib, random, json, sys
S=pathlib.Path(sys.argv[1]); M=S/"materials"
files="".join(f"\n\n===== FILE: {n} =====\n\n{(M/f).read_text()}" for n,f in (("draft-definition.md","draft-definition.md"),("definition-checks.md","definition-checks.md"),("on-balance-judgments-can-guide-improvement-without-a-global-measure.md","on-balance-note.md")))
A_head="You are reviewing a draft definition written for a knowledge base about agent-operated knowledge systems. The draft names the learning process the project works on. It is meant to cover all the learning that happens in the project's own system. Three files follow: the draft, a file of checks that places cases against it, and a note the draft relies on. Links to other files will not resolve."
A_task="Propose the three changes to the definition that you consider most important, most important first. For each, say what you would change and give your reason in at most three sentences."
D1="Remove one condition or one exclusion from the definition. Say which one you remove, and give your reason in at most three sentences."
hints={"D2":"Each of your three changes must remove something from the definition. None may add a condition, an exclusion or a qualification.",
"D3":"Before proposing any addition, look for what can be removed. A definition usually improves more by losing a condition or an exclusion than by gaining one.",
"D4":"The term should be the general one. What distinguishes this project can be stated as a claim about a kind within the term, not as a condition of membership."}
runs=[("D1",i,A_head+"\n\n"+D1+files) for i in range(3)]
for c,h in hints.items():
    for i in range(3): runs.append((c,i,A_head+"\n\n"+h+"\n\n"+A_task+files))
random.seed(2026112102); random.shuffle(runs)
key={}
(S/"prompts2").mkdir(exist_ok=True); (S/"out2").mkdir(exist_ok=True)
for k,(c,i,body) in enumerate(runs,1):
    rid=f"s{k:02d}"; key[rid]={"condition":c,"rep":i}; (S/"prompts2"/f"{rid}.txt").write_text(body)
(S/"key2.json").write_text(json.dumps(key,indent=1)); print(len(runs))
