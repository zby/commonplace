---
description: "MentisDB review: Rust append-only thought ledger with hash-chain integrity, storage adapters, ranked retrieval, MCP/REST/dashboard surfaces, and signed skill registry"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-05-16"
---

# MentisDB

MentisDB, by CloudLLM-ai, is a Rust memory service for agents. It stores typed "thoughts" in append-only hash-chained logs, exposes them through MCP, REST, TUI, and dashboard surfaces, and ships a separate versioned skill registry for agent instruction bundles. Compared with commonplace, MentisDB is a runtime memory daemon: its canonical memory is service-managed binary chain state plus registries and sidecars, while commonplace keeps reviewed methodology artifacts as git-tracked markdown.

**Repository:** https://github.com/cloudllm-ai/mentisdb

**Reviewed commit:** [e2ab66bd8dc205b88517f775f8c1775a7aa1105f](https://github.com/cloudllm-ai/mentisdb/commit/e2ab66bd8dc205b88517f775f8c1775a7aa1105f)

**Last checked:** 2026-05-16

## Core Ideas

**The canonical memory is an append-only thought chain.** The core `ThoughtInput` to `Thought` path separates caller-authored memory from committed records with assigned UUID, append index, timestamp, agent id, previous hash, and final hash ([thought input and record types](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/lib.rs)). `append_thought()` validates refs, expands positional refs into typed `References` relations, timestamps relations, optionally adds `Supersedes` for near-duplicate content, computes `prev_hash` from the current head, computes the canonical hash, persists the thought, and updates in-memory indexes and sidecars ([append path](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/lib.rs)). The stored thought is a knowledge artifact when a later agent reads it as evidence, context, or advice. The chain order, hash fields, relation types, scope tags, and importance/confidence fields become system-definition artifacts when retrieval, traversal, deduplication, or branch logic uses them to route future context.

**Hash-chain integrity is explicit but local.** `MentisDb::verify_integrity()` checks append-order index, previous-hash continuity, and recomputed thought hashes; opening a chain rejects non-legacy integrity failures, while legacy JSON-hash chains can be rehashed into the current bincode hash algorithm ([open and verify logic](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/lib.rs)). This gives the ledger tamper-evidence inside the storage file, not a distributed consensus or signed append log by default. Detached thought signatures are represented in `ThoughtInput` and `Thought`, and signable payload rendering exists, but the server tool metadata describes thought signatures as optional; skill uploads are where signature enforcement is implemented when an agent has registered public keys ([signable thought payload](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/lib.rs), [skill upload verification](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/server.rs)).

**Storage is adapter-shaped, but binary is the live format.** `StorageAdapter` abstracts durable load, append, flush, write-mode, and storage-location behavior. `StorageAdapterKind` only permits `Binary` for new chains; JSONL remains as a legacy read-only migration source ([storage adapter contract](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/lib.rs)). The binary adapter stores length-prefixed bincode records and supports durable group-commit acknowledgements or buffered batched writes controlled by `auto_flush` ([binary adapter docs](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/lib.rs)). Agent and entity registries, chain registrations, vector sidecars, skill registries, webhook registrations, interaction logs, and dashboard settings sit beside the thought chains as auxiliary service state.

**Agent, key, and entity registries are first-class sidecars.** Each chain maintains an `AgentRegistry` keyed by stable `agent_id`, including display name, owner, description, aliases, status, public keys, first/last seen positions, and thought count ([agent registry types](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/lib.rs)). Server and dashboard surfaces expose upsert, alias, description, public-key add/revoke, and disable operations ([agent registry service methods](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/lib.rs), [dashboard routes](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/dashboard.rs)). Entity types are observed from thought metadata and can also be explicitly upserted. These registries are system-definition artifacts: they determine attribution, ownership, key trust, search filters, skill-upload authorization, and dashboard lifecycle state.

**Retrieval is layered over the ledger rather than replacing it.** The basic `ThoughtQuery` filters by type, role, agent, tags, concepts, text, time, importance, confidence, scope, and entity type. The lexical index is derived state built from committed thoughts plus agent metadata, with BM25-style scoring over content, tags, concepts, agent id, and agent registry text ([lexical index](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/search/lexical.rs)). Ranked search blends lexical, optional vector-sidecar similarity, graph expansion, relation weights, seed support, importance, confidence, recency, and session cohesion; federated search merges hits across chains and can apply reciprocal rank fusion over lexical, vector, and graph rankings ([ranked and federated search](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/lib.rs), [server ranked/federated handlers](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/server.rs)). Context bundles group supporting thoughts beneath lexical seeds. Retrieval results are knowledge artifacts; the indexes, score weights, RRF merge, graph traversal, scope tags, and filters have ranking and routing authority.

**Vector sidecars are rebuildable derived artifacts.** The vector module defines provider metadata, embedding inputs, embedding vectors, a deterministic local text embedding provider, and cosine search ([vector module](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/search/vector.rs)). Persisted vector sidecars record chain key, embedding metadata, thought count, head hash, generation time, entries keyed by thought UUID/index/hash, and an integrity digest; freshness checks detect chain, model, version, dimension, thought-count, and head-hash mismatch ([vector sidecar](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/search/sidecar.rs)). The sidecar is not source memory. It is a distributed-parametric derived view over the thought ledger, with lineage back to thought IDs and hashes and rebuild rules based on head hash and embedding metadata.

**Runtime surfaces are unusually complete for a small memory service.** The server exposes streamable HTTP MCP, legacy `/tools/list` and `/tools/execute`, REST endpoints for append/search/recent-context/markdown import-export/chains/agents/entity types/vectors/skills/webhooks/LLM extraction, and optional HTTPS with generated certificates ([server module overview](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/server.rs)). The dashboard embeds static HTML in the binary and exposes PIN-gated chain, thought, search, agent, key, vector, skill, version, and settings routes ([dashboard](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/dashboard.rs)). The CLI and setup integrations target several agent harnesses, while the embedded MCP bootstrap instructions tell agents to load the core skill, prefer relevant chains, use ranked search/context bundles, reuse existing specialist identities, and checkpoint before compaction ([server bootstrap instructions](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/server.rs), [embedded skill](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/MENTISDB_SKILL.md)).

**The skill registry is the strongest behavior-shaping surface.** Skills are Markdown or JSON instruction bundles parsed into structured documents with frontmatter, sections, tags, triggers, warnings, and schema version ([skill parser and schema](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/skills.rs)). Uploading a skill creates an immutable version; subsequent uploads to the same `skill_id` are stored as diffs, versions can be reconstructed, summaries are indexed, and lifecycle status can be active, deprecated, or revoked ([skill registry upload/search/read](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/skills.rs)). Through the server, uploading agents must already be registered in the chain, and if they have active public keys then `signing_key_id` and a valid Ed25519 signature over the raw skill content are mandatory ([server skill upload](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/server.rs)). Unlike ordinary thoughts, skills are explicit system-definition artifacts: when loaded by an agent, they instruct future behavior.

**LLM extraction exists, but it is review-before-append.** The opt-in extraction module calls an OpenAI-compatible API to transform free-form text into `ThoughtInput` records, but its security note says LLM output is untrusted and must be reviewed, validated, and optionally signed before appending ([LLM extraction module](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/llm.rs)). The MCP tool description repeats that extracted records are not automatically appended ([MCP tool metadata](https://github.com/cloudllm-ai/mentisdb/blob/e2ab66bd8dc205b88517f775f8c1775a7aa1105f/src/server.rs)). This is memory extraction support, not an implemented trace-derived learning loop by itself.

## Comparison with Our System

| Dimension | MentisDB | Commonplace |
|---|---|---|
| Primary substrate | Binary append-only thought chains plus registry and sidecar files | Git-tracked markdown notes, sources, instructions, reviews, schemas, generated indexes |
| Canonical knowledge | Committed `Thought` records with types, roles, relations, tags, concepts, importance, confidence, agent ids, and hashes | Typed markdown artifacts governed by collection/type contracts |
| Derived views | In-memory query indexes, lexical index, vector sidecars, ranked-search scores, context bundles, memory markdown exports | Directory indexes, curated indexes, connect reports, review reports, validation outputs |
| Behavior-shaping artifacts | MCP bootstrap instructions, embedded operating skill, versioned skills, tool schemas, retrieval/ranking logic, registries, key status | `AGENTS.md`, skills, type specs, validation/review commands, authored links |
| Trust model | Hash-chain integrity, optional thought signatures, signed skill upload when agent keys exist, key revocation, skill deprecation/revocation | Git history, source citations, frontmatter status, validation, review gates, explicit archived replacements |
| Activation | Agent calls MCP/REST tools; bootstrap skill instructs agents to read recent context and checkpoint | Agent searches files, follows indexes/links, loads local skills and instructions |

MentisDB is better than commonplace at serving a shared runtime memory to many harnesses. It gives agents one daemon with stable tools for append, search, recent context, branch/federated search, skill upload/read, and dashboard inspection. It also treats agent identity and public keys as operational data, which matters for multi-agent fleets where attribution and signature checks affect trust.

Commonplace is stronger at reviewable knowledge curation. A MentisDB thought can say "this is a lesson" or "this corrects an earlier thought," but it is still a ledger entry, not a typed note with collection conventions, outbound-link semantics, discriminating description, validation rules, review history, and a curated index position. MentisDB can export memory markdown and can read skills as text, but its canonical thought substrate is service-managed state; commonplace keeps the source of truth in files that ordinary code review can inspect.

The central artifact split is important. Raw thoughts/logs in MentisDB are knowledge artifacts until a retrieval or bootstrap path consumes them. Lexical indexes, vector sidecars, graph expansions, RRF ranking, context bundles, agent registries, key revocations, and skill lifecycle status are derived or auxiliary system-definition artifacts because they route, rank, authorize, or warn. Skills are the clearest system-definition artifacts: they are versioned instructions that agents are explicitly told to load before work.

MentisDB also has a different stance on provenance. It preserves append order, hashes, writer identity, optional signatures, source episode, relation timestamps, and sidecar freshness metadata. That is strong ledger provenance. It does not, by itself, produce a reviewable derivation chain from evidence to a claim in the way commonplace reviews and notes do. The ledger can record such a derivation if agents write it well, but the system mostly enforces storage integrity and retrieval structure rather than epistemic review quality.

Trace-derived status is not supported for this review. The code supports manual memories, retrospective writes, summaries, LLM-extracted candidate `ThoughtInput`s, interaction logs, and exported/imported memory markdown. Those are useful sources and surfaces, but at this commit there is no implemented loop that consumes agent traces or outcomes and automatically promotes them into durable behavior-shaping artifacts such as reviewed rules, skills, tests, validators, rankers trained from outcomes, or prompt patches. Agents can manually store lessons from traces, and they can upload skills after learning, but that is an operator-mediated write path rather than trace-derived learning.

**Read-back:** both — agents query thought chains through MCP or REST tools, while bootstrap instructions and core skills can load behavior rules before retrieval.

## Borrowable Ideas

**Treat append-only memories and behavior instructions as separate products.** Ready to borrow as vocabulary. MentisDB's ordinary thought chain and skill registry have different authority, lifecycle, and trust requirements. Commonplace already separates notes from instructions, but MentisDB is a useful external example of why runtime memory and executable guidance should not be collapsed.

**Use head-hash freshness for derived retrieval layers.** Ready if commonplace grows vector or compiled search sidecars. MentisDB's vector sidecar stores thought count, head hash, embedding metadata, and integrity digest. A commonplace sidecar should similarly prove which source tree and model/version produced it, and it should be disposable when freshness fails.

**Make agent identity reusable and governed.** Worth borrowing for multi-agent workflows. The embedded skill's strongest practical advice is to avoid new agent IDs for every run and reuse registered identities. Commonplace could apply the same idea to review workers or recurring agent roles without adopting MentisDB's full registry.

**Sign system-definition artifacts before trusting them.** MentisDB enforces skill signatures when an agent has registered public keys. Commonplace does not need cryptographic signing for local repo use, but the distinction is right: skills, instructions, and other behavior-changing artifacts need stronger trust gates than ordinary remembered observations.

**Expose memory as MCP only after bootstrap semantics are precise.** MentisDB's MCP initialize instructions, `mentisdb://skill/core` resource, bootstrap tool, and fallback skill endpoint define a startup protocol, not just a tool list. A commonplace MCP surface should similarly tell agents what to read first, how to choose scope, and when to checkpoint.

**Do not borrow binary ledgers as the canonical methodology KB.** The ledger is a good runtime substrate for append-heavy agent activity, but it would be a poor replacement for reviewed markdown notes. For commonplace, a MentisDB-like service would fit as a working-memory or runtime-history sidecar, with promoted insights still landing in typed files.

## Curiosity Pass

**MentisDB is more operational than epistemic.** The code spends serious effort on storage durability, migration, hash verification, concurrent chain access, search surfaces, vector sidecars, dashboard routes, keys, webhooks, and MCP/REST compatibility. It spends less effort on whether a remembered claim is true, reviewed, superseded by a better note, or worth promoting into an instruction.

**The "hash-chained brain" phrase can overstate the trust model.** The hash chain detects local tampering and bad migration. It does not make a thought correct, reviewed, signed, or globally non-repudiable. Skill signatures are stronger because uploads are rejected when required signatures fail; thought signatures are represented and surfaced, but optional in the exposed append tools at this commit.

**Retrieval authority is broad.** Importance, confidence, recency, graph proximity, relation kind, seed support, session cohesion, vector similarity, lexical fields, and RRF can all affect what an agent sees. That is useful, but these numeric and symbolic knobs are system-definition artifacts and should be treated as such during review.

**LLM extraction is deliberately conservative in authority.** The extraction module returns candidate `ThoughtInput`s and warns that callers must review them. This is the right trust posture, but it also means extraction is not yet a closed learning loop.

**Skill lifecycle is stronger than thought lifecycle.** Skills have immutable versions, diffs, content hashes, deprecation, revocation, warnings, and optional upload signatures. Thoughts have correction/supersession/invalidating relations and hash integrity, but less explicit review state. The behavior-shaping layer is more governed than the general memory layer.

**The dashboard turns sidecars into operator surfaces.** Chain, vector, agent, key, skill, and settings routes make derived state inspectable and mutable through a browser. That is a practical adoption move, but it also widens the trusted control plane beyond MCP and CLI.

## What to Watch

- Whether thought append starts enforcing signatures when an agent has registered public keys, matching the stronger skill-upload path.
- Whether trace/outcome logs become a real learning loop that promotes repeated failures or successful repairs into reviewed skills, instructions, validators, or ranking changes.
- Whether thoughts gain explicit review states, approval provenance, source offsets, extraction prompt/model metadata, or confidence-oracle metadata.
- Whether vector sidecars expand beyond deterministic local embeddings and how model downloads, API keys, and sidecar invalidation are handled.
- Whether branch and merge semantics mature for multi-agent fleets, especially around provenance and identity remapping.
- Whether the skill registry starts distinguishing trusted, reviewed, signed, deprecated, and revoked skills in the agent bootstrap protocol more forcefully.

---

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - classifies: MentisDB needs separate treatment for thought records, storage files, registries, vector sidecars, retrieval scores, MCP tool schemas, and skills.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: committed thoughts advise later agents when retrieved as context or evidence.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: skills, bootstrap instructions, ranking logic, key status, and tool schemas instruct, route, authorize, or rank future behavior.
- [Lineage](../../notes/definitions/lineage.md) - clarifies: MentisDB has strong ledger and sidecar freshness lineage, but not full reviewed claim derivation.
- [Retained artifact](../../notes/definitions/retained-artifact.md) - frames: MentisDB's retained state matters when later MCP/REST/dashboard consumers use it to change behavior.
