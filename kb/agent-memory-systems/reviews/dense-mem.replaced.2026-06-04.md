---
description: "Dense-Mem review: self-hosted MCP memory server with Neo4j fragment/claim/fact graph, verifier gates, tiered recall, and trace-derived claims"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-03"
---

# dense-mem

Replaced by [dense-mem.md](./dense-mem.md) on 2026-06-04.

Dense-Mem, by markhuangai, is a self-hosted Go memory server for MCP and REST clients. It stores evidence fragments, host-extracted typed claims, promoted facts, community summaries, and audit/control metadata behind profile-scoped API keys; the host LLM keeps responsibility for conversation judgment and extraction, while Dense-Mem owns persistence, embeddings, verification, promotion gates, conflict handling, and recall.

**Repository:** https://github.com/markhuangai/dense-mem

**Reviewed commit:** [96158d8b672883d1239f4acc7ab0b7296638d0d7](https://github.com/markhuangai/dense-mem/commit/96158d8b672883d1239f4acc7ab0b7296638d0d7)

**Last checked:** 2026-06-03

## Core Ideas

**Memory is a governed graph, not a loose vector cache.** The central contract is `SourceFragment -> Claim -> Fact`: fragments preserve raw evidence and embeddings, claims carry typed subject/predicate/object assertions plus verification state, and facts are promoted active memory with truth score and supersession metadata ([knowledge-pipeline-contracts.md](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/docs/knowledge-pipeline-contracts.md), [knowledge_contract.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/domain/knowledge_contract.go)). The code persists fragments, claims, facts, and relationships in Neo4j, while Postgres carries teams, API-key profiles, embedding config, audit logs, advisory locks, usage metrics, and skill-pack import ledgers ([schema.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/storage/neo4j/schema.go), [2026041501_core_schema.sql](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/migrations/postgres/2026041501_core_schema.sql)).

**The host LLM extracts; Dense-Mem gates.** The high-level `remember` path saves a granular conversation evidence entry, accepts host-supplied typed claims, verifies them against supporting fragments, and promotes only validated claims that pass predicate-specific gates ([memory.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/memoryservice/memory.go), [memory_tools.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/tools/registry/memory_tools.go)). The host can still use lower-level tools such as `save_memory`, `post_claim`, `verify_claim`, and `promote_claim`, but the registry keeps tool schemas, scope requirements, and invokers in one catalog for MCP, HTTP, and OpenAPI discovery ([toolset.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/tools/registry/toolset.go), [registry.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/tools/registry/registry.go)).

**Promotion has explicit authority policy.** Dense-Mem's high-level personal-memory predicates are allow-listed, and fact promotion is deny-by-default outside `DefaultPromotionGates` ([memory.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/memoryservice/memory.go), [gates.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/factservice/gates.go)). Gates combine extraction confidence, resolution confidence, assertion modality, verifier entailment, and support evidence; `single_current` predicates compare candidate strength against active facts and defer comparable conflicts to user clarification rather than overwriting silently ([promote.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/factservice/promote.go)).

**Verification is provider-backed but structurally constrained.** Claim verification loads supporting fragments, builds a verifier request from the claim triple plus evidence text, calls an OpenAI-compatible verifier, and maps `entailed`, `contradicted`, or `insufficient` into claim state ([verify.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/claimservice/verify.go), [openai_verifier.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/verifier/openai_verifier.go)). The verifier is not an external truth oracle; it evaluates whether stored evidence supports the claim. Its quality is runtime/provider-dependent, but the state transition and audit fields are explicit in code.

**Context efficiency is mostly pull-time shaping.** Writes are intentionally granular: memory entries are capped just under 1000 characters in tool schemas, and docs tell callers to split large scenarios into claim-worthy evidence pieces ([toolset.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/tools/registry/toolset.go), [standalone-mcp-memory-architecture.md](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/docs/standalone-mcp-memory-architecture.md)). Reads are tiered and bounded: active facts and validated claims are matched separately, fragments use semantic + BM25 Reciprocal Rank Fusion, limits clamp at 50, and `include_evidence` controls whether fact/claim evidence payloads are expanded ([recall.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/recallservice/recall.go), [knowledge-pipeline-client-contracts.md](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/docs/knowledge-pipeline-client-contracts.md)).

**Isolation and operations are first-class.** MCP calls are bound to a server-side profile derived from the bearer key; `team_id` and `profile_id` arguments are stripped before tool invocation ([server.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/mcp/server.go)). Neo4j scoped readers/writers require a `$profileId` placeholder and inject it centrally, Postgres uses row-level security and advisory locks, Redis is optional for single-node coordination but required for multi-instance rate limits and SSE concurrency ([profile_scope.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/storage/neo4j/profile_scope.go), [standalone-mcp-memory-architecture.md](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/docs/standalone-mcp-memory-architecture.md)).

## Artifact analysis

- **Storage substrate:** `graph` - The central retained memory persists in Neo4j as `SourceFragment`, `Claim`, `Fact`, and `Community` nodes plus scoped relationships; Postgres and Redis support control, audit, locks, metrics, import ledgers, and runtime coordination rather than serving as the primary knowledge substrate.
- **Representational form:** `prose` `symbolic` `parametric` - Dense-Mem combines prose evidence, symbolic triples/statuses/policies/schemas, vector embeddings on fragments, deterministic community summaries, and JSON skill-pack artifacts.
- **Lineage:** `authored` `imported` `trace-extracted` - Authored gates, schemas, registry code, and policies shape the system; conversation, document, observation, manual, historical-summary, and skill-pack inputs are imported; live and historical conversation evidence is trace-extracted into fragments, claims, and facts.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` - Fragments, claims, facts, and communities advise recall; tool schemas, scopes, profile guards, promotion gates, verifier schemas, embedding/index configuration, import decisions, and fact state transitions instruct, constrain, route, validate, rank, and learn durable memory from supplied traces.

**Source fragments.** Storage substrate: Neo4j `SourceFragment` nodes with content, source metadata, labels, classification JSON, content hash, idempotency key, embedding vector, embedding model, dimensions, and creator fields. Representational form: mixed prose plus symbolic metadata plus distributed-vector embedding. Lineage: imported from conversation, document, observation, or manual inputs; the high-level `remember` path marks live chat evidence as `source_type="conversation"` and `authority="primary"`, while `import_memories` marks historical summaries as secondary document evidence ([memory.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/memoryservice/memory.go), [create.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/fragmentservice/create.go)). Behavioral authority: knowledge artifact authority when returned as evidence or tier-2 recall; system-definition influence through embeddings, dedupe hashes, source quality, retraction state, and support-gate counts.

**Claims.** Storage substrate: Neo4j `Claim` nodes linked to supporting fragments with `SUPPORTED_BY`. Representational form: symbolic claim triples with prose object strings, confidence scores, modality, polarity, extraction model/version, pipeline run id, verifier result, classification, and evidence links. Lineage: host-extracted from conversation/import traces or posted directly from supporting fragments; verifier output derives a validated/disputed/candidate state from evidence. Behavioral authority: knowledge artifact while candidate or validated recall context; system-definition artifact at promotion time because claim status, predicate, confidence, source quality, support count, and verification fields decide whether a fact can be created.

**Facts and supersession edges.** Storage substrate: Neo4j `Fact` nodes connected from claims by `PROMOTES_TO` and from older facts by `SUPERSEDED_BY` or contradiction-related paths. Representational form: symbolic fact triples with truth score, status, valid-time/known-time fields, source quality, and classification lattice state. Lineage: promoted from validated claims, never directly overwritten; confirmation can accept a claim and supersede active conflicting facts. Behavioral authority: strongest knowledge artifact in recall tier 1, and system-definition artifact for later conflict comparison, revalidation, temporal filtering, and truth-score ordering.

**Verifier, embedding, and index configuration.** Storage substrate: external OpenAI-compatible providers, Neo4j full-text/vector indexes, and Postgres `embedding_config`. Representational form: distributed-parametric model outputs plus symbolic configuration and strict verifier JSON schema. Lineage: embeddings are generated synchronously from fragment text and recall queries; query embeddings are request-scoped and not persisted, while fragment embeddings are stored. Behavioral authority: ranking, write acceptance, and state-transition authority. Fragment writes fail if embeddings fail, startup checks reject model/dimension mismatches, and verifier failures leave claim state unchanged ([embedding_consistency.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/embedding_consistency.go), [recall.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/recallservice/recall.go)).

**Tool registry, MCP, REST, and OpenAPI surfaces.** Storage substrate: authored Go registry code and generated runtime OpenAPI/catalog responses. Representational form: symbolic JSON schemas and prose tool descriptions. Lineage: built from `registry.BuildDefault` at server startup and consumed by `/mcp`, `/api/v1/tools`, tool execution, and OpenAPI handlers ([tool_execute_handler.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/http/handler/tool_execute_handler.go), [server.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/mcp/server.go)). Behavioral authority: system-definition artifact authority; these surfaces define what agents can call, which scopes are required, and what arguments are accepted or stripped.

**Community summaries.** Storage substrate: Neo4j `community_id` properties plus persisted `Community` nodes. Representational form: symbolic community metadata plus deterministic prose summaries. Lineage: Neo4j GDS Leiden writes community ids for same-profile fragments, claims, and facts; summaries are deterministically rendered from fact or claim triples and replaced on detection runs ([leiden.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/communityservice/leiden.go), [summary.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/communityservice/summary.go)). Behavioral authority: knowledge artifact when listed or fetched; routing/navigation authority when communities shape what an agent inspects next.

**Skill-pack artifacts and import ledger.** Storage substrate: canonical JSON skill-pack files, Neo4j graph mutations, and Postgres `skill_pack_imports` / import change rows. Representational form: symbolic JSON items with optional support fragments/claims. Lineage: exported from facts, validated claims, or manual items; imported in review or trusted mode with artifact hash checks, conflict decisions, change recording, and rollback support ([types.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/skillpackservice/types.go), [artifact.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/skillpackservice/artifact.go), [skill_pack.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/domain/skill_pack.go)). Behavioral authority: portability and mutation authority, because imports can create claims/facts or supersede local facts under recorded decisions.

**Promotion path.** Dense-Mem has a strong promotion path: trace or document evidence -> source fragment -> host-extracted typed claim -> verifier status -> predicate gate -> active fact -> later recall/conflict/revalidation. What it does not have is autonomous semantic extraction from raw chat logs; the host LLM must supply candidate claims.

## Comparison with Our System

| Dimension | Dense-Mem | Commonplace |
|---|---|---|
| Primary purpose | Operational memory server for MCP/REST clients | Methodology KB and framework for agent-operated knowledge bases |
| Main substrate | Neo4j knowledge graph, Postgres control/audit state, optional Redis coordination | Git-tracked Markdown collections, type specs, generated indexes, review artifacts |
| Write model | Host extracts evidence/claims; server verifies, gates, promotes, and audits | Agent writes repo artifacts under collection/type contracts, review, validation, and git diffs |
| Retrieval | Tiered fact/claim/fragment recall with vector + full-text fragment RRF | Lexical search, descriptions, indexes, authored links, skills, and review reports |
| Governance | Predicate gates, verifier calls, profile isolation, scopes, audit logs, locks | Schemas, validation, semantic review, source citations, link vocabulary, archive lifecycle |
| Activation | Agent/host explicitly calls MCP or REST tools | Mostly deliberate pull through `rg`, indexes, skills, and task-local instructions |

Dense-Mem is much stronger than Commonplace on operational service boundaries. It treats profile isolation, bearer-key scopes, RLS, rate limits, SSE lifecycle, startup checks, provider errors, and audit metadata as product surfaces. Commonplace is stronger on human-readable methodology and source-review discipline: durable claims live in reviewable Markdown with explicit collection contracts and citation expectations.

The architectural divergence is where truth is made explicit. Commonplace preserves evidence by citing source material and asking agents or reviewers to reason over prose. Dense-Mem turns host-extracted assertions into graph facts only after a verifier and gate sequence, which is a clearer machine state but also depends on host extraction quality and verifier reliability. Dense-Mem's trust boundary is therefore narrower but sharper: it can say why a fact was promoted, but not whether the host should have extracted that candidate in the first place.

**Read-back:** `pull` - Retained memory reaches the agent only when a host explicitly calls `recall_memory`, `get_memory`, fact/claim tools, graph query, community tools, or related REST/MCP endpoints; the repository defines tool descriptions encouraging use before answers, but I did not find an implemented hook or situation matcher that pushes retained memories into the agent context without a tool call.

### Borrowable Ideas

**Tiered authority in recall results.** Ready as a design pattern. Dense-Mem's fact/claim/fragment tiers make authority visible at read time instead of returning all matches as equivalent snippets. Commonplace could make search bundles distinguish reviewed notes, drafts, sources, generated indexes, and work artifacts in a similarly explicit way.

**Promotion gates as named policy objects.** Ready for cases where Commonplace wants stronger automated transitions. Dense-Mem's `DefaultPromotionGates` shows how predicate-specific policy can be centralized and tested. Commonplace should not copy these predicates, but a similar policy map could govern artifact promotion from workshop drafts to library notes.

**Clarification instead of silent overwrite.** Ready now. Comparable conflicts produce `clarifications[]` and require `confirm_memory`; Commonplace write tools could return structured "existing claim conflicts with draft" tasks rather than letting an agent overwrite or duplicate silently.

**Embedding model consistency checks.** Worth borrowing if Commonplace adds a persistent vector layer. Dense-Mem records the active embedding model/dimensions and rejects mixed-vector deployments. That is the right operational contract for any optional search index that outlives one command.

**Profile-scoped query guard.** Needs a Commonplace analogue only if we expose graph/database query tools. Dense-Mem's central `$profileId` injection and read-only Cypher validator are useful examples of making advanced query access available without giving agents unconstrained database authority.

**Do not borrow verifier-backed promotion as a substitute for review.** Dense-Mem's verifier is appropriate for operational personal memory. Commonplace methodology claims need source-grounded review and argument quality, not only entailment against a fragment.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
**Trace source:** `session-logs` - Dense-Mem consumes current conversation evidence and summarized historical conversations rather than full transcripts, tool logs, event streams, or trajectories.

**Learning scope:** `cross-task` - The loop is profile-scoped and can carry facts across later conversations and skill-pack transfers, while the review does not identify project- or task-bounded learning semantics.

**Learning timing:** `online` `staged` - Live `remember` calls process current conversation evidence online; historical imports and skill-pack imports use staged review/trusted modes.

**Distilled form:** `prose` `symbolic` - Raw conversational evidence is distilled into prose-bearing fragments and symbolic claims/facts/skill-pack JSON, with embeddings used for stored fragment retrieval rather than as the distilled artifact itself.

**Trace source.** Dense-Mem qualifies as trace-derived because the normal `remember` path consumes current conversation evidence and host-extracted typed claims, while `import_memories` consumes summarized historical conversations. The raw trace boundary is intentionally outside the server: Dense-Mem receives one granular evidence string and optional structured claims rather than full transcripts or tool logs.

**Extraction.** Semantic extraction is delegated to the host LLM. Dense-Mem constrains the extracted claim schema, validates predicate vocabulary and confidence fields, verifies the claim against supporting evidence, and applies promotion gates. A successful path distills raw conversational evidence into durable graph facts; a conflict path distills it into a clarification task and waits for explicit user confirmation.

**Storage substrate.** Raw trace-derived evidence persists as `SourceFragment` nodes. Distilled trace-derived assertions persist as `Claim` and `Fact` nodes, with `SUPPORTED_BY`, `PROMOTES_TO`, `SUPERSEDED_BY`, and contradiction-related relationships. Audit and import/change ledgers persist in Postgres.

**Representational form.** Raw evidence is prose plus metadata and embeddings. Claims and facts are symbolic triples with prose object fields, confidence/verification/status metadata, and optional classification. Skill-pack exports are symbolic JSON with optional support evidence.

**Lineage.** Lineage is better than in a plain vector memory: claims retain supporting fragment IDs, facts retain their promoted claim ID, retracted fragments remain tombstoned for lineage, and fact revalidation can mark facts that lost sufficient active support ([retract.go](https://github.com/markhuangai/dense-mem/blob/96158d8b672883d1239f4acc7ab0b7296638d0d7/internal/service/fragmentservice/retract.go)). The weakest lineage point is before Dense-Mem receives input: it trusts the host's extraction and does not retain the full original conversation unless the host supplies it as evidence.

**Behavioral authority.** Raw fragments are knowledge artifacts for evidence and tier-2 recall. Validated claims are stronger knowledge artifacts and candidates for promotion. Active facts carry the strongest downstream authority: they outrank claims and fragments in recall, participate in conflict handling, and can block or supersede later facts. Promotion gates, verifier schemas, tool schemas, and profile-scoped query guards are system-definition artifacts.

**Scope and timing.** The loop is profile-scoped and online for live `remember` calls. Imports are staged more conservatively: historical summaries default to evidence and validated claims without auto-promotion. Skill-pack import/export adds a cross-installation transfer path with review/trusted modes and rollback history.

**Survey placement.** Dense-Mem sits in the trace-to-symbolic-memory branch of the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md). It strengthens the survey's distinction between raw trace retention and distilled behavior-shaping artifacts: the learned object is not a model update but a promoted symbolic fact with preserved evidence lineage and gates.

## Curiosity Pass

Dense-Mem is unusually explicit about what the agent does not own. The README says the host LLM owns conversation and judgment; the implementation backs that up by requiring callers to send typed claims rather than mining everything itself.

The graph is a memory authority surface, but the control plane is just as important. API-key scopes, profile resolution, Postgres locks, RLS, audit immutability, and tool schema filtering do as much work as retrieval in making the system usable for multi-tenant agents.

The verifier gate is both a strength and a dependency. It prevents arbitrary host-extracted text from becoming a fact without evidence entailment, but it introduces model/provider behavior into the promotion path. The code records verifier model and raw response, but a review of runtime calibration is outside what this source read can prove.

The community detection feature is more deterministic than "AI summary" wording might suggest. Current summaries are rendered from top entities, predicates, and representative triples after Leiden writes `community_id`; they are not LLM-generated narrative summaries.

The skill-pack path hints at a second product: governed memory portability. Export/import with support bundles, hashes, review/trusted modes, conflict decisions, import ledger, and rollback is closer to package management for memory than simple backup.

## What to Watch

- Whether host-side extraction protocols become a shipped client or reference prompt; that boundary currently determines the quality of all high-level memories.
- Whether verifier quality gets measured with adversarial or calibration tests, since promotion correctness depends on more than schema-constrained JSON.
- Whether skill-pack imports become a common cross-team transfer mechanism; if so, their conflict policy may matter as much as ordinary recall.
- Whether community summaries move from deterministic triples to LLM-generated summaries, which would add another derived artifact with verifier-like quality concerns.
- Whether Dense-Mem adds any pre-action hook or situation matcher; that would change the read-back classification from pull-only to engineered push.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - positions Dense-Mem as trace-to-symbolic-memory rather than trace-to-weight learning.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Dense-Mem separates graph memory, provider outputs, control-plane state, tool contracts, and import artifacts by substrate, form, lineage, and authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: Dense-Mem can store governed memory, but retained content still enters context through explicit recall/tool calls.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: fragments, claims, facts, and community summaries mostly advise or evidence future work when recalled.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: promotion gates, verifier schemas, tool schemas, profile-scoped query guards, and import policies directly constrain behavior.
