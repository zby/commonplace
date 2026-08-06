# Workshop: Agent Harness Design

## Question

What must an agent harness provide around a bounded model call so the resulting system can complete useful work reliably, safely, and economically? Which properties are general requirements, and which are choices that only make sense for particular tasks, authority levels, or deployment settings?

## Why this workshop exists

The agent-memory work established a useful sequence: start from what future work needs, derive requirements and boundaries, and only then turn the stable comparison lens into a review type and writing workflow. Its durable results now include [Designing a Memory System for LLM-Based Agents](../../notes/designing-agent-memory-systems.md), the [agent-memory requirements](../../notes/agent-memory-requirements/README.md), the [agent-memory-system review type](../../agent-memory-systems/types/agent-memory-system-review.md), and the [review-writing skill](../../instructions/write-agent-memory-system-review/SKILL.md).

Harness coverage has reached the point where the same move is useful. [`kb/agentic-systems/`](../../agentic-systems/README.md) contains code-grounded analyses of execution loops, orchestration APIs, sub-agent surfaces, permission boundaries, recovery, and self-modification, but those analyses do not yet share a requirements-derived review contract. The collection contract already says that a mature harness methodology should follow the memory collection's path.

This workshop develops that methodology. It does not begin by standardizing the current reviews. First it must determine what outcomes a harness is responsible for, what failure modes expose missing machinery, and which distinctions support fair comparison across unlike systems.

## Working boundary

For this workshop, an **agent harness** is the operational system around one or more model calls that turns model judgments into situated work. The starting decomposition is [scheduler, context engine, and execution substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md), but the workshop may revise or extend it.

The boundary includes control flow, context assembly, tool and environment access, durable run state, delegation, permissions, recovery, observability, and human control. It also includes the interface to memory when the harness decides what retained material enters a call. It excludes the internal design of the memory subsystem, which remains covered by [`kb/agent-memory-systems/`](../../agent-memory-systems/README.md).

The workshop must distinguish the runtime that executes work from any builder or improvement plane that changes the harness. It must also distinguish a harness capability from a behavior that a particular application actually wires and uses.

## Current working material

- [Question map](./question-map.md) — initial scenarios, pressure areas, comparison tests, and open questions.
- [Agentic systems collection](../../agentic-systems/README.md) — current heterogeneous evidence base.
- [Agent runtime decomposition](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md) — starting component model, not a fixed conclusion.
- [Bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) — starting account of symbolic scheduling around semantic calls.
- [Agent orchestration occupies a multi-dimensional design space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — warning against ranking harnesses on one ladder.
- [Runtime structure determines governance control surfaces](../../notes/runtime-structure-determines-governance-control-surfaces.md) — starting account of how architecture constrains intervention and audit.

## Possible graduated artifacts

The analysis may earn some or all of these artifacts:

- a synthesis note explaining what an agent harness is for and what requirements follow;
- a small requirements inventory, split only where individual requirements are useful on their own;
- a code-grounded review type for `kb/agentic-systems/`;
- a local skill for writing or updating harness reviews;
- a comparison matrix or survey if repeated controlled fields prove useful.

These are possible outputs, not a required package. In particular, the workshop should not create a review schema until the fields discriminate real systems and change an architectural judgment.

## Working conventions

- Derive requirements from concrete work stories and observable failures, not feature catalogues.
- Keep unconditional requirements separate from scenario-dependent capabilities.
- Record whether a responsibility is supplied by the harness, delegated to the host application, or left to the model or operator.
- Separate capability from deployed behavior, and documented claims from code-grounded or first-hand evidence.
- Keep memory-system internals out of scope while recording the harness-side memory interface.
- Treat current review headings as evidence about useful questions, not as a schema to preserve.

## What closes the workshop

The workshop closes when it has:

1. a requirements map grounded in several materially different work stories and their failure modes;
2. a clear boundary among model, harness runtime, host application, memory subsystem, and builder or improvement plane;
3. a comparison lens tested against heterogeneous systems in the current collection, including at least one interactive harness, one durable or distributed runtime, and one self-modifying or builder-oriented system;
4. an explicit account of which requirements are general, conditional, or externalized;
5. durable conclusions promoted to the appropriate library collections.

If those conclusions support a stable review type and writing skill, promote them too. If they do not, record why a shared methodology would erase important differences. Then remove this workshop and its entry from the active-workshop index.
