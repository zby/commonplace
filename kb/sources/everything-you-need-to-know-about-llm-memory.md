---
source: https://rosebudjournal.notion.site/Everything-you-need-to-know-about-LLM-memory-33b328e8e3f780858d3df3acb06d23b9
description: Notion essay arguing that LLM memory needs retrieval, salience, summarization, forgetting, and memory objects rather than raw chat logs.
captured: 2026-04-13
capture: notion-api
type: kb/sources/types/snapshot.md
tags: [web-page]
---

# Everything you need to know about LLM memory

Author: Unknown
Source: https://rosebudjournal.notion.site/Everything-you-need-to-know-about-LLM-memory-33b328e8e3f780858d3df3acb06d23b9
Date: Not visible; Notion created time 2026-04-07

Despite what you see, memory for conversational LLMs remains an unsolved problem.

The dream is: the model remembers what you said before and draws meaning across it over time. Not just recall, but interpretation, narrative, the kind of memory that makes a conversation feel continuous and cumulative across months or years.

Today, you can achieve an illusion of this dream. For days, or weeks if you're lucky. Until the illusion breaks when the LLM starts forgetting.

### Why does this happen?

As your conversation history grows, the memory system must decide what to capture, how to represent it, and what to surface on any given conversation turn. Every one of those decisions is lossy, opinionated, and non-deterministic.

Over time, either the corpus of information becomes too large to reliably search, or what the system remembers starts to drift from what was actually said due to repeated summarization. The model forgets because the system either can't hold a complete picture, or the picture becomes distorted.

### So how do we solve for this?

In an ideal world, the LLM would have perfect historic context on the conversation turns that matter. Infinite attention across every word you've ever exchanged, with none of the cost or latency that would actually entail.

Since that's not possible, every memory system is an attempt to approximate it. Each with its own drawbacks.

There are ultimately only two ways to preserve information from a conversation:

1. **Raw** — original messages, stored verbatim

1. **Derived** — summaries, narratives, structured extractions

Every memory system is choosing a position on this spectrum. And neither extreme works.

Raw is lossless but inert. A pile of transcripts isn't understanding. The information is all there, but nothing is connected, prioritized, or interpreted. It's just buried in the source material.

Derived is compact and usable, but repeated derivation drifts from the source the way a photocopy of a photocopy degrades. You don't lose the information all at once. You lose it gradually, and can't tell exactly when it stopped being accurate.

### Won't infinite context solve this?

This is the most natural objection. Context windows keep getting bigger. Won't they eventually get big enough that we can just skip the memory system entirely and feed in the full history?

Not anytime soon. For two reasons:

1. **Cost.** Even if you could fit two years of conversation history into a context window, you'd be paying to process all of it on every single turn. The economics are brutal and they scale linearly with history. No consumer product survives that margin structure.

1. **Degradation.** Models get worse as the context window fills. Attention drops on information in the middle, overall reasoning quality declines, instruction following gets sloppier. You're paying more for worse performance.

Infinite context is just the extreme version of the raw path. And we've already established why raw alone doesn't work.

### The evaluation paradox

To know if a memory system is working, you need ground truth. But for real conversational memory spanning months or years, the ground truth is the entire history, which is larger than any context window and larger than any human can reasonably annotate.

Benchmarks like LongMem can test needle-in-haystack retrieval, but retrieval isn't memory. Memory is what happens when facts change, when old context gets superseded, when the significance of a conversation only becomes clear weeks later. The right answer depends on the full arc of the relationship, and the arc is always in motion. No benchmark captures arcs.

Synthetic datasets can't replicate these real-world examples at scale. The conversations lose coherence long before they reach realistic length, and even if they didn't, nobody can confirm ground truth for a synthetic relationship that evolved across a million tokens.

That's why every new memory approach you see land is a different set of trade-offs dressed up as a solution. Nobody can actually prove theirs works, because any judge you'd use to evaluate the full history has the same context limitations as the system it's judging.

### Where this leaves us

The dream from the top of this piece, a model that remembers what you said and draws meaning across it over time, requires solving both sides of the raw/derived tradeoff simultaneously. Perfect preservation and perfect interpretation. Every current approach sacrifices one for the other.

This isn't a criticism of the people building these systems, it's an honest description of the constraint they're working within. Compression is lossy. Retrieval is imperfect. And the thing we actually want, meaning that accumulates and evolves, might be the hardest thing to formalize in a system that runs on pattern matching over tokens.

Memory for LLMs remains unsolved not because nobody's tried hard enough, but because the problem is very, very hard to solve.

We're getting closer. But we're not there.

---

## How memory systems are built

> "There are no solutions. There are only trade-offs." — Thomas Sowell

Every memory system is a composition of choices across a set of axes. Different products pick different paths, but the axes themselves are stable. When a new memory solution lands, you can lay it on this map and see exactly which choices it made and which ones it's punting on.

### What gets stored

Memory systems hold onto either raw material, derived material, or some mix.

**Raw:**

| Type | Description |
| --- | --- |
| Session logs | Full transcripts of each conversation session |
| User/assistant message pairs | Individual exchanges preserved in their original sequence |
| Tool call traces | Records of tool invocations, inputs, and outputs during a session |
| Attachments | Files, images, or other artifacts shared during conversation |

**Derived:**

| Type | Description |
| --- | --- |
| Session summaries | Condensed recaps of individual conversations, capturing key points and outcomes |
| Daily / weekly / monthly rollups | Periodic aggregations that compress multiple sessions into a single narrative at different time scales |
| Topic fan-out summaries | One evolving summary per topic the user discusses |
| Metadata | Topic labels, sentiment, entities mentioned, importance scores |
| Graph data | Nodes for entities, edges for relationships |
| Embeddings | Vector representation of raw or derived material |
| Cross-session inferences | Conclusions drawn across multiple sessions that weren't said in any single one |
| Self-directed prompts | Instructional text the system writes for its own future consumption, like "always remember the user prefers concise answers" |

This is not an exhaustive list - there can be infinite types of derivations, but there are just some common ones.

### When derivation happens

Derived artifacts have to be produced somewhere, and the timing is its own design decision.

| Timing | Description |
| --- | --- |
| Synchronous, at conversation time | Runs before or after the model responds. |
| Asynchronous, in background processes | Nightly auto-dreams, periodic summarization, drift correction passes. |
| On-demand, at retrieval time | Nothing is derived ahead of time. Summaries and rollups are generated when they're needed. |

Most production systems are a mix. Fast derivations run synchronously, expensive ones run in the background, and a few specialized rollups happen on demand.

### What triggers a write

Every memory system has to decide when to capture something at all.

| Trigger | Description |
| --- | --- |
| Write everything by default | Store all raw turns, derive summaries of everything. Simple, expensive, eventually unwieldy. |
| Heuristic triggers | Store when a length threshold is hit, when sentiment shifts, when a new entity appears, when a session ends. |
| LLM-as-curator | Ask a model whether the current turn is worth remembering. Cheap to set up, terrible at predicting what'll matter later. |
| User-triggered | Only store when the user explicitly marks something. Accurate but requires user effort. |

Write-triggering is upstream of everything else. If you write the wrong things, no amount of clever retrieval will save you.

### Where it gets stored

The storage backend constrains everything downstream.

| Backend | Description |
| --- | --- |
| Filesystem (a la OpenClaw) | Files, folders, markdown pages, optionally with frontmatter or links |
| SQL DB | Structured rows with typed columns |
| NoSQL / document DB | Schema-flexible documents (Mongo, Firestore, DynamoDB). Not great as a primary retrieval surface, but useful for storing derived structured artifacts that get indexed elsewhere. |
| Vector DB | Embeddings indexed for similarity search (Pinecone, Weaviate, Qdrant, pgvector) |
| Graph DB | Nodes and edges (Neo4j, Dgraph, Kuzu) |

Most real systems use more than one. A common pattern is filesystem or document DB for the source of truth, vector DB for retrieval, and sometimes a graph DB on top for relationship traversal.

### How it gets retrieved

Storage backend constrains retrieval strategy.

| Backend | Retrieval strategies |
| --- | --- |
| Vector DB | Semantic similarity, hybrid (vector + BM25), filtered similarity |
| SQL DB | Full-text search, structured queries, joins |
| NoSQL DB | Key lookup, field queries, occasional full-text |
| Filesystem | Filename match, grep, glob, model-driven navigation |
| Graph DB | Node lookup, traversal, multi-hop queries |

Each strategy has a characteristic strength. Semantic search is good at "find me things conceptually like this." Full-text is good at exact phrases and proper nouns. Graph traversal is good at "what does the system know about this entity and everything connected to it." Filesystem navigation is good when the model is expected to actively explore.

### Post-retrieval processing

Once you have candidates, you usually want to narrow further.

| Method | Description |
| --- | --- |
| Vector DB re-rankers | Use a more expensive model to re-score the top-k from a cheap initial retrieval |
| LLM-based narrowing | Pass candidates through a cheap LLM with a prompt like "which of these are relevant to the current turn?" |
| Filtering by metadata | Drop candidates outside a date range, topic, or other tag |
| Deduplication | Collapse candidates that say similar things |
| Token-budget trimming | Drop or summarize candidates to fit within a context budget |

Post-processing is where a lot of the perceived quality of a memory system actually comes from. Cheap retrieval plus smart re-ranking often beats expensive retrieval alone.

### When retrieval happens

Three modes.

| Mode | Description |
| --- | --- |
| Always injected | The payload is in context every turn. Either fixed (user profile, name, timezone) or recomputed each turn (always run a retrieval pass and inject the top-k regardless of what the user said). |
| Hook-driven | Retrieval runs in the harness between turns, before the model sees the message. The harness decides what to fetch based on the incoming turn, and the model receives whatever the harness loaded. |
| Tool-driven | The model decides whether and when to fetch. It sees the turn first, then chooses to call a search tool or read a file if it wants more context. |

These have very different failure modes. Always-injected pollutes context with irrelevant history. Hook-driven covers passive awareness but is expensive and can make the model perform memory rather than have it. Tool-driven respects the model's judgment but the model doesn't know what it doesn't know, so it often fails to fetch when it should.

### Who or what is doing the curating

At every decision point in a memory system, something is making a choice. Who or what is it?

| Curator | Description |
| --- | --- |
| The harness | Deterministic code, heuristics, scheduled jobs |
| A cheap model | A small LLM running in the pipeline for cheap classification, narrowing, or routing |
| The main model | The same LLM that's serving the user, making decisions via tool calls |
| A background process | A separate LLM (often a stronger model) running offline for derivation and housekeeping |
| The user | Explicit marking, editing, deleting |

Worth tracking as its own dimension because the cost, quality, and accountability profile of each curator is different. Systems that put the main model in charge of curation pay for quality on every turn. Systems that put cheap models in charge pay less but get sloppier decisions. Systems that lean on the user are accurate but require effort the user usually won't give.

### Forgetting

Every memory system has a forgetting policy, whether or not the designer chose one. The question isn't whether to forget, it's how.

**What gets forgotten:**

| Strategy | Description |
| --- | --- |
| Nothing (append-only) | Contradictions accumulate, the system gets stuck on who the user used to be |
| Old versions when superseded (overwrite) | Clean but loses history |
| Low-importance items (decay) | Gradual, weighted by some signal of relevance or recency |
| Explicitly marked items (user-triggered deletion) | Accurate but requires user effort |
| Entire time windows or topics (bulk forgetting) | "Forget everything from before March" or "forget everything about my old job" |

**How forgetting propagates:** Forgetting in a memory system isn't a single delete operation. If you stored raw turns and derived summaries from them, deleting the raw turns doesn't delete the summaries. If you extracted facts into a graph, deleting the source conversation leaves the facts orphaned. Real forgetting requires either tracking provenance (so you can cascade deletes) or periodically re-deriving everything from a smaller raw corpus, which is expensive.

Most systems get this wrong. They delete the obvious thing (the raw turn) and leave the derived artifacts, which means the user's request to be forgotten is only partially honored, and often not in the places that matter most.

**When forgetting happens:**

| Timing | Description |
| --- | --- |
| Never | The system retains everything indefinitely, no matter how old or irrelevant |
| On user request | Deletion only happens when the user explicitly asks for it |
| On a schedule | Drop anything older than X |
| Continuously, via decay | Items lose weight over time and are gradually pruned as they fall below a relevance threshold |
| Triggered by contradiction detection | When new information conflicts with old |

Forgetting is structurally hard for the same reason the rest of memory is: you don't know at write time what'll matter later, and you don't know at delete time what'll matter later either. Forgetting too aggressively means losing context the user wanted preserved. Forgetting too conservatively means accumulating an inaccurate model of the user that gets harder to correct over time. There's no right setting, only trade-offs.

And like the rest of memory, forgetting is hard to evaluate. How do you know if a system forgot the right things? The ground truth would be "what did the user actually want forgotten," which isn't recorded anywhere and changes over time.

### Comparing existing approaches

A memory system is a path through this map. You make a choice on each axis, and the choices interact. Some examples of how existing systems compose:

|  | OpenClaw | ChatGPT's first memory | Rosebud V1 | Zep / graph-based | QMD (OpenClaw hybrid) | Lossless Claw | Claude Code (3-layer) | MemPalace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| What | Derived (LLM-written pages) | Derived (extracted facts) | Raw (every message)<br>Derived (entry summaries) | Derived (entities + relationships) + raw fallback | Raw (markdown files on disk), indexed for hybrid retrieval | Derived (compacted turns with pointers to raw originals) | Derived (domain-specific markdown files) + static project config ([CLAUDE.md](http://CLAUDE.md)) | Raw (verbatim in "drawers") + derived (AAAK lossless shorthand in "closets") + knowledge graph (temporal entity triples) |
| When derived | Synchronous + occasional async cleanup | Synchronous | On entry save | Synchronous + async refinement | Synchronous (BM25 + embedding at index time) | Synchronous (compaction fires when context window fills) | Synchronous (agent writes during session) + async (AutoDream consolidation between sessions) | Batch (mine command ingests conversations/projects) + synchronous (MCP tool writes during session) |
| Write trigger | LLM-as-curator, every meaningful turn | LLM-as-curator | Write everything | Heuristic + LLM-as-curator | LLM-as-curator (same file writes as OpenClaw) | Heuristic (context window pressure triggers compaction) | LLM-as-curator (agent decides when to update memory files) | User-triggered (batch mining) + LLM-as-curator (MCP adds during session) |
| Curator | Main model | Cheap model for extraction, main model for use | Harness | Cheap model for extraction, main model for use | Main model (queries via MCP tools) | Harness (compaction) + main model (decides when to expand) | Main model (self-healing — rewrites its own files when outdated) | Harness (mining pipeline) + main model (MCP tools for live adds) |
| Where | Filesystem<br>SQLite vector | Structured store (probably SQL or document) | Pinecone (messages)<br>Firestore (summaries) | Graph DB + vector DB | Filesystem + local hybrid index (BM25 + vector) | Filesystem (raw transcripts preserved on disk, compacted summaries in context) | Filesystem ([memory.md](http://memory.md) pointer index + domain files + [CLAUDE.md](http://CLAUDE.md) static config) | Filesystem (palace: wings/rooms/closets/drawers) + ChromaDB (vectors) + SQLite (knowledge graph) |
| When retrieved | Tool-driven | Always injected | Hook-driven | Hook-driven | Tool-driven (MCP interface) | Always injected (compacted) + tool-driven (expand to raw) | Always injected ([CLAUDE.md](http://CLAUDE.md)) + tool-driven ([memory.md](http://memory.md) → domain files) | Always injected (L0+L1 wake-up, ~170 AAAK tokens) + tool-driven (L2/L3 search on demand) |
| How retrieved | Filename + grep + model-driven exploration | Full payload always loaded | Semantic similarity (msgs)<br>Injected recent summaries | Graph traversal + semantic similarity | Hybrid (BM25 + semantic similarity + reranking) | Compacted summaries in context; model expands to raw via tool call | Read pointer index → load specific domain file. No semantic search. | Structural navigation (wing → hall → room narrows 34%) + semantic similarity within scope |
| Post-retrieval | None | None | Top-k filtering, llm-filtering | Graph-aware re-ranking | Cross-encoder reranking | On-demand expansion of pointers to full raw content | None (pointer structure replaces search) | Contradiction detection against knowledge graph |
| Forgetting | Append-only with occasional manual overwrites | Append-only with user-triggered deletion | Append-only, never forgets | Append-only with entity merging | MCP-driven pruning (agent can delete stale entries and reindex) | Lossless — raw is never deleted, only compacted out of active context | Self-healing overwrites + AutoDream (async prune/merge/refresh cycle between sessions) | Knowledge graph invalidation (temporal validity windows — facts have start/end dates) |

Every system on the market is a path through this map. The value of having the map is that it lets you ask precise questions about a new system instead of generic ones. Not "does this solve memory" but "what does this store, how does it derive, when does it write, where does it live, how does it retrieve, what does it forget, and who's making each of those decisions."

### What this map is and isn't

This is a map of mechanisms, not a map of quality. It tells you what choices a memory system can make, but it doesn't tell you which choices are good. Good choices depend on the product, the user, the budget, and the failure modes you can tolerate. The map is the design space, not the answer.

The axes aren't fully orthogonal. Some choices constrain others. Picking a graph DB forces certain retrieval strategies. Picking "write everything" forces you to think about forgetting. The map is more accurately a partially-ordered set of decisions than a free composition. But treating the axes as independent is useful for surveying the design space, even if the final design has to respect the dependencies.

### Common failure modes

Every memory system fails. The question is how, and whether the failure is recoverable. These are the patterns that show up most often in practice.

| Failure mode | What happens | Example |
| --- | --- | --- |
| Session amnesia | New session starts with no awareness of previous ones. The user is back to zero every time. | You explained your entire project context yesterday. Today the model asks "what are you working on?" |
| Entity confusion | The model misidentifies or merges distinct entities during derivation. Two people with the same name become one, or categories bleed into each other. | You mention your daughter and your dog in separate sessions. The system encodes "user has a child named Luna" when Luna is the dog. |
| Over-inference | The model jumps to conclusions and encodes exaggerated or incorrect interpretations as facts. Without careful prompting, it fills gaps with plausible-sounding fabrications. | You mention feeling tired once. The system encodes "user struggles with chronic fatigue" and references it in future sessions. |
| Derivation drift | Chained summarizations compound small errors. Each derivation is slightly lossy, and the losses accumulate. After enough rounds, the derived memory diverges from what was actually said. | "I'm considering a career change" becomes "user is unhappy at work" becomes "user has a history of job dissatisfaction." |
| Retrieval misfire | The system surfaces semantically similar but contextually wrong memories. Embeddings are close, but the meaning is different. | You mention "anxiety about the product launch" and the system retrieves a memory about "anxiety about flying" because both score high on the anxiety vector. |
| Stale context dominance | Old, heavily-referenced memories crowd out recent ones. The system keeps surfacing outdated context because it was discussed more frequently. | You moved on from a project three months ago. The system keeps bringing it up because it's the densest cluster in the memory space. |
| Selective retrieval bias | Retrieval only finds what matches the current query's framing. Relevant memories stored under a different topic or emotional register are invisible. | You ask about work and the system pulls work memories. The insight you need is in a personal conversation from last week that happens to be relevant, but retrieval never crosses that boundary. |
| Compaction information loss | When summaries replace raw turns, specific details vanish. The compression is lossy in ways that destroy the most useful information. | "My daughter's recital is on March 15th" gets compressed to "user has a daughter involved in activities." The date, the specificity, the actionable detail, all gone. |
| Confidence without provenance | The system states a "memory" with full confidence but there's no way to trace it back to what was actually said. The user can't tell if this was stated, inferred, or hallucinated. | The model says "as you've mentioned, you prefer direct feedback." You never said this. It inferred it, encoded it, and now treats it as ground truth. |
| Memory-induced bias | The system's responses are always colored by what it already knows about you. Sometimes that helps. But sometimes you want an uncolored take. | You've journaled about stress at work for weeks. When you mention a new job opportunity, the system assumes you want to leave, rather then remaining curious. |

### Notes

This doc is a work-in-progress, there are some things it doesn’t cover which are interesting:

1. Skills - a form of procedural memory for repeatable workflows

1. Evaluation techniques - working around the eval paradox

1. Additional landscape examples (Claude Code, Hermes Agent, etc)
