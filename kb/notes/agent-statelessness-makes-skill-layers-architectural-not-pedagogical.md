---
description: The methodology→skill relationship is permanent infrastructure for LLM agents, not a learning progression — because agents never internalize, the two tiers serve different consumers (design-time reasoning vs runtime execution) and lossy compilation creates systematic blind spots
type: structured-claim
traits: [has-comparison]
areas: [claw-design]
status: seedling
---

# Agent statelessness makes skill layers architectural, not pedagogical

## Claim

A human who reads methodology and then writes procedures *internalizes* the reasoning. The methodology changes how they think. Eventually they might need neither document — the understanding persists in them. Both the skill and the methodology are external artifacts supporting an internal understanding.

An LLM agent has no persistent internal state. Each session, it's either reading the skill or reading the methodology or reading neither. The two tiers aren't stages of learning (novice → expert) — they're permanent architectural layers. The agent never "graduates" from needing the skill by internalizing the methodology. It will always need one or the other loaded in context.

This makes the relationship between tiers more consequential than in human knowledge systems:

- **For humans:** methodology → skill is a *pedagogical convenience*. You can skip the skill and just understand the methodology deeply enough.
- **For LLM agents:** methodology → skill is an *architectural necessity*. You can't load 15 methodology notes every time the agent needs to connect something. The skill exists because context is finite and expensive.

## Evidence

### The two tiers serve different consumers

If the agent never internalizes methodology, who reads the methodology notes? Two audiences:

1. The **human designer**, for whom methodology provides reasoning, context, and justification
2. The **LLM session that writes or revises skills**, which needs the methodology as source material

This is source code vs. compiled binary. You ship the binary (load the skill at runtime); you maintain the source (read methodology when revising skills). The [context loading strategy](./context-loading-strategy.md) says "match instruction specificity to loading frequency." Agent statelessness explains *why* this is load-bearing rather than merely convenient: the agent cannot compensate for missing specificity by drawing on remembered methodology. If the specific instruction isn't loaded, it doesn't exist.

The two genres have structurally different quality criteria. Methodology notes can be exploratory, tentative, argumentative — they're for reasoning. Skills must be imperative, complete, unambiguous — they're for execution. This isn't a style preference; it follows from the difference in consumer: the methodology reader (human + design-session LLM) has rich context and time to deliberate, while the skill reader (executing LLM) has limited context and must act.

### Skills are prosthetics, not training wheels

For a human, a procedure manual is a transitional object — read, practice, internalize, discard. For an LLM agent, a skill is a permanent prosthetic. The [methodology enforcement as stabilisation](./methodology-enforcement-is-stabilisation.md) note describes a "maturation trajectory" where practices harden from instruction → skill → hook → script. But the *practice* matures; the *agent* never does. The practice hardens; the agent stays exactly as raw as it was on day one.

Design consequence: skills are load-bearing infrastructure, not scaffolding. They need the same engineering discipline as production code — versioned, tested, reviewed. A bug in a skill doesn't self-correct through the agent "learning better" — it produces systematic errors until a human or a maintenance session fixes the artifact.

### Lossy compilation creates systematic blind spots

When a human compresses methodology into a procedure, gaps can be filled by understanding. The human knows *why* each step exists and adapts when circumstances deviate. When a claw compiles methodology into a skill, any reasoning omitted from the skill is permanently unavailable at runtime. The agent follows the skill's letter, not its spirit, because it has no access to the spirit.

This is insidious: a lossy skill works correctly 90% of the time, failing only on edge cases where the omitted reasoning would have mattered. A human using a lossy procedure notices "something feels off" and returns to first principles. An LLM agent has no such signal — it executes confidently within whatever scope the skill provides, unaware of what's missing.

### No graceful degradation

When a human encounters a situation their procedure doesn't cover, they reason from first principles — slower, less confident, but usually adequate. When an LLM agent's loaded context doesn't cover a situation, it falls back on training — which may have no relationship to the claw's methodology. It doesn't degrade into "the same person, but less certain." It degrades into a *different* system — a generic LLM rather than a claw-augmented one.

The human system degrades along a continuum: expert → competent → novice → uncertain. The LLM system has a cliff: claw-augmented → generic. Either the context is loaded or it isn't.

### The routing table replaces learned intuition

An experienced human develops intuition for "what kind of task is this?" and reaches for the right methodology without conscious effort. CLAUDE.md's routing table does exactly this work — pattern-matching situations to capabilities. But unlike human intuition, the routing table doesn't improve through practice. If a skill isn't mentioned in the routing table, the agent won't develop a hunch that it might exist.

Errors in the routing table — missing entries, wrong triggers, ambiguous descriptions — create failures the agent can't self-correct. The human workaround: browse and think "oh, this one looks relevant." The agent workaround doesn't exist unless you explicitly build a "search for relevant skills" meta-capability.

## Reasoning

### The claw learns; the agent doesn't

Since [stabilisation is learning](../notes/agentic-systems-learn-through-three-distinct-mechanisms.md), and since the [crystallisation timescales](../notes/deploy-time-learning-the-missing-middle.md) identify three levels of adaptation (training, in-context, crystallisation), statelessness sharpens both claims: crystallisation isn't just the *best* form of learning available — it's the *only* form. There is no agent-internal learning to complement it. Every improvement that isn't crystallised into an artifact evaporates when the session ends. The investment in crystallisation infrastructure isn't a nice-to-have; it's the entire learning mechanism.

This also reveals that "in-context learning" is a misnomer for agents. The session doesn't *adapt* the agent; it *configures* it. In-context isn't learning at all — it's loading.

### The right metaphors come from systems engineering, not pedagogy

The agent isn't a learner; it's a runtime. The claw isn't a curriculum; it's a deployment environment. The productive metaphors are: compiled vs. source, cached vs. computed, preloaded vs. fetched-on-demand. For why pedagogical metaphors mislead — and why the opposite error (ignoring human traditions entirely) is equally wrong — see [human-LLM differences are load-bearing for knowledge system design](../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md).

## Caveats

- This analysis applies to current LLM architectures. Persistent fine-tuning, retrieval-augmented memory layers, or other future capabilities could change the picture. But even with persistent memory, context window constraints would still make the compilation relationship architecturally necessary.
- The claim is about the *structural* relationship between methodology and skills, not about whether LLMs are "worse" than humans. In some ways the architectural clarity is an advantage — the separation is explicit and maintainable rather than implicit and fragile.
- "No graceful degradation" overstates slightly — an LLM's training may include knowledge relevant to the task, providing some baseline. The point is that this baseline is unpredictable and unrelated to the claw's specific methodology.

## Design implications for claw systems

1. **Skills must be behaviorally complete** within their scope — including enough reasoning for the agent to handle edge cases, and explicit boundaries so the agent recognizes when it's outside the skill's domain.
2. **Methodology notes should be optimized for the skill author**, not the executing agent. The primary consumer is the human or LLM session that writes and revises skills.
3. **The routing table is critical infrastructure**, not a convenience. Invest in its accuracy and completeness with the same rigor as the skills themselves.
4. **Skill maintenance needs a staleness mechanism.** When methodology changes, skills derived from it can silently drift. For humans, outdated procedures get caught by "that doesn't seem right" intuitions. For LLMs, stale skills execute faithfully. The claw needs a way to propagate methodology changes to skills.
5. **In-context "learning" should be reframed as "loading."** This affects how we think about session setup, context budgeting, and what counts as system improvement.

---

Relevant Notes:
- [context-loading-strategy](./context-loading-strategy.md) — foundation: the loading hierarchy this note explains the deep rationale for; "match specificity to frequency" is architecturally necessary, not just convenient
- [methodology-enforcement-is-stabilisation](./methodology-enforcement-is-stabilisation.md) — extends: the stabilisation gradient describes how practices harden; this note adds that the agent never hardens with them
- [crystallisation: the missing middle](../notes/deploy-time-learning-the-missing-middle.md) — foundation: the three timescales; this note argues in-context is really "loading" not "learning" for agents
- [stabilisation is learning](../notes/agentic-systems-learn-through-three-distinct-mechanisms.md) — foundation: Herbert Simon's definition; this note sharpens it — crystallisation is the *only* form of learning available
- [indirection is costly in LLM instructions](../notes/indirection-is-costly-in-llm-instructions.md) — supports: the reason lossy compilation is dangerous — the agent can't resolve omitted reasoning by loading the source at runtime
- [generate instructions at build time](./generate-instructions-at-build-time.md) — example: build-time generation is exactly the source→binary compilation pattern this note describes
- [claw learning is broader than retrieval](./claw-learning-is-broader-than-retrieval.md) — extends: the action-oriented knowledge types (preferences, procedures, precedents) also need the architectural-not-pedagogical treatment
- [human-LLM differences are load-bearing](../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — motivates: the upstream argument for why human-LLM differences matter; develops the dual failure modes (anthropomorphism vs mechanism-ism) that this note's metaphor section points to

Topics:
- [claw-design](./claw-design.md)
