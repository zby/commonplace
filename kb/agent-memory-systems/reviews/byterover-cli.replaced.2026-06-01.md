---
description: "ByteRover CLI review: file-backed context tree with curate/query agents, BM25 retrieval, summaries, manifests, VC, review gates, MCP, and trace-derived runtime ranking"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# ByteRover CLI

> Replaced 2026-06-01. See [byterover-cli](./byterover-cli.md) for the current review.

ByteRover CLI is a TypeScript/Oclif system by ByteRover/Campfire for giving coding agents a persistent project context tree. The shipped package exposes `brv` as an interactive React/Ink REPL, daemon-routed CLI, web UI, MCP server, connector installer, and cloud-backed version-control surface. The memory substrate is not a hidden vector database: canonical knowledge lives under a project `.brv/context-tree/` as markdown files, while derived summaries, manifests, archive stubs, curate logs, query logs, review backups, and runtime ranking signals sit beside that tree in local data stores and cloud sync paths.

**Repository:** https://github.com/campfirein/byterover-cli

**Reviewed commit:** [93f2514378c114a5293b22f6e7bf5a029078093d](https://github.com/campfirein/byterover-cli/commit/93f2514378c114a5293b22f6e7bf5a029078093d)

## Core Ideas

**A markdown context tree is the canonical memory substrate.** `FileContextTreeService` initializes and resolves `.brv/context-tree/`, and the curate tool writes domain/topic/subtopic markdown entries with semantic frontmatter, facts, raw concepts, narrative sections, snippets, relations, and timestamps ([file-context-tree-service.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/context-tree/file-context-tree-service.ts), [curate-tool.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/agent/infra/tools/implementations/curate-tool.ts), [markdown-writer.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/core/domain/knowledge/markdown-writer.ts)). These markdown entries are knowledge artifacts when read as evidence or context by `brv query`, MCP `brv-query`, search, and the web UI. They become system-definition artifacts only indirectly, when the agent prompt instructs future agents to ground answers in them or when connectors install ByteRover rules into external agent environments.

**Curation is an agentic write path with a strict operation schema.** `CurateExecutor` preloads user-provided text/files, optionally pre-compacts large context, computes deterministic reconnaissance, and runs an isolated task session whose prompt tells the agent to extract and apply `ADD`, `UPDATE`, `UPSERT`, `MERGE`, or `DELETE` operations through `tools.curate` ([curate-executor.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/executor/curate-executor.ts)). The tool schema requires motivation, confidence, impact, summary, path/title separation, and optional domain/topic context. That means the operative part of a curated file is mixed: prose and structured markdown for future readers, plus symbolic frontmatter and path placement for search, review, sync, and lifecycle machinery.

**Retrieval combines BM25, symbolic tree structure, and runtime signals.** `SearchKnowledgeService` builds a MiniSearch index over context files, summaries, shared sources, and symbol paths, then supports path-like queries, scoped subtree search, overview mode, kind/maturity filters, excerpt extraction, parent-score propagation, and out-of-domain filtering ([search-knowledge-service.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/agent/infra/tools/implementations/search-knowledge-service.ts)). Scores are not BM25 alone: raw BM25 is normalized, blended with sidecar importance and recency, boosted by maturity tier and local-origin preference, then gap-filtered. Returned results accumulate access hits for later sidecar updates. This is ranking influence, not just display metadata.

**Summaries, manifests, abstracts, and archive stubs are derived views with partial lineage.** Directory `_index.md` summaries are generated bottom-up from child hashes and carry `children_hash`, `covers`, token counts, compression ratio, and condensation order ([file-context-tree-summary-service.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/context-tree/file-context-tree-summary-service.ts)). `_manifest.json` allocates active context into summary/context/stub lanes under token budgets and is invalidated by a stat fingerprint ([file-context-tree-manifest-service.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/context-tree/file-context-tree-manifest-service.ts)). Archive stubs point to lossless `.full.md` copies and preserve original path/token metadata ([file-context-tree-archive-service.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/context-tree/file-context-tree-archive-service.ts)). The lineage story is stronger than a plain summary cache but weaker than a fully reproducible build graph: some artifacts have hashes and pointers, while LLM-generated content depends on model behavior and fail-open fallbacks.

**Lifecycle is split between human review, runtime scoring, and "dream" consolidation.** High-impact curate operations and deletes produce pending review metadata and first-write-wins backups, while `brv review approve/reject` and the local review UI update curate-log operation status or restore backed-up files ([file-curate-log-store.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/storage/file-curate-log-store.ts), [file-review-backup-store.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/storage/file-review-backup-store.ts), [review-api-handler.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/http/review-api-handler.ts)). In parallel, runtime signals store access counts, update counts, importance, recency, and maturity in a sidecar instead of markdown frontmatter ([runtime-signal-store.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/context-tree/runtime-signal-store.ts), [runtime-signals-schema.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/core/domain/knowledge/runtime-signals-schema.ts), [memory-scoring.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/core/domain/knowledge/memory-scoring.ts)). Dream cycles then consolidate, synthesize, and prune the tree using changed-file evidence, BM25 related-file search, LLM classification, archive services, and stale-summary propagation ([dream-executor.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/executor/dream-executor.ts), [consolidate.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/dream/operations/consolidate.ts), [synthesize.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/dream/operations/synthesize.ts), [prune.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/dream/operations/prune.ts)).

**Adoption is treated as an integration problem, not only a data model.** The README advertises REPL, web UI, cloud sync, MCP, hub packages, connectors, and many LLM providers ([README.md](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/README.md), [package.json](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/package.json)). The code backs that up: `ByteRoverMcpServer` exposes `brv-query` and `brv-curate` over MCP, while `ConnectorManager` installs hook, MCP, rules, and skill connectors for supported agents ([mcp-server.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/mcp/mcp-server.ts), [brv-query-tool.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/mcp/tools/brv-query-tool.ts), [brv-curate-tool.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/mcp/tools/brv-curate-tool.ts), [connector-manager.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/connectors/connector-manager.ts)). Version control is also first-class: the daemon handles add, commit, branch, checkout, clone, fetch, merge, pull, push, diff, status, reset, and remote operations through isomorphic-git over the context tree ([vc-handler.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/transport/handlers/vc-handler.ts), [isomorphic-git-service.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/git/isomorphic-git-service.ts)).

## Comparison with Our System

| Dimension | ByteRover CLI | Commonplace |
|---|---|---|
| Primary substrate | `.brv/context-tree/` markdown plus sidecars, daemon state, logs, and optional cloud VC | Repo KB under `kb/`, with typed notes, indexes, instructions, reviews, and deterministic validators |
| Main consumer | Coding agents and developers using `brv`, MCP, TUI, web UI, and connectors | Agents and maintainers navigating a methodology KB through files, indexes, skills, and commands |
| Canonical knowledge | Curated context markdown files with semantic frontmatter | Typed markdown artifacts whose collection/type contracts define quality and use |
| Derived views | `_index.md`, `.abstract.md`/`.overview.md`, `_manifest.json`, archive stubs, query summaries | Directory indexes, curated indexes, generated reports, validation/review outputs |
| Retrieval | BM25 plus symbolic paths, parent propagation, maturity filters, runtime score sidecar, direct-response tiers | `rg`, descriptions, indexes, authored links, and skill-guided navigation |
| Learning loop | Access/update signals alter importance, maturity, ranking, manifest allocation, pruning; dream can synthesize and consolidate | Review bundles, validation, manual/agent revision, and promotion from workshop to library |
| Governance | HITL review for high-impact/deleting curate ops; VC for context tree; fail-open derived maintenance | Deterministic validation, semantic review runs, explicit collection/type contracts, git review |
| Integration surface | Productized CLI, daemon, web UI, MCP tools, connector installers, provider switching, cloud sync | Local skills and `commonplace-*` commands, intentionally repo-native and methodology-focused |

The strongest alignment is the shared commitment to inspectable files as the durable substrate. ByteRover's canonical memories are markdown files that can be searched, versioned, merged, archived, reviewed, and rendered. That makes it much closer to commonplace than systems whose only retained state is an embedding store or opaque service object.

The main divergence is where authority lives. In commonplace, the behavior-shaping contract is mostly in explicit artifact types, collection conventions, validation, and authored links. ByteRover pushes more authority into runtime services: the daemon chooses retrieval tiers, the search service ranks by sidecar signals, dream decides consolidation/pruning candidates, review logs gate high-impact changes, MCP tools queue writes, and connectors insert ByteRover into external agents. Its context entries are knowledge artifacts, but its sidecars, tool schemas, review status, manifest lanes, and connector rules are system-definition artifacts because they route, rank, validate, enforce, or configure future behavior.

ByteRover is also more productized. It has the adoption affordances commonplace deliberately avoids: OAuth, provider switching, cloud space sync, web dashboard, TUI, MCP, connectors, and an internal context-tree VC. Commonplace is thinner operationally but more explicit methodologically: it explains why note types, link labels, review flows, and workshop/library boundaries matter. ByteRover is a rich implementation of an agent-facing memory product; commonplace is a framework for designing and reviewing such systems.

**Read-back:** both — agents can call `brv-query`, and query/connector services inject ranked context-tree results into prompts.

## Borrowable Ideas

**Separate canonical prose from runtime ranking signals.** ByteRover moved importance, recency, maturity, access count, and update count out of markdown into a sidecar so ordinary query use does not dirty shared files. Commonplace should borrow the principle if it ever adds usage-derived ranking: keep canonical note prose reviewable under git, and keep volatile usage telemetry in a separate, explicitly lower-authority substrate. Ready as a design principle; needs a concrete search/ranking use case before implementation.

**Use manifest lanes as a compiled context budget.** `_manifest.json` allocates summaries, contexts, and stubs into separate token lanes and resolves them for query prompt injection. A commonplace analogue could compile descriptions, curated indexes, active workshop state, and selected notes into lane-budgeted bundles for specific agent tasks. Not ready by default; useful if we build an agent scheduler that needs predictable context budgets.

**Make review backups first-write-wins.** ByteRover's review backup store captures the pre-curate file content once, then preserves that snapshot through later operations until approval/rejection. That is a clean pattern for reversible agent edits. Commonplace review runs already preserve artifacts, but a first-write-wins backup rule would be useful for any future auto-fix system that can touch library notes.

**Treat query logs as evaluation data, not just debugging logs.** ByteRover records query tiers, matched documents, timings, search metadata, and coverage summaries. Commonplace's semantic review system evaluates notes, but it does not yet measure navigation demand or retrieval failure patterns. A lightweight query/navigation log could identify notes that are often needed but poorly discoverable. Needs privacy and workflow clarity before use.

**Expose curation through MCP only after the write path has governance.** `brv-curate` is fire-and-forget, but the underlying curate path has operation schemas, review metadata, backups, and review disable semantics. That ordering is worth copying: make an agent-callable write tool only after rejection, audit, and review surfaces exist.

**Let background consolidation write ordinary artifacts.** Dream syntheses are written as regular context files and seeded into the same runtime-signal store rather than hidden in a separate "dream output" silo. If commonplace adds background consolidation, outputs should land in ordinary workshop/library artifacts with normal validation and review, not in a private cache.

## Trace-derived learning placement

ByteRover qualifies, but the trace-derived mechanism is narrower than "learns from full conversations." The durable learning signal is mostly retrieval and curation telemetry translated into ranking/lifecycle state.

**Trace source.** The raw signal includes query/search access events, returned result paths, curate updates, and task/query logs. `SearchKnowledgeService` accumulates access hits for returned result paths, `QueryLogHandler` stores query task traces and matched documents, and curate writes bump update counts ([search-knowledge-service.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/agent/infra/tools/implementations/search-knowledge-service.ts), [query-log-handler.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/server/infra/process/query-log-handler.ts), [curate-tool.ts](https://github.com/campfirein/byterover-cli/blob/93f2514378c114a5293b22f6e7bf5a029078093d/src/agent/infra/tools/implementations/curate-tool.ts)).

**Extraction.** There is no transcript parser or reflective lesson extractor on the ranking path. Extraction is deterministic: returned result path -> access-count bump; curate update -> update-count and recency bump; importance -> maturity tier through fixed thresholds and hysteresis. Dream synthesis is LLM-mediated, but its source is domain summaries and changed context-tree files, not raw agent transcripts.

**Storage substrate.** Raw query traces live as JSON query-log files in the project data directory. Reviewable curation traces live as curate-log JSON plus review backups. The distilled ranking state lives in the runtime-signal sidecar keyed by context-tree relative path. Canonical memories remain markdown in `.brv/context-tree/`.

**Representational form.** The runtime-signal operative part is symbolic/numeric state: `importance`, `recency`, `maturity`, `accessCount`, and `updateCount`. Curated markdown is prose plus symbolic frontmatter. Query logs are structured audit records and analytics inputs, not direct prompt context by default.

**Lineage.** Runtime signals retain little source lineage beyond the affected path and aggregate counters. Query logs preserve richer evidence about query, tier, matched documents, timing, and search metadata, but the sidecar ranking state does not point back to the exact queries that caused each bump. Derived summaries have better lineage through child hashes and coverage metadata; archive stubs preserve pointers to full archived content.

**Behavioral authority.** Query logs are knowledge artifacts for audit and recall analytics. Runtime signals are system-definition artifacts: they influence retrieval ranking, manifest allocation, maturity filters, archive candidacy, and pruning protection. Review statuses are also system-definition artifacts because they determine whether changed files can be approved, rejected, pushed, or restored.

**Scope and timing.** The learning is per project/context tree, online during ordinary use, and accumulative across query/curate operations. It is not cross-project model training and it does not produce weights or embeddings.

**Survey placement.** On the survey axes, ByteRover is best placed as usage-derived symbolic ranking and lifecycle control over a file-backed KB. It strengthens the claim that trace-derived learning does not have to mean transcript-to-prose distillation: small numeric sidecars can meaningfully change future agent behavior when they control activation, ranking, and retirement.

## Curiosity Pass

**The system is more hybrid than the README's "context tree" shorthand suggests.** The durable user-facing story is markdown, but important behavior lives in sidecars, daemon routing, task lifecycle hooks, review logs, query logs, manifests, and cloud VC. That is not a criticism; it is the real architecture. The markdown tree is canonical for knowledge content, not for every behavior-shaping fact.

**The lineage model is uneven.** Summary and manifest artifacts have explicit invalidation hashes or fingerprints. Archive stubs point to full preserved content. Runtime signals, however, collapse many usage events into counters without retaining why the importance changed. That is acceptable for ranking, but weak for audit: a future reviewer can see that a file became important, not what user need made it important.

**Fail-open behavior keeps the product usable but weakens guarantees.** Summary generation, manifest rebuilds, sidecar writes, archive candidate scans, and dream operations often catch errors and continue. This is sensible for a developer tool, but it means operators should treat derived views as opportunistic accelerators rather than hard invariants.

**The direct-response tier is a bold authority move.** `QueryExecutor` can skip the LLM when search results are strong enough, formatting a direct answer from curated files. That is efficient and grounded, but it gives the retrieval threshold a lot of behavioral authority: below the threshold, the system synthesizes; above it, it largely quotes structured stored knowledge.

**Dream is promising but governance-heavy.** Consolidate, synthesize, and prune are exactly the maintenance jobs a growing context tree needs. They also touch source-of-truth files and can archive or merge knowledge. ByteRover mitigates this with logs, review entries, undo history, backups, and sidecar maturity, but the maintenance loop is complex enough that most bugs will be governance bugs, not storage bugs.

**The benchmark claims should be read as product claims unless the paper and harness are reviewed separately.** The README reports strong LoCoMo and LongMemEval-S results, but this review inspected the CLI implementation, not the paper methodology or benchmark harness. The code clearly implements a serious memory system; the benchmark numbers need their own source-grounded review before being used as evidence for design decisions.

## What to Watch

- Whether runtime signals gain auditable lineage from query logs, so importance/maturity changes can be explained instead of only observed.
- Whether dream operations become more deterministic or remain LLM-mediated maintenance with broad fail-open behavior.
- Whether the context-tree VC matures enough to make sidecar/local-state conflicts, cloud sync, and review status easy for teams to reason about.
- Whether MCP and connector surfaces converge on the same behavioral contract as the CLI/TUI, or drift into separate agent-facing semantics.
- Whether benchmark code and paper details are published in enough detail to evaluate retrieval, curation, and dream separately.

---

Relevant Notes:

- [Files not database](../../notes/files-not-database.md) - exemplifies: ByteRover keeps canonical memories in inspectable markdown while using services and sidecars around them
- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - compares-with: ByteRover's curate logs, review backups, query logs, dream logs, and review UI are a concrete workshop layer around the context tree
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - extends: ByteRover shows a narrow trace-derived path where usage events become ranking/lifecycle state rather than prose lessons
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - defined-in: curated context entries are usually consumed as evidence, reference, context, or advice
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - defined-in: runtime signals, review status, manifests, MCP schemas, and connector rules have routing, ranking, validation, or configuration force
- [Pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) - converges: ByteRover's summaries, manifests, archive stubs, excerpts, and symbolic paths are several pointer layers over the same markdown tree
- [Napkin](./napkin.md) - compares-with: both use markdown and progressive retrieval, but Napkin stays closer to an Obsidian-vault CLI while ByteRover adds daemon services, sidecar ranking, review logs, VC, MCP, and cloud collaboration
