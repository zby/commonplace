---
description: "ReframeWeb review: SurrealDB graph memory for a voice agent; LLM-hinted tag/substring + recency-cutoff retrieval, per-turn push, agent-emitted preference memories, no curation"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-07-07"
---

# ReframeWeb

ReframeWeb, by jubjub727, is an experimental "agent-native" workflow environment meant to replace the browser mental model with semantic Stores, visual panels, and a voice-driven assistant ("Reframe" / "Jarvis"). Most of that vision (WebAssembly Semantic Stores, Rust Data Lenses, CEF/React Visual Panels, Compute Modules) is still future-facing architecture; the only running code is a Python "Agent Host" that runs a voice turn through a BAML-driven decision pipeline, plus a SurrealDB-backed **memory graph**. This review covers the memory subsystem (`agent-host/src/reframe_memory/`) and the flow that consumes it, not the voice pipeline.

**Source:** https://github.com/jubjub727/ReframeWeb

**Reviewed commit:** [5b8726b39da4ad01f03bb67294b286b4652cb0f1](https://github.com/jubjub727/ReframeWeb/commit/5b8726b39da4ad01f03bb67294b286b4652cb0f1)

**Last checked:** 2026-07-07

## Core Ideas

**A single typed node table over a SurrealDB graph, addressed through fixed roots.** The schema defines one `memory_node` table (an array of `tags`, a `FLEXIBLE` object `content`, and `created_at`/`updated_at`/`read_at` datetimes) plus a `memory_root` table, wired by RELATION tables `contains`, `provides_task`, `has_conversation`, `has_message` (carrying a `position`), and `has_session_memory` ([reframe_memory/schema.py](https://github.com/jubjub727/ReframeWeb/blob/5b8726b39da4ad01f03bb67294b286b4652cb0f1/agent-host/src/reframe_memory/schema.py)). Eleven fixed roots (`providers`, `tasks`, `sessions`, `conversations`, `session_memories`, `task_choice_memories`, `conversation_evaluation_memories`, `search_depth_memories`, `relevance_memories`, `task_prompt_memories`, `user_preferences`) are upserted at startup and every node hangs off one of them ([reframe_memory/database.py](https://github.com/jubjub727/ReframeWeb/blob/5b8726b39da4ad01f03bb67294b286b4652cb0f1/agent-host/src/reframe_memory/database.py)). The store defaults to embedded SurrealKV (`surrealkv://.reframe-memory`), so it degrades to a local on-disk database rather than a hosted service ([reframe_memory/config.py](https://github.com/jubjub727/ReframeWeb/blob/5b8726b39da4ad01f03bb67294b286b4652cb0f1/agent-host/src/reframe_memory/config.py)).

**Context efficiency: retrieval is relation-scoped, precision-biased, and gated on recency rather than ranked.** Retrieval never scans the node table globally; it walks from a root along typed relations (task root → tasks; sessions → conversations → messages / session-memories), so scope is bounded by graph structure ([reframe_memory/graph_retrieval.py](https://github.com/jubjub727/ReframeWeb/blob/5b8726b39da4ad01f03bb67294b286b4652cb0f1/agent-host/src/reframe_memory/graph_retrieval.py)). A candidate is kept only if it passes both a `TimestampBreadth` (per-domain recency window) and positive `GraphSearchHints` (tag intersection or case-insensitive substring on named content fields); with no positive hint, nothing matches ([reframe_memory/retrieval_terms.py](https://github.com/jubjub727/ReframeWeb/blob/5b8726b39da4ad01f03bb67294b286b4652cb0f1/agent-host/src/reframe_memory/retrieval_terms.py)). There is no top-k, no token budget, and no embedding or semantic score anywhere in the code — "relevance" is tag/substring match plus a recency cutoff, later pruned by an LLM. Volume is thus controlled indirectly (by how tight the LLM makes the hints and the window), not by an explicit budget.

**Recency, including "recently read," is the ranking proxy.** `TimestampBreadth` requires `created_at` and `updated_at` after per-domain cutoffs, and — distinctively — a node also fails if it was read *before* the `read_after` cutoff (a never-read node always passes). Because every serve marks the returned nodes read (`mark_records_read` / `mark_record_ids_read` set `read_at = time::now()`), a memory surfaced on one turn is suppressed on later turns until its window reopens ([reframe_memory/database.py](https://github.com/jubjub727/ReframeWeb/blob/5b8726b39da4ad01f03bb67294b286b4652cb0f1/agent-host/src/reframe_memory/database.py)). This is an anti-repetition / freshness mechanism built into the read path itself.

**The pipeline is a chain of BAML LLM stages, each seeded by its own few-shot memory pool.** A turn runs: choose task → generate memory search hints → choose per-domain timestamp breadth → retrieve from graph → LLM relevance filter → build task prompt → execute ([README.md](https://github.com/jubjub727/ReframeWeb/blob/5b8726b39da4ad01f03bb67294b286b4652cb0f1/README.md)). Each decision stage reads a dedicated root of `{title, description}` example memories (`task_choice_memories`, `relevance_memories`, `search_depth_memories`, etc.) and passes them into the BAML call as few-shot context ([agent_flow/task_choice.py](https://github.com/jubjub727/ReframeWeb/blob/5b8726b39da4ad01f03bb67294b286b4652cb0f1/agent-host/src/reframe_agent_host/agent_flow/task_choice.py)). These pools are the intended "learn how to steer the pipeline" surface, but no production code writes to them (see Write side).

**Trust and adoption.** Memory is plain structured records in a local embedded DB: inspectable via SurrealQL, no metered API, no cloud lock-in. There is no source-preservation, review-state, or validation metadata on memories — a `SessionMemory` is just an LLM-authored `{title, description}` pair with tags; nothing records where it came from or whether it was ever confirmed. Model choice is pushed into the memory graph itself: a `Provider` node names a `baml_surface`, `model_id`, and `reasoning_effort`, so per-task model routing is data, not config ([reframe_memory/models.py](https://github.com/jubjub727/ReframeWeb/blob/5b8726b39da4ad01f03bb67294b286b4652cb0f1/agent-host/src/reframe_memory/models.py)).

## Artifact analysis

- **Storage substrate:** `graph` — All retained state is SurrealDB `memory_node`/`memory_root` records joined by RELATION edges; the default backend is embedded SurrealKV on local disk. It is used graph-first (root-anchored relation traversal), not as a document or vector store.
- **Representational form:** `prose` `symbolic` — Memory payloads are natural-language prose (session-memory and preference `title`/`description`, conversation `content`, task descriptions/prompts); the tags, graph relations, `position`, timestamps, and `Provider` model/effort fields are symbolic scaffolding. No parametric form — there are no embeddings, weights, or adapters in the code.
- **Lineage:** `authored` `trace-extracted` — Session memories and user preferences are authored inline by the agent's own turn output; tasks and providers are authored by seed scripts; the session→conversation→message tree is retained interaction history (transcript), i.e. trace-extracted. No `imported` (nothing external is ingested) and no automatic distillation of the transcript into new memory.
- **Behavioral authority:** `knowledge` `routing` `ranking` — Session/preference memories and transcripts are injected as advisory context (knowledge); the task catalog is the routable option set consumed by the task-choice decision (routing); the per-stage few-shot pools bias the LLM decisions (ranking/routing steer). Everything is advisory — no memory is an enforced gate or a validator, and effective authority is *not verified from code* (no test shows a retrieved memory changing the final output).

**Standing preference / session memory** (`SessionMemory`, `UserPreferenceMemory`). LLM-authored `{title, description}` nodes the agent emits during a turn to remember a durable fact ("always use compact view for this site"). Consumed later as advisory context; `session_memory` is scoped to its session via `has_session_memory`, `user_preference` is global ([task_execution/primitives.py](https://github.com/jubjub727/ReframeWeb/blob/5b8726b39da4ad01f03bb67294b286b4652cb0f1/agent-host/src/reframe_agent_host/task_execution/primitives.py)).

**Conversation transcript** (`Session` → `Conversation` → `ConversationMessage`). Human utterances, agent replies, and agent thoughts are recorded live with an ordering `position`; this is the retained execution trace, held as knowledge/continuity rather than distilled into anything ([reframe_memory/conversations.py](https://github.com/jubjub727/ReframeWeb/blob/5b8726b39da4ad01f03bb67294b286b4652cb0f1/agent-host/src/reframe_memory/conversations.py)).

**Task catalog and providers.** `Task` nodes (`name`, `description`, `input`, `output`, `prompt`, `provider_id`) are the routable capability set; `Provider` nodes bind each task to a BAML surface, model id, and reasoning effort. Seeded, not learned ([memory_seed/core_task_seed.py](https://github.com/jubjub727/ReframeWeb/blob/5b8726b39da4ad01f03bb67294b286b4652cb0f1/agent-host/src/reframe_agent_host/memory_seed/core_task_seed.py)).

**Per-stage few-shot memory pools.** Five roots of `{title, description}` example memories, one per BAML decision stage, read via `.search()` and passed as few-shot examples to steer that stage ([agent_flow/memory_relevance.py](https://github.com/jubjub727/ReframeWeb/blob/5b8726b39da4ad01f03bb67294b286b4652cb0f1/agent-host/src/reframe_agent_host/agent_flow/memory_relevance.py)). Architecturally the system's adaptation surface, but currently written only by tests/benchmarks.

**Promotion path.** None implemented. There is no route that moves an advisory memory toward a validator, an enforced instruction, or a reviewed rule; the few-shot pools could in principle promote observed decisions into steering examples, but nothing writes them in production.

## Comparison with Our System

ReframeWeb and Commonplace agree on one adoption bet — memory should be locally inspectable with no hosted dependency — but reach it differently: Commonplace uses version-controlled Markdown files, ReframeWeb uses an embedded database. The database costs diffability, rename-stable links, and git history; it buys typed relation traversal and cheap timestamp gating.

The sharper divergence is trust discipline. Commonplace wraps each retained artifact in a type contract, source citations, validation, and review gates before it can shape future work. A ReframeWeb memory is an unvalidated LLM-authored `{title, description}` with no provenance, no review state, and no faithfulness check — it is trusted the moment the agent emits it. Where Commonplace's read-back is a deliberate `rg`/index pull the operator can audit, ReframeWeb pushes memory into every turn automatically and never tests whether it landed.

ReframeWeb's most novel idea relative to us is treating recency — including "recently read" — as the whole relevance model, with the read itself mutating the store to suppress repeats. Commonplace deliberately keeps reads side-effect-free.

### Borrowable Ideas

**LLM-planned retrieval as a two-stage query (hints + breadth).** Splitting "what to look for" (tags/strings) from "how far back to look" (per-domain recency window), both LLM-chosen, is a clean separation. In Commonplace this would look like a router that emits an `rg` term set plus a freshness scope before a sweep. Needs a concrete use case — our retrieval is operator-driven, so the value only appears with autonomous multi-turn agents.

**Parent-wrapper hydration.** When a child node matches (a message, a session-memory), the retriever includes its unmatched ancestor (conversation, session) purely so the match is legible in context. The Commonplace analogue is auto-including a note's index/section header when a fragment matches. Ready-ish as a navigation nicety; needs a use case to justify the complexity.

**"Recently read" suppression as an anti-repetition read filter.** Ready only as an idea to watch, not adopt: it couples reads to writes (our reads are pure) and can hide a persistently relevant memory. Worth noting as a design point, not importing.

**Per-decision few-shot example pools as memory.** The pattern of a dedicated, growable example store per pipeline stage is interesting, but ReframeWeb has not wired the writer, so there is no evidence it works. Needs a use case first.

## Write side

**Write agency:** `automatic` — The store changes as a side effect of the agent flow, with no human curator in the loop: `voice-turn` creates session/conversation nodes, each turn records human/agent/thought messages, and the agent's own `session_memory` / `user_preference` action primitives create durable memory nodes ([task_execution/primitives.py](https://github.com/jubjub727/ReframeWeb/blob/5b8726b39da4ad01f03bb67294b286b4652cb0f1/agent-host/src/reframe_agent_host/task_execution/primitives.py)). Tasks/providers arrive via seed scripts. The five few-shot pools have no production writer at all — only benchmarks and tests call their `.create()`.

**Curation operations:** `none` — Every automatic write is *acquisition*: create a message node, create a memory node, seed a task. Nothing operates over already-stored memory — no consolidate, dedup, evolve, synthesize, invalidate, decay, or promote. The one recurring in-place write is the *read_at* timestamp stamped on served nodes, which is access-tracking maintenance for the recency filter, not content curation. Duplicate or contradictory memories simply accumulate.

## Read-back

**Read-back:** `push` — Retrieval is not a tool the executing agent chooses to call; the host runs the full retrieve → relevance-filter → inject chain automatically on every voice turn and hands the kept memories to the task-prompt stage ([agent_flow/memory_retrieval.py](https://github.com/jubjub727/ReframeWeb/blob/5b8726b39da4ad01f03bb67294b286b4652cb0f1/agent-host/src/reframe_agent_host/agent_flow/memory_retrieval.py)). From the executing agent's perspective the memory arrives unsolicited; the search hints are themselves produced by an upstream BAML stage (orchestrator-side), which is push to the receiver.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / judgment` — Current-session memories are always loaded regardless of hints or breadth (`coarse` always-load). Tag hints match against a node's assigned `tags` (`identifier`). String hints do a case-insensitive substring test on named content fields (`inferred / lexical` — content-keyed, sense-blind). A final BAML relevance stage (`EvaluateRelevantMemories`) prunes candidates to `kept_memory_ids` by LLM judgment (`inferred / judgment`).

**Faithfulness tested:** `no` — The repo has benchmark harnesses (`test_task_choice_benchmark`, `test_memory_relevance_benchmark`, `test_conversation_evaluation_benchmark`, control-flow/search-depth) that score each stage's *decision* against expected cases, but none run a WITH/WITHOUT-memory ablation on the final task output, so nothing verifies that injected memory actually changes behavior.

**Direction edge cases.** Retrieval is precision-biased to the point of silence: `GraphSearchHints` with no positive tag or string matches nothing (confirmed by `test_empty_positive_hints_do_not_match_historic_candidates`), so on a turn where the hint-generation stage emits nothing, only the always-loaded current-session memories reach the agent. Everything else is gated behind an LLM-supplied hint.

**Targeting and signal.** Positive tags are `any_of ∪ all_of` intersected with the node's tags (an assigned-symbol match, `identifier`); strings are substring `contains` (or exact `equals`) over the type's searchable content fields — `name` for tasks/sessions/conversations, `title`/`description` for memories, `role`/`content` for messages. `none_of` tags exclude. There is no embedding or lexical-index scoring; substring is the only content signal.

**Injection point.** All resolution happens pre-invocation: hints, breadth, graph match, and the relevance prune all run before the task-prompt/execution model call. The post-turn work (recording the new messages, stamping `read_at`) is write-side maintenance, not a second read.

**Selection, scope, complexity.** No top-k and no token budget — the kept set is whatever passes hints+breadth and survives the LLM relevance prune. Scope is per-domain (`task_catalog`, `past_conversation_context`) plus the always-on current session. Loaded complexity can be non-trivial: a matched message pulls in its sibling messages and ancestor wrappers, so a single hit can hydrate a whole conversation slice. Actual context dilution is runtime and *not verified from code*.

**Authority at consumption.** Injected memory is advisory context inside a generated task prompt; it is never a hard gate. Effective authority needs the faithfulness check that is absent.

## Curiosity Pass

- **The declared "learning" surface is empty scaffolding.** The five per-stage few-shot pools are read on every turn but have no production writer — only tests populate them. As shipped, the pipeline's adaptive steering runs on empty example sets; the system's most interesting adaptation mechanism is unwired.
- **"Graph memory" is a shallow tree, not graph reasoning.** Relations only scope traversal (root→child, session→conversation→message). There are no multi-hop queries, path ranking, or graph algorithms; a relational or document store with the same parent links would behave identically. The graph substrate buys traversal-scoping, nothing more.
- **Recency-as-relevance can hide durable truths.** A `user_preference` like "always scroll slowly" is exactly the memory you want on every turn, yet the `read_after` cutoff plus read-stamping can suppress it after it surfaces once, until its window reopens. Only current-session memories are exempt (always-loaded). Whether long-lived preferences survive the recency filter is untested.
- **Memories never die or merge.** With `Curation operations: none`, repeated or contradicting preferences accumulate as separate nodes; the only bound on growth is the retrieval filter, not any consolidation or invalidation.
- **`website_memory` is declared but unsupported.** The primitive dispatcher lists `website_memory` (and window/website actions) as explicitly *unsupported*, so the browser-scoped memory the vision promises is not yet a memory type — the only durable agent-authored memories today are session memory and user preference.

## What to Watch

- Whether the per-stage few-shot pools get a production writer that distills observed decisions into steering examples — that would turn the pipeline into genuine trace-derived learning and would require re-tagging this review `trace-derived`.
- Whether substring matching is replaced by embeddings or a lexical index; the current tag+substring+recency model is the load-bearing retrieval design and its precision-or-silence behavior is a real limitation.
- Whether any curation lands (dedup/invalidate over accumulating preference memories, or consolidation of transcripts) — today the store only grows.
- Whether a faithfulness/ablation harness appears; the benchmarks score decisions but never test that injected memory changes the final output.
- Whether `website_memory` and the Store/Lens/panel layer ship, adding a website-scoped memory type and new consumers beyond the voice loop.

## Related Systems

- [graphiti](./graphiti.md) - compares-with: both classify their storage substrate as `graph`, but ReframeWeb's "graph memory" is a shallow root→child tree that (its own Curiosity Pass admits) a relational store would serve identically, whereas Graphiti actually exploits graph structure — BFS expansion, communities, multi-hop, hybrid BM25+embedding+traversal. Same substrate label, opposite answer to "does the graph earn its keep?"
- [siftly](./siftly.md) - compares-with: both run two-stage retrieval — a lexical/structured candidate narrowing (ReframeWeb: LLM-emitted tag/substring hints + per-domain recency breadth; Siftly: FTS5 + category-intent regex + keywords) followed by an LLM rerank/prune — and both carry the identical precision-or-silence failure, where a hard miss in candidate selection prevents the LLM stage from ever seeing a relevant item.
- [reasoning-bank](./reasoning-bank.md) - compares-with: both break read-purity by giving retrieval a store-mutating side effect — ReframeWeb stamps `read_at` on served nodes to suppress repeats (anti-repetition/freshness), reasoning-bank appends the current task embedding to its cache on every retrieval (a side-effect log). Shared distinctive axis: retrieval is not side-effect-free, against the common design where reads are pure.
- [expel](./expel.md) - compares-with: both treat a pool of few-shot examples as retrievable memory that steers LLM decisions; ExpeL wires the writer (distills successful trajectories into the few-shot slot via a FAISS store), while ReframeWeb ships five per-stage example pools with no production writer — the wired-vs-scaffolding contrast on "few-shot examples as an adaptation surface."

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - grounds the read-back direction and the observation that ReframeWeb pushes memory every turn but never tests activation.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains why the targeted push depends on LLM-emitted tag hints and substring terms, and why empty hints yield silence.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - supports separating standing memories, transcripts, the task catalog, and few-shot pools by substrate, form, lineage, and authority.
- [Storage substrate](../../notes/definitions/storage-substrate.md) - classifies the embedded SurrealDB graph as the retained-state substrate.
- [Representational form](../../notes/definitions/representational-form.md) - frames the prose payload vs symbolic relation/timestamp scaffolding.
- [Lineage](../../notes/definitions/lineage.md) - distinguishes agent-authored preference memories from the retained (trace-extracted) transcript.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - classifies memories/transcripts as knowledge, the task catalog as routing, and the few-shot pools as ranking/routing steer.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - covers the advisory memories, transcripts, and few-shot examples.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - contrasts ReframeWeb's advisory-only memory with stronger instruction/enforcement/validation authority it lacks.
