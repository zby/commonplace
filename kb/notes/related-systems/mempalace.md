---
description: Local-first memory system that stores verbatim project and conversation chunks in ChromaDB, adds a sidecar SQLite fact graph, and layers optional AAAK compression and MCP tooling on top
type: related-system
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: 2026-04-07
---

# MemPalace

MemPalace is a Python memory system by `milla-jovovich` that mines project files and conversation exports into a local "palace" backed by ChromaDB, then exposes that memory through a CLI, an MCP server, a small [context engineering](../definitions/context-engineering.md) (the work of getting the right knowledge into a bounded context) stack, and an optional SQLite knowledge graph. The repo's core implementation is strongest where it keeps the claim narrow: store verbatim text locally, attach a spatial taxonomy, and retrieve it with semantic search. It is weaker where the README presents AAAK compression, contradiction checking, and palace metaphors as deeper transformation mechanisms than the current code actually implements.

**Repository:** https://github.com/milla-jovovich/mempalace

## Core Ideas

**The real substrate is verbatim ChromaDB drawers, not extracted memories.** `miner.py` and `convo_miner.py` chunk files or transcript exchanges into short verbatim documents and store them in a persistent Chroma collection with `wing`, `room`, `source_file`, and timestamp metadata. The default search path in `searcher.py` queries those raw drawers directly and returns the original text, not a synthesized memory object.

**The palace structure is a retrieval prior implemented mostly as metadata filters.** The "wing" and "room" model is real in code: mining assigns those labels, search can filter on them, and `palace_graph.py` can infer cross-wing "tunnels" when the same room name appears in multiple wings. But the richer README language around halls and spatial navigation mostly exceeds the implementation. Outside diary entries, mining does not appear to populate `hall` metadata, so the strongest implemented effect is scoped filtering plus graphing repeated room names.

**AAAK is an auxiliary compression and protocol layer, not the default memory substrate.** `dialect.py` can compress text into a compact symbolic format and `cli.py` exposes that through `mempalace compress`, storing results in a separate `mempalace_compressed` collection. The MCP server also ships an AAAK spec and asks agents to write diary entries in that style. But the default wake-up path in `layers.py` still renders identity text plus truncated top drawers, and the default search path still reads raw drawer text. AAAK is real, but it is optional and sidecar in the current repo.

**Mutable facts live in a separate local temporal graph.** `knowledge_graph.py` implements a SQLite store for entity triples with validity windows and invalidation, and the MCP server exposes direct tools for querying and mutating that graph. This is a genuine second substrate: Chroma stores the verbatim evidence, while SQLite stores operator-supplied or tool-supplied facts about entities over time.

**The main integration surface is operational guidance through MCP, not autonomous knowledge maintenance.** `mcp_server.py` exposes nineteen tools for search, taxonomy, graph queries, graph writes, and agent diaries, plus a "Palace Protocol" that tells the model when to query memory before speaking. That is a useful control-plane move. But it is still instruction plus tools, not a strong automated learning loop. Diaries are append-only entries in the same Chroma collection, and the "general" conversation mode is heuristic classification into five memory types rather than durable curation or [distillation](../definitions/distillation.md) (directed context compression) into a maintained knowledge layer.

## Comparison with Our System

| Dimension | MemPalace | Commonplace |
|---|---|---|
| Primary substrate | ChromaDB documents plus SQLite fact graph | Markdown notes, links, instructions, and workshop artifacts in git |
| Main unit | Drawer chunks with `wing` and `room` metadata | Notes and instructions with explicit semantic links |
| Retrieval model | Semantic search over stored chunks, optionally filtered by palace structure | Search-first reading decisions over authored artifacts, descriptions, and curated indexes |
| Knowledge transformation | Minimal by default: store verbatim, optionally compress or classify | Stronger artifact shaping: write, connect, validate, review, and mature |
| Mutable facts | Separate temporal KG with explicit invalidation | Usually stay in notes unless a narrower operational store is justified |
| Agent surface | MCP tools plus protocol guidance and diary writes | Instructions, skills, notes, and validation/review gates |
| Learning from traces | Stores conversations directly; can heuristically classify and append diary entries | Workshop layer exists, but trace-to-library promotion is more deliberate and explicit |

MemPalace is stronger where the problem is "make the full conversational corpus locally searchable for an assistant right now." It offers a direct path from raw exports to retrievable evidence with little authoring overhead. Commonplace is stronger where the problem is "turn experience into inspectable, composable knowledge with clear semantics and maintenance discipline."

The deepest architectural divergence is where the structure lives. MemPalace puts more structure into runtime behavior: metadata filters, retrieval collections, MCP protocol, optional compression, and a fact sidecar. Commonplace puts more structure into the artifacts themselves: claim titles, descriptions, link semantics, note types, and the split between workshop and library.

**Trace-derived learning placement.** MemPalace belongs near the weak-to-middle end of the live-session artifact side of [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md). It clearly turns conversations and agent interactions into durable local artifacts: verbatim drawers, heuristic memory-type drawers in `general` mode, and append-only agent diaries. It can also hold temporal KG facts, but that path currently depends on explicit graph writes rather than an inspected automatic mining loop. It does not yet show a strong maintenance loop that revises, retires, or synthesizes those artifacts beyond storage, filtering, and optional compression.

## Borrowable Ideas

**Use lightweight structural priors to narrow retrieval before deeper reading.** Ready now. The `wing` and `room` filters are a practical reminder that even coarse spatial tags can materially reduce search scope before the expensive part of reasoning begins. In our system, this would look like stronger operational filters over workshop artifacts or source collections before loading full notes.

**Keep mutable fact state in a narrow sidecar instead of overloading the main corpus.** Needs a use case first. The SQLite temporal graph is a sensible separation for facts that truly need invalidation windows and direct query operations. If we add a similar layer, it should stay narrow and rebuildable, not absorb the library.

**Expose the memory protocol as part of the interface, not hidden in prompts.** Ready now. MemPalace makes the agent contract explicit: query before asserting, invalidate facts when they change, write a diary after sessions. That is stronger than burying usage expectations in a system prompt and would transfer well to any tool-backed subsystem we want agents to use consistently.

**Benchmark the honest baseline separately from the enhanced path.** Ready now. The repo distinguishes "raw local retrieval" from optional reranked benchmark modes instead of collapsing them into one marketing number. We should keep the same discipline whenever we compare simple artifact-first baselines against more assisted variants.

## Curiosity Pass

The strongest thing in this repo is narrower than the README's grand framing: "store everything, then make it findable" is real. The implementation repeatedly comes back to verbatim storage, cheap metadata structure, and local semantic retrieval. That is enough to make MemPalace interesting.

The palace metaphor is only partly mechanized. Wings and rooms are implemented, and repeated room names can form useful cross-wing tunnels. But halls are mostly vocabulary, not populated first-class routing data, so some of the spatial richness is naming rather than mechanism.

AAAK is the clearest naming-versus-mechanism tension. The repo calls it "lossless" compression, but `Dialect.compress()` extracts entities, topic words, one key sentence, emotion signals, and flags into a compact summary string. That representation is not invertible. The system only stays lossless because the original drawer remains elsewhere in Chroma. So AAAK currently behaves more like a derived shorthand or [constraining](../constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) move than a lossless compiled memory substrate.

The contradiction-checking story shows the same pattern. The repo does contain a real temporal KG with invalidation, but I did not find an automated contradiction-checker that emits the README's example warnings. The current mechanism is closer to "tools exist so an agent can check or maintain facts" than to "the system automatically catches mistakes before they reach you."

That does not make the project weak. It just sharpens what it actually contributes: a strong local baseline for memory retrieval, an explicit operational protocol for using it, and a useful example of how far simple storage-first design can go before heavier knowledge-maintenance machinery is warranted.

## What to Watch

- Whether future mining passes start populating hall metadata and automatic graph facts, which would turn more of the palace vocabulary into real mechanism
- Whether AAAK becomes the default closet representation rather than a separate optional compression path and diary convention
- Whether the knowledge graph gains automated extraction or validation instead of relying on direct tool writes and manual invalidation
- Whether the diary and `general` extraction paths grow a real promotion, revision, or retirement lifecycle instead of remaining append-only trace storage
- Whether the benchmark story stays clean as reranking and hybrid heuristics become a larger share of the top-line numbers

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: MemPalace is a useful live-session artifact-learning boundary case where traces become durable local memory without a strong revision loop
- [files-not-database](../files-not-database.md) — contrasts: MemPalace is a good example of what a local operational database buys when retrieval, not authored semantics, is the center of gravity
- [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — sharpens: its diaries and heuristic memory extractions behave more like workshop artifacts than mature library knowledge
- [browzy.ai](./browzy-ai.md) — compares: both systems keep durable local artifacts plus a derived retrieval layer, but MemPalace stays storage-first while browzy.ai is built around compilation into a wiki
- [OpenViking](./openviking.md) — compares: both use tiered loading and retrieval scoping, but MemPalace keeps the substrate local and simple while OpenViking pushes more logic into a service-owned context database
