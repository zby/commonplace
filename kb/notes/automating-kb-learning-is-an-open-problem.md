---
description: The KB already learns through manual work (every improvement is capacity change per Simon). The open problem is automating the judgment-heavy mutations — connections, groupings, synthesis — which require oracles we can't yet manufacture.
type: note
traits: []
areas: [claw-design]
status: speculative
---

# Automating KB learning is an open problem

The KB already has a learning loop — human + agent working together. Every session that improves notes, sharpens connections, or discovers principles is [learning in Simon's sense](../notes/learning-is-capacity-change.md): a change that increases the system's adaptive capacity. This happens all the time, from fixing typos (narrow scope) to discovering design principles (wide scope).

The open problem is not "the KB needs a learning loop" but **automating the judgment-heavy parts** of the loop we already run manually.

## What is a KB for?

A knowledge base exists to answer questions about the project. This defines value for every artifact: a note is valuable if it helps answer a question, a link is valuable if it helps navigate from a question to an answer, a grouping is valuable if it makes related answers findable together.

New knowledge — extracting claims, writing synthesis notes, discovering connections — is valuable only insofar as it improves future question-answering. The [scenarios](./scenarios.md) that define actual KB usage (upstream change analysis, proposing our own changes) are the closest thing we have to a requirements spec for what this question-answering capacity must serve.

## Knowledge lives in both notes and links

A KB's knowledge is in the content of its notes and in the structure of its links — neither alone is sufficient. A note without links still says something. A link without good notes on both ends is useless. But the link structure is the part that's hardest to get right and most underinvested in: adding notes is easy, discovering which notes genuinely connect and why requires judgment.

This suggests that learning at scale for a KB involves improving both — better notes and better links — but that the link structure is where the most untapped value sits, because it's where understanding is encoded: which ideas support each other, which are in tension, which compose into larger arguments. When [stale indexes suppress search entirely](./observations/stale-indexes-are-worse-than-no-indexes.md), the cost of underinvestment in link structure becomes concrete: notes that exist but aren't linked become invisible.

## The boiling cauldron (aspirational)

The visible KB is the production system. Learning could happen through a background process that continuously proposes mutations:

- **Extract**: pull a claim from a source that hasn't been extracted yet
- **Split**: break a note that makes two claims into two notes
- **Synthesise**: two notes that together imply something neither says alone
- **Relink**: find semantically similar notes that aren't linked
- **Reformulate**: improve a title so it works better as prose when linked
- **Regroup**: a cluster of notes suggests an index that doesn't exist yet
- **Retire**: an automated check, link, or note has outlived its usefulness — four signals: zero catches over months, false positives exceed true positives, methodology change made it irrelevant, replaced by a better mechanism (from [arscontexta](https://github.com/agenticnotetaking/arscontexta) methodology review)

Each mutation would be speculative — staged separately, surfaced for human review only when it scores high enough. This is the automated version of what [stabilisation as learning](../notes/agentic-systems-learn-through-three-distinct-mechanisms.md) describes as the manual stabilise/soften cycle — the same system-level adaptation, but with the agent proposing mutations instead of a human driving each one.

## Open problems

**Evaluation.** The KB's value is defined by the questions it answers, but those questions evolve with the project. There's no static benchmark to optimise against. Eventually, logging actual usage (queries, failed retrievals, how many hops to an answer) could provide signal — but we don't have enough usage yet to learn from.

**Quality gates.** Structural metrics (PageRank, betweenness centrality, cluster density) are proxies at best. A note can be well-connected because it's vague enough to "relate to" everything. The real test is whether a change helps answer a question that couldn't be answered before — and we don't have a systematic way to measure that yet. The [text testing framework](./text-testing-framework.md) provides quality checks at both the note level (structural contracts, LLM rubric grading) and the corpus level (contradiction detection, coverage and linking behavior, terminology alignment), but these test artifact quality and inter-document consistency, not the graph's end-to-end question-answering capacity. The [quality signals brainstorm](./quality-signals-for-kb-evaluation.md) catalogues graph-topology, content-proxy, and LLM-hybrid signals that could be combined into a composite oracle — addressing this gap by manufacturing a soft oracle from many weak signals rather than waiting for usage data.

**Surfacing rate.** Too many proposals and the human ignores them. Too few and the system isn't learning. Calibrating this requires feedback on what gets accepted, which requires enough volume to learn from.

These are all instances of the same gap: **we need more usage before we can design the learning loop properly.** The right move for now is to keep building the KB manually, pay attention to [what works](./what-works.md) and [what doesn't](./what-doesnt-work.md), and revisit this when there's enough history to learn from. Those two review notes ARE the manual observation log this approach recommends — they capture proven patterns and anti-patterns that would eventually feed a learning loop's evaluation function.

## Connection to crystallisation

The [bitter lesson boundary](../notes/bitter-lesson-boundary.md) distinguishes calculator-like artifacts (spec captures the problem) from vision-feature-like artifacts (spec encodes a theory). The KB's infrastructure — file formats, frontmatter schema, sync scripts — is calculator-like. The knowledge organisation — which links exist, how notes are grouped, what gets extracted — is vision-feature-like. A learning loop would be the mechanism for continuously improving the vision-feature layer. We're not ready to build it, but the distinction tells us where it would operate.

---

Relevant Notes:
- [learning-is-capacity-change](../notes/learning-is-capacity-change.md) — foundation: Simon's definition of learning as capacity change; every KB improvement is learning, the spectrum of generalisation scope shows why automating wide-scope mutations is the hard part
- [stabilisation-is-learning](../notes/agentic-systems-learn-through-three-distinct-mechanisms.md) — describes the stabilise/soften cycle in both human-driven and automated forms (DSPy, ProTeGi); the boiling cauldron is a KB-specific instantiation of that cycle, applying it to note and link mutations rather than prompts and code
- [what-cludebot-teaches-us](./what-cludebot-teaches-us.md) — co-retrieval reinforcement and consolidation passes are concrete mechanisms for the boiling cauldron; cludebot's "need enough query volume" conclusion mirrors the "need usage first" gap here
- [what-works](./what-works.md) — the observation log this note recommends as interim approach; proven patterns that would feed a learning loop's evaluation
- [what-doesnt-work](./what-doesnt-work.md) — the anti-pattern log; complements what-works as ground truth for what the loop should avoid proposing
- [needs-testing](./needs-testing.md) — the extract/connect/review cycle is a primitive version of the boiling cauldron, already partially operational
- [notes-need-quality-scores-to-scale-curation](./notes-need-quality-scores-to-scale-curation.md) — note scoring addresses part of the quality gates problem: composite scores from status, type, inbound links, and recency make automated curation tractable at scale
- [scenarios](./scenarios.md) — the actual use cases the learning loop's evaluation function would need to optimise against
- [text-testing-framework](./text-testing-framework.md) — quality gates at both note and corpus level that could serve as building blocks for the loop's evaluation, though they test artifact quality and consistency, not end-to-end question-answering capacity
- [quality-signals-for-kb-evaluation](./quality-signals-for-kb-evaluation.md) — addresses the quality gates gap: proposes a composite oracle from graph-topology, content-proxy, and LLM-hybrid signals that could serve as the evaluation function for the boiling cauldron, using structure alone rather than requiring usage data
- [claw-learning-is-broader-than-retrieval](./claw-learning-is-broader-than-retrieval.md) — extends: argues the retrieval-oriented framing here is one layer of a broader problem; a Claw's learning loop must also improve action capacity (classification, communication, planning)

Topics:
- [claw-design](./claw-design.md)
