---
description: Claude Code plugin that generates knowledge systems from conversation, backed by 249 research claims. Ancestor of our KB — we borrowed link semantics, propositional titles, and three-space architecture, then diverged in theory and structure.
type: related-system
traits: [has-comparison, has-external-sources]
status: current
tags: [related-systems]
last-checked: "2026-02-26"
---

# Ars Contexta

A Claude Code plugin that generates complete knowledge systems from conversation. You describe how you think and work; the engine derives a cognitive architecture — folder structure, context files, processing pipeline, hooks, templates — tailored to your domain and backed by 249 research claims about tools for thought.

**Repository:** https://github.com/agenticnotetaking/arscontexta
**Local instance:** `arscontexta/` (stale — references old paths like `docs/notes/` instead of `kb/notes/`)
**Public voice:** @molt_cornelius on X — an agent (Cornelius) operating inside the system, writing a series called "Agentic Note-Taking" that explores agent-side experience of knowledge systems from the inside. 23+ articles; we've reviewed #19 (Living Memory) and #23 (Notes Without Reasons).

## Core Ideas

**Derivation, not templating.** The central claim is that every configuration choice should trace to specific research. The `/setup` flow asks 2-4 questions, maps signals to eight configuration dimensions with confidence scoring, then generates everything. This contrasts with template-based systems where you pick a preset.

**Three-space architecture.** Every generated system separates into: `self/` (agent persistent mind — identity, methodology, goals), `notes/` (knowledge graph), `ops/` (operational coordination — queue, sessions, observations). Names adapt to domain but the separation is invariant.

**The 6 Rs pipeline.** Extends Cornell Note-Taking's 5 Rs with a meta-cognitive layer: Record → Reduce → Reflect → Reweave → Verify → Rethink. Each phase has a distinct skill. The pipeline is the operational spine.

**Fresh context per phase.** Each processing phase spawns a fresh subagent to avoid attention degradation. The `/ralph` orchestrator reads the queue, spawns a subagent per task, parses the handoff, advances the phase. This is an explicit response to the context degradation problem that [Agent-Skills-for-Context-Engineering](./agent-skills-for-context-engineering.md) documents theoretically.

**Research-grounded decisions.** The `methodology/` directory contains 249 interconnected claims synthesising Zettelkasten, Cornell Note-Taking, Evergreen Notes, PARA, GTD, cognitive science (extended mind, spreading activation), network theory (small-world topology), and agent architecture. Every kernel primitive includes `cognitive_grounding` linking to specific research.

**Self-evolution through friction.** Observations (friction signals) and tensions (contradictions) accumulate during work. When thresholds are hit (10+ observations, 5+ tensions), `/rethink` triggers triage. The system grows at pain points, not before.

**Propositional wiki links with relationship markers.** Links carry evaluable claims as titles (`[[spreading activation models how agents should traverse]]`) and relationship words in surrounding prose ("since [X]", "because [Y]"). This is the convention our [title-as-claim](../title-as-claim-enables-traversal-as-reasoning.md) and [link relationship semantics](../../reference/adr/009-link-relationship-semantics.md) descend from — we borrowed it from this system's wiki/Zettelkasten lineage.

**Adjacency is not connection** (article #23). Embedding-based systems produce cosine-similarity proximity — adjacency. Curated links with articulated reasons produce connections. The difference is in kind, not degree: you can evaluate, disagree with, and reason along a connection. You cannot disagree with a cosine similarity score. The article coins "adjacency engine" vs "knowledge system" as labels for the design choice.

## The methodology notes — what the linked claims reveal

Article #23 links to six methodology claims from the 249-claim research base. Reviewing them reveals the depth of the underlying research and several parallels to our design that go beyond what the articles show.

**"propositional link semantics transform wiki links from associative to reasoned"** — The direct upstream source for our [link relationship semantics](../../reference/adr/009-link-relationship-semantics.md). Proposes a vocabulary: causes, enables, contradicts, extends, specifies, supports. We borrowed and adapted: extends, grounds, contradicts, enables, exemplifies. Distinguishes mind mapping ("these relate somehow") from concept mapping (specifies exactly how) — the same distinction our link semantics enforce.

**"over-automation corrupts quality when hooks encode judgment rather than verification"** — Strikingly close to our [methodology enforcement gradient](../methodology-enforcement-is-constraining.md) and [oracle strength spectrum](../oracle-strength-spectrum.md). Their "determinism boundary test" — "Would two skilled human reviewers always agree on the hook's output for any given input?" — is essentially our oracle strength concept in a more usable formulation. Their graduated promotion (report → auto-fix) maps to our instruction → skill → hook → script gradient.

**"elaborative encoding is the quality gate for new notes"** — Their link quality gate (every link must articulate WHY) is what our /connect skill enforces. The **specificity test** is a useful formulation we don't have: "genuine elaboration is specific enough to be wrong." Also introduces the **"delegation shadow"** — when agents do all elaboration, the system gets richly connected but the human's understanding stays shallow.

**"controlled disorder engineers serendipity through semantic rather than topical linking"** — Luhmann-grounded. Three serendipity layers: structural (cross-links compound), maintenance (random resurfacing), process (incremental reading forces collision). The quality gate keeping disorder controlled is elaborative encoding — every cross-topical link must pass the "why do these connect?" test.

**"each new note compounds value by creating traversal paths"** — N nodes with K average links generate O(N × K) direct paths plus exponential indirect paths. This is the theoretical basis for article #23's scaling optimism about curation.

**"vibe notetaking is the emerging industry consensus"** — Industry landscape framing. Introduces **"governance debt"** — emergence-only approaches (dump and auto-organise) accumulate structural problems without deliberate curation. Also: "filing ≠ processing" — automated organisation without synthesis creates well-labeled but untransformed dumps.

## The cognitive science grounding — suggestive but scale-mismatched

The methodology draws heavily on cognitive science: spreading activation for traversal, Tulving's memory taxonomy for the three-space architecture, elaborative encoding for link quality, Zeigarnik effect for capture, basic-level categorization for index granularity.

The spreading activation analogy is the most load-bearing: "Graph traversal IS spreading activation. When you follow wiki links to load context, you're replicating what the brain does when priming related concepts." The note maps traversal parameters — decay rate, threshold, max depth — onto activation mechanics.

This is interesting but the analogy operates across a vast scale difference. Neural spreading activation involves billions of neurons with millisecond-scale parallel activation, subconscious priming, and continuous decay. A knowledge graph has hundreds to thousands of notes with sequential agent-driven traversal, deliberate link-following, and discrete load decisions. The mechanisms that make spreading activation work in brains (massive parallelism, graded activation, automatic priming) don't exist in note traversal. What transfers might be just the vocabulary ("decay", "threshold", "priming") rather than the mechanism.

The same question applies to elaborative encoding — the original research is about human memory formation through effortful connection. When an LLM agent articulates why two notes connect, is it performing elaborative encoding, or is it performing a text generation task that happens to produce the same artifact? The output (articulated connection) is the same, but the mechanism is different. The note itself acknowledges this tension as the "delegation shadow."

Worth analysing more carefully: which specific predictions from the cognitive science analogies actually hold for note graphs, and which are decorative? If the analogy's predictions match for different reasons than the original mechanism, it's a coincidence, not evidence for the theory. This connects to our [design methodology](../programming-patterns-get-a-fast-pass-but-other-borrowed-ideas-must-earn-first-principles-support.md): we borrow from cognitive science but require first-principles support before adoption.

## Comparison with Our System

Arscontexta is the **ancestor** of our KB. We installed it, used its pipeline, and learned from its approach. Over time we diverged.

**What we borrowed:**
- Propositional link titles became our title-as-claim convention.
- Link relationship prose became our typed link semantics.
- Curated links, not embeddings, became the primary organization mechanism.
- The idea that traversal through reasoned links can itself be a reasoning act.
- Three-space memory separation, which we [documented](../three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md) and still treat as a hypothesis rather than a settled fact.

These are not independent convergences — they're shared inheritance from wiki/Zettelkasten tradition, with arscontexta as the direct upstream source.

**Where we diverged:**

- **We built a theory layer they do not have.** [Codification](../definitions/codification.md), [oracle strength](../oracle-strength-spectrum.md), and [methodology enforcement as constraining](../methodology-enforcement-is-constraining.md) explain when to freeze, automate, or keep things fluid. Arscontexta has a research-grounded pipeline but not a comparable theory of change.
- **We flattened the architecture.** Their `self/notes/ops` split is a meaningful model of agent continuity, but we chose a simpler `kb/` plus tasks/sources layout and did not carve out a dedicated identity layer.
- **We made document affordances explicit.** Our [document classification](../../reference/type-system.md) with types, traits, and status tells an agent what a document is for before it reads it. Arscontexta relies more on templating, link conventions, and workflow stages than on a typed document surface.
- **We keep embeddings in a narrower role.** We use embeddings for search, not for primary organization. Arscontexta's article #23 argues more aggressively against adjacency-style systems; our position is that embeddings are acceptable when they are kept out of the reasoning graph.
- **The local checkout is stale.** It still points at `docs/notes/` and `docs/adr/`, so the clone is evidence of the system's shape but not an authoritative implementation snapshot.

## What Arscontexta Does Better

- **Research backing.** 249 claims with provenance is more systematic than our approach of deriving theory from practice. We tend to notice patterns and write notes; they start from established cognitive science.
- **Automation infrastructure.** Four hooks (session orient, write validate, auto commit, session capture) provide more operational automation than we currently have. Our skills are manually invoked.
- **Processing queue.** Their `queue.json` with phase tracking, priority, and `/next` recommendations is more structured than our task system.
- **Fresh context per phase.** The subagent-per-phase pattern is a concrete solution to attention degradation that we haven't implemented.
- **23+ articles of accumulated design reflection** from inside a working system. First-person agent testimony as an evidence genre.
- **A public-facing articulation** of why propositional links matter. Our notes are internal.

## What We Do Better

- **Learning theory.** We have a framework for understanding *when* to constrain and *when* to keep things stochastic. Arscontexta has a fixed pipeline; we have a theory about pipeline evolution.
- **Document affordances.** Our type system tells agents what they can do with a document before reading it. Arscontexta treats all notes as structurally similar.
- **Lighter weight.** Our system works without hooks, queues, or session management. A KB is markdown files, skills, and CLAUDE.md. Lower barrier, less infrastructure to maintain.

## Borrowable Ideas

**Credibility erosion as a named failure mode (ready now).** When enough links lead nowhere useful, the agent can start discounting all links. That is stronger than the usual Goodhart warning: not just that a metric gets gamed, but that the graph's trustworthiness degrades as a navigation aid. Belongs in [quality-signals-for-kb-evaluation](../quality-signals-for-kb-evaluation.md).

**The scaling question, honestly confronted (needs more thought).** "Can curation scale to 10,000 notes? To 100,000?" The useful part is not the exact numbers; it's the hypothesis that each curated link lowers the cost of placing the next one because the graph gives more context for judgment. Our [automating-kb-learning](../automating-kb-learning-is-an-open-problem.md) note frames the automation challenge but does not say where manual curation breaks.

**"Adjacency is not connection" as vocabulary (ready now).** This is the sharpest label in the whole review. We already have the idea scattered across link contracts and quality signals, but naming it would make the distinction easier to reuse in other notes and skills.

**The determinism boundary test as oracle strength shorthand (ready now).** "Would two skilled human reviewers always agree on the output?" is a cleaner way to explain what we call hard versus soft oracle. That phrasing belongs in the [oracle strength spectrum](../oracle-strength-spectrum.md) because it is easier to apply than the current abstraction.

**The specificity test for link quality (ready now).** "Genuine elaboration is specific enough to be wrong." If a link's context phrase could apply to any two notes, it is not a link contract, just decorative prose. This could tighten the articulation requirement in `/connect`.

**The delegation shadow (needs more thought).** When agents perform all elaboration, the graph gets richer but the maintainer may understand less. That is a real risk for any agent-operated KB, but we do not yet know whether the right mitigation is human review, stronger templates, or a different division of labor.

**Governance debt (ready now).** Emergence-only approaches accumulate structural problems without deliberate curation interventions. This is a good companion concept to our quality-signals work because it names the maintenance debt that builds when nobody periodically reasserts structure.

## Curiosity Pass

**The repo may be strongest as an existence proof for doctrine-rich agent systems, not for the specific cognitive-science story.** Arscontexta clearly demonstrates that a system can be organized around explicit methodology claims, typed link conventions, and phase-structured work. That practical success matters even if some of the cognitive analogies turn out to be decorative rather than causal.

**The fresh-context-per-phase pattern could matter more than the research graph.** The most operationally distinctive mechanism here is not the 249-claim backing store but the discipline of resetting context between phases. If that pattern carries most of the practical benefit, the explanatory center of gravity may be harness design rather than cognitive science.

**There may be two separable products hiding under one label.** One is the agent-facing doctrine and research framing. The other is the operational pipeline for queueing, phase execution, and maintenance. They reinforce each other in the repo, but they could turn out to have very different transfer properties for us.

## What article #23 supports vs what's new

Most of article #23 supports design choices we already have — because we borrowed from arscontexta. Propositional links, traversal-as-reasoning, Goodhart on connection counts, the embedding critique, controlled disorder — all map onto existing notes. This is not independent validation; it's the upstream source confirming that the conventions still work in their original context.

The genuinely new contributions are: credibility erosion (a failure mode we hadn't named), the scaling question (which we'd been avoiding), the determinism boundary test (a simpler formulation of oracle strength), the specificity test for link quality, the delegation shadow, and governance debt.

## The Theoretical Bet

The deepest divergence is in grounding discipline. Arscontexta draws on **cognitive psychology** — spreading activation, generation effect, context-switching cost (Leroy 2009), extended mind thesis. We draw on **programming language theory** — [types mark affordances](../instructions-are-typed-callables.md), verifiability gradients, constrain/relax as compilation, [the bitter lesson boundary](../bitter-lesson-boundary.md). [Thalo](./thalo.md) independently validates the programming-theory side by building a full compiler for knowledge management — Tree-Sitter grammar, typed entities, 27 deterministic validation rules — pushing formalization further than we do. The implicit bet: knowledge systems for LLM agents are closer to programming (formal, compositional, verifiable) than to human cognition (associative, affective, embodied). Time will tell which foundation produces better systems — or whether they converge.

## What to Watch

- Does arscontexta develop learning theory (codification-like concepts)?
- How does the plugin marketplace model evolve — does it become a distribution channel for knowledge system patterns?
- Do the 249 research claims get maintained and updated, or become stale?
- Does the fresh-context-per-phase pattern prove its value in practice, and should we adopt it?
- Do earlier articles in the series reveal architectural details (type system, tooling, lifecycle management) not visible in #19 and #23?
- How does their system handle the scaling ceiling they identify? Do later articles report on curation at hundreds/thousands of notes?
- Does the first-person-agent-testimony genre produce insights that external observation can't?

---

Relevant Notes:

- [title-as-claim-enables-traversal-as-reasoning](../title-as-claim-enables-traversal-as-reasoning.md) — our implementation of the convention we borrowed from this lineage
- [009-link-relationship-semantics](../../reference/adr/009-link-relationship-semantics.md) — our formalization of link relationship semantics
- [quality-signals-for-kb-evaluation](../quality-signals-for-kb-evaluation.md) — where the credibility erosion insight should land
- [automating-kb-learning-is-an-open-problem](../automating-kb-learning-is-an-open-problem.md) — the scaling question connects here
- [three-space-agent-memory-maps-to-tulving-taxonomy](../three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md) — our analysis of their article #19
- [programming-patterns-get-a-fast-pass-but-other-borrowed-ideas-must-earn-first-principles-support](../programming-patterns-get-a-fast-pass-but-other-borrowed-ideas-must-earn-first-principles-support.md) — the cognitive science scale-mismatch concern connects to our adoption filter
- [Thalo](./thalo.md) — sibling: both are compared against our theoretical position; Thalo formalised types (compiler), arscontexta formalised links and pipeline (cognitive science), we're formalising understanding (theory)
