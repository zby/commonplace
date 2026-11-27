---
description: "Use a procedure-maintenance decision to distinguish when a fixed-weight selection loop needs its base LLM to interpret an instruction, diagnose a failure, or judge a trade-off."
type: types/note.md
tags: [self-improving-systems, improvement-loop, continual-learning, learning-theory]
---

# What a fixed-weight selection loop still needs from its base model

A fixed-weight LLM can change how it works by revising the procedures, hypotheses, and code it uses on later tasks. In [selection-based learning](./definitions/selection-based-learning.md), a proposed change takes effect only if an evaluation accepts it. Neither proposing nor selecting necessarily requires an LLM. Code can enumerate patches, run a decisive test, retain a passing patch, and roll it back if a regression appears.

What, then, must the base model contribute? Consider a system that maintains its own procedures. Its harness can record which procedure ran, replay a failing case, and enforce a context budget. Assume the frozen LLM is the only component available to interpret new prose, and no person intervenes during a decision. Three kinds of work can then fall to the model.

**1. Interpret a procedure when its application has not been encoded.** Suppose a procedure says, “Keep enough evidence for another maintainer to reconstruct why the change was accepted.” The harness can load that sentence and cap the record at 2,000 tokens. Neither operation determines which evidence matters in this case. If the maintainer needs to know why a passing alternative was rejected, a record of the winning test alone is insufficient. Once a rule specifies which comparison to retain, the harness can execute it. The model is needed where the instruction still has to be interpreted, not every time the rule runs.

**2. Diagnose a failure when diagnosis makes a repair reachable.** Suppose replay shows that the comparison is missing. If the harness can try every available logging configuration and a check recognizes an adequate record, the loop can fix the omission without explaining it. But suppose every configuration records only the accepted candidate. Searching those configurations for longer cannot recover a rejected candidate’s result. A model that traces the omission to the point where the alternatives are discarded can propose a different repair: capture the comparison *before* selection. The value of diagnosis here is specific. It identifies a candidate outside the current search. Diagnosis is not a logical prerequisite for every successful update.

**3. Judge a trade-off when the checks do not settle it.** Suppose one repair retains the comparison but exceeds the normal context budget; another stays within budget but omits the reason for rejection. If the budget is a hard limit, the harness can rule out the first repair. If it is a default that may yield to an audit requirement, the decision turns on the commitments that apply to this case. A model may be able to justify an exception or propose a shorter record that satisfies both. If the available evidence does not show what the maintainer needs to reconstruct, the warranted verdict may be to retain neither patch. Recognizing missing evidence is different from supplying it.

The same distinctions apply when the proposed change is to the store or to a check itself. Code can flag two procedures that always load together; that does not establish that one can replace the other. A model can propose a less costly audit check and judge it against the unchanged requirement that decisions remain reconstructible. Changing *that requirement* is a different decision. Authority to revise a check does not confer authority to discard the commitment it serves.

## Scope

These are distinctions among jobs, not evidence for three independent model faculties. One inference can serve more than one job: understanding why a comparison matters may both explain a failure and support a repair. Nor does a weakness of the model that executes tasks establish a weakness of the model that selects changes; they need not be the same model.

**The design question is therefore conditional:** for the changes this loop is expected to make, which decisions can its rules settle, which repairs can its search reach, and when may it decline to act? What remains is a concrete demand on the base LLM only if the loop must handle it autonomously and no other component can supply it. Meeting that demand makes those decisions possible; it does not guarantee sustained improvement.

---

Relevant Notes:

- [Selection-based learning](./definitions/selection-based-learning.md) — defined-in: why a loop with an automatic test can still learn by selection
- [Semantic work can be relocated, not eliminated](./semantic-work-can-be-relocated-but-not-eliminated.md) — grounds: why a demand on the loop need not be a demand on its base model
- [Diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) — grounds: which failure distinctions a proposer can recover from a trace
- [On-balance judgment with an LLM](./on-balance-judgment-with-an-llm.md) — extends: how to compare candidates when no encoded rule settles their trade-off
