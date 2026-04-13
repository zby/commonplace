---
description: TypeScript memory system for AI agents with scored observations, session handoffs, and reflection pipelines — has a working workshop layer where we have theory, making it the strongest source of borrowable patterns for ephemeral knowledge
type: agent-memory-system-review
traits: [has-comparison, has-external-sources]
status: outdated
tags: []
last-checked: "2026-02-26"
---

# ClawVault

> Replaced 2026-04-12. See [clawvault](./clawvault.md) for the current review.

**A structured memory system for AI agents** that uses markdown as the storage primitive. Solves "context death" (agents losing context between sessions) through checkpoints, handoffs, and observation pipelines.

**Repository:** https://github.com/nickarummel/clawvault
**Status:** v2.6.1, 466 tests, 20+ PRs from external contributors, TypeScript/Node.js

## Core Ideas

**Session lifecycle as a first-class problem.** ClawVault's central contribution is treating context death not as an inconvenience but as the defining constraint. The wake/sleep/checkpoint/recover cycle makes session boundaries explicit and survivable:

```
wake → checkpoint* → sleep → [recovery if crash] → recap → wake
```

Each transition produces artifacts: handoff documents capture "what was I doing, what's next, what's blocked," checkpoints snapshot mid-session state, recovery detects context death and restores from the last good state. These are exactly the [workshop layer](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) artifacts our design notes say we need but haven't built.

**Scored observations with promotion.** Observations extracted from sessions carry structured metadata:

```
- [decision|c=0.9|i=0.85] Use PostgreSQL for persistence
- [lesson|c=0.8|i=0.6] Context death is survivable with checkpointing
- [preference|c=0.7|i=0.4] Prefer TypeScript for type safety
```

The type taxonomy — decision, lesson, preference, commitment, fact, relationship — maps directly to what [claw learning loops must improve action capacity not just retrieval](../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) calls "action-oriented knowledge types": preferences, procedures, judgment precedents. They have concrete types for things we've identified theoretically but not structured.

**Promotion by recurrence.** Importance thresholds drive what gets promoted to permanent vault knowledge:
- **structural** (i >= 0.8): auto-promotes
- **potential** (i >= 0.4): promotes if seen on 2+ different dates
- **contextual** (i < 0.4): reference only

The "seen twice on different dates" heuristic is simple and testable — a concrete mechanism for the text-to-seedling transition that we currently handle through pure human judgment.

**Observation-reflection-promotion pipeline.** Weekly reflection reviews accumulated observations, extracts durable insights, promotes to vault categories. This is a working implementation of the [boiling cauldron](../../notes/automating-kb-learning-is-an-open-problem.md) mutations (extract, synthesise, regroup) that we describe as an open problem.

## Borrowable Ideas

**1. Session handoff documents.** The clearest immediate borrow. A stable end-of-session record for what was in progress, what is blocked, and what should happen next would close a gap we still leave to ad hoc judgment. This belongs in the workshop layer, alongside tasks, not in durable notes.

**2. Observation capture with type taxonomy.** Our `kb/log.md` already records one-line observations, but without a shared vocabulary the entries stay flat. ClawVault's decision/lesson/preference/commitment labels are useful because they tell later triage what kind of thing was observed, not just that something happened.

**3. Promotion by recurrence.** The recurrence heuristic is useful as a low-cost filter, not as a final judge. If the same point shows up across sessions, that is evidence it deserves promotion review. That is a plausible first gate for our log, but only if we keep it clearly advisory.

**4. The reflection cycle as a skill.** Their weekly `reflect` command is worth borrowing as a manual or semi-manual review rhythm even before automation. Periodic review of recent observations and notes would surface patterns, contradictions, and promotion candidates that otherwise decay in the log.

**5. Retrieval codification patterns (needs more data).** ClawVault's KB-area patterns — injection triggers, retrieval profiles, context frontloading — look like a codified retrieval ladder:

- **Triggers** in frontmatter (`triggers: ["deployment", "rollback"]`) — codified retrieval conditions on individual artifacts. The knowledge becomes self-routing: instead of the agent needing to find it, the system knows when to surface it.
- **Profiles** (`planning`, `incident`, `handoff`) — codified retrieval strategies for classes of tasks. Someone observed "during incident response, recent observations matter most" and hardened that into a named strategy.
- **Full frontloading** — codified context assembly. The system pre-loads a curated package before the agent even starts.

Each step encodes more retrieval judgment into the system and removes more from the agent. That is only worth adopting if the pattern has already proven itself through repeated use. We do not yet know which notes should have triggers, what retrieval profiles our work actually needs, or whether frontloading would help or just burn context. ClawVault has the usage volume to discover that empirically; we are still early enough that this should remain a candidate pattern, not a default.

## What We Should Not Borrow (Yet)

**LLM-heavy automation.** Their compression, fact extraction, and injection pipelines all run through LLMs. This adds capability but also opacity — you can't easily tell why something was promoted or what was lost in compression. We want to understand the fundamental patterns before automating them. The [verifiability gradient](../../notes/verifiability-gradient.md) matters here: automating a process before understanding it locks in assumptions.

**The 8 primitives taxonomy.** Goals, Agents, State Space, Feedback, Capital, Institution, Synthesis, Recursion — this is a framework that organises their features, but it's unclear whether these are fundamental categories or a retroactive grouping of what they happened to build. We'd rather discover our categories from practice.

**The specific scoring format.** Confidence and importance as floats (c=0.9, i=0.85) implies a precision that LLM extraction can't actually deliver. The buckets (structural/potential/contextual) are more honest than the numbers. If we adopt anything here, it should be the buckets, not the scores.

## Comparison with Our System

**Frontloaded context vs. agent-driven retrieval.** ClawVault pre-assembles context before the agent starts work. Their `context` command gathers from five sources, scores and deduplicates them, caps per source by profile, fits a token budget, and injects the result into the prompt. A `session:start` hook can also auto-inject results. The agent gets a curated package.

Our approach — [instruction specificity should match loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md) — takes the opposite tack: load CLAUDE.md at startup, then trust the agent to navigate and fetch the rest. Progressive disclosure, not preassembly. The trade-off is sharp: frontloading reduces first-turn friction but has to guess relevance in advance; agent-driven retrieval is cheaper to scale and more precise, but only if the agent can navigate well.

**They operationalized the workshop; we are still defining it.** ClawVault already has concrete artifacts for session lifecycle, checkpoints, handoffs, observations, and reflection. Our notes describe the need for a workshop layer and the kinds of artifacts it should hold, but we have not committed to this particular shape. That makes their pipeline a stronger operational reference than a theory reference.

**Human-in-the-loop vs. agent-driven.** Their promotion pipeline is largely automated: LLMs extract, score, and route observations, while recurrence heuristics decide what rises. Our model still keeps humans in the promotion loop. That means ClawVault is better evidence about what an automated curation loop can actually sustain, but also a stronger warning about opacity and score inflation.

**No learning theory.** Like [Thalo](./thalo.md), ClawVault has no framework for deciding when to formalise something versus leave it fluid. No [verifiability gradient](../../notes/verifiability-gradient.md), no constrain/relax boundary. The structure is designed; it does not explain its own maturation. That is the gap between an effective workflow and a theory of why the workflow should change over time.

## Curiosity Pass

**The strongest claim here is operational, not theoretical.** ClawVault is interesting because it actually runs a workshop loop with handoffs, checkpoints, observations, and reflection. That makes it a useful answer to the "what does the middle layer look like?" question, even if its scoring and extraction choices remain somewhat opaque.

**The recurrence heuristic is valuable mainly because it is inspectable.** "Seen twice on different dates" is crude, but that crudeness is a feature: it creates a transparent promotion threshold that can be challenged or replaced later. The important question is whether that cheap signal catches the right candidates without flooding the durable store.

**There are two separable gains in the system.** One is artifact structure: session handoffs, observation labels, and reflection rhythm. The other is automation: preloaded context, scoring, and routing. If we borrow from ClawVault, we should be clear about which gain we are borrowing, because they do not transfer together.

## What to Watch

- Does promotion by recurrence actually surface the right things? Their system has enough usage to generate evidence.
- How do handoff documents evolve over time — do they converge on a stable structure, or do they stay heterogeneous?
- Does the observation type taxonomy (decision, lesson, preference, commitment) hold up, or do new types emerge that break the categories?
- How does the system handle contradictory observations (high-confidence entries that conflict)?

---

Relevant Notes:

- [a-functioning-kb-needs-a-workshop-layer](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — foundation: ClawVault's observations, handoffs, and reflections are concrete workshop artifacts where we have only the theoretical need
- [claw-learning-loops-must-improve-action-capacity-not-just-retrieval](../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) — foundation: ClawVault's observation types (decision, preference, lesson) are concrete implementations of the action-oriented knowledge types this note identifies as missing
- [automating-kb-learning-is-an-open-problem](../../notes/automating-kb-learning-is-an-open-problem.md) — extends: ClawVault's reflection pipeline is a working (if LLM-heavy) implementation of the boiling cauldron mutations
- [deploy-time-learning](../../notes/deploy-time-learning-is-the-missing-middle.md) — contrasts: ClawVault automates promotion without a theory of when automation is premature; their results would test whether early automation helps or locks in assumptions
- [Always-loaded context has two surfaces with different affordances](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) — contrasts: ClawVault frontloads context via profiles and injection; our two always-loaded surfaces use progressive disclosure with agent-driven retrieval — different bets on whether the system or the agent should decide what's relevant
- [Thalo](./thalo.md) — sibling: both are compared against our theoretical position; Thalo formalised types (compiler), ClawVault formalised lifecycle (pipeline), we're formalising understanding (theory)
- [Siftly](./siftly.md) — extends: another staged pipeline reference, but optimized for deterministic ingest throughput and resumable source loading
