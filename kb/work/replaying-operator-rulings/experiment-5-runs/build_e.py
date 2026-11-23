import pathlib, sys
S=pathlib.Path(sys.argv[1]); M=S/"materials"
def f(n,file): return f"\n\n===== FILE: {n} =====\n\n{(M/file).read_text()}"
mat=f("draft-definition.md","draft-definition.md")+f("definition-checks.md","definition-checks.md")+f("on-balance-judgments-can-guide-improvement-without-a-global-measure.md","on-balance-note.md")
conds={"D1":("1","Legible store"),"D2":("2","Judgment in the loop"),"D3":("3","Open to criticism")}
head="You are editing a draft definition written for a knowledge base about agent-operated knowledge systems. The draft names the learning process the project works on. Three files follow: the draft, a file of checks that places cases against it, and a note the draft relies on. Links to other files will not resolve."
for c,(n,name) in conds.items():
    task=f'The authors have decided to make this change to the definition:\n\nRemove condition {n}, "{name}", from the conditions of membership. Report it instead as a property that a learner may or may not have. Place again the cases that this condition alone put outside the term.\n\nWrite the whole revised draft definition that results, complete and consistent, as the authors would publish it. Carry the change through every part of the draft that depends on it. Keep everything the change does not touch. Do not judge the change, do not mark the draft as a proposal, and do not describe your edits. Output only the revised draft, starting with its title line.'
    for i in (1,2):
        (S/"eprompts"/f"{c}-{i}.txt").write_text(head+"\n\n"+task+mat)
print("ok")
