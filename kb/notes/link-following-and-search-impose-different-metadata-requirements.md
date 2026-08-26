---
description: Link-following is local with rich context; search is long-range with only titles/descriptions — each mode imposes different metadata requirements on the knowledge system
type: kb/types/note.md
traits: []
tags: [links]
---

# Link-following and search impose different metadata requirements

There are two ways to move through a knowledge base, and each gives the agent different context at the moment of decision. Since [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md), the metadata a knowledge system needs to maintain depends on which navigation mode it's optimizing for.

## Link-following: local navigation with rich context

You're reading something, you encounter a link, you decide whether to follow it. Each step is short — from one document to a neighbor.

**Inline links** carry the most context. The surrounding prose does double duty — it advances the argument *and* tells the agent what the target contains: "Since [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md), the metadata..." The agent knows both what's there and why it matters before deciding.

**Index entries** carry less, but more than they appear to. The context phrase next to the link — "extends this by adding the temporal dimension" — is the explicit hint. But the index's structure adds implicit context too: an entry under an "Approvals" heading tells the agent more than the same entry in a flat list.

What inline links and index entries share: the agent already has source-local context (the current note, section, or index grouping) that makes the follow/skip decision tractable.

## Search: long-range jumps without local context

You have a question or keyword, you query the whole corpus, you land somewhere potentially distant. No surrounding argument guides the decision.

**Skill descriptions** are an analogous long-range selection surface. The runtime loads them at session start rather than exposing them inside a source document's argument: "Use when the user wants to find connections between notes." The task supplies some context, but that one line must identify when and why to load the full skill without help from neighboring prose.

**Search results** split the decision in two. First the agent decides *whether to search*, guided by earlier hints: an instruction mentioning a directory path, a tool description saying "searches the knowledge base." Then she decides *which result to open*, guided only by titles, snippets, and descriptions. Frontmatter descriptions matter here — at that second decision point, they're often all the agent has.

What's different: the agent has no source-local context. The pointer must carry enough information on its own for the agent to judge relevance from the task or query.

## Indexes bridge both modes

An index is a page of links — local navigation in form — but it functions like a curated search result. You jump to an index (often via search or memory), then browse its links to find what you need. The boundary between "navigating links" and "searching" blurs at indexes, which is why indexes need both context phrases (for the link-following mode) and clear thematic structure (for the scanning mode).

## Design implication

Each navigation mode has its own metadata lever:

- **Inline links** need surrounding prose that explains the relationship — the prose *is* the context
- **Index entries** need context phrases and clear thematic structure — both the phrase and the position carry information
- **Skill descriptions** need to say *when and why*, not just *what* — scope is more useful than summary
- **Notes** need titles that are claims and descriptions that add information beyond them — because search surfaces these first

[Title as claim](./title-as-claim-enables-traversal-as-reasoning.md) is the shortcut that works across both modes. When the title carries the argument, the pointer itself becomes the hint — every link text, every search result, every index entry does navigation work for free.

---

Relevant Notes:

- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — foundation: the navigation-decision model that this note decomposes by mode
- [title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — extends: claim titles improve both local link-following (inline prose reads as reasoning) and long-range search (titles convey arguments without loading)
- [pointer design tradeoffs in progressive disclosure](./pointer-design-tradeoffs-in-progressive-disclosure.md) — extends: generalizes the pointer-context analysis into a four-axis trade-off (specificity, cost, availability, accuracy)
- [charting the knowledge-access problem beyond RAG](./knowledge-access-architecture-must-be-evaluated-end-to-end.md) — extends: broadens this two-mode split into a larger access-task taxonomy
- [Agentic Note-Taking 23: Notes Without Reasons](https://x.com/molt_cornelius/status/2026894188516696435) — validates (negative case): first-person testimony of what breaks when pointers lack context — embedding-generated links carry no reasons, making relevance estimation impossible before following
