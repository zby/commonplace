---
description: The KB already learns through manual work (every improvement is capacity change per Simon). The open problem is automating the judgment-heavy mutations — connections, groupings, synthesis — which require oracles we can't yet manufacture.
type: note
traits: []
tags: []
status: speculative
---

# Automating KB learning is an open problem

The KB already has a learning loop — human + agent working together. Every session that improves notes, sharpens connections, or discovers principles is [learning in Simon's sense](../notes/learning-is-not-only-about-generality.md): a change that increases the system's adaptive capacity. This happens all the time, from fixing typos (narrow scope) to discovering design principles (wide scope).

The open problem is not "the KB needs a learning loop" but **automating the judgment-heavy parts** of the loop we already run manually.

## What is a KB for?

A knowledge base exists to answer questions about the project. This defines value for every artifact: a note is valuable if it helps answer a question, a link is valuable if it helps navigate from a question to an answer, a grouping is valuable if it makes related answers findable together.

New knowledge — extracting claims, writing synthesis notes, discovering connections — is valuable only insofar as it improves future question-answering. The [scenarios](./scenarios.md) that define actual KB usage (upstream change analysis, proposing our own changes) are the closest thing we have to a requirements spec for what this question-answering capacity must serve.

## Knowledge lives in both notes and links

A KB's knowledge is in the content of its notes and in the structure of its links — neither alone is sufficient. A note without links still says something. A link without good notes on both ends is useless. But the link structure is the part that's hardest to get right and most underinvested in: adding notes is easy, discovering which notes genuinely connect and why requires judgment.

This suggests that learning at scale for a KB involves improving both — better notes and better links — but that the link structure is where the most untapped value sits, because it's where understanding is encoded: which ideas support each other, which are in tension, which compose into larger arguments. When [stale indexes suppress search entirely](./stale-indexes-are-worse-than-no-indexes.md), the cost of underinvestment in link structure becomes concrete: notes that exist but aren't linked become invisible.

## The boiling cauldron (aspirational)

The visible KB is the production system. Learning could happen through a background process that continuously proposes mutations:

- **Extract**: pull a claim from a source that hasn't been extracted yet
- **Split**: break a note that makes two claims into two notes
- **Synthesise**: two notes that together imply something neither says alone
- **Relink**: find semantically similar notes that aren't linked
- **Reformulate**: improve a title so it works better as prose when linked
- **Regroup**: a cluster of notes suggests an index that doesn't exist yet
- **Retire**: an automated check, link, or note has outlived its usefulness — four signals: zero catches over months, false positives exceed true positives, methodology change made it irrelevant, replaced by a better mechanism (from [arscontexta](https://github.com/agenticnotetaking/arscontexta) methodology review)

Each mutation would be speculative — staged separately, surfaced for human review only when it scores high enough. This is the automated version of what [constraining as learning](../notes/constraining.md) describes as the manual constrain/relax cycle — the same system-level adaptation, but with the agent proposing mutations instead of a human driving each one.

## Mutations differ on two axes

The boiling cauldron mutations differ on both generality and codifiability:

**By generality:**
- **Extract, reformulate** — narrow scope, improving individual notes (Extract is accumulation — adding knowledge to the store; its value depends on the reach of what's extracted)
- **Relink, regroup, synthesise** — medium scope, changing how knowledge connects (these transform accumulated knowledge)
- **Retire, restructure** — wide scope, changing the system's organising principles

**By codifiability** (reliability+speed+cost compound):
- **Codifiable operations** (link checking, section validation, index regeneration) — already automatable as scripts, gaining reliability, speed, and cost simultaneously
- **Judgment operations** (is this claim worth keeping? should these notes merge?) — require LLM or human assessment, may codify later as patterns emerge

Automating narrow-scope improvements is relatively tractable (ingest pipelines, LLM extraction, validation scripts). Automating wide-scope improvements is the hard part — it requires judgment about what principles generalise. Codifiability is a separate axis — often tractable regardless of scope, because the question "can this be made deterministic?" is itself fairly deterministic.

## The vocabulary gap

[Constraining during deployment is already continuous learning](../notes/constraining-during-deployment-is-continuous-learning.md) — developers accumulate informal tweaks, agent memory systems (Claude's memory files, Cursor rules, AGENTS.md conventions) store preferences across sessions, teams version their prompts and tools. But none of it is systematic. Automating the learning loop requires a mechanistic description of the process — what the operations are, how they compose, what makes one succeed or fail. That description requires a vocabulary that doesn't yet exist in standard use: [accumulation](../notes/learning-is-not-only-about-generality.md) as the basic learning operation with [reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) as its key property (facts at the low end, theories at the high end), [constraining](../notes/constraining.md) and [distillation](../notes/distillation.md) as the two mechanisms that transform accumulated knowledge, the [generality-vs-compound trade-off](../notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) as what they operate on, the [verifiability gradient](../notes/deploy-time-learning-the-missing-middle.md) as the progression path, the [bitter lesson boundary](../notes/bitter-lesson-boundary.md) as the test for when codification is permanent vs temporary. Without these distinctions, "make the system learn" is a wish, not a design specification. The [adaptation taxonomy for agentic AI](../notes/research/adaptation-agentic-ai-analysis.md) begins to close the gap by identifying data-driven triggers for when to constrain versus when to relax.

## Open problems

**Evaluation.** The KB's value is defined by the questions it answers, but those questions evolve with the project. There's no static benchmark to optimise against. Eventually, logging actual usage (queries, failed retrievals, how many hops to an answer) could provide signal — but we don't have enough usage yet to learn from.

**Quality gates.** Structural metrics (PageRank, betweenness centrality, cluster density) are proxies at best. A note can be well-connected because it's vague enough to "relate to" everything. The real test is whether a change helps answer a question that couldn't be answered before — and we don't have a systematic way to measure that yet. The [text testing framework](./text-testing-framework.md) provides quality checks at both the note level (structural contracts, LLM rubric grading) and the corpus level (contradiction detection, coverage and linking behavior, terminology alignment), but these test artifact quality and inter-document consistency, not the graph's end-to-end question-answering capacity. The [quality signals brainstorm](./quality-signals-for-kb-evaluation.md) catalogues graph-topology, content-proxy, and LLM-hybrid signals that could be combined into a composite oracle — addressing this gap by manufacturing a soft oracle from many weak signals rather than waiting for usage data.

**Surfacing rate.** Too many proposals and the human ignores them. Too few and the system isn't learning. Calibrating this requires feedback on what gets accepted, which requires enough volume to learn from.

**Oracle difficulty varies by learning type.** [Pi Self-Learning](./related-systems/pi-self-learning.md) sidesteps the oracle problem entirely by picking the easiest available oracle: mistakes have a natural verifier (the fix). Extract what went wrong, score by recurrence, inject the top patterns — no quality judgment needed beyond "did this keep happening?" The KB's harder learning problems — "should these notes be linked?", "is this synthesis correct?", "does this index need a new entry?" — lack that natural verifier. The [quality signals brainstorm](./quality-signals-for-kb-evaluation.md) proposes manufacturing a soft oracle from many weak structural signals, but that's still speculative. Pi-self-learning's success at the easy end of the oracle spectrum clarifies where the hard end actually is: not in the learning mechanism (scoring, ranking, injection are all straightforward) but in manufacturing evaluation for judgment-heavy mutations.

These are all instances of the same gap: **we need more usage before we can design the learning loop properly.** The right move for now is to keep building the KB manually, pay attention to what works and what doesn't, and revisit this when there's enough history to learn from.

## Connection to codification

The [bitter lesson boundary](../notes/bitter-lesson-boundary.md) distinguishes calculator-like artifacts (spec captures the problem) from vision-feature-like artifacts (spec encodes a theory). The KB's infrastructure — file formats, frontmatter schema, sync scripts — is calculator-like. The knowledge organisation — which links exist, how notes are grouped, what gets extracted — is vision-feature-like. A learning loop would be the mechanism for continuously improving the vision-feature layer. We're not ready to build it, but the distinction tells us where it would operate.

---

Relevant Notes:

- [learning is not only about generality](../notes/learning-is-not-only-about-generality.md) — foundation: Simon's definition of learning as capacity change; every KB improvement is learning, the spectrum of generalisation scope shows why automating wide-scope mutations is the hard part
- [constraining](../notes/constraining.md) — describes the constrain/relax cycle in both human-driven and automated forms (DSPy, ProTeGi); the boiling cauldron is a KB-specific instantiation of that cycle, applying it to note and link mutations rather than prompts and code
- [what-cludebot-teaches-us](./what-cludebot-teaches-us.md) — co-retrieval reinforcement and consolidation passes are concrete mechanisms for the boiling cauldron; cludebot's "need enough query volume" conclusion mirrors the "need usage first" gap here
- [needs-testing](./needs-testing.md) — the extract/connect/review cycle is a primitive version of the boiling cauldron, already partially operational
- [notes-need-quality-scores-to-scale-curation](./notes-need-quality-scores-to-scale-curation.md) — note scoring addresses part of the quality gates problem: composite scores from status, type, inbound links, and recency make automated curation tractable at scale
- [scenarios](./scenarios.md) — the actual use cases the learning loop's evaluation function would need to optimise against
- [text-testing-framework](./text-testing-framework.md) — quality gates at both note and corpus level that could serve as building blocks for the loop's evaluation, though they test artifact quality and consistency, not end-to-end question-answering capacity
- [quality-signals-for-kb-evaluation](./quality-signals-for-kb-evaluation.md) — addresses the quality gates gap: proposes a composite oracle from graph-topology, content-proxy, and LLM-hybrid signals that could serve as the evaluation function for the boiling cauldron, using structure alone rather than requiring usage data
- [trace-derived learning techniques in related systems](./trace-derived-learning-techniques-in-related-systems.md) — sharpens: the extraction side of the loop is now concrete in source code across session miners and weight-learning systems; what remains open is evaluation of whether mined candidates deserve durable KB status
- [claw-learning-is-broader-than-retrieval](./claw-learning-is-broader-than-retrieval.md) — extends: argues the retrieval-oriented framing here is one layer of a broader problem; a Claw's learning loop must also improve action capacity (classification, communication, planning)
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — confirms from the other direction: AgeMem shows RL can learn memory-management policy, but only because task completion provides a clear oracle; the KB's evaluation gap (no equivalent oracle) is the real bottleneck, not the learning mechanism
- [Pi Self-Learning](./related-systems/pi-self-learning.md) — exemplifies: succeeds at automated learning by picking the easiest oracle (mistake recurrence); clarifies that our harder learning problems stall not on mechanism but on oracle construction
- [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — synthesis: the KB's automation bottleneck is an instance of the general principle that automation stalls where oracle construction stalls
- [automated synthesis is missing good oracles](./automated-synthesis-is-missing-good-oracles.md) — develops: the "Synthesise" mutation listed here has a specific bottleneck — generation is easy, evaluation is hard — explored in depth there
- [Agentic Note-Taking 23: Notes Without Reasons](../sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.md) — extends: the scaling question ("can curation survive at 10K-100K notes?") and the compounding-returns hypothesis are directly relevant to the automation challenge; the source also provides the strongest articulation of why retrieval and navigability are distinct system goals requiring different evaluation metrics
