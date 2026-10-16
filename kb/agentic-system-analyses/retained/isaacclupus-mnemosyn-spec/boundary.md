---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Mnemosyne's memory-system specification and legacy integration prototype at commit 0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92."
run-id: AAS-2026-10-15-isaacclupus-mnemosyn-spec-1887e13dcc13-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92"
analysis-cutoff: "2026-10-15"
evidence-tier: doc-grounded
source:
  identity: https://github.com/noirblue/IsaacCLupus_mnemosyn_spec
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-16-isaacclupus-mnemosyn-spec/related-systems/noirblue--IsaacCLupus_mnemosyn_spec
  revision: "0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92"
  sha256: null
---

# IsaacCLupus_mnemosyn_spec boundary

## Boundary and evidence

The target is Mnemosyne / Jarvis Knowledge OS as specified in this repository, including its superseded Python integration prototype. It is in scope as a **memory/knowledge/context-engineering system**: the design serves agent knowledge queries and retained memories, and describes model-driven extraction, compilation and auditing. It is not an enclosing general-purpose agent runtime. The intended use is to explain this memory substrate's design and distinguish its contracts from the narrower behavior inspectable in the prototype. SRC-1, `README.md`, `ARCHITECTURE.md`, `AGENTS.md`, `SPECIFICATION.md`.

> In Mnemosyne, the **agent is a client of the OS**, not a component inside it. The OS provides the memory substrate; the agent consumes it.
> --- `AGENTS.md`

The boundary kind is **complete artifact, partial loop**. The frozen repository is a coherent, complete specification artifact with SQL DDL, implementation studies and legacy bridge code, not a shipped implementation of the proposed unified lifecycle. This is not a boundary restricted to a library API: the shipped CLI driver, publish pipeline, gateway, proxy, configuration and service launchers all belong to the target. Their state-producing and state-consuming responsibilities remain included. A complete disposition means the target and frozen evidence are established, not that its proposed runtime is complete. SRC-1, `README.md`, `GETTING_STARTED.md`, `ROADMAP.md`, `prior-art/v0-glue/pyproject.toml`, `prior-art/v0-glue/jarvis_kb/cli.py`.

> **Concept / Architecture Proposal.**
> This repository contains the specification, data models, and roadmap.
> We are seeking core contributors to begin implementation.
> --- `README.md`

### Functional scope and entry-point trace

The design boundary includes raw-source ingestion; fast-model extraction and heavy-model compilation; draft audit, approval and publication; persistent pages, links, conversations and audit state; memory proposal and commitment; retrieval and context budgets; and agent-facing MCP, REST, CLI and exported packs. These are design responsibilities, not established executable guarantees. `SPECIFICATION.md` identifies itself as canonical, labels v0.1 superseded and v0.2 a draft. Phase 2 additions must not be conflated with the initial DDL. SRC-1, `ARCHITECTURE.md`, `SPECIFICATION.md`, `schema/001-init.sql`.

The tracked tree and executable entry-point chain were inspected read-only. The package's `jarvis-kb` script resolves to `jarvis_kb.cli:main`. That driver loads configuration and dispatches initialization, publication, proxy serving, MCP serving or status inspection. The systemd units launch the same driver. These are shipped callers, not excluded host applications. SRC-1, `prior-art/v0-glue/pyproject.toml`, `prior-art/v0-glue/jarvis_kb/cli.py`, `prior-art/v0-glue/jarvis_kb/config.py`, `prior-art/v0-glue/config.yaml`, `prior-art/v0-glue/systemd/jarvis-kb-mcp.service`, `prior-art/v0-glue/systemd/jarvis-kb-proxy.service`.

The legacy publication path reads Synto and Synthadoc wiki files, normalizes metadata into a unified vault, resolves filename collisions, invokes LLM-WIKI ingestion and reindexing, and requests Link snapshot/load operations. The gateway later consumes retained content through LLM-WIKI search/ask and Link query; it also routes ingestion, memory writes, compilation and evaluation to external tools. The proxy forwards model requests to Ollama through an in-memory priority queue or a two-node router. This traces persistence, reload, later consumption and evaluation through the shipped bridge, but not inside the external backends. SRC-1, `prior-art/v0-glue/jarvis_kb/vault_sync.py`, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`, `prior-art/v0-glue/jarvis_kb/ollama_proxy.py`.

>         # 3. Rebuild frontline search indexes
>         self._rebuild_llm_wiki_index()
>
>         # 4. Tell Link to load the new state
>         self._link_load_latest()
> --- `prior-art/v0-glue/jarvis_kb/vault_sync.py`

### Coverage and limits

Initial inspection covers the architecture, canonical specification, agent-role guidance, complete getting-started workflow, roadmap, schema and schema guide, both implementation-study indexes, prior-art guide, executable bridge modules other than the one-line package initializer, package entry-point metadata, bridge configuration and both service units. The source register permits later inspection of any tracked path at this same revision; initial inspection is not a source allowlist.

The historical v0.1 and draft v0.2 specifications, detailed `python_thoughts/` and `rust_thoughts/` studies, `FAQ.md`, `MOTIVATION.md`, `COMPARISON.md`, `CONTRIBUTING.md`, `STRUCTURE_CHECK.md`, `config.sample.yaml`, `LICENSE`, package initializer and `assets/` images were not initially inspected. They are available frozen evidence, not access gaps or excluded material. In particular, the study indexes identify compilation/prompt work and queue, watcher, graph and pack-export sketches; their details remain to be inspected before making claims about those proposals. SRC-1, `python_thoughts/README.md`, `rust_thoughts/README.md`.

External Synto, Synthadoc, LLM-WIKI-MCP, Link and Ollama implementations, models, live vaults and enclosing agent clients are outside this frozen source set. Their implementations and execution records are unavailable here. Consequently this analysis cannot establish backend persistence semantics, actual retrieval quality, model-call outcomes, end-to-end approval enforcement, deployment compatibility or successful cross-tool synchronization. The bridge's calls establish intended integration points, not the behavior of their recipients. Agent recommendations in `AGENTS.md` are target-authored design claims, not verified integrations. SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`, `prior-art/v0-glue/jarvis_kb/vault_sync.py`, `AGENTS.md`.

The immutable applicability boundary is commit `0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92`, with an analysis cutoff of **2026-10-15**. No later revisions or live pages supply evidence. The overall tier is **doc-grounded**, because the unified system is a proposal; static implementation evidence exists for the legacy bridge and SQL schema only. No target code, tests or examples were executed. No observed-run or causal-experiment evidence was supplied. The prior-art guide's assertion that its prototype works is reported operation, not an independently inspected run. SRC-1, `README.md`, `prior-art/README.md`.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/noirblue/IsaacCLupus_mnemosyn_spec` | 0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92 | doctrine/design; implementation; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-16-isaacclupus-mnemosyn-spec/related-systems/noirblue--IsaacCLupus_mnemosyn_spec`. Doctrine/design: `README.md`, `ARCHITECTURE.md`, `SPECIFICATION.md`, `AGENTS.md`, `GETTING_STARTED.md`, `ROADMAP.md`, `schema/README.md`, `python_thoughts/README.md`, `rust_thoughts/README.md`. Implementation: `schema/001-init.sql`; `prior-art/v0-glue/pyproject.toml`, `prior-art/v0-glue/config.yaml`, `prior-art/v0-glue/jarvis_kb/cli.py`, `prior-art/v0-glue/jarvis_kb/config.py`, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`, `prior-art/v0-glue/jarvis_kb/ollama_proxy.py`, `prior-art/v0-glue/jarvis_kb/vault_sync.py`, and both `prior-art/v0-glue/systemd/` service units. Reported operation: `prior-art/README.md`. | Doctrine: [canonical specification](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec/blob/0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92/SPECIFICATION.md). Implementation: [bridge driver](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec/blob/0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92/prior-art/v0-glue/jarvis_kb/cli.py), [publication and reload](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec/blob/0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92/prior-art/v0-glue/jarvis_kb/vault_sync.py). Reported operation: [prototype account](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec/blob/0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92/prior-art/README.md). | No checkout access gap. External backend implementations and live execution evidence are absent; the unified runtime is proposed. Design supports declared contracts, bridge code supports static integration behavior, and reported operation supports attribution only. None establishes successful end-to-end operation or causal effects. |
