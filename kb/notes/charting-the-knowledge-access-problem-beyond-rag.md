---
description: Brainstorming note that decomposes the "how should an agent find what it needs?" problem into storage substrate, pointers, navigation, synthesis, and maintenance beyond RAG-vs-filesystem debates
type: kb/types/note.md
traits: []
tags: [foundations]
status: seedling
---

# Charting the knowledge-access problem beyond RAG

Discussion about RAG, filesystems, databases, and graphs often treats storage or interface choice as the main question. But those are only part of the design space. The deeper problem is: how should a knowledge system be structured so a bounded agent can find, judge, combine, and trust the information needed for a task?

This is a brainstorming note, not a settled position. The goal is to chart the subproblems so comparisons stop collapsing unlike things into the same bucket.

## What success should be measured against

The goal is not retrieval accuracy in isolation. A knowledge system for an agent should improve [contextual competence through discoverable, composable, trusted remembered knowledge](./agent-memory-needs-discoverable-composable-trusted-knowledge-under.md): not just answering a question, but helping the agent classify, plan, explain, and act appropriately under bounded context.

That widens the evaluation target. An access strategy might be good at exact lookup but poor at orientation. Good at landing on a page but poor at surfacing contradictions. Good at retrieving chunks but poor at helping the agent compose them into an argument. Once the target is contextual competence rather than search accuracy, "best retrieval system" stops being a single-axis question.

## The parts of the problem

**Storage substrate** — where knowledge lives and what operations are cheap. Files make hierarchical browsing and exact reads cheap. Databases make scored queries and derived indexes cheap. Graphs make typed traversal and neighborhood operations cheap. This is the [storage-substrate](./definitions/storage-substrate.md) question, not yet the navigation strategy. [Files beat a database for agent-operated knowledge bases](./files-not-database.md) is one answer at one stage of maturity, but it does not settle how an agent decides what to load next.

**Pointers** — what the agent sees before it commits to reading. Titles, descriptions, table-of-contents entries, index blurbs, link phrases, path names, and graph edge labels are all pointers. Their job is not to answer the question directly, but to make the follow/skip decision cheap. This is the design space described by [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md).

**Navigation modes** — there are several distinct tasks usually lumped together as "retrieval":

- long jump: find a promising landing point from the whole corpus
- local traversal: move from one relevant item to nearby ones
- exact lookup: find the place containing a string, syntax, or API name
- orientation: get the shape of an area before descending
- synthesis setup: assemble the subset worth reading together

Search, hierarchy browsing, link-following, grep, and indexes support different mixes of these tasks. [Link-following and search impose different metadata requirements](./link-following-and-search-impose-different-metadata-requirements.md) names one important split, but there are probably more than two modes.

These modes also consume context differently. A representation that works well for exact lookup may work poorly for synthesis setup because [effective context is task-relative and complexity-relative, not a fixed model constant](./effective-context-is-task-relative-and-complexity-relative-not-a.md). The same token count can be easy for one task shape and unusable for another.

**Transformation burden** — queries also differ in how much work remains after the relevant inputs have been found. This seems independent from navigation mode. Some questions are mostly lookup: "Who is the HR head?" Some are derivation or aggregation: "What were last year's expenses?" if the answer requires selecting records and summing them. Some are synthesis: "Why did expenses increase?" Some are conjectural or creative: "How should we reorganize HR next year?"

This suggests a second axis alongside access difficulty:

- access burden: how hard is it to find the right inputs?
- transformation burden: how hard is it to turn those inputs into the requested output?

That distinction matters because "creating new information" covers several different operations. A derived answer may be new in the sense that it was not stored verbatim, but it is mechanically implied by existing data. That is different from open-ended synthesis or conjecture.

**Symbolic vs semantic post-processing** — one important split inside transformation burden is whether the work after retrieval can be done symbolically or requires semantic judgment. Summing last year's expenses is a symbolic operation over selected records. Explaining why expenses increased requires semantic processing over the records and their context. A common architecture is therefore symbolic search or filtering first, then semantic processing over the retrieved material. Plain RAG is one version of this. Agentic RAG is a stronger version where the LLM also helps decide which symbolic searches to run next.

This symbolic/semantic split is not incidental. It is close to the KB's central architectural move: keep bookkeeping, filtering, aggregation, and orchestration symbolic where possible, and reserve LLM calls for semantic judgment. [Bounded-context orchestration model](./bounded-context-orchestration-model.md) states this explicitly as symbolic steps outside context and bounded agent calls for semantic work. On that framing, some queries should stay mostly symbolic end-to-end, while others need a symbolic retrieval stage that prepares inputs for a semantic call.

**Synthesis** — some questions are not "which page contains the answer?" but "which set of pages must be reconciled to produce the answer?" This is different from landing on the right document. Once a question requires comparison, contradiction resolution, or a whole-picture narrative, the problem becomes one of prompt assembly or pre-[distillation](./definitions/distillation.md), not just retrieval. [Evolving understanding needs re-distillation, not composition](./evolving-understanding-needs-re-distillation-not-composition.md) is one case of this broader pattern.

**Maintenance** — any navigation aid can go stale. A table of contents, index, abstract, or graph edge is valuable only while it still predicts what the target contains. This is why [stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md). The more a system depends on pointers and distillates, the more it needs maintenance loops that keep them trustworthy.

## Why the RAG framing is too narrow

"RAG" usually names one move: turn a question into a query, retrieve chunks, stuff them into context, answer. That is one routing and loading strategy. It is not the full problem.

The framing becomes misleading when it hides these differences:

- selecting one landing point vs assembling a reading plan
- finding the right inputs vs transforming them into the requested output
- symbolic derivation over retrieved inputs vs semantic synthesis over them
- retrieving chunks vs exposing structure the agent can traverse
- finding candidate pages vs preparing a synthesizable packet
- storing knowledge vs activating it in the right context

A filesystem interface can outperform naive RAG not because files are magical, but because it converts one hard global decision into many cheaper local ones: `ls` to orient, `grep` to narrow, `cat` to inspect, then continue. A graph can outperform both when typed neighborhoods matter. A database can outperform both when scoring and filtering dominate. The right comparison is task-relative, not ideology-relative.

The bounded-context reason for this is easy to miss. Since [agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), access strategies should be compared by how they manage degradation for a task shape, not by whether they match a preferred storage metaphor.

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

## Discovery and synthesis want different structures

[Short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md) argues that the library should be optimized for co-loading many small independent claims. That is one access goal: discovery by juxtaposition.

But the same structure can be bad for consumers who need the whole current picture. When the task is onboarding into an evolving situation, resolving tensions across many notes, or carrying forward a current strategy, fragment composition can exceed effective context. In those cases, a synthesized narrative or workshop artifact may be the right access surface. This suggests that "knowledge access" includes a tension between discovery-optimized structures and synthesis-optimized structures, not just a choice of retriever.

## Historical analogy

Libraries solved analogous problems long before computers. They did not rely on one universal access mechanism. They used catalogues, subject headings, shelf order, abstracts, bibliographies, and reference desks. The pattern seems durable: one corpus, multiple projections, each optimized for a different access task.

The broader pattern may be older and wider than libraries. [Soft-bound traditions as sources for context engineering strategies](./soft-bound-traditions-as-sources-for-context-engineering-strategies.md) identifies recurring responses wherever a bounded processor cannot consume everything at once: selection pressure, compression, progressive formalization, and modularity. Library systems, technical writing, hypertext, and faceted classification all look like members of this family.

What seems new in agent systems is not the existence of these layers but the hard bounded-context constraint. For an LLM, bad organization is not just inconvenient. It directly competes with the task for limited reasoning budget. That makes [context engineering](./definitions/context-engineering.md) the umbrella problem and makes [distillation](./definitions/distillation.md) part of the access architecture, not just a summarization afterthought.

## Open questions

- How many distinct navigation modes are there beyond link-following and search?
- What is the right taxonomy for transformation burden: lookup, derivation, aggregation, synthesis, conjecture, or something else?
- Can access burden and transformation burden be estimated separately for a query?
- Which query classes should stay symbolic end-to-end, and which should hand off to semantic processing?
- When does a question cross from retrieval into synthesis, and can that boundary be detected automatically?
- What is the right division of labor between discovery-optimized library structures and synthesis-optimized workshop artifacts?
- What kinds of distillates are worth maintaining by hand, and which should be generated?
- When does graph structure earn its maintenance cost over indexes plus links?
- Can a system measure whether its pointers actually improve read/skip decisions, rather than only final answer accuracy?

---

Relevant Notes:

- [agent memory needs discoverable, composable, trusted knowledge under bounded context](./agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) — broadens the success criterion from answer-finding to contextual competence
- [context engineering](./definitions/context-engineering.md) — frames the umbrella problem as routing, loading, scoping, and maintenance under bounded context
- [distillation](./definitions/distillation.md) — treats TOCs, abstracts, and synthesized overviews as task-targeted compressions rather than generic summaries
- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — grounds the pointer-design part of the problem
- [link-following and search impose different metadata requirements](./link-following-and-search-impose-different-metadata-requirements.md) — names one navigation split this note broadens into a larger task taxonomy
- [a knowledge base should support fluid resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) — extends the navigation question from retrieval accuracy to movement between abstraction levels
- [effective context is task-relative and complexity-relative not a fixed model constant](./effective-context-is-task-relative-and-complexity-relative-not-a.md) — sharpens why access strategies should be compared per task shape rather than globally
- [agent context is constrained by soft degradation not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — grounds the claim that access architecture must manage degradation rather than only fit under a hard limit
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — grounds the symbolic/semantic split as symbolic scheduling and bounded semantic calls rather than treating all post-retrieval work as one kind
- [ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — adds the case where answers are mechanically derived on demand rather than retrieved verbatim or persisted as durable knowledge
- [short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md) — adds the discovery-optimized side of the library vs synthesis tension
- [soft-bound traditions as sources for context engineering strategies](./soft-bound-traditions-as-sources-for-context-engineering-strategies.md) — extends the library analogy into a broader family of bounded-processor traditions
- [evolving understanding needs re-distillation, not composition](./evolving-understanding-needs-re-distillation-not-composition.md) — grounds the claim that some questions are synthesis problems, not page-selection problems
- [files beat a database for agent-operated knowledge bases](./files-not-database.md) — narrows one layer of the design space to substrate choice rather than treating it as the whole architecture
- [access burden and transformation burden are independent query dimensions](./access-burden-and-transformation-burden-are-independent-query.md) — extracted: develops the two-axis decomposition and the symbolic/semantic corollary into a standalone claim
