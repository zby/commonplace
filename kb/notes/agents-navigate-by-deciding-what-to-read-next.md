---
description: "Models agent navigation as repeated follow/skip judgment under bounded context: cue diagnosticity must repay its own context cost, so longer pointer context is not automatically better"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [links]
---

# Agents navigate by deciding what to read next

An agent has a task and needs information she does not yet have. She cannot read everything, so each pointer — a link, index entry, search result, or skill description — creates a local decision: follow now or skip for now. This note uses that decision as a model of navigation; it does not claim that every navigation operation reduces to it.

## What makes the decision tractable

Every pointer asks the same question: **should I follow this?** The decision is made under uncertainty because a cue predicts relevance rather than revealing it. In the LLM-agent setting, the reader must compare the expected benefit of following with the context and interaction cost of finding out.

[Pirolli's Web-navigation account](../sources/pirolli-proximal-information-scent-distal-content.ingest.md) provides a narrower human source-side analogue: information-scent cues such as links and citations give users concise information about content that is not immediately available, and users assess proximal cues to choose actions leading toward distal information sources. The transfer rests on the shared information structure: both a human Web user and an LLM agent choose among distal sources from proximal cues. The resource and mechanism do not transfer automatically; Pirolli studies human judgment and interaction cost, while an LLM agent pays context tokens and tool calls.

For an LLM agent, diagnostic context can make the decision tractable by reducing uncertainty before the target is loaded. A cue that does not discriminate among candidates leaves the agent needing another information-bearing step, often target loading. Explanatory prose can defer that step when its added information justifies its own context cost. As [linking theory](./linking-theory.md) proposes, the useful quantity is navigation-uncertainty reduction per unit of context consumed. More context is not automatically better.

## Context varies by navigation mode

Different pointer types expose different kinds and typical amounts of context. Inline links can use surrounding prose to explain both what the target contains and why it matters. Search results usually expose only titles and descriptions. Since [link-following and search impose different metadata requirements](./link-following-and-search-impose-different-metadata-requirements.md), the knowledge system must invest in different metadata for each mode: surrounding prose for link-following, titles and descriptions for search, and both for indexes that bridge the two.

## Design implication

If navigation is deciding what to read, the knowledge system should make that decision as cheap as possible. [Title as claim](./title-as-claim-enables-traversal-as-reasoning.md) is a shortcut across links, search results, and indexes. When the title carries the argument, the pointer itself becomes the hint — link text, search results, and index entries can do navigation work before the target is opened.

---

Relevant Notes:

- [link-following and search impose different metadata requirements](./link-following-and-search-impose-different-metadata-requirements.md) — extends: decomposes the context-varies-by-pointer observation into two navigation modes with distinct metadata needs
- [title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — foundation: claim titles carry the argument in the pointer itself, reducing the cost of the navigation decision
- [Agentic Note-Taking 23: Notes Without Reasons](https://x.com/molt_cornelius/status/2026894188516696435) — validates (negative case): first-person testimony of what breaks when pointers lack context — embedding-generated links carry no reasons, making relevance estimation impossible before following
