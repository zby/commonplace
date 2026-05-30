---
description: "Stash review: self-hosted Postgres/pgvector MCP memory backend that consolidates agent-written episodes into facts, relationships, goals, failures, hypotheses, and decay state"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# Stash

Stash is Mohamed Al-Ashaal's Go service for self-hosted agent memory behind MCP. It stores raw agent-written observations as embedded episodes in PostgreSQL/pgvector, then a consolidation service derives facts, relationships, causal links, patterns, goal annotations, failure repeats, hypothesis state, contradictions, and confidence decay. Compared with commonplace, it is a compact database-backed memory backend with strong agent tool prompts and weak review/governance machinery.

**Repository:** https://github.com/alash3al/stash

**Reviewed commit:** [10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c](https://github.com/alash3al/stash/commit/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c)

**Last checked:** 2026-05-16

## Core Ideas

**The storage substrate is PostgreSQL plus pgvector, not files.** Migrations create `namespaces`, `episodes`, `facts`, `fact_sources`, `relationships`, `patterns`, `contexts`, `consolidation_progress`, `embedding_cache`, `contradictions`, `causal_links`, `hypotheses`, `goals`, and `failures` ([migrations](https://github.com/alash3al/stash/tree/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/db/migrations)). Startup runs goose migrations, applies configured vector dimensions to embedding columns, creates HNSW indexes over episode and fact embeddings, stores vector-dimension/model metadata, and wraps embeddings with a database cache ([database bootstrap](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/db/db.go), [embedding cache](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/embedder/cache.go)). Docker Compose runs a pgvector Postgres container plus the Stash MCP server with background consolidation enabled ([docker-compose.yml](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/docker-compose.yml)).

**Namespaces are hierarchical paths with descendant expansion.** Namespace slugs are path-like strings such as `/projects/myapp`; validation requires lowercase path segments, `/` means all namespaces, and each path expands to itself plus descendants for list/recall/query operations ([namespace resolution](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/brain/brain.go), [namespace migration](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/db/migrations/00002_create_namespaces.sql)). The MCP `init` tool creates `/self`, `/self/capabilities`, `/self/limits`, and `/self/preferences`, making self-model memory an ordinary namespace convention rather than a special store ([MCP server](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/cmd/cli/mcp.go)).

**Episodes and facts are separate retained artifacts.** `Remember` validates content and namespace, embeds the text, and inserts an `episodes` row with content, embedding, model, occurrence time, and soft-delete field ([episode service](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/brain/episode.go), [episodes table](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/db/migrations/00004_create_episodes.sql)). Consolidation clusters new episodes by cosine similarity, asks the reasoner for a grounded structured fact, embeds the fact, deduplicates by vector similarity, writes `facts`, and records source episode links in `fact_sources` ([consolidation](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/brain/consolidate.go), [facts table](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/db/migrations/00005_create_facts.sql), [fact sources](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/db/migrations/00006_create_fact_sources.sql)). Episodes are raw knowledge artifacts; facts are distilled knowledge artifacts with stronger retrieval priority and some system-definition force when confidence, expiry, contradiction, and hypothesis promotion affect future answers.

**Recall is facts-first with episode fallback.** `Recall` embeds the query, resolves namespaces, searches facts first up to the requested limit, then searches episodes only for remaining slots, and sorts the combined results by score ([recall service](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/brain/recall.go), [recall SQL](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/queries/recall.sql.tmpl)). This gives consolidated facts higher behavioral authority than raw episodes: both are retrieved as context, but raw episodes are a fallback when the distilled layer is sparse.

**Consolidation is staged and checkpointed.** The public result names more than the README's three-stage comment: episode-to-fact extraction plus contradiction detection, fact-to-relationship extraction, causal-link extraction, goal-progress inference, failure-pattern detection, pattern extraction, hypothesis-evidence scanning, and SQL confidence decay all run in one consolidation pass ([consolidation driver](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/brain/consolidate.go)). `consolidation_progress` stores per-namespace checkpoints for last episode, fact, relationship, pattern sources, goal-progress facts, failure rows/episodes, hypothesis facts, decay run, and last run ([progress migrations](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/db/migrations/00010_create_consolidation_progress.sql), [checkpoint extension](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/db/migrations/00020_add_consolidation_checkpoints.sql)). Several stages advance checkpoints only after successful processing, which gives generated artifacts a minimal regeneration boundary.

**The structured memory families are real tables, not just prompt language.** Relationships are typed entity edges sourced from facts; causal links connect cause/effect fact IDs; contradictions compare facts with matching entity/property and can auto-supersede old facts; patterns abstract across multiple facts/relationships; goals are persistent outcomes with active/completed/abandoned status; failures store content/reason/lesson; hypotheses move through proposed/testing/confirmed/rejected and confirmation creates a fact ([relationships](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/db/migrations/00007_create_relationships.sql), [causal links](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/brain/causal.go), [contradictions](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/brain/contradiction.go), [patterns](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/db/migrations/00008_create_patterns.sql), [goals](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/brain/goal.go), [failures](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/brain/failure.go), [hypotheses](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/brain/hypothesis.go)).

**The reasoner is prompt-constrained JSON extraction with local validation.** The OpenAI-compatible reasoner uses a strict system prompt, explicit JSON schemas in prompts, one retry after invalid output, ID filtering for patterns/causal links/goals/hypotheses/failures, confidence clamping, relationship entity grounding, and an anti-verbatim check for synthesized facts ([reasoner interface](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/reasoner/reasoner.go), [OpenAI reasoner](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/reasoner/openai.go)). These prompts and validators are system-definition artifacts: they decide what can become structured memory and what IDs can receive update authority.

**Agent surfaces are CLI, MCP, minimal HTTP, and background service.** The CLI exposes namespace, remember/recall/forget, purge, facts, consolidate, context, contradictions, causal links, hypotheses, goals, failures, HTTP, MCP, and `serve` commands ([CLI entrypoint](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/cmd/cli/main.go)). The MCP server exposes tools for initialization, recall, writes, consolidation, fact/relationship queries, contradiction resolution, causal tracing, hypothesis/goal/failure management, and can run over SSE or stdio with optional consolidation ticker ([MCP server](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/cmd/cli/mcp.go)). HTTP is operational only: `/metrics`, `/healthz`, and `/readyz`, not a memory API ([HTTP server](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/cmd/cli/server.go)). `serve` runs HTTP, MCP SSE, and consolidation together ([serve-all command](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/cmd/cli/serve_all.go)).

## Comparison with Our System

| Dimension | Stash | Commonplace |
|---|---|---|
| Primary artifact | Database rows: episodes, facts, relationships, patterns, goals, failures, hypotheses, contexts, checkpoints | Typed markdown notes, sources, instructions, reviews, ADRs, generated indexes |
| Storage substrate | PostgreSQL with pgvector, HNSW indexes, settings, embedding cache | Git-tracked files plus deterministic generated reports/indexes |
| Representational form | Mixed prose rows, symbolic schemas/SQL state, vector embeddings, numeric confidence/checkpoint state | Mostly prose plus frontmatter, links, schemas, scripts, validation reports |
| Lineage | `fact_sources`, source fact IDs, relationship IDs, hypothesis source IDs, checkpoint cursors | Source snapshots, commit-pinned reviews, authored links, archive/replacement lifecycle |
| Activation | MCP prompts/tools, facts-first vector recall, namespace expansion, background consolidation | `rg`, descriptions, indexes, authored links, skills, validation/review commands |
| Authority | Prompt contract, reasoner schemas, confidence decay, contradiction/hypothesis transitions, retrieval ranking | Type specs, collection contracts, AGENTS.md, skills, validation/review commands |

Stash is much closer to a self-hosted memory service than a knowledge base. Its agent reads and writes through MCP/CLI tools; durable state is opaque rows and embeddings; and consolidation is a background process. Commonplace keeps the canonical artifact readable and reviewable as a file, while Stash makes retrieval and consolidation the primary interface.

The strongest design split is artifact authority. A Stash episode is a raw knowledge artifact: it records something the agent or user asserted. A fact is a distilled knowledge artifact, but it also gains system-definition force through confidence, validity windows, contradiction supersession, recall ordering, and hypothesis confirmation. Relationships, causal links, goals, failures, and hypotheses similarly straddle advice and control: they are evidence when listed, but they route future search, planning, caution, and status decisions when tools and prompts tell the agent to use them.

Stash has better runtime ergonomics than commonplace for arbitrary MCP-compatible agents. The prompt templates tell an agent when to initialize, recall, remember, create goals, log failures, and end a session; the tool catalog makes those actions available without teaching the agent the database schema ([MCP prompts](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/cmd/cli/mcp_prompts.tmpl)). Commonplace has stronger governance over what a retained artifact means: type specs, collection rules, validation, review sweeps, replacement archives, and explicit source citations.

Stash's lineage is useful but not sufficient for epistemic review. `fact_sources`, source IDs on patterns/hypotheses, contradiction records, checkpoints, and timestamps help reconstruct derivation. They do not provide reviewed claims, source excerpts, extraction prompt/model version per row, human approval state, supersedes links for patterns, or a file-level diff a maintainer can inspect before promotion.

The governance gap is therefore not storage seriousness; the database model is substantial. The gap is authority management. Any MCP client that can reach the service appears able to call memory-changing tools; the checked-in HTTP surface has no memory API, and the MCP surface has no authentication, approval queue, namespace ACL, audit review, redaction, retention policy, or trust-tier distinction beyond soft deletes, purge commands, contradiction resolution, and namespace organization.

**Read-back:** pull — agents deliberately call MCP or CLI recall/query tools, which return facts first and raw episodes as fallback context.

## Borrowable Ideas

**Facts-first fallback to raw episodes.** Ready as a retrieval pattern. Commonplace already distinguishes notes from sources; a future search surface could prefer reviewed claims and fall back to raw snapshots or logs only when the reviewed layer is sparse.

**Checkpoint each derived stage separately.** Useful if commonplace adds heavier generated views. Stash's per-stage cursors avoid rescanning everything and make failed stages less likely to lose unprocessed input. The file-backed analogue would be generated-view manifests keyed by source artifact revision.

**Keep failure and hypothesis memory first-class.** Stash's `failures` and `hypotheses` tables are more operational than generic notes. Commonplace should not import the database schema, but task reviews and workshop artifacts could benefit from explicit "failed approach + lesson" and "uncertain claim + verification plan" forms.

**Use tool descriptions as behavior-shaping artifacts.** The MCP prompt template is one of Stash's strongest parts. It tells agents when memory is mandatory, how to choose namespaces, what not to store, and how to end sessions. Commonplace can borrow the packaging lesson for command/tool descriptions while keeping canonical policy in reviewed files.

**Do not borrow opaque consolidation as the source of truth.** Stash's fact extraction, relationship extraction, and pattern synthesis are useful compiled layers. They would be risky as canonical methodology notes because LLM-derived rows have limited review state and weak derivation displays.

## Trace-derived learning placement

Stash qualifies as trace-derived learning when used through its intended MCP contract: the agent stores durable observations from sessions, and consolidation turns those observations into durable structured memory. It is not automatic transcript ingestion; the trace boundary is agent/tool-mediated `remember`, goal, failure, hypothesis, context, and session-summary writes.

**Trace source.** Raw traces are self-contained observations and session summaries written by the agent or user through `remember`, plus explicit goal/failure/hypothesis/context tool calls. The MCP prompt directs agents to store user preferences, corrections, decisions, project facts, failed approaches, useful session summaries, and self-knowledge, and to recall before answering history-sensitive questions ([MCP prompt contract](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/cmd/cli/mcp_prompts.tmpl), [remember tool](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/cmd/cli/mcp.go)).

**Extraction.** Episodes are clustered by embedding similarity, synthesized into grounded structured facts, deduplicated by vector similarity, and linked to source episode IDs. Later stages extract relationships, causal links, patterns, goal progress notes, repeated failures, failure-pattern facts, and hypothesis evidence. The oracle is a mix of LLM JSON extraction, local validation, SQL constraints, confidence thresholds, and manual tool actions such as resolving contradictions, confirming hypotheses, completing goals, and creating failures.

**Storage substrate.** Raw episodes, consolidated facts, relationship/goal/failure/hypothesis/contradiction rows, embeddings, embedding cache, checkpoints, settings, and contexts all live in PostgreSQL. pgvector provides vector columns and HNSW search indexes for episodes and facts; no durable memory artifact is stored as a readable file.

**Representational form.** Episodes, facts, goal notes, failure lessons, hypothesis content, and pattern text are prose. Relationship rows, causal links, contradiction records, goal/hypothesis status, checkpoints, SQL schemas, and prompt schemas are symbolic. Episode/fact embeddings and vector distances are distributed-parametric. Confidence scores, decay thresholds, and auto-confirm/reject thresholds are numeric control state.

**Lineage.** Fact lineage is explicit through `fact_sources`; relationship and causal rows cite fact IDs; patterns cite source fact/relationship IDs; hypotheses can cite source fact IDs and create confirmed facts; contradictions cite old/new fact IDs. Lineage is weaker for row-level extraction context: source snippets, prompt version, model version per extraction, and human review status are not retained with each derived artifact.

**Behavioral authority.** Episodes are knowledge artifacts consumed as evidence or fallback context. Consolidated facts are knowledge artifacts with higher retrieval priority. Relationships, causal links, goals, failures, hypotheses, contradictions, embeddings, checkpoints, prompts, thresholds, and confidence decay become system-definition artifacts when they rank recall, mark facts expired, supersede old facts, instruct agents to avoid repeated failures, advance goals, or confirm/reject hypotheses.

**Scope and timing.** Scope is per namespace and descendant namespace, with `/self` conventions for agent self-knowledge. Timing is online for writes and recall, and staged for consolidation through manual `consolidate`, background MCP consolidation, or the combined service command.

**Survey placement.** Stash strengthens the survey's trace-to-structured-memory axis. It is a trace-derived retrieval and operational-memory backend: traces become facts, edges, goals, failure lessons, hypotheses, contradiction records, confidence state, and vector indexes. It does not strengthen the stronger artifact-learning axis where traces promote into reviewed instructions, tests, skills, or code patches.

## Curiosity Pass

**The MCP prompt is more governance-heavy than the database.** The tool descriptions say agents must initialize, recall before history-sensitive answers, verify namespaces, consolidate periodically, store session summaries, and avoid noisy memory. Those rules shape behavior, but they are prompt-level obligations rather than enforced authorization or review gates.

**The "8-stage" claim is mostly supported, but stage numbering is uneven.** The code implements the named families, though comments still call consolidation "3-stage" while the driver runs contradiction, causal, goal, failure, pattern, hypothesis, and decay steps. Reviewers should trust the driver/result fields more than the README shorthand.

**Facts are not inherently verified.** The reasoner is explicitly strict and locally validated, but it still synthesizes facts from agent-written observations. A fact's confidence is based on cluster size and structured fields, then later decayed or superseded; it is not a human-reviewed truth claim.

**Working context is intentionally short-lived but database-backed.** `contexts` stores one focus per namespace with expiry, so active handoff state is separate from durable episodes/facts ([contexts](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/db/migrations/00009_create_contexts.sql), [context service](https://github.com/alash3al/stash/blob/10bc4e74bfdb1b34a501d0df0dcc5e7c10d1f76c/internal/brain/context.go)). That is a clean authority split: context is operational state, not a canonical memory.

**The CLI surface looks younger than the core.** The command tree includes duplicated `forget` registration and some rough formatting in `main.go`, while the brain/database layers are more coherent. That does not invalidate the memory model, but it suggests the MCP/Docker path is the primary intended path.

## What to Watch

- Whether Stash adds authentication, namespace ACLs, audit logs, redaction, retention policy, or approval gates around MCP writes and consolidation outputs.
- Whether derived rows start retaining prompt/model version, source excerpts, extraction errors, and review state for each fact/relationship/pattern.
- Whether facts-first recall gains explicit score/confidence fusion instead of sorting fact and episode vector scores after a fixed facts-first fill.
- Whether failure lessons and hypotheses become prompt-time guardrails with clearer scope and retirement rules.
- Whether the HTTP surface grows beyond health/metrics into a secured memory API.
- Whether consolidation starts producing reviewed instructions, skills, tests, or other stronger system-definition artifacts rather than database facts and ranking state only.

---

Relevant Notes:

- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: Stash episodes and facts are consumed as evidence, reference, context, and advice.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: Stash prompts, schemas, confidence decay, checkpoints, embeddings, contradiction transitions, and hypothesis/goal state can route or rank future behavior.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - clarifies: the same row can advise when retrieved and control behavior when used by ranking, expiry, or status-transition paths.
- [Storage substrate](../../notes/definitions/storage-substrate.md) - exemplifies: Stash's canonical retained state lives in Postgres/pgvector rather than files.
- [Lineage](../../notes/definitions/lineage.md) - compares: Stash keeps source IDs and checkpoints but lacks reviewable derivation artifacts for every generated claim.
- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Stash is trace-derived through agent-written episodes and consolidation into durable structured memory.
