---
description: Terminal personal knowledge base that compiles raw sources into a markdown wiki, uses SQLite FTS as a derived retrieval layer, and writes lightweight session-derived digests and insight drafts
type: kb/agent-memory-systems/types/agent-memory-system-review.md
traits: [has-comparison, has-implementation, has-external-sources]
tags: []
status: outdated
last-checked: "2026-04-04"
---

# browzy.ai

> Replaced 2026-04-12. See [browzy-ai](./browzy-ai.md) for the current review.

browzy.ai is a TypeScript terminal personal knowledge base that turns raw sources into a compiled local wiki, then answers questions against that wiki. The reviewed repo combines a readable file substrate (`raw/`, `wiki/`, `drafts/`, `output/`) with a derived SQLite FTS5 index, an LLM-driven compile step, a prompt-shaped schema file, and a lightweight session-memory layer that can write digests and draft "crystallized" insights. The repo is strongest where it treats knowledge as a compiled middle layer between raw captures and question answering, and weaker where the README implies a deeper self-improving memory lifecycle than the implementation currently supports.

**Repository:** https://github.com/VihariKanukollu/browzy.ai

## Core Ideas

**The repo is files-first for artifacts, SQLite-first for retrieval mechanics.** Sources land as real files, compiled articles are real markdown, and derived insights go to `drafts/`. But the search and ranking path is not "grep over markdown." The implementation maintains a `.browzy/browzy.db` FTS index with BM25 ranking and metadata tables. This makes browzy a useful counterexample to simplistic files-versus-database debates: the readable files are the user-facing substrate, while SQLite is a rebuildable operational layer that earns its place.

**The central mechanism is raw -> compiled wiki -> retrieved sections -> answer.** `ingest/index.ts` normalizes web pages, PDFs, images, and text into raw source records. `compile/compiler.ts` then either templates very short sources directly or sends longer sources through an LLM compiler that writes wiki articles, backlinks, and index metadata. At query time, `contextBuilder.ts` does candidate search, multi-signal ranking, section extraction, token budgeting, and gap detection before `query/engine.ts` calls the answering model. The core bet is not generic chat over documents, but ahead-of-time compilation into a more navigable intermediate layer.

**`browzy.schema.md` is a real control plane.** The schema file is not decorative documentation. `schema.ts` ensures it exists, loads non-comment content, and injects it into compilation and query behavior. That makes browzy interesting as a prompt-governed KB runtime: the operator can shape what kinds of articles get written and how the assistant should interpret the knowledge base without editing code.

**Session continuity is real, but lighter than the marketing line suggests.** The repo persists session JSON, can generate a short session digest, optionally saves that digest as a `session-YYYY-MM-DD` wiki article, and can run a crystallizer that turns multi-source answers into markdown drafts under `drafts/`. That is genuine trace-derived artifact writing. But it is still a thin lifecycle: no scored maintenance, contradiction resolution for derived drafts, or robust promotion path from draft to trusted wiki article. "Every question makes your browzy smarter" is directionally true only in this weaker artifact sense.

**Gap hunting and health checks exist, but they are narrow.** The gap resolver mostly turns missing terms into a DuckDuckGo HTML query and suggests the first safe result. The linter mixes deterministic checks like broken wiki-links and missing fields with one prompt-based quality pass. Those are useful capabilities, but they are materially thinner than a full autonomous research loop or a hard-oracle quality system.

## Comparison with Our System

| Dimension | browzy.ai | Commonplace |
|---|---|---|
| Primary shape | Personal terminal PKB that compiles sources into a local wiki for Q&A | Agent-operated knowledge base centered on authored notes, links, and instructions |
| Main storage interface | Files for raw/wiki/drafts plus derived SQLite FTS index | Files in git, with only scoped operational database exceptions |
| Knowledge transformation | LLM compilation from raw sources into wiki articles | Human+agent authored notes, reviews, and instructions with explicit semantic links |
| Retrieval path | FTS candidate search -> heuristic ranking -> section extraction -> token-budgeted answer context | Search, descriptions, indexes, and explicit reading decisions across authored artifacts |
| Session-derived learning | Digest files/wiki articles plus multi-source crystallized drafts | Workshop artifacts exist, but session-to-library promotion is more manual and theory-led |
| Inspectability | Strong for files, partial for operational state hidden in SQLite/session caches | Stronger overall because more of the important state is already a checked-in artifact |
| Verification | Some deterministic checks plus prompt-shaped linting and tests for retrieval/index behavior | Deterministic note validation and review gates, but weaker automated retrieval/runtime tests |

browzy is stronger where fast personal knowledge compilation matters. It gives the user a direct path from "I have sources" to "I have an interconnected wiki plus question answering" without requiring note-writing discipline. Commonplace is stronger where knowledge needs explicit relationships, inspectable maturation, and a legible theory of why one artifact should exist at all.

The deepest architectural difference is where the structure lives. browzy commits more into the runtime: compiler prompts, retrieval heuristics, SQLite indexes, session logs, and slash-command behavior. Commonplace commits more into the artifacts: titles as claims, relationship semantics, typed note forms, and explicit library-versus-workshop distinctions.

**Trace-derived learning placement.** As an inferred projection onto the axes in [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md), browzy sits near the weak end of the live-session artifact-learning side. On axis 1, it fits the live-session side because digests and crystallized drafts are mined from interactive use. On axis 2, it is a light trace-derived artifact-learning system: the persisted outputs are session digests and draft insights, never weights, but only the wiki-saved digests clearly cross into promoted and queryable knowledge. It is worth tracking as a boundary case because the trace-derived layer is real, but the repo's center of gravity is still source compilation rather than session mining.

## Borrowable Ideas

**Use a small operational database as a derived layer, not a replacement substrate.** browzy's `wiki/` plus SQLite split is a good scoped exception to strict files-only thinking. The important pattern is rebuildable index beside readable files, not "move the KB into SQLite."

**Assemble answer context from relevant sections, not whole documents.** `contextBuilder.ts` does a concrete and useful thing: retrieve candidates symbolically, then clip to relevant sections before paying the final prompt cost. That is ready to borrow anywhere context budgets matter.

**Give the runtime a prompt-shaped schema file.** `browzy.schema.md` is a compact control-plane move. It keeps domain adaptation in an editable artifact rather than scattering it through code and prompts. This is ready to borrow where a subsystem needs operator-tunable doctrine.

**Write mined insights to drafts before promoting them.** The crystallizer's choice to write into `drafts/` instead of directly mutating the trusted wiki is stronger than the README makes it sound. It is a workshop-layer pattern: generated insight first, curation later. That is ready to borrow now.

**Treat retrieval quality as something worth testing directly.** The repo's end-to-end tests for FTS behavior, stemming, schema migration, and query caching are a useful reminder that knowledge systems need runtime-behavior tests, not only artifact validation. This is ready to borrow when a subsystem's retrieval path becomes stable enough to test.

## Curiosity Pass

**The most important idea in browzy is compiled middle-layer knowledge, not ambient chat memory.** The implementation earns the claim that raw sources become a more navigable representation before query time. That is a real transformation. The stronger "your browzy keeps learning from every question" framing is secondary and currently much thinner.

**The storage design is better understood as files plus a derived database, not files versus database.** The repo shows why that distinction matters. Human-inspectable artifacts stay in markdown, but the operational access pattern for search is delegated to SQLite. This is close to the shape our own repo keeps rediscovering in narrower domains.

**The session-memory layer looks more like a workshop than a library.** Session digests and crystallized drafts are durable, but they are not yet fully curated knowledge. They are temporal byproducts that may later deserve promotion. That makes browzy's "memory" loop conceptually closer to our workshop-layer notes than to our mature-note layer.

**Several ambitious features reduce to prompt-shaped heuristics.** Gap discovery, contradiction handling, concept extraction, and health checks all exist in code, but often as thin prompt or heuristic wrappers rather than stronger maintained subsystems. That does not make them fake. It does mean the repo should be read as a promising product-shaped runtime with a few solid mechanisms, not as a fully autonomous knowledge curator.

## What to Watch

- Whether crystallized drafts gain a real review, promotion, or retirement lifecycle instead of remaining a sidecar draft directory
- Whether `browzy.schema.md` stays prompt doctrine or grows stronger deterministic structure around article classes and compile behavior
- Whether the linter and contradiction handling become stronger than prompt-mediated advisory checks
- Whether gap hunting grows beyond "first safe search result" into a more deliberate source-discovery loop
- Whether the compiled wiki remains high quality as the corpus grows, or whether prompt-only article maintenance starts to drift

---

Relevant Notes:

- [Files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) — complicates: browzy is a good example of readable files as source artifacts with SQLite as a justified derived index
- [Agents navigate by deciding what to read next](../../notes/agents-navigate-by-deciding-what-to-read-next.md) — exemplifies: browzy's ranking and section extraction are a runtime implementation of the "what should I read next?" problem
- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — sharpens: browzy's digests and crystallized drafts behave more like workshop artifacts than mature library notes
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) — frames: browzy's session digests are the clearest deploy-time artifact-learning case here, while crystallized drafts are a weaker pre-promotion variant
- [Pal](./pal.md) — compares: both combine a compiled wiki with session-derived continuity artifacts, but PAL has a broader live-tool control plane and a sharper split between routing and learned behavior
- [Siftly](./siftly.md) — compares: both use SQLite-backed operational stages around source ingestion, but browzy pushes further into compiled wiki synthesis and interactive query-time context assembly
- [OpenViking](./openviking.md) — contrasts: both offer durable agent memory with session continuity, but OpenViking makes service-owned memory extraction central while browzy keeps the center of gravity on a local compiled wiki
