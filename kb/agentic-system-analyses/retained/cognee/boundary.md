---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Cognee's shipped memory platform at commit f154b32a9e544dac73e7ddf2010327cf9988edcd, with partial tracing of its memory-use loop."
run-id: AAS-2026-10-14-cognee-d8839fe03c5b-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: f154b32a9e544dac73e7ddf2010327cf9988edcd
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/topoteretes/cognee
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/cognee-d8839fe03c5b/related-systems/topoteretes--cognee
  revision: f154b32a9e544dac73e7ddf2010327cf9988edcd
  sha256: null
---

# Cognee boundary

## Boundary and evidence

This run analyses Cognee's shipped memory platform to explain how content becomes retained knowledge, how sessions and feedback maintain it, and how callers retrieve and reuse it. The target is a **memory/knowledge/context-engineering system**, not a claim that Cognee owns every consuming agent's execution loop. The public package exposes ingestion, knowledge processing, retrieval, memory maintenance and session APIs (SRC-1, `cognee/__init__.py`).

> This module exposes the main functions and objects intended for direct use
> through ``import cognee``. It groups the stable V1 API, memory-oriented V2 API,
> visualization helpers, tracing utilities, migration helpers, and session models
> behind a single package-level entrypoint.
> --- `cognee/__init__.py`

Cognee qualifies even though some routes need no generative LLM. The frozen documentation distinguishes local extraction and retrieval from generated answers, and implementation includes model-provider dispatch and model-facing maintenance instructions (SRC-1, `README.md`, `cognee/infrastructure/llm/LLMGateway.py`, `cognee/infrastructure/llm/prompts/session_distillation_curator_system.txt`).

> Text ingestion, retrieval, and session storage work without an LLM. LLM-dependent improvement stages skip automatically.
> --- `README.md`

> You are reading one slice of a finished working session and proposing durable lessons to persist into a knowledge graph. The slice is in chronological order and contains:
> --- `cognee/infrastructure/llm/prompts/session_distillation_curator_system.txt`

The functional boundary includes the Python library; its V1 and memory-oriented APIs; ingestion, extraction, code indexing, storage, authorization, retrieval and answer construction; sessions, feedback, distillation, improvement, deletion and migration; shipped prompts and maintenance instructions; and shipped CLI, HTTP, MCP, UI, starter-kit and example callers. Shipped evaluators and tests are also inside the source boundary as evidence of evaluation design and intended contracts. Packaging exclusions do not make repository-shipped callers external. Newly inspected material at this same commit remains SRC-1 evidence.

Initial tracing establishes permanent ingestion through `add` and `cognify`, session ingestion with an optional improvement bridge, retrieval from session and graph state, and stage-based maintenance (SRC-1, `cognee/api/v1/remember/remember.py`, `cognee/api/v1/recall/recall.py`, `cognee/api/v1/improve/improve.py`). The memory decorator retrieves context before invoking the wrapped function and persists a trace afterward (SRC-1, `cognee/modules/agent_memory/decorator.py`). These are source-level responsibilities, not observed successful operation.

> context.memory_context = await retrieve_memory_context(context)
> result = await fn(*args, **kwargs)
> --- `cognee/modules/agent_memory/decorator.py`

The shipped Company Brain driver belongs to the target's memory-use evidence: it sets storage roots, ingests text and code, distills a session and offers a separate invocation that queries saved memory. It is not excluded merely because it calls the library (SRC-1, `examples/cookbooks/company_brain/docs_code_conversations/company_brain_demo.py`). Its separate recall branch is explicit:

> if args.recall_only:
>     await recall_saved_memory(cognee)
>     return
> --- `examples/cookbooks/company_brain/docs_code_conversations/company_brain_demo.py`

The MCP client likewise belongs to the shipped interface boundary. Its recall implementation has both an HTTP route and a local Python call; its improve implementation forwards maintenance requests in either mode (SRC-1, `cognee-mcp/src/cognee_client.py`). The CLI's declared entry point and remember/recall command implementations were also located (SRC-1, `pyproject.toml`, `cognee/cli/commands/remember_command.py`, `cognee/cli/commands/recall_command.py`).

### Coverage and remaining loop limits

The boundary kind is **complete artifact, partial loop**. The complete repository artifact is pinned, but initial inspection does not establish whole-system coverage of every shipped state-producing and state-consuming path. In particular, frontend, connector, backend-worker and evaluator paths remain available but not substantively traced. This is an inspection limit, not an access gap. The run must not infer whole-system closure, uniform interface behavior or evaluation effectiveness from the central API trace alone.

| Shipped surface | Initial inspection and role | Conclusion currently prevented |
| --- | --- | --- |
| `cognee/__init__.py`, `cognee/api/v1/remember/remember.py`, `cognee/api/v1/recall/recall.py`, `cognee/api/v1/improve/improve.py` | Package exports read; selected ingestion, retrieval and maintenance branches read. The API directory tree was inspected. | Exhaustive behavior across all API routes, typed entries and alternate branches is not established. |
| `cognee/modules/agent_memory/decorator.py`, `cognee/modules/agent_memory/runtime.py`, `cognee/infrastructure/llm/LLMGateway.py` | Decorator invocation path read; runtime retrieval and persistence entry points located; structured-output dispatch read. | All consumer integrations and provider combinations are not established. |
| `cognee/infrastructure/llm/prompts/`, `cognee/modules/improve/` | Prompt and stage-module inventories inspected; curator instruction read; improve stage execution inspected through its API. | Admission, grounding and publication behavior require further tracing; a prompt alone does not establish enforcement. |
| `cognee/cli/`, `cognee-mcp/`, `cognee-starter-kit/`, `examples/` | CLI call sites searched; MCP server entry points searched and client recall/improve read; starter-kit pipeline calls searched; Company Brain driver read. | Parity across transports and all shipped caller lifecycles is not established. |
| `cognee-frontend/`, `cognee/api/v1/integrations/`, `cognee/modules/integrations/`, `cognee_db_workers/`, `kuzu/` | Available, not substantively traced. These remain included for inspection of UI, connector and storage responsibilities. | UI-driven state changes, connector scheduling, worker recovery and complete persistence semantics cannot yet be characterized. |
| `cognee/eval_framework/`, `evals/`, `tests/`, `cognee/tests/`, `notebooks/` | Evaluation-framework inventory and package test configuration inspected; evaluator implementations and run evidence not reviewed. | No comparative quality, benchmark reproduction, causal benefit or demonstrated reliability conclusion follows. |
| `docs/`, `deployment/`, `distributed/`, Docker and entrypoint files, configuration templates | Deployment and documentation locations inventoried; README deployment contract and package dependencies read. | Deployment-specific behavior and persistence guarantees need source tracing; documentation is declared intent. |
| Repository instructions, catalog, scripts, tools, CI and supporting assets | Available for relevance checks; not treated as governing this worker. | Their operational contribution is not characterized without further inspection. |

All rows describe SRC-1; repository paths are initially inspected evidence locations or explicit remaining inspection work, not additional source identities. No shipped material responsibility is excluded from later inspection at the pinned commit.

External model providers, model weights and their download services, database engine internals, Enola internals, separately hosted Cognee Cloud, and agent plugins or applications outside this repository are excluded implementations. The shipped adapters, configuration and interface calls remain included. Dependency declarations establish required integration surfaces, not external implementations (SRC-1, `pyproject.toml`); README links to a separate integrations repository do not freeze that repository (SRC-1, `README.md`). These exclusions prevent conclusions about provider accuracy, external service behavior, independently distributed plugin capture policies, and whether an arbitrary host actually uses recalled material to change its actions. The wrapped application function is not attributed to Cognee merely because the decorator invokes it.

The frozen source is the acquired Git object, unchanged: `https://github.com/topoteretes/cognee` at `f154b32a9e544dac73e7ddf2010327cf9988edcd`. Checkout HEAD was checked against that pin. The applicability cutoff is **2026-10-14**, the supplied run date. Only this revision supplies evidence; live documentation, linked repositories, releases and later changes are not frozen inputs. The overall tier is **code-grounded**. No target, example or test was executed and no provider was contacted. Initial evidence supports implementation and doctrine/design, not observed-run or causal-experiment claims.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/topoteretes/cognee` | f154b32a9e544dac73e7ddf2010327cf9988edcd | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/cognee-d8839fe03c5b/related-systems/topoteretes--cognee`. Implementation: top-level tracked tree; package export surface; selected remember ingestion/session bridge, recall session/graph and improve stage-loop branches; agent-memory decorator; structured-output gateway; MCP client recall/improve; CLI and starter-kit call-site searches; Company Brain saved-memory driver. Doctrine/design: complete README and package metadata; session-distillation curator prompt. Directory inventories record remaining inspection, not complete executable coverage. | Implementation: [public exports](https://github.com/topoteretes/cognee/blob/f154b32a9e544dac73e7ddf2010327cf9988edcd/cognee/__init__.py), [remember](https://github.com/topoteretes/cognee/blob/f154b32a9e544dac73e7ddf2010327cf9988edcd/cognee/api/v1/remember/remember.py), [recall](https://github.com/topoteretes/cognee/blob/f154b32a9e544dac73e7ddf2010327cf9988edcd/cognee/api/v1/recall/recall.py), [improve](https://github.com/topoteretes/cognee/blob/f154b32a9e544dac73e7ddf2010327cf9988edcd/cognee/api/v1/improve/improve.py), [decorator](https://github.com/topoteretes/cognee/blob/f154b32a9e544dac73e7ddf2010327cf9988edcd/cognee/modules/agent_memory/decorator.py), [gateway](https://github.com/topoteretes/cognee/blob/f154b32a9e544dac73e7ddf2010327cf9988edcd/cognee/infrastructure/llm/LLMGateway.py), [MCP client](https://github.com/topoteretes/cognee/blob/f154b32a9e544dac73e7ddf2010327cf9988edcd/cognee-mcp/src/cognee_client.py), [saved-memory driver](https://github.com/topoteretes/cognee/blob/f154b32a9e544dac73e7ddf2010327cf9988edcd/examples/cookbooks/company_brain/docs_code_conversations/company_brain_demo.py). Doctrine/design: [README](https://github.com/topoteretes/cognee/blob/f154b32a9e544dac73e7ddf2010327cf9988edcd/README.md), [package metadata](https://github.com/topoteretes/cognee/blob/f154b32a9e544dac73e7ddf2010327cf9988edcd/pyproject.toml), [curator prompt](https://github.com/topoteretes/cognee/blob/f154b32a9e544dac73e7ddf2010327cf9988edcd/cognee/infrastructure/llm/prompts/session_distillation_curator_system.txt). | No access gap encountered for inspected tracked files. External implementations and consuming hosts are outside the frozen source. Initial coverage is partial as listed above; uninspected available files are not access gaps. No execution evidence was inspected, so successful persistence, actual host reuse, quality and causal benefits are not established. |
