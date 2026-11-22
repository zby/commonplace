import pathlib, random, json, sys
S=pathlib.Path(sys.argv[1]); M=S/"materials"
files="".join(f"\n\n===== FILE: {n} =====\n\n{(M/f).read_text()}" for n,f in (("draft-definition.md","draft-definition.md"),("definition-checks.md","definition-checks.md"),("on-balance-judgments-can-guide-improvement-without-a-global-measure.md","on-balance-note.md")))
A_head="You are reviewing a draft definition written for a knowledge base about agent-operated knowledge systems. The draft names the learning process the project works on. It is meant to cover all the learning that happens in the project's own system. Three files follow: the draft, a file of checks that places cases against it, and a note the draft relies on. Links to other files will not resolve."
A_task="Propose the three changes to the definition that you consider most important, most important first. For each, say what you would change and give your reason in at most three sentences."
hints={
"R0":"",
"G1":"Agents revising a definition tend to answer each concern by adding a clause, a condition or an exclusion. Give leaving the definition unchanged, making it more general, and removing a condition the same consideration as adding to it.",
"G2":"Prefer the most general definition that still does its job. A feature that separates some systems from others can be a named kind or a reported property instead of a condition of membership.",
"G3":"A good definition is continuous: a small change to a system should not move it across the boundary, unless that difference is what the term exists to mark.",
"G4":"For each condition and each exclusion, name a system it keeps out, and say what the definition would lose if that system were inside.",
"G5":"Review the draft as someone who will have to apply it to many systems built by other people.",
"P2":"Consider whether a learner that keeps or drops changes by one fixed measure should be outside the definition.",
}
B_head="You maintain a draft definition written for a knowledge base about agent-operated knowledge systems. The draft names the learning process the project works on. Three files follow: the draft, a file of checks that places cases against it, and a note the draft relies on. Links to other files will not resolve."
T="The draft is a note of the definition type. The type's specification governs your edit and follows.\n\n===== TYPE SPECIFICATION: definition.md =====\n\n"
types={"B0":"","BT1":T+(M/"type-old.md").read_text()+"\n\n===== END OF TYPE SPECIFICATION =====","BT2":T+(M/"type-new.md").read_text()+"\n\n===== END OF TYPE SPECIFICATION ====="}
B_obj='''A reviewer has raised this objection:

"Condition 2 defines deliberation by the absence of a fixed measure. Judging by reasons and being able to reconsider the criteria are two properties. A system can deliberate at length under a fixed objective. Proposed wording: retention 'through judgments about their expected contribution to future work, with those judgments open to criticism and revision'. Whether a system judges generally enough would then be a question of capability, not of membership."

Nobody else is available to decide. Say what you will do with the definition in response, and give the changed text of any passage you change. Give your reason in at most five sentences.'''
runs=[]
for c,h in hints.items():
    n=2 if c=="P2" else 3
    for i in range(n):
        body=A_head+("\n\n"+h if h else "")+"\n\n"+A_task+files
        runs.append((c,i,body))
for c,tc in types.items():
    for i in range(3):
        body=B_head+("\n\n"+tc if tc else "")+"\n\n"+B_obj+files
        runs.append((c,i,body))
random.seed(20261121); random.shuffle(runs)
key={}
for k,(c,i,body) in enumerate(runs,1):
    rid=f"r{k:02d}"; key[rid]={"condition":c,"rep":i}
    (S/"prompts"/f"{rid}.txt").write_text(body)
(S/"key.json").write_text(json.dumps(key,indent=1))
print(len(runs))
