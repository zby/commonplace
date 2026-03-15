---
description: Practitioner runtime taxonomies converge on three separable components — scheduler, context engine, and execution substrate — because each solves a different class of model limitation
type: note
traits: [has-external-sources]
tags: [computational-model, architecture]
status: seedling
---

# Agent runtimes decompose into scheduler context engine and execution substrate

Practitioner accounts often use one umbrella term for everything around the model: harness, runtime, agent system. That is useful rhetorically but too coarse for architecture. The parts grouped under that umbrella do different jobs, fail in different ways, and connect to different theoretical claims in this KB. The cleaner decomposition is:

- **Scheduler** — owns control flow, decomposition, and state progression across bounded calls. Answers: *what happens next?*
- **Context engine** — decides what enters each bounded call and in what frame. Answers: *what does this call get to see?*
- **Execution substrate** — provides the persistent and executable world outside the model: files, tools, sandboxes, versioned artifacts. Answers: *where do exact state and actions live?*

Not every system exposes these as neat modules; in many real systems the boundaries blur. The claim is that the functions are analytically distinct, and the distinction clarifies why practitioner taxonomies keep converging on similar component lists.

## Why the split matters

Once separated this way, several recurring confusions disappear. A filesystem is not a scheduler. Tool calling is not context engineering. AGENTS.md is not the execution substrate itself; it is a runtime artifact consumed by the context engine. Grouping all of these under one undifferentiated term hides the actual design tradeoffs.

Each component also maps to existing KB theory:

- The scheduler is formalized by the [bounded-context orchestration model](./bounded-context-orchestration-model.md): symbolic bookkeeping outside the model, bounded calls for judgment.
- The context engine is formalized by [context engineering](./context-engineering.md): routing, loading, scoping, and maintenance of bounded context.
- The execution substrate is grounded by [inspectable substrate, not supervision, defeats the blackbox problem](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) and [files beat a database for agent-operated knowledge bases](./files-not-database.md).

## Mapping the practitioner taxonomy

The [Anatomy of an Agent Harness ingest](../sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md) derives six practitioner components from model limitations: filesystem, bash, sandboxes, memory/search, context management, and long-horizon execution. Those map cleanly into the three-part decomposition:

| Practitioner component | Runtime component | Why |
|---|---|---|
| Long-horizon execution / Ralph Loop | Scheduler | Controls iteration boundaries, retries, branching, and progression across calls |
| Context management | Context engine | Compacts, scopes, and injects what each call sees |
| Memory/search | Context engine + execution substrate | Retrieval logic is context engineering; the stored artifacts live on the substrate |
| Filesystem | Execution substrate | Durable exact state outside the model |
| Bash / tool execution | Execution substrate | Deterministic actions outside the model |
| Sandbox / isolated environment | Execution substrate | Constrains execution and protects the outside world |

The source's "everything not the model" definition is descriptively useful but architecturally unstable — it names a perimeter, not a decomposition. The three-part split turns the perimeter into components with distinct responsibilities.

## Scheduler

The [bounded-context orchestration model](./bounded-context-orchestration-model.md) is already the formal treatment: symbolic bookkeeping outside the model, bounded calls for judgment. What this decomposition adds is positioning that model as one component of a larger runtime architecture, alongside the context engine and substrate it depends on.

This framing also clarifies why [unified calling conventions enable bidirectional refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) focuses on an imperative scheduler layer. That note is not about "the whole runtime" — it is about making the control-flow-owning component cheap to refactor as capabilities move between neural and symbolic implementations.

## Context engine

[Context engineering](./context-engineering.md) already decomposes this component into routing, loading, scoping, and maintenance. [Agent statelessness means the context engine should inject context automatically](./agent-statelessness-means-the-context-engine-should-inject-context-automatically.md) specializes one mechanism: reference-triggered loading.

The separation matters because many things attributed vaguely to "memory" are actually context-engine decisions. Retrieval, injection, frame construction, progressive disclosure, and compaction all concern bounded visibility, not durable storage. Durable storage is the substrate's job.

## Execution substrate

The execution substrate gives the system an inspectable world outside the model:

- **Persistent state** — files, indexes, versioned artifacts
- **Tool execution surfaces** — shell commands, deterministic helpers
- **Safety boundaries** — sandboxes, permission layers

Both the scheduler and context engine depend on exact external state. The scheduler needs somewhere to keep bookkeeping state. The context engine needs somewhere to retrieve from. Without an external substrate, both collapse back into flat conversation state.

Two existing notes ground this component from different angles:

- [Inspectable substrate, not supervision, defeats the blackbox problem](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — repo artifacts are governable in a way weights are not: they can be diffed, tested, reviewed, and reverted.
- [Files beat a database for agent-operated knowledge bases](./files-not-database.md) — files defer schema commitment while giving versioning, browsing, and agent access immediately.

Practitioner component lists place filesystems, bash, sandboxes, and versioned memory artifacts here. These are not mainly "reasoning aids." They are the environment in which reasoning becomes durable and actionable.

## Why independent sources converge here

The three sources analyzed in the practitioner trilogy ingests each emphasize different parts of the runtime, but the convergence is clearer under this decomposition:

- **[Lopopolo's report](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md)** emphasizes how constraints harden across the runtime — instructions, structural tests, cleanup agents. That improvement path runs through all three components but is most visible in the scheduler and substrate becoming more reliable over time.
- **[The cybernetics thread](../sources/harness-engineering-is-cybernetics-2030416758138634583.ingest.md)** frames the space as sensors, actuators, and feedback loops. That language cuts across all three components but especially clarifies the scheduler/substrate interface: the scheduler reads state from the substrate and writes decisions back to it.
- **Vtrivedy10's component taxonomy** provides the anatomy — the concrete pieces a runtime needs once you work backward from model limitations.

The KB already had the theory for the scheduler and context engine. What was missing was the runtime-level note connecting those theories as components of one architecture, and showing that remaining practitioner components cluster under execution substrate rather than floating as unrelated infrastructure.

## Scope limits

This is a decomposition, not a claim that these three components are the only ones that matter. Evaluation infrastructure, policy layers, and social workflows may deserve their own treatment. The point is narrower: the practitioner "harness" perimeter becomes much more usable once split into scheduler, context engine, and execution substrate.

It is also not a claim that every implementation must enforce hard module boundaries. A small system may collapse all three into one codebase. The analytical split still clarifies which theoretical arguments apply to which part.

---

Relevant Notes:

- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — formalizes: the scheduler component as symbolic control over bounded calls
- [context engineering](./context-engineering.md) — formalizes: the context engine as routing, loading, scoping, and maintenance
- [agent statelessness means the context engine should inject context automatically](./agent-statelessness-means-the-context-engine-should-inject-context-automatically.md) — specializes: reference-triggered loading as one context-engine mechanism
- [inspectable substrate, not supervision, defeats the blackbox problem](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — grounds: why repo artifacts and exact state belong to a separate substrate component
- [files beat a database for agent-operated knowledge bases](./files-not-database.md) — grounds: why the substrate is often filesystem-first early on
- [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — extends: runtime constraints mature differently across layers, which becomes clearer once the runtime is decomposed
- [unified calling conventions enable bidirectional refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — exemplifies: the scheduler layer as the control-flow-owning part of the runtime
- [Harness Engineering (Lopopolo, 2026)](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — evidence: practitioner report on runtime hardening through instructions, tests, and cleanup agents
- [Harness Engineering as Cybernetics (@odysseus0z, 2026)](../sources/harness-engineering-is-cybernetics-2030416758138634583.ingest.md) — evidence: control-theoretic framing for the scheduler/substrate feedback loop
- [The Anatomy of an Agent Harness](../sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md) — evidence: the practitioner component taxonomy this note reorganizes
