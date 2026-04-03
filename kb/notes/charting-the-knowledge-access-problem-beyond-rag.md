---
description: Brainstorming note that decomposes the "how should an agent find what it needs?" problem into substrate, pointers, navigation, synthesis, and maintenance beyond RAG-vs-filesystem debates
type: note
traits: []
tags: [foundations]
status: seedling
---

# Charting the knowledge-access problem beyond RAG

Discussion about RAG, filesystems, databases, and graphs often treats storage or interface choice as the main question. But those are only part of the design space. The deeper problem is: how should a knowledge system be structured so a bounded agent can find, judge, combine, and trust the information needed for a task?

This is a brainstorming note, not a settled position. The goal is to chart the subproblems so comparisons stop collapsing unlike things into the same bucket.

## The parts of the problem

**Substrate** — where knowledge lives and what operations are cheap. Files make hierarchical browsing and exact reads cheap. Databases make scored queries and derived indexes cheap. Graphs make typed traversal and neighborhood operations cheap. This is the execution-substrate question, not yet the navigation strategy. [Files beat a database for agent-operated knowledge bases](./files-not-database.md) is one answer at one stage of maturity, but it does not settle how an agent decides what to load next.

**Pointers** — what the agent sees before it commits to reading. Titles, descriptions, table-of-contents entries, index blurbs, link phrases, path names, and graph edge labels are all pointers. Their job is not to answer the question directly, but to make the follow/skip decision cheap. This is the design space described by [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md).

**Navigation modes** — there are several distinct tasks usually lumped together as "retrieval":

- long jump: find a promising landing point from the whole corpus
- local traversal: move from one relevant item to nearby ones
- exact lookup: find the place containing a string, syntax, or API name
- orientation: get the shape of an area before descending
- synthesis setup: assemble the subset worth reading together

Search, hierarchy browsing, link-following, grep, and indexes support different mixes of these tasks. [Link-following and search impose different metadata requirements](./link-following-and-search-impose-different-metadata-requirements.md) names one important split, but there are probably more than two modes.

**Synthesis** — some questions are not "which page contains the answer?" but "which set of pages must be reconciled to produce the answer?" This is different from landing on the right document. Once a question requires comparison, contradiction resolution, or a whole-picture narrative, the problem becomes one of prompt assembly or pre-[distillation](./definitions/distillation.md), not just retrieval. [Evolving understanding needs re-distillation, not composition](./evolving-understanding-needs-re-distillation-not-composition.md) is one case of this broader pattern.

**Maintenance** — any navigation aid can go stale. A table of contents, index, abstract, or graph edge is valuable only while it still predicts what the target contains. This is why [stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md). The more a system depends on pointers and distillates, the more it needs maintenance loops that keep them trustworthy.

## Why the RAG framing is too narrow

"RAG" usually names one move: turn a question into a query, retrieve chunks, stuff them into context, answer. That is one routing and loading strategy. It is not the full problem.

The framing becomes misleading when it hides these differences:

- selecting one landing point vs assembling a reading plan
- retrieving chunks vs exposing structure the agent can traverse
- finding candidate pages vs preparing a synthesizable packet
- storing knowledge vs activating it in the right context

A filesystem interface can outperform naive RAG not because files are magical, but because it converts one hard global decision into many cheaper local ones: `ls` to orient, `grep` to narrow, `cat` to inspect, then continue. A graph can outperform both when typed neighborhoods matter. A database can outperform both when scoring and filtering dominate. The right comparison is task-relative, not ideology-relative.

## Distillation as navigation infrastructure

A table of contents is [distillation](./definitions/distillation.md) for the task of search. So are abstracts, descriptions, index entries, overviews, and maybe graph neighborhood summaries. They compress a larger body so the agent can decide whether to descend.

This suggests that good knowledge systems may need multiple distillates of the same source, each aimed at a different navigation or synthesis task:

- title: fastest coarse relevance check
- description: search-result discrimination
- TOC or index entry: orientation within an area
- abstract or overview: mid-resolution relevance judgment
- full text: detailed reasoning material
- synthesized narrative: whole-picture consumption when composition would exceed effective context

If this is right, then the question is not whether semantic search is enough. It is whether the system provides the right pre-compressed views for the decisions the agent must make at each step.

## Historical analogy

Libraries solved analogous problems long before computers. They did not rely on one universal access mechanism. They used catalogues, subject headings, shelf order, abstracts, bibliographies, and reference desks. The pattern seems durable: one corpus, multiple projections, each optimized for a different access task.

What seems new in agent systems is not the existence of these layers but the hard bounded-context constraint. For an LLM, bad organization is not just inconvenient. It directly competes with the task for limited reasoning budget. That makes [context engineering](./definitions/context-engineering.md) the umbrella problem and makes [distillation](./definitions/distillation.md) part of the access architecture, not just a summarization afterthought.

## Open questions

- How many distinct navigation modes are there beyond link-following and search?
- When does a question cross from retrieval into synthesis, and can that boundary be detected automatically?
- What kinds of distillates are worth maintaining by hand, and which should be generated?
- When does graph structure earn its maintenance cost over indexes plus links?
- Can a system measure whether its pointers actually improve read/skip decisions, rather than only final answer accuracy?

---

Relevant Notes:

- [context engineering](./definitions/context-engineering.md) — frames the umbrella problem as routing, loading, scoping, and maintenance under bounded context
- [distillation](./definitions/distillation.md) — treats TOCs, abstracts, and synthesized overviews as task-targeted compressions rather than generic summaries
- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — grounds the pointer-design part of the problem
- [link-following and search impose different metadata requirements](./link-following-and-search-impose-different-metadata-requirements.md) — names one navigation split this note broadens into a larger task taxonomy
- [a knowledge base should support fluid resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) — extends the navigation question from retrieval accuracy to movement between abstraction levels
- [evolving understanding needs re-distillation, not composition](./evolving-understanding-needs-re-distillation-not-composition.md) — grounds the claim that some questions are synthesis problems, not page-selection problems
- [files beat a database for agent-operated knowledge bases](./files-not-database.md) — narrows one layer of the design space to substrate choice rather than treating it as the whole architecture
