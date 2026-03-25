---
description: "Design exploration for enriching web search by reusing /connect's dual discovery and articulation testing on results, building a temporary research graph before bridging to KB"
type: note
traits: [has-comparison]
tags: []
status: seedling
---

# Brainstorming how to enrich web search

The KB's connection methodology (`/connect`) is corpus-agnostic — it runs the same dual discovery, articulation testing, and synthesis detection regardless of what documents it connects. The core idea: temporarily expand the corpus with web search results, run existing connection machinery across the expanded set, then extract durable insights. Phase 3 below goes beyond pure `/connect` reuse (it adds synthesis and query generation), so this is connection methodology as a starting point, not a complete design.

## Two value propositions

1. **Connect retrieved pieces to each other** — build a "search result graph" where relationships between results are articulated, not just listed. This is the `/connect` pattern applied to a temporary research corpus. The process combines both [kinds of navigation](./link-following-and-search-impose-different-metadata-requirements.md) in a new context: long-range search retrieves external results, then local link-following connects them into a traversable temporary graph.
2. **Connect retrieved pieces to existing KB** — what `/ingest` already does, but at scale. The KB provides pre-existing structural understanding that elevates raw search results. This extends [the KB's action capacity](./claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) beyond retrieval into active research — the agent doesn't just look up what it knows, it discovers what it doesn't.

## Why this differs from naive search

The [discovery epistemology note](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) identifies three abstraction depths for connections:

1. **Shared feature** — "both mention X." Embeddings get here cheaply. This is what naive RAG does.
2. **Shared structure** — "both exhibit pattern P." Requires understanding, not just matching. Expensive.
3. **Generative model** — "both are instances of mechanism M that I just named." Requires inventing the dimension. Highest value.

Naive deep search stays at level 1. The `/connect` skill already operates at level 2 (the articulation test forces structural reasoning). The design question: can iterative search reach level 3? Only if the iteration loop explicitly looks for synthesis opportunities — gaps and emergent claims that neither individual result contains.

## Proposed architecture: Search, Connect, Synthesize, Redirect

**Phase 1: Seed search.** User provides a query + optional KB context. Run multiple web searches with query variations.

**Phase 2: Snapshot & inter-connect.** Snapshot top results into a temporary workspace. Run a lightweight `/connect`-like pass across them — not to the KB yet, just among themselves. The articulation test from `/connect` applies: "Result A connects to Result B because [specific reason]."

**Phase 3: Synthesize & redirect.** After building the inter-result graph, look for:
- **Gaps** — clusters of results that don't connect to each other suggest missing concepts
- **Synthesis opportunities** — two results that together imply something neither says alone
- **New queries** — gap/synthesis analysis generates new search queries the original user couldn't have formulated

This is the [boiling cauldron](./automating-kb-learning-is-an-open-problem.md) loop applied to search: propose mutations, evaluate, iterate.

**Phase 4: Bridge to KB.** Only after the search graph is internally coherent, connect it to the existing KB. This is where the KB's structural understanding elevates raw results.

**Phase 5: Report.** Key findings, the connection graph with articulated reasons, what's genuinely new vs. already captured, recommended next actions.

## Architectural tensions

**Depth vs. cost.** Each iteration means more LLM calls. `/connect` already uses depth modes (deep/standard/quick). Deep search compounds this — N results x connection passes x iteration rounds. Aggressive pruning heuristics are needed — the same candidate-explosion problem that [notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md) identifies for /connect, but amplified by web-scale result sets. The [quality signals](./quality-signals-for-kb-evaluation.md) note has relevant metrics (centrality measures to identify which results are worth deeper investigation).

**Workshop lifecycle.** Where do intermediate artifacts live? This is quintessential [workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) material — high-churn, value-consuming-over-time, needing extraction bridges to become library material. Candidate: `kb/research/{session-id}/` with explicit human review before anything becomes permanent.

**Stopping criterion.** Iterative search can loop forever. Each heuristic below is a proxy oracle of different strength on the [oracle-strength spectrum](./oracle-strength-spectrum.md) — the stronger the signal, the more confidently the loop can terminate:
- Diminishing returns — new results mostly overlap with existing graph (soft oracle: structural convergence)
- Query exhaustion — synthesis step generates no new queries (soft oracle: generative capacity depleted)
- Budget — hard cap on iterations/API calls (deterministic but says nothing about output quality — verifies cost compliance, not result value)
- User checkpoint — pause after N rounds for human steering (interactive oracle: human judgment)

## Minimum viable version

The MVP reuses existing skills without the iteration loop:

1. Multi-query web search (the genuinely new part)
2. Snapshot results to temp workspace (reuse `/snapshot-web`)
3. Run `/connect` across the temp workspace
4. Bridge to KB (reuse `/ingest`'s connection logic)
5. Produce research report

Even single-pass "search, snapshot, connect, bridge, report" would validate whether connection quality on web search results justifies the iteration investment. The iteration loop (Phase 3) is the ambitious part — build it only after validating the base case. The MVP's five-step chain is itself a [scenario decomposition](./scenario-decomposition-drives-architecture.md) — each phase has concrete context needs that could be measured the same way write-a-note and ingest-a-source are measured.

## Open Questions

- What's the right granularity for snapshotting? Full pages vs. extracted passages?
- Should the temporary workspace use the same document types as the KB, or a lighter format? Since [skills are typed callables](./instructions-are-typed-callables.md), deep search's type signature would be something like `query + context → research-report + source-reviews` — a compound output that chains multiple existing skill signatures.
- How does the iteration budget interact with the two learning mechanisms — is this [constraining](./definitions/constraining.md) (constraining search), [distillation](./definitions/distillation.md) (extracting procedure from exploration), or something else?
- Can the extract/connect/review cycle be validated through enriched search before investing in the full [boiling cauldron](./automating-kb-learning-is-an-open-problem.md)?
- How should the process handle search results that *contradict* existing KB content? The two value propositions are both additive (connect results to each other, connect to KB). Contradiction detection is a different operation — it challenges the KB rather than extending it.

---

Relevant Notes:

- [discovery is seeing the particular as an instance of the general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — provides the abstraction depth framework that distinguishes this from naive search
- [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — the boiling cauldron concept maps directly to the iterative search loop
- [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — deep search results are workshop material needing extraction bridges
- [linking-theory](./linking-theory.md) — link quality criteria inform how inter-result connections should be expressed
- [quality signals for KB evaluation](./quality-signals-for-kb-evaluation.md) — centrality metrics for pruning search result graphs
- [skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) — deep search skill would distill from this methodology note
- [oracle-strength spectrum](./oracle-strength-spectrum.md) — stopping criteria for the iteration loop map to oracle types of varying strength
- [notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md) — extends: deep search amplifies the candidate-explosion problem /connect faces at KB scale
- [claw learning loops must improve action capacity not just retrieval](./claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) — exemplifies: deep search is active research capacity, not retrieval; the agent discovers what it doesn't know rather than looking up what it does
- [two kinds of navigation](./link-following-and-search-impose-different-metadata-requirements.md) — synthesizes: deep search creates a temporary corpus where both navigation modes operate — long-range search retrieves, then local link-following inter-connects
- [scenario decomposition drives architecture](./scenario-decomposition-drives-architecture.md) — enables: the MVP's five phases are a scenario decomposition whose context needs could be measured like other scenarios
- [instructions are typed callables](./instructions-are-typed-callables.md) — extends: deep search's compound type signature (query + context → research-report + source-reviews) chains multiple existing skill signatures
- [scenario-decomposition-drives-architecture](./scenario-decomposition-drives-architecture.md) — extends: deep search defines a third scenario type ("research a topic deeply") beyond upstream change analysis and proposing changes
