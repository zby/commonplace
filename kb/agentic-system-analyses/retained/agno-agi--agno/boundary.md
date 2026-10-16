---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Agno's Python SDK and AgentOS runtime at commit 00497422d4a386d93ab3b45c1a11faf42fcc932f, excluding terminal operations and infrastructure provisioning."
run-id: AAS-2026-10-13-agno-60e6e09dd4a6-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: subsystem-only
reviewed-boundary: "00497422d4a386d93ab3b45c1a11faf42fcc932f"
analysis-cutoff: "2026-10-13"
evidence-tier: code-grounded
source:
  identity: https://github.com/agno-agi/agno
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/agno-60e6e09dd4a6/related-systems/agno-agi--agno
  revision: "00497422d4a386d93ab3b45c1a11faf42fcc932f"
  sha256: null
---

# Agno boundary

## Boundary and evidence

This run characterizes the agent execution, orchestration and retained-state mechanisms of **Agno's Python SDK and AgentOS server runtime**. It supports source-grounded comparison of how agents build context, invoke models and tools, coordinate other agents, and retain and reuse sessions, memory, learning and knowledge. It does not characterize the entire Agno product platform or every package in the monorepo.

The target is in scope because it owns model-dependent execution rather than merely returning a tool result to another runtime. Its target class is `enclosing runtime`: the local Agent run implementation prepares messages and tools and issues the model call. Team and Workflow provide additional orchestration entry points. This is a `subsystem-only` boundary within the repository, not a claim of whole-monorepo coverage. AgentOS is included, not treated as an external caller. The shipped cookbook drivers and their prompts are also included as consumers and configuration evidence. SRC-1: `libs/agno/agno/agent/agent.py`, `libs/agno/agno/agent/_run.py`, `libs/agno/agno/team/team.py`, `libs/agno/agno/workflow/workflow.py`, `cookbook/00_quickstart/run.py`.

The runtime's model-call responsibility is visible in the inspected run path:

> model_response: ModelResponse = call_model_with_fallback(
>     agent.model,
>     agent.fallback_config,
> --- `libs/agno/agno/agent/_run.py:554-556`

The shipped AgentOS driver registers agents, a team and a workflow, obtains the app and serves it. AgentOS app construction includes database and optional scheduler and durable-queue lifespans. Its agent HTTP streaming adapter calls `agent.arun` and yields formatted run events. These are shipped runtime responsibilities inside this boundary, not responsibilities attributed to a hypothetical application. SRC-1: `cookbook/00_quickstart/run.py`, `libs/agno/agno/os/app.py`, `libs/agno/agno/os/routers/agents/router.py`.

> app = agent_os.get_app()
> --- `cookbook/00_quickstart/run.py`

> async for run_response_chunk in run_response:  # type: ignore[union-attr]
>     yield format_sse_event(run_response_chunk)  # type: ignore
> --- `libs/agno/agno/os/routers/agents/router.py`

Retained-state production and consumption belong inside the functional boundary. Initial inspection traced session loading through database/cache selection, and persistence through separate session and run writes. The shipped storage example enables history context with a stable session ID; the memory example teaches preferences in one session and requests recall in another under the same user ID. The knowledge example inserts a local document and gives its Knowledge object to an agent with search enabled. Those examples establish shipped usage, not successful observed recall. SRC-1: `libs/agno/agno/agent/_session.py`, `libs/agno/agno/agent/_run.py`, `cookbook/00_quickstart/agent_with_storage.py`, `cookbook/00_quickstart/agent_with_memory.py`, `cookbook/00_quickstart/agent_search_over_knowledge.py`.

> # Persist the session row and this single run (both O(1))
> _session.save_session(agent, session=session)
> _session.save_run(
> --- `libs/agno/agno/agent/_run.py`

The memory manager itself issues model calls with database tools. LearningMachine declares a unified interface for recall, processing, tool generation and maintenance; its detailed stores and curator remain available for later inspection. SRC-1: `libs/agno/agno/memory/manager.py`, `libs/agno/agno/learn/machine.py`.

> # Generate a response from the Model (includes running function calls)
> response = model_copy.response(
>     messages=messages_for_model,
>     tools=_tools,
> )
> --- `libs/agno/agno/memory/manager.py:1095-1099`

### Functional scope and exclusions

The following map distinguishes inclusion from initial inspection. Available but uninspected included code is not an access gap or evidence for its behavior.

| Paths | Treatment | Role and limit |
|---|---|---|
| `libs/agno/agno/` | Included | SDK and AgentOS implementation, including agents, teams, workflows, model/tool adapters, sessions and databases, memory, learning, knowledge, context, compaction, offload, skills, registry/factory, evaluation, tracing, approvals, guardrails, scheduling, queues, interfaces and remote clients. Initial inspection reached the entry points and state paths cited above; adapter and subsystem details await their assigned analyses. |
| `libs/agno/tests/`, `libs/agno/migrations/`, `libs/agno/scripts/`, `libs/agno/pyproject.toml` | Included | Runtime contracts, migration and development/evaluation context. Package metadata was inspected; tests and migration behavior were not yet inspected or executed. Their presence does not establish passed tests or operational outcomes. |
| `cookbook/` | Included | Shipped callers, prompts, ingestion/maintenance usage and evaluators, including AgentOS drivers. Initial inspection covered the quickstart storage, memory, knowledge, sequential-workflow and combined server examples. Other examples remain available, not excluded merely because they invoke library APIs. |
| `README.md` | Included | Product positioning and dependency/context declarations, not independent implementation or observed-run evidence. |
| `libs/agnoctl/` | Deliberately excluded after package-metadata inspection | Separate terminal client/operations package. Exclusion prevents conclusions about CLI-driven administration, client-side persistence or the complete operator control loop. The SDK's `agno` console entry points here, so it is not claimed as an SDK execution entry point. |
| `libs/agno_infra/` | Deliberately excluded after package-metadata inspection | Separate Docker/AWS infrastructure package. Exclusion prevents conclusions about provisioning, deployment orchestration and infrastructure state maintenance. |
| `.github/`, root `scripts/`, `.cursorrules`, `.editorconfig`, `.gitignore`, `AGENTS.md`, `CLAUDE.md`, `CODEOWNERS`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `LICENSE` | Deliberately excluded from behavioral characterization | Repository automation, contributor/coding-agent guidance and governance. Exclusion prevents conclusions about the repository's development-agent workflow, release process or CI results; it does not exclude prompts embedded in the shipped SDK and cookbook. |

The separate package boundaries and console-entry-point distinction are grounded in SRC-1: `libs/agno/pyproject.toml`, `libs/agnoctl/pyproject.toml`, `libs/agno_infra/pyproject.toml`.

> [project.scripts]
> agno = "agnoctl.main:app"
> --- `libs/agno/pyproject.toml`

External dependencies include model and embedding providers, database/vector-store services and their client libraries, tool-accessed services, FastAPI/Uvicorn and optional interface/telemetry integrations. The source includes their Agno-side adapters and configuration, not their independently implemented guarantees. SRC-1: `libs/agno/pyproject.toml`, `cookbook/00_quickstart/agent_search_over_knowledge.py`. The hosted AgentOS UI, online documentation and separately linked deployment-template repositories are outside the frozen source. The root introduction separates SDK, runtime and UI:

> - Build your agent platform using the Agno SDK.
> - Run your agent platform using the AgentOS runtime.
> - Manage everything using the AgentOS UI.
> --- `README.md`

Those external exclusions prevent conclusions about browser-side operation, deployed platform configuration, current online documentation and end-to-end service behavior. No model calls, target execution or tests were performed for this boundary. Consequently it supplies implementation and declared-intent evidence, not observed operation, reliability measurements or causal experiments. There is no identified source-access gap for the selected subsystem; material not yet inspected remains explicitly uninspected.

The frozen evidence is repository `https://github.com/agno-agi/agno` at commit `00497422d4a386d93ab3b45c1a11faf42fcc932f`. The acquired checkout's HEAD was verified against that pin. The applicability cutoff is the supplied run date, **2026-10-13**; it does not imply that later changes or a running deployment match this checkout. Overall evidence tier: `code-grounded`.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/agno-agi/agno` | 00497422d4a386d93ab3b45c1a11faf42fcc932f | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/agno-60e6e09dd4a6/related-systems/agno-agi--agno`. Implementation: bounded entry-point/run/persistence reads in `libs/agno/agno/agent/agent.py`, `libs/agno/agno/agent/_run.py`, `libs/agno/agno/agent/_session.py`, `libs/agno/agno/team/team.py`, `libs/agno/agno/workflow/workflow.py`, `libs/agno/agno/os/app.py`, `libs/agno/agno/os/routers/agents/router.py`, `libs/agno/agno/memory/manager.py`; quickstart callers in `cookbook/00_quickstart/run.py`, `agent_with_storage.py`, `agent_with_memory.py`, `agent_search_over_knowledge.py`, `sequential_workflow.py` under that directory. Doctrine/design: `README.md`, the three library `pyproject.toml` files, example instructions and `libs/agno/agno/learn/machine.py` interface documentation. Tracked top-level tree and SDK directory tree inspected for scope selection. | Implementation: [Agent dispatch](https://github.com/agno-agi/agno/blob/00497422d4a386d93ab3b45c1a11faf42fcc932f/libs/agno/agno/agent/agent.py), [run loop and persistence](https://github.com/agno-agi/agno/blob/00497422d4a386d93ab3b45c1a11faf42fcc932f/libs/agno/agno/agent/_run.py), [shipped server caller](https://github.com/agno-agi/agno/blob/00497422d4a386d93ab3b45c1a11faf42fcc932f/cookbook/00_quickstart/run.py). Doctrine/design: [root introduction](https://github.com/agno-agi/agno/blob/00497422d4a386d93ab3b45c1a11faf42fcc932f/README.md), [package metadata](https://github.com/agno-agi/agno/blob/00497422d4a386d93ab3b45c1a11faf42fcc932f/libs/agno/pyproject.toml). All local anchors above are relative to this commit. | No identified access gap in the selected subsystem. Deliberate exclusions: terminal client, infrastructure package, repository development machinery and external UI/services/templates. Implementation reads establish code paths, not successful executions; doctrine/design establishes stated contracts, not compliance. No observed-run or causal-experiment evidence was supplied or produced. |
