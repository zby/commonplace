=== SEMANTIC REVIEW: two-kinds-of-navigation.md ===

Claims identified: 9

1. "There are two ways to move through a knowledge base" (title + opening line) -- enumeration: exactly two kinds
2. "Following links" is "local navigation" -- definition
3. "Each step is short -- from one document to a neighbor" -- characterization
4. "The context around the link informs the decision" -- causal claim, cites agents-navigate note
5. "Search" is "long jumps" -- definition
6. "No local context guides the decision" -- scope claim about search (absolute: "no")
7. "Indexes sit in between" -- positional claim: indexes are a hybrid
8. "An index is a page of links -- local navigation in form -- but it functions like a curated search result" -- dual-nature definition
9. "links need surrounding context... search results need good titles and descriptions... indexes need both" -- design implication

WARN:
- [Completeness] The note claims "two ways to move through a knowledge base" but the cited source (agents-navigate-by-deciding-what-to-read-next.md) identifies four pointer types: inline links, index entries, skill descriptions, and search tools. Skill descriptions are a navigation mechanism that does not fit cleanly into either "following links" or "search" as defined here -- they are more like declarative routing hints than either local traversal or keyword query. The note's own acknowledgment that "indexes sit in between" already concedes the binary is leaky, but skill-based navigation is a further case that falls outside the two-pole framing entirely.
- [Completeness] Direct access by memory/recall -- navigating to a known document by typing its path or recalling its location from a previous session -- is a common navigation mode in practice (especially for agents that accumulate session history). It involves neither following a link in context nor issuing a search query. The note's framing has no place for it.
- [Grounding alignment] The note cites agents-navigate-by-deciding-what-to-read-next.md in support of the two-kinds framing, but that source actually models navigation as a single continuum of pointer-following with varying context, not a binary split. The source's core abstraction is "every pointer asks the same question: should I follow this?" with context as a sliding scale. The note's binary taxonomy (local vs. long-range) is the note's own interpretive move, not something the source asserts. A reader following the link would find a different and arguably incompatible framing.

INFO:
- [Completeness] Browsing a file tree or directory listing is a navigation mode that straddles the boundary: it resembles search (scanning many options) but involves no query, and it resembles link-following (clicking entries) but lacks the surrounding prose context the note associates with links. It could be forced into "search" but the fit is strained since there is no query step.
- [Internal consistency] The note says search has "no local context" guiding the decision, but then describes indexes as functioning "like a curated search result" while being "local navigation in form." If indexes provide local context and function like search results, then the "no local context" characterization of search is too absolute -- it holds for raw search but not for index-mediated search-like behavior. The note partially acknowledges this ("the boundary... blurs at indexes") but the initial framing is starker than the conclusion supports.
- [Grounding alignment] The link to link-contracts-framework.md is labeled "source material" in a "See also" section. The link-contracts note is about link quality practices (anchor text, intent taxonomy, decision hints), not about a navigation taxonomy. The relationship is topical adjacency rather than grounding, which is fine for "See also" but worth noting since the note's own argument does not draw on that source.

PASS:
- [Internal consistency] The definitions of "following links" (local, short steps, context-rich) and "search" (long-range, no local context, title/description-dependent) are internally consistent as described -- they define opposite poles cleanly. No pairwise contradiction between these two definitions.
- [Internal consistency] The design implication ("links need surrounding context to inform decisions, search results need good titles and descriptions to enable picking, and indexes need both") follows logically from the two definitions and the bridge claim about indexes. Each navigation mode's design need is correctly derived from its characterization.
- [Grounding alignment] The claim that "context around the link informs the decision" accurately reflects the cited source's argument. agents-navigate-by-deciding-what-to-read-next.md devotes its central section to explaining how context reduces the cost of navigation decisions, and the note's characterization of link-following as context-rich is faithful to that source.

Overall: 3 warnings, 3 info
===
