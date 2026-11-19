---
description: "What crosses the boundary between Commonplace workflow runs: durable outputs, the input version and authorized scope, and a record of effects already published."
type: types/note.md
tags: []
---

# Coordination between workflow runs

Commonplace uses a workflow invocation as the unit of coordination with an operator, another workflow or a separate process. The workflow owns its internal control flow. A recipient acts on a durable output without having to reconstruct which internal step should run next. When adding or changing a handoff, ask: **can a fresh process tell what it may do, to which version, and what has already happened?**

A run is not an all-or-nothing transaction. Under [the revise and rewrite stop contract](./adr/138-a-stop-ends-the-run-and-naming-its-output-is-the-approval.md), a revise run can publish an edit and then stop for a wording decision. The edit remains published even if nobody answers. If the operator does answer, a new run applies the approved proposals to the text they were made for. A restriction such as “the opening only” belongs in that handoff: naming the editing operation without its scope would authorize work on the whole note.

The design assumes that starting a fresh invocation is relatively cheap, not that repeating every judgment or effect is cheap or safe. [Review](./review-architecture.md) can reuse a finding while its inputs remain fresh; an earlier publication is a change to account for, not an instruction to publish again. This boundary does not prohibit internal recovery: a [gate sweep can resume its own interrupted work](./README-REVIEW-SYSTEM.md), and [an analysis workflow](./adr/118-analyses-run-as-a-workflow-over-headless-harnesses.md) can schedule its workers in code. Neither requires another workflow to interpret the scheduler’s private state.
