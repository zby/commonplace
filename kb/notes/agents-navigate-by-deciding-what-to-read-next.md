---
description: An agent doing a task navigates by deciding what to read — links, index entries, search tools, and skill descriptions are all pointers with varying amounts of context for that decision
type: note
traits: []
areas: [links]
status: current
---

# Agents navigate by deciding what to read next

An agent has a task. To accomplish it, she needs information she doesn't yet have. So she reads documentation — but she can't read everything. At every step, she encounters pointers to more information and decides which to follow. That decision is the fundamental unit of navigation.

## The decision

Every pointer — a link, an index entry, a search tool, a skill description — asks the agent: **should I use this to find what I need?** She can never be sure before following — the hint might be misleading, the content might not deliver. The decision is always probabilistic: how likely is it that this pointer leads to something relevant, and what does it cost to find out?

The quality of the hint determines how well the agent can estimate that likelihood. A bare pointer forces her to load the target to find out. A pointer with context lets her judge without paying that cost.

## A spectrum of context

The pattern is the same everywhere. What varies is how much context the agent has at the decision point.

**Inline links** carry the richest context. The surrounding prose does double duty — it advances the argument *and* tells the agent what the target contains: "Since [thin adapters reduce coupling](./thin-adapters.md), we chose..." The agent knows both *what's there* and *why it matters here* before deciding.

**Index entries** carry less, but more than they seem. The context phrase next to the link — "extends this by adding the temporal dimension" — is the explicit hint. But the index itself adds implicit context: an entry under an "Approvals" heading tells the agent more than the same entry in a flat list. The index's structure is part of the hint.

**Skill descriptions** work at global scope. Claude Code loads all descriptions at session start: "Use when the user wants to find connections between notes." The description is the hint; the full SKILL.md is the target. The agent decides which skill to invoke without loading its definition.

**Search tools** split the decision in two. First the agent decides *whether to search* — guided by earlier hints: a CLAUDE.md instruction mentioning `docs/notes/`, a tool description saying "searches the knowledge base", prior experience with the project. Then she decides *which result to open* — guided only by titles, snippets, and descriptions. The hint to search comes before the search; the hint to pick a result comes from the results themselves. Frontmatter descriptions matter so much because at that second stage, they're all the agent has.

## Design implication

The knowledge system should make these decisions cheap. Every mechanism has its own lever:

- Inline links need surrounding prose that explains the relationship
- Index entries need context phrases — and indexes need clear thematic structure
- Skill descriptions need to say *when and why*, not just *what*
- Notes need titles that are claims and descriptions that add information beyond them

Prose-as-title is the shortcut that works across all of these — because [title as claim enables traversal as reasoning](../title-as-claim-enables-traversal-as-reasoning.md), the pointer carries the argument by itself. But bare pointers without context force the agent to open every target, which is expensive in tokens and attention.

Topics:
- [links](./links.md)
