---
description: "Task families group obligations or evaluations; software product families group products through declared commonality, variability, and reusable production scope"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [foundations, computational-model, self-improving-systems]
---

# Task families and product families classify different things

A **task family** groups tasks because they share some relation relevant to solving, learning, or evaluation. A **software product or solution family** groups software products because they share declared commonality and variability that justify reusable family-level production machinery. The two classifications can overlap, but neither implies the other.

The distinction matters because Greenfield's [software-factory](./definitions/software-factory.md) identity depends on a product or solution family. A benchmark task grouping does not become a software-product family merely because one agent or evaluator handles all of its members.

## Different classification questions

| Classification | Primary members | Grouping relation | Why the relation matters |
|---|---|---|---|
| Task family | Requests, obligations, episodes, or problem instances | Shared skill, domain, input form, objective, operation, difficulty, evidence regime, or evaluation protocol | Supports comparison, curriculum design, coverage claims, or reuse of solving strategies |
| Product or solution family | Software systems or solutions | Declared commonality, variability, variants, constraints, architecture, and lifecycle production knowledge | Supports systematic reuse of schemas, assets, processes, tools, tests, and other production machinery |

A task family is often solver-relative. “Tasks requiring map-reduce over intermediate results” can group many domains and products because they stress the same computational strategy. A product family is producer-relative. “Tenant-configurable accounting services on one platform” groups products because a declared factory can reuse production knowledge across their anticipated variation.

## The axes cross in several ways

One product can generate many tasks. A long-lived repository may receive a sequence of bug fixes, feature additions, migrations, performance work, security reviews, and deployment changes. These are distinct software-production tasks or episodes, while the evolving repository may remain one family member.

One task family can range across many product families. “Add audit logging,” “upgrade a dependency,” or “repair a race condition” can be evaluated across unrelated repositories whose product-family machinery differs substantially.

One product family can require many task families. Requirements work, architecture design, code generation, testing, deployment, operation, maintenance, and migration have different task structures even when they contribute to members of the same product family.

A collection can satisfy both classifications. Repeated requests to configure and deploy variants of one declared service family may be both a task family and product-family work. That conjunction must be shown rather than assumed.

## Why the distinction is load-bearing

First, it prevents a post-hoc singleton factory. Solving one task and then declaring its output to be a one-member family does not demonstrate reusable family production knowledge. The family and the variation or reuse relation should be declared before the result is used as evidence for factory capability.

Second, it separates evaluation reach from factory scope. A system may perform well across a broad task family by using different manually supplied factories for each domain. That shows broad task performance, not acquisition of the family-specific production knowledge used by those factories. Conversely, a factory may support a rich product family while being evaluated on only a narrow set of tasks.

Third, it clarifies what is retained. A general task-solving heuristic may transfer across product families without becoming part of any one family's production knowledge. A family-specific schema or test suite may transfer across members of one product family while being useless elsewhere. Both are reusable, but their reuse scopes differ.

Fourth, it prevents decomposition from being smuggled into the benchmark. If tasks are grouped only after observing which decomposition worked, the grouping can hide failures outside the selected method's reach. Task-family selection and product-family definition should be independently inspectable.

## A task-family evaluation needs a declared frame

A longitudinal software-task assessment should declare more than an initial prompt. At minimum it should fix:

- the task-family membership or prospective sampling rule;
- the initial product state, including any repository and lifecycle artifacts;
- the objective and acceptance conditions;
- the evidence sources and user or environment interactions the solver may use;
- the horizon and resource limits; and
- how failures, timeouts, abstentions, retries, and requests for human rescue are counted.

The initial request need not be an exhaustive specification. Requirements, constraints, corrections, tests, telemetry, dependency changes, and user answers may arrive later when the declared interaction protocol permits them. What must remain fixed for the assessment is the rule governing those arrivals and their interpretation.

Changing the objective, acceptance relation, coverage rule, or allowed human help after seeing outcomes creates a different assessment frame. Otherwise a system can appear broad by silently dropping hard cases or by reclassifying an exported design decision as ordinary feedback.

This frame defines the evaluated task process; it does not turn the task family into a software product family. Product-family reuse still requires independently declared commonality, variability, and reusable production machinery.

## Mapping between the axes

A study that uses both concepts should declare:

1. the task-family membership or sampling rule;
2. the product-family commonality and variability being assumed;
3. which reusable machinery is general across task families, which is family-specific, and which is product-local;
4. whether evidence comes from repeated work on one product, multiple members of one product family, or products from several families; and
5. what transfer result would show reuse at the claimed level.

A held-out task can test task-family transfer. A distinct held-out product variant can test reuse of family production machinery. These are complementary controls, not substitutes.

## Scope

- Neither family concept requires a formal mathematical partition; both require an explicit enough membership relation to support the claim being made.
- Product families can evolve. A later factory revision may widen, narrow, or reorganize the admitted variation, but the change should not be hidden by relabeling products after evaluation.
- Task families may be defined by empirical similarity, institutional workflow, or benchmark construction. That does not make their relation identical to software-product-line commonality and variability.
- The distinction classifies scope. It does not by itself establish learning, improvement, or generality.

---

Relevant Notes:

- [Software factory](./definitions/software-factory.md) — grounds: makes a declared product or solution family part of factory identity
- [Factory development](./definitions/factory-development.md) — extends: changes reusable machinery for a product family rather than merely solving another task
- [An agentic substrate becomes a software factory through family-specific production machinery](./agentic-substrate-needs-family-specific-machinery-to-be-a-factory.md) — extends: uses the product-family boundary when mapping generic agentic machinery to a configured factory
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — compares: shows why a task grouping should not protect the decomposition used to define it
- [Program synthesis](../sources/program-synthesis-gulwani-polozov-singh-2017.ingest.md) — evidenced-by: shows why initial examples or natural-language instructions may require later interaction to discriminate intended behavior
