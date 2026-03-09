---
description: Agents never develop navigation intuition — every session is day one — so all knowledge routing infrastructure (skills, type templates, routing tables, naming conventions, activation triggers) is permanent architecture, not scaffolding that learners outgrow
type: note
traits: [has-comparison]
areas: [kb-design]
status: current
---

# Agent statelessness makes routing architectural, not learned

A human developer who works in a knowledge base gradually builds intuition: "for this kind of task, look here." They learn which wiki page covers authentication, which convention governs naming, which template fits a design note. Eventually they navigate without conscious effort.

An LLM agent never does this. Each session starts cold. It cannot learn "last time I needed the structured-claim template, I found it in `notes/types/`." It cannot develop a hunch that a relevant skill might exist. Every session is day one.

This means every mechanism that directs the agent to the right knowledge at the right time — routing tables, skill descriptions, type templates, naming conventions, directory structure, activation triggers, area indexes — is permanent architecture. For a human, these are conveniences you outgrow. For an agent, they're prosthetics you never stop needing.

The [methodology enforcement](./methodology-enforcement-is-stabilisation.md) gradient describes practices hardening from instruction → skill → hook → script. The *practices* mature. The *agent* stays exactly as raw as it was on day one. This asymmetry is the core of the note: the system learns, the agent doesn't.

## Progressive disclosure replaces navigation intuition

A human holds an approximate mental model of the whole knowledge base. An agent can only hold what's loaded. Since [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md), you can't load everything — so you must route to the right layer at the right time. In this KB, the loading hierarchy is our concrete progressive disclosure system:

1. **CLAUDE.md** loads unconditionally — the agent always knows where to route
2. **Skill descriptions** load cheaply — the agent decides whether to load the full skill
3. **Skill bodies** load on activation — imperative instructions for the current task
4. **Type templates** load per directory — structural guidance matching the destination
5. **Methodology notes** load on demand — deep reasoning for edge cases

Each layer filters what the agent needs to consider, and each layer must route correctly to the next. A gap at any level creates unreachable knowledge.

## The degradation cliff

When a human encounters a situation their routing aids don't cover, they reason from experience — slower, less confident, but adequate. They notice "something feels off" and search more broadly.

An agent has no equivalent signal. When its loaded context doesn't cover a situation, it falls back on training — which may have no relationship to the KB's methodology. It doesn't degrade into "the same agent, but less certain." It degrades into a *different* system — a generic LLM rather than a KB-augmented one. The human system degrades along a continuum: expert → competent → novice → uncertain. The agent system has a cliff: KB-augmented → generic.

This makes every omission in routing infrastructure dangerous. A routing table missing an entry means the agent doesn't know the destination exists. A skill omitting edge-case reasoning produces confident execution with systematic errors. A naming convention not followed makes the note unfindable. The agent executes confidently within whatever scope is loaded, unaware of what wasn't routed to it.

## Source vs. compiled

The cliff creates a maintenance discipline: routing artifacts must stay in sync with methodology, because the agent can't bridge the gap when they drift apart.

Methodology notes are source code. Skills, routing tables, type templates, and naming conventions are compiled artifacts. You maintain the source (read methodology when revising routing); you ship the binary (load routing artifacts at runtime). The [context loading strategy](./context-loading-strategy.md) says "match instruction specificity to loading frequency." Agent statelessness explains *why* this is load-bearing: the agent cannot compensate for missing specificity by drawing on remembered methodology. If the specific routing isn't loaded, it doesn't exist.

The two genres have structurally different quality criteria. Source can be exploratory, tentative, argumentative — it's for reasoning. Compiled artifacts must be imperative, complete, unambiguous — they're for execution. The methodology reader has rich context and time to deliberate; the routing consumer has limited context and must act. The agent isn't a learner; it's a runtime. The KB isn't a curriculum; it's a deployment environment. (The [human-LLM differences](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) note develops why both pedagogical and purely mechanistic metaphors mislead here.)

## Design consequences

Three requirements follow:

1. **Engineering discipline.** Routing infrastructure needs the same treatment as production code — versioned, tested, reviewed.
2. **Staleness detection.** When methodology changes, routing artifacts derived from it silently drift. The agent has no "that doesn't seem right" intuition to catch it. Some mechanism — diffing, periodic audit, dependency tracking — must detect when compiled routing has diverged from its source.
3. **Behavioral completeness.** Each routing artifact must include enough reasoning for edge cases and explicit boundaries so the agent recognizes when it's outside scope. Partial routing produces confident execution with systematic errors — worse than no routing at all.

Persistent memory across sessions would soften the statelessness assumption, but routing scales with the knowledge base itself. Even an agent that remembers where it found things last time faces a navigation problem proportional to KB size.

---

Relevant Notes:

- [context-loading-strategy](./context-loading-strategy.md) — foundation: the loading hierarchy this note explains the deep rationale for; "match specificity to frequency" is architecturally necessary, not just convenient
- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — foundation: why progressive disclosure exists; routing is the mechanism that makes context efficiency achievable
- [methodology-enforcement-is-stabilisation](./methodology-enforcement-is-stabilisation.md) — extends: the stabilisation gradient describes how practices harden; this note adds that the agent never hardens with them
- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — supports: the reason lossy routing is dangerous — the agent can't resolve omitted reasoning by loading the source at runtime
- [generate instructions at build time](./generate-instructions-at-build-time.md) — example: build-time generation is exactly the source→compiled pattern this note describes
- [skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) — instance: the skill-specific case of routing-as-architecture; distillation is the compilation pattern applied to methodology→skill
- [claw learning is broader than retrieval](./claw-learning-is-broader-than-retrieval.md) — extends: the action-oriented knowledge types (preferences, procedures, precedents) also need routing-as-architecture treatment
- [human-LLM differences are load-bearing](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — motivates: the upstream argument for why human-LLM differences matter; develops the dual failure modes (anthropomorphism vs mechanism-ism) that this note's metaphor section points to
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — enables: frontloading is the primary technique for making routing work within context constraints

Topics:

- [kb-design](./kb-design.md)
