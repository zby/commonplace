=== SEMANTIC REVIEW: agents-navigate-by-deciding-what-to-read-next.md ===

Claims identified: 11

1. "That decision is the fundamental unit of navigation." (intro)
2. Pointer enumeration: links, index entries, search results, skill descriptions (intro + "How much context" section)
3. "The more context a pointer carries, the cheaper the navigation decision." (What makes the decision tractable)
4. "A bare filename forces the agent to load the target just to judge relevance." (What makes the decision tractable)
5. "The decision is always probabilistic." (What makes the decision tractable)
6. "Inline links carry the most [context]." (How much context section)
7. "Index entries carry less, but more than they appear to." (How much context section)
8. "Skill descriptions carry only what fits in a single line." (How much context section)
9. "Search tools split the decision in two." (How much context section)
10. "Title as claim is the shortcut that works across all of these." (Design implication)
11. Design lever enumeration: four levers for four pointer types (Design implication)

WARN:
- [completeness] The four-type pointer enumeration (links, index entries, skill descriptions, search tools) omits **error messages and validation output as pointers**. When an agent runs a validation check or encounters an error, the output often points to specific files or instructions and carries diagnostic context (the error itself). This is a genuine navigation pathway in agent workflows -- the agent reads the error, decides what to open next -- and it does not map cleanly to any of the four enumerated types. Error output carries context similarly to inline links (the message explains why the target matters) but is triggered by failure rather than by reading prose.

INFO:
- [completeness] The enumeration does not explicitly account for **directory listings as pointers**. The note mentions "a bare filename" as a degenerate case, but `ls` output or file-tree browsing is a common agent navigation strategy that falls between "search tools" and "bare filename." The note's framework can accommodate this (it would be a low-context pointer, similar to a bare filename), but listing it as a distinct pointer type with its own context characteristics might strengthen the analysis -- directory structure itself carries implicit context (path segments, sibling files) much as index structure does.
- [completeness] **Conversation history / prior context as pointer** is absent. An agent may decide what to read next based on something mentioned earlier in the conversation or in a previous tool output. These are not pointers embedded in documents but pointers embedded in working memory. The note scopes itself to pointers encountered during navigation of a knowledge system, which arguably excludes conversational context, but the boundary is unstated.
- [completeness] The claim that "inline links carry the most" context is presented as a strict ordering (inline > index > skill > search), but the ordering conflates two axes: **context richness** (how much the agent learns about the target) and **context specificity** (how task-relevant the context is). A search result snippet surfaced by a well-targeted query may carry more task-relevant context than a generic inline link like "see [X] for details." The note's ordering holds for the typical case but the exceptions are worth acknowledging.
- [grounding] The source "Agentic Note-Taking 23" is cited as validating "the negative case: what breaks when pointers lack context." The source does describe this, but its primary argument is broader -- it is a critique of embedding-based organization as an industry paradigm, covering Goodhart corruption, controlled disorder, and scaling objections. The note's citation accurately extracts the pointer-context thread but does not flag that the source's scope extends well beyond the navigation-decision framing. This is not a misattribution, but readers who follow the link expecting a focused treatment of pointer context will encounter a much wider argument.

PASS:
- [grounding] The link to "title-as-claim-enables-traversal-as-reasoning" accurately represents the source. The note says title-as-claim "is the shortcut that works across all of these" pointer types, and the linked note explicitly argues that claim titles make navigation cheaper by carrying the argument in the pointer itself. The relationship semantic ("foundation") is correctly stated in the Relevant Notes section.
- [grounding] The attribution to "Agentic Note-Taking 23" as validating the negative case is accurate. The source contains extensive first-person testimony of the qualitative difference between following propositional links with "since [X]" framing and encountering embedding-based "related" items with no articulated reason. The specific mechanism the note describes -- inability to estimate relevance before following -- is directly stated in the source.
- [internal consistency] The note maintains consistent definitions throughout. "Navigation" is always decision-to-follow-a-pointer. "Context" is always information-that-helps-judge-relevance-before-loading. "Pointer" is always an artifact that references a target the agent might read. No definition drift detected.
- [internal consistency] The probabilistic framing ("the decision is always probabilistic: how likely is this pointer to lead somewhere relevant, and what does it cost to find out?") is consistent with the cost-based framing in the design implication section ("make that decision as cheap as possible"). Both treat navigation as an expected-value calculation under uncertainty.
- [internal consistency] The four-type ordering in "How much context different pointers carry" is consistent with the four design levers in "Design implication." Each pointer type gets exactly one lever, and the lever addresses the specific context-carrying mechanism described for that type. No items are introduced or dropped between sections.

Overall: 1 warning, 4 info
===
