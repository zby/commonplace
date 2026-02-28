---
description: Knowledge systems both inherit human-oriented materials and produce dual-audience documents (human + LLM), making human-LLM cognitive differences a first-class design concern rather than a generic disclaimer
type: note
traits: []
areas: [document-system]
status: seedling
---

# Human-LLM differences are load-bearing for knowledge system design

A knowledge system for LLM agents can't ignore how LLMs differ from humans, but neither can it ignore how they resemble humans. The differences matter practically for two reasons: the system *inherits* materials designed for human consumption, and it *produces* documents that serve both human and LLM readers.

## Reason 1: Inherited materials assume human readers

Knowledge systems don't start from scratch. They draw on existing traditions and materials:

- **Design patterns** borrowed from human knowledge management — Zettelkasten, PKM, library science, Toulmin argumentation — all evolved under selection pressure from human cognition. They assume readers who internalize over time, who fill gaps from background knowledge, who develop intuition through practice.
- **Source materials** ingested into the system — blog posts, papers, methodology descriptions — were written for human readers. Authors assume persistent memory across paragraphs, ability to cross-reference with prior knowledge, tolerance for ambiguity that will be resolved by understanding. An LLM reader gets the tokens but not these affordances.
- **Methodology documentation** that informs system design — research on note-taking, argument structure, knowledge organization — reports findings about human cognitive processes that may or may not apply to LLM text processing.

None of this means the materials are useless. It means each convention needs individual evaluation: *what specific problem does this convention solve, and does the LLM agent have the same problem?* The [failure-mode overlap argument](./human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) demonstrates this methodology — Toulmin structure works for LLMs not because of blind analogy but because LLMs exhibit the specific human-like failures that the structure prevents.

The [design methodology](../claw-design/design-methodology-borrow-widely-filter-by-first-principles.md) note establishes the adoption filter: first principles reasoning is the main gate, programming patterns get a fast pass, everything else earns its way in. But that note addresses *which sources to trust*. The point here is upstream: *why* the filter is necessary. It's necessary because the target system's consumer differs fundamentally from the consumer these traditions were designed for.

## Reason 2: Claw documents serve dual audiences

This is the deeper reason. A note in the knowledge system might be read by:

- A **human** — reviewing the knowledge base, maintaining it, making design decisions, revising skills
- An **LLM agent** — loading the note as context for a task, using it to inform classification, connection, or action

These readers need different things from the same document:

| Need | Human reader | LLM agent reader |
|------|-------------|-----------------|
| Reasoning | Wants to understand *why* — context, trade-offs, alternatives considered | Needs enough reasoning to handle edge cases, but excess reasoning wastes context |
| Completeness | Can fill gaps from background knowledge and experience | Cannot fill gaps — if it's not in the loaded context, it doesn't exist |
| Persistence | Remembers this document next time they encounter the topic | Starts fresh every session — the document must be self-sufficient |
| Navigation | Can browse, skim, and get a "feel" for relevance | Relies on routing tables and descriptions to decide what to load |
| Nuance | Appreciates hedging, qualification, open questions | May perform worse with excessive hedging (reduced instruction clarity) |

The tension is genuine: a document optimized for human understanding (rich reasoning, extensive context, open-ended exploration) may be suboptimal for LLM execution (needs clarity, completeness, directness). A document optimized for LLM execution (imperative, complete, no ambiguity) may be opaque to human maintainers (why does it say this? what's the reasoning?).

The claw's primary response is **tier separation** — methodology notes for reasoning, skills for execution. Since [agent statelessness makes skill layers architectural, not pedagogical](../claw-design/agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md), these tiers serve genuinely different consumers, not different stages of the same learner. A complementary response is **context injection** — the harness [automatically providing referenced context](../claw-design/agent-statelessness-means-harness-should-inject-context-automatically.md) (definitions, ADRs) that a human reader would carry from prior sessions but an LLM agent cannot. Tier separation addresses the writing problem (who is the primary reader?); context injection addresses the loading problem (what must be present for the agent to reason correctly?).

But neither eliminates the tension — they manage it. A methodology note might be loaded by an agent doing a design task. A skill description is read by humans deciding whether to invoke it. Within each tier, the question remains: who is the primary reader?

## What goes wrong without this awareness

**Naive anthropomorphism:** Treating the agent as a "junior colleague who'll learn" or a "student who needs training" bakes in assumptions about internalization, intuition development, and graceful degradation that don't apply. This leads to under-investing in skill completeness ("the agent will figure it out"), under-investing in routing tables ("it'll know where to look"), and treating methodology as sufficient without compilation into skills.

**Naive mechanism-ism:** Treating the agent as "just a text processor" and ignoring human knowledge management traditions is equally wrong. Many human conventions *do* transfer — just not because the mechanisms are the same. [Indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) for different reasons than it's costly for humans (context budget vs. cognitive load), but the design response (resolve at build time) is similar. The right approach evaluates each convention's specific arguments for transfer.

**Audience-blind documents:** Writing without awareness of which audience a document primarily serves produces text that's suboptimal for both. Methodology notes cluttered with imperative instructions confuse the human reasoning process. Skills padded with exploratory reasoning waste the agent's context budget. The [context loading strategy](../claw-design/context-loading-strategy.md) — match specificity to frequency — is one response, but it addresses loading, not writing. The writing side needs its own heuristic: *who is the primary reader of this specific document, and what do they need from it?*

## The methodological claim

The operational principle: **evaluate each human convention individually, checking whether its specific arguments transfer to LLM agents, rather than either wholesale adopting or wholesale rejecting human-oriented designs.** This is more work than either naive position, but it's the only approach that captures the genuine partial overlap between human and LLM cognitive properties.

The specific differences that matter most are developed elsewhere: [agent statelessness](../claw-design/agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md) (no persistent state, no graceful degradation, routing replaces intuition), [indirection costs](./indirection-is-costly-in-llm-instructions.md) (finite context makes every abstraction expensive), and [failure-mode overlap](./human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) (some human structures transfer, but each argument needs independent verification). This note adds the dual-audience observation: even where a convention transfers, the document embodying it may need to serve readers with conflicting needs.

---

Relevant Notes:
- [human writing structures transfer to LLMs because failure modes overlap](./human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) — exemplifies: the methodology of evaluating each human convention's specific arguments for LLM transfer
- [design methodology — borrow widely, filter by first principles](../claw-design/design-methodology-borrow-widely-filter-by-first-principles.md) — foundation: the adoption filter this note motivates; that note says *how* to filter, this note says *why* filtering is necessary
- [agent statelessness makes skill layers architectural, not pedagogical](../claw-design/agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md) — extends: the most consequential specific difference; the tier separation is the primary mechanism for managing dual audiences
- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — example: a specific difference (context budget vs cognitive load) that produces a similar design response (resolve at build time) for different reasons
- [context loading strategy](../claw-design/context-loading-strategy.md) — addresses the loading side of the dual-audience problem; this note identifies the writing side as a separate concern
- [crystallisation: the missing middle](./deploy-time-learning-the-missing-middle.md) — context: the three timescales framing; agent statelessness reframes in-context as "loading" not "learning"
- [agent statelessness means the harness should inject context automatically](../claw-design/agent-statelessness-means-harness-should-inject-context-automatically.md) — complementary response: tier separation addresses writing for different audiences; context injection addresses loading what the agent can't carry from prior sessions

Topics:
- [document-system](./document-system.md)
