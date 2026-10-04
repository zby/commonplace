---
description: "Separates exact checking, acceptance authority, and repair-session placement; explains when worker-local feedback avoids a handoff and when a fresh context is justified."
type: types/note.md
traits: [title-as-claim, has-comparison]
tags: [computational-model, context-engineering]
---

# Acceptance authority does not require a separate repair session

A workflow can retain authoritative acceptance in its orchestrator while letting a worker check and repair its draft within its current session. This separation is possible when the worker may inspect the check's required inputs, the check can run without accepting the output, and repair remains within the worker's authority. The need for an enforced check does not itself require a new worker invocation for each correction.

Three decisions are distinct: which operations code performs exactly, who may authorize workflow progress, and which context should contain the next repair judgment. Moving checking into code settles the first decision, not the other two.

## Exact checking can be a worker capability

The [scheduler–LLM separation argument](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) motivates symbolic execution for fully specified operations. Comparing an identity field, resolving a reference, or matching a quotation need not consume model judgment. But symbolic execution does not require the orchestrator to be the only caller. A worker tool can invoke the same implementation.

The check reports the violated rule, the defect's location, and the information needed to repair it. Where an accepted value is determined, code can state it. Where several mechanically valid alternatives remain, code can enumerate them without deciding which serves the task. The worker interprets those results and revises its draft.

For example, a quotation checker can locate every exact occurrence of a passage. Choosing which occurrence supports a finding remains the author's judgment. A failed occurrence check may require revising the finding, not merely its citation.

Exposing that check does not transfer acceptance authority. The tool returns findings; it cannot mark the job accepted or release dependent work. As [cross-task transition policy remains scheduling behind tools](./cross-task-transition-policy-remains-scheduling-behind-tools.md), an interface's tool shape does not determine its authority. The relevant distinction is which transitions the implementation owns.

## Acceptance remains a separate operation

A worker-local route is:

```text
draft → check → judge the feedback → revise → check → submit
```

The orchestrator then checks the submitted output and accepts or refuses it. It retains dependency enforcement, attempt limits, and decisions about retrying, blocking, or advancing.

Both callers can use one checking implementation. Their results agree when the draft bytes, checking rules, and relevant context inputs are identical. A local pass cannot guarantee later acceptance if any of those inputs changes. Acceptance therefore checks the submitted bytes against its authoritative context rather than trusting the worker's report that a check passed.

This is reuse of an evaluator, not independent verification. Repeating a deterministic check enforces its predicate at two boundaries; it does not provide a second assessment of whether that predicate is sufficient or whether the findings are sound.

## A repair boundary should earn its context cost

Orchestrator-mediated repair instead follows:

```text
submit → refuse → prepare a handoff → invoke a worker → reconstruct context → revise
```

If the next worker is only meant to continue the author's correction work, this route introduces a handoff without introducing a new analytical role. The draft survives, but source selections, unresolved alternatives, and reasons for particular choices must be supplied, reread, or reconstructed. In-session feedback makes a separate repair handoff unnecessary while that working context remains useful.

This is a [context-engineering](./definitions/context-engineering.md) question: how knowledge reaches and remains available to bounded model calls. A session is a sequence of calls with retained or reassembled context, not one unbounded call. The [bounded-context orchestration model](./bounded-context-orchestration-model.md) represents qualifying workflows but does not rank their decompositions. It does not require each tool check to become an outer workflow transition.

Nor does continuity justify retaining everything. Since [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md), the reason to preserve a repair session is useful task context, not the identity of the agent or the existence of its transcript. Stale reasoning and repeated failure messages can make that context worse than a fresh assembly.

The conditional cost hypothesis is that worker-local checking reduces completion effort when repair fits the remaining usable context, relevant knowledge is already available there, and a fresh invocation adds no required isolation, capability, or independent judgment. The avoided handoff is a mechanism for savings, not proof of a net improvement.

## Scope

This division applies to revisable drafts whose checks can be exposed within the worker's authority. It does not imply that every repair belongs in the original session.

A fresh invocation has a distinct purpose when:

- Repair requires evidence or reasoning that no longer fits usable context. As [oversized semantic sub-goals become scheduling problems](./semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md), decomposition may be necessary.
- Independent review requires excluding the author's reasoning history.
- The next operation needs a different permission or capability surface.
- The original session has ended, become unreliable, or exhausted its budget.
- The failure changes the task's scope or requires a decision outside the worker's authority.

Checks that require inputs the worker may not read cannot simply be exposed unchanged. Checks with irreversible effects also need a separate inspection interface before they can serve as draft feedback.

Worker-local tools do not guarantee that a worker will call them or act on their results. Enforced acceptance and bounded failure handling remain necessary. If a worker submits invalid output, an orchestrator retry is still a legitimate fallback.

## How to test the cost hypothesis

Compare worker-local repair with orchestrator-mediated repair on the same task class, acceptance rules, source access, model, and overall resource budget. Count all checking calls, context loading, repair work, and orchestration work through accepted completion or terminal failure. Keeping the gate fixed prevents fewer refusals from appearing to be an improvement when the contract was merely weakened.

Repeated cases in which fresh repair contexts achieve better accepted completion within the same budget would challenge the cost hypothesis. They would not show that acceptance authority logically requires a separate session. The structural separation and its practical value are different claims.
