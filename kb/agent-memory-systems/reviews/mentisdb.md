---
description: "MentisDB review: Rust append-only thought chains with ranked/vector/graph retrieval, skill registry, MCP/REST/dashboard surfaces, and candidate LLM extraction"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-02"
---

# MentisDB

MentisDB, from CloudLLM-ai, is a Rust durable memory engine and versioned skill registry for AI agents. At the reviewed commit, it stores typed "thoughts" in append-only hash-chained files, layers lexical/ranked/vector/graph retrieval and summary-candidate selection over those chains, exposes MCP, REST, dashboard, CLI, stdio, Python, LangChain, and host-config integrations, and keeps skill packages in an immutable diff-based registry. Its LLM extraction path is implemented as candidate generation: it returns structured `ThoughtInput` records for caller review rather than automatically committing trace-derived memories.

**Repository:** https://github.com/cloudllm-ai/mentisdb

**Reviewed commit:** [5a7d9a1588617f3e40a7fd62178da515b99e4390](https://github.com/cloudllm-ai/mentisdb/commit/5a7d9a1588617f3e40a7fd62178da515b99e4390)

**Last checked:** 2026-06-02

## Core Ideas

**The canonical memory unit is a committed thought.** `ThoughtInput` is the proposed memory payload; `append_thought()` validates refs, sets relation timestamps, applies optional deduplication, assigns id/index/timestamp/agent/hash fields, persists through the storage adapter, and updates registries and indexes ([src/lib.rs](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/lib.rs)). A committed `Thought` carries type, role, content, confidence, importance, tags, concepts, refs, typed relations, entity type, `source_episode`, previous hash, and hash. The storage story is therefore append-only memory plus derived indexes, not mutable fact rows.

**Thought relations are a real graph surface.** The relation enum includes `References`, `Summarizes`, `Corrects`, `Invalidates`, `CausedBy`, `Supports`, `Contradicts`, `DerivedFrom`, `ContinuesFrom`, `BranchesFrom`, `RelatedTo`, and `Supersedes`, with optional cross-chain keys and temporal `valid_at` / `invalid_at` fields ([src/lib.rs](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/lib.rs)). Append-time dedup can add `Supersedes`; branch creation creates a genesis `StateSnapshot` with `BranchesFrom`; query-time filters can exclude superseded/corrected/invalidated thoughts for an `as_of` timestamp.

**Retrieval is additive and deliberately split from baseline filtering.** Plain `ThoughtQuery` remains deterministic filtering over committed thoughts. Ranked search adds lexical scoring, optional vector sidecars, graph expansion, session-cohesion boosts, RRF reranking, opt-in LLM reranking, thesaurus/synonym expansion, scope filters, and top-k limits ([src/lib.rs](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/lib.rs), [src/search/ranked.rs](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/search/ranked.rs), [src/search](https://github.com/cloudllm-ai/mentisdb/tree/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/search)). Context bundles group supporting graph-expanded context beneath lexical seed thoughts, which is closer to progressive disclosure than returning one flat mixed list.

**Vector and graph sidecars are rebuildable derived artifacts.** Persisted vector sidecars store source thought id, index, hash, vector, embedding metadata, thought count, head hash, generation time, and integrity digest; freshness checks compare them to the live chain ([src/search/sidecar.rs](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/search/sidecar.rs)). The implicit edge overlay derives top-k semantic neighbors from sidecar vectors and can rebuild from sidecar state ([src/search/implicit_edges.rs](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/search/implicit_edges.rs)). These artifacts rank and expand retrieval, but the thought chain remains the source of truth.

**The daemon turns the crate into MCP, REST, dashboard, and stdio infrastructure.** `src/server.rs` declares HTTP MCP, legacy MCP endpoints, REST routes for thoughts, search, ranked search, context bundles, chains, agents, entity types, vector rebuilds, skills, webhooks, extraction, and admin flush; `src/bin/mentisdb.rs` starts HTTP/HTTPS MCP, REST, and dashboard servers from `MENTISDB_*` environment configuration ([src/server.rs](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/server.rs), [src/bin/mentisdb.rs](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/bin/mentisdb.rs)). MCP initialize instructions tell agents to read the embedded skill resource, but memory content itself still returns through explicit tools such as ranked search, recent context, context bundles, and skill read.

**The skill registry is a versioned behavior store.** Skills are Markdown or JSON instruction bundles stored in `mentisdb-skills.bin`; the first version is full content, later versions are unified diffs, and lifecycle states include active, deprecated, and revoked. Uploads store uploader identity, content hash, optional signing metadata, and immutable versions; reads surface warnings and status ([src/skills.rs](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/skills.rs)). This is the system's strongest high-authority retained artifact surface, because a loaded skill can tell future agents how to operate.

**LLM extraction is candidate extraction, not automatic learning.** The `llm` module prompts an OpenAI-compatible model to extract typed memory records from free text, validates JSON into `ThoughtInput`, and returns an `ExtractionResult`; its module docs explicitly frame LLM output as untrusted and require callers to review, validate, and optionally sign before appending ([src/llm.rs](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/llm.rs)). The MCP/REST tool metadata repeats that extracted records are not automatically appended ([src/server.rs](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/server.rs)). That makes this a candidate-memory tool, not a trace-derived durable learning loop under this collection's tag rule.

**Context efficiency is mostly retrieval-time selection.** The system avoids loading whole chains by using filters, top-k limits, lexical/vector/graph ranking, context bundles, recent-context windows, summary-candidate windows, chain scope, agent scope, entity type, tags, concepts, time bounds, and memory scope ([README.md](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/README.md), [src/search/summary_index.rs](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/search/summary_index.rs)). Complexity is still host-managed: a caller decides which search surface to use, how many results to inject, and whether retrieved thoughts become prompt context, summaries, or instructions.

## Artifact analysis

**Committed thought chains.** Storage substrate: local chain files through `StorageAdapter`, with binary `.tcbin` as the supported new-chain storage, plus per-chain agent/entity registries. Representational form: mixed prose content, symbolic typed metadata, hashes, relations, timestamps, scopes, and optional signatures. Lineage: authored/manual, API-imported, or caller-approved candidate memories; `source_episode` can record an origin label, and hash chaining records append-order integrity, but exact source spans or model/prompt versions are not inherent to a thought. Behavioral authority: knowledge artifacts when searched or read as evidence/context; relation validity, dedup/supersession, scopes, and query filters have system-definition authority over what is eligible and current.

**Search indexes, vector sidecars, implicit edges, and context bundles.** Storage substrate: in-memory lexical/query indexes, persisted vector sidecar JSON files, persisted auto-edge overlays, and ephemeral bundle results. Representational form: symbolic indexes and scores plus distributed-parametric vectors. Lineage: derived from committed thoughts, embedding provider metadata, chain head hash, and graph relations; sidecar freshness and integrity metadata determine when to rebuild. Behavioral authority: ranking, selection, expansion, and grouping authority over read-back, not canonical memory authority.

**Skill registry entries.** Storage substrate: `mentisdb-skills.bin` under the MentisDB directory. Representational form: prose skill content plus symbolic manifests, tags, triggers, lifecycle status, warnings, content hashes, version ids, diffs, and optional signing metadata. Lineage: uploaded by registered agents or callers, versioned immutably, reconstructed from full base plus deltas, and lifecycle-marked by deprecation/revocation. Behavioral authority: system-definition artifact when an agent loads a skill; warnings and lifecycle status are governance metadata but the code stores signing metadata rather than proving effective safety by itself.

**MCP, REST, dashboard, CLI, stdio, Python, and host integration surfaces.** Storage substrate: repository source code, generated/user config files, dashboard static assets, and installed host configuration. Representational form: symbolic route/tool schemas, config patches, HTTP/TLS/auth settings, and prose bootstrap instructions. Lineage: authored integration layer over the crate. Behavioral authority: system-definition authority over available operations, authentication, setup, and recommended startup procedure. The integrations write MCP configuration for Codex, Claude Code/Desktop, Gemini, OpenCode, Qwen, Copilot CLI, and VS Code Copilot; they do not install a code-grounded relevance matcher that injects selected memories before each action ([src/integrations](https://github.com/cloudllm-ai/mentisdb/tree/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/integrations)).

**LLM extraction and summary candidates.** Storage substrate: extraction code, prompt templates, returned `ExtractionResult`, and read-only summary candidate outputs. Representational form: prose prompts plus symbolic schemas and typed candidate records. Lineage: derived from caller-supplied free text or existing thought windows, but not durable unless a caller separately appends the candidates as thoughts or summaries. Behavioral authority: candidate/advisory until accepted; the extraction prompt has system-definition authority over candidate shape, but not over durable memory admission.

**Auth, webhook, backup, and benchmark artifacts.** Storage substrate: bearer-token JSON with hashed tokens, webhook registry JSON, `.mentis` backup archives with manifests/checksums, and benchmark/test directories. Representational form: symbolic policy/state files and evaluation scripts/results. Lineage: authored operations code plus runtime-created registries/backups. Behavioral authority: authentication and chain-scope enforcement for MCP, event notification on append, disaster recovery, and evaluation evidence rather than ordinary memory content ([src/auth.rs](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/auth.rs), [src/webhooks.rs](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/webhooks.rs), [src/backup.rs](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/src/backup.rs), [benches](https://github.com/cloudllm-ai/mentisdb/tree/5a7d9a1588617f3e40a7fd62178da515b99e4390/benches), [lme-benches](https://github.com/cloudllm-ai/mentisdb/tree/5a7d9a1588617f3e40a7fd62178da515b99e4390/lme-benches), [locomo-benches](https://github.com/cloudllm-ai/mentisdb/tree/5a7d9a1588617f3e40a7fd62178da515b99e4390/locomo-benches)).

Promotion path: MentisDB has a strong manual promotion path from candidate thought or free-form text to committed thought, from committed thoughts to derived sidecars/bundles/summaries, and from skill drafts to immutable skill versions. It does not automatically promote raw traces into durable high-authority rules; callers or agents must choose to append thoughts or upload skills.

## Comparison with Our System

| Dimension | MentisDB | Commonplace |
|---|---|---|
| Primary purpose | Runtime durable memory daemon/crate for agents and agent fleets | Git-native methodology KB for agent-operated knowledge bases |
| Canonical artifact | Append-only hash-chained `Thought` and versioned skill entry | Typed Markdown notes, instructions, reviews, ADRs, sources, indexes |
| Storage substrate | Local binary chain files, sidecars, registries, service config | Repository files plus generated indexes and review/validation reports |
| Retrieval | Filtered search, ranked lexical/vector/graph search, context bundles, recent context, client wrappers | `rg`, descriptions, indexes, authored links, skills, validation/review outputs |
| Governance | Hash-chain integrity, signatures metadata, bearer tokens, skill lifecycle, backups, tests/benches | Git diffs, collection contracts, type specs, validation, semantic gates, archives |
| Activation | Explicit MCP/REST/CLI/dashboard/Python/LangChain calls plus bootstrap instructions | Mostly explicit pull through local search, instructions, and loaded skills |

MentisDB is stronger as a runtime service substrate. It has multiple transport surfaces, chain registries, auth tokens, webhooks, TLS/dashboard support, backup/restore, Python and LangChain clients, host setup writers, vector sidecars, and performance benchmarks. Commonplace is stronger as an inspectable library layer: each durable methodology artifact is a file with local type contracts, source citations, review status, and ordinary git history.

The largest design difference is artifact authority. In MentisDB, most thoughts are advisory knowledge artifacts until a host queries and places them into context. The skill registry can hold high-authority instructions, but loading and trusting those skills is a separate read path. In Commonplace, many retained artifacts are already system-definition artifacts: `COLLECTION.md`, type specs, instructions, and validators constrain later agents by design.

MentisDB's hash-chain and sidecar design is a useful contrast to Commonplace's plain-file approach. MentisDB gives append-order integrity, rebuildable search sidecars, and transport-ready service state. Commonplace gives line-diffable prose and simpler review of semantic claims. The right borrow is not "replace Markdown with thought chains"; it is "treat derived search state as disposable and trace it back to canonical artifacts."

Read-back: mostly pull, with unconditional or host-mediated context loading in some integrations. Agents or hosts call MCP/REST/CLI/dashboard/Python/LangChain search/read APIs, and the MCP bootstrap pushes instructions to load the core skill; I did not find a code-grounded relevance-gated pre-action memory-content injection path that warrants `push-activation`.

### Borrowable Ideas

**Rebuildable sidecars with freshness proofs.** Ready conceptually. Commonplace could give future vector/graph indexes explicit source artifact counts, source hashes, generation time, and freshness status so agents know whether a search layer is current.

**Separate baseline retrieval semantics from ranked retrieval experiments.** Ready now as design discipline. MentisDB keeps deterministic filtering separate from ranked/hybrid search. Commonplace should keep `rg`/indexes as stable primitives even if richer search layers appear.

**Use context bundles for grouped evidence.** Needs a concrete search UI or command. Grouping supporting notes beneath seed matches would fit Commonplace better than a flat top-k list when an agent is trying to understand why a claim or instruction surfaced.

**Treat skill registries as governed system-definition stores.** Ready as vocabulary. MentisDB's immutable versions, lifecycle status, warnings, uploader identity, and read format are useful design axes for Commonplace skills, but Commonplace should add stronger source review and validation before trusting generated or uploaded skills.

**Borrow `source_episode` only with stronger lineage.** Needs a trace workflow. An episode label is useful, but Commonplace should retain source snapshots, exact spans, or review reports when an extracted memory could affect future behavior.

**Do not borrow candidate extraction as automatic learning.** Ready now as a caution. MentisDB's LLM extraction is safer because candidates are not appended automatically; Commonplace should keep the same boundary for any trace-to-note assistant.

## Curiosity Pass

**The product story sounds more automatic than the durable write path.** README and skill language emphasize self-improving agents and fleets, but the implemented LLM extraction API returns candidates and leaves acceptance to callers. That is a good safety boundary, and it is also why this review does not mark the system trace-derived.

**The skill registry is more behavior-shaping than ordinary memories.** A thought retrieved as context can advise; a loaded skill can tell the agent what to do. Reviews of MentisDB-like systems should not flatten both into "memory."

**Append-only does not mean immutable meaning.** Later thoughts can supersede, correct, invalidate, summarize, branch from, or support earlier thoughts. Retrieval decides which relations matter at read time, so the chain is immutable while the effective knowledge state is temporal.

**LangChain memory is a push-capable host adapter, but not a relevance-gated recall engine.** `MentisDbMemory.load_memory_variables()` retrieves recent matching thought types and formats them into a prompt variable ([pymentisdb/langchain.py](https://github.com/cloudllm-ai/mentisdb/blob/5a7d9a1588617f3e40a7fd62178da515b99e4390/pymentisdb/langchain.py)). That is host-mediated context loading, but it is not the kind of engineered relevance-gated memory activation this collection tracks with `push-activation`.

**Operational features are unusually complete for a memory substrate.** Backup/restore, bearer tokens, TLS, dashboard, webhooks, migration, benchmark directories, and host setup writers make MentisDB more like a local memory appliance than a pure library.

## What to Watch

- Whether LLM extraction begins recording source spans, prompt/model versions, and acceptance decisions on appended thoughts; that would make candidate extraction auditable rather than merely typed.
- Whether a host integration adds real pre-action recall with a relevance signal, token budget, and injection path; that would change the read-back classification and likely add `push-activation`.
- Whether summary candidates grow into an automatic summarization/append loop, and whether that loop preserves `Summarizes` relations and review state.
- Whether skill signature metadata becomes enforced verification before upload/read, especially for remote or multi-agent deployments.
- Whether vector sidecars and implicit edge overlays remain rebuildable support artifacts as retrieval grows more central to user workflows.
- Whether benchmark directories start measuring with/without-memory behavioral changes in agents, not only search quality or throughput.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: MentisDB stores rich memory and exposes many read surfaces, but most memory content reaches agents through explicit calls.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: thoughts, relations, vector sidecars, skills, auth tokens, webhooks, backups, and integrations need separate substrate, form, lineage, and authority labels.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: committed thoughts and search results mostly advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: skill entries, MCP/REST contracts, auth policy, extraction prompts, ranking code, and integration config constrain future behavior.
- [Automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) - contrasts: MentisDB can extract candidate memories but still leaves durable acceptance and high-authority promotion outside the automatic path.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - contrasts: MentisDB has the candidate extraction tool shape, but not an implemented durable trace-derived learning loop.
