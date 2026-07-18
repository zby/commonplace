---
description: "Swamp as an agent-facing automation control plane: typed resource models, declarative DAGs, remote workers, policy gates, and extension distribution."
type: kb/types/note.md
traits: [has-external-sources]
tags: [tool-loop]
---

# Swamp

**Evidence basis:** first-hand reading of the `swamp-club/swamp` checkout at commit [cf38c4e](https://github.com/swamp-club/swamp/commit/cf38c4ec1068613bb7d3432eb74a1ad854156dd7) on 2026-07-18, covering its agent integration, model and workflow domains, remote execution, access control, vaults, reports, audit path, extension system, and tests. I did not operate a live Swamp deployment.

Swamp is an agent-facing automation control plane, not primarily a memory system and not itself a general-purpose autonomous agent loop. A coding agent interprets the user's operational intent, discovers or authors typed integrations, and commits declarative models and workflows. Swamp then takes over the parts that benefit from stable semantics: validation, dependency scheduling, concurrency, permission checks, secret resolution, execution, data persistence, reporting, and audit. Its central move is to convert one agent-authored procedure into an inspectable symbolic artifact that can execute repeatedly without asking an LLM to reconstruct the procedure each time.

This boundary explains the product's breadth. Swamp combines an agent adoption layer, a typed resource/action model, a workflow runtime, an extension package ecosystem, a distributed executor, an operational data plane, and governance surfaces. The retained data reviewed separately as memory is one supporting subsystem inside that larger architecture.

## Agent At The Control Edge

`swamp repo init` installs tool-specific instructions and progressively disclosed skills for Claude Code, Cursor, OpenCode, Codex, Copilot, and Kiro. The generated rules force model discovery before implementation, prefer existing extensions and model types over shell bypasses, route the word "workflow" to Swamp's YAML workflow abstraction, require verification before destructive methods, and direct agents to reuse retained data through CEL rather than re-fetching it ([repo_service.ts](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/src/domain/repo/repo_service.ts), [skill_assets.ts](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/src/infrastructure/assets/skill_assets.ts)). This is more than command documentation: it is an adoption protocol that constrains how an otherwise general coding agent maps requests onto Swamp's abstractions.

The agent is nevertheless outside the execution kernel. Swamp does not need a model call to advance a workflow, enforce a check, resolve a dependency, or run a scheduled trigger. The LLM handles ambiguous interpretation and artifact authoring; the runtime handles repeatable control flow. That separation gives the agent a large operational action space without making every repeated action another probabilistic planning turn.

There are two authoring paths. Git-tracked definitions in `models/` are deliberate configuration objects with stable identity and reviewable YAML. Direct type execution instead accepts runtime inputs, routes them through schemas, and creates local auto-definitions as execution state. Both instantiate a model type and invoke a named method; they differ in whether configuration itself is a maintained repository artifact ([models.md](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/design/models.md)).

## Typed Operational Model

A model type represents an external API, CLI, or operational domain through schemas, methods, output specifications, checks, and optional reports. A definition binds that type to a named instance and global arguments. At execution, a method receives validated arguments plus a `MethodContext` through which it can write versioned resources and files, query prior data, resolve secrets, call another model, or decide a suspended workflow gate ([model.ts](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/src/domain/models/model.ts), [method_context.ts](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/src/domain/models/method_context.ts)).

The model boundary is both an integration API and a control boundary. Mutating methods can carry pre-flight checks for policy, dependency readiness, quota, or live-state validation. Cross-model calls have depth, cycle, and total-call limits; extension models must declare cross-extension dependencies; nested calls resolve their own vault context and record output lineage. These constraints make model composition more structured than arbitrary tool calling, though users can explicitly skip selected pre-flight checks and therefore remain part of the authority model ([models.md](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/design/models.md)).

CEL is the connective tissue between retained state and execution. Definitions and workflow inputs can resolve values from vaults, prior model data, workflow context, and other structured inputs. The result is a dataflow system in which symbolic references replace much of the value-copying and prompt-mediated handoff an agent would otherwise perform.

## Workflow Runtime

Swamp workflows are declarative DAGs of jobs and steps. A step can invoke a model method, invoke a nested workflow, or suspend at a manual approval gate. Jobs declare dependencies and conditions; jobs and steps are scheduled with a weighted topological sort for maximum available parallelism, while explicit concurrency caps bound fan-out against rate-limited systems ([workflow.md](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/design/workflow.md), [execution_service.ts](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/src/domain/workflows/execution_service.ts)).

The runtime persists enough state to behave as a resumable state machine rather than a fire-and-forget script. Workflow runs record job and step status, outputs, parent invocation context, approvals, failures, and cancellation. Scheduled and webhook triggers can start workflows without an agent present. Manual approval steps persist a gate token and suspend the run; a human command or model method can approve or reject it, after which the run is explicitly resumed. Approval provenance is populated by the runtime rather than accepted from extension code ([workflow.md](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/design/workflow.md), [models.md](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/design/models.md)).

This is the strongest sense in which Swamp is agentic infrastructure: it lets an agent author an operational policy once, then delegates repeated temporal coordination to a deterministic scheduler. The runtime can still call agent-backed or AI-backed model methods if an extension defines them, but its own orchestration semantics do not depend on an LLM.

## Distributed Execution And Capability Control

Remote execution separates a state-owning orchestrator from disposable workers. Workers dial out to the orchestrator, enroll with time-boxed credentials, advertise labels and platform information, and receive extension code with each dispatch. They carry no repository, datastore, vault configuration, or preinstalled extension state. The orchestrator retains the DAG, scheduler, definitions, extension bundles, locks, secrets, data, and audit trail ([remote-execution.md](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/design/remote-execution.md)).

Method code sees the same `MethodContext` locally and remotely. On a worker, its capabilities are proxy adapters: metadata operations travel over the control channel, bulk bytes use a separate HTTP/2 data plane, and durable writes land immediately at the orchestrator. This ports-and-adapters shape allows extension methods to remain execution-location agnostic while keeping the orchestrator as the authorization and audit chokepoint.

Swamp deliberately removes per-step execution-driver selection. A method either runs in-process on the orchestrator's loopback executor or in-process on a selected worker. Isolation is a deployment property of the worker: containerize the worker, place it on a GPU host, or run it in a restricted VM, then route work by labels and platform. This simplifies the execution contract, but it shifts sandbox correctness from workflow configuration to fleet provisioning.

The control protocol exposes read, write, run, and admin operations across data, models, workflows, vaults, reports, extensions, workers, and diagnostics. Grant-based access decisions match principals, actions, resource selectors, and optional CEL conditions; the `can-i` and `check` surfaces make authorization inspectable before execution ([grant_based_access_decision_service.ts](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/src/domain/access/grant_based_access_decision_service.ts), [access_handlers.ts](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/src/serve/handlers/access_handlers.ts)). The architecture is therefore capability-oriented at the worker boundary and policy-oriented at the client boundary.

## Extensions As The Scaling Unit

Extensions package models, workflows, vault providers, datastores, reports, skills, and supporting files under a collective-scoped identity. The registry supplies CalVer versions, release channels, metadata-only promotion, deprecation, dependency resolution, integrity checks, lockfile tracking, and update reporting. Pulled TypeScript is bundled and validated before use; lazy catalogs defer bundle loading until a named type is needed ([extension.md](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/design/extension.md)).

This package boundary connects the human/agent authoring surface to the deterministic runtime. A useful integration can carry not only executable code, but also the skills that teach an agent when to select it, the workflow templates that compose it, the vault and datastore adapters it needs, and reports that interpret its outputs. Swamp therefore distributes operational vocabulary and agent routing policy alongside implementation.

The trust model is substantial but not absolute. Collective identity, declared dependencies, archive checksums, path validation, release channels, and adversarial review directories constrain supply-chain risk. Installed extension code still executes with the capabilities exposed by its `MethodContext` and deployment environment, so registry trust and runtime grants remain load-bearing.

## Evidence, Reports, And Audit

Every model invocation and workflow run emits structured state and versioned outputs. Reports are post-execution functions at method, model, or workflow scope; they receive execution context and persisted data handles, then produce Markdown and JSON artifacts even for failed executions ([reports.md](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/design/reports.md)). This turns observability into an extension point rather than fixing one presentation layer into every model.

Swamp also records commands invoked by supported coding agents through tool-specific hooks. Normalizers convert each harness's hook payload into an append-only JSONL timeline, while diagnostics verify that the integration is alive ([audit.md](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/design/audit.md)). That audit path observes the outer agent session; workflow and model run records observe the deterministic inner runtime. Correlating both gives an operator a route from user request and agent commands to workflow execution and produced data, though the code does not prove that the agent's interpretation was correct.

Vaults complete the operational boundary. Providers resolve secrets lazily for definitions and methods, sensitive arguments and outputs can be marked for redaction or vault storage, refresh hooks can rotate short-lived values on read, and optional read-access audit records show which invocation retrieved a secret ([vaults.md](https://github.com/swamp-club/swamp/blob/cf38c4ec1068613bb7d3432eb74a1ad854156dd7/design/vaults.md)). Secrets remain centrally owned even when computation runs remotely.

## Reading Swamp As An Agentic System

Swamp's architecture is best understood as **agent-authored, runtime-executed automation**. It does not compete with coding agents on open-ended planning. Instead, it gives them a target language and runtime for operational work that should survive the current conversation. The agent supplies semantic judgment at design time; schemas, CEL, checks, grants, DAG scheduling, and method code progressively narrow that judgment into executable commitments.

That makes Swamp closer to an agent-oriented infrastructure-as-code and workflow platform than to a conventional tool-use harness. Its "tools" are typed domain models with data lineage and lifecycle. Its "plan" can become a versioned workflow. Its sub-execution surface is a distributed worker fleet rather than a sub-agent chat tree. Its feedback comes back as structured outputs, reports, telemetry, and audit evidence rather than only natural-language observations.

The main tradeoff is architectural weight. A one-off task can become a model type, definition, extension bundle, workflow, datastore record, report, and policy decision. Swamp mitigates this with direct type execution, generated agent skills, extension search, and reusable packages, but the system pays complexity to make automation repeatable, inspectable, distributable, and governable. It is strongest where those properties matter and weakest where a transparent shell command would genuinely remain one-off.

## What To Watch

- Whether agents reliably choose the right existing model and workflow abstractions rather than producing plausible but semantically wrong automation; structural validation cannot answer that selection question.
- Whether the grant model, worker capability proxies, and extension dependency declarations converge into one legible authority story for operators.
- Whether remote worker deployment profiles become explicit enough that isolation assumptions are reviewable rather than external fleet knowledge.
- Whether applications, environments, and drift detection move from the design roadmap into implemented control-loop primitives.
- Whether agent-command audit, workflow history, telemetry, reports, and data lineage can be queried as one causal execution trace without losing their distinct trust levels.

---

Relevant Notes:

- [Swamp memory-system review](../agent-memory-systems/reviews/swamp.md) - contains: the versioned operational data, retained definitions, progressive-disclosure skills, and agent read-back behavior analysed as Swamp's memory subsystem.
- [Scheduler-LLM separation exploits an error-correction asymmetry](../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) - rationale: explains why Swamp assigns repeatable DAG bookkeeping to a deterministic runtime after the agent authors the workflow.
