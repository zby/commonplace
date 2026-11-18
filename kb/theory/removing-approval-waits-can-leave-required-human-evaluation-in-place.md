---
description: "Separates removing a human approval wait from automating or retiring a specified evaluation task; optional assessment need not be part of either change"
type: types/note.md
traits: [title-as-claim, has-comparison]
tags: []
---

# Removing approval waits can leave required human evaluation in place

Removing a human approval wait and removing a specified evaluation task are different changes. Adoption may proceed without a person while the process specification still assigns monitoring or later revision decisions to one. A claim of full automation must say which tasks it preserves and which requirements it retires. Whether a specified task is useful or necessary is a separate question.

An actual wait prevents execution from proceeding until a person acts. A specified task can remain undone while execution continues. The first is a blocking dependency; the second is an unfulfilled requirement, not by itself evidence that the system would fail or degrade without the task. Optional assessment creates neither when the process can proceed without it and its specification does not require it.

This distinguishes human work within the process from optional assessment of its results, rather than deciding who deserves causal credit for an improvement. It complements [the comparison of a system before and after an adopted change](./a-better-factory-claim-compares-operative-states.md): a judgment that the system improved does not by itself show whether human evaluation was required to operate it.

## The same activity can perform different roles

Consider two hypothetical cases involving a new written procedure for an agent.

**Required approval.** An agent proposes the instruction, a maintainer examines test results, and the agent adopts it only after approval. The process depends on human intervention even if the maintainer always approves. Removing the wait leaves a separate question: what happens to the check? It might remain human work performed later, be replaced by an automated check, or be retired. Repeated acceptance does not settle that choice; [routine approvals do not establish that human judgment is dispensable](./routine-approvals-do-not-show-that-human-judgment-is-dispensable.md).

**Optional assessment.** The agent adopts the instruction under its existing rules. A week later, a maintainer examines the results to assess whether it helped. This is an optional study: neither adoption nor a required monitoring or revision task depends on it.

Both cases involve examining results and forming a verdict. Calling an activity evaluation does not tell us whether execution waits for it or the specification requires it. A non-binding recommendation still creates a dependency if the agent must wait for it. Conversely, a program can apply human-authored acceptance rules without requiring a new human judgment for each change.

## Name the process being automated

Suppose adoption is automatic, but the process specification assigns a maintainer a weekly sample review and rollback of harmful changes. Adoption continues if the maintainer does nothing, but the specified review goes undone. Calling the whole process automated would conceal an omitted task.

The same distinction applies to subsequent revisions. If the next revision requires the maintainer's assessment, that assessment is a dependency of the revision process, though not of the earlier adoption. Using an optional study's available findings does not itself require future studies. Making a new human assessment a condition of each revision does.

A claim about automated adoption alone need not include monitoring or revision. For the wider process, the account must say what work still requires a person and what changed: a check may have moved, been partly or wholly automated, been replaced by a different control, or ceased to be required. These changes can be combined. Retiring an unnecessary review may be justified, but it is a change in requirements, not automation of that review.

## Scope

- The distinction concerns required human intervention, not every human influence. Anticipated assessment can shape proposals without creating a human stop.
- A habitual wait for human input can block automation even without a written rule. It is an actual wait to remove, not evidence that the evaluation is needed to meet a stated requirement.
