---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "RightMemory's shipped memory lifecycle, native-assistant path, integrations and evaluators at commit 62534bd82c58718f31c99692fed4c5d159e218ec."
run-id: AAS-2026-11-08-rightmemory-cbec05309c2b-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "62534bd82c58718f31c99692fed4c5d159e218ec"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/rightl/rightmemory
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/rightmemory-238e66962233/related-systems/rightl--rightmemory
  revision: "62534bd82c58718f31c99692fed4c5d159e218ec"
  sha256: null
---

# RightMemory boundary

## Boundary and evidence

RightMemory is in scope as a memory/knowledge/context-engineering system for coding agents. Its intended use is to preserve and later supply durable context, a human-owned direction map and reusable correction cases across conversations and clients. It is not classified as the enclosing coding-agent runtime. The whole-system boundary includes its internal model-executing runtime, its alternative native-assistant protocol, its shipped callers and maintenance instructions, and the storage, retrieval, admission, synchronization and sharing paths around them. SRC-1: `README.md`, `rightmemory/entrypoint.py`, `rightmemory/runtime.py`, `rightmemory/assistant_cli.py`.

> RightMemory gives people and coding agents three semantic modules: durable context lives in Memory, the user's directions form a Pursuit map, and reusable cases of user redirection live in Agent Corrections. Memory and Pursuit are Markdown document trees in one addressable graph; Agent Corrections is a fixed, non-graph case library.
> --- `README.md`

The applicability cutoff is 2026-11-08. The frozen evidence is the acquired repository at full commit `62534bd82c58718f31c99692fed4c5d159e218ec`; HEAD was checked against that pin and the checkout was clean. Only that revision supplies evidence. This is code-grounded source analysis, not a new execution, benchmark or causal experiment. Documentation and source-authored experimental reports remain attributed statements rather than independently observed results.

### Shipped lifecycle and entry-point coverage

The installed script resolves to `rightmemory.entrypoint:main` in SRC-1: `pyproject.toml`. Inspection followed its dispatch into ordinary CLI roles, native-assistant CLI and MCP adapters, then into storage and retrieval consumers. The ordinary CLI's queued Update batch reloads role configuration and calls `RightMemoryRuntime.run_session_turn` with the candidate batch; runtime constructs an isolated write operation and retains candidate evidence. Its supervisor checks role-owned commit paths and validates the candidate. Thus the boundary includes the driver and admission layer, not only a retrieval API. SRC-1: `rightmemory/entrypoint.py`, `rightmemory/cli.py`, `rightmemory/runtime.py`, `rightmemory/isolated_write.py`.

The internal agent retriever converts model selections into source-authored output using `RetrieveSelectionRenderer`; the embedding backend builds a current corpus, selects entries and renders original source text. Shipped orchestrator instructions tell the host to reconcile returned content with current evidence and use relevant guidance in its work. The host's actual compliance is outside source observation, but these instructions are part of the target. SRC-1: `rightmemory/runtime.py`, `rightmemory/embedding_retrieval.py`, `skills/rightmemory-auto-orchestrator-cli/SKILL.md`.

> Apply relevant guidance in the work itself; do not merely quote or acknowledge it.
> --- `skills/rightmemory-auto-orchestrator-cli/SKILL.md`

The native-assistant path is a distinct shipped loop, not an excluded host application. The assistant CLI dispatches into a model-free service, which saves submissions, prepares live-file retrieval access and claims update work. Its skill assigns model judgment and file editing to host-native children, then requires program completion for publication. `AssistantWriteManager` prepares persistent worktrees using the same write-supervisor family. This path must not be assumed to inherit internal-runtime session history or retrieval selection semantics. SRC-1: `rightmemory/assistant_cli.py`, `rightmemory/assistant.py`, `rightmemory/assistant_context.py`, `rightmemory/assistant_write.py`, `skills/rightmemory-assistant/SKILL.md`, `DESIGN_NOTES.md`.

> Only the program's completion receipt confirms that candidate work reached the active root. A prepared candidate is not a completed update.
> --- `skills/rightmemory-assistant/SKILL.md`

Maintenance includes explicit direct-edit skills as well as runtime Update, Pruner, Historian and Insight roles. Prompt assembly loads package-owned role instructions and semantic references. Web Studio's Pursuit service reads canonical state, applies map operations through `PursuitStore`, and generates opening context for later host use. Sync and shared-view imports can change the state later retrieval sees, so they are included rather than treated as incidental utilities. Sharing coverage includes the Git-file branches present in implementation even though the README emphasizes HTTP. SRC-1: `rightmemory/prompt.py`, `rightmemory/cli.py`, `rightmemory/web/service.py`, `rightmemory/sync.py`, `rightmemory/shared_view_files.py`, `rightmemory/shares.py`, `skills/maintain-rightmemory/SKILL.md`, `skills/maintain-pursuit-map/SKILL.md`.

### Tracked top-level coverage

All rows refer to SRC-1. Included means inside the analysis boundary, not that every file has already received a line-by-line audit. Initial inspection traced the material lifecycle above and inventoried the tracked tree. Paths named as inventoried or supporting material remain available for later inspection at this same commit; they are neither access gaps nor silently excluded paths.

| Top-level file or directory | Classification | Material paths and role | Initial inspection and limits / conclusion prevented |
| --- | --- | --- | --- |
| `.gitattributes` | Excluded | Repository text attributes | Deliberate exclusion from behavioral assessment; no conclusion about checkout normalization portability. |
| `.github/` | Included | `workflows/tests.yml`; issue templates | Workflow inspected for shipped Python and frontend verification surfaces; issue templates inventoried only. No CI execution result supplied. |
| `.gitignore` | Excluded | Repository development ignore rules | Deliberate exclusion; no audit of development-tree artifact leakage. The memory-root allowlist generated by `rightmemory/install_core.py` remains included. |
| `AGENTS.md` | Included | Developer guidance and repository map | Inspected for the distinction between development guidance and runtime prompts; not treated as runtime instructions or proof of enforced invariants. |
| `DESIGN_NOTES.md` | Included | Native-assistant, embedding and Pursuit design rationale | Inspected as doctrine/design, not execution evidence. |
| `LICENSE` | Excluded | License text | Deliberate exclusion; no legal or license-compliance conclusion. |
| `MEMORY.example.md` | Included | Installer seed and illustrative memory representation | Inventoried and connected through package metadata and installer documentation; example content not treated as actual user memory. Detailed seed review remains open. |
| `PURSUITS.example.md` | Included | Installer seed for direction-map state | Inventoried with the same seed-versus-user-state limit. |
| `README.md` | Included | Intended use, commands, modes, lifecycle, configuration and file layout | Read as doctrine/design and reported operation; executable paths take precedence when they differ. |
| `RIGHTMEMORY_EDIT_CORRECTIONS.example.md` | Included | Example of feedback about proposed memory edits | Inventoried as illustrative state, not observed correction effectiveness. |
| `docs/` | Included | `ASSISTANT_EXECUTION.md`, `MCP.md`, `AGENT_FILES.md`, `PURSUIT_MAP.md`, `shared-views-usage.md`, demonstrations, correction examples, maintainer background and `assets/` diagrams | Inventoried and connected from README and implementation. Detailed document and asset inspection remains open; availability is not an access gap. |
| `experiments/` | Included | `retrieval_embeddings.py`, `retrieval_reranker.py`, `retrieval_runtime.py`, `README.md` | README read and runtime benchmark entry inspected. Harnesses and attributed reports are included; private corpus, labels and raw results referenced under ignored `tmp/` are not supplied, preventing independent reproduction or quality/latency verification. |
| `install.ps1` | Included | Windows installation bootstrap | Inventoried; shared transaction traced to `rightmemory/install_core.py` through repository documentation. Detailed platform-bootstrap review remains open. |
| `install.sh` | Included | POSIX installation bootstrap | Same scope and initial inspection limit as PowerShell bootstrap. |
| `pyproject.toml` | Included | Script entry point, dependencies, packaging and optional model-service/SDK extras | Read; dependency implementations are not frozen in this source. |
| `rightmemory/` | Included | `entrypoint.py`, `cli.py`, `mcp.py`: internal-runtime callers; `assistant*.py`, `native_sync.py`: host-native loop; `runtime.py`, `agent_cli.py`, `codex_sdk.py`, `codex_app_server.py`, provider/session modules: model execution and continuity; `graph.py`, `tools.py`, `validation.py`, retrieval/index modules: state interpretation and consumption; `async_update.py`, `update_queue*.py`, `update_record.py`, `semantic_operation.py`, `isolated_write.py`, `memory_git.py`: durable submission and admission; `prune.py`, `insight_trigger.py`, `watch*.py`: maintenance; `guidance.py`, `corrections.py`: guidance capture and correction state; `sync.py`, `shares.py`, `shared_view*.py`, `git_share_transport.py`, `hub/`: transport, collaboration and imports; `web/`, `pursuit_store.py`, `pursuit_tree.py`, `opening_context.py`: human editing and later context consumption; `prompts/`, `reference/`: role and semantic contracts; configuration, installation, profiles, status and platform modules support these paths | Entry-point dispatch, selected runtime retrieval/write methods, prompt assembly, Update/Retrieve prompts, assistant service/context/write preparation, web Pursuit service, sync refresh, share publication/import and embedding selection/rendering inspected. Other listed modules, remaining prompts/references, frontend source and generated bundles inventoried for subsequent detailed analysis, not excluded. |
| `skills/` | Included | Automatic and approval-gated orchestrators, read-only retriever, native assistant, Memory and Pursuit maintenance, guidance-inbox review, Manager and onboarding interview | Native assistant, automatic orchestrator, both maintenance skills, guidance review, Manager and onboarding read. These callers decide when to submit, consume or directly edit retained state; other variants inventoried. Host compliance is not observed. |
| `tests/` | Included | Runtime, queues, isolated admission, sync, sharing, retrieval, native-assistant, web/editor, installation, provider and platform tests; test runner and fixtures | Tree inventoried; `test_assistant_service.py` inspected for submission → edit → completion → fresh-context assertions. Tests are inspectable executable expectations, not a supplied passing run or evidence of model judgment quality. |

### Dependencies, exclusions and evidence limits

The boundary includes RightMemory's shipped adapters and instructions for Pydantic AI, Codex SDK/App Server, Claude CLI, MCP, embedding/reranking services, Git transport and browser clients. It excludes those external products' implementations, model weights and provider services. Consequently this run cannot establish their scheduling, sandbox strength, model reliability, service availability or actual host-agent behavior. Package dependencies and adapter entry points are inspectable, not independently pinned dependencies: SRC-1, `pyproject.toml`, `rightmemory/entrypoint.py`, `rightmemory/runtime.py`.

Actual user memory roots, credentials, remote repositories, running hubs, private benchmark files and conversations are not supplied. The source-authored experiment report explicitly locates private inputs and raw results outside the tracked repository. Their absence prevents reproduction and independent validation of reported performance or downstream task benefit; it does not prevent a complete source-level boundary for the shipped system. SRC-1: `experiments/README.md`.

> Private inputs and raw results remain under ignored `tmp/embedding-retrieval/`.
> --- `experiments/README.md`

No new target execution is included. No source beyond this repository revision is registered, and external links in its documentation do not enlarge the frozen evidence set.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/rightl/rightmemory` | 62534bd82c58718f31c99692fed4c5d159e218ec | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/rightmemory-238e66962233/related-systems/rightl--rightmemory`. Implementation: tracked-tree inventory, package entry, CLI dispatch and batch/maintenance callers, selected runtime retrieval and isolated-write paths, native assistant CLI/service/context/write preparation, embedding retrieval, web Pursuit service, sync refresh, shared-view import/share publication, installer allowlist, experiment runtime entry and assistant-service test assertions. Doctrine/design: README, design notes, repository guidance, prompt assembly, Retrieve/Update prompts and the inspected skills identified above. Reported operation: retrieval experiment README. | Implementation: [package entry](https://github.com/rightl/rightmemory/blob/62534bd82c58718f31c99692fed4c5d159e218ec/pyproject.toml), [dispatch](https://github.com/rightl/rightmemory/blob/62534bd82c58718f31c99692fed4c5d159e218ec/rightmemory/entrypoint.py), [runtime](https://github.com/rightl/rightmemory/blob/62534bd82c58718f31c99692fed4c5d159e218ec/rightmemory/runtime.py), [native service](https://github.com/rightl/rightmemory/blob/62534bd82c58718f31c99692fed4c5d159e218ec/rightmemory/assistant.py). Doctrine/design: [README](https://github.com/rightl/rightmemory/blob/62534bd82c58718f31c99692fed4c5d159e218ec/README.md), [native caller](https://github.com/rightl/rightmemory/blob/62534bd82c58718f31c99692fed4c5d159e218ec/skills/rightmemory-assistant/SKILL.md), [Update prompt](https://github.com/rightl/rightmemory/blob/62534bd82c58718f31c99692fed4c5d159e218ec/rightmemory/prompts/update.md). Reported operation: [retrieval experiments](https://github.com/rightl/rightmemory/blob/62534bd82c58718f31c99692fed4c5d159e218ec/experiments/README.md). Other commit-relative anchors in this member identify additional initial inspection. | No repository access gap found. Uninspected available material is distinguished in the coverage table. Private benchmark corpus/labels/raw traces, deployed roots and external dependencies are not supplied; no independent performance reproduction, observed host compliance, end-to-end task improvement or causal attribution is supported. No observed-run or causal-experiment layer is registered. |
