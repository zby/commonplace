---
description: "Dense-Mem review: self-hosted MCP memory server with Neo4j evidence, typed claims, verifier gates, fact promotion, and tiered recall"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
last-checked: "2026-06-04"
---

# dense-mem

Dense-Mem, from `markhuangai/dense-mem`, is a self-hosted Go memory server for MCP and REST clients. At the reviewed commit it stores evidence fragments, host-extracted claims, promoted facts, community summaries, skill-pack imports, audit/control records, and profile-scoped API keys. The host LLM remains responsible for conversational judgment and candidate extraction; Dense-Mem owns persistence, embeddings, verification, promotion policy, conflict handling, recall, and operational isolation.

**Repository:** https://github.com/markhuangai/dense-mem

**Reviewed commit:** [96158d8b672883d1239f4acc7ab0b7296638d0d7](https://github.com/markhuangai/dense-mem/commit/96158d8b672883d1239f4acc7ab0b7296638d0d7)

**Source directory:** `related-systems/markhuangai--dense-mem`

## Core Ideas

**Memory is a governed graph pipeline.** The central implemented shape is `SourceFragment -> Claim -> Fact`: fragments retain source evidence and embeddings, claims carry typed subject/predicate/object assertions with support links and verification state, and facts are promoted active memory with temporal/status metadata ([internal/domain/knowledge_contract.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/domain/knowledge_contract.go), [internal/storage/neo4j/schema.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/storage/neo4j/schema.go)). Neo4j is the primary knowledge substrate; Postgres stores control-plane state such as teams, API keys, embedding configuration, advisory locks, audit/import ledgers, and metrics, while Redis is optional runtime coordination.

**The host extracts; Dense-Mem constrains and gates.** The high-level `remember` tool stores one conversation evidence fragment and optional host-supplied typed claims, validates predicate/confidence fields, verifies claims against supporting fragments, and auto-promotes validated claims by default ([internal/service/memoryservice/memory.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/memoryservice/memory.go), [internal/tools/registry/memory_tools.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/tools/registry/memory_tools.go)). Historical imports are deliberately more conservative: `import_memories` stores summarized document evidence and defaults auto-promotion to false.

**Promotion is explicit policy, not similarity overwrite.** `DefaultPromotionGates` is deny-by-default outside its predicate map and combines policy, extraction confidence, resolution confidence, assertion requirements, entailment requirements, support count, and source quality ([internal/service/factservice/gates.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/factservice/gates.go)). Promotion runs under profile-scoped advisory locks, checks idempotency, handles multi-valued and single-current policies differently, and defers comparable conflicts to user clarification instead of silently replacing active facts ([internal/service/factservice/promote.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/factservice/promote.go)).

**Verification is evidence entailment, not external truth.** Claim verification loads the claim and supporting fragments under profile scope, builds a verifier request from the claim triple plus evidence text, calls an OpenAI-compatible verifier, and maps `entailed`, `contradicted`, or `insufficient` into claim status/verdict fields ([internal/service/claimservice/verify.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/claimservice/verify.go), [internal/verifier/openai_verifier.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/verifier/openai_verifier.go)). The verifier can only judge support from stored evidence; extraction quality before the claim reaches Dense-Mem is outside this server's proof boundary.

**Context efficiency is mostly pull-time tiering.** Writes are constrained to granular entries by the tool schemas and descriptions, with content capped under 1000 characters for memory entries ([internal/tools/registry/toolset.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/tools/registry/toolset.go)). Recall clamps limits to at most 50, uses active facts as tier 1, validated claims as tier 1.5, fragments as tier 2, and merges fragment semantic/BM25 branches with Reciprocal Rank Fusion; `include_evidence` controls whether fact/claim evidence is expanded ([internal/service/recallservice/recall.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/recallservice/recall.go)).

**Operational boundaries are part of the memory design.** MCP and HTTP tool calls are bound to a server-side profile derived from credentials, and MCP strips `team_id` / `profile_id` arguments before invocation ([internal/mcp/server.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/mcp/server.go)). Neo4j scoped readers/writers require a `$profileId` placeholder and inject it centrally; schema bootstrap adds profile indexes and relationship constraints where supported ([internal/storage/neo4j/profile_scope.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/storage/neo4j/profile_scope.go), [internal/storage/neo4j/schema.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/storage/neo4j/schema.go)).

## Artifact analysis

- **Storage substrate:** `graph` — The primary retained knowledge persists in Neo4j as `SourceFragment`, `Claim`, `Fact`, and `Community` nodes plus evidence/promotion/supersession/contradiction relationships; Postgres and Redis support control, audit, locking, import ledgers, embedding configuration, and deployment coordination rather than serving as the main knowledge substrate.
- **Representational form:** `prose` `symbolic` `parametric` — Fragment content, summaries, and evidence are prose; triples, policies, schemas, statuses, scopes, audit rows, import decisions, and graph relationships are symbolic; embeddings and verifier/embedding model outputs are parametric behavior-shaping state.
- **Lineage:** `authored` `imported` `trace-extracted` — Tool schemas, gates, query guards, and service code are authored; documents, historical summaries, manual fragments, and skill-pack JSON are imported; live conversation evidence and host-extracted claims are trace-derived into fragments, claims, and facts.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Fragments, claims, facts, and communities advise future work when recalled; tool schemas, scopes, promotion gates, verifier schemas, profile guards, graph query validators, import policies, and embedding/index configuration instruct, constrain, route, validate, rank, and learn durable memory from supplied traces.

**Source fragments.** Storage substrate: Neo4j `SourceFragment` nodes. Representational form: prose content plus symbolic metadata, labels, authority/source fields, dedupe hashes, status, classification JSON, embedding model/dimensions, and stored vector embeddings. Lineage: created from conversation, document, observation, manual, historical-summary, or skill-pack-import inputs; high-level `remember` marks current chat evidence as `source_type="conversation"` and `authority="primary"` ([internal/service/memoryservice/memory.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/memoryservice/memory.go)). Behavioral authority: knowledge when returned as evidence or tier-2 recall; ranking and validation authority through embeddings, active/retracted status, dedupe hashes, source quality, and support counts.

**Claims.** Storage substrate: Neo4j `Claim` nodes linked to supporting fragments by `SUPPORTED_BY`. Representational form: symbolic claim triples with prose object strings, modality/polarity, confidence scores, extraction model/version, pipeline run id, verifier verdict, status, and evidence links. Lineage: host-extracted from current conversation/import traces or posted directly against supporting fragments. Behavioral authority: knowledge while candidate/validated recall context; system-definition influence during promotion, because predicate, confidence, support, status, and verifier verdict decide whether a fact can be created.

**Facts and truth-maintenance edges.** Storage substrate: Neo4j `Fact` nodes linked from claims with `PROMOTES_TO` and from older facts through supersession/contradiction paths. Representational form: symbolic fact triples with truth score, active/superseded/revalidation status, source quality, temporal fields, and optional evidence. Lineage: promoted from validated claims, then superseded or rejected through explicit policy paths and clarification decisions. Behavioral authority: strongest knowledge artifact in recall tier 1, and system-definition artifact for later conflict comparison, revalidation, temporal filtering, and truth-score ordering.

**Verifier, embedding, and recall indexes.** Storage substrate: external OpenAI-compatible providers, Neo4j full-text/vector indexes, and Postgres embedding configuration. Representational form: parametric embeddings/verifier outputs plus symbolic model identifiers, dimensions, JSON schemas, index definitions, and failure policies. Lineage: embeddings derive from fragment text and recall queries; query embeddings are request-scoped and not persisted, while fragment embeddings persist. Behavioral authority: ranking and validation. Fragment creation fails if embedding fails, startup checks reject model/dimension mismatches, and verifier failures leave claim state unchanged ([internal/service/fragmentservice/create.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/fragmentservice/create.go), [internal/service/embedding_consistency.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/embedding_consistency.go)).

**Tool registry and transport surfaces.** Storage substrate: authored Go registry objects exposed through HTTP, OpenAPI, and MCP. Representational form: symbolic JSON schemas, required scopes, invokers, and prose tool descriptions. Lineage: generated at server startup from `registry.BuildDefault`; consumed by the catalog endpoint, OpenAPI generator, tool execution handler, and MCP server ([internal/tools/registry/registry.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/tools/registry/registry.go), [internal/tools/registry/toolset.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/tools/registry/toolset.go)). Behavioral authority: system-definition artifact authority because these surfaces determine what agents can call, which scopes are needed, what payloads are valid, and which profile receives the operation.

**Communities and skill packs.** Storage substrate: Neo4j `community_id` properties, persisted `Community` nodes, canonical skill-pack JSON, graph mutations, and Postgres import/change ledgers. Representational form: symbolic community metadata and skill-pack items plus deterministic prose community summaries. Lineage: communities derive from Neo4j GDS Leiden over same-profile fragments/claims/facts and deterministic summary rendering; skill packs derive from facts, validated claims, manual items, optional support bundles, and reviewed/trusted imports ([internal/service/communityservice/leiden.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/communityservice/leiden.go), [internal/service/communityservice/summary.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/communityservice/summary.go), [internal/service/skillpackservice/service.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/skillpackservice/service.go)). Behavioral authority: knowledge and routing for communities; portability and mutation authority for skill-pack imports, because trusted/reviewed imports can create claims/facts or supersede local facts under recorded decisions.

Promotion path: Dense-Mem's main trajectory is trace or document evidence -> source fragment -> host-extracted typed claim -> verifier status -> predicate gate -> active fact -> later recall, reflection, confirmation, conflict handling, or revalidation. The server does not autonomously mine raw chat logs into claims; the host must supply candidate claims.

## Comparison with Our System

| Dimension | Dense-Mem | Commonplace |
|---|---|---|
| Primary purpose | Operational memory server for MCP/REST clients | Git-native methodology KB and framework for agent-operated knowledge bases |
| Main substrate | Neo4j knowledge graph plus Postgres control/audit state | Typed Markdown collections, source snapshots, generated indexes, validation, and review artifacts |
| Write model | Host extracts evidence/claims; server verifies, gates, promotes, audits, and clarifies conflicts | Agent writes source-grounded artifacts under collection/type contracts, semantic review, validation, and git history |
| Retrieval | Explicit recall/fact/claim/fragment/community tools with tiering and vector/BM25 fragment RRF | `rg`, indexes, authored links, collection contracts, reports, and skills |
| Governance | Predicate gates, verifier calls, profile isolation, scopes, locks, audit logs, import ledgers | Schemas, validation, semantic review, citations, link vocabulary, archive/replacement lifecycle |
| Activation | Client explicitly calls MCP/REST tools | Mostly deliberate pull through search, links, skills, and task-local instructions |

Dense-Mem is stronger than Commonplace on service boundaries. It treats profile isolation, bearer-key scopes, row/graph scoping, rate limits, embedding consistency, provider failures, audit state, and import rollback as product surfaces. Commonplace is stronger on human-readable methodology and source-review discipline: durable claims live as cited Markdown arguments rather than verifier-gated graph triples.

The deepest difference is where truth becomes machine state. Commonplace preserves source citations and asks agents/reviewers to reason over prose. Dense-Mem turns host-extracted assertions into facts only after evidence entailment and predicate policy. That gives Dense-Mem clearer operational state, but it also means memory quality depends on host extraction and verifier calibration.

### Borrowable Ideas

**Tiered authority in recall results.** Ready as a design pattern. Dense-Mem's fact/claim/fragment tiers make authority visible at read time; Commonplace search bundles could distinguish reviewed notes, drafts, sources, generated indexes, reports, and workshop artifacts with comparable labels.

**Promotion gates as named policy objects.** Ready where Commonplace wants stronger automated transitions. Dense-Mem centralizes predicate-specific promotion policy; a Commonplace analogue could govern when workshop outputs become library notes, instructions, or validators.

**Clarification instead of silent overwrite.** Ready now. Dense-Mem turns comparable single-current conflicts into structured clarification work. Commonplace write tools could return "existing artifact or claim conflicts with this draft" tasks instead of letting agents overwrite or duplicate silently.

**Embedding configuration consistency.** Worth borrowing if Commonplace adds persistent vector indexes. Dense-Mem records embedding model/dimensions and rejects mismatched deployments, which is the right contract for any derived search layer that outlives one command.

**Profile-scoped query guard.** Needs a database-backed Commonplace surface first. The `$profileId` placeholder requirement and central injection are useful examples for exposing advanced graph/database queries without giving agents unconstrained cross-tenant authority.

**Do not borrow verifier-backed promotion as a substitute for review.** Dense-Mem's entailment verifier suits operational personal memory. Commonplace methodology claims still need source-grounded argument quality, not only evidence support for one extracted triple.

## Write side

**Write agency:** `manual` `automatic` — Callers manually save fragments, post claims, verify/promote claims, confirm conflicts, import skill packs, and run community detection through tools/API; the server automatically embeds fragments, deduplicates, verifies claims when wired through high-level memory, applies promotion gates, creates facts, records audit/import changes, builds community summaries, and handles conflict/supersession paths.

**Curation operations:** `dedup` `synthesize` `invalidate` `promote` — Fragment and claim create paths use idempotency/content-hash or identity checks; community summaries synthesize grouped fact/claim triples into persisted summaries; retraction, supersession, disputed claims, confirmation rejection, rollback, and revalidation status invalidate or weaken retained state; validated claims promote into active facts and skill-pack imports can create or supersede graph entries under recorded decisions.

### Trace-derived learning

**Trace source:** `session-logs` — Dense-Mem consumes current conversation evidence and summarized historical conversations supplied by the host, not full transcripts, tool/action traces, event streams, or rollouts.

**Learning scope:** `cross-task` — The store is profile-scoped and designed to carry facts across later conversations, recall calls, reflection, and skill-pack transfer.

**Learning timing:** `online` `staged` — Live `remember` calls process current conversation evidence online; historical imports and skill-pack imports are staged/reviewed paths, with auto-promotion off by default for historical imports.

**Distilled form:** `prose` `symbolic` `parametric` — Raw evidence becomes prose fragments, symbolic claims/facts/skill-pack items/community summaries, and persisted fragment embeddings used for later ranking.

**Extraction.** Dense-Mem qualifies as trace-derived because the normal high-level memory path consumes current conversation evidence plus host-extracted typed claims, and the historical import path consumes summarized prior conversations. The raw trace boundary sits outside the server: Dense-Mem receives granular evidence strings and optional structured claims rather than owning a full transcript parser.

**Scope and timing.** The write path is online for ordinary chat-session memory and staged for historical or portable memory. Successful extraction can become an active fact immediately only when verification and promotion gates pass; conflicts become clarification tasks and require a later `confirm_memory` decision.

**Survey fit.** Dense-Mem fits the trace-to-symbolic-memory branch of the trace-derived learning landscape. Its useful split is raw trace retention versus stronger distilled authority: fragments remain evidence, claims become validated candidates, and only gated facts become the durable top-tier memory returned ahead of lower-authority evidence.

## Read-back

**Read-back:** `pull` — Retained memory reaches an agent only when a host, user, or integration explicitly calls tools or endpoints such as `recall_memory`, `get_memory`, `list_recent_memories`, fact/claim reads, `reflect_memories`, graph query, community summary, or skill-pack candidate tools; I did not find an implemented hook, scheduler, situation matcher, or host loop that pushes retained memory into a receiving agent context without such a call.

The read path is still substantial: active facts and validated claims are matched separately, fragment recall runs semantic and keyword branches in parallel, RRF merges fragment hits, tier sorting puts facts ahead of claims and fragments, and profile/temporal/evidence flags bound what is returned. That is a strong pull interface, not automatic activation. Tool descriptions may instruct clients to use memory before answering, but the repository-visible mechanism leaves invocation to the host.

## Curiosity Pass

**The README's boundary claim is implemented unusually consistently.** Dense-Mem really does make the host responsible for extraction: the high-level `remember` schema expects typed claims, and server-side code constrains, verifies, and promotes them rather than trying to infer all claims from raw chat itself.

**The verifier is a guardrail with a model dependency.** It prevents arbitrary host-extracted triples from becoming validated claims without support evidence, but a provider/model behavior now sits inside the promotion path. The code stores verifier model and raw response; it does not prove calibration quality.

**Community summaries are deterministic, not LLM summaries.** The inspected community service writes Leiden community ids, loads fact/claim triples, and renders summaries from top entities/predicates and representative triples. That makes the current summary artifact more auditable than "AI community summary" wording might suggest.

**Skill packs are closer to memory package management than backup.** Export/import carries canonical JSON, artifact hashes, optional support bundles, reviewed/trusted modes, conflict decisions, durable import ledgers, and rollback. That makes portability a governed mutation path, not just a serialization format.

**The weakest lineage boundary is upstream.** Dense-Mem preserves support links after a claim arrives, but it cannot prove the host extracted the right candidate from the original conversation unless the host supplied enough precise evidence as the fragment.

## What to Watch

- Whether the project ships first-party extraction prompts or clients. That boundary controls the quality of every high-level claim.
- Whether verifier quality gets adversarial or calibration tests. Promotion correctness depends on more than schema-constrained JSON.
- Whether a host integration starts automatically invoking recall before model calls. That would change the read-back verdict from pull-only to push or both.
- Whether community summaries move from deterministic rendering to LLM-generated prose. That would add another derived artifact needing lineage and quality controls.
- Whether skill-pack imports become a common cross-profile or cross-team memory transfer path. If so, conflict policy and rollback evidence may matter as much as ordinary recall quality.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - positions Dense-Mem as trace-to-symbolic-memory rather than trace-to-weight learning.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Dense-Mem separates graph memory, provider outputs, control-plane state, tool contracts, and import artifacts by substrate, form, lineage, and authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Dense-Mem stores governed memory, but retained content enters context through explicit recall/tool calls.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: fragments, claims, facts, and community summaries mostly advise or evidence future work when recalled.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: promotion gates, verifier schemas, tool schemas, profile-scoped query guards, and import policies directly constrain behavior.
