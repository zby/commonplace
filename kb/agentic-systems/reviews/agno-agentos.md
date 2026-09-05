---
description: "Whole-system analysis of Agno AgentOS as an open-source execution and control plane, distinguishing its runtime loops from the companion coding-agent and Studio builder loops"
type: kb/types/note.md
traits: [has-comparison, has-external-sources, has-implementation]
tags: [computational-model, tool-loop, self-improving-systems]
---

# Agno AgentOS

**Evidence basis:** first-hand reading on 2026-08-03 of the Apache-2.0 `agno-agi/agno` checkout at commit [21d274d6](https://github.com/agno-agi/agno/commit/21d274d63052a229fccd6b2621ea2a7da8eb1527) and the Apache-2.0 `agno-agi/agent-platform-railway` reference-platform checkout at commit [6fe7af1b](https://github.com/agno-agi/agent-platform-railway/commit/6fe7af1bb11162b6aa46e68e43b74b3599a6e1c4), covering the framework execution paths, AgentOS application and routers, workflow controls, scheduler, authorization, Studio tools, reference agents, evals, and coding-agent skills. I did not run a live deployment.

Agno is usefully analysed as an agentic system, but not as one homogeneous loop. The core repository contains a framework for model/tool agents, multi-agent teams, deterministic and agent-triggered workflows, plus AgentOS: a FastAPI execution and control plane that adds persistence, streaming, scheduling, approvals, evaluation, tracing, authentication, interfaces, and dynamic component management. The separate reference platform then supplies two builder loops over that substrate: an Agent Builder that creates versioned components through constrained Studio tools, and an external coding agent that edits Python, restarts the container, probes behavior, and runs regression evals.

That separation is the central architectural fact. AgentOS is not intrinsically a recursively self-improving agent. It is an unusually broad runtime on which an improvement system can be assembled. The advertised auto-improvement path belongs to the repository-development environment and inherits the coding agent's filesystem, Docker, and git authority rather than AgentOS's runtime RBAC.

## Three execution layers

### Agent and team model loops

An `Agent` is the ordinary model/tool loop. Its behavior is assembled from a model, instructions, tools, context providers, session history, knowledge and memory settings, hooks, guardrails, and structured-output controls. A database can persist sessions and runs; an AgentOS-level `checkpoint` policy can additionally place recovery boundaries at runs, tool batches, or individual tools. AgentOS does not require its native implementation: the minimal [`AgentProtocol`](https://github.com/agno-agi/agno/blob/21d274d63052a229fccd6b2621ea2a7da8eb1527/libs/agno/agno/agent/protocol.py) is an id, optional name, and asynchronous run method, allowing external-framework adapters to enter the same HTTP surface.

A `Team` puts another model loop above agents or nested teams. Its four explicit modes are coordinate, route, broadcast, and tasks. Coordinate lets the leader choose members, formulate delegated tasks, and synthesize results; route returns a selected member's response; broadcast calls every member; tasks gives the leader a persistent task list and task-management tools, bounded by `max_iterations` ([team modes](https://github.com/agno-agi/agno/blob/21d274d63052a229fccd6b2621ea2a7da8eb1527/libs/agno/agno/team/mode.py), [task-tool selection](https://github.com/agno-agi/agno/blob/21d274d63052a229fccd6b2621ea2a7da8eb1527/libs/agno/agno/team/_tools.py)). The scheduler inside these modes is still the leader model: framework code supplies the action vocabulary and iteration cap, while the model chooses decomposition and delegation.

### Workflow control flow

`Workflow` supplies a different orchestration regime. Python lists and callables compose agents, teams, functions, nested workflows, sequential groups, parallel branches, conditions, routers, and bounded loops. Conditions and routers may use Python callables or Common Expression Language expressions; a workflow may also have a `WorkflowAgent` that decides when to invoke it ([workflow object](https://github.com/agno-agi/agno/blob/21d274d63052a229fccd6b2621ea2a7da8eb1527/libs/agno/agno/workflow/workflow.py), [loop](https://github.com/agno-agi/agno/blob/21d274d63052a229fccd6b2621ea2a7da8eb1527/libs/agno/agno/workflow/loop.py), [router](https://github.com/agno-agi/agno/blob/21d274d63052a229fccd6b2621ea2a7da8eb1527/libs/agno/agno/workflow/router.py)).

This is not merely a visual graph abstraction. The host language remains the practical scheduler: it determines ordering, parallelism, branch eligibility, retry and error behavior, and maximum iteration counts. Models enter as executors or selectors only where the author places them. The result is a useful orchestration ladder rather than a forced choice between deterministic pipelines and free-running agents.

Human review is integrated into that control flow. Steps, loops, conditions, and routers can pause before execution, after outputs, after each iteration, on errors, or for user route selection; rejection can skip, retry with feedback, choose an else branch, or cancel. Paused run requirements are stored so the run can later continue, and AgentOS has a separate approval record and resolution API for externally resolved tool approvals ([workflow review types](https://github.com/agno-agi/agno/blob/21d274d63052a229fccd6b2621ea2a7da8eb1527/libs/agno/agno/workflow/types.py), [approval enforcement](https://github.com/agno-agi/agno/blob/21d274d63052a229fccd6b2621ea2a7da8eb1527/libs/agno/agno/run/approval.py)). These are operative gates, not just prompt requests, although their safety still depends on authors placing them before the consequential operation.

### AgentOS control plane

`AgentOS` registers agents, teams, workflows, knowledge bases, and interfaces into one FastAPI application. The built-in surface includes run and continue endpoints, WebSocket streaming, sessions, memory and learnings, evals, metrics, knowledge, traces, database migration, schedules, approvals, service accounts, a component registry, and optional MCP and A2A interfaces ([application assembly](https://github.com/agno-agi/agno/blob/21d274d63052a229fccd6b2621ea2a7da8eb1527/libs/agno/agno/os/app.py)). This is a genuine execution plane: it normalizes unlike executors behind stable protocols and gives them shared state, observation, authorization, and lifecycle services.

The cron scheduler is database-coordinated rather than an in-process timer alone. A poller repeatedly claims due schedules, spawns asynchronous executions for each claim, and records attempts; the executor submits background agent, team, or workflow runs over the local HTTP API, polls their durable status, retries failures, treats a human-paused run as a terminal scheduler outcome, then releases the schedule with its next run time ([poller](https://github.com/agno-agi/agno/blob/21d274d63052a229fccd6b2621ea2a7da8eb1527/libs/agno/agno/scheduler/poller.py), [executor](https://github.com/agno-agi/agno/blob/21d274d63052a229fccd6b2621ea2a7da8eb1527/libs/agno/agno/scheduler/executor.py)). Database claiming supports multiple workers, but in-flight tasks are still process-local and cancelled during poller shutdown. The durable boundary is the claimed schedule and background run record, not the Python task itself.

## State, observation, and recovery

AgentOS persists the state needed to operate agents over time: sessions and run outputs, workflow session state, approvals, schedules and attempts, component versions, eval results, and traces. Agents and teams can receive session state and bounded history, search earlier sessions, and use Agno's memory, learning, and knowledge facilities. Those memory mechanisms are a substantial subsystem and are outside this whole-system review; the [Pal review](../../agent-memory-systems/reviews/pal.md) shows how one Agno application combines them with files, SQL, vector search, teams, and schedules, while also identifying which learning behavior remains hidden behind the framework boundary.

Recovery is deliberately tiered. Database-backed paused workflows can reconstruct step requirements and continue; approval records preserve who or what resolved a gate; background-run status lets clients and the scheduler reconnect after the initiating HTTP request. Agent checkpointing can narrow replay after a failure. Cancellation, by contrast, has an in-memory default manager, so process loss is not equivalent to durable cancellation propagation. AgentOS provides many restart and resume primitives, but it should not be described as a general exactly-once workflow engine: tool side effects remain as idempotent as the tool author makes them, and checkpoint granularity does not make an external mutation transactional.

Observability is correspondingly rich. Run events and tool calls can stream to clients; sessions and executor outputs can be stored; evaluations and traces have first-class APIs; OpenTelemetry tracing can be enabled across agents and teams. This gives an outer improvement loop much better diagnostic material than a final score alone. It does not itself interpret the trace, attribute a failure, or choose a repair.

## Authority is split between runtime and builder planes

The runtime plane has meaningful controls. JWT authorization fails at application construction if enabled without a verification key. Scopes distinguish read, write, delete, and run operations globally or for a particular agent, team, or workflow; service accounts and an internal scheduler token enter the same middleware; optional user isolation adds ownership scoping ([authorization setup](https://github.com/agno-agi/agno/blob/21d274d63052a229fccd6b2621ea2a7da8eb1527/libs/agno/agno/os/app.py), [scope map](https://github.com/agno-agi/agno/blob/21d274d63052a229fccd6b2621ea2a7da8eb1527/libs/agno/agno/os/scopes.py)). A significant caveat is that authorization is opt-in, user isolation is separately opt-in, and an authenticated route absent from the scope map is allowed by default. Custom interfaces therefore need correct declared mappings; authentication is fail-closed when requested without keys, but route authorization is not globally deny-by-default.

Tool authority remains component-local. An agent gets whatever tools its constructor or dynamic configuration grants, hooks and guardrails are author-selected, and approval gates only cover tools marked for confirmation. AgentOS supplies the control vocabulary, not a universal least-privilege policy.

The reference platform's Agent Builder demonstrates the narrower path well. Its public registry exposes a default model, shared database, documentation MCP, search, reasoning, two reference agents, and two small functions. Its instructions refuse secret access, `.env` reads, unrestricted writes, shell execution, and private tools. Mutating Studio calls require tool confirmation. New components are published as version one; later edits become drafts, published configurations are immutable, and a prior published version can be selected as current for rollback ([Agent Builder](https://github.com/agno-agi/agent-platform-railway/blob/6fe7af1bb11162b6aa46e68e43b74b3599a6e1c4/agents/agent_builder.py), [registry](https://github.com/agno-agi/agent-platform-railway/blob/6fe7af1bb11162b6aa46e68e43b74b3599a6e1c4/app/registry.py), [Studio tools](https://github.com/agno-agi/agno/blob/21d274d63052a229fccd6b2621ea2a7da8eb1527/libs/agno/agno/tools/studio.py)). This is a controlled runtime builder: it can assemble only registered capabilities, and approval sits on the mutation itself.

The coding-agent loop has a different authority envelope. Its `/improve-agent` skill reads a target's instructions and tools, derives golden-path, edge, tool-selection, and adversarial probes, calls the live container, inspects responses and Docker logs, edits `agents/<slug>.py`, restarts the API, and iterates up to five times. It advises using a feature branch but does not enforce a worktree, patch allowlist, or protected file boundary. The external coding harness supplies filesystem and Docker access; AgentOS sees only ordinary runs before the edit and a restarted component afterward ([improvement skill](https://github.com/agno-agi/agent-platform-railway/blob/6fe7af1bb11162b6aa46e68e43b74b3599a6e1c4/.agents/skills/improve-agent/SKILL.md)). Runtime RBAC therefore does not constrain the most powerful improvement actor.

## What the auto-improvement loop establishes

The reference platform has a real proposal-selection loop:

| Function | Placement |
|---|---|
| Failure discovery | The coding agent derives probes from the target's stated instructions and may incorporate user-named failure modes. The practitioner variant also mines stored usage sessions. |
| Candidate production | The coding agent classifies failures and changes one lever at a time: instructions first, then tools, context mode, model, history, or code. |
| Evaluation | Expected behavior, live responses, tool-call logs, and the coding agent's judgment reject candidates; a separate suite uses binary LLM-judge rubrics and tool-call assertions. |
| Operative retention | Accepted edits land in Python and become active after reload or container restart; git is recommended for rollback. Studio-created components instead retain immutable published versions in the database. |
| Stop rule | All generated probes pass, one failure repeats three times on the same lever, or five iterations elapse. |

The loop is diagnostically strong but epistemically closed around the target specification. The same `INSTRUCTIONS` supply both the behavior to test and the expected behavior used to judge it. Generated probes are selection cases, not an untouched test distribution. Rerunning only failed probes plus one or two earlier passes is a useful fast inner loop, but weak regression coverage. The companion `/eval-and-improve` skill closes part of that gap by rerunning committed profiles, refusing to weaken real assertions, distinguishing LLM-judge variance from regressions, and requiring the release profile to finish green ([eval skill](https://github.com/agno-agi/agent-platform-railway/blob/6fe7af1bb11162b6aa46e68e43b74b3599a6e1c4/.agents/skills/eval-and-improve/SKILL.md), [eval cases](https://github.com/agno-agi/agent-platform-railway/blob/6fe7af1bb11162b6aa46e68e43b74b3599a6e1c4/evals/cases.py)). At the pinned commit the suite contains a small hand-authored set for three reference agents, not the hundreds of independently held-out probes suggested in the practitioner report.

This is convergent hardening, not evidence of compounding recursive self-improvement. The target agent changes; the coding agent, probe derivation method, target specification, judge policy, iteration cap, framework architecture, and permissions remain supplied. Broad repository access establishes technical writability, but the observed path primarily tunes target instructions and wiring. Because [a repeatable operative path keeps a redesign class open to revision](../../notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md), a stronger claim would need later evidence reaching a represented and authorized redesign path for the improvement machinery itself.

There are nevertheless two legitimate self-improvement boundaries. If the target is assessed alone, another agent improves it. If the coding agent, skill, target, runtime, evaluator, repository, and retained edits are declared as one human-inclusive development system, that composite improves one of its operative components. Neither boundary shows that AgentOS core improves itself, and neither supports an open-ended capability-growth claim.

## Architectural assessment

AgentOS's strongest design is separation without isolation. Model loops, team supervision, host-language workflows, cron activation, approval state, durable runs, component versions, evaluation, and observability are distinct mechanisms that can be combined without pretending one abstraction solves every orchestration problem. `AgentProtocol`, remote entities, MCP, A2A, and configurable interfaces make the control plane broader than an Agno-only agent class.

Its central tradeoff is that policy remains highly author-composed. This is appropriate for a framework, but it limits security claims about applications built with it. Operators choose whether authorization and user isolation exist, authors choose tool sets and approval placement, custom routes must enter the scope map, and external side effects inherit tool semantics. The reference platform is safer because it chooses a constrained registry and confirmation list, not because every AgentOS deployment gets those properties automatically.

The ecosystem's two builder paths are complementary:

- **Studio Builder:** narrow capability registry, human confirmation on mutations, database versions, immutable published configurations, immediate rollback. It can safely compose what the registry already knows, but the pinned reference agent deliberately does not trial-run a newly created component unless asked, so wiring validation is stronger than behavioral validation.
- **Coding-agent builder:** broad source-level expressiveness, live probes, logs, restarts, and full regression profiles. It can add capabilities and repair implementation defects that Studio cannot express, but its permissions and change safety come from the external coding harness and git workflow rather than AgentOS controls.

The important future design question is not whether to merge them. Their different authority is useful. It is whether a controlled promotion path can connect them: diagnose from production traces without leaking private data, propose source or component changes in an isolated candidate, evaluate on held-out and adversarial cases, require an authority appropriate to the capability change, publish a version, canary it, and roll back while preserving the failed attempt. AgentOS already supplies many of the nouns—traces, evals, approvals, versions, schedules, and durable runs—but the reference platform does not yet assemble that complete production loop.

## What to watch

- Whether component creation gains mandatory behavioral canaries rather than treating validated wiring and stored instructions as sufficient for version one.
- Whether generated improvement probes are separated into selection and held-out sets, with judge prompts, outcomes, costs, and variance retained for audit.
- Whether production-session mining receives explicit privacy, sampling, provenance, and contamination controls.
- Whether runtime authorization changes from allow-on-unmapped routes to an auditable deny-by-default policy, especially for custom interfaces and future routers.
- Whether coding-agent improvement gets an enforced mutable-path boundary, isolated candidate deployment, full regression before promotion, and automatic rollback.
- Whether the improvement skill itself, its evaluators, or its editable-surface policy ever enter a demonstrated operative redesign path rather than merely remaining source files a powerful coding agent could edit.

---

Relevant Notes:

- [How to Recursively Improve Your Agents](../../sources/how-to-recursively-improve-your-agents-2084301728363462919.ingest.md) — evidenced-by: captures the affiliated practitioner's broader loop and effectiveness claims, whose architecture is partly inspectable in the reference platform but whose reported result is not independently reproduced
- [A repeatable operative path keeps a redesign class open to revision](../../notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) — rests-on: distinguishes broad code writability from demonstrated revision of the improvement machinery itself
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — rests-on: supplies the functional decomposition used for the coding-agent improvement loop
- [Diagnostic richness constrains outer-loop learning quality](../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — rests-on: explains the value of responses, tool calls, traces, errors, sessions, and logs to the external repair loop
- [Warranted autonomy is bounded by oracle domain](../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) — rests-on: bounds what instruction-derived probes, LLM judges, reliability assertions, and wiring validation can safely authorize
- [The practical scheduler is the host language](../../notes/the-practical-scheduler-is-the-host-language.md) — rests-on: explains workflow composition and team control as host-code selection over bounded model calls
- [Pal](../../agent-memory-systems/reviews/pal.md) — see-also: shows how one Agno application composes framework memory, sessions, teams, schedules, files, SQL, and vector retrieval
- [Exo](./exo.md) — compares-with: Exo makes a protected substrate, rewritable executor, restart path, and preserved failure record part of one running system, while Agno's broad source-editing loop remains in an external coding harness
