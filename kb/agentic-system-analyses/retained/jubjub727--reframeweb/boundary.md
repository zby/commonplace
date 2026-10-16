---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "ReframeWeb's shipped agent workflow environment, including its memory, workspace, Store and panel consumers, at commit 318987dcde9a016f8e3db819ed9a73abf6b3ad81."
run-id: AAS-2026-10-14-reframeweb-cff918d7eb1e-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: 318987dcde9a016f8e3db819ed9a73abf6b3ad81
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/jubjub727/ReframeWeb
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/reframeweb-cff918d7eb1e/related-systems/jubjub727--ReframeWeb
  revision: 318987dcde9a016f8e3db819ed9a73abf6b3ad81
  sha256: null
---

# ReframeWeb boundary

## Boundary and evidence

This analysis covers ReframeWeb as the shipped agent workflow environment, not just its memory library or its native browser API. Its intended use is agent-driven interactive work through semantic capabilities, visual panels, persistent memory and deterministic tools. The target is in scope because it issues model calls and owns the surrounding task-selection, retrieval, execution, completion and retry flow. It is classified as an **enclosing runtime**: Python owns external I/O and process lifetimes, while the BAML flow owns routed agent decisions. A delegated Codex process is an execution dependency, not the entirety of the target (SRC-1, `README.md`, `agent-host/pyproject.toml`, `agent-host/src/reframe_agent_host/agent_flow/voice_turn_flow.py`, `agent-host/baml_src/ns_voice_turn/task_flow.baml`, `agent-host/src/reframe_agent_host/agent_execution/codex.py`).

> The project starts from the user interaction loop: Python receives audio, BAML
> drives the agentic flow, and the rest of the system is called from there. Native
> visual panels, a transport layer, WebAssembly Stores, Data Lenses, Compute
> Modules, and memory hang off that host-driven flow.
> --- `README.md`

The **whole-system** boundary includes the Agent Host and its shipped CLI drivers; BAML prompts and orchestration; graph-memory creation, retrieval, selection and subsequent prompt consumption; filesystem-memory publication and recovery; task tools and delegated execution; native Store and panel services; Store/React clients; the session-management application; authoring and maintenance instructions; and shipped evaluation surfaces. The session-management application and publication scripts are included rather than treated as an external application: they create startup memory and task/instruction metadata that the host later loads. Native daemons are included even when called through APIs or companion executables (SRC-1, `agent-host/pyproject.toml`, `agent-host/src/reframe_agent_host/startup_stores.py`, `applications/session-management/publish.py`, `applications/session-management/README.md`, `workspace-fs/README.md`, `semantic-store/README.md`, `panel-manager/README.md`).

### Entry points and state-loop coverage

Initial inspection traced these shipped paths. This establishes a functional boundary, not a completed audit of every implementation leaf.

| Shipped entry or producer | State, admission or maintenance responsibility | Shipped consumer and boundary decision |
| --- | --- | --- |
| `reframe-agent-host` entry in `agent-host/pyproject.toml`; `agent-host/src/reframe_agent_host/cli.py` and `agent-host/src/reframe_agent_host/commands/voice_turn.py` | CLI dispatch reaches the voice pipeline; the Python flow calls generated `RunVoiceTurn_async` with host callbacks. | The BAML orchestrator in `agent-host/baml_src/ns_voice_turn/task_flow.baml` selects tasks, retrieves/selects memory, composes prompts, dispatches work and checks completion. Include host, generated SDK, prompt sources and drivers together (SRC-1). |
| `agent-host/baml_src/ns_voice_turn/task_flow.baml` and `agent-host/baml_src/ns_voice_turn/memory_review_flow.baml` | Candidate guidance is reviewed by model-backed selection before a write batch reaches the host. | `agent-host/src/reframe_agent_host/agent_flow/candidate_memory_writeback.py` writes to five guidance collections; `agent-host/src/reframe_memory/context_memories.py` creates graph nodes and collection relations. Include both admission and persistence (SRC-1). |
| `agent-host/src/reframe_agent_host/agent_flow/memory_contexts.py` and `agent-host/src/reframe_agent_host/agent_flow/voice_turn_context.py` | Reload stored guidance, preferences, task/provider metadata and conversation/session context for later turns. | `agent-host/src/reframe_agent_host/voice/task_flow_host.py` supplies those inputs to BAML. `agent-host/src/reframe_agent_host/agent_flow/memory_retrieval.py` separately translates model search plans into graph retrieval; selected context reaches task prompting and execution. Include these consumers, not only record APIs (SRC-1). |
| `agent-host/src/reframe_agent_host/agent_execution/retention.py` and `agent-host/src/reframe_agent_host/workspace/publication_service.py` | Explicit retained output checkpoints selected workspace paths and publishes filesystem memory; the retention handler can link it to a task. | Workspace planning/recovery and saved artifact startup consume retained content. `agent-host/src/reframe_agent_host/startup_stores.py` resolves saved artifacts, loads immutable Store revisions, binds graph metadata and invokes saved startup functions. Include the workspace service, graph publication and later startup (SRC-1). |
| `applications/session-management/publish.py` | Checks matching build/acceptance receipts, publishes checkpoint and maintenance instruction memories, publishes Store metadata and tasks, and enables startup membership. | The host startup loader and the application's Store/React documents use that persisted state. This is shipped production/maintenance participation, not an excluded host (SRC-1, `agent-host/src/reframe_agent_host/startup_stores.py`, `applications/session-management/README.md`). |
| `semantic-store/crates/store-host/src/main.rs`; `workspace-fs/crates/workspace-daemon/src/main.rs`; `panel-manager/crates/panel-service/src/bin/manager.rs` | Native entry points dispatch to Store CLI, workspace daemon and platform manager composition. Their guides and manifests identify protocol/runtime/package, filesystem storage/mount, and panel authorization/lifecycle responsibilities. | Agent Host companion dependencies and adapters consume these services; Store components can also consume panel capabilities. Include native implementations and their clients, examples and acceptance suites (SRC-1, `agent-host/pyproject.toml`, `semantic-store/README.md`, `workspace-fs/README.md`, `panel-manager/README.md`). |
| `agent-host/src/reframe_agent_host/benchmarks/memory_relevance_execution.py`; `agent-host/tests/test_candidate_memory_writeback.py` | Benchmark code records expected/selected memory IDs and correctness; the unit test checks collection-specific writes with fake stores. | Include evaluators as evidence of evaluation design, not proof that current production runs succeed. Other shipped benchmark, BAML test and native acceptance paths remain eligible for later inspection (SRC-1). |

The candidate-memory write/read loop is executable source, not only a README aspiration:

> let review_context = MemoryReviewContext(completion_context);
> let write_batch = ReviewMemories(candidate_memories, review_context, client = client);
> let memories_selected = root.memory.internal.HasSelectedCandidates(write_batch);
> if (memories_selected) {
>     //# Save selected memories
>     let _ = write_candidate_memories(write_batch);
> --- `agent-host/baml_src/ns_voice_turn/task_flow.baml`

> for store, candidates in destinations:
>         for candidate in candidates:
>             await store.create(
>                 ContextMemory(
>                     title=candidate.title,
>                     description=candidate.description,
>                 )
>             )
> --- `agent-host/src/reframe_agent_host/agent_flow/candidate_memory_writeback.py`

> async def task_prompt_memories(database: MemoryDatabase):
>     return [
>         baml_task.TaskPromptMemoryContext(
>             title=memory.content.title,
>             description=memory.content.description,
>             tags=list(memory.tags),
>             **timestamp_fields(memory),
>         )
>         for memory in await database.task_prompt_memories.search()
>     ]
> --- `agent-host/src/reframe_agent_host/agent_flow/memory_contexts.py`

The shipped authoring instructions also affect retained state and therefore stay inside the boundary:

> Host verifies a staged copy, records its identity/dependency/hash manifest, checkpoints
> it without permanently linking this task, and records a relevance-filtered locator.
> --- `docs/authoring/instructions/save-store.md`

### Top-level tracked coverage

Every top-level tracked file or directory at the frozen commit is accounted for below. “Included” means eligible evidence within the functional target, not that every file has already been read. Named initial inspections distinguish examined material from available material awaiting detailed analysis. No material shipped path was unavailable at boundary establishment.

| Top-level tracked path | Treatment and material paths/role | Initial inspection and limits |
| --- | --- | --- |
| `.gitattributes` | Excluded from operational characterization: repository file handling. | Tree-listed, not content-inspected. No conclusions about cross-checkout line-ending or attribute behavior. |
| `.gitignore` | Excluded from operational characterization: ignored build/local artifacts. | Tree-listed, not content-inspected. No inference that ignored runtime data or generated binaries were captured. |
| `AGENTS.md` | Included: source-native development and control-flow doctrine. | Read completely as evidence, not as authority for this analysis. Its intended ownership split is not itself execution proof (SRC-1, `AGENTS.md`). |
| `README.md` | Included: product intent, host setup, conceptual components and declared status. | Read completely. Future architecture and reported implementation status are not automatically implementation facts (SRC-1, `README.md`). |
| `agent-host/` | Included: `pyproject.toml`, `baml_src/`, generated `src/baml_sdk/`, `src/reframe_agent_host/`, `src/reframe_memory/`, native panel bridge/launcher, `tests/`, `benchmark-results/`, and package/configuration files. Covers model orchestration, state production/admission/retrieval/consumption, speech, tools, delegated execution, maintenance UI and evaluation. | Inspected manifest, CLI/voice entry dispatch, BAML voice planning/orchestration/review, host callbacks, guidance persistence/reload, graph retrieval adapter, task execution, Codex invocation, retention, startup, publication search, memory-relevance evaluator and writeback test. Generated SDK internals, audio internals, most native bridge leaves, tests and stored benchmark results are available but not yet deeply inspected; no blanket correctness or benchmark-performance conclusion (SRC-1, paths in the entry-point table). |
| `applications/` | Included: `session-management/` Store schema/guest, React UI, build/prepare/publish/update scripts, maintenance instructions and acceptance programs. | Read application guide and initial publication driver; traced persisted startup membership to host loader. Guest/UI internals and acceptance artifacts remain available for later inspection. Do not infer live application acceptance from script presence (SRC-1, `applications/session-management/README.md`, `applications/session-management/publish.py`). |
| `docs/` | Included: architectural decisions/designs, `authoring/instructions/`, panel/Store/shared authoring guides, task/project lifecycle and startup documents, and source-native reports/audits. These describe prompts, retention contracts and maintenance, not an external enclosing application. | Initially read `docs/authoring/instructions/save-store.md`; other documents tree-listed and available, not access gaps. Target-authored results/audits may support attributed reports only until underlying evidence is inspected. This boundary makes no finding from an unread report (SRC-1). |
| `native-support/` | Included: `protobuf_json_schema.rs`, shared descriptor-to-tool-schema conversion. | Read implementation and searched its inclusion by native panel bridge and Store CLI tool-schema adapter. No exhaustive schema soundness claim (SRC-1, `native-support/protobuf_json_schema.rs`, `agent-host/native/panel-agent-bridge/src/tool_schemas.rs`, `semantic-store/crates/store-host/src/cli/tool_schema.rs`). |
| `panel-manager/` | Included: `crates/` model, policy, protocol, transport, client, runtime, host, service, backend and platform implementations; `native/edge-webview2-host/`; `react-client/`; `acceptance/`; distribution and DRM contracts. | Read subsystem guide; inspected service manifest/Unix manager entry and tree of integration paths. Detailed platform, authentication, packaging, DRM and acceptance code remains available. Native guide claims are not evidence that a particular external distribution or hardware passes qualification (SRC-1, `panel-manager/README.md`, `panel-manager/crates/panel-service/Cargo.toml`, `panel-manager/crates/panel-service/src/bin/manager.rs`). |
| `scripts/` | Included as bounded auxiliary examples/evaluation: `netflix/` and `crunchyroll/` launchers and prepare/restore JavaScript, not the production orchestration loop. | Read both guides. Script implementations remain available; no live website/account playback conclusion. The guides assign production orchestration to Rust and Stores (SRC-1, `scripts/netflix/README.md`, `scripts/crunchyroll/README.md`). |
| `semantic-store/` | Included: protocol/package/catalog/SDK/runtime/transport/host crates, `authoring/` publication and verification, `react-client/`, `acceptance/react/`, `examples/`, protobuf/WIT and build inputs. | Read guide architecture and panel-import contract; inspected host executable entry, manifest and shared tool-schema consumer. Detailed Wasmtime execution, package validation, authoring publication, React and conformance tests remain available. No claim of conformance-test success (SRC-1, `semantic-store/README.md`, `semantic-store/crates/store-host/src/main.rs`, `semantic-store/crates/store-host/Cargo.toml`). |
| `workspace-fs/` | Included: `crates/workspace-daemon/` daemon/protocol, resident files, policy, sessions, checkpoints, SQLite/blob storage and platform mounts, plus packaging and license material. | Read guide's host ownership, memory registration and mounted-session sections; inspected daemon entry/manifest and host retention/publication paths. Storage/mount implementation leaves and recovery/performance tests remain available. No measured durability, mount compatibility or performance conclusion (SRC-1, `workspace-fs/README.md`, `workspace-fs/crates/workspace-daemon/src/main.rs`, `agent-host/src/reframe_agent_host/agent_execution/retention.py`). |

### Frozen evidence and external limits

The evidence identity is the canonical repository at full commit `318987dcde9a016f8e3db819ed9a73abf6b3ad81`, not the local directory name. The acquired checkout's HEAD was verified against that pin and its working-tree status was clean. The analysis cutoff is **2026-10-14**: later revisions, live documentation changes and untracked deployment state are outside this run. Overall evidence tier is **code-grounded**, with source-native doctrine kept distinct from executable behavior. Only SRC-1 is registered; no target execution, dependency installation, provider request or experiment was performed.

External implementations and deployment materials are excluded: model-provider services and weights, the Codex executable's internal agent loop, BAML compiler/runtime dependencies beyond shipped bindings and prompts, SurrealDB internals, Wasmtime/WASI internals, CEF/WebView2 and platform filesystem/windowing implementations, proprietary codec/CDM/signing material, live websites, credentials and user-specific databases/checkpoints. These dependencies are identified by shipped integration code, guides and manifests; they are not independently frozen sources. The exclusions prevent claims about provider quality, delegated-runtime internals, database/VM/browser security guarantees, actual platform compatibility, DRM/service acceptance or a user's retained state. ReframeWeb's adapters, supplied policies and process ownership remain in scope (SRC-1, `agent-host/pyproject.toml`, `agent-host/src/reframe_agent_host/agent_execution/codex.py`, `semantic-store/README.md`, `workspace-fs/README.md`, `panel-manager/README.md`).

Data Lenses and Compute Modules are included only to the extent represented in this commit; the README describes their runtimes as future-facing. Their conceptual mention does not establish an implemented execution path. Likewise, source code, test definitions and author reports do not establish observed end-to-end success, causal improvement from memory, production reliability or current performance. Unread available files are inspection work left to later jobs, not evidence access gaps (SRC-1, `README.md`, `agent-host/src/reframe_agent_host/benchmarks/memory_relevance_execution.py`, `agent-host/tests/test_candidate_memory_writeback.py`).

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/jubjub727/ReframeWeb` | 318987dcde9a016f8e3db819ed9a73abf6b3ad81 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/reframeweb-cff918d7eb1e/related-systems/jubjub727--ReframeWeb`. Implementation: tracked tree and entry manifests; Agent Host CLI/voice dispatch, BAML orchestration and review, Python callback flow, memory-context loaders/writeback/store, graph-retrieval adapter, task execution/Codex, retention/publication/startup; application publication; native main entry points; shared JSON-schema converter; memory-relevance evaluator and writeback unit test. Doctrine/design: root README and AGENTS, application/panel guides, Store guide architecture/import sections, workspace guide ownership/memory/session sections, save-Store instruction, website smoke-test guides. The coverage table records paths and remaining available inspection. | Implementation: [voice-turn orchestration](https://github.com/jubjub727/ReframeWeb/blob/318987dcde9a016f8e3db819ed9a73abf6b3ad81/agent-host/baml_src/ns_voice_turn/task_flow.baml), [guidance persistence](https://github.com/jubjub727/ReframeWeb/blob/318987dcde9a016f8e3db819ed9a73abf6b3ad81/agent-host/src/reframe_agent_host/agent_flow/candidate_memory_writeback.py), [guidance reload](https://github.com/jubjub727/ReframeWeb/blob/318987dcde9a016f8e3db819ed9a73abf6b3ad81/agent-host/src/reframe_agent_host/agent_flow/memory_contexts.py), [startup consumer](https://github.com/jubjub727/ReframeWeb/blob/318987dcde9a016f8e3db819ed9a73abf6b3ad81/agent-host/src/reframe_agent_host/startup_stores.py), [application publication](https://github.com/jubjub727/ReframeWeb/blob/318987dcde9a016f8e3db819ed9a73abf6b3ad81/applications/session-management/publish.py). Doctrine/design: [product guide](https://github.com/jubjub727/ReframeWeb/blob/318987dcde9a016f8e3db819ed9a73abf6b3ad81/README.md), [retention instruction](https://github.com/jubjub727/ReframeWeb/blob/318987dcde9a016f8e3db819ed9a73abf6b3ad81/docs/authoring/instructions/save-store.md). Other commit-relative anchors appear in the coverage tables. | No repository access gap found. External services, runtime dependencies and user/deployment state are not frozen. No observed-run or causal-experiment layer established by initial inspection; tests and evaluator source support intended checks, not their success or an effect on outcomes. Later inspection may use any tracked path at this same commit, without adding another source identity. |
