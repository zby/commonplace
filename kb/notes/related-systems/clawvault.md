---
description: TypeScript memory system for AI agents with scored observations, session handoffs, and reflection pipelines — has a working workshop layer where we have theory, making it the strongest source of borrowable patterns for ephemeral knowledge
type: note
status: current
areas: [related-systems]
last-checked: 2026-02-26
---

# ClawVault

**A structured memory system for AI agents** that uses markdown as the storage primitive. Solves "context death" (agents losing context between sessions) through checkpoints, handoffs, and observation pipelines.

**Repository:** https://github.com/nickarummel/clawvault
**Status:** v2.6.1, 466 tests, 20+ PRs from external contributors, TypeScript/Node.js

## Core Ideas

**Session lifecycle as a first-class problem.** ClawVault's central contribution is treating context death not as an inconvenience but as the defining constraint. The wake/sleep/checkpoint/recover cycle makes session boundaries explicit and survivable:

```
wake → checkpoint* → sleep → [recovery if crash] → recap → wake
```

Each transition produces artifacts: handoff documents capture "what was I doing, what's next, what's blocked," checkpoints snapshot mid-session state, recovery detects context death and restores from the last good state. These are exactly the [workshop layer](../../claw-design/a-functioning-claw-needs-a-workshop-layer-not-just-a-library.md) artifacts our design notes say we need but haven't built.

**Scored observations with promotion.** Observations extracted from sessions carry structured metadata:

```
- [decision|c=0.9|i=0.85] Use PostgreSQL for persistence
- [lesson|c=0.8|i=0.6] Context death is survivable with checkpointing
- [preference|c=0.7|i=0.4] Prefer TypeScript for type safety
```

The type taxonomy — decision, lesson, preference, commitment, fact, relationship — maps directly to what [claw learning is broader than retrieval](../../claw-design/claw-learning-is-broader-than-retrieval.md) calls "action-oriented knowledge types": preferences, procedures, judgment precedents. They have concrete types for things we've identified theoretically but not structured.

**Promotion by recurrence.** Importance thresholds drive what gets promoted to permanent vault knowledge:
- **structural** (i >= 0.8): auto-promotes
- **potential** (i >= 0.4): promotes if seen on 2+ different dates
- **contextual** (i < 0.4): reference only

The "seen twice on different dates" heuristic is simple and testable — a concrete mechanism for the text-to-seedling transition that we currently handle through pure human judgment.

**Observation-reflection-promotion pipeline.** Weekly reflection reviews accumulated observations, extracts durable insights, promotes to vault categories. This is a working implementation of the [boiling cauldron](../../claw-design/automating-kb-learning-is-an-open-problem.md) mutations (extract, synthesise, regroup) that we describe as an open problem.

## What We Could Borrow

**1. Session handoff documents.** The most immediately useful pattern. A structured format for end-of-session state capture — what was in progress, what's blocked, what should happen next. We have no mechanism for this. The handoff artifact type could live in the workshop layer alongside tasks.

**2. Observation capture with type taxonomy.** Our `kb/log.md` accepts one-line observations appended during traversal. ClawVault's observation types (decision, lesson, preference, commitment) give agents a vocabulary for what they're recording. Even just "what kind of thing is this?" as a prefix convention in the log would improve discoverability and later triage.

**3. Promotion by recurrence.** A cheap signal for what matters: if the same insight surfaces across multiple sessions, it's probably worth promoting. This could be a heuristic for reviewing the log — check whether similar observations already exist, and if so, flag for promotion.

**4. The reflection cycle as a skill.** Their weekly `reflect` command reviews recent observations and produces a synthesis. This could be a `/reflect` skill for us — periodic review of the log and recent notes to surface patterns, contradictions, and promotion candidates. Lower-ceremony than their automated pipeline, but the practice itself is valuable.

**5. Retrieval crystallisation patterns (needs more data).** ClawVault's KB-area patterns — injection triggers, retrieval profiles, context frontloading — are interesting not as retrieval mechanisms but as a [crystallisation](../deploy-time-learning-the-missing-middle.md) spectrum for how knowledge gets surfaced:

- **Triggers** in frontmatter (`triggers: ["deployment", "rollback"]`) — crystallised retrieval conditions on individual artifacts. The knowledge becomes self-routing: instead of the agent needing to find it, the system knows when to surface it.
- **Profiles** (`planning`, `incident`, `handoff`) — crystallised retrieval strategies for classes of tasks. Someone observed "during incident response, recent observations matter most" and hardened that into a named strategy.
- **Full frontloading** — crystallised context assembly. The system pre-loads a curated package before the agent even starts.

Each step encodes more retrieval judgment into the system and removes more from the agent. Each step is also premature if the pattern hasn't been validated through enough usage. We don't yet know which notes should have triggers, what retrieval profiles our work actually needs, or whether frontloading would help or waste tokens. ClawVault has the usage volume to discover these empirically; we're still building the KB that would be retrieved from. Worth revisiting once we have enough content and sessions to see recurring retrieval patterns.

## What We Should Not Borrow (Yet)

**LLM-heavy automation.** Their compression, fact extraction, and injection pipelines all run through LLMs. This adds capability but also opacity — you can't easily tell why something was promoted or what was lost in compression. We want to understand the fundamental patterns before automating them. The [verifiability gradient](../deploy-time-learning-the-missing-middle.md) matters here: automating a process before understanding it locks in assumptions.

**The 8 primitives taxonomy.** Goals, Agents, State Space, Feedback, Capital, Institution, Synthesis, Recursion — this is a framework that organises their features, but it's unclear whether these are fundamental categories or a retroactive grouping of what they happened to build. We'd rather discover our categories from practice.

**The specific scoring format.** Confidence and importance as floats (c=0.9, i=0.85) implies a precision that LLM extraction can't actually deliver. The buckets (structural/potential/contextual) are more honest than the numbers. If we adopt anything here, it should be the buckets, not the scores.

## Key Divergences

**Frontloaded context vs. agent-driven retrieval.** ClawVault pre-assembles context before the agent starts work. Their `context` command gathers from 5 sources (daily notes, observations, search results, graph neighbors, structural observations), scores and deduplicates them, caps per source by profile, fits a token budget, and injects the result into the prompt. A hook fires on `session:start` and auto-injects up to 4 results. The agent gets a curated package.

Our [context-loading-strategy](../../claw-design/context-loading-strategy.md) takes the opposite approach: load CLAUDE.md (routing table + conventions) at startup, then trust the agent to navigate. Progressive disclosure — descriptions first, full content on demand. The agent reads, decides what's relevant, follows links.

The trade-offs are real. Frontloading means the agent starts with relevant context immediately, no wasted turns — good for weaker models or constrained tool access. But the system must guess what's relevant *before knowing what the agent will need*, and tokens spent on pre-loaded context are tokens unavailable for the task. Agent-driven retrieval loads exactly what's needed when needed and scales better (the KB can grow without ballooning startup context), but depends on the agent being good at navigation and costs turns on retrieval.

These aren't mutually exclusive. You could frontload a minimal context (as we already do with CLAUDE.md) and leave the agent to retrieve the rest. But the deeper question is whether frontloading is a fundamental pattern or a workaround for agents that can't navigate well. Both frontloading and the component patterns it's built from (triggers, profiles) can be viewed as retrieval crystallisation — see "What We Could Borrow" item 5.

**They automated the workshop; we're still mapping it.** ClawVault has 40+ commands and a full pipeline from session transcript to vault knowledge. We're still figuring out what the workshop layer should contain. This is a legitimate strategic difference — [our claw-design notes](../../claw-design/a-functioning-claw-needs-a-workshop-layer-not-just-a-library.md) argue the workshop needs state machines, dependencies, and expiration, but we haven't committed to specific artifact types. ClawVault's choices (observations, handoffs, reflections) are one answer.

**Human-in-the-loop vs. agent-driven.** Their promotion pipeline is largely automated — LLMs extract, score, and route observations. Our model keeps humans in the promotion loop (text → seedling → note requires human judgment). This reflects different bets on whether LLM judgment is reliable enough for knowledge curation. We're more conservative, but their system generates evidence about whether the automated approach works.

**No learning theory.** Like [Thalo](./thalo.md), ClawVault has no framework for deciding when to formalise something vs. leave it fluid. No [verifiability gradient](../deploy-time-learning-the-missing-middle.md), no stabilise/soften boundary. Their observation format was designed; it doesn't evolve based on what the system learns about its own learning. This is the gap between building a knowledge system and understanding knowledge systems.

## What to Watch

- Does promotion by recurrence actually surface the right things? Their system has enough usage to generate evidence.
- How do handoff documents evolve over time — do they converge on a stable structure, or do they stay heterogeneous?
- Does the observation type taxonomy (decision, lesson, preference, commitment) hold up, or do new types emerge that break the categories?
- How does the system handle contradictory observations (high-confidence entries that conflict)?

---

Relevant Notes:
- [a-functioning-claw-needs-a-workshop-layer](../../claw-design/a-functioning-claw-needs-a-workshop-layer-not-just-a-library.md) — foundation: ClawVault's observations, handoffs, and reflections are concrete workshop artifacts where we have only the theoretical need
- [claw-learning-is-broader-than-retrieval](../../claw-design/claw-learning-is-broader-than-retrieval.md) — foundation: ClawVault's observation types (decision, preference, lesson) are concrete implementations of the action-oriented knowledge types this note identifies as missing
- [automating-kb-learning-is-an-open-problem](../../claw-design/automating-kb-learning-is-an-open-problem.md) — extends: ClawVault's reflection pipeline is a working (if LLM-heavy) implementation of the boiling cauldron mutations
- [deploy-time-learning](../deploy-time-learning-the-missing-middle.md) — contrasts: ClawVault automates promotion without a theory of when automation is premature; their results would test whether early automation helps or locks in assumptions
- [context-loading-strategy](../../claw-design/context-loading-strategy.md) — contrasts: ClawVault frontloads context via profiles and injection; we use progressive disclosure with agent-driven retrieval — different bets on whether the system or the agent should decide what's relevant
- [Thalo](./thalo.md) — sibling: both are compared against our theoretical position; Thalo formalised types (compiler), ClawVault formalised lifecycle (pipeline), we're formalising understanding (theory)

Topics:
- [related-systems](./related-systems-index.md)
