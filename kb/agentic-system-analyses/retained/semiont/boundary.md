---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Semiont's shipped knowledge platform at a920067ac4ea63a57b1855b7d263485fbd22bab4, with a complete repository capture and partial initial loop inspection."
run-id: AAS-2026-10-15-semiont-d516c7013d8f-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: a920067ac4ea63a57b1855b7d263485fbd22bab4
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  kind: git
  identity: https://github.com/The-AI-Alliance/semiont
  revision: a920067ac4ea63a57b1855b7d263485fbd22bab4
  path: /home/zby/llm/commonplace/.commonplace/worktrees/semiont-d516c7013d8f/related-systems/The-AI-Alliance--semiont
  sha256: null
---

# Semiont boundary

## Boundary and evidence

This run analyses Semiont as a shared knowledge platform serving humans and model-based agents, not just its MCP adapter or an SDK library. Its intended use is building and maintaining source-linked knowledge that can later be retrieved and supplied to generation. The target is in scope as a **memory/knowledge/context-engineering system**: shipped services connect retained resources and annotations to context assembly, model calls and subsequent writes. The overall evidence tier is **code-grounded**; architecture prose remains declared design rather than proof of implementation or successful operation. SRC-1, `README.md`, `docs/architecture/KNOWLEDGE-SYSTEM.md`, `apps/worker/src/semiont_worker/held_job.py`.

The platform describes its purpose explicitly:

> **Semiont is an open, source-grounded semantic knowledge platform for building and maintaining trusted AI knowledge bases and context layers. It gives humans and AI agents a shared workspace and architecture to annotate, connect, enrich, and govern domain knowledge for accurate applications, agents, and workflows.**
> --- `README.md`

The frozen evidence is the complete Git repository at **a920067ac4ea63a57b1855b7d263485fbd22bab4**. The checkout's HEAD was checked against the acquired revision. The applicability cutoff is **2026-10-15**, the supplied run date, not a claim that a deployed service or later release has this behavior. The acquired source object is retained unchanged above. No additional repository, live documentation, release image, model output or external knowledge-base corpus is frozen.

### Functional inclusions and traced entry points

All shipped paths at this commit remain eligible evidence under SRC-1. Functional inclusions are content admission and annotation; durable records and derived views; graph/vector maintenance and repair; retrieval and context assembly; queued model work and generated-content admission; human and SDK consumers; MCP integration; launcher/deployment configuration; shipped agent instructions, prompts and evaluators. Shipped callers are part of the target, not external applications merely because they use an SDK. SRC-1, `Cargo.toml`, `package.json`, `docs/architecture/ACTOR-MODEL.md`, `docs/builder/skills/README.md`.

Initial implementation inspection establishes a real shipped caller beyond the library API. The Worker service constructs inference clients from configured providers and models; an `AgentWorker` opens an authenticated SDK transport and claims jobs; claimed work reaches `run_job`. For a yield job, `_yield` invokes generation processing, uploads the artifact through `client.yield_.resource`, commits links/citations and completes the job. The Python SDK's `YieldNamespace.resource` forwards that upload to its content transport. These are included platform responsibilities, not behavior attributed to an unspecified enclosing agent. SRC-1, `apps/worker/src/semiont_worker/service.py`, `apps/worker/src/semiont_worker/agent.py`, `apps/worker/src/semiont_worker/held_job.py`, `packages/sdk-python/src/semiont/namespaces/yield_.py`.

>     made = await process_generation_job(inference, params, on_progress=reports.say, cancelled=job.cancelled)
> --- `apps/worker/src/semiont_worker/held_job.py`

>     def resource(self, data: PutBinaryRequest) -> Upload:
>         """Upload bytes as a new resource: the upload's progress, and the resource created."""
>         return self._content.put_binary(data)
> --- `packages/sdk-python/src/semiont/namespaces/yield_.py`

On the record side, `yield_create` registers the content, derives attribution, constructs the event payload and appends a `YieldCreated` event. The generation prompt builder consumes retained resource content, graph connections and semantic matches. The Librarian service wires graph/vector readers, embedding and inference clients, and listens for gather/match requests and projection-progress signals. The initial inspection does not yet trace every transport hop between these endpoints. SRC-1, `apps/archivist/src/commands.rs`, `apps/worker/src/semiont_worker/generation/resource_generation.py`, `apps/librarian/src/semiont_librarian/service.py`.

>     archivist.append(event(YieldCreated::NAME, Some(&resource_id), user, payload))?;
> --- `apps/archivist/src/commands.rs`

The MCP executable is a separate included client: it constructs a `SemiontClient` over HTTP transports and exposes it through a stdio MCP server. This does not make Semiont itself merely an MCP tool. SRC-1, `packages/mcp-server/src/index.ts`.

### Coverage and partial-loop limit

The boundary kind is **complete artifact, partial loop**, not `whole-system`. The repository tree and the shipped paths above were inspected, but material routes through gateway authorization, dispatcher admission, projection repair, Browser/desktop consumers and the full launcher have not yet been traced in implementation. They are **not yet inspected**, not unavailable and not deliberately excluded. That distinction prevents an initial claim of exhaustive whole-system loop coverage, global access-control enforcement or complete maintenance/recovery behavior. Later jobs may inspect these paths at the same registered commit; the source register's initial paths are not an allowlist.

| Shipped area | Initial inspection and role | Limit at boundary declaration |
|---|---|---|
| `apps/worker` | Service/client wiring, agent claiming, held-job generation/upload, generation prompt construction inspected in bounded source ranges. | Detection, retry/checkpoint and provider-call details remain to be traced. |
| `apps/archivist` | `src/commands.rs` yield admission and event append inspected. | Record storage, materialized-view durability and full command policy not yet traced. |
| `apps/librarian` | `src/semiont_librarian/service.py` startup dependencies and request-channel roster inspected. | Gather/match internals and actual retrieval quality not established. |
| `apps/gateway`, `apps/dispatcher`, `apps/weaver`, `apps/smelter` | Tree inspected; roles described by the target's architecture documentation. | Implementation of authorization, scheduling, replay, graph/vector repair and extraction not yet inspected. |
| `apps/launcher`, `apps/browser`, `apps/desktop` | Launcher README opening inspected; Browser and desktop trees identified. These are included shipped operators/consumers. | No implementation-level claim about all entry points, UI proposal review or startup lifecycle. |
| `packages` | Python SDK yield namespace and MCP executable inspected; root manifests and package tree identify TS/Rust/Python/Go SDKs, core/schema, HTTP, graph, vector, inference, service, UI and observability packages. | SDK parity, provider guarantees and all later consumers remain unestablished. |
| `docs` | README, actor model, knowledge-system architecture and builder-skills index inspected. The skills index identifies ingest, annotate, canonical-node, relate and aggregate workflows. | Individual skill procedures and all prompt/maintenance contracts not yet assessed; not omitted from the functional target. |
| `tests` | Conformance tree and Librarian suite README inspected. Includes source-level evaluation infrastructure, not run evidence. | Test cases and harness internals have not been evaluated or executed. No passing-suite or efficacy conclusion follows. |
| `specs`, `scripts`, `.github` | Tree/manifests identify protocol contracts, code generation, fixtures, lint/build/release and CI infrastructure. Included where they determine shipped behavior or evaluation conditions. | Detailed contract/implementation agreement and CI outcomes not yet assessed. |
| `website` | Tree identified; README's illustrative image belongs here. | Website assets and promotional content provide no independent operational evidence. |
| Root files | `README.md`, `package.json`, `Cargo.toml` inspected; remaining tracked root files are policy/license documents, dependency locks, toolchain/version, lint, test and build configuration. | No dependency-security, licensing-compliance or reproducible-build audit is claimed. |

### External dependencies and evidence exclusions

The target's deployment description names container infrastructure and external services including Keycloak/PostgreSQL, NATS, Neo4j, Qdrant and optional local Ollama; its model configuration also permits configured provider endpoints. These are external dependencies, not additional frozen implementations. Their configured use and Semiont-side adapters are in scope; their internal correctness, uptime and security are not established. The launcher itself remains inside the target. SRC-1, `apps/launcher/README.md`, `apps/worker/src/semiont_worker/service.py`, `apps/librarian/src/semiont_librarian/service.py`.

No target execution was performed. The Librarian conformance documentation describes scripted model/embedding stand-ins and real surrounding services. It supplies evaluation design, not an observed run, a measurement of model quality or a causal experiment. External assistant runtimes that load skills or call MCP, third-party models, separately hosted knowledge-base repositories and deployment-specific human decisions are excluded; this prevents conclusions about their reasoning, corpus quality or end-to-end production outcomes. SRC-1, `tests/conformance/librarian/README.md`, `docs/builder/skills/README.md`, `packages/mcp-server/src/index.ts`.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/The-AI-Alliance/semiont` | a920067ac4ea63a57b1855b7d263485fbd22bab4 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/semiont-d516c7013d8f/related-systems/The-AI-Alliance--semiont`. Implementation: repository tree; `package.json`, `Cargo.toml`; bounded ranges of Worker `service.py`, `agent.py`, `held_job.py`, generation `resource_generation.py`; Archivist `src/commands.rs`; Librarian `service.py`; Python SDK `namespaces/yield_.py`; MCP `src/index.ts`. Doctrine/design: `README.md`, `docs/architecture/ACTOR-MODEL.md`, `docs/architecture/KNOWLEDGE-SYSTEM.md`, `docs/builder/skills/README.md`, opening of `apps/launcher/README.md`, `tests/conformance/librarian/README.md`. | Implementation: [worker caller](https://github.com/The-AI-Alliance/semiont/blob/a920067ac4ea63a57b1855b7d263485fbd22bab4/apps/worker/src/semiont_worker/held_job.py), [record admission](https://github.com/The-AI-Alliance/semiont/blob/a920067ac4ea63a57b1855b7d263485fbd22bab4/apps/archivist/src/commands.rs), [Librarian wiring](https://github.com/The-AI-Alliance/semiont/blob/a920067ac4ea63a57b1855b7d263485fbd22bab4/apps/librarian/src/semiont_librarian/service.py), [MCP entry](https://github.com/The-AI-Alliance/semiont/blob/a920067ac4ea63a57b1855b7d263485fbd22bab4/packages/mcp-server/src/index.ts). Doctrine/design: [knowledge architecture](https://github.com/The-AI-Alliance/semiont/blob/a920067ac4ea63a57b1855b7d263485fbd22bab4/docs/architecture/KNOWLEDGE-SYSTEM.md), [skills index](https://github.com/The-AI-Alliance/semiont/blob/a920067ac4ea63a57b1855b7d263485fbd22bab4/docs/builder/skills/README.md), [evaluation design](https://github.com/The-AI-Alliance/semiont/blob/a920067ac4ea63a57b1855b7d263485fbd22bab4/tests/conformance/librarian/README.md). | No repository access gap established. Material implementation not yet inspected is identified above, preventing exhaustive loop claims. No observed-run or causal-experiment layer; actual service success, model accuracy and deployment outcomes are not established. External dependency implementations and external corpora are not frozen. |
