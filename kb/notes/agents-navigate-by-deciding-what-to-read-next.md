---
description: Context surrounding a pointer determines how cheaply an agent judges relevance without loading the target; inline links carry most, search results least — descriptions are load-bearing
type: note
traits: []
tags: [links]
status: current
---

# Agents navigate by deciding what to read next

An agent has a task and needs information she doesn't yet have. She can't read everything, so at every step she encounters pointers — links, index entries, search results, skill descriptions — and decides which to follow. That decision is the fundamental unit of navigation.

## What makes the decision tractable

Every pointer asks the same question: **should I follow this?** The agent can never be sure before following — the content might not deliver. So the decision is always probabilistic: how likely is this pointer to lead somewhere relevant, and what does it cost to find out?

What makes it tractable is *context* — information surrounding the pointer that hints at what the target contains. A bare filename forces the agent to load the target just to judge relevance. A pointer embedded in explanatory prose lets her judge without paying that cost. The more context a pointer carries, the cheaper the navigation decision.

## Context varies by navigation mode

Different pointer types carry different amounts of context. Inline links carry the most — the surrounding prose explains both what the target contains and why it matters. Search results carry the least — the agent has only titles and descriptions. Since [link-following and search impose different metadata requirements](./link-following-and-search-impose-different-metadata-requirements.md), the knowledge system must invest in different metadata for each mode: surrounding prose for link-following, titles and descriptions for search, and both for indexes that bridge the two.

## Design implication

If navigation is deciding what to read, the knowledge system should make that decision as cheap as possible. [Title as claim](./title-as-claim-enables-traversal-as-reasoning.md) is the shortcut that works across all pointer types. When the title carries the argument, the pointer itself becomes the hint — every link text, every search result, every index entry does navigation work for free.

---

Relevant Notes:

- [link-following and search impose different metadata requirements](./link-following-and-search-impose-different-metadata-requirements.md) — extends: decomposes the context-varies-by-pointer observation into two navigation modes with distinct metadata needs
- [title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — foundation: claim titles carry the argument in the pointer itself, reducing the cost of the navigation decision
- [Agentic Note-Taking 23: Notes Without Reasons](../sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.md) — validates (negative case): first-person testimony of what breaks when pointers lack context — embedding-generated links carry no reasons, making relevance estimation impossible before following
