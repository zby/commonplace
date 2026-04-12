---
description: Proxy-owned context virtualization layer that compacts conversation and tool traces into durable summaries, facts, and demand-paged topic memory instead of treating retrieval as an additive sidecar
type: agent-memory-system-review
traits: [has-comparison, has-implementation]
tags: [related-systems]
status: current
last-checked: "2026-04-09"
---

# Virtual Context

Virtual Context is a Python package and HTTP proxy that sits between an LLM client and the upstream provider, rewrites the request payload, and persists conversation state into a service-managed memory store. The repo is broader than the landing-page pitch: beyond proxying Anthropic/OpenAI/Gemini formats, it ships a real engine, SQLite/Postgres/graph-backed storage paths, an MCP server, a TUI, and a large regression-heavy test suite. The core bet is not "add retrieval to a chat app" but "treat the context window itself as managed memory."

**Repository:** https://github.com/virtual-context/virtual-context

## Core Ideas

**The context window is treated as managed memory, not as a fixed buffer plus optional retrieval.** The proxy intercepts requests, tags the inbound message, retrieves relevant stored summaries, assembles a budgeted `<virtual-context>` block, and injects that into the provider-specific request shape. The implementation in `virtual_context/engine.py`, `virtual_context/core/retriever.py`, and `virtual_context/core/assembler.py` matches the architecture docs closely: retrieval and assembly are on the critical path before the upstream call, while response-side indexing and compaction happen after the turn.

**Conversation traces are promoted into a multi-layer symbolic memory store.** The stored substrate is not just embeddings or raw transcripts. SQLite schema and engine code show persistent segments, segment tags, tag summaries, turn messages, facts, fact links, aliases, and engine checkpoints. The README's three-layer picture is mechanically real in the shipped code: recent turns remain live, segment summaries compress topic slices, and tag summaries roll those slices into a higher-level working-set description.

**Tool-heavy agent traces are compressed as first-class memory objects rather than truncated away.** This is one of the strongest concrete mechanisms in the repo. The proxy collapses tool chains into compact stubs, preserves full outputs durably, and exposes restore/expand paths later. That is materially different from "just drop old tool output": the system keeps the trace available while reducing its prompt footprint. For coding-agent sessions, this is probably the most practically interesting part of the design.

**Retrieval is demand-paged and topic-shaped rather than "append nearest chunks."** The retriever combines multiple signals, skips already-active tags, and builds a scored candidate set; the assembler then greedily fills a bounded pool with retrieved tag sections and facts. MCP and proxy tool surfaces (`find_quote`, `remember_when`, `expand_topic`, `recall_all`) make the paging model explicit. The important distinction is that retrieval is coupled to eviction and working-set management, not layered on top of an unchanged transcript.

**The integration strategy is infrastructure-level compatibility.** Virtual Context prefers the proxy as the primary product boundary, then adds MCP, CLI, daemon mode, and a TUI around the same engine. That is a different distribution instinct from commonplace. We optimize the knowledge substrate and authoring conventions first; Virtual Context optimizes for "drop this in front of whatever client you already have."

## Comparison with Our System

| Dimension | Virtual Context | Commonplace |
|---|---|---|
| Primary unit of knowledge | Service-managed summaries, facts, tag memories, and stored traces in SQLite/Postgres/graph backends | Repo-hosted notes, links, instructions, and other authored symbolic artifacts |
| Main operating point | Runtime memory management for long live conversations | Durable methodology and library curation for future agent use |
| Distillation target | Compress the active conversation so the next inference fits and stays relevant | Compress reasoning into notes, indexes, skills, and instructions that survive beyond one session |
| Retrieval model | Automatic inbound retrieval plus explicit paging tools over stored session memory | Search, descriptions, indexes, and authored link semantics over a file corpus |
| Governance / inspectability | Symbolic and queryable, but largely service-owned and mediated through tooling | Symbolic, directly inspectable as files, diffable in git, and easier to curate manually |
| Integration surface | Proxy, MCP server, CLI commands, daemon, TUI | Repo conventions, scripts, and agent skills inside the workspace |
| Learning loop | Continuous live-session compaction and fact supersession | Slower, more manual promotion from workshop reasoning into curated artifacts |

The systems agree on the high-level problem: raw context is too expensive and too noisy to keep shoving back into the model. The main difference is what each system is trying to preserve. Virtual Context preserves conversational continuity during runtime. Commonplace preserves higher-reach methodology and design knowledge across time. Virtual Context is stronger on automatic live memory management; commonplace is stronger on inspectable authoring, explicit link semantics, and governance over what becomes durable knowledge.

Virtual Context is also a useful counterexample to the repo-first instinct in this KB. It shows that the symbolic artifact substrate can live inside a service-managed database and still remain meaningfully structured. But it also demonstrates what we give up when we move there: the memory objects are queryable and testable, yet they are not as browsable, linkable, or editorially inspectable as plain KB files.

## Borrowable Ideas

**Compress tool traces into visible stubs with explicit restore paths.** This is ready to borrow now as a general runtime principle. Virtual Context's chain-collapse approach preserves the fact that hidden material exists and gives the model a way to ask for it back. That is better than silent truncation for any agent workflow dominated by tool output.

**Defer payload rewrites when prompt-cache economics matter.** The cache-aware compaction idea is also ready to borrow now as a systems principle. Even when compaction is beneficial overall, rewriting the prompt too early can destroy byte-identical cache prefixes and erase the savings. Commonplace is not a proxy, but the underlying lesson transfers: token optimization and cache optimization are not always aligned.

**Use conversation-scoped tag vocabularies with consolidation and splitting.** This needs a use case first, but the mechanism is strong. The repo does not just assign tags; it canonicalizes aliases, splits over-broad tags, and skips already-active topics on retrieval. If commonplace ever adds live session memory or workshop-session recall, this is a better model than static tags or naive embeddings alone.

**Expose paging as explicit tools instead of pretending the first retrieval pass is enough.** This is ready to borrow now in spirit, though not necessarily in the same interface. The `expand_topic` / `find_quote` split is clean: broad topic expansion is a different operation from exact fact search. Systems get more robust when those retrieval modes are made explicit.

**Keep the engine and the integration shells separate.** This needs a use case first, but the packaging is instructive. The same engine powers the proxy, MCP server, CLI, TUI, and daemon. If commonplace grows runtime services around the KB, keeping the knowledge logic below the interface layer would preserve flexibility.

## Curiosity Pass

**"20M virtual context" is framing over selective reconstruction, not literal addressability.** The property claimed is effectively unlimited working memory. The mechanism is real but narrower: summaries, facts, active-tag filtering, and paging tools let the system reconstruct relevant slices of past context. That is useful and often enough, but it is not equivalent to actually having a 20M-token context window. The ceiling is set by the quality of tag assignment, compaction summaries, and retrieval scoring.

**Persistent memory is real here, but it is service memory rather than inspectable knowledge.** The repo genuinely stores durable symbolic outputs derived from traces: summaries, facts, fact links, aliases, checkpoints, and raw tool outputs. So this is not just "vector DB attached to a chatbot." But the simpler alternative for some use cases is still "store the transcripts and add retrieval." Virtual Context earns its complexity mainly where the system must actively manage prompt budgets and compress tool-heavy sessions, not just remember facts.

**The benchmark story is documented and scaffolded, but not independently established by this review.** The repo contains benchmark docs and a `benchmarks/` tree, so the benchmark claim is not pure marketing vapor. Still, the headline accuracy numbers remain self-reported unless we run the harnesses and inspect the datasets. The right conclusion is "benchmark infrastructure exists," not "the reported win is proven."

**VCATTACH is more interesting as conversation-pool surgery than as shared knowledge collaboration.** The claimed property is cross-platform shared memory. The mechanism mostly works by aliasing conversation IDs, loading from the same store, and invalidating/resetting session state around the target conversation. That is a real interoperability feature, but it is still service-level memory continuity, not the richer kind of collaborative knowledge production that commonplace wants from shared artifacts.

**Fact extraction with supersession is substantive, but its epistemic ceiling is bounded.** The repo does more than keyword memory: it extracts structured facts, typed relations, and supersession links. That is useful for long-session recall. But even if it works perfectly, it mostly produces adaptive memory objects, not explanatory knowledge with much reach. Virtual Context improves runtime continuity more than it improves theory-bearing knowledge.

## What to Watch

- Whether the tag-and-summary pipeline stays reliable outside benchmark-like or founder-shaped workloads, especially once topic drift and contradictions get messier than the current tests encode.
- Whether the proxy boundary remains stable as provider payload formats, prompt-cache behavior, and tool-calling schemas keep changing.
- Whether the service-owned memory objects gain stronger governance and inspection surfaces, or remain operationally powerful but editorially thin.
- Whether the benchmark claims hold up under independent reproduction rather than repo-local documentation.

---

Relevant Notes:

- [related-systems-index](../related-systems-index.md) — navigation hub for the related-systems collection
- [context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: Virtual Context is a direct systems-level response to context scarcity, with compaction and paging as its main architectural moves
- [distillation](../../notes/definitions/distillation.md) — exemplifies: segment summaries, tag summaries, and fact extraction are runtime distillations of a larger conversational trace
- [pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) — extends: tag summaries and paging tools form a query-time pointer stack over stored sessions rather than over KB notes
- [substrate class, backend, and artifact form are separate axes that get conflated](../../notes/substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md) — sharpens: Virtual Context is still in the symbolic artifact substrate even though its backend is a service-managed store rather than repo files
- [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) — contrasts: Virtual Context shows a legitimate database-backed symbolic-memory case, but also makes the browseability and governance trade-offs visible
- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: this is a live-session trace-to-symbolic-memory system, closer to service memory than to note or playbook production
- [inspectable substrate, not supervision, defeats the blackbox problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — contrasts: Virtual Context keeps symbolic artifacts, but they are inspectable mainly through tooling and schema, not directly as human-authored files
