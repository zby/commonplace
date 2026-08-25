---
description: "The KB already learns through manual improvement; automating judgment-heavy mutations needs oracles for connections, groupings, and synthesis we cannot yet manufacture"
type: kb/types/note.md
traits: [title-as-claim]
tags: []
---

# Automating KB learning is an open problem

The KB already has a learning loop — human + agent working together. Every session that improves notes, sharpens connections, or discovers principles is [learning in Simon's sense](../notes/learning-is-not-only-about-generality.md): a change that increases the system's adaptive capacity. This happens all the time, from fixing typos (narrow scope) to discovering design principles (wide scope).

The open problem is not "the KB needs a learning loop" but **automating the judgment-heavy parts** of the loop we already run manually.

## What is a KB for?

A knowledge base exists to answer questions about the project. This defines value for every artifact: a note is valuable if it helps answer a question, a link is valuable if it helps navigate from a question to an answer, a grouping is valuable if it makes related answers findable together.

New knowledge — extracting claims, writing synthesis notes, discovering connections — is valuable only insofar as it improves future question-answering. The [scenarios](./scenario-decomposition-drives-architecture.md) that define actual KB usage (upstream change analysis, proposing our own changes) are the closest thing we have to a requirements spec for what this question-answering capacity must serve.

## Knowledge lives in both notes and links

A KB's knowledge is in the content of its notes and in the structure of its links — neither alone is sufficient. A note without links still says something. A link without good notes on both ends is useless. But the link structure is the part that's hardest to get right and most underinvested in: adding notes is easy, discovering which notes genuinely connect and why requires judgment.

This suggests that learning at scale for a KB involves improving both — better notes and better links — but that the link structure is where the most untapped value sits, because it's where understanding is encoded: which ideas support each other, which are in tension, which compose into larger arguments. [Stale indexes reduce discovery when they suppress fallback search](./stale-indexes-reduce-discovery-when-they-suppress-fallback-search.md); the cost of underinvestment becomes concrete when apparently complete navigation omits notes and closes a broader discovery route.

## The boiling cauldron (aspirational)

The visible KB is the production system. Learning could happen through a background process that continuously proposes mutations:

- **Extract**: pull a claim from a source that hasn't been extracted yet
- **Split**: break a note that makes two claims into two notes
- **Synthesise**: two notes that together imply something neither says alone
- **Relink**: find semantically similar notes that aren't linked
- **Reformulate**: improve a title so it works better as prose when linked
- **Regroup**: a cluster of notes suggests an index that doesn't exist yet
- **Retire**: an automated check, link, or note has outlived its usefulness — candidate signals include zero catches over a declared window, false positives exceeding true positives, a methodology change making it irrelevant, or replacement by a better mechanism

Each mutation would be speculative — staged separately, surfaced for human review only when it scores high enough. This proposal applies [constraining](./definitions/constraining.md) and its reverse direction, relaxing, as an iterative adaptation pattern: the agent proposes mutations while a human still governs their admission.

## Mutations differ on two axes

The boiling cauldron mutations differ on both generality and codifiability:

**By generality:**
- **Extract, reformulate** — narrow scope, improving individual notes (Extract is accumulation — adding knowledge to the store; its value depends on the explanatory-reach of what's extracted)
- **Relink, regroup, synthesise** — medium scope, changing how knowledge connects (these transform accumulated knowledge)
- **Retire, restructure** — wide scope, changing the system's organising principles

**By codifiability** (reliability+speed+cost compound):
- **Codifiable operations** (link checking, section validation, index regeneration) — already automatable as scripts, gaining reliability, speed, and cost simultaneously
- **Judgment operations** (is this claim worth keeping? should these notes merge?) — require LLM or human assessment, may codify later as patterns emerge

Automating narrow-scope improvements is relatively tractable (ingest pipelines, LLM extraction, validation scripts). Automating wide-scope improvements is the hard part — it requires judgment about what principles generalise. Codifiability is a separate axis — often tractable regardless of scope, because the question "can this be made deterministic?" is itself fairly deterministic.

## The vocabulary gap

[Constraining during deployment is already continuous learning](../notes/constraining-during-deployment-is-continuous-learning.md) — developers accumulate informal tweaks, agent memory systems (Claude's memory files, Cursor rules, AGENTS.md conventions) store preferences across sessions, teams version their prompts and tools. But none of it is systematic. Automating the learning loop requires a mechanistic description of the process — what the operations are, how they compose, what makes one succeed or fail. That description requires a vocabulary that doesn't yet exist in standard use: [accumulation](../notes/learning-is-not-only-about-generality.md) as the basic learning operation with [explanatory-reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) as its key property (facts at the low end, theories at the high end), [constraining](./definitions/constraining.md) and source-derived reshaping ([theory and methodology form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md)) as the mechanisms that transform accumulated knowledge, the [generality trade-off](./constraining-and-extraction-both-trade-generality-for-reliability.md) as what they operate on, the [verifiability gradient](./verifiability-gradient.md) as the progression path, and the [fixed-artifact distinction](./exact-implementation-does-not-validate-a-requirement.md) as the reminder that exact artifact-to-requirement conformance does not validate a proxy requirement-to-objective link. Without these distinctions, "make the system learn" is a wish, not a design specification. [Adaptation signals choose pressure; artifact analysis chooses the retained surface](../notes/research/adaptation-agentic-ai-analysis.md) begins to close the gap by separating observed adaptation pressure from the retained artifact surface, authority path, and review evidence that should absorb it.

## Open problems

**Evaluation.** The KB's value is defined by the questions it answers, but those questions evolve with the project. There's no static benchmark to optimise against. Eventually, logging actual usage (queries, failed retrievals, how many hops to an answer) could provide signal — but we don't have enough usage yet to learn from.

**Quality gates.** Structural metrics (PageRank, betweenness centrality, cluster density) are proxies at best. A note can be well-connected because it's vague enough to "relate to" everything. The real test is whether a change helps answer a question that couldn't be answered before — and we don't have a systematic way to measure that yet. The [text testing framework](./text-testing-framework.md) provides quality checks at both the note level (structural contracts, LLM rubric grading) and the corpus level (contradiction detection, coverage and linking behavior, terminology alignment), but these test artifact quality and inter-document consistency, not the graph's end-to-end question-answering capacity. The [quality signals brainstorm](./quality-signals-for-kb-evaluation.md) catalogues graph-topology, content-proxy, and LLM-hybrid signals that could be combined into a composite oracle — addressing this gap by manufacturing a soft oracle from many weak signals rather than waiting for usage data.

**Surfacing rate.** Too many proposals and the human ignores them. Too few and the system isn't learning. Calibrating this requires feedback on what gets accepted, which requires enough volume to learn from.

**Oracle difficulty varies by learning type.** [Pi Self-Learning](../agent-memory-systems/reviews/pi-self-learning.md) uses an LLM to infer mistakes and candidate fixes from session traces, then normalizes and scores lessons before selected material is rendered into automatically injected core memory. Recurrence contributes to rank alongside other signals; it is not a verifier of the inferred lesson or reported fix. The reviewed system supplies neither source-message lineage nor a behavioral ablation showing that injected memory is correct. Pi therefore illustrates that extraction, ranking, and injection can be straightforward while lesson validity remains unresolved. The KB's harder learning problems — "should these notes be linked?", "is this synthesis correct?", "does this index need a new entry?" — have the same need for judgment at a wider scope. The [quality signals brainstorm](./quality-signals-for-kb-evaluation.md) proposes manufacturing a soft oracle from many weak structural signals, but that remains speculative.

**A bounded positive case for automated curation.** [Knowledge-Centric Self-Improvement](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) automates a three-stage curation protocol. It turns task attempts into evidence-grounded local claims, tests cross-task claims through evidence-citing agree/disagree/synthesize discussion, and uses an LLM distiller to select actionable, scoped material into typed bundles of transferable insights, confirmed constraints, rejected hypotheses, pitfalls, checks, and next steps. This demonstrates extraction, cross-claim criticism, synthesis, and selection. It does not establish retirement of previously retained knowledge.

The protocol's oracles are split. Benchmark-specific symbolic evaluators establish attempt outcomes and aggregate solve rates. Forum discussion and the LLM distiller decide which natural-language claims remain actionable and supported; a passing task does not mechanically validate every generalization drawn from it. In the held-out transfer experiment, the generation-10 knowledge asset was frozen and used without new forums or recipient-side distillation on selected Polyglot and ARC-AGI-1 splits. Zero-shot solve rate improved in every reported GPT/Haiku donor–recipient pairing, including both cross-family directions. The artifact was consumed through a task-conditioned adapter.

This is evidence that the automated loop is buildable for benchmark tasks with fixed outcome evaluators and LLM-mediated curation. It does not establish curation for open-ended question-answering, where value is defined by evolving questions and no comparable solve-rate oracle has been supplied. Manufacturing that evaluation remains the open problem.

These cases expose the same unresolved oracle problem: **we lack a validated way to judge whether mutations improve evolving, open-ended KB question-answering.** Usage data could supply part of that signal. Composite structural and LLM signals or task-grounded evaluations are other possible routes, but none is yet validated for this setting. Until one is, manual curation remains the appropriate baseline.

## Connection to codification

The [fixed-artifact distinction](./exact-implementation-does-not-validate-a-requirement.md) applies to links in a reasoning path, not to whole artifact classes. KB infrastructure can conform exactly to adopted requirements for file formats, frontmatter schemas, or script behavior; those requirements can still be proxies for a higher objective such as reliable question-answering. Choices about which links exist, how notes are grouped, and what gets extracted are conjectured requirements for that evolving objective until outcome evidence warrants their scope. A learning loop would continuously test and revise those proxy links while leaving exact conformance checks to validators. We're not ready to build that loop, but the distinction identifies the relations it would need to improve.

---

Relevant Notes:

- [learning is not only about generality](../notes/learning-is-not-only-about-generality.md) — foundation: Simon's definition of learning as capacity change; every KB improvement is learning, the spectrum of generalisation scope shows why automating wide-scope mutations is the hard part
- [constraining](./definitions/constraining.md) — describes the constrain/relax cycle in both human-driven and automated forms (DSPy, ProTeGi); the boiling cauldron is a KB-specific instantiation of that cycle, applying it to note and link mutations rather than prompts and code
- [cludebot](../agent-memory-systems/reviews/cludebot.md) — co-retrieval reinforcement and consolidation passes are concrete mechanisms for the boiling cauldron; cludebot's "need enough query volume" conclusion mirrors the "need usage first" gap here
- [notes-need-quality-scores-to-scale-curation](./notes-need-quality-scores-to-scale-curation.md) — note scoring addresses part of the quality gates problem: composite scores from status, type, inbound links, and recency make automated curation tractable at scale
- [scenario-decomposition-drives-architecture](./scenario-decomposition-drives-architecture.md) — the actual use cases the learning loop's evaluation function would need to optimise against
- [text-testing-framework](./text-testing-framework.md) — quality gates at both note and corpus level that could serve as building blocks for the loop's evaluation, though they test artifact quality and consistency, not end-to-end question-answering capacity
- [quality-signals-for-kb-evaluation](./quality-signals-for-kb-evaluation.md) — addresses the quality gates gap: proposes a composite oracle from graph-topology, content-proxy, and LLM-hybrid signals that could serve as the evaluation function for the boiling cauldron, using structure alone rather than requiring usage data
- [trace-learning techniques in related systems](../agent-memory-systems/trace-learning-techniques-in-related-systems.md) — sharpens: the extraction side of the loop is now concrete in source code across session miners and weight-learning systems; what remains open is evaluation of whether mined candidates deserve durable KB status
- [claw-learning-loops-must-improve-action-capacity-not-just-retrieval](./claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) — extends: argues the retrieval-oriented framing here is one layer of a broader problem; a Claw's learning loop must also improve action capacity (classification, communication, planning)
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — confirms from the other direction: AgeMem shows RL can learn memory-management policy, but only because task completion provides a clear oracle; the KB's evaluation gap (no equivalent oracle) is the real bottleneck, not the learning mechanism
- [Pi Self-Learning](../agent-memory-systems/reviews/pi-self-learning.md) — exemplifies: automates candidate extraction, multi-signal ranking in which recurrence contributes, and injection while leaving lesson validity without a direct verifier
- [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — synthesis: the KB's automation bottleneck is an instance of the general principle that automation stalls where oracle construction stalls
- [Knowledge-Centric Self-Improvement ingest](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) — evidenced-by: an automated task-forum → cross-task-forum → distillation loop with symbolically scored task outcomes and bounded held-out transfer gains; it leaves open-ended KB judgment untouched
- [automated synthesis is missing good oracles](./automated-synthesis-is-missing-good-oracles.md) — develops: the "Synthesise" mutation listed here has a specific bottleneck — generation is easy, evaluation is hard — explored in depth there
