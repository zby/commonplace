---
description: "MentisDB review: append-only hash-chained agent memory with MCP/REST tools, skill registry, LLM extraction, and LangChain memory"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
last-checked: "2026-06-04"
---

# MentisDB

MentisDB, from `cloudllm-ai/mentisdb`, is a Rust daemon and library for durable agent memory. It stores semantically typed "thoughts" in append-only hash-chained memory chains, exposes them through MCP, REST, CLI, dashboard, Python, and LangChain surfaces, and includes a versioned skill registry for agent instruction bundles. At the reviewed commit, the strongest implemented memory behavior is a governed store plus explicit retrieval tools; automatic context return exists as a LangChain memory adapter capability rather than as the default MCP/REST agent loop.

**Repository:** https://github.com/cloudllm-ai/mentisdb

**Reviewed commit:** [204afbdceff3e3f69cb779e3c7a30002076f7f22](https://github.com/cloudllm-ai/mentisdb/commit/204afbdceff3e3f69cb779e3c7a30002076f7f22)

**Source directory:** `related-systems/mentisdb`

## Core Ideas

**Thoughts are append-only, typed, linked records.** `ThoughtInput` carries semantic type, role, content, confidence, importance, tags, concepts, refs, relations, entity type, source episode, and optional signing fields; `append_thought` validates refs, converts refs into `References` relations, adds timestamps and hashes, writes through the storage adapter, and indexes the committed `Thought` ([src/lib.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/lib.rs)). The hash chain and append-only update style make memory auditable, but not automatically true.

**The retrieval stack is hybrid and bounded by request shape.** `query_ranked` filters candidates, scores lexical matches with synonyms, optionally scores vectors and graph expansion, adds session-cohesion boosts, and can rerank lexical/vector/graph lists with RRF before truncating to `limit`; context bundles group graph-expanded support under lexical seed thoughts ([src/lib.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/lib.rs), [src/search/bundle.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/search/bundle.rs)). Context efficiency is therefore selection-time: filters, limits, seed bundles, graph depth, and reranking constrain volume, while the complexity can still include flat thoughts, graph support, branch/ancestor results, and recent context.

**MCP and REST are broad agent-facing surfaces.** The server exposes append, retrospective append, lexical/ranked/federated search, context bundles, recent context, traversal, bootstrap, branch/merge, agents, entity types, vectors, markdown import/export, skill registry operations, webhooks, extraction, and admin flush over REST and MCP-compatible tools ([src/server.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/server.rs)). MCP initialize instructions and `mentisdb://skill/core` teach agents how to use memory, but those baseline instructions are not themselves read-back of retained chain memory.

**Bearer tokens and the dashboard changed the operational boundary.** The daemon can require bearer tokens for MCP/REST requests, stores only token hashes in `bearer-tokens.json`, supports global and chain-scoped token records, and exposes token management through both CLI/dashboard-oriented APIs and dashboard UI code ([src/auth.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/auth.rs), [src/server.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/server.rs), [src/dashboard.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/dashboard.rs)). The dashboard also browses chains, searches, branches/merges, manages agents, skills, settings, vector sidecars, and bearer tokens; it is a human/operator surface, not just decoration.

**Skills are versioned behavior bundles beside memory chains.** `SkillRegistry` stores imported Markdown or JSON skill documents as immutable versions, tracks active/deprecated/revoked lifecycle state, supports search/read/upload/version/diff operations, and can require Ed25519 signatures for uploads from agents with registered keys ([src/skills.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/skills.rs), [src/server.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/server.rs)). This is the part of MentisDB most directly about system-definition artifacts, not just remembered facts.

**LLM extraction is opt-in candidate generation.** The `llm` module sends free-form text to an OpenAI-compatible chat completion API, validates returned JSON into `ThoughtInput` records, and returns them for review/sign/append; the MCP tool description repeats that extracted records are not automatically appended ([src/llm.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/llm.rs), [src/server.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/server.rs), [docs/llm-extracted-memories-design.md](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/docs/llm-extracted-memories-design.md)). That makes it trace-derived when the caller feeds agent traces and appends the reviewed output, but the durable write is a separate act.

## Artifact analysis

- **Storage substrate:** `files` `service-object` `in-memory` — Chain files, agent/entity registries, vector sidecars, auto-edge overlays, skill registries, webhook registries, bearer-token registries, TLS files, backups, and dashboard-static assets persist on disk; HTTP/MCP/REST/dashboard services expose shared in-process chain maps and registries while running ([src/lib.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/lib.rs), [src/server.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/server.rs), [src/backup.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/backup.rs)).
- **Representational form:** `prose` `symbolic` `parametric` — Thought content, summaries, skills, extracted memories, recent context, and memory markdown are prose; thought types, roles, scopes, tags, concepts, relations, hashes, signatures, bearer-token scopes, API schemas, tool contracts, registry rows, and lifecycle states are symbolic; vector sidecars, embedding scores, graph/lexical/vector/RRF scores, and optional LLM extraction outputs carry parametric/model-mediated behavior.
- **Lineage:** `authored` `imported` `trace-extracted` — Agents and humans author appended thoughts and skill versions; markdown import, REST/Python clients, and dashboard operations import outside text into chains; LLM extraction can transform free-form agent text, logs, or reasoning traces into typed `ThoughtInput` candidates that become trace-extracted durable memory only after review and append.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Thoughts, recent context, context bundles, and memory markdown advise as knowledge; MCP bootstrap text and skill documents instruct agents; bearer tokens, dashboard PINs, signature checks, revoked skills, and chain-scoped authorization enforce boundaries; chain keys, agent ids, scopes, tags, concepts, entity types, branches, and tool schemas route operations; refs, signatures, storage checks, extraction schemas, and backup manifests validate; retrieval scores and vector/graph/search indexes rank memory; LLM extraction and skill uploads let prior work change future retained artifacts.

**Thought chains.** The central knowledge artifacts are committed `Thought` records: typed prose memories with symbolic metadata, hashes, append indexes, optional signatures, relations, and retrieval fields. Superseded/corrected/invalidated targets remain stored for audit, while query paths can deprioritize or exclude them depending on relation state and `as_of` filters ([src/lib.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/lib.rs)).

**Indexes, vector sidecars, and graph overlays.** Lexical indexes, managed vector sidecars, implicit edges, query expansion, graph expansion, branch-aware/federated search, and context-bundle construction are derived access structures with ranking and routing authority. They help select memory, but the chain remains the evidence source ([src/lib.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/lib.rs), [src/search](https://github.com/cloudllm-ai/mentisdb/tree/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/search)).

**Skill registry.** Skills are system-definition artifacts: Markdown/JSON instruction bundles parsed into structured documents, uploaded as immutable versions, signed when required, and later read by agents or hosts. Search/read operations make them retrievable; deprecate/revoke state changes consumption safety without deleting history ([src/skills.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/skills.rs), [MENTISDB_SKILL.md](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/MENTISDB_SKILL.md)).

**Remote service controls.** Bearer-token records, dashboard PIN settings, agent public keys, webhook records, TLS certs, and server configuration are system-definition artifacts. They do not become memory content, but they decide who can read/write, which agents can sign, which endpoints receive append notifications, and how remote clients reach the store ([src/auth.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/auth.rs), [src/dashboard.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/dashboard.rs), [src/webhooks.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/webhooks.rs)).

**LLM extraction candidates.** Extracted `ThoughtInput` records are candidate artifacts until appended. Their prose content, type, importance, confidence, tags, and concepts come from an LLM oracle over supplied free-form text; the code validates schema and clamps scores but does not prove semantic truth. Once appended, they become ordinary chain thoughts with trace-derived lineage if the source text was an agent/session trace ([src/llm.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/llm.rs)).

**Promotion path.** MentisDB promotes free-form operational experience into durable chain thoughts, summaries/checkpoints, graph relations, vector/search state, versioned skills, and optionally LLM-extracted typed candidates. The strongest promotion crossing authority boundaries is skill upload: learned operational guidance can become an instruction bundle, but signature/lifecycle checks are the visible guardrails.

## Comparison with Our System

| Dimension | MentisDB | Commonplace |
|---|---|---|
| Primary purpose | Runtime memory daemon/library for agents and teams | Git-native methodology KB and framework |
| Canonical artifact | Hash-chained `Thought` plus metadata, relations, indexes, and optional signatures | Typed Markdown artifact with citations, links, validation, and review |
| Write path | Append tools/API, markdown import, skill upload, optional LLM extraction, automatic dedup relation | Authored notes/sources/reviews under collection/type contracts |
| Read-back | Explicit MCP/REST/CLI/Python pulls plus LangChain memory-variable capability | Mostly explicit file/index/search/link loading |
| Governance | Hashes, signatures, bearer tokens, dashboard PIN, skill lifecycle, scoped tokens, backup checks | Git diffs, schemas, collection contracts, citations, validation, semantic reviews |

MentisDB is stronger as a deployable runtime substrate. It gives existing agents a daemon, MCP/REST endpoints, dashboard, Python client, LangChain memory adapter, bearer-token auth, and a versioned skill registry. Commonplace is stronger where memory needs to become durable methodology: its notes carry explicit source citations, type contracts, curated links, validation, and review history.

The deepest divergence is source authority. MentisDB can preserve what an agent wrote, who wrote it, when, how it links, and whether it was signed, but it does not force a source-citation discipline for factual memories. Commonplace is slower and less automatic, but its maintained artifacts are designed to remain inspectable claims rather than only recalled runtime context.

### Borrowable Ideas

**Append-only relations with invalidation semantics.** Ready now as a design reference. Commonplace already archives/replaces files, but typed relations like `Corrects`, `Invalidates`, `Supersedes`, and `Summarizes` would make replacement semantics easier to query.

**Skill registry lifecycle states.** Ready for future skill governance. Active/deprecated/revoked states with immutable version history map well to Commonplace skills if we need runtime distribution beyond git.

**Scoped bearer tokens for agent memory tools.** Needs an API surface first. If Commonplace exposes MCP/HTTP read/write tools, chain/project-scoped bearer tokens are a useful operational boundary.

**Context bundles over seed memories.** Ready as an experiment. A Commonplace bundle command could return a query hit plus direct backlinks, sources, and type metadata under a token budget.

**LLM extraction as candidate generation only.** Ready as a policy. MentisDB's "return candidates, do not append automatically" is the right default for trace-derived memory that might later gain durable authority.

**Do not borrow ambient writes without citation discipline.** MentisDB makes appending easy; Commonplace should keep source snapshots, citations, validation, and review gates before extracted runtime experience becomes library theory or instruction.

## Write side

**Write agency:** `manual` `automatic` — Manual writes come from agents, humans, SDKs, CLI, REST/MCP tools, dashboard operations, markdown import, webhook registration, and skill uploads. Automatic writes include bootstrap-on-empty behavior, vector/index/registry sidecar updates after appends, and optional dedup relations added during `append_thought`; LLM extraction automatically generates candidate `ThoughtInput` records but requires a separate append to change the chain.

**Curation operations:** `dedup` — When `dedup_threshold` is configured, `append_thought` scans recent thoughts and adds a `Supersedes` relation to the most similar prior thought. `Corrects`, `Invalidates`, and `Supersedes` relations are retained and indexed so later queries can treat target thoughts as invalidated or superseded, but contradiction detection itself is caller-authored rather than automatic. Summary/checkpoint thoughts are authored append records, and extraction from new text is acquisition rather than curation over already-stored memory.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `trajectories` — The extraction API accepts free-form text and the design docs frame the input as conversational text, raw agent text, logs, or reasoning traces; the tool itself does not require a specific trace envelope.

**Learning scope:** `per-task` `per-project` `cross-task` — Scope depends on the chain key, agent id, tags, concepts, entity type, branch, and memory scope selected by the caller. A chain can be per session, project, user, team, branch, or fleet.

**Learning timing:** `online` `staged` — Agents can call extraction during a run, but extracted records are staged candidates until reviewed/signed/appended through the normal write path.

**Distilled form:** `prose` `symbolic` — Distilled candidates contain prose memory statements plus symbolic thought type, role, importance, confidence, tags, and concepts. Embeddings or vector sidecar state may later be built for appended thoughts, but extraction itself does not return parametric state.

**Extraction.** `extract_memories_from_text` sends the source text to an OpenAI-compatible chat completion API with a low-temperature prompt for typed JSON memories, parses the returned `thoughts` array, validates thought types/content, clamps scores, and returns `ThoughtInput` values ([src/llm.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/llm.rs)). The oracle is the configured model plus prompt; code verifies schema shape, not truth.

**Scope and timing.** This is not autonomous continual learning. The caller chooses what trace text to submit, receives candidates, and must decide whether to append them. That staged design reduces accidental authority transfer but means the trace-derived path is only as good as host discipline.

**Survey fit.** MentisDB belongs in the trace-to-structured-memory family with a review gate: traces can become typed memories, but the extraction service does not by itself make them durable or authoritative. It strengthens the distinction between extraction and store mutation.

## Read-back

**Read-back:** `both` — MCP/REST/CLI/Python search, recent-context, traversal, memory-markdown, and skill-read operations are explicit pull. The Python LangChain `MentisDbMemory` adapter also implements `load_memory_variables`, which retrieves recent thoughts and returns a `chat_history` string for pre-invocation prompt use when a host wires it into a LangChain chain ([pymentisdb/langchain.py](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/pymentisdb/langchain.py)).

**Read-back signal:** `coarse` `identifier` — The push-capable LangChain memory adapter loads up to 20 recent thoughts filtered by thought type and chain key. Lexical, vector, graph, session-cohesion, and RRF signals belong to explicit pull search surfaces rather than the push signal ([src/lib.rs](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/src/lib.rs), [pymentisdb/langchain.py](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/pymentisdb/langchain.py)).

**Faithfulness tested:** `no` — I found tests for server contracts, ranked search, context bundles, bearer-token auth, dashboard mechanics, extraction structure, and state sharing, but not a with/without memory ablation or post-action audit proving that returned memory changed downstream model behavior correctly.

**Direction edge cases.** The MCP bootstrap instructions, embedded skill, and tool descriptions push operating instructions to clients, but shipped operating instructions are baseline documentation, not retained memory read-back. `mentisdb_recent_context` and `mentisdb_ranked_search` are pull from the agent's perspective because the agent or host chooses the tool call. The LangChain adapter is the narrow push capability: if the application uses it as a memory variable, retained thoughts are loaded before the model call without the model asking for them.

**Targeting and signal.** Recent-context and LangChain memory are coarse within chain/type scope. Ranked search and context bundles are instance-targeted by query text and symbolic filters. Agent/tool instructions encourage startup `recent_context`, primary `ranked_search`, and checkpoint writes, but compliance depends on the host agent.

**Injection point.** The LangChain path returns a formatted string under `memory_key` before prompt assembly. MCP/REST read tools return data to the caller; any injection into a model context happens in the host harness after the pull. Post-append webhooks and index/vector rebuilds are write-side or access-structure maintenance, not read-back for the current action.

**Selection, scope, and complexity.** Search callers can constrain chain, limit, offset, thought type, role, tags, concepts, agent identity, owner, importance, confidence, time windows, scope, entity type, graph settings, reranking, and branch/federation. Complexity can grow beyond flat snippets when context bundles include supporting graph hits or federated results include ancestor/source chain annotations.

**Authority at consumption.** Returned memories are advisory context unless the host elevates them. Skill documents have stronger instruction authority, but the registry surfaces warnings and lifecycle state; bearer-token and signature checks govern access/provenance, not semantic correctness.

**Other consumers.** Humans consume the same memory through the dashboard, CLI, backups, markdown export, and Python client. Operators consume bearer-token, agent, skill, vector, backup, and settings state for administration.

## Curiosity Pass

**The name overstates semantic automation if used through MCP alone.** The MCP tools are powerful, but retained memory reaches the agent only when the agent or host calls the tools; startup instructions do not make stored thoughts ambient.

**LangChain memory ignores the current input query.** `MentisDbMemory.get_messages()` calls ranked search with no text and a limit of 20, filtered by thought type. That is closer to recent/history recall than semantic relevance to the current question ([pymentisdb/langchain.py](https://github.com/cloudllm-ai/mentisdb/blob/204afbdceff3e3f69cb779e3c7a30002076f7f22/pymentisdb/langchain.py)).

**The LLM extraction pipeline is safer than an auto-writer, but easy to overclaim.** The code produces candidate `ThoughtInput` records and explicitly does not append them. Any review should distinguish candidate extraction from durable learning.

**The dashboard is a real governance surface.** It can manage chains, agents, skills, bearer tokens, settings, vector sidecars, branches, imports, and restarts; that changes the system from a local memory library into an operator-managed service.

**Skill registry and memory chain authority are different.** Thoughts usually advise; skills instruct. MentisDB stores both, so consumers need to know whether they are reading evidence or behavior-shaping procedure.

## What to Watch

- Whether LangChain memory becomes query-aware or bounded by tokenizer budgets; that would change the push path from coarse history replay to targeted read-back.
- Whether `mentisdb_extract_memories` gains an optional append/review workflow; that would strengthen or weaken the staged trace-derived boundary depending on safeguards.
- Whether bearer-token settings become consistently documented for MCP and REST, since code enforces both when enabled.
- Whether skill provenance checks become mandatory for more paths; that would make the skill registry a stronger system-definition substrate.
- Whether context bundles get explicit token budgets and citation/provenance fields; that would make MentisDB easier to use for high-fidelity agent context.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: MentisDB stores durable chain memory, but MCP/REST read-back is mostly explicit pull.
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - relates: MentisDB's LLM extraction can turn agent/session text into typed memory candidates before append.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: thoughts, relations, vector sidecars, skill versions, bearer-token records, and dashboard settings carry different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: remembered thoughts, recent context, and context bundles mainly advise later work.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: skills, MCP tool contracts, bearer-token policy, signatures, and dashboard settings instruct or constrain behavior.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - relates: MentisDB has a staged extraction path from free-form traces to typed memory candidates.
