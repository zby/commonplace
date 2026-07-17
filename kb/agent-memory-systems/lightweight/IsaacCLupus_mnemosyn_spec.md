---
description: "Lightweight doc-grounded coverage of Mnemosyne, a spec-first local semantic memory OS with unified SQLite, vault, MCP, and agent-pack design"
type: ../types/agent-memory-system-review.md
source-tier: doc-grounded
traits: [has-comparison, has-external-sources]
tags: [trace-learning]
last-checked: "2026-06-18"
---

# Mnemosyne / IsaacCLupus mnemosyn spec

Mnemosyne, in `noirblue/IsaacCLupus_mnemosyn_spec`, is a specification for a local-first "semantic memory OS" intended to unify Synto, Synthadoc, LLM-WIKI-MCP, and Link behind one vault, one SQLite schema, and MCP/REST/CLI interfaces. Coverage here is **doc-grounded**: the repository declares itself a concept / architecture proposal, with a schema migration and a superseded v0 glue prototype rather than a current reference implementation.

**Source:** [noirblue/IsaacCLupus_mnemosyn_spec](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec)

**Reviewed commit:** [0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec/commit/0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92)

## Core Ideas

- **The target product is an OS-like substrate, not an agent loop.** The docs frame agents as clients that call Mnemosyne through MCP, REST, or CLI while the OS owns vault layout, database state, job queue, audit, publication, and packs ([AGENTS.md](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec/blob/0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92/AGENTS.md), [ARCHITECTURE.md](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec/blob/0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92/ARCHITECTURE.md)). The repository's root `AGENTS.md` is recommendation and architecture prose, not an activation file loaded by an external agent.
- **A single SQLite schema is the strongest executable artifact.** `schema/001-init.sql` defines `pages`, `links`, `jobs`, `conversations`, `audit_log`, `contradictions`, views, indexes, WAL, and triggers, while `SPECIFICATION.md` adds API schemas and approved Phase 2 fields such as write guards, receipts, conversation tiers, and user profiles ([schema/001-init.sql](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec/blob/0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92/schema/001-init.sql), [SPECIFICATION.md](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec/blob/0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92/SPECIFICATION.md)).
- **Memory is specified as a lifecycle.** The target vault separates `raw/`, `wiki/.drafts/`, published `wiki/`, `memory/inbox/`, `memory/committed/`, and `packs/`; agent memories are proposed into inbox, audited, human-approved, committed, and eventually archived ([ARCHITECTURE.md](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec/blob/0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92/ARCHITECTURE.md), [AGENTS.md](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec/blob/0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92/AGENTS.md)).
- **Context efficiency is a design requirement, not an observed mechanism.** The spec gives `kb_ask` a `context_budget`, `history_budget`, hybrid search, graph context retrieval, source budgets, and pack exports, but the roadmap still places the core engine, MCP server, conversation history, graph retrieval, and REST layer in future phases ([SPECIFICATION.md](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec/blob/0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92/SPECIFICATION.md), [config.sample.yaml](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec/blob/0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92/config.sample.yaml), [ROADMAP.md](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec/blob/0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92/ROADMAP.md)).
- **The v0 glue layer explains the design pressure but is not the current system.** The prior-art package exposes a working `jarvis-kb` CLI, MCP gateway, vault sync, and Ollama proxy over four separate tools, and its README explicitly says it is functional, not maintained, and superseded by the unified architecture ([prior-art/README.md](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec/blob/0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92/prior-art/README.md), [prior-art/v0-glue/jarvis_kb/mcp_gateway.py](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec/blob/0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92/prior-art/v0-glue/jarvis_kb/mcp_gateway.py)).

## Artifact analysis

Claim-level, from specification documents and schema:

- **Storage substrate:** `files` `sqlite` — The claimed target persists human-readable vault files plus one `state.db`; the reviewed repository itself persists the design as repo files and a runnable SQL migration, not as a working Mnemosyne store.
- **Representational form:** `prose` `symbolic` — The behavior-shaping design is prose architecture plus symbolic SQL DDL, JSON tool schemas, REST endpoints, config keys, vault paths, job priorities, and lifecycle enums. Optional vectors and model calls are specified as future query/embedding machinery, not inspected retained parametric state.
- **Lineage:** `authored` `imported` `trace-extracted` — The spec's main artifacts are authored; the target design imports raw notes, papers, documents, and migrated tool outputs; Phase 2 conversation memory and user profile proposals are reported as extracted from conversations. No implementation was inspected that performs those extractions.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Published pages and packs would advise agents as knowledge; generated pack entrypoints and MCP tool descriptions would instruct; write guards, approval, audit, and contradictions would enforce or validate; jobs, namespaces, links, graph retrieval, and API surfaces would route; search budgets, priorities, and future heat scores would rank or learn. These are claimed authorities in the design, not observed runtime behavior.

The promotion path is unusually explicit for a spec-first project: raw source or proposed memory becomes a draft, then an audited and approved published page or committed memory, then a pack/index/graph artifact for agent consumption. The strongest current executable substrate for that path is the schema; the reference implementation that would keep the path honest is still future work.

## Comparison with Our System

Mnemosyne and Commonplace share the basic bet that agent memory should be inspectable, local, lifecycle-aware, and governed by typed artifacts rather than hidden prompt sludge. Mnemosyne's design is more service-shaped: one SQLite state database, job queue, API surface, and pack export layer. Commonplace is more repo-native: Markdown artifacts, collection contracts, schemas, validation, review reports, and generated indexes remain the primary system surface.

The key divergence is implementation authority. Commonplace's methodology is itself running in this repository: collection contracts, validators, skills, and review workflows are executable today. Mnemosyne's current repository is a blueprint with a schema and prior-art glue. That makes its ideas easy to compare, but the review has to treat most behavior as proposed.

### Borrowable Ideas

- **One schema for lifecycle state.** Commonplace could eventually benefit from a narrow SQLite sidecar for job receipts, review runs, or search traces, but only where the repo files should remain source of truth. Needs a concrete bottleneck.
- **Agent packs as generated consumption artifacts.** A generated package containing an index, graph adjacency, audit summary, and entrypoint instructions is a useful way to separate authoring artifacts from agent-facing context. Ready as a design pattern, not as default behavior.
- **Receipts for agent-submitted intents.** The proposed `receipts` table is a clean vocabulary for "who asked, what was routed, what artifacts resulted." Commonplace review and snapshot commands could use that pattern when provenance needs to survive beyond shell history.
- **Write guards distinct from review status.** Mnemosyne separates content hash protection from lifecycle stage. Commonplace already has validation/review status; explicit write-guard semantics would only be useful for generated or hand-protected files.

## Write side

**Write agency:** `manual` `automatic` — The spec proposes manual approval and hand-edit protection plus automatic ingestion, extraction, compilation, audit, publish, query synthesis, profile extraction, heat updates, decay, and pack/index rebuilds. The current repository does not implement the Mnemosyne write loop beyond schema/prototype scaffolding.

**Curation operations:** `synthesize` `promote` `decay` — The claimed system writes cited synthesis pages from retrieved knowledge, promotes drafts/proposed memories through approval into published or committed locations, and decays or archives conversation/memory state through the Phase 2 conversation-memory design. Treat these as specified operations, not verified implementation behavior.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` — The docs specify conversation rows, receipts, agent ids, intents, routes, phase logs, and user profile extraction from conversations.

**Learning scope:** `per-project` `cross-task` — The target `kb_remember` accepts a project, while committed memory and profiles are meant to persist across later sessions in the same local vault.

**Learning timing:** `online` `staged` — Conversations and receipts are recorded during use; profile extraction, heat decay, memory promotion, audit, and publish are described as staged jobs or approval steps.

**Distilled form:** `prose` `symbolic` — Proposed memories and generated wiki/synthesis pages are prose; profile rows, heat scores, receipts, stages, statuses, and links are symbolic. No parametric learned artifact is claimed for this path.

The reported learning loop is conversation or agent-event trace to proposed memory/profile/lifecycle state, with human approval before long-term committed memory. This is closer to Commonplace's review-gated promotion than to systems that directly inject every extracted fact into future prompts.

## Read-back

**Read-back:** `both` — The target design is pull through `kb_search`, `kb_ask`, REST query/graph endpoints, and CLI commands; it also claims a push-like export path through `packs/INDEX.json`, `packs/graph/links.json`, audit data, and `pack/AGENTS.md`, which would be generated agent-facing context if implemented. The repository's root `AGENTS.md` does not count as this push path because it is ordinary architecture/recommendation prose.

**Read-back signal:** `coarse` — The claimed pack entrypoint is coarse generated context for an external agent rather than instance-specific relevance targeting. Pull tools carry their own query, budget, and scope arguments.

**Faithfulness tested:** `no` — I found no behavioral test or ablation showing that generated packs, MCP tool results, or remembered facts alter agent behavior correctly.

The pull side is the better-specified path: `kb_search` returns top-k results, `kb_ask` carries context and history budgets, and REST/CLI surfaces mirror the same operations. The push side is only a planned export/activation surface. Its quality would depend on generated pack contents, how an external agent loads `pack/AGENTS.md`, and whether pack indexes preserve enough provenance.

Authority at consumption is intended to vary by surface. Search and ask results are advisory knowledge; committed memory and published wiki pages can become prompt context; write guards, audit results, and contradictions can block or route publication; packs would compile knowledge into an agent-consumable form. Effective authority is not verifiable from the spec alone.

## Curiosity Pass

- The spec is strongest where it is least glamorous: the unified schema and lifecycle vocabulary are more concrete than the agent recommendations.
- There is a small mismatch between `SPECIFICATION.md` and `schema/001-init.sql`: the spec says Phase 2 fields such as `write_guard`, receipts, and conversation tiers are approved, while the checked-in initial migration still contains the Phase 1 shape.
- The v0 glue code supports the diagnosis that four-tool integration is brittle, but it does not prove the unified OS design works. It proves the pain and some gateway shapes.
- The proposed `pack/AGENTS.md` is exactly the sort of AGENTS-style artifact that could count as activation if generated from a vault. The repository's root `AGENTS.md` is not that artifact.

## What to Watch

- A reference implementation of `state.db`, migrations, and the basic MCP server. That would promote this from doc-grounded to code-grounded review material.
- Whether generated packs actually include source ids, maturity, audit status, and graph edges compact enough for agent use.
- Whether conversation memory extraction keeps human approval as a real gate or becomes ambient automatic prompt memory.
- Whether the schema migration catches up with the approved Phase 2 fields or splits them into later migrations.

## Relevant Notes

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Mnemosyne's stored pages and memory rows only become active through pull tools or generated packs.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Mnemosyne's vault files, SQLite rows, API schemas, packs, and audit records have different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: published pages, committed memories, synthesis pages, packs, and search results primarily advise future work.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: schema, tool contracts, write guards, lifecycle stages, pack entrypoints, and audit gates shape or constrain behavior.
- [Use Trace Extraction As Meta-Learning](../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) - compares: Mnemosyne's proposed conversation/profile loop extracts durable behavior-shaping artifacts from traces while retaining a human gate.
- [Keep Lineage And Compiled Views From Drifting](../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) - warns: generated wiki pages, synthesis answers, and packs need source alignment if they become agent-facing context.
