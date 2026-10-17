---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Memori's shipped SDKs, native engine, integrations and evidence artifacts at commit 574b1ea3e876f100ef82c37817d603eb7e258e59, with a partial service-dependent memory loop."
run-id: AAS-2026-10-17-memori-fd4a0418c09b-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: 574b1ea3e876f100ef82c37817d603eb7e258e59
analysis-cutoff: "2026-10-17"
evidence-tier: code-grounded
source:
  identity: https://github.com/MemoriLabs/Memori
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-memori/related-systems/MemoriLabs--Memori
  revision: 574b1ea3e876f100ef82c37817d603eb7e258e59
  sha256: null
---

# Memori boundary

## Boundary and evidence

This run examines how Memori captures interactions and agent activity, maintains retained memory, and supplies it to later model calls. The target is the complete shipped repository artifact, not just the `Memori` library API. It is an in-scope **memory/knowledge/context-engineering system**: its public entry points connect conversation persistence, augmentation and recall to model clients and agent hosts. It is not classified as the enclosing agent runtime. The initial entry-point trace covers Python registration and post-response handling, TypeScript middleware hooks, a shipped SQLite caller, OpenClaw lifecycle registration and the Hermes memory-provider implementation (SRC-1: `memori/__init__.py`, `memori/llm/pipelines/post_invoke.py`, `memori-ts/src/memori.ts`, `examples/sqlite/main.py`, `integrations/openclaw/src/index.ts`, `integrations/hermes/src/memori_hermes/__init__.py`).

The TypeScript constructor connects the three responsibilities explicitly:

> this.axon.hook.before(this.recallEngine.handleRecall.bind(this.recallEngine));
> this.axon.hook.after(this.persistenceEngine.handlePersistence.bind(this.persistenceEngine));
> this.axon.hook.after(this.augmentationEngine.handleAugmentation.bind(this.augmentationEngine));
> --- `memori-ts/src/memori.ts:250-279`

Python's recall pipeline formats retained facts and summaries into model context; its post-response pipeline dispatches conversation persistence and augmentation. These are both consumption and production paths, not merely storage APIs (SRC-1: `memori/llm/pipelines/recall_injection.py`, `memori/llm/pipelines/post_invoke.py`). A shipped caller exercises successive model calls against a SQLite-backed instance and waits for background augmentation; it remains part of the target's usage evidence rather than an excluded application (SRC-1: `examples/sqlite/main.py`). Hermes also ships model-facing recall instructions, completed-turn capture, tool dispatch and session handling, while OpenClaw registers prompt-building and end-of-agent hooks (SRC-1: `integrations/hermes/src/memori_hermes/__init__.py`, `integrations/openclaw/src/index.ts`). For example, the Hermes prompt declares:

> Recall is agent-controlled and
> intentional: use `memori_recall` or `memori_recall_summary` when prior context
> matters, not on every turn.
> --- `integrations/hermes/src/memori_hermes/__init__.py`

**The boundary kind is `complete artifact, partial loop`, not `whole-system`.** The repository exposes service calls whose server-side memory derivation and hosted persistence are not established by this source set. Even the inspected Python BYODB augmentation path submits a payload to a service before interpreting returned memories and scheduling local writes (SRC-1: `memori/memory/augmentation/augmentations/memori/_augmentation.py`):

> api_response = await api.augmentation_async(payload)
> --- `memori/memory/augmentation/augmentations/memori/_augmentation.py`

The TypeScript implementation similarly distinguishes native-engine submission from hosted augmentation (SRC-1: `memori-ts/src/engines/augmentation.ts`):

> this.collectorApi.post('cloud/augmentation', payload).catch((e: unknown) => {
> --- `memori-ts/src/engines/augmentation.ts`

These anchors establish a service-dependent loop, not the service's internal extraction, admission or maintenance policy. No claim of complete end-to-end implementation coverage follows from the cloned repository or the `complete` disposition; that disposition means the boundary itself is established.

### Functional coverage and limits

- **Included:** Python SDK paths under `memori/`, TypeScript SDK paths under `memori-ts/`, and the Rust engine and bindings under `core/`. Initial inspection establishes SDK entry points, Python recall-context construction and persistence routing, augmentation response handling, TypeScript augmentation routing and Rust worker lifecycle. Detailed storage drivers, retrieval algorithms and binding behavior remain available for later inspection; they are not access gaps. The Rust architecture document supplies declared responsibilities, not proof of every implementation detail (SRC-1: `memori/__init__.py`, `memori/memory/_manager.py`, `memori/llm/pipelines/recall_injection.py`, `memori/memory/augmentation/augmentations/memori/_augmentation.py`, `memori-ts/src/memori.ts`, `memori-ts/src/engines/augmentation.ts`, `core/src/runtime/worker.rs`, `core/docs/architecture.md`).
- **Included:** shipped callers, integrations, prompts, skills and operational guidance in `examples/`, `integrations/` and `docs/`, including Claude Code, Hermes, OpenClaw and documented MCP usage. Initial code inspection covers the SQLite caller and the Hermes/OpenClaw entry points above. Claude Code implementation, other examples and documentation remain uninspected at boundary declaration, not unavailable or deliberately excluded. Their inclusion prevents treating shipped state producers or consumers as external merely because they call an SDK (SRC-1: repository tree; `README.md`, `examples/sqlite/main.py`, `integrations/hermes/src/memori_hermes/__init__.py`, `integrations/openclaw/src/index.ts`).
- **Included:** evaluators, tests and reported results under `benchmarks/`, `tests/`, `core/tests/`, SDK/integration test directories and benchmark documentation. The initially inspected benchmark README describes notebooks that download augmented memory data, build indexes and evaluate answers. The notebooks and stored outputs have not yet been inspected; this boundary does not validate benchmark accuracy or reproduce any result (SRC-1: `benchmarks/README.md`, `README.md`).
- **Included as supporting context:** root packaging, dependency locks, build/deployment configuration, `.github/`, policy documents and images. Tree inspection establishes their presence, not their correctness or runtime effect (SRC-1: `pyproject.toml`, `setup.py`, `docker-compose.yml`, `README.md`).
- **Unavailable beyond the artifact:** hosted API/collector implementation, dashboard internals and hosted MCP server internals. Client calls and source-native documentation may describe their interfaces or reported behavior, but cannot establish private derivation prompts, server-side memory acceptance, deduplication, retention, isolation or operational reliability. The frozen evidence contains no newly performed service observation (SRC-1: `README.md`, `memori/memory/_manager.py`, `memori-ts/src/engines/augmentation.ts`).
- **External dependencies, not target responsibilities:** enclosing applications and agent runtimes outside this repository, provider inference services, database engines, embedding model artifacts and external middleware such as Axon. Their interfaces may be traced through shipped consumers, but their implementations are not separately frozen here. This prevents attributing host scheduling, tool execution, model reasoning, database durability or external middleware guarantees to Memori (SRC-1: `memori-ts/src/memori.ts`, `examples/sqlite/main.py`, `integrations/openclaw/src/index.ts`, `integrations/hermes/src/memori_hermes/__init__.py`).

The immutable evidence boundary is commit **574b1ea3e876f100ef82c37817d603eb7e258e59**, verified as the acquired checkout's HEAD. The applicability cutoff is **2026-10-17**, the supplied run date; it is not a claim about later releases or current hosted behavior. The overall tier is **code-grounded**. Documentation remains attributed design or reported operation. No target code, tests, examples, providers or services were executed. Linked live documentation, papers, benchmark datasets, model downloads, cookbook repositories and other revisions are not additional frozen sources.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/MemoriLabs/Memori` | 574b1ea3e876f100ef82c37817d603eb7e258e59 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-memori/related-systems/MemoriLabs--Memori`. Tracked repository tree inspected. Implementation: `memori/__init__.py`, `memori/llm/pipelines/post_invoke.py`, `memori/llm/pipelines/recall_injection.py`, `memori/memory/_manager.py`, `memori/memory/augmentation/augmentations/memori/_augmentation.py`, `memori-ts/src/memori.ts`, `memori-ts/src/engines/augmentation.ts`, `core/src/runtime/worker.rs`, `examples/sqlite/main.py`, `integrations/openclaw/src/index.ts`, `integrations/hermes/src/memori_hermes/__init__.py`. Doctrine/design: `README.md`, `core/docs/architecture.md`, `benchmarks/README.md` and the Hermes embedded prompt. Reported operation: README benchmark and deployment claims, not independently verified. | [Python entry point](https://github.com/MemoriLabs/Memori/blob/574b1ea3e876f100ef82c37817d603eb7e258e59/memori/__init__.py); [TypeScript entry point](https://github.com/MemoriLabs/Memori/blob/574b1ea3e876f100ef82c37817d603eb7e258e59/memori-ts/src/memori.ts); [augmentation service boundary](https://github.com/MemoriLabs/Memori/blob/574b1ea3e876f100ef82c37817d603eb7e258e59/memori/memory/augmentation/augmentations/memori/_augmentation.py); [Hermes producer and consumer](https://github.com/MemoriLabs/Memori/blob/574b1ea3e876f100ef82c37817d603eb7e258e59/integrations/hermes/src/memori_hermes/__init__.py); [benchmark contract](https://github.com/MemoriLabs/Memori/blob/574b1ea3e876f100ef82c37817d603eb7e258e59/benchmarks/README.md) | Hosted services and external dependencies are not supplied implementations. No observed run or causal experiment is established. Prevents end-to-end hosted-policy, reliability and benchmark-reproduction conclusions. Available but uninspected files remain within this Git source, not excluded evidence. |
