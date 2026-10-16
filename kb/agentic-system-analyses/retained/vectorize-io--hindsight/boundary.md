---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Hindsight's memory service and shipped consumers at commit 610c135b6f2d0d8b972da94146ae635943f36271, with partial loop inspection."
run-id: AAS-2026-10-14-hindsight-34c2ca821edf-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "610c135b6f2d0d8b972da94146ae635943f36271"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/vectorize-io/hindsight
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/hindsight-34c2ca821edf/related-systems/vectorize-io--hindsight
  revision: "610c135b6f2d0d8b972da94146ae635943f36271"
  sha256: null
---

# Hindsight boundary

## Boundary and evidence

This run examines Hindsight as a memory/knowledge/context-engineering system. Its intended use is an evidence-grounded account of memory production, maintenance, admission and later consumption for design-space comparison. It does not evaluate Commonplace adoption or establish benchmark superiority.

The target is the repository artifact, not only its Python library API. Functional inclusions are the memory service, asynchronous maintenance, retained-state retrieval and reflection, shipped clients and embedded launchers, integration hooks, agent-facing instructions, administration and evaluators. A shipped caller remains inside the target when it selects content to retain or injects retrieved content into an agent's context. The external host's own model orchestration and task execution do not thereby become Hindsight responsibilities.

Hindsight's own declared purpose supports the memory-system classification (SRC-1, `README.md`):

> Hindsight™ is an agent memory system built to create smarter agents that learn over time. Most agent memory systems focus on recalling conversation history. Hindsight is focused on making agents that learn, not just remember.
> --- `README.md`

This classification is also code-grounded, rather than solely a reading of its branding. The packaged service exposes HTTP and optional MCP over a supplied memory engine (SRC-1, `hindsight-api-slim/hindsight_api/api/__init__.py`). The reflection implementation issues model tool calls itself (SRC-1, `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`):

> result = await llm_config.call_with_tools(**ct_kwargs)
> llm_duration = int((time.time() - llm_start) * 1000)
> queued_ms = int(queue_wait.seconds * 1000)
> consecutive_errors = 0
> --- `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`

The initial trace follows the packaged `hindsight-api` and `hindsight-worker` entry points into the memory engine and API construction. The worker imports the engine, initializes it with a worker task backend and constructs a poller; the service has separate HTTP/MCP construction paths. These are shipped runtime responsibilities, not an excluded enclosing application (SRC-1, `hindsight-api/pyproject.toml`, `hindsight-api-slim/hindsight_api/main.py`, `hindsight-api-slim/hindsight_api/worker/main.py`, `hindsight-api-slim/hindsight_api/api/__init__.py`). Pipeline inspection initially covers retain orchestration, the consolidation module's declared maintenance contract and reflection's executable model-call boundary; it is not an exhaustive trace of storage, admission or recovery.

A shipped Claude Code caller provides a concrete later-consumption path. Its hook manifest schedules recall on `UserPromptSubmit` and asynchronous retention on `Stop`. The retain script submits transcript content, a document ID, metadata and tags through its client. The recall script calls recall, formats returned results and emits context for the host (SRC-1, `hindsight-integrations/claude-code/hooks/hooks.json`, `hindsight-integrations/claude-code/scripts/retain.py`, `hindsight-integrations/claude-code/scripts/recall.py`):

> output = {
>     "hookSpecificOutput": {
>         "hookEventName": "UserPromptSubmit",
>         "additionalContext": context_message,
>     }
> }
> json.dump(output, sys.stdout)
> --- `hindsight-integrations/claude-code/scripts/recall.py`

This establishes a shipped injection interface, not evidence that a real host used the returned context or improved its decisions. The host runtime is an external dependency; the scripts and hook contract are included Hindsight evidence.

### Extent of inspection

The boundary kind is **complete artifact, partial loop**. The complete repository at the frozen commit is available as evidence. Initial inspection establishes the service and one concrete caller, but does not trace every material shipped consumer, evaluator, administrative mutation or deployment mode. No missing file or source-access failure is asserted. Available but uninspected material is not an access gap and is not excluded from the registered Git source. Later jobs may inspect it at this same commit; the present boundary does not warrant a whole-system coverage claim.

| Area | Initial inspection and included responsibility | Remaining limit and conclusion prevented |
|---|---|---|
| Root packaging and project description | `README.md` opening and quick-start material; `pyproject.toml`, `package.json` and API package entry-point declarations searched. Establishes repository layout, declared use and packaged launch surfaces. | Root instructions, build scripts and release automation not fully inspected; no complete release/development workflow account. |
| `hindsight-api`, `hindsight-api-slim` | Wrapper entry points; `hindsight_api/main.py` and `worker/main.py` bounded reads and construction searches; `api/__init__.py` API composition; `engine/memory_engine.py` operation searches; bounded reads of `engine/retain/orchestrator.py`, `engine/consolidation/consolidator.py` and `engine/reflect/agent.py`. | Storage implementations, migrations, detailed HTTP/MCP handlers, extension admission, maintenance dispatch and recovery not fully traced; no exhaustive service-loop or failure-isolation conclusion. |
| `hindsight-integrations` | Tree inspection identifies many shipped integrations. Claude Code `hooks/hooks.json` read completely; retain and recall scripts inspected at API submission and host-context output. LangGraph package and tests located. | Claude Code transcript selection, local state and client transport not fully traced; other integration implementations not inspected. No cross-integration lifecycle or universal persistence/consumption claim. |
| `skills`, `.claude-plugin`, `.cursor-plugin` | Skill and plugin paths enumerated; `skills/hindsight-self-hosted/SKILL.md` inspected through setup, retain, recall and reflect guidance. Its instructions are target doctrine, not commands executed in this run. | Other skills and complete plugin/skill wiring not inspected; no exhaustive prompt or maintenance-instruction coverage. |
| `hindsight-clients`, `hindsight-cli` | Language SDK and CLI trees enumerated; root quick-start caller examples inspected. | Implementations not traced end to end; no SDK parity, CLI transport or retry guarantees. |
| `hindsight-all`, `hindsight-all-slim`, `hindsight-all-npm`, `hindsight-embed` | Embedded Python and launcher paths located, including `hindsight-all/hindsight/embedded.py` and `hindsight-embed/hindsight_embed/cli.py`; embedded usage declarations searched. | Embedded persistence/reload, daemon/profile ownership and alternate distribution launch paths not traced; no deployment-mode equivalence. |
| `hindsight-control-plane`, `hindsight-extensions` | Present in tracked root tree; service code identifies an extension surface. | UI mutations and additional extension behavior not inspected; no complete operator-control or extension-policy account. |
| `hindsight-system-evals`, `hindsight-system-tests`, `hindsight-integration-tests`, package tests | Evaluation paths enumerated; opening of `hindsight-system-evals/README.md` inspected for declared quality-test conditions and reported regressions. | Evaluator implementations and retained results not inspected; no observed-run, comparative accuracy or causal-effect evidence claimed. |
| `hindsight-docs`, `cookbook`, `docker`, `helm`, `monitoring`, `hindsight-dev`, `scripts` | Present in tracked root tree; quick-start documentation identifies deployment and documentation surfaces. | Material examples, deployment configuration, observability and developer utilities not traced; no complete operational/deployment account. |

This is an initial-inspection map, not the exhaustive top-level coverage table required for a `whole-system` boundary. Remaining tracked root metadata and assets are available at the same pin but have not been treated as evidence of memory behavior.

### Frozen source, exclusions and dependencies

The frozen evidence is SRC-1 at full commit `610c135b6f2d0d8b972da94146ae635943f36271`; the applicability cutoff is `2026-10-14`, the supplied run date. The acquired checkout's HEAD was verified to equal that pin. The source object is retained unchanged. The cutoff records this run's evidence boundary, not an assertion that the repository describes every deployed instance on that date. No live documents, additional repositories, provider calls, tests or examples were executed.

Deliberate exclusions are external agents and framework implementations, hosted Cloud internals, live benchmark dashboards, linked papers and moving online documentation. Excluding external hosts prevents conclusions about their own scheduling, reasoning and actual response to injected context. Excluding hosted internals prevents conclusions about managed-service tenancy, backups and reliability. Excluding unregistered benchmarks and papers prevents independent verification of comparative accuracy or research claims. Frozen in-repository declarations remain attributable evidence, not independent confirmation (SRC-1, `README.md`).

External dependencies include model providers and database deployments, plus host hook/framework protocols where integrations use them. The README declares provider choices and PostgreSQL/Oracle deployment options; the inspected reflection code demonstrates the model-call interface. Provider behavior, database behavior and host implementation are not supplied execution evidence (SRC-1, `README.md`, `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`, `hindsight-integrations/claude-code/hooks/hooks.json`). These limits prevent guarantees of real-world model quality, database reliability or host interoperability. They do not prevent source-level analysis of Hindsight's side of those interfaces.

The overall evidence tier is **code-grounded**. Module comments, agent instructions and README descriptions supply doctrine/design. Evaluation documentation supplies attributed reported operation only. No inspected execution trace or controlled intervention establishes observed operation or causal effects.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/vectorize-io/hindsight` | 610c135b6f2d0d8b972da94146ae635943f36271 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/hindsight-34c2ca821edf/related-systems/vectorize-io--hindsight`. Implementation: packaged entry-point declarations, bounded service/worker construction reads and searches, API composition, retain orchestration opening, reflection model-call block, Claude Code hook manifest and retain/recall submission/output blocks. Doctrine/design: README opening/quick start, consolidation module opening, self-hosted skill's setup and memory-operation guidance. Reported operation: system-evaluation README opening and attributed regression descriptions. Additional initial searches located engine operation methods, fact-extraction/storage paths, SDKs, embedded surfaces, other integrations and evaluation files; location alone is not behavioral evidence. | Implementation: [entry points](https://github.com/vectorize-io/hindsight/blob/610c135b6f2d0d8b972da94146ae635943f36271/hindsight-api/pyproject.toml), [API composition](https://github.com/vectorize-io/hindsight/blob/610c135b6f2d0d8b972da94146ae635943f36271/hindsight-api-slim/hindsight_api/api/__init__.py), [reflection](https://github.com/vectorize-io/hindsight/blob/610c135b6f2d0d8b972da94146ae635943f36271/hindsight-api-slim/hindsight_api/engine/reflect/agent.py), [retain caller](https://github.com/vectorize-io/hindsight/blob/610c135b6f2d0d8b972da94146ae635943f36271/hindsight-integrations/claude-code/scripts/retain.py), [recall caller](https://github.com/vectorize-io/hindsight/blob/610c135b6f2d0d8b972da94146ae635943f36271/hindsight-integrations/claude-code/scripts/recall.py). Doctrine/design: [README](https://github.com/vectorize-io/hindsight/blob/610c135b6f2d0d8b972da94146ae635943f36271/README.md), [consolidation contract](https://github.com/vectorize-io/hindsight/blob/610c135b6f2d0d8b972da94146ae635943f36271/hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py), [self-hosted skill](https://github.com/vectorize-io/hindsight/blob/610c135b6f2d0d8b972da94146ae635943f36271/skills/hindsight-self-hosted/SKILL.md). Reported operation: [evaluation documentation](https://github.com/vectorize-io/hindsight/blob/610c135b6f2d0d8b972da94146ae635943f36271/hindsight-system-evals/README.md). | No repository access gap identified. Initial inspection is partial as specified above, preventing exhaustive shipped-loop characterization. Linked external services and publications are outside the frozen source. No execution evidence was supplied or generated; source intent and attributed reports cannot establish observed success, benchmark replication or causal improvement. |
