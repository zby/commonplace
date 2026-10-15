---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "AIDE2 workflow: an incumbent harness rewrite passes through task search, public review, private grading and successor selection."
run-id: AAS-2026-10-14-2609-26457-6b3bcd4791cf-01
reviewed-boundary: arxiv-2609.26457v1-2026-10-14
---

# AIDE2 workflow report

## Workflow account

### Selected workflow and evidence boundary

This account follows the principal experiment's harness-rewrite workflow, from the experiment's inputs to the returned best-grade research agent. It is representative because Algorithm 1 defines this nested procedure and §3.2 reports a complete trajectory using it. It includes a graded-rewrite rejection path. It is not a reconstructed trace of one particular proposal: SRC-1 supplies design and attributed operation, not raw worker messages, executable harnesses or run artifacts. The frozen paper and partial-loop boundary are fixed in [the boundary member](boundary.md).

The workflow uses the existing [RT-RTE-harness-admission](runtime.md#rt-rte-harness-admission) and [RT-RTE-inner-search](runtime.md#rt-rte-inner-search) records. The account separates reviewer interpretation from the task evaluator and from the outer admission decision. They have different consumers and consequences even though the paper describes them within one nested search.

### 1. Establish the request and baseline

The experiment supplies an initial harness, an outer agent, selection tasks, per-task dollar budgets and a trajectory length. This is a bounded optimization experiment, not an ordinary user's open-ended request. Algorithm 1 grades the initial harness before requesting rewrites. Human experimental design sets the tasks, metrics, models and constraints; the paper does not describe human approval of each generated rewrite. Authentication, launch arguments and a production delivery interface are uninspected (SRC-1 §2.1, Algorithm 1; [RT-RTE-harness-admission](runtime.md#rt-rte-harness-admission)).

### 2. Delegate a rewrite, then evaluate the resulting agent

AIDEhuman receives previously proposed agents and grades and edits the current incumbent. Its reviewer explores evaluation artifacts over several steps. The resulting proposal is an entire research-agent codebase, not a task solution or an approval decision. The fixed outer selector, rather than this proposer, decides whether it becomes incumbent (SRC-1 §§2.1–2.2; [RT-OBJ-agent-code](runtime.md#rt-obj-agent-code), [RT-RTE-harness-admission](runtime.md#rt-rte-harness-admission)).

The grading procedure runs the proposed harness on each selection task, beginning with that task's codebase. The inner harness receives public objective feedback and owns its editable next-candidate and final-return policies. Draft explores ideas, debug repairs execution errors, and improve refines promising candidates. AIDE0 selects a highest-scoring parent greedily; this is not a permanent rule for later rewritten agents (SRC-1 §2.2; [RT-RTE-inner-search](runtime.md#rt-rte-inner-search)). Thus delegation carries both inputs and a policy-bearing executor: changing the harness can change how the delegated task is organized.

### 3. Interpret execution feedback without confusing it with admission

The experimental executor runs solution scripts. The inner reviewer consumes execution outputs and extracts a score and relevant feedback for the ongoing search. The task's evaluator supplies the measurable outcome; reviewer interpretation is not an independent correctness oracle. The reviewer is not described as a separate human approval gate. The paper does not expose parse rules, complete prompts or what happens when score extraction is wrong (SRC-1 §2.2; [RT-RTE-inner-search](runtime.md#rt-rte-inner-search)).

Inner and outer review have different granularity:

> For the same reason, the inner-loop reviewer makes a single LLM call over each solution’s execution output, while the outer-loop agent’s reviewer explores the evaluation artifacts over several steps.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

This establishes a documented feedback handoff, not complete visibility of all artifacts. It does not establish a subprocess protocol, independent worker contexts or successful reviewer compliance.

### 4. Return task solutions and make the private-grade decision

When a task's budget is spent, its agent returns one candidate of its own choosing. Private held-out scoring consumes that returned candidate, not every solution in the search tree. Scores are averaged over tasks and independent repeated runs to produce the harness grade. The outer driver sees grades; the inner task optimizer is described as seeing public feedback rather than private selection outcomes. Hidden-data isolation cannot be verified from the capture (SRC-1 §2.1, Algorithm 1; [RT-CLM-private-signal](runtime.md#rt-clm-private-signal)).

The outer selection rule keeps the best graded agent. A public improvement is therefore insufficient for acceptance. The paper reports that about a quarter of graded rejected rewrites improved the agent-visible public signal but failed the private-grade comparison. This illustrates the consequence of separating optimization feedback from admission evidence, not proof that every rejected mechanism is intrinsically worse (SRC-1 appendix D; [RT-RTE-harness-admission](runtime.md#rt-rte-harness-admission)).

### 5. Recover from rejection and define delivery

A rejected rewrite does not replace the incumbent. The next proposal can still edit the best previously graded code. This is selection-level recovery owned by the fixed outer procedure, not evidence of filesystem rollback or process restart. Buggy proposals receive no grade in the reported trajectory; their diagnosis and retry protocol are unspecified. A wrongly accepted noisy proposal is a different failure: §5 warns that it can redirect subsequent search, and supplies no automatic correction procedure (SRC-1 §§2.1, 3.2, 5; [RT-RTE-harness-admission](runtime.md#rt-rte-harness-admission)).

At the trajectory limit, Algorithm 1 returns the highest-grade harness. During the run, accepted code becomes the next edit base and the research-agent harness used in subsequent evaluation. Those are the documented delivery and reuse boundaries; installation, packaging and deployment into a production service are not established (SRC-1 §2.1, Algorithm 1; [RT-BAP-incumbent-code](runtime.md#rt-bap-incumbent-code)). The paper reports seven accepted changes in its 100-node principal trajectory, but that attributed result does not verify executable handoffs or guarantee generalization outside selection ([RT-CLM-harness-improvement](runtime.md#rt-clm-harness-improvement)).

The separate held-out evaluation protocol can score a best available solution after a secondary constraint or context error ends search. That fallback is not silently substituted for Algorithm 1's ordinary budget termination, and does not establish resumable inner workers (SRC-1 appendix A; [RT-RTE-terminal-fallback](runtime.md#rt-rte-terminal-fallback)).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-inner-search](runtime.md#rt-rte-inner-search)

Workflow handoff: execution output crosses to a one-call reviewer; extracted score and feedback enter the next-step search decision. The returned task candidate crosses to private grading. Debug supplies documented local error repair, not a guarantee that a failed candidate becomes valid. Exact review parsing and recovery from misinterpreted output remain uninspected.

#### On [RT-RTE-harness-admission](runtime.md#rt-rte-harness-admission)

Workflow acceptance boundary: the outer reviewer supplies multi-step artifact inspection, while the fixed private-grade selector accepts or rejects the rewrite. Rejection preserves the incumbent as the next edit base. Terminal delivery is return of the highest-grade harness at the trajectory limit, not production deployment. Reviewer inspection, grade comparison and accepted-code reuse do not establish a general rollback or restart contract.
