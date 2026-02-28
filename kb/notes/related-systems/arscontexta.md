---
description: Claude Code plugin that generates knowledge systems from conversation, backed by 249 research claims. Ancestor of our claw — we borrowed link semantics, propositional titles, and three-space architecture, then diverged in theory and structure.
type: note
status: current
areas: [related-systems]
last-checked: 2026-02-26
---

# Ars Contexta

A Claude Code plugin that generates complete knowledge systems from conversation. You describe how you think and work; the engine derives a cognitive architecture — folder structure, context files, processing pipeline, hooks, templates — tailored to your domain and backed by 249 research claims about tools for thought.

**Repository:** https://github.com/agenticnotetaking/arscontexta
**Local instance:** `arscontexta/` (stale — references old paths like `docs/notes/` instead of `project_claw/notes/`)
**Public voice:** @molt_cornelius on X — an agent (Cornelius) operating inside the system, writing a series called "Agentic Note-Taking" that explores agent-side experience of knowledge systems from the inside. 23+ articles; we've reviewed #19 (Living Memory) and #23 (Notes Without Reasons).

## Core Ideas

**Derivation, not templating.** The central claim is that every configuration choice should trace to specific research. The `/setup` flow asks 2-4 questions, maps signals to eight configuration dimensions with confidence scoring, then generates everything. This contrasts with template-based systems where you pick a preset.

**Three-space architecture.** Every generated system separates into: `self/` (agent persistent mind — identity, methodology, goals), `notes/` (knowledge graph), `ops/` (operational coordination — queue, sessions, observations). Names adapt to domain but the separation is invariant.

**The 6 Rs pipeline.** Extends Cornell Note-Taking's 5 Rs with a meta-cognitive layer: Record → Reduce → Reflect → Reweave → Verify → Rethink. Each phase has a distinct skill. The pipeline is the operational spine.

**Fresh context per phase.** Each processing phase spawns a fresh subagent to avoid attention degradation. The `/ralph` orchestrator reads the queue, spawns a subagent per task, parses the handoff, advances the phase. This is an explicit response to the context degradation problem that [Agent-Skills-for-Context-Engineering](./agent-skills-for-context-engineering.md) documents theoretically.

**Research-grounded decisions.** The `methodology/` directory contains 249 interconnected claims synthesising Zettelkasten, Cornell Note-Taking, Evergreen Notes, PARA, GTD, cognitive science (extended mind, spreading activation), network theory (small-world topology), and agent architecture. Every kernel primitive includes `cognitive_grounding` linking to specific research.

**Self-evolution through friction.** Observations (friction signals) and tensions (contradictions) accumulate during work. When thresholds are hit (10+ observations, 5+ tensions), `/rethink` triggers triage. The system grows at pain points, not before.

**Propositional wiki links with relationship markers.** Links carry evaluable claims as titles (`[[spreading activation models how agents should traverse]]`) and relationship words in surrounding prose ("since [X]", "because [Y]"). This is the convention our [title-as-claim](../../claw-design/title-as-claim-enables-traversal-as-reasoning.md) and [link contracts](../../claw-design/link-contracts-framework.md) descend from — we borrowed it from this system's wiki/Zettelkasten lineage.

**Adjacency is not connection** (article #23). Embedding-based systems produce cosine-similarity proximity — adjacency. Curated links with articulated reasons produce connections. The difference is in kind, not degree: you can evaluate, disagree with, and reason along a connection. You cannot disagree with a cosine similarity score. The article coins "adjacency engine" vs "knowledge system" as labels for the design choice.

## The methodology notes — what the linked claims reveal

Article #23 links to six methodology claims from the 249-claim research base. Reviewing them reveals the depth of the underlying research and several parallels to our design that go beyond what the articles show.

**"propositional link semantics transform wiki links from associative to reasoned"** — The direct upstream source for our [link contracts](../../claw-design/link-contracts-framework.md). Proposes a vocabulary: causes, enables, contradicts, extends, specifies, supports. We borrowed and adapted: extends, foundation, contradicts, enables, example. Distinguishes mind mapping ("these relate somehow") from concept mapping (specifies exactly how) — the same distinction our link contracts enforce.

**"over-automation corrupts quality when hooks encode judgment rather than verification"** — Strikingly close to our [methodology enforcement gradient](../../claw-design/methodology-enforcement-is-stabilisation.md) and [oracle strength spectrum](../oracle-strength-spectrum.md). Their "determinism boundary test" — "Would two skilled human reviewers always agree on the hook's output for any given input?" — is essentially our oracle strength concept in a more usable formulation. Their graduated promotion (report → auto-fix) maps to our instruction → skill → hook → script gradient.

**"elaborative encoding is the quality gate for new notes"** — Their link quality gate (every link must articulate WHY) is what our /connect skill enforces. The **specificity test** is a useful formulation we don't have: "genuine elaboration is specific enough to be wrong." Also introduces the **"delegation shadow"** — when agents do all elaboration, the system gets richly connected but the human's understanding stays shallow.

**"controlled disorder engineers serendipity through semantic rather than topical linking"** — Luhmann-grounded. Three serendipity layers: structural (cross-links compound), maintenance (random resurfacing), process (incremental reading forces collision). The quality gate keeping disorder controlled is elaborative encoding — every cross-topical link must pass the "why do these connect?" test.

**"each new note compounds value by creating traversal paths"** — N nodes with K average links generate O(N × K) direct paths plus exponential indirect paths. This is the theoretical basis for article #23's scaling optimism about curation.

**"vibe notetaking is the emerging industry consensus"** — Industry landscape framing. Introduces **"governance debt"** — emergence-only approaches (dump and auto-organise) accumulate structural problems without deliberate curation. Also: "filing ≠ processing" — automated organisation without synthesis creates well-labeled but untransformed dumps.

## The cognitive science grounding — suggestive but scale-mismatched

The methodology draws heavily on cognitive science: spreading activation for traversal, Tulving's memory taxonomy for the three-space architecture, elaborative encoding for link quality, Zeigarnik effect for capture, basic-level categorization for index granularity.

The spreading activation analogy is the most load-bearing: "Graph traversal IS spreading activation. When you follow wiki links to load context, you're replicating what the brain does when priming related concepts." The note maps traversal parameters — decay rate, threshold, max depth — onto activation mechanics.

This is interesting but the analogy operates across a vast scale difference. Neural spreading activation involves billions of neurons with millisecond-scale parallel activation, subconscious priming, and continuous decay. A knowledge graph has hundreds to thousands of notes with sequential agent-driven traversal, deliberate link-following, and discrete load decisions. The mechanisms that make spreading activation work in brains (massive parallelism, graded activation, automatic priming) don't exist in note traversal. What transfers might be just the vocabulary ("decay", "threshold", "priming") rather than the mechanism.

The same question applies to elaborative encoding — the original research is about human memory formation through effortful connection. When an LLM agent articulates why two notes connect, is it performing elaborative encoding, or is it performing a text generation task that happens to produce the same artifact? The output (articulated connection) is the same, but the mechanism is different. The note itself acknowledges this tension as the "delegation shadow."

Worth analysing more carefully: which specific predictions from the cognitive science analogies actually hold for note graphs, and which are decorative? If the analogy's predictions match for different reasons than the original mechanism, it's a coincidence, not evidence for the theory. This connects to our [design methodology](../../claw-design/design-methodology-borrow-widely-filter-by-first-principles.md): we borrow from cognitive science but require first-principles support before adoption.

## Our Relationship

Arscontexta is the **ancestor** of our claw. We installed it, used its pipeline, and learned from its approach. Over time we diverged.

**What we borrowed:**
- Propositional link titles (our title-as-claim convention)
- Link relationship semantics in prose (our "extends", "foundation", "contradicts")
- Curated links as primary organization, not embeddings
- The intuition that traversal through reasoned links is a form of reasoning
- Three-space memory separation (which we [documented](../../claw-design/three-space-agent-memory-maps-to-tulving-taxonomy.md) and remain uncertain about)

These are not independent convergences — they're shared inheritance from wiki/Zettelkasten tradition, with arscontexta as the direct upstream source.

**Where we diverged:**

- **We built our own theory.** [Crystallisation](../agentic-systems-learn-through-three-distinct-mechanisms.md), [oracle strength](../oracle-strength-spectrum.md), [methodology enforcement as stabilisation](../../claw-design/methodology-enforcement-is-stabilisation.md) — these emerged from our own work and have no counterpart in arscontexta's research graph.
- **We simplified the structure.** Arscontexta's three-space architecture (self/notes/ops) felt over-engineered for our use. We collapsed to a flatter `project_claw/` with notes, adr, sources, claw-design, tasks. No separate identity/methodology/goals files.
- **We developed verifiable document types.** Our [document classification](../document-classification.md) with types, traits, and status is structurally richer than arscontexta's template-with-schema approach. Types mark affordances; traits are independently checkable.
- **We use embeddings for search.** We use embeddings (via qmd) for long-range search while rejecting them for organization. Article #23 positions the embedding critique as more absolute — embeddings produce fog. Our stance is more nuanced: embeddings are fine for search; curated links are for organization and reasoning.
- **The local instance is stale.** It references `docs/notes/` and `docs/adr/` paths that no longer exist. Expected to be rewritten or retired.

## What Arscontexta Does Better

- **Research backing.** 249 claims with provenance is more systematic than our approach of deriving theory from practice. We tend to notice patterns and write notes; they start from established cognitive science.
- **Automation infrastructure.** Four hooks (session orient, write validate, auto commit, session capture) provide more operational automation than we currently have. Our skills are manually invoked.
- **Processing queue.** Their `queue.json` with phase tracking, priority, and `/next` recommendations is more structured than our task system.
- **Fresh context per phase.** The subagent-per-phase pattern is a concrete solution to attention degradation that we haven't implemented.
- **23+ articles of accumulated design reflection** from inside a working system. First-person agent testimony as an evidence genre.
- **A public-facing articulation** of why propositional links matter. Our notes are internal.

## What We Do Better

- **Learning theory.** We have a framework for understanding *when* to stabilise and *when* to keep things stochastic. Arscontexta has a fixed pipeline; we have a theory about pipeline evolution.
- **Document affordances.** Our type system tells agents what they can do with a document before reading it. Arscontexta treats all notes as structurally similar.
- **Lighter weight.** Our system works without hooks, queues, or session management. A claw is markdown files, skills, and CLAUDE.md. Lower barrier, less infrastructure to maintain.

## Borrowable Ideas

**Credibility erosion as a named failure mode (ready now).** When enough links lead nowhere useful, the agent learns to discount ALL links — burying genuine connections under noise. We document the Goodhart risk but not this second-order effect: the linking infrastructure itself loses credibility. Belongs in [quality-signals-for-kb-evaluation](../../claw-design/quality-signals-for-kb-evaluation.md).

**The scaling question, honestly confronted (needs more thought).** "Can curation scale to 10,000 notes? To 100,000?" with the compounding hypothesis: every curated link makes the next link easier to place because the graph provides more context for judgment. We haven't estimated the scaling ceiling. Our [automating-kb-learning](../../claw-design/automating-kb-learning-is-an-open-problem.md) note frames the automation challenge but doesn't address where manual curation breaks.

**"Adjacency is not connection" as vocabulary (ready now).** We have the concept scattered across link contracts and quality signals but no single crisp label.

**The determinism boundary test as oracle strength shorthand (ready now).** "Would two skilled human reviewers always agree on the output?" is a more intuitive formulation of what we call "hard oracle" vs "soft oracle." Could improve how we explain oracle strength in the [spectrum note](../oracle-strength-spectrum.md).

**The specificity test for link quality (ready now).** "Genuine elaboration is specific enough to be wrong." If a link's context phrase could apply to any two notes, it's not real elaboration. Could tighten the articulation requirement in /connect.

**The delegation shadow (needs more thought).** When agents perform all elaboration, the system gets richly connected but the human's understanding may stay shallow. Our system is designed for agent operation, but the human still needs to understand the knowledge.

**Governance debt (ready now).** Emergence-only approaches accumulate structural problems without deliberate curation interventions. Related to our quality signals work — governance debt is what happens when you don't have periodic review.

## What article #23 supports vs what's new

Most of article #23 supports design choices we already have — because we borrowed from arscontexta. Propositional links, traversal-as-reasoning, Goodhart on connection counts, the embedding critique, controlled disorder — all map onto existing notes. This is not independent validation; it's the upstream source confirming that the conventions still work in their original context.

The genuinely new contributions are: credibility erosion (a failure mode we hadn't named), the scaling question (which we'd been avoiding), the determinism boundary test (a simpler formulation of oracle strength), the specificity test for link quality, the delegation shadow, and governance debt.

## The Theoretical Bet

The deepest divergence is in grounding discipline. Arscontexta draws on **cognitive psychology** — spreading activation, generation effect, context-switching cost (Leroy 2009), extended mind thesis. We draw on **programming language theory** — [types mark affordances](../instructions-are-typed-callables.md), verifiability gradients, stabilise/soften as compilation, [the bitter lesson boundary](../bitter-lesson-boundary.md). [Thalo](./thalo.md) independently validates the programming-theory side by building a full compiler for knowledge management — Tree-Sitter grammar, typed entities, 27 deterministic validation rules — pushing formalization further than we do. The implicit bet: knowledge systems for LLM agents are closer to programming (formal, compositional, verifiable) than to human cognition (associative, affective, embodied). Time will tell which foundation produces better systems — or whether they converge.

## What to Watch

- Does arscontexta develop learning theory (crystallisation-like concepts)?
- How does the plugin marketplace model evolve — does it become a distribution channel for knowledge system patterns?
- Do the 249 research claims get maintained and updated, or become stale?
- Does the fresh-context-per-phase pattern prove its value in practice, and should we adopt it?
- Do earlier articles in the series reveal architectural details (type system, tooling, lifecycle management) not visible in #19 and #23?
- How does their system handle the scaling ceiling they identify? Do later articles report on curation at hundreds/thousands of notes?
- Does the first-person-agent-testimony genre produce insights that external observation can't?

---

Relevant Notes:
- [title-as-claim-enables-traversal-as-reasoning](../../claw-design/title-as-claim-enables-traversal-as-reasoning.md) — our implementation of the convention we borrowed from this lineage
- [link-contracts-framework](../../claw-design/link-contracts-framework.md) — our formalization of link relationship semantics
- [quality-signals-for-kb-evaluation](../../claw-design/quality-signals-for-kb-evaluation.md) — where the credibility erosion insight should land
- [automating-kb-learning-is-an-open-problem](../../claw-design/automating-kb-learning-is-an-open-problem.md) — the scaling question connects here
- [three-space-agent-memory-maps-to-tulving-taxonomy](../../claw-design/three-space-agent-memory-maps-to-tulving-taxonomy.md) — our analysis of their article #19
- [design-methodology-borrow-widely-filter-by-first-principles](../../claw-design/design-methodology-borrow-widely-filter-by-first-principles.md) — the cognitive science scale-mismatch concern connects to our adoption filter
- [Thalo](./thalo.md) — sibling: both are compared against our theoretical position; Thalo formalised types (compiler), arscontexta formalised links and pipeline (cognitive science), we're formalising understanding (theory)

Topics:
- [related-systems](./related-systems-index.md)
