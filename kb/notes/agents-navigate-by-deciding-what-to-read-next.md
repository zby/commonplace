---
description: An agent doing a task navigates by deciding what to read — links, index entries, search tools, and skill descriptions are all pointers with varying amounts of context for that decision
type: note
traits: []
tags: [links]
status: current
---

# Agents navigate by deciding what to read next

An agent has a task and needs information she doesn't yet have. She can't read everything, so at every step she encounters pointers — links, index entries, search results, skill descriptions — and decides which to follow. That decision is the fundamental unit of navigation.

## What makes the decision tractable

Every pointer asks the same question: **should I follow this?** She can never be sure before following. The content might not deliver. The decision is always probabilistic: how likely is this pointer to lead somewhere relevant, and what does it cost to find out?

What makes the decision tractable is *context* — the information surrounding the pointer that hints at what the target contains. A bare filename forces the agent to load the target to judge relevance. A pointer embedded in explanatory prose lets her judge without paying that cost. The more context a pointer carries, the cheaper the navigation decision.

## How much context different pointers carry

The mechanism is the same everywhere — what varies is how much context the agent has at the moment of decision.

**Inline links** carry the most. The surrounding prose does double duty — it advances the argument *and* tells the agent what the target contains: "Since [thin adapters reduce coupling](./thin-adapters.md), we chose..." The agent knows both *what's there* and *why it matters here* before deciding.

**Index entries** carry less, but more than they appear to. The context phrase next to the link — "extends this by adding the temporal dimension" — is the explicit hint. But the index's structure adds implicit context: an entry under an "Approvals" heading tells the agent more than the same entry in a flat list.

**Skill descriptions** carry only what fits in a single line. Claude Code loads all descriptions at session start: "Use when the user wants to find connections between notes." The description is the entire hint; the full SKILL.md is the target. The agent decides which skill to invoke without loading its definition.

**Search tools** break the pattern — they split the decision in two. First the agent decides *whether to search*, guided by earlier hints: a CLAUDE.md instruction mentioning `docs/notes/`, a tool description saying "searches the knowledge base", prior experience with the project. Then she decides *which result to open*, guided only by titles, snippets, and descriptions. Frontmatter descriptions matter so much because at that second decision point, they're often all the agent has.

## Design implication

If the fundamental unit of navigation is the decision to follow a pointer, then the knowledge system should make that decision as cheap as possible. Each pointer type has its own lever:

- **Inline links** need surrounding prose that explains the relationship — the prose *is* the context
- **Index entries** need context phrases and clear thematic structure — both the phrase and the position carry information
- **Skill descriptions** need to say *when and why*, not just *what* — scope is more useful than summary
- **Notes** need titles that are claims and descriptions that add information beyond them — because search surfaces these first

[Title as claim](./title-as-claim-enables-traversal-as-reasoning.md) is the shortcut that works across all of these. When the title carries the argument, the pointer itself becomes the hint — every link text, every search result, every index entry does navigation work for free.

Relevant Notes:

- [title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — foundation: claim titles carry the argument in the pointer itself, reducing the cost of the navigation decision
- [Agentic Note-Taking 23: Notes Without Reasons](../sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.md) — validates (negative case): first-person testimony of what breaks when pointers lack context — embedding-generated links carry no reasons, making relevance estimation impossible before following
