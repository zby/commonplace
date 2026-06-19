---
description: "Memori review: SDK and agent integrations with trace-derived augmentation, SQL/Rust storage, hybrid recall, and pre-call memory injection"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# Memori

Memori, from `MemoriLabs/Memori`, is an agent/application memory SDK and hosted service. At the reviewed commit it includes Python and TypeScript SDKs, a Rust core for BYODB storage/retrieval/augmentation workers, SQL storage drivers, cloud agent endpoints, and integrations for OpenClaw, Hermes, Claude Code, and MCP-style recall. The central behavior is a loop around LLM calls: registered clients recall facts and recent history before invocation, persist the completed turn after invocation, and send the turn to an augmentation service or Rust-backed pipeline that writes facts, semantic triples, process attributes, and conversation summaries.

**Repository:** https://github.com/MemoriLabs/Memori

**Reviewed commit:** [819a55fe9357a09fddaf1d9deccece473d18a40b](https://github.com/MemoriLabs/Memori/commit/819a55fe9357a09fddaf1d9deccece473d18a40b)

**Last checked:** 2026-06-04

## Core Ideas

**The SDK wraps LLM calls as a memory loop.** Python `Invoke` injects recalled facts and conversation history before the provider call, then writes the completed response and runs augmentation afterward; TypeScript registers Axon before/after hooks for recall, persistence, and augmentation in the same order ([memori/llm/invoke/invoke.py](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori/llm/invoke/invoke.py), [memori/llm/pipelines/post_invoke.py](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori/llm/pipelines/post_invoke.py), [memori-ts/src/memori.ts](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori-ts/src/memori.ts)). The direct `recall()` APIs remain available, but the registered client path makes memory ambient for the wrapped model call.

**BYODB storage is SQL-first, with Rust doing orchestration and retrieval math.** The new Rust core owns embedding, retrieval, background worker runtimes, augmentation submission, and a `RustStorageManager` bridge over SQLite, PostgreSQL/CockroachDB, and MySQL drivers; the TypeScript storage manager exposes host DB connections to that Rust bridge and serializes adapters that need it ([core/src/lib.rs](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/core/src/lib.rs), [core/src/storage/manager.rs](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/core/src/storage/manager.rs), [memori-ts/src/storage/manager.ts](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori-ts/src/storage/manager.ts)). Embeddings are stored in SQL rows rather than in a separate vector database in the inspected BYODB path.

**Augmentation is trace-derived and service-mediated.** Completed turns are converted into augmentation payloads containing user/assistant messages, attribution, session, LLM/provider metadata, and sometimes tool traces; local BYODB mode sends those through Rust or Python augmentation workers, while cloud mode posts to Memori collector endpoints ([memori/memory/augmentation/_handler.py](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori/memory/augmentation/_handler.py), [core/src/augmentation/pipeline.rs](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/core/src/augmentation/pipeline.rs), [memori-ts/src/engines/augmentation.ts](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori-ts/src/engines/augmentation.ts)). The extraction oracle is mostly the Memori API response contract, not an inspectable local prompt.

**Context efficiency is bounded retrieval plus provider-specific injection.** Recall embeds the user query, loads a bounded dense candidate set, reranks with BM25/lexical scoring, truncates to `limit`, filters by relevance threshold, then injects relevant fact lines and optional summaries into system/instruction context; cloud recall can also return recent conversation history for replay ([core/src/retrieval/pipeline.rs](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/core/src/retrieval/pipeline.rs), [core/src/search/api.rs](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/core/src/search/api.rs), [memori/llm/pipelines/recall_injection.py](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori/llm/pipelines/recall_injection.py), [memori-ts/src/engines/recall.ts](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori-ts/src/engines/recall.ts)). The visible policy limits volume; actual context dilution and recall quality are not proven by code alone.

**Agent integrations split between explicit recall tools and automatic capture.** Claude Code, Hermes, and OpenClaw expose agent recall, recall summary, compaction, quota, signup, feedback, and augmentation/capture surfaces; OpenClaw captures recent agent-end turns including tool calls when conversation access is enabled, while its memory recall is a tool the agent must call ([integrations/claude-code/index.ts](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/integrations/claude-code/index.ts), [integrations/hermes/src/memori_hermes/client.py](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/integrations/hermes/src/memori_hermes/client.py), [integrations/openclaw/src/index.ts](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/integrations/openclaw/src/index.ts), [integrations/openclaw/src/handlers/augmentation.ts](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/integrations/openclaw/src/handlers/augmentation.ts), [integrations/openclaw/src/tools/memori-recall.ts](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/integrations/openclaw/src/tools/memori-recall.ts)).

**Governance is mostly scoping, quotas, schemas, and best-effort failure handling.** Attribution requires entity/process identifiers; agent recall accepts project/session/source/signal filters; storage migrations enforce unique entity/fact/triple rows; collector augmentation is usually fail-soft after the durable conversation write ([memori/__init__.py](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori/__init__.py), [memori/agent.py](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori/agent.py), [core/src/storage/migrations/sqlite.rs](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/core/src/storage/migrations/sqlite.rs), [memori-ts/src/engines/augmentation.ts](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori-ts/src/engines/augmentation.ts)). I did not find a local review artifact or provenance chain from extracted facts back to exact transcript spans beyond conversation/mention links and service responses.

## Artifact analysis

- **Storage substrate:** `rdbms` `service-object` `files` - BYODB stores entities, processes, sessions, conversations, conversation messages, entity facts, fact mentions, process attributes, and semantic triples in SQL databases through Python/TS/Rust drivers; cloud memory is accessed as hosted service objects through Memori APIs; integration manifests, skills, and CLI scripts live as repository files ([core/src/storage/migrations/sqlite.rs](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/core/src/storage/migrations/sqlite.rs), [core/src/storage/manager.rs](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/core/src/storage/manager.rs), [memori/storage/drivers/sqlite/_driver.py](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori/storage/drivers/sqlite/_driver.py), [integrations/claude-code/SKILL.md](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/integrations/claude-code/SKILL.md)).
- **Representational form:** `prose` `symbolic` `parametric` - Conversation text, facts, summaries, attributes, tool results, and injected memory context are prose; entity/process/session/project ids, source/signal filters, schema rows, semantic triples, hook/tool definitions, and SQL migrations are symbolic; embeddings and dense/BM25 blended ranking scores are parametric or learned retrieval state.
- **Lineage:** `authored` `trace-extracted` - SDK code, integrations, schemas, and prompts/tool descriptions are authored; memory facts, semantic triples, process attributes, summaries, conversation messages, and agent trace payloads are derived from completed LLM turns, user/assistant messages, tool calls, session summaries, and cloud augmentation responses.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` - Recalled facts and histories advise as knowledge context; injected `<memori_context>` and integration skill text instruct the model; entity/process/project/session/source/signal identifiers route memory; storage schemas, allowed source/signal pairs, and tool argument checks validate; dense, lexical, recency, and frequency signals rank; augmentation turns traces into durable memory artifacts.

**Conversation rows and messages.** These are raw or lightly normalized trace records: user/assistant messages are persisted with role/type/content and grouped by entity/process/session/conversation. They are knowledge artifacts as history and source material; in the registered client path they can also be replayed into the next call as short-term context ([memori/memory/_writer.py](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori/memory/_writer.py), [memori/llm/pipelines/conversation_injection.py](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori/llm/pipelines/conversation_injection.py), [memori-ts/src/engines/persistence.ts](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori-ts/src/engines/persistence.ts)).

**Entity facts and fact mentions.** Facts are prose records with embeddings, frequency counters, last-seen timestamps, uniqueness hashes, creation/update timestamps, and optional links to conversations. Recalled facts are knowledge artifacts; their embeddings and counters also carry ranking authority ([core/src/storage/drivers/sqlite.rs](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/core/src/storage/drivers/sqlite.rs), [core/src/retrieval/pipeline.rs](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/core/src/retrieval/pipeline.rs)).

**Semantic triples and process attributes.** Augmentation responses can produce entity triples and process attributes. The SQL tables deduplicate repeated triples/attributes by uniqueness keys and update counters, so these artifacts are symbolic/prose distilled memory rather than merely transcript storage ([memori/memory/_struct.py](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori/memory/_struct.py), [memori/memory/augmentation/augmentations/memori/_augmentation.py](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori/memory/augmentation/augmentations/memori/_augmentation.py), [core/src/augmentation/pipeline.rs](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/core/src/augmentation/pipeline.rs)).

**Recall and integration surfaces.** Registered SDK hooks are system-definition artifacts because they decide when stored memory is read and injected. Claude Code, Hermes, OpenClaw, and agent endpoints expose explicit recall/capture tools and configure scopes, but those tool surfaces do not by themselves prove that a host agent will call memory before acting ([memori-ts/src/memori.ts](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori-ts/src/memori.ts), [integrations/claude-code/index.ts](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/integrations/claude-code/index.ts), [integrations/hermes/src/memori_hermes/tools.py](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/integrations/hermes/src/memori_hermes/tools.py), [integrations/openclaw/src/tools/memori-recall.ts](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/integrations/openclaw/src/tools/memori-recall.ts)).

**Promotion path.** Memori promotes completed turns into stored conversation rows, then into extracted facts, triples, attributes, summaries, embeddings, and ranked recall context. Repetition promotes existing rows by incrementing `num_times` and refreshing `date_last_time`. It does not promote extracted facts into git-native reviewed notes or symbolic validators.

## Comparison with Our System

| Dimension | Memori | Commonplace |
|---|---|---|
| Primary purpose | Runtime memory for applications and coding agents | Git-native methodology KB for agents and maintainers |
| Canonical retained artifact | Conversation row, fact, triple, attribute, summary, embedding, service memory | Typed Markdown artifact with citations, links, validation, and review |
| Write path | Automatic post-call persistence and augmentation plus explicit tools/API | Authored notes, snapshots, indexes, validation, and review gates |
| Read-back | Registered-client push plus explicit pull APIs/tools | Mostly explicit pull through files, indexes, `rg`, links, and loaded instructions |
| Governance | Attribution scope, SQL constraints, source/signal filters, quotas, tests | Collection contracts, type specs, git diffs, citations, deterministic validation, semantic review |

Memori is stronger as an adoptable runtime layer. It sits in the LLM invocation path, captures turns without extra application code once registered, supports hosted and BYODB modes, and gives agent integrations a ready memory API. Commonplace is stronger as a durable knowledge system: the behavior-shaping artifacts are inspectable files with schema, links, citations, and review history.

The main tradeoff is authority visibility. Memori can insert extracted facts into a future model call quickly, but the extraction judgment and memory quality mostly live behind service responses and runtime rows. Commonplace makes memory slower to create and activate, but the intended authority, source, and revision are visible before the artifact shapes later work.

### Borrowable Ideas

**Registered-client recall hooks.** Needs a concrete Commonplace serving surface. The useful idea is not silent memory injection, but a clearly labeled pre-call hook that can cite exactly which reviewed artifacts were loaded.

**Per-request memory scopes.** Ready now as vocabulary. Memori's TypeScript `forRequest()` isolates entity/process/session state for concurrent backends; Commonplace could use the same distinction for workshop, project, and user-scoped temporary memory.

**Frequency and last-seen counters on repeated facts.** Ready for workshop memory, not library claims. Repetition can promote operational salience, but it should not by itself increase the truth authority of a methodology note.

**Agent compaction as an explicit endpoint.** Needs a use case. Memori's `agent_compaction` API is a good shape for continuing active work after truncation, but Commonplace should retain the compacted source bundle and distinguish compaction from durable synthesis.

**Source/signal pairs for agent memory filters.** Ready as a design reference. The Claude/OpenClaw integrations constrain allowed memory categories and derivation signals; Commonplace could adopt comparable controlled filters for temporary trace memory.

**Do not borrow opaque augmentation as final authority.** Memori's service-mediated extraction is useful for runtime continuity. Commonplace should require visible provenance and review before extracted behavior becomes instruction, validation, or durable theory.

## Write side

**Write agency:** `manual` `automatic` - Manual writes come from SDK/API/tool calls such as explicit capture, augmentation, compaction, feedback, and storage operations in the SDK and agent integrations; automatic writes come from registered LLM after-hooks, persistence engines, Rust/Python augmentation workers, cloud collector calls, and OpenClaw agent-end capture.

**Curation operations:** `consolidate` `dedup` `promote` - Conversation summaries consolidate stored turn material into a shorter summary row; duplicate facts, triples, and process attributes are merged by uniqueness keys; repeated facts/triples/attributes increment `num_times` and refresh `date_last_time`, and retrieval loads recent/frequent fact rows first. Fact/triple extraction itself is acquisition from traces, not a curation operation on already-stored memory.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` - Qualifying traces include conversation messages, completed user/assistant turns, OpenClaw tool calls/results, Claude Code advanced-augmentation traces, session ids, project ids, and provider/model metadata.

**Learning scope:** `per-project` `cross-task` - Memory is scoped by entity/process/session in the core SDK and by project/session in agent endpoints; persisted facts and summaries can affect later calls for the same entity/project across tasks.

**Learning timing:** `online` `staged` - Registered SDK calls persist and augment after each model response; collector augmentation is background/best-effort after durable turn writes; Rust and Python augmentation workers process jobs asynchronously and expose `wait` helpers.

**Distilled form:** `prose` `symbolic` `parametric` - Distilled outputs include prose facts and summaries, symbolic triples/attributes/source-signal metadata/scope ids, and embeddings/rank scores used for later retrieval.

**Extraction.** The raw input is the completed turn plus metadata and optional trace. In BYODB Python mode, `AdvancedAugmentation` sends selected messages and existing summary to the Memori API, parses facts/triples/process attributes/conversation summary from the response, embeds facts, and schedules DB writes. In Rust mode, `run_advanced_augmentation` builds the same style of payload, calls `sdk/augmentation`, builds write batches, and attaches fact embeddings before storage ([memori/memory/augmentation/augmentations/memori/_augmentation.py](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori/memory/augmentation/augmentations/memori/_augmentation.py), [core/src/augmentation/pipeline.rs](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/core/src/augmentation/pipeline.rs)).

**Scope and timing.** The loop is optimized for immediate continuity: memory is written after a completed turn and can be recalled before later calls. Agent integrations preserve project/session scope, but the strongest extraction logic is service-mediated, so code alone does not show the prompt, model policy, or quality threshold that decides which trace-derived claims become facts.

**Survey fit.** Memori fits the trace-to-runtime-memory family: session transcripts and agent/tool traces become durable facts, summaries, triples, attributes, and embeddings. It strengthens the survey distinction between trace acquisition and curation: much of its apparent intelligence is extraction from new traces, while the visible store-maintenance operations are duplicate merge, summary update, and salience counters.

## Read-back

**Read-back:** `both` - Direct SDK/API/agent tools expose explicit pull recall, but registered Python and TypeScript LLM clients also retrieve memory and inject facts/history into the next provider request before the receiving model acts.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / embedding` - Conversation history replay is coarse within the current session; entity/process/project/session/source/signal ids scope recall; query text is inferred from the user's prompt; BYODB retrieval uses embeddings plus BM25 lexical reranking, while cloud agent recall exposes service-side filters and ranking.

**Faithfulness tested:** `no` - I found tests for recall injection, augmentation payloads, storage writes, ranking, source/signal validation, and integration mechanics, but not a with/without memory ablation or post-action audit proving that injected memory changes downstream agent behavior correctly.

**Direction edge cases.** The OpenClaw plugin itself registers memory tools and appends static skill/config context, while actual memory recall is a tool call; that is pull for retained memory. The SDK registration path is different: `inject_recalled_facts` and TypeScript `handleRecall` run before the model call and modify the request whether or not the model explicitly asked for memory, so deployed registered-client use is push from the model's perspective ([memori/llm/pipelines/recall_injection.py](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori/llm/pipelines/recall_injection.py), [memori-ts/src/engines/recall.ts](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/memori-ts/src/engines/recall.ts), [integrations/openclaw/src/index.ts](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/integrations/openclaw/src/index.ts)).

**Targeting and signal.** Registered-client push is instance-targeted by the latest user query, entity id, and sometimes session history. Agent recall tools can filter by project, session, source, signal, and date. Claude Code recall intentionally avoids defaulting to session id so reads stay project-scoped across new Claude Code sessions unless a session filter is passed ([integrations/claude-code/index.ts](https://github.com/MemoriLabs/Memori/blob/819a55fe9357a09fddaf1d9deccece473d18a40b/integrations/claude-code/index.ts)).

**Injection point.** Read-back is pre-invocation in registered clients: facts are inserted into Anthropic/Bedrock system text, Google system instructions, OpenAI-style system messages, or Responses API instructions before the provider call; conversation history can be prepended before the current messages. Post-response persistence and augmentation are write-side maintenance for later turns, not read-back for the current answer.

**Selection, scope, and complexity.** BYODB retrieval loads up to `recall_embeddings_limit` embedding rows, dynamically overfetches candidates, reranks with dense plus lexical scores, truncates to a configured limit, then filters by threshold before injection. Complexity is moderate: the injected context can include facts, summaries, and conversation history, not just flat fact strings. Effective precision/recall and context dilution are not verified from code.

**Authority at consumption.** Recalled facts are framed as relevant context and include an instruction to use them only if relevant. That is advisory/instructional prompt authority, not enforcement. Tool descriptions can strongly nudge agents to call recall before claiming ignorance, but compliance depends on the host agent.

**Other consumers.** Humans and agents can inspect or request memory through dashboard/cloud APIs, CLI commands, Claude Code skill commands, Hermes memory tools, OpenClaw tools, and SDK `recall`/`agent_recall` methods. Rust/Python/TS storage and augmentation workers consume the same state operationally for search, history replay, and further augmentation.

## Curiosity Pass

**The storage story changed from vector-store framing to SQL embedding rows.** The reviewed BYODB implementation stores embeddings beside facts in SQL tables and searches them through Rust, so classifying it as a separate vector-store system would overstate the current code.

**The strongest memory behavior is in wrapper registration, not in the manual recall API.** A host that only uses `mem.recall()` or MCP-style tools is pull-first; a host that registers the LLM client gets automatic pre-call recall.

**The graph vocabulary is implemented as relational triples.** Memori writes subject/predicate/object tables and a `memori_knowledge_graph` table, but I did not find a graph database or traversed graph reasoning as the canonical retrieval path at this commit.

**The augmentation oracle is partly outside the repo.** The code shows payload construction and response handling, but not the service prompt/model policy that decides which facts, summaries, or triples are produced.

**Conversation replay has a practical compatibility filter.** Python and TypeScript drop malformed tool messages or empty assistant tool-call turns before replaying history, which is a small but useful example of context-quality guardrails.

## What to Watch

- Whether BYODB augmentation becomes fully local and inspectable rather than service-mediated; that would change the provenance and reviewability of trace-derived facts.
- Whether recall gains behavioral ablations or post-answer audits; that would upgrade the faithfulness assessment from plumbing-tested to behavior-tested.
- Whether agent recall source/signal filters become backed by visible stored fields in the open BYODB path; that would make cloud and local governance more comparable.
- Whether semantic triples become part of retrieval beyond insertion and counting; that would change the artifact analysis from relational side structure to active graph memory.
- Whether OpenClaw or Claude Code integrations add automatic memory insertion rather than explicit recall tools; that would change typical deployed agent read-back for those integrations.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Memori has both explicit recall tools and registered-client pre-call injection.
- [Trace-derived learning techniques in related systems](../../trace-derived-learning-techniques-in-related-systems.md) - places: Memori turns conversation and agent traces into facts, triples, attributes, summaries, and embeddings.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: Memori's conversations, facts, triples, summaries, embeddings, hooks, and tools differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: recalled facts, summaries, and conversation history mostly advise later action.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: SDK hooks, storage schemas, source/signal validators, and integration tool definitions route or constrain memory behavior.
- [Use trace-derived extraction as meta-learning](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - relates: completed turns and tool traces are distilled into retained memory for later tasks.
